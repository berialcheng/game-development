# Project Scaffold

Use this reference when setting up a game project so Codex can work predictably.

## Recommended Files

```text
AGENTS.md
docs/
  vision/
    game_vision.md
    target_player.md
    design_pillars.md
  working/
    ux_principles.md
    ui_flow_inventory.md
    sprite_style_bible.md
    implementation.md
    implementation_details.md
    balance_notes.md
  evidence/
    playtest_log.md
    ux_review_reports.md
    validation_reports.md
    screenshots_index.md
    code_review.md
  output/
    milestone_summary.md
    build_manifest.md
    release_notes.md
    final_asset_register.md
  iteration_log.md
  ai_asset_register.md
assets/
  raw/
  generated_placeholders/
  final/
  atlases/
tests/
```

For small projects, a flat `docs/` directory is acceptable. Preserve the four document roles even if folders are flattened.

## Document Layers

Vision docs:

- Decide direction and should not change casually.
- Examples: game vision, target player, design pillars.

Working docs:

- Current iterating design and implementation context.
- Examples: UX principles, UI flow inventory, sprite style bible, implementation roadmap/details, balance notes.

Evidence docs:

- Records of what happened and what was observed.
- Examples: playtest logs, UX reviews, validation reports, screenshots index, code review notes.

Output docs:

- Milestone/release packaging.
- Examples: milestone summary, build manifest, release notes, final asset register.

## File Roles

`AGENTS.md`:

- Short project rules for Codex.
- Engine version, forbidden paths, validation commands, review checklist, asset rules.
- Keep under about 120 lines unless the project genuinely needs more.

`game_vision.md`:

- Genre, target player, emotional promise, core loop, session length, platform constraints.

`ux_principles.md`:

- Player clarity rules, feedback rules, menu depth, input support, accessibility goals.
- Examples: "player knows current goal within 1 second", "damage has visual and audio feedback", "settings are reachable from pause".

`ui_flow_inventory.md`:

- Every screen/panel, enter path, exit path, empty state, error state, pause behavior, focus/navigation support, risk.

`sprite_style_bible.md`:

- Resolution, camera, frame sizes, pivot, padding, outline, palette, animation names/frame counts, naming, atlas grouping, restrictions.

`implementation.md`:

- High-level phases only.
- Do not mix every detailed task into this file.
- Treat it as a roadmap, not the current work order.

`implementation_details.md`:

- Current phase scope, tasks, acceptance criteria, test commands, screenshots needed, stop condition.
- Keep only the active/current phase here so Codex does not accidentally execute the whole roadmap.

`playtest_log.md`:

- Session observations, quotes, metrics, input device, build, issues, next hypotheses.

`ai_asset_register.md`:

- Date, tool/model if known, prompt/source, generated file path, intended use, placeholder/final status, human review status, rights/disclosure notes.

`iteration_log.md`:

- Why a feature changed, what hypothesis was tested, what evidence was produced, what decision was made, and what comes next.

## AGENTS.md Template

```md
# AGENTS.md

## Project
This is a game project. Prioritize readable, testable, maintainable player-facing changes.

## Engine
- Engine: Godot 4.x / Unity / custom.
- Do not change engine version or project settings unless explicitly asked.
- Keep UI logic separate from gameplay logic where practical.
- Keep content data separate from code when possible.

## UX Rules
- Every player action must produce clear feedback.
- Menus must support keyboard/controller navigation when the project supports those inputs.
- Error, empty, loading, disabled, pause, and game-over states must be handled.
- Do not add new UI screens without updating `docs/ui_flow_inventory.md`.

## Sprite / Asset Rules
- Never overwrite `assets/final`.
- AI-generated or placeholder art must go into `assets/generated_placeholders`.
- Update `docs/ai_asset_register.md` for generated assets.
- Maintain consistent frame size, pivot, padding, naming, and atlas grouping.
- Do not imitate a named living artist or use unlicensed references.

## Implementation Rules
- Work one phase at a time.
- Before editing, summarize scope and likely files.
- After editing, report changed files, assumptions, validation, and risks.
- Add or update tests when behavior changes.
- Do not make broad architecture changes without explicit approval.

## Review Checklist
- Gameplay regression
- UI state bugs
- Input/navigation issues
- Accessibility issues
- Asset import mistakes
- Performance risks
- Unverified assumptions
```
