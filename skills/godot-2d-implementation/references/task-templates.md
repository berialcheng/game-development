# Task Templates Reference

Use these templates for common Godot 4 2D tasks. Keep each task scoped to Read, Change, Validate, Report.

## Add Enemy

Read:

- Enemy scenes/scripts/data.
- Spawner/wave rules.
- Combat design slice if present.

Change:

- Add or extend enemy data.
- Add scene/script only if data cannot express the behavior.
- Add telegraph, hit feedback, and collision setup.

Validate:

- Data load or logic test.
- Deterministic combat scenario or enemy showcase screenshot.

Report:

- Behavior, tuning values, feedback layer, validation, missing tests.

## Add Weapon Or Ability

Read:

- Weapon/ability data.
- Player controller/combat scripts.
- Effect and audio conventions.

Change:

- Add data-driven ability fields.
- Add projectile/hitbox/effect scenes only where needed.
- Keep cooldown, damage, range, and cost testable.

Validate:

- Logic test for cooldown/damage/range if tests exist.
- Combat screenshot/manifest for hit feedback.

Report:

- Player-facing purpose, balance values, validation gap.

## Tune Economy Or Balance

Read:

- Data tables, progression docs, shop/drop rules, existing tests.

Change:

- Prefer data changes over script changes.
- Keep old and new values easy to diff.

Validate:

- Data load check.
- Deterministic fixture for shop/drop/progression if available.

Report:

- Before/after intent, risks, untested player experience.

## Add HUD Or Menu Panel

Read:

- Existing UI scenes, themes, focus rules, localization/text constraints.

Change:

- Use `Control`, Containers, Theme resources, and signals.
- Cover empty, long-text, large-number, pause, and gamepad focus states.

Validate:

- Screenshot for at least one target state.
- Headless startup for scene/resource load.

Report:

- States checked, overflow/focus risk, screenshot path if produced.

## Harden Demo Player Path

Read:

- GDD demo promises, test matrix, menu/HUD scripts, save/settings code, screenshot scenarios, playtest manifests.

Change:

- Pick one player-facing gap: first action clarity, invalid-action reason, route guidance, shop affordability, save/continue, pause/settings, victory recap, failure recap, or retry path.
- Make the state explain itself on screen with concrete next actions and short reason text.
- Store important outcome reasons in summary/manifest data when tests or screenshots need to assert them.

Validate:

- Run the nearest deterministic scenario that reaches the state through gameplay or player-equivalent automation.
- Capture the affected visible state when UI changed.
- Inspect stdout/stderr for Godot errors and inspect the screenshot for decision context.

Report:

- Player path improved, scenario/seed, screenshot path, and any remaining unverified subjective quality.

## Add VFX, Camera, Or Audio Feedback

Read:

- Effect scenes, audio bus conventions, camera scripts, combat readability rules.

Change:

- Define signal, timing, priority, owner, and cleanup.
- Use pooling for frequent effects.
- Keep gameplay logic out of effect-only nodes.

Validate:

- Headless startup.
- Deterministic combat/showcase screenshot or manifest.

Report:

- What the player should notice, what remains readable, budget/cleanup choices.

## Import Character Animation

Read:

- Aseprite spec, source `.aseprite`, export scripts, SpriteFrames importer, character controller.

Change:

- Export PNG/JSON repeatably.
- Regenerate or update SpriteFrames.
- Align pivot, sockets, hitbox/hurtbox, and animation FPS.

Validate:

- PNG/JSON/frame/tag checks.
- Godot import/load.
- Character showcase screenshot if available.

Report:

- Tags, frame counts, runtime alignment, missing visual baseline.

## Add Screenshot Scenario

Read:

- Automation runner, screenshot folder, manifest schema, existing scenarios.
- Rendering mode constraints. Check whether headless uses dummy rendering or can actually produce viewport pixels.

Change:

- Add the smallest deterministic scenario that proves the target state.
- Record seed, scenario, labels, event counts, and output paths.
- Save captures to verified paths and record requested/saved/error fields.

Validate:

- Run the scenario if the command is available.
- Inspect manifest for missing captures, failed save fields, or event mismatch.
- Open at least one produced PNG when the task concerns visual output.

Report:

- Scenario name, seed, captures, unverified visual quality.

## Add Runtime-Generated Pixel Asset

Read:

- Asset spec, Aseprite/source pipeline, Godot import settings, current runtime loader code.

Change:

- Generate source and runtime PNG/JSON from a repeatable script.
- Keep `.aseprite` source separate from exported runtime files.
- If the asset is generated during the task, load PNGs with runtime-safe APIs or run the documented import step.

Validate:

- Check source file, PNG/JSON existence, dimensions, frame counts, and tags.
- Run Godot startup and treat resource loader errors as failures even with exit code `0`.
- Produce a showcase screenshot if readability or alignment matters.

Report:

- Source path, export path, validation command, any CLI/tool limitations.

## Add Playtest Metric Or Manifest Field

Read:

- Automation runner, manifest schema, existing scenario outputs, baseline comparison code.

Change:

- Add the smallest counter or metric that proves a real gameplay, UI, effect, or performance risk.
- Keep metric names stable and documented by example output.
- Avoid logging every frame unless the project already has a bounded profiling path.

Validate:

- Run the smallest scenario that emits the manifest.
- Check that the field is present, deterministic with a fixed seed, and meaningful for regression.

Report:

- Field name, scenario, seed, observed value, baseline/tolerance if available.

## Investigate Regression

Read:

- Recent run manifests, screenshots, tests, logs, changed scenes/scripts/data.

Change:

- Reproduce with the same seed/scenario before editing.
- Patch the smallest likely cause.
- Add or tighten a metric, test, or screenshot if the regression was previously invisible.

Validate:

- Re-run the failing command or scenario.
- Compare manifest deltas and screenshots against the expected baseline.

Report:

- Root cause, proof of fix, metric/screenshot evidence, remaining uncertainty.

## Execute Production Phase

Read:

- `AGENTS.md`.
- Current implementation phase doc, usually `docs/working/implementation_details.md`.
- Relevant design docs such as UX principles, UI flow inventory, sprite style bible, combat/progression notes.
- Existing tests, automation, and validation commands.

Change:

- Implement only the current phase.
- Keep explicit non-scope untouched.
- Update docs only when the implementation changes active knowledge, and report why.
- Preserve rollbackability by avoiding broad unrelated refactors.

Validate:

- Run the phase's required validation.
- Treat Godot script/resource errors as failures even with exit code 0.
- Produce screenshot/manifest evidence for player-facing visual changes when available.

Report:

- Changed files by category: code, scenes/resources, data, assets, docs.
- Validation result.
- Whether acceptance criteria passed.
- Remaining risks.
- Suggested next iteration or promotion state.

## Add First GUT Or gdUnit4 Test

Read:

- Existing addons, test directories, CI scripts, data loaders.

Change:

- Use the framework already installed.
- Start with pure logic: formulas, RNG, data, shop, drops, wave rules.

Validate:

- Run the test command or document missing runner setup.

Report:

- Test scope, command, pass/fail, next high-value test.
