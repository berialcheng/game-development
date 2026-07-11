# Cutout Character Validation

## Contents

- Preserve The Accepted Baseline
- Runtime Adapter Contract
- Validation Stages
- IK, Sockets, And Visual Contact
- Portrait And UI Context
- Mechanical Versus Human Gates
- Promotion
- Evidence And Cost

Use this reference when integrating or reviewing paper-doll, skeletal, Spine-compatible, or other semantic-part 2D characters in Godot. It assumes a cutout source bundle already exists.

## Preserve The Accepted Baseline

When replacing a working character:

```text
accepted baseline -> isolated candidate -> in-engine review -> explicit promotion -> rollback retained
```

- Keep the accepted character active while reviewing the candidate.
- Load candidate parts through an isolated adapter or review scene.
- Prevent candidate review scripts from writing accepted runtime files.
- Record source hashes and prepare a dry-run promotion/rollback plan before replacement.

For a new prototype with no baseline, treat the first mechanically valid character as a runtime candidate, not final art.

## Runtime Adapter Contract

Prefer data-driven adapter records over hardcoded offsets spread through GDScript. Record only fields the runtime uses, such as:

- coordinate basis and conversion rule
- bones/parents and local transforms
- semantic part/region paths
- slot and draw order
- skins/outfit groups
- pivots, sockets, grips, and attachments
- original offset, user correction, final offset, and review state
- runtime/candidate state and source hashes

Keep corrections layered so regenerated source data can be compared and corrections replayed.

## Validation Stages

### 1. Mechanical Intake

Check files, alpha, dimensions, part/slot references, skin completeness, draw order, pivots/sockets, and Godot load/import. Mechanical success does not approve visual quality.

### 2. Neutral Assembly

Render a complete character and inspect seams, duplicated/missing anatomy, outfit identity, attachment placement, and bounds. This proves assembly compatibility only.

### 3. Isolated Godot Stage

Render the candidate through the same adapter/renderer intended for gameplay while the accepted baseline remains unchanged. Compare at real viewport and character scale.

### 4. True Runtime Idle

Drive the same idle, equipment guard, secondary motion, framing, and attachment chain used by gameplay. Do not review a reset assembly and call it idle.

Check:

- silhouette and face readability
- weapon visibility outside the body silhouette
- support-hand/grip contact when intended
- outfit and attachment draw order
- safe stage bounds and nearby actor/UI occlusion

### 5. Action Extremes

Inspect representative windup, impact, and recover states through the real runtime action path. Check limb seams, face occlusion, weapon silhouette, body articulation, grip/release intent, and attachment visibility.

Static extremes prove pose separation, not smooth timing.

### 6. Continuous Motion

Sample ordered progress/time values or capture a short rendered sequence. Inspect and, when useful, measure:

- start/end stance closure
- adjacent wrapped rotation and position deltas
- unintended direction reversals
- alpha flicker or one-frame visibility drops
- phase weights returning to zero
- body/weapon continuity through anticipation, impact, follow-through, and recover
- weapon-specific tempo rather than one generic duration

Thresholds belong to the target project's scale, FPS, and style. Numerical continuity still requires human playback review.

### 7. Gameplay Context

Verify the character in the actual game state with camera, nearby actors, HUD, VFX, collision, and input. Review/debug overlays must not be mistaken for gameplay presentation.

## IK, Sockets, And Visual Contact

A zero-distance wrist/socket or grip target does not guarantee a convincing pose.

- Inspect the visible palm/glove, forearm, sleeve, and weapon handle together.
- Use two-hand contact when it improves the intended idle/guard.
- Allow deliberate support-hand release during attacks when forced IK stretches limbs or creates floating gloves.
- Define contact/release by action phase instead of enforcing one global constraint.
- Prefer an authored readable silhouette over mechanically perfect but visually broken contact.

## Portrait And UI Context

Review portrait assets at their actual HUD size, separately from the full-body runtime character. Confirm face readability, outfit identity, and that weapon/aura layers do not obscure the portrait.

## Mechanical Versus Human Gates

Automation can establish:

- file/reference completeness
- import/load success
- skin/slot/attachment coverage
- bounds/clipping and deterministic transforms
- scenario/capture production
- bounded continuity metrics

Human review decides:

- identity and facial readability
- material/style quality
- silhouette and grip credibility
- motion weight, rhythm, and appeal
- final-art and rights acceptance

Do not infer human approval from a passing manifest.

## Promotion

Before promotion:

- confirm candidate hashes and approval state
- verify the current accepted baseline and rollback location
- dry-run copy/update actions
- block final-art writes unless explicitly approved

After explicit promotion:

- update runtime references atomically
- rerun startup/import, true idle, representative action, and focused smoke
- confirm the previous baseline can still be restored
- report runtime acceptance separately from final-art acceptance

## Evidence And Cost

Default to the smallest evidence set that answers the current question:

- one part/neutral assembly review
- one true-idle matrix or representative set
- one action-extremes review when poses changed
- one continuous playback when timing changed
- one gameplay-context capture before promotion

Do not build a new dashboard, gallery, or browser approval surface for every candidate. A simple comparison board, GIF, manifest, and explicit user decision are normally sufficient for a personal project.
