---
name: generate2dsprite
description: "Generate and postprocess 2D game sprites, animation sheets, transparent props, FX, projectiles, portraits, and cutout or paper-doll character parts. Use when Codex needs image-generated visual assets plus deterministic cleanup, frame extraction, alignment, QC, or preview exports; keep engine integration separate."
---

# Generate 2D Sprites

## Purpose

Create the smallest useful 2D asset bundle from a natural-language request. Infer the asset plan, generate requested visual art with built-in image generation, and use bundled scripts only for deterministic cleanup, extraction, alignment, QC, and preview exports.

Keep engine integration separate. When working inside a managed project, hand accepted candidates to the engine implementation skill rather than wiring runtime code here.

## Choose An Asset Mode

| Need | Mode |
| --- | --- |
| One icon, portrait, prop, projectile, or static asset | `single_asset` |
| One coherent animated action | `action_grid` |
| Several related actions or related units | `asset_bundle` |
| Compact map-local or reusable prop set | `prop_pack` |
| Engine-required strip or mixed atlas | `delivery_atlas` after per-action QC |
| Replaceable body, outfit, grip, weapon, or attachment parts | `cutout_character` |

Read `references/modes.md` when sheet shape, frame count, bundle structure, or processor mode is unclear.

## Core Rules

- Use built-in image generation for every new raw visual asset. Do not replace requested art with Canvas, SVG, HTML/CSS, PIL shape drawing, procedural geometry, placeholder primitives, or code-rendered screenshots.
- Write the creative prompt yourself and save the exact prompt before generation. Treat missing prompt provenance as a failed managed bundle.
- Make any local visual reference visible with `view_image` immediately before generation; a path string is not visual context.
- Generate one coherent action or asset family per raw sheet. Build mixed engine atlases only after the component sheets pass QC.
- Use centered multi-row grids for animated bodies; keep body scale and the feet/bottom anchor stable. Generate detached or cell-expanding FX separately.
- Match the target project's art style before applying pixel-art defaults.
- Reject or regenerate frames that touch cell edges, drift materially in scale, lose identity, or break the requested motion/readability.
- Do not write generated candidates directly to a final-art folder.

Read `references/prompt-rules.md` for reference handling, containment, style, action, grid, and bundle prompt patterns.

## Workflow

1. Infer the smallest asset plan.
   - Identify asset type, action, view, art style, reference role, expected runtime use, and whether the result is standalone or managed.
   - Use separate action grids for a controllable hero or other high-value multi-action character.
   - Use cutout mode only when the runtime needs replaceable semantic parts, outfits, grips, weapons, or skeletal attachments.

2. Choose generation shape.
   - Prefer `2x2` for short four-frame body actions and compact grids for longer body sequences.
   - Keep canonical directional locomotion, coherent long actions, prop packs, and tileset-like atlases as explicit exceptions.
   - Use one-by-one or wide cells for important, irregular, wide, tall, or collision-aligned props.
   - Use square prop packs only for compact assets sharing style, perspective, scale, and quality bar.

3. Prepare provenance and optional layout guidance.
   - Create the output bundle before generation and write `source/prompt-used.txt`.
   - Use `scripts/make_layout_guide.py` only when slot geometry needs help. The guide may define spacing and padding, never creative style, and must not appear in final art.

4. Generate the raw image.
   - State exact sheet shape, identity/style constraints, containment, safe padding, and background/alpha workflow.
   - For referenced work, state what identity, silhouette, palette, costume, material, or style must remain fixed.

5. Postprocess deterministically.
   - Resolve script paths relative to this skill folder, not the target project's working directory.
   - Run `scripts/generate2dsprite.py process` with explicit input, target, mode, output directory, rows/columns, alignment, component policy, and `--prompt-file`.
   - Use `component-mode=largest` for body-only grids and `all` for deliberately detached FX/projectile/impact sheets.
   - Treat the legacy `build-prompt` subcommand as compatibility only; it is not the preferred creative workflow.

6. Review mechanical and visual QC.
   - Check frame count, alpha, edge touch, identity, scale, anchor, component filtering, action readability, and preview/GIF coherence.
   - Mechanical success does not establish final subjective quality.

7. Return the right bundle.
   - Standalone output: return the requested runtime-ready asset plus prompt and minimal QC/preview evidence.
   - Managed output: preserve source, processed, and preview artifacts; list runtime candidates explicitly in the target project's asset contract.

## Managed Bundle Shape

Use this only when the target project already has an asset lifecycle policy or the task explicitly establishes one:

```text
assets/generated_placeholders/<asset-id-or-run-id>/
  source/
  processed/
  preview/
  asset-manifest.json
```

Keep raw images, prompts, guides, GIFs, and QA previews as provenance/evidence rather than runtime art. Import only explicitly accepted runtime candidates.

## Cutout Boundary

Cutout production owns semantic source parts and neutral assembly evidence, not engine animation or runtime promotion. Plan body parts, outfit parts, grip families, weapons/attachments, pivots, sockets, and draw order before generation. Keep a full-body gameplay asset separate from any HUD portrait requirement.

Read `references/cutout-character-pipeline.md` only for cutout/paper-doll production. Keep project-specific bones, weapon counts, frame thresholds, and promotion tools in the target project.

## Bundled Tools

- `scripts/generate2dsprite.py`: chroma cleanup, frame extraction, alignment, scale normalization, component filtering, QC metadata, transparent sheet/frame output, and GIF export.
- `scripts/make_layout_guide.py`: deterministic grid-spacing and safe-padding guide.

## Output Contract

Report:

- Asset mode, action/view/style, sheet or part plan, and reference role.
- Raw source and exact prompt path.
- Processed runtime candidate paths and previews.
- QC results, rejected/regenerated output, and subjective review still needed.
- Managed-project manifest and lifecycle state when applicable.
- Engine integration still required.