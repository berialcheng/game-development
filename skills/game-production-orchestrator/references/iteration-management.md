# Iteration Management

Use this reference when a game feature, UX flow, sprite, combat feel, menu, onboarding path, balance rule, or content system needs repeated improvement rather than one-shot completion.

## Core Loop

```text
Goal -> Hypothesis -> Phase Plan -> Implement -> Validate -> Playtest/Review -> Analyze -> Update Docs -> Decide Next Step
```

For player-facing work, a phase is not final by default. A phase creates evidence for the next decision.

## Iteration States

- `idea`: not committed to the build yet.
- `prototype`: quick version to test direction.
- `playtestable`: stable enough for human testing.
- `candidate`: likely direction, needs polish.
- `approved`: accepted for the current milestone.
- `final`: release-ready unless a later regression appears.
- `deprecated`: replaced by a newer decision.

## Each Iteration Must Produce

- Updated docs or an explicit "docs unchanged" note.
- Changed code/assets, if any.
- Validation result or a named validation gap.
- Playtest notes, review findings, screenshot, manifest, or other evidence.
- Decision: keep, tweak, revert, split, promote, or package milestone.
- Next iteration task list.

## Documentation Lifecycle

Use docs as living production artifacts.

Doc statuses:

- `draft`: early idea.
- `proposed`: suggested change, needs human approval.
- `active`: current working rule.
- `testing`: being validated through implementation/playtest.
- `approved`: accepted for current milestone.
- `final`: release-ready.
- `deprecated`: no longer valid.
- `superseded`: replaced by a newer doc or decision.

Only `active`, `approved`, and `final` docs are strong constraints. Treat `draft`, `proposed`, and `testing` as context. Do not use `deprecated` or `superseded` docs as authority unless explaining history.

Suggested frontmatter:

```md
---
status: proposed
owner: human
last_updated: 2026-06-21
source: playtest-003
supersedes:
next_review:
---
```

## Doc Change Protocol

Before changing docs:

- Identify whether the doc is a stable rule, working design, evidence, or output.
- Do not overwrite active/final decisions without explaining why.
- Mark uncertain design changes as `proposed`.

After changing docs:

- List every changed doc.
- Explain why it changed.
- Link it to implementation, playtest, review, research, or validation evidence.
- Update `docs/iteration_log.md` when the project has one.
- Mark old decisions as deprecated or superseded when needed.

## Iteration Log Template

```md
# Iteration Log

## Iteration 001: Inventory Tooltip First Pass

Date:
Build:
Related docs:
- docs/working/implementation_details.md
- docs/working/ux_principles.md
- docs/working/ui_flow_inventory.md

Goal:

Hypothesis:

Changes:

Docs Updated:

Validation:
- Tests:
- Screenshot:
- Manual check:

Playtest or Review Result:

Decision:
- keep / tweak / revert / split / promote / package

Next Iteration:
```

## Iteration Decision Table

```md
| Area | Evidence | Decision | Docs to update | Implementation task | Status |
|---|---|---|---|---|---|
| HUD health feedback | Player missed damage twice | Increase hit flash and add sound | ux_principles.md, ui_flow_inventory.md | Add damage flash pass | proposed |
| Tooltip position | Tooltip covers items | Clamp near screen edge | implementation_details.md | Update tooltip layout | active |
| Slime sprite | Silhouette unclear at 1x zoom | Stronger outline | sprite_style_bible.md, ai_asset_register.md | New placeholder pass | testing |
```

## Milestone Output

A milestone is not just code. A milestone output should include:

- Playable build or runnable project state.
- Active/final docs.
- Changed files summary.
- Asset manifest.
- AI asset register updates.
- Validation summary.
- Playtest summary.
- Known issues.
- Next milestone recommendations.

Suggested folder:

```text
outputs/
  milestone_001_vertical_slice/
    build_manifest.md
    release_notes.md
    final_decisions.md
    known_issues.md
    validation_summary.md
    playtest_summary.md
    asset_manifest.md
    screenshots/
```

## Do Not

- Treat first implementation as final.
- Rewrite multiple systems without a rollback plan.
- Change UX direction without updating docs.
- Promote placeholder assets to final without review.
- Continue indefinitely without exit criteria.
