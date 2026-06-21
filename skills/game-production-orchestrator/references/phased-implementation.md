# Phased Implementation

Use this reference when asking Codex to implement game features.

## Phase Contract

Each implementation phase should define:

- Iteration state: idea, prototype, playtestable, candidate, approved, final, or deprecated.
- Goal: player-facing outcome.
- Hypothesis: what this phase is trying to prove.
- Scope: exactly what changes.
- Non-scope: what not to touch.
- Constraints: engine, architecture, UI, asset, and data rules.
- Acceptance criteria: observable pass/fail behavior.
- Validation: tests, startup, screenshot, automation, or manual playtest.
- Docs to read and docs that may need updates.
- Stop condition: stop after this phase and report, do not continue.

## Good Prompt Shape

```text
Implement Phase 1 only.

Goal:
- Add item tooltip basics for inventory hover/focus.

Scope:
- Tooltip panel.
- Item name, rarity, description, stat changes.
- Mouse hover and controller focus.

Non-scope:
- No animation.
- No localization.
- No inventory architecture rewrite.
- Do not modify final art.

Acceptance:
- Hover shows tooltip.
- Mouse leave hides tooltip.
- Controller focus updates tooltip.
- Empty slot shows no tooltip.
- Closing inventory hides tooltip.

Validation:
- Run existing UI/game tests.
- Capture or inspect one screenshot/state if available.
- Report changed files, assumptions, risks.
- Stop after Phase 1.
```

## Anti-Patterns

- "Improve the whole UX."
- "Make all sprites final quality."
- "Refactor the whole inventory while adding one tooltip."
- "Keep going through all phases unless I stop you."
- "Use whatever art looks good."

## Execution Rules For Codex

- Read existing project structure and rules before editing.
- Identify docs that may need updates before editing.
- Prefer existing patterns over new abstractions.
- Keep one phase reviewable.
- Add data tables or resources for tunable content when practical.
- Validate with the strongest available command.
- Report missing validation infrastructure instead of pretending confidence.

## Implementation Docs Split

`implementation.md` is the roadmap:

- Milestones.
- Phase list.
- Rough ordering and dependencies.
- No deep implementation details.

`implementation_details.md` is the current work order:

- Current phase only.
- Status.
- Related iteration.
- Goal, hypothesis, scope, non-scope.
- Acceptance criteria.
- Validation plan.
- Docs to update.
- Likely files to touch.
- Stop condition.
