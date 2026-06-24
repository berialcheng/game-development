# AGENTS.md

## How To Use This Template

Copy this file to your Godot 4 2D project root. Keep the filename as `AGENTS.md`; Codex, Claude Code, and OpenCode all read it by that exact name from the project root.

Replace these placeholders with values for your machine and project:

- `<YOUR_GODOT_CONSOLE_EXE>` — absolute path to your Godot console executable, including the real version number. Example: `C:/Godot/Godot_v4.3-stable_win64_console.exe`.
- `<YOUR_PROJECT_ROOT>` — absolute path to the folder containing `project.godot`. Example: `C:/games/my-game`.

Then delete this "How To Use" section. The rest is project rules and stays.

## Project

This is a Godot 4 2D game project. Work should preserve the existing scene/script/data structure and optimize for playable, verifiable iteration.

## Commands

Set the local Godot console path before using these commands:

```powershell
$GODOT = "<YOUR_GODOT_CONSOLE_EXE>"
$PROJECT = "<YOUR_PROJECT_ROOT>"
```

Run the game:

```powershell
& $GODOT --path $PROJECT
```

Fast validation after script, scene, or resource changes:

```powershell
& $GODOT --path $PROJECT --headless --quit
```

Recommended automation shape for visual/gameplay checks:

```powershell
& $GODOT --path $PROJECT -- --automation scenario=feedback_baselines auto_quit=true
```

## Repository Layout

Prefer this layout unless the project already has a clear equivalent:

```text
game/
  project.godot
  scenes/
    main/
    player/
    enemy/
    combat/
    ui/
    effects/
  scripts/
    autoload/
    main/
    player/
    enemy/
    combat/
    ui/
    effects/
  data/
  assets/
    characters/
    ui/
    vfx/
  themes/
  docs/
  screenshot/
    automation/
```

## Godot Conventions

- Keep scene and script pairs together by feature, for example `Player.tscn` plus `PlayerController.gd`.
- Use GDScript for gameplay unless the repository already uses another language.
- Prefer typed parameters, typed returns, and clear exported variables.
- Use tabs in `.gd` files when the project uses Godot's default style.
- Keep reusable global state in a small set of autoloads. Do not turn every convenience helper into a singleton.
- Prefer signals for UI refresh and cross-system notifications.
- Prefer JSON or Resources for gameplay tuning. Check `data/` before hardcoding values.
- Use deterministic seed support for gameplay and screenshot automation.

## UI Rules

- Build UI with `Control` nodes, Containers, Theme resources, and type variations.
- Do not implement menus or HUD by absolute positioning unless the existing project requires it.
- Verify UI at 1280x720 and 1920x1080 if screenshots are available.
- Check long labels, large numbers, pause state, shop state, level-up state, and game-over state.
- If UI visuals change, produce or inspect a screenshot. A `.tscn` diff is not enough.

## 2D Art And Aseprite

- Treat `.aseprite` files as source assets and exported PNG/JSON as runtime assets.
- AI-generated PNGs belong in `generated/` and should not be treated as final runtime assets.
- Keep character specs explicit: canvas size, origin, layers, palette, tags, frame counts, FPS, loop flags, and silhouette notes.
- Keep FX, shadow, body, head, weapon, and foreground pieces on stable named layers when possible.
- Use Aseprite CLI/Lua scripts for repeatable import/export, retiming, and palette fixing.
- Add `.gdignore` to bulk candidate folders that Godot should not import.

## Visual Verification

For visual changes, prefer deterministic screenshot scenarios:

- player/character showcase
- enemy showcase
- mixed combat snapshot
- HUD combat snapshot
- shop panel
- level-up panel
- pause panel
- game-over panel

Each automation run should ideally write:

- stamped PNG screenshots
- per-capture JSON manifests
- a run-level manifest containing seed, scenario, capture labels, and timing-sensitive events

## Testing Strategy

Use the smallest test level that proves the change:

- Startup/resource checks: run Godot headless with `--quit`.
- Pure logic tests: use GUT or gdUnit4 for formulas, RNG, shop rules, wave rules, data loaders, and other code that does not require real rendering.
- Scene tests: use gdUnit4 scene testing or a lightweight project test runner for panels, scene setup, signal wiring, and autoload transitions.
- Integration tests: use deterministic project automation, GodotTestDriver, or equivalent simulated-input tooling for player flows.
- Visual regression: use screenshot scenarios plus JSON manifests. Codex may automatically judge missing labels/events and manifest mismatches, but not final subjective art quality.
- CI/export: use GitHub Actions only after local commands are stable. Consider gdUnit4-action for tests and godot-ci/godot-export for release builds.

## Codex Work Rules

- Read the relevant scene/script/data files before changing behavior.
- Keep edits scoped to the requested feature.
- Do not rewrite unrelated architecture to make a small change.
- Do not assume visual quality from code alone.
- If a change affects gameplay timing, say so explicitly.
- If a change is presentation-only, keep it presentation-only.
- When Codex repeats a mistake, update this file or a linked project rule.

## Done Criteria

A task is done only when the relevant checks match the change:

- Script/resource changes: headless startup passes.
- Gameplay changes: deterministic seed or smoke scenario passes.
- Visual changes: screenshot or manifest is produced and reviewed.
- UI changes: key states are checked for layout overflow.
- Asset pipeline changes: Aseprite export outputs expected PNG/JSON and Godot can load them.
- Documentation changes: links, commands, and paths are current for this repository.

## Do Not Edit

Avoid editing these unless the task specifically requires it:

- `.godot/`
- build/export output
- generated import cache files
- raw AI candidate dumps
- unrelated scenes or data tables
