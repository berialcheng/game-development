# Validation Layers Reference

Use this reference for testing, screenshot baselines, CI, export, and unattended optimization.

## Minimum Gate

Run the strongest available check that matches the change. If the repository lacks the right tool, report that gap and the lower-level check that was run.

Godot process exit code is not sufficient proof. Treat `ERROR:`, `SCRIPT ERROR:`, parse errors, resource loader errors, and failed screenshot saves in command output or manifests as validation failures until fixed or explicitly explained.

| Change type | Minimum verification |
| --- | --- |
| GDScript/resource/scene | Headless startup |
| Data/balance | Data load or schema check plus deterministic fixture when possible |
| Gameplay behavior | Logic test or deterministic scenario with metrics when outcomes change |
| UI layout | Screenshot or manifest for one target state |
| VFX/camera/audio | Deterministic combat/showcase capture or manifest |
| Spawn density/performance | Run manifest with object/effect counts and frame/FPS proxy if available |
| Aseprite export | PNG/JSON, frame/tag, and Godot load check |
| CI/export | Local equivalent command passes first |

## Layer 1: Startup And Import

Run headless startup after scene, script, resource, import, or project setting changes:

```powershell
& $GODOT --path $PROJECT --headless --quit
```

If files were added or imported, run the repository's import command if documented.

If generated PNG/JSON files are used immediately, either run the import path or load them through runtime-safe APIs such as `Image.load()` and `ImageTexture.create_from_image()`. A file existing on disk does not prove `ResourceLoader.load()` can read it before import metadata exists.

## Layer 2: Pure Logic Tests

Use GUT or gdUnit4 for:

- Damage formulas
- RNG helpers
- Shop refresh
- Drop tables
- Economy/progression curves
- Data loaders
- Wave rules
- Cooldowns and spawn rules

Prefer tests that do not depend on rendering or real time.

## Layer 3: Scene And Autoload Tests

Use gdUnit4 scene tests or the repository's test runner for:

- Scene setup
- Signal wiring
- Autoload transitions
- Panel open/close behavior
- Save/load integration points
- Hitbox/hurtbox or socket setup

## Layer 4: Player-Path Integration

Use deterministic automation scenarios, GodotTestDriver, or existing simulated input tooling for:

- Start game
- Move/attack/interact
- Open shop/menu
- Trigger level-up
- Take damage and recover
- Game over/retry
- Save/continue when the project supports persistence
- First-minute tutorial or route guidance when onboarding text changes

Keep visual/integration tests serial unless the project explicitly supports parallel execution.

For interaction polish, include invalid and non-scoring paths, not only happy paths:

- selection limit feedback
- empty or unavailable primary actions
- shop purchase/reroll failures
- sort or utility-action feedback
- modal shortcuts and retry/menu flows

Scenarios should use the same input path a player uses when practical, assert both state changes and player-facing text, print a compact JSON result, and exit nonzero on failure.

Do not prove a player outcome only by calling the final internal function. For win/loss, economy unlocks, tutorial completion, save/continue, or other player-facing outcomes, drive the prerequisite state through gameplay systems or a fixture that mirrors the player path, then assert the final overlay, reason text, run summary, and event log.

For demo-quality menu/UI flow, include at least one deterministic scenario for:

- title menu start path
- invalid input feedback
- settings or audio persistence
- pause/resume/retry path
- save/continue if supported
- victory and failure recap paths

## Layer 5: Screenshot And Manifest Regression

For visual, UI, and effect changes, prefer scenario captures with JSON manifests:

- player showcase
- enemy showcase
- combat HUD
- effect-heavy combat
- shop
- level-up
- pause
- game-over

Codex can judge missing files, missing labels, obvious overflow, event mismatch, excessive counts, and manifest mismatch. Do not let Codex claim final subjective art quality without a human-approved baseline.

For UI changes, headless startup is not sufficient. Pair the affected visible state with at least one deterministic screenshot or manifest, and inspect it for text overflow, unclear disabled states, missing reasons, incorrect event tags, and blocked decision context.

When checking a screenshot, look for player-decision context, not just nonblank pixels: current goal, next action, affordability/missing requirements, risk forecast where relevant, disabled-action reason, and a clear retry/back path on modals.

Screenshot capture rules:

- Headless Godot may use dummy rendering; viewport textures can be null or empty. Use non-headless rendering for actual PNG screenshots when headless cannot produce pixels.
- Save screenshots to an absolute path or a verified project-relative path, then check the file exists and has nonzero size.
- Do not set `screenshot_saved=true` before the save operation completes and the file existence check passes.
- Record screenshot path, absolute path, requested/saved booleans, and save error code in the manifest.
- Inspect at least one produced screenshot with an image viewer/tool when the task concerns UI, art, camera framing, or readability.

Godot headless caveat:

- Restricted sandboxes may crash or hang when Godot cannot write `user://logs`.
- Treat this as an environment/permission failure, not as a gameplay failure or pass.
- Retry with normal permissions when available.
- If retry is unavailable, report the exact unverified scenarios and keep the validation gap explicit.

## Layer 5.5: Run Metrics And Regression Evidence

For balance, performance, effects, and unattended optimization, prefer structured run output. See `playtest-observability.md` for the manifest contract.

At minimum, useful scenarios should record:

- scenario name and seed
- captures and labels
- event counts
- max active enemies/projectiles/effects/damage numbers
- warnings and errors
- run result and duration

Treat missing expected metrics as a validation gap, not a successful proof.

## Layer 6: CI And Export

Add CI only after local commands are stable.

- Use gdUnit4-action for Godot tests when gdUnit4 is chosen.
- Use `godot-ci` or `godot-export` for release export.
- Upload test reports, screenshots, and manifests as artifacts.
- Keep auto-fix steps separate from broad release/export permissions.
