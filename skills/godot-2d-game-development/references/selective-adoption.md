# Selective Adoption Reference

Use this reference when deciding what to absorb from external game-development skill and repo research.

## Adopt

- Headless Godot startup and import checks.
- GDScript syntax/test discipline.
- Patch -> smoke -> logic test -> screenshot/manifest workflow.
- GUT or gdUnit4 test layering.
- Screenshot scenario manifests for visual/UI/effect work.
- GDD templates that become small repo-local design files.
- QA gates and done criteria.
- Aseprite spec-first asset pipeline.
- `.gdignore` protection for generated candidate assets.
- Effects budget rules for combat readability, VFX density, audio priority, and camera shake.
- Task templates that reduce repeated planning mistakes.

## Do Not Adopt By Default

- Large multi-agent studio hierarchies.
- Dozens of overlapping micro-skills.
- Engine-agnostic abstractions that hide Godot project reality.
- CI/export complexity before local commands are stable.
- Subjective AI art scoring without a human-approved baseline.
- External editor bridges before a small proof works on the current machine.
- Generic "juice" advice that does not define timing, visibility, ownership, and validation.

## External Repos And Use

- `fernforestgames/agent-skill-godot`: extract Godot command discipline and screenshot verification.
- `abagames/headless-godot-skill-kit`: extract unattended headless workflow.
- `haxqer/godot-skill`: extract Codex-compatible inspect/edit/run/debug structure.
- `thedivergentai/gd-agentic-skills`: extract taxonomy only; avoid install-all behavior.
- `jame581/GodotPrompter`: extract Godot domain skill categories.
- `Donchitos/Claude-Code-Game-Studios`: extract GDD, QA, release gates, and review templates only.
- `Aetik-yue/godot-indie-dev`: extract Godot + Aseprite solo-indie flow.
- `indiesoftby/defold-agent-config`: extract `AGENTS.md` plus local skill folder structure, not engine specifics.

## Adoption Test

Before adding any external rule, ask:

- Does it reduce repeated mistakes in this repository?
- Can it be validated with an existing command, screenshot, manifest, test, or QA gate?
- Does it fit the current Godot version and platform?
- Does it stay small enough to read when triggered?
- Does it belong in `AGENTS.md`, this skill, a test, or a project-specific design doc?
- Will it improve a real player-facing outcome, or only add process?

If the answer is only "this repo looked impressive", do not adopt it.
