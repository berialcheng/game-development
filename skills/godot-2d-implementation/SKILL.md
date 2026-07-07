---
name: godot-2d-implementation
description: "Godot 4 2D implementation and validation workflow. Use when executing a defined production phase in a Godot project, including scenes, scripts, UI, gameplay, effects, Aseprite/sprite import, tests, screenshots, manifests, and next-iteration reports."
---

# Godot 2D Game Development

## Purpose

Use this skill to make Godot 4 2D game changes that are playable, scoped, readable in motion, and verifiable. Keep it lightweight: extract useful workflows from external game-development skills, but do not import large multi-agent studio systems unless the repository already has the validation discipline to support them.

## Priority Order

When instructions conflict, apply this order:

1. User request.
2. Target Godot project's `AGENTS.md` (project-specific rules, commands, forbidden paths).
3. Project design docs and test matrix.
4. This skill.
5. External repositories and general Godot advice.

`AGENTS.md` here refers to the target Godot project's file, not this skill repository's `AGENTS.md` (which governs skill maintenance, not in-project work).

If the target Godot project has no `AGENTS.md`, create or propose one only when it would capture commands, forbidden paths, validation rules, or repeated project-specific mistakes.

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
   - For production-loop projects, also read `docs/working/implementation_details.md`, `docs/working/ux_principles.md`, `docs/working/ui_flow_inventory.md` for UI work, and `docs/working/sprite_style_bible.md` for asset work when present.

2. Classify the task and load only the needed reference.
   - Gameplay/system/UI/data: `references/implementation.md`
   - Effects/camera/audio/juice/performance budget: `references/effects-management.md`
   - Aseprite/pixel-art/source asset pipeline: `references/aseprite-art-pipeline.md`
   - Tests/screenshots/CI/unattended checks: `references/validation-layers.md`
   - Playtest metrics, structured logs, run manifests, regression evidence: `references/playtest-observability.md`
   - GDD/core loop/scope/design critique: `references/game-design-audit.md`
   - Common task flows: `references/task-templates.md`
   - External skill or repo adoption: `references/selective-adoption.md`

3. Route generated visual assets before Godot import.
   - If the task requires new or revised character sprites, NPCs, enemies, animation sheets, spells, projectiles, impacts, props, transparent frames, or GIF previews, invoke `$generate2dsprite` first and then import/validate the accepted outputs in Godot.
   - If the task requires new or revised maps, levels, rooms, tilemaps, parallax backgrounds, layered raster scenes, prop packs, collision zones, walkable areas, or map previews, invoke `$generate2dmap` first and then wire the accepted outputs into Godot scenes, resources, collision, and metadata.
   - Use both skills when a playable phase needs map art plus actor/prop/FX assets. `$generate2dmap` owns map/scene assets and `$generate2dsprite` owns actors, animation sheets, props, projectiles, impacts, and FX.
   - Keep this skill responsible for Godot integration after asset generation: import settings, SpriteFrames, TileMap or scene data, collision, rendering order, deterministic screenshots, manifests, and runtime validation.
   - Consume `asset-manifest.json` when generated assets come from a managed bundle. Import only entries marked `accepted_for_runtime`; leave raw outputs, prompts, reference mockups, GIFs, and QA previews out of runtime scenes.
   - Keep generated bundle `source/` and `preview/` folders behind `.gdignore` or outside Godot import paths when bulk import would create noise.
   - Do not bypass the asset skills with code-drawn art when the user asks for real visual assets. Use procedural placeholders only when explicitly requested or when validation scaffolding needs throwaway fixtures.

4. Convert intent into an implementation contract.
   - Define the player-facing outcome.
   - Identify systems, scenes, scripts, data, assets, and effects touched.
   - Name the likely failure mode.
   - Choose the minimum validation artifact before editing.

5. Make the smallest coherent change.
   - Keep scene/script/data ownership boundaries intact.
   - Put tuning values in JSON, Resources, or existing data tables when available.
   - Do not rewrite unrelated architecture to make a local feature easier.
   - Do not treat AI-generated art candidates as final source assets.

