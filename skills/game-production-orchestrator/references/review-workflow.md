# Review Workflow

Use this reference for Codex code review, UX review, and dual-agent workflows.

## Role Split

Developer Codex:

- Implements one phase.
- Runs tests/checks.
- Reports changed files, assumptions, and risks.

Reviewer Codex:

- Does not modify code unless asked.
- Reviews diff, behavior, UX states, input, accessibility, assets, performance, and untested assumptions.

Human:

- Owns final UX/product/art decisions.
- Playtests.
- Approves final assets and release disclosure.

## Review Prompt

```text
Review current diff only. Do not modify code.

Focus on:
- AGENTS.md violations.
- Gameplay regression.
- UI state bugs.
- Input/controller navigation.
- Tooltip/menu close edge cases.
- Sprite import, atlas, scale, pivot issues.
- Accessibility regression.
- Performance risk.
- Untested assumptions.

Output:
- P0 must fix.
- P1 should fix before merge.
- P2 useful improvement.
- P3 optional.
- Human-playtest questions.
```

## Review Rules

- Lead with findings, not summary.
- Cite files and lines when available.
- Prefer concrete repro steps or state transitions.
- Treat missing tests/screenshots as risk, not proof of failure.
- Do not block on subjective art taste unless there is a stated baseline.

## Rollback Discipline

- Prefer one phase per commit.
- Keep broad refactors separate from feature work.
- If a phase changes many ownership boundaries, stop and request human approval.
- Keep generated placeholders separate so they can be removed without touching final assets.
