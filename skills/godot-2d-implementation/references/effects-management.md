# Effects Management Reference

Use this reference for VFX, SFX, camera feedback, hit feel, damage numbers, particles, screen shake, trails, decals, shader flashes, and combat readability.

## Effect Intent First

Define the player-facing intent before editing:

- Signal: what should the player notice?
- Timing: when does it start, peak, and end?
- Priority: what must remain readable while it plays?
- Ownership: which system spawns and cleans it up?
- Validation: which capture, manifest, or scenario proves it works?

Do not add effects just because an event exists. Add effects to clarify state, impact, danger, reward, or control response.

## Feedback Stack

For combat or interaction feedback, consider the stack in this order:

1. Gameplay state: hit, miss, block, crit, heal, pickup, danger, cooldown.
2. Animation or pose change.
3. VFX: flash, impact sprite, particles, trail, decal, telegraph.
4. Camera: shake, zoom, follow lag, pause-frame.
5. UI: damage number, status icon, health bar response.
6. Audio: hit, crit, warning, pickup, confirm, fail.

Use fewer layers for low-importance events. Reserve stacked feedback for high-value player information.

## Readability Rules

- Keep enemies, projectiles, player hurtbox, and danger telegraphs visible during effects.
- Avoid damage numbers covering enemy tells or player position.
- Keep screen shake short and bounded; it should not break aim or UI reading.
- Use z-index/layering intentionally: telegraphs under actors, critical UI above effects, damage numbers above combat but below menus.
- Snapshot effect-heavy scenes in deterministic combat scenarios.

## Performance Budget

Define or infer budgets before adding high-volume effects:

- Max enemies on screen.
- Max projectiles on screen.
- Max damage numbers on screen.
- Max particles per effect and effect lifetime.
- Max dropped items or pickups.
- Target resolution and FPS.
- Pooling requirement for frequently spawned effects.

Prefer pooling or reusable scenes for frequent effects. One-shot instancing is acceptable for rare events.

## Cleanup Rules

- Effects must have a clear lifetime or completion signal.
- Camera shake and time scale changes must restore state.
- Audio cues should respect mix priority and not stack into noise.
- Effects spawned by deleted actors must clean up safely.
- Avoid hidden gameplay logic inside effect-only nodes.

## Validation

Minimum validation for effect-heavy changes:

- Headless startup for load errors.
- Deterministic showcase, combat screenshot, or short capture manifest for readability.
- Event count or manifest check when many effects can spawn.
- Active effect/damage-number counts when effects can stack.

Report subjective visual quality separately from objective checks.
