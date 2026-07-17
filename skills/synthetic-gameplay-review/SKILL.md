---
name: synthetic-gameplay-review
description: Play or inspect a current build through synthetic player lenses and turn observable friction into small, testable improvements. Use for AI-controlled play or developer-supplied non-participant runtime evidence. May continue into a scoped fix when requested; never present synthetic observations as human feedback.
---

# Synthetic Gameplay Review

## Purpose

Shorten the loop from playable evidence to a better build:

```text
play or inspect -> find costly friction -> choose a small change -> replay
```

Optimize for a solo developer's decision speed. This is a design stress test, not a substitute for real-player research.

## Solo-Developer Defaults

- Ask one useful question and use the smallest pass that can answer it.
- Reuse the playable path, captures, logs, and notes that already exist. Do not create a report surface by default.
- Keep only evidence needed to reproduce a problem or protect a useful behavior.
- Return at most three high-leverage changes unless the user asks for a broad audit.
- Increase rigor only for a blind-first-use study, repeated-run comparison, disputed conclusion, milestone, or release decision.

## Routing

- Use direct play when a safe control path exists; otherwise inspect current-build recordings, captures, logs, or synthetic telemetry.
- Send supplied first-party human feedback to `$synthesize-playtest-feedback` and public external commentary to `$game-reference-research`.
- Ask about unknown provenance only when it would change the route or conclusion; otherwise proceed with a short caveat.
- If the user asks only for review, do not edit the project.
- If the user asks for review and a small scoped fix, use `$godot-2d-implementation` for the implementation portion and continue without adding orchestration merely because the task has two steps.
- Use `$game-production-orchestrator` only for unclear scope, cross-system work, competing hypotheses, mixed evidence decisions, or a managed milestone.

Do not claim to have played when only reviewing evidence. Do not use this skill for source-only critique or automated regression.

## Fast Loop

1. **Frame the pass.** Record the question, build/scenario, mode, and any constraint that changes interpretation.
2. **Play or inspect.** Follow visible information and normal controls. Note only decision-relevant actions, outcomes, retries, dead ends, recovery, and payoff.
3. **Diagnose.** Separate observation, likely cause, and smallest testable improvement. Use a player lens only when it changes how the scenario is approached.
4. **Prioritize.** Prefer blockers, repeated high-cost friction, visible regressions, and cheap high-impact improvements. Preserve intentional difficulty and useful payoff.
5. **Act or hand off.** When implementation is requested, make the smallest reversible fix, validate it, and replay the affected path. Otherwise provide an implementation-ready next action.
6. **Stop.** End when the question is answered or the next change is clear; do not turn a focused pass into a general design audit.

Read [references/session-method.md](references/session-method.md) for blind passes, multiple runs, recording review, or a deeper report.

## Evidence Guardrails

- Ground material findings in a reproduction step, checkpoint, capture, clip, or metric. Formal IDs are optional for a small pass.
- Multiple lenses are heuristics, not independent testers. Repeated runs may be reported as `x/y synthetic runs` under the named scenario, never as a player percentage.
- Do not invent quotes, emotion, enjoyment, accessibility lived experience, retention, or purchase intent.
- Separate environment or control failures from game failures.
- Treat source knowledge learned after the pass as diagnosis, not retroactive player evidence.

## Default Output

Keep the response compact:

- question and short verdict
- what worked and should be preserved
- top findings: observation -> impact -> evidence -> change or next test
- change made and replay result, or the single best next action
- real-player validation only where synthetic evidence cannot answer the question
