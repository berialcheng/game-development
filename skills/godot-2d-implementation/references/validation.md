# Validation

## Contents

- Choose A Level
- Process Result Rules
- Safe Unattended Godot
- Risk-To-Evidence Matrix
- Player-Path Scenarios
- Screenshots
- Structured Run Evidence
- Regression Rules
- Evidence Retention
- Reporting

Use this reference to choose risk-appropriate Godot checks, safe unattended execution, rendered evidence, and bounded run metrics. The goal is to catch the likely expensive failure, not to maximize evidence volume.

## Choose A Level

### Fast

Use for local internal changes:

- parse/startup/resource load
- data/schema load
- focused pure-logic test

### Focused

Use when player behavior or presentation changes:

- fast checks
- one deterministic scenario or relevant scene state
- one rendered capture/short sequence for UI, art, camera, animation, or VFX
- only metrics that answer the current risk

### Full

Use for broad integration, milestone, export, or release:

- documented project smoke/regression
- representative player paths and captures
- asset/import and run-summary checks
- platform/export checks when relevant

Do not run full validation for every local edit.

## Process Result Rules

A process exit code is not enough. Treat these as failures until fixed or explicitly classified:

- `ERROR:` or `SCRIPT ERROR:`
- parse/resource loader/import errors
- timeout or native crash dialog
- expected scenario/capture not produced
- manifest says saved/pass while the artifact is missing or errors are nonempty

Distinguish environment failures from gameplay failures, but do not claim the unrun gameplay path passed.

## Safe Unattended Godot

Prefer the target project's `AGENTS.md` watchdog commands. Concrete executable paths, modes, timeouts, and evidence directories belong to the project.

If no safe wrapper exists and native dialogs can hang automation, copy `assets/godot-watchdog/run_godot_with_watchdog.ps1` into the project and adapt local defaults.

A safe wrapper should:

- capture stdout/stderr and a Godot log outside fragile `user://` paths
- enforce a timeout
- terminate the same-run Godot process and `WerFault` on timeout
- scan output for engine/script errors
- return a failing status for invalid runs

Use non-headless execution for screenshots when headless uses dummy rendering or empty viewport textures.

## Risk-To-Evidence Matrix

| Risk | Useful evidence |
| --- | --- |
| Script/scene/resource cannot load | Startup/import/load check. |
| Formula/data/RNG is wrong | Pure deterministic fixture/test. |
| Signals/state transitions are wrong | Focused scene/player-path scenario. |
| UI is clipped/confusing | Actual target-state capture and focus/input path. |
| VFX/camera/audio feedback is wrong | Short deterministic rendered sequence. |
| Animation/sockets/draw order are wrong | Gameplay-scale capture or continuous sequence. |
| Spawn/effect density regresses | Bounded run counts and frame/FPS proxy if already available. |
| Export/CI breaks | Stable local equivalent before CI/export. |

## Player-Path Scenarios

Drive the prerequisite state through gameplay systems or a fixture that mirrors them. Assert both state change and player-facing result where relevant.

Useful paths include start, move/attack/interact, shop/menu, pause/resume, invalid action, victory/failure/retry, and save/continue only when the affected feature needs them.

Do not require a demo to automate every possible route before a scoped change can ship.

## Screenshots

- Prefer in-game capture written to a workspace evidence path over OS desktop screenshots.
- Verify the requested capture was actually saved, exists, has nonzero size, and has expected dimensions.
- Inspect the image with an available viewer when the task concerns layout, art, camera, animation, or readability.
- If direct image viewing is blocked, use an existing local review page or bounded checks such as dimensions, hash prefix, nonblank pixel sample, and manifest fields; report the fallback.
- One relevant capture is the default. Add more only when different states answer different acceptance questions.

For visual questions, manifest/node visibility alone is insufficient if the actual pixels can contradict it.

## Structured Run Evidence

Add a run manifest only when behavior, balance, effects, stability, or performance needs repeatable evidence. Use the project's schema when present.

A minimal run summary can contain:

```json
{
  "schema_version": 1,
  "scenario": "combat_baseline",
  "seed": 12345,
  "duration_seconds": 30.0,
  "result": "pass",
  "captures": [],
  "events": {},
  "metrics": {},
  "warnings": [],
  "errors": []
}
```

Record only metrics that can change the current decision, such as outcome/reason, damage, kills, cooldown failures, affordability, max active objects/effects, missing captures, or frame-time proxy.

Avoid per-frame logs unless running a bounded motion/performance investigation.

## Regression Rules

Fail or investigate when:

- a required key/artifact disappears
- an expected feature event remains zero
- a saved capture is missing/empty
- new engine/script/import errors appear
- fixed-seed outcomes drift outside an accepted tolerance
- an object/effect budget is exceeded under project policy

Do not fail subjective visual taste without a human baseline or explicit project threshold.

## Evidence Retention

- Fast/focused runs may overwrite `latest` evidence.
- Keep recent failed runs only when useful for diagnosis.
- Archive milestone/release bundles separately.
- Rotate large logs according to project policy.
- Do not append every successful run to hand-maintained Markdown.

## Reporting

Report validation level, command/scenario/seed, captures or key metrics, warnings/errors, environment limitations, and what still requires human review.
