# Godot + Codex 2D 游戏开发学习与自动化手册

更新时间：2026-06-14

## 目标

这份文档面向一个现实目标：用 Godot 做 2D 游戏，用 Codex 持续推进工程、玩法、UI、角色和验证流程，同时承认 AI 在美术上的边界，把“随机生成到满意”为主的流程，改造成“规格约束 + 自动导入 + 固定基线 + 可回放评审”的流程。

结论先放前面：

- 代码、系统、数据表、Godot 场景结构，Codex 可以高效推进。
- UI 和角色不能只靠“一句提示词生成最终图”。更稳的做法是先定义规格、层级、调色板、动画标签、游戏距离下的可读性标准，再让 AI 只生成候选，最终由 Aseprite 结构化导入和修正。
- 想尽量无人干预，关键不是让 AI 审美“自动正确”，而是把验收条件变成截图、manifest、seed、基线对比、UI 溢出检查、启动检查、release checklist。
- 对 2D 小团队项目，最佳路径是：Godot 负责系统和可验证运行时，Aseprite 负责像素资产源文件，Codex 负责工程执行、脚本化管线、截图回归和文档化决策。

## 当前本地经验

工作区里已有几个有用样本：

- `workingcopy/brotato-like/game`：最接近目标。已有 Godot 4.6、GDScript、autoload、数据驱动 JSON、DevPanel、automation screenshots、seed、baseline manifest、headless validation。
- `workingcopy/aseprite-demo`：已有 Aseprite CLI + Lua + JSON spec 的角色资产流程，包含 `wizard.json`、模板创建、导出、导入 AI sheet、retime、palette fix。
- `workingcopy/godot-2d-space-game`：可参考 2D 场景组织和游戏世界初始化。
- `workingcopy/tower-defense-godot4`：可参考 UI 场景和传统塔防结构。
- `workingcopy/godot-2d-agent-template/AGENTS.md`：新项目可复制的 Codex/Godot 2D 项目规则模板。
- `workingcopy/game-development/gd-game-skill-redesign.md`：GitHub game development skill 调研后的有限吸收总结和本地 skill 重构说明。
- `workingcopy/game-development/skills/godot-2d-game-development/SKILL.md`：重新整理后的 Godot 4 2D game development 本地 skill。

其中 `brotato-like` 最值得沉淀成通用模式：视觉变化必须看截图，玩法变化必须有固定 seed，Codex 任务必须跑 headless 和相关 automation，不把“代码看起来对”当作完成。

## 核心工程原则

### Godot 2D 架构

推荐结构：

```text
game/
  project.godot
  scenes/
    main/
    player/
    enemy/
    combat/
    ui/
    effects/
  scripts/
    autoload/
    main/
    player/
    enemy/
    combat/
    ui/
    effects/
  data/
    gameplay.json
    enemies.json
    weapons.json
    waves.json
    feedback_baselines.json
  assets/
    characters/
    ui/
    vfx/
  themes/
  docs/
  screenshot/
    automation/
```

实践要点：

- 场景是主要组合单位，脚本服务场景，而不是把所有逻辑塞进一个巨型脚本。
- 每个重要实体尽量有 scene + script 对：例如 `Player.tscn` + `PlayerController.gd`，`ShopPanel.tscn` + `ShopPanel.gd`。
- 共享状态只放必要 autoload：`GameManager`、`DataRepository`、`SettingsService`、`AudioService`、`AutomationService`、`RngService`。不要把所有东西都全局化。
- 玩法数值优先放 JSON 或 Resource，Codex 改数值时优先改数据，不硬编码。
- UI 用 Godot `Control`、Container、Theme，不用纯坐标堆。能用主题和样式变体解决的，不在每个按钮上重复写。
- 像素图导入后要检查 texture filter、repeat、mipmap、压缩；像素风首要目标是清晰，不是默认平滑。

### 2D 动画选择

简单角色：

- `AnimatedSprite2D` + `SpriteFrames`。
- 适合 run/attack/hurt/death 这种帧动画。
- Aseprite 导出的 sheet + JSON 可以映射到 SpriteFrames。

复杂表现：

- `AnimationPlayer` 驱动非帧图属性，例如 weapon swing、hit flash、hurt offset、UI tween、粒子触发。
- 不要把所有视觉反馈画进角色帧。命中、暴击、受击闪、伤害数字、屏幕震动应该是独立 VFX 层。

大量背景或循环小动画：

- 考虑 TileMap/TileSet 或更少节点，避免每个草、火花、装饰物都变成独立高频节点。

## Aseprite 资产管线

不要把 AI 生成的 PNG 当源文件。源文件应该是 `.aseprite`，AI 产物只是候选输入。

