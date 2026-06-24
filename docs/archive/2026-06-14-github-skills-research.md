# GitHub Game Development Skills And Repos

更新时间：2026-06-14

## 结论

GitHub 上已经有不少和 game development 相关的 agent skills、Godot skills、项目模板和资源仓库。对当前 Godot + Codex + 2D 工作流，最有价值的不是“全装”，而是按用途拆开吸收：

- Godot 代码/测试工作流：优先参考 `fernforestgames/agent-skill-godot`、`abagames/headless-godot-skill-kit`。
- Godot 领域知识库：选择性参考 `thedivergentai/gd-agentic-skills` 或 `jame581/GodotPrompter`，不要一次装全部技能。
- 游戏设计流程：参考 `Donchitos/Claude-Code-Game-Studios` 的文档模板、QA gate、studio role 划分，但不要照搬 49 agents/70+ skills 的重型组织。
- Godot 项目模板：参考 `sempitern0/indie-blueprint`。
- 资源索引：参考 `ellisonleao/magictools` 和 `Calinou/awesome-gamedev`。
- 非 Godot 的 skill repo：`indiesoftby/defold-agent-config` 值得学习它的 `AGENTS.md + .agents/skills + dependency context` 结构。

## 推荐 Skill 仓库

| 仓库 | 类型 | 适合吸收的部分 | 注意事项 |
| --- | --- | --- | --- |
| `fernforestgames/agent-skill-godot` | Godot/GDScript agent skill | GDScript 修改前查文档、Godot CLI import、语法检查、GUT 测试、编辑器 MCP 截图/UI 验证流程 | 很适合作为我们 `godot-2d-agent-template` 的下一版参考 |
| `abagames/headless-godot-skill-kit` | Headless Godot skill kit | 不开编辑器也能 scene edit、test、export；强调 patch -> smoke run -> logic tests -> Web export 的完整流水线 | 适合无人值守方向；采用前先用小项目验证脚本兼容 Windows |
| `haxqer/godot-skill` | Codex-compatible Godot skill | 面向 Codex-compatible agents 的 inspect/edit/run/debug 工作流 | 规模较小，适合抽取思路，不直接依赖 |
| `thedivergentai/gd-agentic-skills` | Godot 4.5+ 高密度技能库 | `godot-master` orchestrator、micro-skills、project foundations、resource data patterns、genre blueprints | 明确提示不要 “install all”；一次装太多会造成 token flood 和指令冲突 |
| `jame581/GodotPrompter` | Godot 4.x agentic skills framework | Godot domain-specific skills，覆盖 GDScript/C# 项目 | 可作为 Godot skill 分类参考 |
| `Donchitos/Claude-Code-Game-Studios` | 大型 Claude Code 游戏工作室模板 | 设计、编程、美术、音频、叙事、QA、release 的角色和模板；GDD、ADR、HUD design、accessibility 等模板 | 过重，不建议照搬；适合拆出文档模板和 QA gate |
| `rhino-ty/game-architect` | Indie game design skill | 系统机制、数值平衡、GDD、叙事、音频、营销、post-launch ops | 小仓库，适合设计流程灵感 |
| `threeaus/schell-game-design` | 早期游戏规划 skill | 用 Jesse Schell lens 压测游戏想法 | 适合 idea 阶段，不适合直接工程实现 |
| `Aetik-yue/godot-indie-dev` | Godot + Aseprite solo indie skill | MVP planning、GDScript、pixel art、rapid iteration | 和当前目标很接近，可进一步细读 |
| `indiesoftby/defold-agent-config` | Defold agent config/skills | `AGENTS.md`、`.agents/skills`、依赖上下文 `.deps`、多 agent 目录适配 | 虽然不是 Godot，但结构很值得借鉴 |

## 推荐 Repo / Resource 仓库

