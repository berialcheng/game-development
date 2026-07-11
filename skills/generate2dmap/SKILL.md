---
name: generate2dmap
description: "Generate and revise 2D game maps, stages, tilemaps, layered scenes, parallax backgrounds, collision plans, object placement, and map previews. Use when Codex needs map or level structure plus the visual and runtime data required to make it playable; use the lightest fitting pipeline, and do not use it for actor or animation assets."
---

# Generate 2D Maps

## Purpose

Create the smallest map bundle that satisfies the visual and gameplay need. A flat image is enough only for an explicitly non-playable background; playable maps need separate runtime structure such as layers, objects, collision, zones, or engine-native data.

This skill owns map composition, map-local static environmental props, placement, collision planning, scene hooks, and map previews. Use `$generate2dsprite` for actors, animation, FX, projectiles, or reusable asset-library sprites.

## Choose A Map Mode

| Need | Mode |
| --- | --- |
| Editable tile or grid map | `tile_mode` |
| Top-down/base scene plus separate objects | `scene_mode` |
| Side-view stage or parallax scene | `side_scroll_mode` |
| Tactical, factory, board, or rules-first grid | `grid_mode` |
| Reusable procedural rooms or chunks | `room_chunk_mode` |
| Fixed non-playable background or concept | `baked_scene_mode` |

Read `references/map-strategies.md` when genre, editability, or runtime structure does not make the choice obvious.

## Pipeline Axes

After choosing the mode, select only the axes the project needs:

- `visual_model`: baked raster, layered raster, tilemap, layered tilemap, or parallax layers.
- `runtime_object_model`: none, separate/y-sorted props, platform objects, interactive objects, foreground occluders, or scene hooks.
- `collision_model`: none, coarse/precise shapes, tile collision, walkmesh, or trigger zones.
- `engine_target`: raw canvas, Tiled, LDtk, Phaser, Godot, Unity, or project-native.

Prefer the project's existing format. Do not introduce a new editor or data model merely because the skill supports it.

## Standalone And Managed Output

- **Standalone request**: return the requested map assets, prompts/provenance for newly generated art, the minimum runtime metadata, and a useful preview. Do not create a production document tree.
- **Managed project**: follow the target project's asset policy and bundle layout. Keep source/reference/preview artifacts out of runtime imports, mark runtime candidates explicitly, and never write generated art directly to a final folder.

When the project has no asset policy, do not invent a release-grade approval system for a prototype.

## Workflow

1. Inspect the target.
   - Find viewport/camera size, map dimensions, perspective, coordinate system, render order, collision support, asset loading, and existing map format.
   - Preserve established project conventions.

2. Choose the lightest playable pipeline.
   - Select map mode and only the required pipeline axes.
   - Use `baked_scene_mode` only when the user wants a flat/non-editable result.

3. Produce visual assets.
   - Use built-in image generation for new visible art unless the user supplies existing assets or explicitly requests procedural placeholders.
   - Write creative prompts manually and save the exact prompt beside the generated source or in the project manifest.
   - Use code only for deterministic assembly, extraction, normalization, metadata, previews, or engine wiring.

4. Separate runtime structure.
   - For layered scenes, generate a foundation-only base before runtime-controlled objects.
   - For tilemaps, keep gameplay objects and collision as editable data rather than flattening them into the art.
   - For side-view stages, keep parallax scenery separate from platforms, hazards, doors, pickups, checkpoints, and collision.
   - Read `references/layered-map-contract.md` before producing layered raster maps.

5. Produce map-local objects when needed.
   - Use one-by-one generation for large, unique, wide, tall, or collision-aligned objects.
   - Use compact prop packs only for small static environmental props that share style, scale, and perspective.
   - Read `references/prop-pack-contract.md` before creating or extracting a prop pack.
   - Route actors, animated assets, FX, or reusable asset-library sprites to `$generate2dsprite`.

6. Write runtime metadata.
   - Record placement, render layer/order, collision, walk/build zones, exits, spawn markers, encounter/trigger zones, camera bounds, scroll factors, and chunk/grid fields only when relevant.
   - Keep collision independent from decorative pixels unless the target uses tile collision.

7. Validate and preview.
   - Check file existence, dimensions, alpha where expected, JSON/data parseability, referenced object paths, critical walkability, and chosen-mode requirements.
   - Compose one QA preview for layered output; do not turn every intermediate image into a review product.

## Visual Reference Rule

When a later image must preserve an existing base/background:

1. Save the exact base image.
2. Make it visible in the conversation immediately before generation; use `view_image` for a local file.
3. State which framing, terrain, horizon, entrances, exits, and landmarks must remain fixed.
4. Generate an in-world reference mockup, not an annotated diagram.
5. Treat the reference as planning evidence, then continue to separate runtime objects and metadata.

Do not rely on a path string as visual context, and do not ship a reference mockup as the runtime map unless the user explicitly requested reference-only output.

## Hard Rules

- Do not generate player, NPC, enemy, boss, projectile, or animation art as map deliverables.
- Do not ship a single baked image as a playable/editable map.
- Do not bake runtime-controlled objects into a foundation layer.
- Do not use scripts to procedurally draw requested final art.
- Do not infer collision, triggers, or spawn points from preview pixels when structured data is available.
- Do not use square prop packs for platforms, floors, bridges, walls, buildings, long hazards, or collision-critical objects.
- Do not stop at a dressed/stage reference when the request needs separate editable objects.
- Do not promote generated candidates to final art without the project's explicit human gate.

## Bundled Tools

Resolve these paths relative to this skill folder, not the target project's working directory:

- `scripts/extract_prop_pack.py`: extract alpha-cleaned compact prop sheets and emit `prop-pack.json`.
- `scripts/compose_layered_preview.py`: compose a base plus placement data into a QA preview/report.

## Output Contract

Report:

- Selected map mode and pipeline axes.
- Visual assets and saved prompt/provenance paths.
- Runtime objects, placement, collision, zones, and scene hooks produced.
- Managed-project manifest/runtime candidate paths when applicable.
- Validation performed and preview path.
- Missing engine integration, human review, or known risks.