推荐最小角色规格：

```json
{
  "character": "wizard",
  "canvas": { "w": 64, "h": 64 },
  "origin": { "x": 32, "y": 52 },
  "palette": "fixed-32",
  "animations": {
    "run": { "frames": 8, "fps": 12, "loop": true },
    "attack": { "frames": 6, "fps": 10, "loop": false },
    "hurt": { "frames": 3, "fps": 8, "loop": false },
    "death": { "frames": 8, "fps": 8, "loop": false }
  },
  "layers": ["shadow", "body", "head", "weapon", "fx"]
}
```

推荐流程：

1. 写 `specs/character.json`：尺寸、origin、动画标签、帧数、FPS、层名、调色板、剪影要求。
2. 用 Lua 创建 `.aseprite` 模板：先有正确帧数、tag、layer，再填图。
3. 用 AI 生成粗略 sheet，导入到 `generated/`，不要直接进游戏。
4. 用脚本拆帧导入到对应 tag/layer。
5. 用 `fix_palette.lua` 固定调色板，用 `retime_tags.lua` 固定 timing。
6. 导出 `exports/character.png` + `exports/character.json`。
7. Godot 只读取导出物，永远不要把 AI 原图当最终 runtime 资产。

Aseprite CLI 的关键能力：

```powershell
& "D:\Program Files (x86)\Steam\steamapps\common\Aseprite\Aseprite.exe" -b character.aseprite --sheet character.png --data character.json
```

常用扩展：

- `--split-layers`：把层信息导入 JSON，适合检查 AI 是否污染层级。
- `--list-tags`：导出动画标签，适合 Godot importer 校验。
- `--sheet-pack`：多个角色或 UI 小图合成 atlas。

## AI 美术的边界与解决办法

### 角色难点

AI 常见失败：

- 同一角色不同帧脸、比例、武器、服装细节漂移。
- 角色 idle/run/attack 的重心不一致。
- 游戏内缩小后剪影不清楚。
- 动作好看但命中时机不匹配。
- 帧间像素抖动导致动画脏。

解决策略：

- 先做“剪影锁定”：单帧黑白 silhouette 在 64x64 和 32x32 下仍要认得出。
- 角色拆成层：shadow/body/head/weapon/fx，允许 AI 只补某层。
- 固定 palette，不让每次生成重新发明颜色。
- 只让 AI 生成候选帧，不让它决定帧数、origin、tag、碰撞盒。
- 用 Aseprite 手工或脚本做最后清理：统一轮廓、清 stray pixels、重建关键帧。

### UI 难点

AI 生成 UI 图很难直接可用，因为 UI 需要布局、状态、文字、响应式、输入焦点、主题一致性。

推荐做法：

- UI 不走图像生成主线，走 Godot Control + Theme。
- AI 可以生成 moodboard、icon 候选、装饰边框，但按钮、列表、商店卡、HUD 必须是可布局控件。
- Codex 生成 UI 时要给明确目标：分辨率、最长文本、键鼠/手柄焦点、低血/商店/暂停状态。
- 每次 UI 改动都用截图验证，而不是只看 `.tscn` diff。

UI 验收标准：

- 1280x720、1920x1080、窗口缩放下不溢出。
- 中英文或长数字不遮挡。
- 手柄焦点路径明确。
- 战斗 HUD 在混战截图里仍可读。
- 商店、升级、暂停、Game Over 每个状态有 screenshot baseline。

## Codex 工作流

### 单次任务提示词模板

```text
目标：
在 Godot 4 2D 项目中改进 [系统/角色/UI/VFX]。

上下文：
- 相关场景：
- 相关脚本：
- 相关数据：
- 当前问题截图或 automation label：

约束：
- 保持现有 scenes/scripts/data 分层。
- 数值优先改 data。
- UI 使用 Control/Theme/Container。
- 视觉改动必须跑截图 automation。
- 不重构无关文件。

完成条件：
- Godot headless 启动通过。
- 对应 automation scenario 通过。
- 输出截图/manifest 可用于评审。
- 说明改动影响 gameplay timing 还是 presentation-only。
```

### repo 级 `AGENTS.md`

每个 Godot 项目都应有 `AGENTS.md`，至少写：

- Godot 可执行路径。
- headless 检查命令。
- automation scenario 命令。
- 项目目录结构。
- GDScript 风格：tab、typed parameters、scene/script 配对。
- UI 验收标准。
- 视觉变化必须截图。
- 哪些文件不能乱改，例如导入文件、build 输出、`.godot/`。

`brotato-like/game/AGENTS.md` 已经是一个好样本，可以抽出通用模板。

