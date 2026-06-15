---
name: godot-2d-game-development
description: Godot 4 2D game development workflow for Codex. Use when implementing or reviewing Godot 2D gameplay, UI, scene, script, data, effects, camera feedback, audio cues, Aseprite asset pipeline, automated tests, screenshot baselines, GDD slices, or repo-local AGENTS.md rules. Especially useful for small/solo indie game projects that need scoped implementation, player-facing effect management, deterministic validation, and limited adoption of external game-development skill repositories.
---

# Godot 2D Game Development

## Purpose

Use this skill to make Godot 4 2D game changes that are playable, scoped, readable in motion, and verifiable. Keep it lightweight: extract useful workflows from external game-development skills, but do not import large multi-agent studio systems unless the repository already has the validation discipline to support them.

## Priority Order

When instructions conflict, apply this order:

1. User request.
2. Repository `AGENTS.md`.
3. Project design docs and test matrix.
4. This skill.
5. External repositories and general Godot advice.

If the project has no `AGENTS.md`, create or propose one only when it would capture commands, forbidden paths, validation rules, or repeated project-specific mistakes.

## Phase Mode

Identify the project phase before choosing validation strictness:

- Prototype: move quickly, but mark disposable code and avoid pretending exploratory work is production architecture.
- Vertical slice: prove one core loop, one HUD path, one enemy/reward family, and one deterministic validation scenario.
- Production: require tests, screenshots, manifests, or QA gates for new gameplay, UI, asset, or effect changes.

If the phase is unclear, assume vertical slice for new game features.

## Workflow

1. Read local context.
   - Find `project.godot`, `AGENTS.md`, `docs/design/`, scenes, scripts, data, assets, tests, and automation commands.
   - Prefer current project structure over generic templates.
   - Read the relevant design slice before changing behavior.

2. Classify the task and load only the needed reference.
   - Gameplay/system/UI/data: `references/implementation.md`
   - Effects/camera/audio/juice/performance budget: `references/effects-management.md`
   - Aseprite/pixel-art/source asset pipeline: `references/aseprite-art-pipeline.md`
   - Tests/screenshots/CI/unattended checks: `references/validation-layers.md`
   - Playtest metrics, structured logs, run manifests, regression evidence: `references/playtest-observability.md`
   - GDD/core loop/scope/design critique: `references/game-design-audit.md`
   - Common task flows: `references/task-templates.md`
   - External skill or repo adoption: `references/selective-adoption.md`

3. Convert intent into an implementation contract.
   - Define the player-facing outcome.
   - Identify systems, scenes, scripts, data, assets, and effects touched.
   - Name the likely failure mode.
   - Choose the minimum validation artifact before editing.

4. Make the smallest coherent change.
   - Keep scene/script/data ownership boundaries intact.
   - Put tuning values in JSON, Resources, or existing data tables when available.
   - Do not rewrite unrelated architecture to make a local feature easier.
   - Do not treat AI-generated art candidates as final source assets.

5. Validate against the minimum matrix.
   - Always run the repository's documented command first.
   - Treat Godot `ERROR:` and `SCRIPT ERROR:` output as failed validation even when the process exits `0`.
   - If a required tool is missing, run the strongest available lower-level check and report the missing validation infrastructure.

6. Report outcome.
   - State what changed, what validation ran, what remains unverified, and whether the gap belongs in `AGENTS.md`, `docs/design/`, a test, or this skill.

## Minimum Verification Matrix

| Change type | Minimum verification |
| --- | --- |
| GDScript, resource, scene, or project setting | Headless startup or the repository's equivalent smoke command |
| Data or balance | Data/schema load check plus one deterministic fixture when tests exist |
| Gameplay behavior | Logic test, deterministic scenario, and run metrics when behavior changes player outcomes |
| UI layout | Screenshot or automation capture for at least one target state |
| VFX, camera, damage feedback, or audio cue | Deterministic combat/showcase capture or manifest, not only headless startup |
| Performance or spawn-density change | Run manifest with counts, duration, FPS/frame-time proxy if available, and object/effect totals |
| Aseprite export | PNG/JSON existence, frame/tag validation, and Godot import/load check |
| CI/export | Local equivalent command must pass before adding CI/export config |
| Design-only change | Updated design slice with implementation and validation implications |
| Skill/rule change | `quick_validate.py` passes for the skill folder |

## Project Shape

Prefer this layout only when the repository does not already have a clear equivalent:

```text
game/
  project.godot
  scenes/
  scripts/
  data/
  assets/
  themes/
  docs/design/
  tests/
  screenshot/automation/
```

For new Godot 2D repositories, create or adapt `AGENTS.md` with Godot paths, headless command, test command, screenshot command, forbidden generated paths, and done criteria.

## Guardrails

- Use GDScript for gameplay unless the project already uses C# or another language.
- Prefer typed GDScript signatures and exported variables for designer-tunable values.
- Use deterministic seed support for gameplay, screenshots, and tests.
- Use non-headless rendering for screenshot capture when headless uses dummy rendering or returns empty viewport textures.
- Use Godot Containers and Theme resources for UI rather than absolute-positioned panels.
- Keep `.aseprite` files as source assets and exported PNG/JSON as runtime assets.
- Put AI image candidates in generated or ignored folders until curated.
- Do not let Codex judge final subjective art quality without a human-approved baseline.
- Avoid importing external skills wholesale. Extract workflows, commands, templates, QA gates, and failure checks instead.

## Learning Loop

After repeated mistakes or useful discoveries:

- Put project-specific commands, paths, and forbidden edits in `AGENTS.md`.
- Put player-facing intent and design constraints in `docs/design/`.
- Put repeatable validation in tests, screenshot scenarios, or CI.
- Put run metrics, counters, and screenshot manifests in automation outputs.
- Put cross-project durable workflow rules in this skill.
- Turn any recurring failure into either a rule, a fixture, a screenshot scenario, or a checklist item.

## Sample Prompts

```text
Use $godot-2d-game-development to add a data-driven enemy with one deterministic combat screenshot.
Use $godot-2d-game-development to import an Aseprite character sheet and verify SpriteFrames.
Use $godot-2d-game-development to review a GDD slice and produce implementation/test implications.
Use $godot-2d-game-development to add hit feedback VFX without hiding combat readability.
```
