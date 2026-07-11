# Map Pipeline Selection

## Contents

- Select The Mode
- Define Pipeline Axes
- Deliver The Smallest Playable Bundle
- Use Visual References Safely
- Handle Side-Scroll Stages
- Choose Runtime And Collision Models
- Apply Presets
- Control Cost

Use this reference only when the correct map pipeline is not already obvious. Select a product-level mode first, then define the visual, runtime-object, collision, and engine axes.

## Select The Mode

| Mode | Use for | Minimum output |
| --- | --- | --- |
| `tile_mode` | Editable RPG routes, towns, platform tiles, large maps, existing Tiled/LDtk/Godot/Unity tile workflows | Tileset, tile/object layers, collision, exits/zones, preview |
| `scene_mode` | Top-down showcase maps, tower defense, survivors arenas, foundation-plus-props scenes | Foundation, separate objects, placement, collision/zones, preview |
| `side_scroll_mode` | Platformers, runners, side-view action/shooters, brawlers | Scenery layers, playable geometry/objects, collision, hooks, camera bounds, preview |
| `grid_mode` | Tactical, factory, board/card, build-grid, terrain-cost scenes | Grid/cells, rules metadata, objects, collision, debug-readable preview |
| `room_chunk_mode` | Roguelike rooms, modular dungeons, procedural room networks | Chunks, sockets/exits, collision, spawns, seam check, layout preview |
| `baked_scene_mode` | Title screens, visual novels, fixed battle backgrounds, explicit flat images | One image and optional coarse zones |

Do not treat `hybrid` as a mode. Most playable maps combine visual art, runtime objects, and collision.

## Define Pipeline Axes

Record only the axes that affect output:

- `visual_model`: `baked_raster`, `layered_raster`, `tilemap`, `layered_tilemap`, or `parallax_layers`
- `runtime_object_model`: `none`, `separate_props`, `platform_objects`, `y_sorted_props`, `interactive_scene_objects`, `foreground_occluders`, or `scene_hooks`
- `collision_model`: `none`, `coarse_shapes`, `precise_shapes`, `tile_collision`, `polygon_walkmesh`, and/or `trigger_zones`
- `engine_target`: raw images plus JSON, Tiled, LDtk, Godot, Unity, Phaser, or the project's existing schema

Use the simplest combination that preserves editing, collision, occlusion, and interaction requirements.

## Deliver The Smallest Playable Bundle

A playable map, level, stage, room, prototype, or engine scene must not end as one flattened generated image.

- Top-down: ground/foundation, controlled objects, placement, collision, zones/exits, and spawn hooks.
- Side-view: scenery/parallax, playable geometry or walkable lane, collision, hazards/doors/checkpoints when present, camera bounds, and hooks.
- Tile/editor: tileset, tile/object layers, collision, zones, and native map/scene data.
- Rules-first grid: cells plus movement/build/resource rules and a logic-readable preview.
- Fixed non-playable scene: a baked image is sufficient.

Map-local static objects may remain in the map workflow when that is cheapest. Route reusable transparent props, animated objects, actors, or FX to `$generate2dsprite`.

For layered raster maps, read [layered-map-contract.md](layered-map-contract.md). For packed reusable objects, read [prop-pack-contract.md](prop-pack-contract.md). Do not duplicate those contracts here.

## Use Visual References Safely

Use an in-world reference mockup when separate runtime objects must form a coherent composition.

1. Save and view the exact foundation/background immediately before generation.
2. Tell image generation to use the image just shown and name the framing, horizon, terrain boundaries, entrances, exits, silhouettes, and landmarks that must stay fixed.
3. Ask for a natural in-world mockup, not an annotated diagram.
4. Keep non-visual data such as spawn markers, triggers, patrol hints, and camera bounds in metadata.
5. Limit a first pass to about nine distinct visible object candidates; repeat instances later through placement data.
6. Treat the mockup as planning evidence. Produce separate runtime objects/layers and a composed QA preview afterward.

Do not cut final props out of the dressed mockup or infer collision from its pixels. If the source image was not visible to the image model, stop and restore the reference handoff.

## Handle Side-Scroll Stages

Use one shared `stage_canvas` for the main scenery plates, stage reference, and QA preview. Default to the project camera aspect ratio; when unknown, use a practical 16:9 canvas.

Typical scenery stack:

- `sky`: atmosphere, near-static
- `far_bg`: skyline or distant terrain, slow
- `mid_bg`: readable landmarks, medium
- `near_bg`: near non-colliding scenery, faster
- optional `foreground_overlay`: fog, silhouettes, smoke, or framing above actors

Parallax art is scenery, not gameplay geometry. Keep floors, platforms, ladders, hazards, pickups, doors, checkpoints, gates, and collidable foreground pieces in separate runtime objects or tile layers. Record scroll factors, anchors, scale, repeat axis, and loop policy where relevant.

For brawlers, replace jump-platform geometry with a walkable belt polygon, enemy-wave zones, foreground/background props, and camera locks.

Reject a background that bakes in obvious foreground gameplay geometry. A full-stage image plus hitboxes is acceptable only when the user explicitly chooses that prototype tradeoff.

## Choose Runtime And Collision Models

- Use `y_sorted_props` when top-down actors pass in front of and behind tall objects.
- Use `platform_objects` for independent stage geometry and hazards.
- Use `interactive_scene_objects` for doors, pickups, switches, checkpoints, signs, exits, and destructibles.
- Use `scene_hooks` for metadata-only player/actor spawns, encounter areas, patrol hints, arena triggers, cameras, exits, and checkpoint ids.
- Use explicit blockers or walk regions; do not derive gameplay collision from PNG bounds.
- Preserve the project's existing engine schema instead of creating a parallel generic format.

## Apply Presets

| Request | Default axes |
| --- | --- |
| Fixed battle/menu background | `baked_scene_mode + baked_raster + none` |
| RPG exploration | `scene_mode + layered_raster + y_sorted_props + precise_shapes/trigger_zones` |
| Editable dungeon or large route | `tile_mode + layered_tilemap + tile_collision/trigger_zones` |
| Side-view action | `side_scroll_mode + parallax_layers + platform_objects/scene_hooks + explicit collision` |
| Tactical or factory grid | `grid_mode + tile/layered visual + rules metadata + tile/explicit collision` |
| Procedural rooms | `room_chunk_mode + chunks/sockets + explicit collision/spawns` |

## Control Cost

- Start with one representative room, route, or viewport before generating the full map set.
- Produce only layers and object classes that the runtime currently needs.
- Reuse existing schemas, tiles, and props when they meet the visual bar.
- Use one composed preview and focused metadata checks; do not build a custom review UI for a one-off map.
- Escalate from baked to layered or tile-based output only when editing, collision, occlusion, reuse, or scale requires it.
