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

For prototype work, define only:

- player-facing result
- smallest coherent change
- cheapest evidence that would show improvement
- stop condition

Add explicit in/out scope, failure analysis, or broader acceptance only when ambiguity or cost makes it useful. If the next change is already clear, start without creating a planning document.

## Loop

```text
define -> implement -> validate -> review -> decide
```

1. **Define** the smallest coherent change that can prove or disprove the current hypothesis.
2. **Implement** only the agreed scope.
3. **Validate** the likely failure with the cheapest sufficient check.
4. **Review** runtime behavior, captures, playtest notes, or asset evidence against acceptance.
5. **Decide** keep, tweak, revert, split, promote, package, or stop.

Do not add a phase merely to create another evidence surface. A phase should change player value, production readiness, or a meaningful risk.

## Phase Sizing

A useful phase usually:

- has one observable outcome
- touches a coherent set of systems
- can be validated without proving the whole game
- leaves a playable or safely reversible state
- has an obvious stop condition

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
- Present remaining release risks clearly; the user decides whether to ship.

## Playtest Intake

Record only what changes a decision: build/scenario when relevant, the observation or short quote, enough source context to interpret it, and the resulting change or test.

Use `$synthesize-playtest-feedback` when first-party human material needs theme synthesis or meaningful counting. Keep participant, synthetic-run, public-comment, and telemetry counts separate only when counts affect the decision. Compare what each lane says about the same hypothesis; do not normalize incompatible evidence into one score.

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