### Codex 自动化能力边界

适合 Codex 自动做：

- 读项目结构、补 `AGENTS.md`、补 README。
- 根据现有模式新增 Godot scene/script/data。
- 写 Aseprite Lua 导入导出脚本。
- 写 Godot automation runner、seed、manifest、screenshot baseline。
- 跑 headless、整理日志、定位 parse/runtime 错误。
- 做 PR 风格代码 review。
- 在 CI 或本地 `codex exec` 中生成报告、尝试修复失败。

不适合完全交给 Codex 无约束做：

- 最终角色审美判断。
- 品牌风格选择。
- “这张图好不好看”的纯主观判断。
- 未定义验收标准的 UI 重设计。
- 无 seed 的手感平衡。

最佳实践是把主观判断前置成客观准则：可读性、占屏尺寸、对比度、状态数量、动画帧数、baseline 截图、失败条件。

## 无人干预优化循环

目标不是“一次生成满意”，而是让 Codex 可以持续跑循环。

### 循环 1：工程健康

触发：每次脚本、场景、数据变化后。

命令：

```powershell
C:/opt/godot/Godot_v4.6.1-stable_win64_console.exe --path "C:/Users/beria/workingcopy/brotato-like/game" --headless --quit
```

产物：

- exit code
- Godot output
- 最近日志

Codex 判断：

- parse error、missing preload、bad resource path 直接修。
- warning 记录到 tech debt，不阻塞除非影响运行。

### 循环 2：视觉基线

触发：角色、敌人、VFX、HUD、UI 改动后。

命令：

```powershell
C:/opt/godot/Godot_v4.6.1-stable_win64_console.exe --path "C:/Users/beria/workingcopy/brotato-like/game" -- --automation scenario=feedback_baselines auto_quit=true
```

产物：

- `screenshot/automation/*.png`
- per-capture manifest
- `run_*.json`

Codex 判断：

- 缺 label、缺 expected event、smoke failed：自动修。
- manifest 标记 timing_sensitive：需要更严格说明。
- presentation_only：可自动继续迭代，但仍保留截图。

### 循环 3：Aseprite 资产重建

触发：角色或 UI icon 资产候选更新后。

步骤：

1. 导入 AI 候选。
2. 检查 canvas、frame count、tag、layer、origin。
3. 固定 palette。
4. 导出 sheet/json。
5. Godot importer 或脚本生成 SpriteFrames。
6. 跑角色 showcase 截图。

Codex 可自动失败判定：

- 文件不存在。
- tag 缺失。
- 帧数不符。
- JSON 无 frame tags。
- 导出尺寸错误。
- palette 超过上限。
- Godot runtime 找不到资源。

Codex 不应自动判定：

- 角色是否“足够有魅力”。
- 风格是否最终满意。

解决方式：你先批准一版 baseline，之后 Codex 只做“不低于 baseline”的检查。

### 循环 4：玩法平衡

触发：武器、敌人、wave、shop、level-up 改动后。

最小指标：

- 固定 seed 下 1 分钟内敌人数量曲线。
- 玩家受击次数。
- 平均击杀时间。
- 升级次数。
- 商店购买力。
- boss 预警是否出现。

这些指标写进 `run_*.json`，Codex 就能自动比较新旧结果。

## GitHub 调研补充：设计文档与开发测试

这次补充搜索了 GitHub 上和 Godot、2D 游戏、GDD、unit testing、scene testing、CI/export 相关的公开仓库。筛选标准不是 star 数最高，而是能直接转成当前 Godot + Codex 流程里的规则。

### 可借鉴仓库

