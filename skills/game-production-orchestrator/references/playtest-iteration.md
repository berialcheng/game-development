# Playtest Iteration

Use this reference to turn playtest notes into UX backlog and implementation tasks.

## Playtest Log Template

```md
# Playtest Log

## Session
Date:
Build:
Player:
Device:
Input:
Duration:

## Observations
- First death:
- First confusion:
- Did player understand goal:
- Did player notice damage:
- Did player open settings:
- Misclicks:
- Tutorial skipped or completed:

## Quotes
- "..."

## Metrics
- Time to first objective:
- Time to first damage:
- Death count:
- Menu opens:
- Inventory opens:
- Tutorial completion:
- Quit point:

## Issues
1.
2.
3.
```

## Codex Processing Prompt

```text
Read docs/evidence/playtest_log.md and turn it into a UX backlog.

Classify issues:
- Information unclear.
- Operation friction.
- Feedback insufficient.
- Difficulty/balance.
- Visual misleading.
- Performance.
- Bug.

Output:
1. Top 10 issues.
2. Severity.
3. Affected player goal.
4. Root cause hypothesis.
5. Low-cost fix.
6. Medium-cost fix.
7. Needs design decision.
8. GitHub issue-ready task.
9. What next playtest should verify.
```

## Iteration Rules

- Do not optimize from a single anecdote unless it blocks play.
- Look for repeated confusion across sessions.
- Preserve direct quotes as evidence, but convert them into testable hypotheses.
- Feed only the next highest-value phase into implementation.
- After fixes, update playtest questions and acceptance criteria.

## Required Updates After Playtest

After each playtest, update or explicitly mark unchanged:

- `docs/evidence/playtest_log.md` or the project's equivalent playtest log.
- `docs/iteration_log.md`.
- `docs/working/implementation_details.md`.
- `docs/working/ux_principles.md` if a UX rule changes.
- `docs/working/ui_flow_inventory.md` if a screen/state changes.
- `docs/working/sprite_style_bible.md` if art direction changes.
- `docs/output/known_issues.md` or the milestone known-issues file when unresolved issues remain.

Do not let playtest findings live only in chat. Convert them into docs, issues, or explicit non-actions.
