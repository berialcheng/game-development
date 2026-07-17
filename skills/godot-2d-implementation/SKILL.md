---
name: godot-2d-implementation
description: "Implement and validate scoped Godot 4 2D changes, including scenes, scripts, UI, gameplay, effects, data, imported assets, tests, and captures. Use for concrete project changes with a testable outcome; escalate broad or cross-system work to the production orchestrator."
---

# Godot 4 2D Implementation

## Purpose

Make scoped Godot 4 2D changes that are playable, readable, and verified in proportion to their risk. Prefer the target project's structure and commands over generic templates.

## Priority Order

1. User request.
2. Target project's `AGENTS.md`.
3. Current project design/state docs and test contracts.
4. This skill and its conditional references.
5. External repositories or general Godot advice.

`AGENTS.md` here means the target Godot project's file, not this skill repository's maintenance file.

## Entry Gate

- **Scoped task**: the requested outcome, affected area, and useful validation are clear. Implement directly; a formal production phase is not required.
- **Broad or ambiguous task**: the work spans systems, changes product/UX/art direction, or has no testable outcome. Use `$game-production-orchestrator` first to define scope, acceptance, and stop condition.
- **Asset-only task**: produce visual assets with `$generate2dmap` or `$generate2dsprite`, and music/SFX with `$generate-game-audio`; return here only when engine integration is requested.

Do not expand a local fix into a production-planning cycle.

## Validation Level

Choose the cheapest level that can catch the likely failure:

- `fast`: startup/parse/data-load or focused logic check for local internal changes.
- `focused`: fast checks plus one deterministic scenario or relevant capture for gameplay, UI, asset, camera, or VFX changes.
- `full`: project smoke/regression, representative captures/manifests, and milestone evidence for broad integration or release work.

Read `references/validation.md` for detailed checks, watchdog policy, rendered evidence, run metrics, and retention guidance.

## Workflow

1. Read local context.
   - Find `project.godot`, target `AGENTS.md`, relevant scenes/scripts/data/assets, current design/state docs, and documented validation commands.
   - Read only the design slice and references relevant to the requested change.

2. Classify the task.
   - Gameplay/system/UI/data: `references/implementation.md`.
   - Effects/camera/juice/performance: `references/effects-management.md`.
   - Accepted music, ambience, or SFX import/playback: `references/audio-integration.md`.
   - Aseprite/pixel-art source pipeline: `references/aseprite-art-pipeline.md`.
   - Cutout, paper-doll, skeletal, or Spine-compatible character integration: `references/cutout-character-validation.md`.
   - GDD/core loop/scope critique: `references/game-design-audit.md`.
   - Unfamiliar common task flow: use the common task patterns in `references/implementation.md`.
   - External workflow adoption: `references/selective-adoption.md`.

3. Route new visual and audio assets.
   - Use `$generate2dsprite` for new/revised actors, animation sheets, transparent props, FX, projectiles, portraits, or cutout-character parts.
   - Use `$generate2dmap` for maps, levels, tilemaps, layered/parallax scenes, map-local static props, placement, collision plans, zones, or previews.
   - Use `$generate-game-audio` for new/revised music, ambience, stingers, UI sounds, one-shot SFX, or variation banks.
   - Keep this skill responsible for imports, engine resources, scene wiring, runtime data, tests, and captures.
   - In a managed project, import only assets explicitly accepted by the target project's asset contract. For generated audio, require `accepted_for_runtime` plus non-empty `runtime_candidates` in `asset-manifest.json`; keep source/reference/preview bundles out of runtime imports.

4. Define a small implementation contract.
   - State player-facing outcome, in/out scope, likely failure, validation level, and required evidence.
   - Report contradictions in current docs or asset state before broad changes; do not silently decide product, UX, or art direction.

5. Make the smallest coherent change.
   - Preserve scene/script/data ownership boundaries and existing architecture.
   - Put tunable values in the project's data/resources when appropriate.
   - Do not rewrite unrelated systems to make a local feature easier.

6. Validate the likely failure.
   - Run the repository's documented command first.
   - Use startup/parse checks for engine-load risk, focused scenarios for logic/behavior risk, and captures for visible risk.
   - Treat headless startup as insufficient evidence for UI, animation, VFX, camera, or other rendered behavior.
   - Report missing validation infrastructure rather than pretending a weaker check proves more.

7. Report the outcome.
   - State changed files, validation and evidence, remaining risks, and the next useful step only when one remains.

## Minimum Verification

| Change | Minimum useful evidence |
| --- | --- |
| Script, scene, resource, or setting | Project smoke/startup or equivalent load check. |
| Data or balance | Parse/load plus a focused fixture or deterministic scenario when behavior changes. |
| Gameplay behavior | Focused logic/scenario check; add metrics only when outcomes need them. |
| UI layout | One relevant non-headless capture at a target state. |
| Animation, VFX, camera, or feedback | Short deterministic rendered sequence, capture, or manifest. |
| Imported visual asset | File/alpha/frame or part checks plus Godot import/load and one gameplay-scale view. |
| Imported audio asset | File/format QC plus Godot import/load, event/bus check, and representative runtime listening or recording. |
| Broad integration or release | Full documented smoke/regression and representative evidence. |

## Safe Godot Execution

- Prefer the target project's watchdog/capture wrapper for unattended Godot runs.
- On Windows, use a timeout wrapper that can terminate same-run crash dialogs and `WerFault`.
- Treat `ERROR:` and `SCRIPT ERROR:` as failures unless the project explicitly classifies a known environment-only diagnostic; report that distinction.
- Use non-headless rendering for screenshots when headless uses dummy rendering or returns empty viewport textures.
- If no wrapper exists and unattended runs can hang, copy `assets/godot-watchdog/run_godot_with_watchdog.ps1` into the target project and record concrete commands in its `AGENTS.md`.
- Keep concrete executables, modes, timeouts, and output paths in the target project, not this shared skill.

## Guardrails

- Use the project's existing language; default to typed GDScript only for new GDScript projects or files.
- Prefer deterministic seeds for reproducible gameplay tests and captures.
- Use Godot Containers and Theme resources for adaptable UI instead of unnecessary absolute positioning.
- Keep source art/audio and runtime exports distinct; do not treat generated candidates as final assets.
- Do not use code-drawn art when the user requested real visual assets.
- Do not let manifest counters stand in for actual pixel review when the question is visual.
- Do not add CI/export configuration before its local equivalent passes.

## Durable Learning

- Put project-specific commands and forbidden edits in target `AGENTS.md`.
- Put player-facing intent in project design/current-state docs.
- Put repeated checks in tests or automation.
- Put cross-project rules in this skill only after they prevent a recurring or high-cost failure.

## Output Contract

Report:

- Changed code, scene/resource, data, asset, and doc files.
- Validation level, commands/checks, and notable evidence.
- Imported visual/audio asset contract and state when relevant.
- What remains unverified and why.
- Known risks and whether broader planning or human visual/product review is still required.
