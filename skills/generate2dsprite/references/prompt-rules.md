# Prompt Rules

## Contents

- Core Prompt Contract
- Match Style And References
- Control Layout And Containment
- Describe Motion
- Separate Hero Actions And FX
- Choose Sheet Shapes
- Build Bundles
- Quick Prompt Pattern

Use this file when writing image-generation prompts by hand. Keep creative prompting agent-written; use scripts only for deterministic postprocessing or compatibility with an older workflow.

## Core Prompt Contract

For chroma-key sheets, state:

- background is solid flat magenta `#FF00FF`, with no gradient
- exact row and column count
- no text, labels, UI, speech bubbles, borders, or visible cell guides
- one stable asset identity, bounding-box scale, and anchor convention
- the entire subject, weapon, trail, or effect fits inside each cell with magenta margin
- no element crosses a cell edge

Raw sprite art must come from built-in image generation or user-supplied art. Do not substitute code-drawn placeholder geometry for final visual assets.

If detached FX are unwanted, prohibit them. If required, keep them close enough to the subject to remain contained, or generate them separately.

## Match Style And References

Choose style from the request, the target project, or a visible map/asset reference:

- `clean_hd`: clean hand-painted HD, crisp silhouette, smooth surfaces, low noise, controlled lighting, no chunky pixels
- `pixel_inspired`: modern pixel-inspired readability without forced 16-bit wording or heavy dithering
- `retro_pixel`: explicit 16-bit/retro pixel treatment only when requested
- `project-native`: match the visible existing asset or map

When a reference matters:

1. View or attach the exact image immediately before generation.
2. Say to use the image just shown as the visual reference.
3. Name invariants: silhouette family, palette, face/markings, costume, accessories, materials, and scale.
4. Name allowed changes: pose, action phase, progression trait, or effect intensity.
5. Preserve the chroma-key and containment contract.

A path or filename alone is not a visual reference.

## Control Layout And Containment

Use a layout guide only when prior generations drift in spacing, scale, or edge safety. It is helpful for prop packs, tileset-like atlases, fixed-row atlases, and long non-directional sequences; it may reduce pose clarity in four-direction locomotion.

When using one, state that it is layout-only and must not appear in the result: no boxes, marks, labels, borders, or guide background.

Keep each subject at a consistent readable scale. For large creatures or effects, reserve extra cell margin before increasing detail. If a wide effect makes the body visibly smaller than the accepted idle/run asset, split the effect into its own sheet.

## Describe Motion

Describe phases, not just an action name:

| Action | Useful phases |
| --- | --- |
| idle | neutral, weight/aura change, accent, loop return |
| cast | ready, gather, stronger gather, release, peak, settle |
| attack | wind-up, strike, follow-through, recovery |
| hurt | impact, recoil, stagger, recovery |
| projectile | stable direction with small loopable energy/shape changes |
| impact/explosion | contact, expansion, peak, fade |
| walk/run/hover | grounded stride, bob, crawl, slither, or glide with explicit direction |

For a long sequence, state reading order: left-to-right across each row, then the next row. Keep identity stable while only pose and controlled effects change.

## Separate Hero Actions And FX

Do not ask one raw sheet to contain unrelated hero actions merely because the engine expects a `4x4`, `5x5`, or custom atlas.

For controllable or high-value characters:

1. Generate idle, locomotion, attack, cast/shoot, hurt, and death as separate coherent sheets.
2. Keep projectile, muzzle flash, slash arc, weapon trail, impact, and dust separate when they would expand the body bounding box.
3. QC feet line, body center, scale, silhouette, anchor, and edge safety per action.
4. Assemble the engine atlas only after the source actions pass.

A raw multi-row sheet is appropriate for one directional locomotion family, one continuous action, a prop/tileset pack, or a low-stakes compact enemy atlas. The assembled atlas is a delivery artifact, not necessarily the image-generation target.

## Choose Sheet Shapes

| Shape | Default use | Prompt detail |
| --- | --- | --- |
| `2x2` | four-phase idle, attack, hurt, impact | Name all four phases |
| `2x3` | six-phase cast or compact action | Order anticipation through settle |
| `3x3` | large idle/showcase or nine-object pack | Keep subject around 55–65% of each cell when edge safety is difficult |
| `4x4` directional | four directions x four locomotion phases | Rows: down, left, right, up; columns: neutral, step, neutral, opposite step |
| `4x4` sequence | one 16-frame non-directional action | State row-major reading order and phase progression |
| `1x4` | projectile loop | Same direction/size; only internal pulse changes |
| `5x5` or custom | one coherent long sequence, prop pack, or tileset-like atlas | Avoid unrelated hero actions |

Try four-direction locomotion without a layout guide first. Add a guide only after a concrete grid or containment failure.

## Build Bundles

Write independent prompts for independent runtime roles. Common small bundles:

- caster, projectile, impact
- idle, locomotion, attack
- body action, weapon trail, impact
- map prop pack split by material or size family

Do not force unrelated assets into one generation merely to reduce call count; failed mixed sheets usually cost more to regenerate and normalize.

## Quick Prompt Pattern

1. State asset role, view, style, and exact sheet shape.
2. Describe identity and visible reference invariants.
3. Describe ordered motion or cell contents.
4. State scale, anchor, containment, and separation rules.
5. Restate solid magenta background and no-text/no-guide rules.
6. Name the intended postprocessing and runtime use when it affects framing.
