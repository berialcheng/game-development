# Iteration Loop

## Contents

- Outcome Contract
- Loop
- Phase Sizing
- Prototype, Milestone, Release
- Playtest Intake
- Documentation Cost
- Decision Rules

Use this reference for managed work that needs more than one implementation/review pass. Do not use it for a scoped standalone task.

## Outcome Contract

Define one outcome with:

- player-facing result
- in-scope and out-of-scope work
- acceptance criteria
- likely failure
- validation level and evidence
- stop condition
- work mode: prototype, milestone, or release

If these are already clear, implementation can start without creating another planning document.

## Loop

```text
define -> implement -> validate -> review -> decide
```

1. **Define** the smallest coherent change that can prove or disprove the current hypothesis.
2. **Implement** only the agreed scope.
3. **Validate** the likely failure with the cheapest sufficient check.
4. **Review** runtime behavior, captures, playtest notes, or asset evidence against acceptance.
5. **Decide** keep, tweak, revert, split, promote, package, or stop.

Do not add a new phase merely to create another evidence surface. A phase should change player value, production readiness, or a meaningful risk.

## Phase Sizing

A useful phase:

- has one observable outcome
- touches a coherent set of systems
- can be validated without proving the whole game
- leaves a playable or safely reversible state
- has an explicit stop condition

Split work when unrelated systems, multiple subjective decisions, or several independent failure modes would make the result hard to review.

## Prototype, Milestone, Release

### Prototype

- Prefer a playable result over complete infrastructure.
- Update only current-state docs that would otherwise become misleading.
- Use focused validation; do not require release rights/final-art approval.

### Milestone

- Integrate a meaningful slice.
- Run core smoke plus representative visual/playtest evidence.
- Record remaining risks and the next milestone decision.

### Release

- Run full relevant regression and platform checks.
- Resolve rights/disclosure and final-asset decisions.
- Require explicit human release readiness.

## Playtest Intake

Record only evidence that can change a decision:

- build/version and scenario
- device/input when relevant
- observation or short quote
- reproduction steps
- severity/frequency
- expected vs actual behavior
- resulting decision or backlog item

Separate observations from proposed solutions. Prefer one reusable issue over repeating the same note across logs.

## Documentation Cost

Keep a short current-work record rather than an append-only narrative for every action:

```text
Outcome:
Scope:
Acceptance:
Evidence:
Decision:
Next or stop:
```

Use version control and milestone summaries for history. Create a durable decision record only for choices that future work could reasonably misunderstand or reverse accidentally.

## Decision Rules

- **Keep** when acceptance passes and no material risk remains.
- **Tweak** when the approach is sound and one focused change addresses the gap.
- **Revert** when the hypothesis failed or the change harms a stronger baseline.
- **Split** when failures are independent.
- **Promote** when a candidate meets the target project's runtime gate.
- **Package** when milestone/release evidence is sufficient.
- **Stop** when the requested outcome is achieved or the explicit stop condition is reached.
