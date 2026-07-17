---
name: game-production-orchestrator
description: "Coordinate game work when a solo developer needs cross-system sequencing, ambiguous scope, mixed evidence, asset promotion, or milestone/release validation. Use only when coordination adds value; route clear implementation, asset, research, review, and review-plus-small-fix tasks directly to specialists."
---

# Managed Game Production

## Purpose

Coordinate only the game work that genuinely benefits from coordination. Optimize for playable progress, short feedback loops, and reversible decisions rather than process completeness.

## Solo-Developer Principles

- **Playable progress over paperwork.** Evidence and docs exist to unlock the next change.
- **One outcome at a time.** Prefer a coherent playable improvement over a broad plan.
- **Cheapest sufficient proof.** Match validation effort to the cost of being wrong.
- **Direct work by default.** A clear task should go straight to the specialist that can finish it.
- **Reversible autonomy.** Proceed with safe in-scope changes the user requested; pause only for a material creative fork, destructive action, external impact, or missing authority.
- **Taste is a choice, not a signoff process.** Present meaningful alternatives when needed, but do not invent approval gates for a personal project.

## Entry Gate

- Route a clear implementation, asset, research, review, or review-plus-small-fix request directly to the owning skill or short specialist sequence.
- Continue here only when scope is unclear, several systems or producers depend on one another, evidence lanes must inform one decision, accepted assets may be replaced, or a milestone/release needs integrated validation.
- Do not orchestrate merely because a task has two steps or belongs to a game project.

## Work Depth

- `prototype` is the default: make the smallest useful playable change and run focused validation.
- Use `milestone` only for an integrated slice that benefits from broader smoke and representative captures/playtest evidence.
- Use `release` only when the user is actually preparing a release; then add relevant regression, platform, rights, packaging, and disclosure checks.

## Workflow

1. **Inspect just enough.** Read the request, target `AGENTS.md`, relevant current state, and established commands.

2. **Define one outcome.** State the player-facing result, smallest coherent scope, what would show it worked, and when to stop. Read `references/iteration-loop.md` only for repeated iteration or milestone management.

3. **Route narrow subtasks.** Use only the required specialist skills. Keep ownership of the managed outcome here; give each specialist only its lane and ask it to return evidence and a result rather than rerouting the whole request.

4. **Implement and integrate.** Give a producer intended use, relevant constraints, acceptance, and output boundary. Read `references/asset-lifecycle.md` only when generated assets move between candidate and accepted runtime use.

5. **Review cheaply.** Use the smallest runtime behavior, test, capture, or feedback set that answers whether to keep the change. Read `references/review.md` only when several review surfaces or evidence lanes matter.

6. **Decide and stop.** Keep, tweak, revert, split, promote, package, or stop. Update an existing current-state document only when leaving it stale would mislead later work.

## Guardrails Worth Their Cost

- Do not expand a focused request into a production program.
- Preserve a rollback point for broad rewrites or replacement of accepted runtime assets.
- Do not turn mechanical checks into claims about fun, style, or market response.
- Keep human participants, synthetic runs, public comments, and telemetry populations distinct when counts influence a decision.
- Do not create a document, dashboard, formal signoff, or new review pass unless it reduces a real project risk.

## Handoff Summary

| Direction | Minimum handoff |
| --- | --- |
| Production -> specialist | Outcome, narrow task, relevant constraints, acceptance, existing inputs, and return target. |
| Specialist -> production | Result, changed/output files, evidence, material risk, and next recommendation. |
| Production -> evidence review | Question, build/scenario, source context, available evidence, and what decision it should inform. |
| Evidence review -> production | What worked, top findings, evidence, disagreement/unknowns that matter, and smallest next action. |

## Output Contract

Default to a short working update:

- outcome and current state
- work completed or next narrow step
- evidence that matters
- decision: keep, tweak, revert, split, promote, package, or stop
- one unresolved creative fork or material risk, only if it blocks useful progress
