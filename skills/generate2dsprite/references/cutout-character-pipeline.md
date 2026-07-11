# Cutout Character Production

## Contents

- Choose Cutout Deliberately
- Define The Character Contract First
- Semantic Part Plan
- Generation Order
- Grip And Equipment Interfaces
- Neutral Assembly Gate
- Portrait Separation
- Bundle Contract
- Handoff To Engine Integration
- Failure Rules
- Cost Controls

Use this reference when a character needs replaceable body/outfit/weapon parts, paper-doll skins, skeletal animation, or Spine-compatible/runtime attachment data. Do not use it for an ordinary raster sprite sheet.

## Choose Cutout Deliberately

Use cutout when the runtime benefits from:

- multiple outfits or equipment combinations
- replaceable attachments and draw-order control
- skeletal pose reuse across skins
- independent weapon/grip/socket animation
- runtime correction without regenerating every animation frame

Prefer raster sheets when the character has few actions, no equipment swapping, and frame-authored motion/style is the primary goal.

## Define The Character Contract First

Before generation, record:

- gameplay view, scale, and target viewport size
- identity anchors: silhouette, face, palette, costume/material language
- neutral pose and body proportions
- semantic part inventory and front/back side
- parent bone/part, pivot, overlap allowance, slot, and draw order
- outfit/skin groups
- grip families, weapon sockets, attachments, and optional portrait role

Do not generate a pile of parts without an assembly contract.

## Semantic Part Plan

A typical plan may include:

```text
body:
  head, hair_back, hair_front
  torso, upper/lower arms, hands
  skirt/hips, legs, boots
outfit:
  torso, sleeves, skirt, cape, headpiece, aura
interfaces:
  hand_cast, hand_blade, hand_pole
  weapon, weapon_socket, optional effect_socket
```

Adapt names and granularity to the rig. Keep each part semantically isolated:

- no unrelated anatomy baked into outfit attachments
- enough overlap to avoid seams during expected rotation
- transparent padding for pivot/rotation
- consistent camera, scale, lighting, and identity
- left/right or front/back naming that matches runtime draw order

## Generation Order

1. Establish an approved full-character visual baseline at gameplay scale.
2. Define semantic parts, pivots, sockets, and draw order.
3. Generate body-part groups with the baseline visible as reference.
4. Generate outfit/skin groups separately.
5. Generate grip families and weapons/attachments separately.
6. Clean alpha and inspect each isolated part.
7. Build a neutral assembly before animation or engine promotion.
8. Correct source-generation failures before compensating with runtime offsets.

Generate small coherent groups rather than one giant sheet when semantic isolation or identity consistency would suffer.

## Grip And Equipment Interfaces

Hands are equipment interfaces, not ordinary decoration.

- Use distinct cast, blade, polearm, or project-specific grip families when one hand shape cannot support all equipment.
- Validate the hand with the weapon inserted, not only as an isolated PNG.
- Check handle visibility, finger occlusion, glove/sleeve width, wrist continuity, and socket reach.
- Keep hands and weapons separate when equipment must swap.
- Treat geometric alignment as a mechanical signal; actual pixels decide whether the grip looks connected.

## Neutral Assembly Gate

Before engine animation, assemble at least one complete character and verify:

- every required part exists and has alpha
- body/outfit identity remains coherent
- shoulder/elbow/wrist and hip/knee/ankle chains connect
- no visible gaps, duplicated anatomy, or impossible overlap
- pivots and draw order permit expected movement
- weapons and grip families can be attached without destructive image edits
- the full silhouette fits the intended camera framing

Neutral assembly proves part compatibility only. It does not prove true idle, action poses, or continuous motion.

## Portrait Separation

A full-body cutout scaled down is not automatically a readable HUD portrait.

When a portrait is needed, treat it as a distinct asset role and check at actual HUD size:

- both eyes and main facial features remain readable
- hair/headwear does not obscure the face center
- outfit identity appears through collar/headpiece/material cues
- weapon/aura layers do not cover the face
- variants preserve the same character identity

The portrait may share visual references and outfit palette, but it should have its own framing and acceptance gate.

## Bundle Contract

For a managed project, keep:

```text
source/       raw generations, exact prompts, visible references
processed/    alpha-clean parts and neutral assembly data
preview/      part contact sheet and neutral assembly review
asset-manifest.json
```

Useful manifest fields include:

- `asset_id`, `source_skill`, lifecycle state, intended use, art style
- semantic part records with path, dimensions, pivot, parent/slot, and side
- outfit/skin groups
- grip/weapon/socket relationships
- draw order
- source, processed, and preview files
- QC, human review, rights notes, and runtime candidates

Do not require this managed bundle for a one-off standalone asset.

## Handoff To Engine Integration

Provide:

- semantic part inventory and files
- neutral assembly and coordinate basis
- pivot/socket/draw-order data
- outfit/skin and grip/weapon mappings
- prompt/source provenance and rejected parts
- mechanical QC and unresolved visual questions
- lifecycle state and explicit runtime-promotion permission

Do not claim engine or animation validity from offline assembly alone.

## Failure Rules

- If a part contains mixed anatomy or unusable padding, regenerate it instead of hiding the problem in runtime offsets.
- If a grip passes geometry but looks detached, fail visual review and revise the grip/interface.
- If the face is unreadable at HUD scale, create a portrait asset rather than repeatedly enlarging the full-body cutout.
- If a candidate is only mechanically valid, keep it out of accepted runtime until in-engine review.
- Keep project-specific bone counts, weapon counts, sample rates, and motion thresholds in the target project.

## Cost Controls

- Validate one representative body/outfit/grip assembly before generating the full variant matrix.
- Reuse an accepted baseline and semantic contract across variants.
- Produce one contact sheet and one neutral assembly review by default.
- Add specialized boards only when they answer a distinct failure question.
- Generalize scripts only after a second project proves the interface is stable.
