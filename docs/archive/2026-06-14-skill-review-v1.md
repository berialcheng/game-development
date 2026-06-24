# Godot 2D Game Development Skill Review

更新时间：2026-06-14

## 总体判断

当前 `godot-2d-game-development` skill 的方向是对的：它避免了全量照搬大型 game studio / micro-skill 仓库，也把 Godot 2D、Aseprite、测试、GDD 分成了可延迟加载的 reference。

但它现在更像“安全守则”，还不够像“游戏开发执行系统”。最大问题不是写得少，而是缺少能约束实际产出质量的中间层：效果预算、玩法感受验收、VFX/SFX 管线、截图基线准入、失败处理、任务分流和项目级落地模板。

## 高优先级问题

### 1. 缺少效果管理层，容易做出“能跑但没手感”的游戏

证据：

- `SKILL.md` 只把任务分为 gameplay/UI/asset/design/automation，缺少 VFX、SFX、camera、hit feedback、juice、performance budget 这些游戏体验层。
- `implementation.md` 只覆盖 scene/script/UI/data，没有效果生命周期、命名、资源预算、层级和性能规则。
- `validation-layers.md` 有截图/manifest，但没有“效果是否可读、是否遮挡、是否过量、是否在低端帧率下仍稳定”的检查。

建议：

- 新增 `references/effects-management.md`。
- 把 effects 作为独立任务类型加入 `SKILL.md` workflow，而不是塞进 asset 或 UI。
- 明确效果管理至少覆盖：
  - hit flash / damage number / knockback / screen shake / pause-frame
  - particles / trails / decals / impact sprites / shader flashes
  - audio cue / music transition / mix priority
  - camera zoom/shake/follow smoothing
  - z-index、visibility、combat readability
  - instance pooling、lifetime cleanup、spawn rate cap

建议写入的规则：

```text
For effect-heavy changes, define the player-facing intent first: what should be noticed, when, for how long, and what must not be obscured.
Validate with a deterministic combat screenshot or short capture manifest, not only headless startup.
```

### 2. Done Criteria 太宽，`when possible` 会让 Codex 自动降级

证据：

- `SKILL.md` 的验证部分写了“when the project supports it”。
- `Done Criteria` 中 gameplay change 允许 “focused manual gap is documented”，这对早期可以，但长期会让 skill 变成“没有测试也算完成”。
- `validation-layers.md` 写了测试层级，但没有定义不同改动的最低验证门槛。

建议：

- 增加一个 `Minimum Verification Matrix`，把改动类型映射到最低检查。
- 如果项目没有对应工具，Codex 应该做两件事：跑现有最低命令，并记录“缺失的验证基础设施”，而不是直接算通过。

建议矩阵：

| 改动类型 | 最低验证 |
| --- | --- |
| GDScript/resource | headless startup |
| data/balance | schema/data load check + one deterministic fixture if tests exist |
| gameplay behavior | logic test or deterministic scenario |
| UI layout | screenshot for at least one target state |
| VFX/camera/audio feedback | deterministic combat showcase screenshot/manifest |
| Aseprite export | PNG/JSON existence + frame/tag validation + Godot import/load |
| CI/export | local equivalent command must pass before CI config |

### 3. 设计审查没有真正接到实现层

证据：

- `game-design-audit.md` 有很好的问题列表，但输出只有 summary、risks、schema implications、test implications、next slice。
- 没有要求把设计意图转成玩家可观察行为、数据字段、场景节点、验收截图。
- `SKILL.md` 让 Codex “read design doc before editing”，但没有要求发现设计缺口时停下来补设计约束。

建议：

- 在 `game-design-audit.md` 增加 `Design To Implementation Contract`。
- 每个设计决策必须落到：
  - player-facing outcome
  - system touched
  - data/resource touched
  - failure mode
  - validation artifact

示例：

```text
Design: elite enemy should feel dangerous but fair.
Outcome: visible windup before charge, clear impact zone, recover window after miss.
Systems: enemy state machine, hitbox, VFX telegraph, audio cue.
Validation: deterministic scenario screenshot at windup + impact; data test for cooldown.
```

### 4. Aseprite 管线还停在“导出正确”，没有到“游戏中正确”

证据：

- `aseprite-art-pipeline.md` 验证了 tag、frame、PNG dimensions、JSON metadata。
- 但没有要求 Godot import preset、nearest filtering、sprite pivot、一致缩放、hitbox/hurtbox 对齐、animation event timing。

建议：

- 把 Aseprite 管线分成 source validation 和 runtime validation。
- 增加这些检查：
  - texture filter 是否符合 pixel art，通常应是 nearest
  - pivot 是否和角色控制器、碰撞体一致
  - animation FPS 是否和 gameplay timing 一致
  - hurtbox/hitbox 或 weapon socket 是否对齐关键帧
  - directional animation 是否有命名约定
  - UI icon 和 world sprite 是否分开规格