6. Validate against the minimum matrix.
   - Always run the repository's documented command first.
   - Prefer the target project's `AGENTS.md` watchdog/capture wrapper for Godot smoke, script, and screenshot runs; do not launch Godot GUI, bare long-running Godot commands, or desktop screenshot commands that can hang unattended.
   - On Windows, run Godot validation through a timeout wrapper that can kill native crash dialogs and `WerFault` instead of waiting forever.
   - If the target project has no wrapper, copy `assets/godot-watchdog/run_godot_with_watchdog.ps1` into the project and register concrete commands in the project `AGENTS.md`.
   - Treat Godot `ERROR:` and `SCRIPT ERROR:` output as failed validation even when the process exits `0`.
   - If a required tool is missing, run the strongest available lower-level check and report the missing validation infrastructure.

7. Report outcome.
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

## Input Contract

Before implementation, identify:

- Current phase and iteration state.
- Design docs read.
- Acceptance criteria.
- In-scope and out-of-scope systems.
- Required validation: startup, logic test, deterministic scenario, screenshot, manifest, Aseprite export, or playtest note.
- Asset manifests to consume and which entries are `accepted_for_runtime`.
- Docs that may need updates.

If the docs are missing, stale, or contradictory, report the conflict before broad changes. Do not silently resolve product/UX/art direction conflicts in code.

If the current phase, acceptance criteria, or in/out scope are not defined, stop and invoke `$game-production-orchestrator` to define the phase before implementing. Do not begin broad Godot work without a decided phase and acceptance.

## Guardrails

- Use GDScript for gameplay unless the project already uses C# or another language.
- Prefer typed GDScript signatures and exported variables for designer-tunable values.
- Use deterministic seed support for gameplay, screenshots, and tests.
- Use non-headless rendering for screenshot capture when headless uses dummy rendering or returns empty viewport textures.
- Do not let direct Godot process launches hang unattended after a native crash popup; use a watchdog wrapper for smoke, script, and screenshot runs.
- Keep concrete wrapper command names, modes, timeouts, and output directories in the target project's `AGENTS.md`; keep this skill limited to cross-project validation policy.
- Use Godot Containers and Theme resources for UI rather than absolute-positioned panels.
- Keep `.aseprite` files as source assets and exported PNG/JSON as runtime assets.
- Put AI image candidates in generated or ignored folders until curated.
- Do not import generated source bundles directly; consume accepted runtime candidates from manifest entries.
- Do not let Codex judge final subjective art quality without a human-approved baseline.
- Avoid importing external skills wholesale. Extract workflows, commands, templates, QA gates, and failure checks instead.

## Related Skills

- Use `$game-production-orchestrator` first when the phase, acceptance criteria, or asset scope is unclear.
- Use `$generate2dmap` for generated or revised maps, levels, tilemaps, parallax stages, layered raster scenes, prop packs, collision-zone planning, and map previews.
- Use `$generate2dsprite` for generated or revised sprites, animation sheets, actors, NPCs, enemies, props, spells, projectiles, impacts, FX, transparent frames, and GIF previews.
- Use this skill after asset generation for Godot import settings, scene wiring, runtime data, tests, screenshots, manifests, and engine validation.

## Learning Loop

After repeated mistakes or useful discoveries:

- Put project-specific commands, paths, and forbidden edits in `AGENTS.md`.
- Put player-facing intent and design constraints in `docs/design/`.
- Put repeatable validation in tests, screenshot scenarios, or CI.
- Put run metrics, counters, and screenshot manifests in automation outputs.
- Put cross-project durable workflow rules in this skill.
- Turn any recurring failure into either a rule, a fixture, a screenshot scenario, or a checklist item.

## Output Contract

After implementation, report:

- Changed code files.
- Changed scene/resource files.
- Changed docs.
- Assets added or modified, including manifest paths and lifecycle states.
- Tests/checks run and notable command output.
- Screenshot, manifest, or manual validation result.
- Known risks and missing validation.
- Suggested next iteration.
- Phase state: prototype, playtestable, candidate, approved, final, or needs another iteration.

## Sample Prompts

```text
Use $godot-2d-implementation to add a data-driven enemy with one deterministic combat screenshot.
Use $generate2dsprite to create a side-view warrior idle/run sheet, then use $godot-2d-implementation to import it and verify SpriteFrames.
Use $godot-2d-implementation to review a GDD slice and produce implementation/test implications.
Use $generate2dmap to create a side-scroller stage background and object plan, then use $godot-2d-implementation to wire the scene and validate runtime collision.
```
