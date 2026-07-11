# Implementation

## Contents

- Before Editing
- Small Contract
- Scene And Script Ownership
- Data And Gameplay
- UI
- Effects, Camera, And Audio
- Asset Integration
- Common Task Patterns
- Architecture Limits
- Completion

Use this reference for scoped Godot 4 2D scene, script, data, UI, gameplay, or asset-integration work.

## Before Editing

Read the target `AGENTS.md`, `project.godot`, affected scene/script/data/resource files, relevant current design state, and existing validation commands. Start from the requested player outcome, not a preferred architecture.

## Small Contract

Identify:

- player-facing outcome
- affected systems/files
- explicit non-scope
- likely failure
- cheapest sufficient validation

A locally clear task does not need a new phase document.

## Scene And Script Ownership

- Keep feature ownership local and scene/script pairs discoverable.
- Use signals for UI/system notifications where they reduce direct coupling.
- Use autoloads for genuine global state/services, not ordinary helpers.
- Prefer existing project patterns over introducing a new framework.
- Use explicit local types when dictionary/JSON/Variant inference is fragile.
- Use exported values, Resources, JSON, or existing data tables for designer-tunable data.
- Defer collision/monitoring mutations triggered inside physics callbacks.
- Keep time/RNG deterministic when tests or captures depend on it.

## Data And Gameplay

- Keep balance values diffable and random rolls seedable.
- Add a small schema/load check or fixture when data contracts change.
- Store important outcome reasons in state/summary data when UI, saves, manifests, or tests must assert them.
- Validate through the player-equivalent path when the outcome depends on prerequisites; do not prove only the final internal function.

## UI

- Use `Control`, Containers, Theme resources, and project focus/navigation conventions.
- Check the states the feature actually introduces: empty, long text, large value, disabled, pause, failure, victory, retry, or gamepad focus as relevant.
- Make high-frequency and invalid actions explain their result at the player's focus point.
- Preserve a clear next action or recovery path.
- Use an actual target-state capture for visible changes; a scene diff does not prove layout/readability.

## Effects, Camera, And Audio

- Keep gameplay truth outside effect-only nodes.
- Define trigger, timing, priority, cleanup, and performance/readability budget.
- Use pooling only for genuinely frequent effects.
- Validate the rendered sequence rather than startup alone.

Read `effects-management.md` when effect layering, camera/audio priority, cleanup, or budgets are material.

## Asset Integration

- Keep source/provenance, processed candidates, previews, and runtime files distinct.
- For managed assets, import only candidates accepted by the target project's contract.
- Validate dimensions/alpha/frames or semantic parts before import, then verify Godot load and gameplay-scale presentation.
- If generated PNG/JSON must load before import metadata exists, use runtime-safe image loading or run the documented import step.
- Keep `.aseprite` sources separate from PNG/JSON exports; read `aseprite-art-pipeline.md` for repeatable pixel-art export.

## Common Task Patterns

### Enemy, Weapon, Or Ability

- Prefer data extension before new architecture.
- Add only required scene/script/projectile/hitbox/effect pieces.
- Validate logic/state plus one focused combat scenario or capture when feedback changes.

### HUD Or Menu

- Reuse existing themes, containers, signals, and focus rules.
- Validate startup/load plus one affected state capture.

### Balance Or Economy

- Prefer data changes and preserve before/after values.
- Validate data load and one deterministic calculation/path when available.

### Character Animation Or Asset

- Check frame/part contract, pivot/socket, draw order, FPS/timing, and import.
- Review one real gameplay state; use continuous rendered evidence when motion quality is the issue.

### Screenshot Scenario

- Add the smallest deterministic scenario that reaches the target state.
- Record scenario/seed, requested/saved capture state, and output path.
- Inspect at least one produced image when the question is visual.

### Regression

- Reproduce the same scenario/seed before editing.
- Patch the smallest likely cause.
- Add a durable check only when the regression was previously invisible and likely to recur.

## Architecture Limits

- Prototype code may be simple but should not silently become a global pattern.
- A vertical slice should connect gameplay, UI, feedback, and one reliable validation path.
- Broad production/release work may justify more tests and evidence; scoped prototype work does not require the full matrix.

## Completion

Report the changed files, validation level/checks, visible or runtime evidence, remaining uncertainty, and whether broader planning or human review is still required.