| 仓库 | 类型 | 适合用途 |
| --- | --- | --- |
| `godotengine/godot-demo-projects` | 官方 Godot demo | 学最小可运行样例、2D/GUI/audio/viewport 的项目拆分方式 |
| `sempitern0/indie-blueprint` | Godot indie project template | 参考项目模板、基础设置、indie game common systems |
| `ellisonleao/magictools` | Game development resources list | 查工具、教程、框架、素材、学习资源 |
| `Calinou/awesome-gamedev` | Free software/culture gamedev resources | 查开源工具、免费素材、学习资源 |
| GitHub `game-engines` collection | Game engine collection | 横向了解 Godot、Turbulenz、Torque3D 等 engine 生态 |
| `bitwes/Gut` | Godot GDScript unit testing | 当前 Godot 2D 项目最实用的单测入口之一 |
| `godot-gdunit-labs/gdUnit4` | Godot 4 testing framework | 更系统的 Godot 4 单测、mock、scene testing |
| `godot-gdunit-labs/gdUnit4-action` | GitHub Action for Godot tests | PR/push 自动跑 Godot tests，上传测试报告 |
| `chickensoft-games/GodotTestDriver` | Godot integration testing | simulated input、node drivers、fixtures，适合真实玩家路径测试 |
| `abarichello/godot-ci` | Godot Docker CI/export | 自动 export、GitHub/GitLab/Itch.io 发布链路 |
| `firebelley/godot-export` | Godot export GitHub Action | 自动导出标准/Mono Godot 构建 |

## 对当前工作流的采用建议

### 1. 不要先装大而全的系统

`Claude-Code-Game-Studios`、`gd-agentic-skills` 这类仓库价值很高，但直接全量导入会带来三个问题：

- prompt/token 被大量技能描述占用；
- 多个相近技能会互相冲突；
- 你的项目还没有足够多的自动验证来约束它们。

建议先抽取规则和模板，而不是直接安装全套。

### 2. 先增强现有模板

当前已有：

- `game-development/godot-codex-2d-game-learning.md`
- `game-development/godot-2d-agent-template/AGENTS.md`

下一步可以从 `fernforestgames/agent-skill-godot` 和 `headless-godot-skill-kit` 吸收这些规则：

- 新增文件后跑 `godot --headless --import`。
- GDScript 修改后跑 syntax/typecheck 脚本。
- 视觉 UI 改动后：启动 scene -> 截图 -> inspect node tree -> 合成输入 -> 再截图。
- 每次改变后固定流水线：patch -> headless smoke -> logic tests -> screenshot/manifest。

### 3. 为当前目标创建 3 个本地轻量 skill

比安装一个大 skill 更稳：

1. `godot-2d-implementation`
   - Godot 2D scene/script/data 修改流程
   - headless/import/test/screenshot 验证

2. `godot-2d-art-pipeline`
   - Aseprite spec、palette、layer、tag、export/import
   - AI 候选图如何进入 source asset

3. `game-design-audit`
   - GDD、core loop、combat/economy/UI/art direction
   - 用 checklist 压测玩法，不直接写代码

### 4. Repo 借鉴优先级

按当前 Godot 2D + Codex 目标：

1. `fernforestgames/agent-skill-godot`
2. `abagames/headless-godot-skill-kit`
3. `bitwes/Gut` 或 `godot-gdunit-labs/gdUnit4`
4. `godot-gdunit-labs/gdUnit4-action`
5. `sempitern0/indie-blueprint`
6. `thedivergentai/gd-agentic-skills`
7. `Donchitos/Claude-Code-Game-Studios`
8. `ellisonleao/magictools`
9. `Calinou/awesome-gamedev`

## 可执行下一步

建议下一轮直接做这件事：

```text
基于 GitHub 调研结果，创建一个 repo-local skill：
game-development/skills/godot-2d-implementation/SKILL.md

要求：
- 适配 Codex
- 专注 Godot 4 2D
- 包含 scene/script/data 修改流程
- 包含 Aseprite asset pipeline 接口
- 包含 headless/import/GUT-or-gdUnit4/screenshot manifest 验证
- 不引入大型多 agent 体系
```

## 来源

- https://github.com/fernforestgames/agent-skill-godot
- https://github.com/abagames/headless-godot-skill-kit
- https://github.com/haxqer/godot-skill
- https://github.com/thedivergentai/gd-agentic-skills
- https://github.com/jame581/GodotPrompter
- https://github.com/Donchitos/Claude-Code-Game-Studios
- https://github.com/rhino-ty/game-architect
- https://github.com/threeaus/schell-game-design
- https://github.com/Aetik-yue/godot-indie-dev
- https://github.com/indiesoftby/defold-agent-config
- https://github.com/godotengine/godot-demo-projects
- https://github.com/sempitern0/indie-blueprint
- https://github.com/ellisonleao/magictools
- https://github.com/Calinou/awesome-gamedev
- https://github.com/collections/game-engines
- https://github.com/bitwes/Gut
- https://github.com/godot-gdunit-labs/gdUnit4
- https://github.com/godot-gdunit-labs/gdUnit4-action
- https://github.com/chickensoft-games/GodotTestDriver
- https://github.com/abarichello/godot-ci
- https://github.com/firebelley/godot-export