### 5. 缺少“真实项目使用后的反馈回路”

证据：

- `gd-game-skill-redesign.md` 建议用真实 Godot 项目试一次小任务。
- 但 skill 本身没有规定什么时候把经验回写到 `AGENTS.md`、skill、design docs。

建议：

- 加一个 `Learning Loop` 段落：
  - 单项目特有规则进 `AGENTS.md`
  - 跨项目稳定规则进 skill reference
  - 玩法意图进 `docs/design/`
  - 验证命令进 `AGENTS.md` 或 CI
  - 重复失败必须变成规则或测试

## 中优先级问题

### 6. Skill 触发范围偏宽，可能抢走项目级 AGENTS 的职责

`description` 覆盖 gameplay、UI、scene、script、data、Aseprite、testing、screenshot、AGENTS.md，几乎所有 Godot 任务都会触发。触发宽不是坏事，但 body 需要更强地提醒“项目规则优先”。

建议：

- 在 `SKILL.md` 前 20 行加入明确优先级：
  1. user request
  2. repo `AGENTS.md`
  3. project docs/test matrix
  4. this skill
  5. external references

### 7. 缺少类型化任务模板

现在 Codex 需要自己把“改一个敌人”翻译成读取哪些文件、改哪些数据、跑哪些检查。skill 可以给更低自由度的模板。

建议新增 `references/task-templates.md`，包含：

- Add enemy
- Add weapon
- Tune economy
- Add HUD panel
- Add VFX feedback
- Import character animation
- Add screenshot scenario
- Add first GUT/gdUnit4 test

每个模板只写：

```text
Read:
Change:
Validate:
Report:
```

### 8. 缺少性能和内容规模预算

Godot 2D 小项目最常见的问题不是架构不够高级，而是粒子、敌人、掉落物、伤害数字、寻路、UI 更新同时爆炸。

建议在 effects 或 validation reference 中加入预算字段：

- max enemies on screen
- max particles per effect
- max simultaneous damage numbers
- max dropped items
- target FPS and resolution
- texture atlas / draw call concerns
- pooled vs one-shot effects

### 9. 没有区分 prototype、vertical slice、production

同一个规则在原型期和生产期强度不同。现在 skill 一律要求可验证，可能让早期探索变慢，也可能让后期质量门槛不够硬。

建议加入 phase mode：

- prototype：允许快速试，但要写 disposal note，不承诺长期架构。
- vertical slice：必须有 core loop、HUD、enemy/reward、one deterministic scenario。
- production：新增功能必须有测试、截图或 QA gate。

## 低优先级问题

### 10. 外部来源列表在 `SKILL.md` 中可能逐渐变成噪音

`SKILL.md` 直接列外部 repo 有帮助，但长期看这部分不是执行流程。更好的做法是保留 2-3 个高价值来源，其余留在 `selective-adoption.md`。

### 11. 缺少 sample prompt

可以加少量任务样例，让 Codex 更容易套用：

```text
Use $godot-2d-game-development to add a data-driven enemy with one deterministic combat screenshot.
Use $godot-2d-game-development to import an Aseprite character sheet and verify SpriteFrames.
Use $godot-2d-game-development to review a GDD slice and produce implementation/test implications.
```

## 我建议的下一版结构

保留一个主 skill，但扩展 references：

```text
godot-2d-game-development/
  SKILL.md
  references/
    implementation.md
    effects-management.md
    aseprite-art-pipeline.md
    validation-layers.md
    game-design-audit.md
    task-templates.md
    selective-adoption.md
```

`SKILL.md` 应该变得更短、更硬：

- 只放任务分流、优先级、最低验证门槛、done criteria。
- 具体玩法/UI/effects/art/test 模板放 reference。
- 外部 repo 只保留“参考，不依赖”的原则。

## 最值得马上改的 5 件事

1. 加 `effects-management.md`，把游戏反馈、VFX/SFX/camera、性能预算纳入 skill。
2. 在 `SKILL.md` 加 `Minimum Verification Matrix`，减少 `when possible` 的逃逸空间。
3. 在 `game-design-audit.md` 加 `Design To Implementation Contract`，把设计审查接到代码和验证。
4. 在 `aseprite-art-pipeline.md` 加 runtime validation：pivot、filter、scale、hitbox、animation timing。
5. 加 `task-templates.md`，让 Codex 面对常见 Godot 任务时不需要临场重新发明流程。

## 不建议现在做的事

- 不建议把 `Claude-Code-Game-Studios` 的角色体系搬进来。
- 不建议把 `gd-agentic-skills` 全部拆进本地 references。
- 不建议先写复杂 CI/export。先把本地 headless、logic test、screenshot manifest 稳定下来。
- 不建议让 Codex 自动评价“好不好看”。应该让人先批准 baseline，Codex 负责防退化。