| 仓库 | 用途 | 可吸收的做法 |
| --- | --- | --- |
| `godotengine/godot-demo-projects` | 官方 Godot demo 集合 | 把 2D、GUI、audio、viewport 等按独立 project 拆分。适合 Codex 学习“一个机制一个最小可运行样例”的方式。 |
| `bitwes/Gut` | GDScript 单元测试框架 | 适合测试数据表、伤害公式、掉落规则、商店刷新、RNG helper 等纯逻辑。支持 CLI 和 JUnit XML 输出，适合接 CI。 |
| `godot-gdunit-labs/gdUnit4` | Godot 4 测试框架 | 支持 GDScript/C#、assertion、mocking、scene testing。适合更系统地测 scene 和 autoload。 |
| `godot-gdunit-labs/gdUnit4-action` | GitHub Actions 测试动作 | 可在 PR/push 时跑 Godot 4 tests，配置 Godot 版本、test path、timeout、report artifact。 |
| `chickensoft-games/GoDotTest` | Godot C# 测试运行器 | C# 项目可用；支持命令行测试、coverage、debug。它明确强调视觉/集成测试不并行，避免 race condition。 |
| `chickensoft-games/GodotTestDriver` | Godot 集成测试 | 用 simulated input、node drivers、fixtures 测更接近真实玩家路径的交互。 |
| `graydwarf/godot-ui-automation` | Godot UI 自动化 | 方向上适合 UI 录制、回放、验证；采用前需要小样本验证维护成本。 |
| `zwx1127/gdx` | Godot AI automation CLI | 方向上接近“AI agent 控 Godot、截图、测试、导出”；适合作为思路参考，不建议直接依赖前先验证稳定性。 |
| `abarichello/godot-ci` | Godot Docker CI/export | 适合构建 GitHub Actions/GitLab CI/Itch.io 发布链路。 |
| `firebelley/godot-export` | Godot GitHub Action export | 适合自动导出标准和 Mono 构建。 |
| `2D-MMORPG/gdd` | 2D GDD 示例 | GDD 放在仓库里，配图片和 `GDD.md`。适合说明设计文档应与实现版本同步。 |
| `Glade-tool/glade-mcp` | AI + Unity/Godot 编辑器上下文 | 借鉴“项目上下文文件 + 编辑器桥 + runtime observation”的方向。Codex 侧可用 `AGENTS.md`、GDD、automation manifest 承担同类上下文。 |

### 推荐测试分层

把 Godot 游戏测试拆成 6 层，Codex 每次按改动风险选择对应层，不要把所有问题都塞进人工游玩。

1. 启动检查  
   目标：项目能加载，资源路径、autoload、scene preload 不炸。  
   命令：`godot --path game --headless --quit`。  
   适用：所有脚本、场景、资源改动。

2. 纯逻辑单元测试  
   工具：GUT 或 gdUnit4。  
   目标：测试不依赖画面和真实时间的逻辑，例如伤害公式、经验曲线、商店刷新、掉落、词条组合、RNG 固定 seed。  
   Codex 做法：新增系统时同步新增 `tests/`，CI 里输出 JUnit XML。

3. scene/autoload 测试  
   工具：gdUnit4 scene testing，或轻量自写 Godot test runner。  
   目标：实例化 scene，确认节点存在、信号连接、autoload 状态切换、UI panel 打开关闭。  
   适用：HUD、shop、level-up、pause、enemy scene、projectile scene。

4. 集成测试和输入路径  
   工具：GodotTestDriver 或自写 automation scenario。  
   目标：模拟开始游戏、移动、攻击、拾取、打开商店、购买、进入下一波、死亡/胜利。  
   注意：视觉/集成测试尽量串行，避免 race condition 和非确定性时序。

5. 视觉回归  
   工具：当前 `AutomationService` 的 screenshot + manifest，必要时吸收 UI automation 思路。  
   目标：固定 seed、固定 camera、固定 label，输出 PNG 和 JSON，检查 HUD、敌人、VFX、角色剪影、商店卡片。  
   Codex 做法：只自动判断“缺失、溢出、事件不一致、label 不全”；审美升级需要人先批准 baseline。

6. CI/export/release gate  
   工具：gdUnit4-action、godot-ci、godot-export。  
   目标：push/PR 时跑测试；tag/release 时导出 Windows/Web/Linux 或 itch.io 包。  
   Codex 做法：CI 不直接持有宽权限修代码，先产出 patch/report，再由单独步骤创建 PR。

### GDD 应该如何服务 Codex

从 GitHub 上的 GDD 仓库和 AI/Godot 工具可以抽出一个原则：GDD 不应该是一次性大文档，而应该是仓库里的活上下文。

推荐拆法：

```text
docs/design/
  GDD.md
  core_loop.md
  combat_rules.md
  economy.md
  enemies.md
  weapons.md
  ui_ux.md
  art_direction.md
  audio.md
  accessibility.md
  test_matrix.md
```

每个文件写 Codex 可执行的信息：

- `core_loop.md`：单局结构、玩家每 10 秒该做什么、失败条件、胜利条件。
- `combat_rules.md`：伤害、无敌帧、击退、命中优先级、子弹生命周期。
- `economy.md`：掉落、经验、商店、刷新、锁定、价格曲线。
- `enemies.md`：敌人职责，不只写名字；要写“给玩家制造什么决策”。
- `weapons.md`：武器家族、攻击节奏、升级方向、build tag。
- `ui_ux.md`：HUD 信息优先级、面板状态、最长文本、手柄焦点。
- `art_direction.md`：palette、角色尺寸、剪影规则、VFX 层级、禁止漂移项。
- `test_matrix.md`：每个系统对应哪些 GUT/gdUnit4/automation screenshot/手动 QA。

