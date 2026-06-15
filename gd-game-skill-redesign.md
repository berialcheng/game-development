# GD Game Skill Redesign

更新时间：2026-06-14

## 目标

把 GitHub 上的 game development skill/repo 调研结果做有限吸收，沉淀成一个可执行、轻量、适合 Godot 4 2D + Codex + Aseprite 的本地 skill。

最终产物：

- `skills/godot-2d-game-development/SKILL.md`
- `skills/godot-2d-game-development/references/implementation.md`
- `skills/godot-2d-game-development/references/effects-management.md`
- `skills/godot-2d-game-development/references/aseprite-art-pipeline.md`
- `skills/godot-2d-game-development/references/validation-layers.md`
- `skills/godot-2d-game-development/references/playtest-observability.md`
- `skills/godot-2d-game-development/references/game-design-audit.md`
- `skills/godot-2d-game-development/references/task-templates.md`
- `skills/godot-2d-game-development/references/selective-adoption.md`

## 有限吸收原则

这次不把外部大型 skill 全部安装进来。原因很实际：

- 大型 multi-agent/game studio 仓库会占用大量上下文。
- 多个相近 skill 容易互相覆盖，反而让 Codex 不稳定。
- 当前最缺的不是更多角色，而是清晰的工程约束、验证命令、截图基线和资产管线。
- Godot 项目差异很大，repo-local 的 `AGENTS.md` 和测试命令比通用大模板更可靠。

所以采用方式是：抽规则、抽检查点、抽文档结构，不抽整套组织。

## 值得吸收的价值

### 1. Godot 工程执行纪律

来自 `fernforestgames/agent-skill-godot`、`haxqer/godot-skill` 一类 Godot skill 的价值：

- 改之前先读 scene/script/data。
- Godot 修改后必须跑 headless 启动或项目测试。
- UI/视觉变更不能只看代码 diff，必须看截图或自动化输出。
- GDScript 尽量 typed，数据尽量进 JSON/Resource。

对应落地：`SKILL.md` 主流程和 `references/implementation.md`。

### 2. Headless/无人值守流水线

来自 `abagames/headless-godot-skill-kit` 的价值：

- 不依赖手动打开编辑器也能做 import、smoke、test、export。
- 每次改动走固定流水线：patch -> headless -> logic tests -> screenshot/manifest。
- 失败要留下可读报告，而不是“看起来修了”。

对应落地：`references/validation-layers.md`。

### 3. 测试分层

来自 GUT、gdUnit4、gdUnit4-action、GodotTestDriver、godot-ci/godot-export 的价值：

- 纯逻辑测试和视觉测试分开。
- scene/autoload 测试和玩家路径集成测试分开。
- CI/export 不要太早引入，先让本地命令稳定。

对应落地：`references/validation-layers.md`。

### 4. Aseprite 资产源文件管线

来自当前本地 Aseprite demo 和 Godot indie skill 调研的价值：

- `.aseprite` 是源文件，PNG/JSON 是导出物。
- AI 图像只是候选，不是最终 runtime 资产。
- 资产要先有 canvas、palette、layer、tag、frame、FPS、pivot 规格。
- Godot import 前要能验证 frame count、tag、JSON metadata。

对应落地：`references/aseprite-art-pipeline.md`。

### 5. 游戏设计不是大文档，而是活上下文

来自 Claude-Code-Game-Studios、game-architect、GDD 仓库的价值：

- GDD 应拆成小文件，服务实现和验证。
- 每个设计文件都要说明实现影响和测试方式。
- 先做 vertical slice，不做宏大 feature list。

对应落地：`references/game-design-audit.md`。

## 明确不吸收的部分

- 不吸收 49 agents/70+ skills 这类完整 studio 组织。
- 不吸收 install-all 的 Godot micro-skills。
- 不把引擎无关的大抽象放在 Godot 项目前面。
- 不在没有本地验证命令前引入复杂 CI/export。
- 不让 Codex 自动决定主观美术质量，除非已有人工批准 baseline。

## 重新设计后的 skill 结构

采用一个主 skill，而不是三个并列 skill：

```text
skills/
  godot-2d-game-development/
    SKILL.md
    agents/
      openai.yaml
    references/
      implementation.md
      aseprite-art-pipeline.md
      validation-layers.md
      game-design-audit.md
      selective-adoption.md
```

这样做的理由：

- Codex 触发更稳定，只需要记住一个 Godot 2D game development skill。
- 细节按任务延迟加载，减少上下文浪费。
- 工程、设计、资产、验证仍然分层，不会混成一份长提示词。
- 新版进一步把效果管理、最低验证矩阵、设计到实现合同、常见任务模板纳入 skill，避免只停留在“能跑”的工程守则。
- 最新版补了 playtest observability：run manifest、事件计数、指标漂移和回归证据，方便无人值守优化不只依赖截图和主观描述。

## 使用方式

当任务是 Godot 4 2D 游戏实现、UI、玩法、Aseprite 资产、测试、截图、GDD 审查时，使用：

```text
Use $godot-2d-game-development to implement and validate ...
```

如果只是项目级约束，优先把命令和禁改目录写进项目 `AGENTS.md`。如果是跨项目通用流程，再写进这个 skill。

## 下一步建议

1. 把 `godot-2d-agent-template/AGENTS.md` 和这个 skill 配套使用。
2. 在真实 Godot 项目里试一次小任务，例如“新增一个 data-driven enemy + 一条 GUT/gdUnit4 测试 + 一个 headless 检查”。
3. 如果某条规则在真实项目里重复有用，再收进 `SKILL.md`；如果只对单个项目有用，留在项目 `AGENTS.md`。
