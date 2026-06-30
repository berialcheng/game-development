---
name: game-production-orchestrator
description: "Iterative game production orchestrator. Use when planning or improving a game through research handoff, living design docs, phased implementation, generated map/sprite asset planning, asset lifecycle governance, UX/sprite review, playtest feedback, validation, documentation updates, code review, and milestone output."
---

# Codex Game Production

## Purpose

Use this skill as the game-production orchestrator for Codex. It coordinates research, living docs, phased implementation, validation, playtest feedback, review, and milestone packaging. Keep human ownership over final experience goals, art direction, licensing, product decisions, and release readiness.

## Core Principle

Treat Codex output as a high-quality draft with tests and evidence, not as final creative authority. For player-facing work, first implementation is an iteration, not final completion.

```text
research/goal -> design docs -> phase plan -> implementation -> validation -> playtest/review -> docs update -> next iteration or milestone output
```

## Workflow

1. Establish project rules.
   - Create or update `AGENTS.md`, `docs/vision/game_vision.md`, `docs/working/ux_principles.md`, `docs/working/sprite_style_bible.md`, `docs/working/implementation.md`, `docs/evidence/playtest_log.md`, and `docs/ai_asset_register.md`.
   - Read `references/project-scaffold.md` for the recommended files and contents.

2. Manage iteration.
   - Use `references/iteration-management.md` when a feature, UX flow, sprite, combat feel, onboarding path, or playable milestone needs repeated improvement.
   - Track the goal, hypothesis, evidence, docs changed, decision, and next step for each iteration.

3. Work in phases.
   - Keep each phase small enough to test and review.
   - Require scope, constraints, acceptance criteria, files touched, validation commands, and stop conditions.
   - Read `references/phased-implementation.md` before implementing features.

4. Review UX from evidence.
   - Use screenshots, recordings, UI flows, and playtest notes.
   - Separate visible UI issues from inferred product decisions.
   - Read `references/ux-review.md` for audit prompts and checklists.

5. Use sprite and AI art safely.
   - Generate placeholders, not final art, unless the user explicitly accepts the asset governance burden.
   - Keep generated assets out of final folders, validate frame size/pivot/naming, and register provenance.
   - Read `references/sprite-pipeline.md` for sprite/animation pipeline.
   - Read `references/ai-asset-governance.md` for AI asset register, folder, rights, and disclosure rules.
   - Read `references/asset-lifecycle.md` before a generated asset is handed to Godot, promoted to a runtime candidate, or reviewed as final art.

6. Use Codex review deliberately.
   - Separate developer and reviewer roles when possible.
   - Review diff, UX states, input/navigation, asset import, performance, accessibility, and untested assumptions.
   - Read `references/review-workflow.md`.

7. Convert playtests into backlog.
   - Record observations, quotes, metrics, device/input, build, and rage-quit points.
   - Let Codex classify feedback and generate issues, but keep human priority decisions.
   - Read `references/playtest-iteration.md`.

## Hard Rules

- Do not ask Codex to "optimize the whole game" in one pass.
- Do not let Codex silently overwrite final art or release assets.
- Do not let Codex choose final art direction, UX tradeoffs, licensing posture, or store disclosure alone.
- Do not merge broad rewrites without human review and a rollback point.
- Do not skip playtesting, screenshots, or relevant engine validation for player-facing changes.
- Prefer one phase, one review, one validation report, and one human decision at a time.
- Do not update active/final design rules silently. Mark uncertain design changes as proposed and ask for approval.

## Relationship To Other Skills

- Use `$game-reference-research` for competitor/store/media research before deciding what to build.
- Use `$generate2dmap` for generated maps, stages, tilemaps, parallax layers, map props, collision-zone planning, and map previews.
- Use `$generate2dsprite` for generated sprites, animation sheets, actors, NPCs, enemies, props, spells, projectiles, impacts, FX, transparent frames, and GIF previews.
- Use `$godot-2d-implementation` for Godot scene/script/data/assets implementation and engine validation after assets are accepted for runtime.
- Use this skill for the production process around Codex: phase scope, asset briefs, lifecycle manifests, AI asset governance, rules, docs, review loops, UX audits, sprite governance, and playtest iteration.

## Routing Rule

When a request could match more than one skill in this set:

- If you are deciding what to build, defining a phase, planning an iteration, reviewing produced evidence, coordinating handoff, governing AI assets, or packaging a milestone -> use this skill.
- If you are inside a decided phase and editing Godot scenes, scripts, data, assets, effects, tests, or screenshots -> use `$godot-2d-implementation`.
- If the current phase, scope, or acceptance criteria are unclear, run this skill first to define the phase and acceptance, then hand off to `$godot-2d-implementation`. Do not let broad Godot work start without a decided phase.

## Handoff Contract

From `$game-reference-research`, consume:

- Research summary and source links.
- Competitor takeaways.
- UX and visual references.
- Prototype implications.
- Risky assumptions and suggested docs to update.

To `$generate2dmap` / `$generate2dsprite`, provide:

- Asset brief: intended use, art style, camera/view, dimensions, runtime role, and references.
- Lifecycle target: placeholder only, processed candidate, or accepted runtime candidate.
- Output folder policy and required `asset-manifest.json` fields.
- Style bible and restrictions from `docs/working/sprite_style_bible.md` or art direction docs.
- Acceptance criteria: frame size, pivot, alpha, collision relevance, preview requirements, and rejected-output policy.

From `$generate2dmap` / `$generate2dsprite`, collect:

- Generated bundle path and `asset-manifest.json`.
- Prompt/provenance files and register updates.
- Runtime candidate paths and lifecycle states.
- QC metadata, rejected outputs, previews, and remaining human review requirements.

To `$godot-2d-implementation`, provide:

- Current phase and iteration state.
- Design docs to obey.
- Acceptance criteria.
- Files/areas in scope and out of scope.
- Required validation and screenshot/manifest expectations.
- Accepted runtime asset manifest paths and import boundaries.
- Stop condition.

After `$godot-2d-implementation`, collect:

- Changed code, scenes, resources, assets, and docs.
- Imported asset manifests, runtime candidate paths, and generated bundle paths.
- Validation results and command output.
- Screenshots/manifests or missing validation gap.
- Known risks and suggested next iteration.
- Phase maturity: prototype, playtestable, candidate, approved, final, or needs another iteration.

## Output Contract

When using this skill, report:

- Project rule/doc changes.
- Current goal and hypothesis.
- Phase scope and stop condition.
- Docs read and docs changed.
- Human decisions still required.
- Validation or review evidence produced.
- Iteration decision: keep, tweak, revert, split, promote, or package milestone.
- Risks: UX, accessibility, licensing, AI assets, performance, or untested assumptions.
