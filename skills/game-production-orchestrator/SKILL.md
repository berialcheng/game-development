---
name: game-production-orchestrator
description: "Coordinate multi-stage game production when scope, acceptance criteria, cross-skill handoffs, asset promotion, playtest iteration, or milestone packaging must be decided. Use for planning and reviewing managed game work; do not use for an already scoped implementation or standalone asset request."
---

# Managed Game Production

## Purpose

Coordinate work that spans planning, research, asset production, implementation, review, or milestone decisions. Keep scoped implementation and standalone asset requests on their specialist skill paths.

Treat Codex output as a tested draft, not final creative authority. Keep human ownership over product goals, art direction, licensing, subjective quality, and release readiness.

## Entry Gate

Classify the request before creating plans or docs:

- **Standalone task**: the outcome and scope are already clear and one specialist can complete it. Route directly to that skill and stop orchestrating.
- **Managed project task**: the work spans stages, has unclear acceptance, replaces runtime assets, or needs coordinated handoffs. Continue with this skill.
- **Milestone or release task**: the work needs integrated validation, playtest review, asset promotion, or packaging. Continue with stricter evidence and human gates.

Do not invoke this skill merely because the task belongs to a game project.

## Work Modes

- `prototype`: default for personal development. Produce the smallest playable result and risk-appropriate evidence; avoid release-only process.
- `milestone`: integrate a meaningful playable slice, representative captures, core smoke coverage, and current-state docs.
- `release`: add full regression, rights/disclosure review, final asset promotion, and release-readiness decisions.

## Workflow

1. Inspect the existing project.
   - Read the user request, target `AGENTS.md`, current design/state docs, and established commands.
   - Reuse equivalent project structures instead of creating a parallel document tree.

2. Define one managed outcome.
   - Record player-facing outcome, in/out scope, acceptance criteria, required evidence, stop condition, and work mode.
   - Read `references/iteration-loop.md` when repeated iteration, phase sizing, playtest intake, or milestone state must be managed.
   - Use the same reference when a broad outcome must be split into implementable phases.

3. Route only required work.
   - Use `$game-reference-research` only when an external design decision needs evidence.
   - Use `$generate2dmap` only for required map, stage, layer, collision, placement, or scene-hook assets.
   - Use `$generate2dsprite` only for required sprites, props, FX, portraits, or cutout-character parts.
   - Use `$godot-2d-implementation` for concrete Godot scenes, scripts, data, imports, tests, and captures.

4. Define handoffs before production.
   - Give each producer intended use, style/context, dimensions or runtime constraints, acceptance criteria, output boundary, and rejected-output policy.
   - For managed generated assets, read `references/asset-lifecycle.md`.

5. Review evidence, not intentions.
   - Compare the result with acceptance criteria using relevant runtime behavior, tests, captures, playtest notes, or asset manifests.
   - Read `references/review.md` for player-facing, implementation, asset, or playtest review.

6. Decide the next state.
   - Choose keep, tweak, revert, split, promote, package, or stop.
   - Update only docs that remain useful as current project state or durable decisions.

## Minimal Project State

For a new managed project, prefer only:

- `AGENTS.md`: project commands, paths, forbidden edits, and done criteria.
- A vision document or equivalent: player-facing purpose and non-goals.
- A current-work document or equivalent: active outcome, scope, acceptance, and next step.
- Optional decision, asset-lifecycle, and evidence records only when the project needs them.

Read `references/project-scaffold.md` when creating or repairing this structure. Do not migrate a healthy existing project merely to match suggested paths.

## Hard Rules

- Do not expand a standalone task into a managed production cycle.
- Do not ask Codex to optimize an entire game in one pass.
- Do not silently overwrite accepted runtime or final assets.
- Do not let mechanical validation stand in for subjective art, UX, or release approval.
- Mark uncertain product/design changes as proposed instead of silently changing active rules.
- Preserve a rollback point for broad rewrites and asset promotions.
- Do not create a new review surface when an existing test, capture, or playtest artifact answers the question.

## Handoff Summary

| Direction | Minimum handoff |
| --- | --- |
| Research -> production | Findings, sources, confirmed vs inferred claims, prototype implications, open risks. |
| Production -> map/sprite | Intended use, style/context, runtime constraints, acceptance, lifecycle/output boundary. |
| Map/sprite -> implementation | Candidate paths, prompt/provenance, QC, manifest/state when managed, remaining review. |
| Production -> Godot | Outcome, scope, acceptance, target docs, accepted assets, required validation, stop condition. |
| Godot -> production | Changed files, validation evidence, captures/manifests, risks, and current maturity. |

## Output Contract

Report:

- Work mode and managed outcome.
- In-scope and out-of-scope work.
- Acceptance criteria and stop condition.
- Required skill handoffs.
- Evidence reviewed or still missing.
- Human decisions and material risks.
- Decision: keep, tweak, revert, split, promote, package, or stop.
