# Game Design Audit Reference

## Contents

- GDD As Living Context
- Audit Questions
- Design To Implementation Contract
- Scope Control
- Phase-Based Output

Use this reference when reviewing a game idea, GDD, core loop, scope, balance, UI readability, effect feel, or milestone plan.

## GDD As Living Context

Prefer small files in `docs/design/` over one giant document:

- `GDD.md`: vision, fantasy, audience, constraints.
- `core_loop.md`: minute-to-minute loop, session loop, long-term loop.
- `combat.md`: player verbs, enemies, damage, difficulty, feedback.
- `progression.md`: XP, unlocks, economy, meta progression.
- `ui.md`: HUD, menus, accessibility, focus states.
- `art_direction.md`: resolution, palette, silhouettes, animation targets.
- `effects.md`: VFX/SFX/camera rules and readability budget.
- `test_matrix.md`: system-to-test mapping.

Each file should include implementation implications and validation criteria.

Every explicit demo promise should map to a proof surface in `test_matrix.md`, an automation scenario, a screenshot scenario, or a documented manual QA gate. If a promise cannot be verified, either narrow the promise or add the missing evidence path before claiming the slice is complete.

## Audit Questions

- What is the primary player verb?
- What makes a 30-second session interesting?
- What changes between minute 1 and minute 10?
- Which systems are data-driven and which are hardcoded?
- Which design assumptions can be tested with deterministic seed runs?
- What is the smallest playable slice?
- Which feedback layer tells the player what happened?
- Which UI states can fail with long text or large numbers?
- Can a new player identify the first useful action within 30 seconds without reading source docs?
- Do win and loss happen through real player/system paths rather than direct debug calls?
- Does each menu path have a reason to exist in the current demo, and does it recover to play?
- What must be human-approved before Codex can use it as a baseline?

## Design To Implementation Contract

Convert each design decision into an implementation contract:

```text
Design:
Player-facing outcome:
Systems touched:
Data/resource touched:
Effects/UI/audio touched:
Failure mode:
Validation artifact:
```

Example:

```text
Design: elite enemy should feel dangerous but fair.
Player-facing outcome: visible windup before charge, clear impact zone, recover window after miss.
Systems touched: enemy state machine, hitbox, cooldown, AI target selection.
Data/resource touched: enemy JSON, windup duration, charge speed, recovery time.
Effects/UI/audio touched: telegraph VFX, warning sound, camera nudge on impact.
Failure mode: charge feels unfair because the tell is hidden or too short.
Validation artifact: deterministic scenario screenshot at windup and impact; data test for cooldown.
```

If a design request lacks a contract, create the smallest reasonable one before implementation.

## Scope Control

Prefer a narrow vertical slice over a broad feature list:

1. One player loop.
2. One enemy or obstacle family.
3. One reward/progression rule.
4. One HUD path.
5. One feedback layer for success/failure.
6. One deterministic validation scenario.

Treat new systems as backlog unless they strengthen that slice.

For Steam-demo-style slices, treat these as core scope once gameplay exists:

- title menu with replayable/custom run start
- first-minute onboarding or route guidance
- pause/resume/settings
- save/continue when runs last long enough to justify it
- market/shop decision context if purchases exist
- victory, failure, retry, and main-menu return
- screenshots or manifests for the important visible states

## Phase-Based Output

Prototype output:

- Fast idea summary.
- Disposable assumptions.
- What to throw away if the idea fails.

Vertical-slice output:

- Contract for the slice.
- Systems/data/effects touched.
- One validation scenario.
- Risks that block playability.

Production output:

- Decision summary.
- Data/schema implications.
- Test and screenshot implications.
- QA gate.
- Next implementation slice.