Codex 任务应先读对应 GDD 小文件，再改 scene/script/data。这样“设计”和“实现”不会变成两条线。

### 采用顺序

对当前工作区，建议按这个顺序吸收 GitHub 调研结果：

1. 先维持现有 `headless + AutomationService screenshot/manifest`，这是最贴近当前项目的测试资产。
2. 给纯逻辑加 GUT 或 gdUnit4：从 `DataRepository`、RNG、shop、damage、wave rules 开始。
3. 给 UI 和 scene 加 scene tests：先测 panel 存在、信号、状态切换，不先追求像素级自动评审。
4. 增加 GitHub Actions：先跑 headless 和 test suite，再上传 screenshot/manifest artifact。
5. release 阶段再接 `godot-ci` 或 `godot-export`，不要太早把导出流水线复杂化。
6. 最后评估 UI automation / GodotTestDriver / gdx 这类更强工具，只在现有 automation 不够用时引入。

## 推荐的下一批工程任务

按优先级：

1. 为当前 Godot 项目建立 `docs/design/`，先补 `GDD.md`、`core_loop.md`、`test_matrix.md`。
2. 选择 GUT 或 gdUnit4，给 `DataRepository`、RNG、shop、damage、wave rules 加第一批纯逻辑测试。
3. 给 `feedback_baselines.json` 增加 UI 专项：main_menu、hud_combat、shop、level_up、pause、game_over。
4. 写一个 screenshot manifest diff 脚本：比较 label、seed、camera_zoom、event、timing_sensitive。
5. 增加 GitHub Actions：headless 启动 + Godot tests + 上传 screenshot/manifest artifact。
6. 给 Aseprite demo 增加 Godot importer：读取 Aseprite JSON，自动生成 `SpriteFrames` 或 `.tres`。
7. 写一个 Codex noninteractive prompt：每天或每次改动后跑“健康检查 + 报告 + 小修复建议”。
8. 给每个角色建立 art spec：canvas、origin、palette、layers、tags、silhouette notes、forbidden drift。
9. 给 UI 建立 Theme token 文档：字体、字号、panel style、rarity colors、focus ring、danger/warn/success。
10. 将 AI 生成资产目录加 `.gdignore`，防止 Godot 导入大量候选垃圾。

## 可复用 Codex 自动检查 Prompt

```text
你在 Godot 4 2D 项目中执行无人值守健康检查。

请完成：
1. 读取 AGENTS.md 和 README.md。
2. 运行 headless 启动检查。
3. 如果有视觉/玩法变更，运行相关 automation scenario。
4. 读取最新 run_*.json manifest。
5. 判断失败是否来自 parse/runtime/resource/manifest 缺失。
6. 可以自动修复确定性问题；不要重做主观美术。
7. 输出：
   - 通过/失败
   - 修复了什么
   - 哪些需要人工审美确认
   - 下次应该固化进 AGENTS.md 的规则
```

## 资料来源

- Godot 2D documentation: https://docs.godotengine.org/en/stable/tutorials/2d/index.html
- Godot 2D sprite animation: https://docs.godotengine.org/en/stable/tutorials/2d/2d_sprite_animation.html
- Godot image importing: https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_images.html
- Godot UI documentation: https://docs.godotengine.org/en/stable/tutorials/ui/index.html
- Godot best practices, scene organization: https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html
- Godot best practices, project organization: https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html
- Godot best practices, autoloads: https://docs.godotengine.org/en/stable/tutorials/best_practices/autoloads_versus_internal_nodes.html
- Aseprite CLI docs: https://www.aseprite.org/docs/cli/
- OpenAI Codex manual: https://developers.openai.com/codex/codex-manual.md
- GitHub, Godot demo projects: https://github.com/godotengine/godot-demo-projects
- GitHub, GUT: https://github.com/bitwes/Gut
- GitHub, gdUnit4: https://github.com/godot-gdunit-labs/gdUnit4
- GitHub, gdUnit4-action: https://github.com/godot-gdunit-labs/gdUnit4-action
- GitHub, GoDotTest: https://github.com/chickensoft-games/GoDotTest
- GitHub, GodotTestDriver: https://github.com/chickensoft-games/GodotTestDriver
- GitHub, godot-ci: https://github.com/abarichello/godot-ci
- GitHub, godot-export: https://github.com/firebelley/godot-export
- GitHub, 2D-MMORPG GDD example: https://github.com/2D-MMORPG/gdd
- GitHub, Glade MCP Godot context/tools: https://github.com/Glade-tool/glade-mcp
