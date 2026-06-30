# Asset Lifecycle

Use this reference whenever generated visual assets, imported source art, runtime candidates, or final art may cross skill boundaries.

## Lifecycle States

```text
asset brief -> generated bundle -> processed candidate -> accepted runtime candidate -> Godot integration -> human-reviewed final
```

Use these state names in manifests and reports:

- `raw_generated`: original image model output, prompt, reference handoff image, or layout guide output.
- `processed_candidate`: chroma-keyed, extracted, resized, split, composed, or previewed output that passed mechanical checks but is not yet imported.
- `accepted_for_runtime`: file selected for Godot import or runtime loading in the current prototype/vertical slice.
- `human_reviewed_final`: final art accepted by a human for quality, rights, and disclosure risk.
- `rejected`: output kept only as evidence, not used by runtime.

## Folder Contract

Prefer this layout when the target project does not already define an equivalent:

```text
assets/
  generated_placeholders/
    <asset_id-or-run_id>/
      source/          # raw image_gen outputs, prompts, references, layout guides, pipeline metadata
      processed/       # transparent sheets, frames, extracted props, cleaned map layers
      preview/         # GIFs, stage-reference, dressed-reference, layered previews, QA composites
      asset-manifest.json
      .gdignore        # recommended when Godot should not import source/preview in bulk
  runtime_candidates/
    sprites/
    maps/
    props/
    tilesets/
    fx/
  final/
  atlases/
```

Do not write generated candidates directly into `assets/final`. If a project already uses `assets/map`, `assets/props`, or another runtime folder, copy only `accepted_for_runtime` files there and keep the generated bundle intact.

## Prompt Provenance Gate

Missing `source/prompt-used.txt` is a provenance failure for generated visual assets. Do not promote an asset to `accepted_for_runtime` until the manifest lists the prompt file and the prompt file exists. If the prompt cannot be recovered, set the lifecycle state to `rejected` or keep it as a provenance-incomplete prototype and report the gap.

## Manifest Contract

Each generated asset run should produce or update `asset-manifest.json` with enough information for a later Godot/import step to work without guessing:

```json
{
  "asset_id": "warrior_run_v001",
  "source_skill": "generate2dsprite",
  "lifecycle_state": "processed_candidate",
  "intended_use": "player run animation candidate",
  "art_style": "pixel_art",
  "prompt_files": ["source/prompt-used.txt"],
  "source_files": ["source/raw-sheet.png"],
  "processed_files": ["processed/sheet-transparent.png"],
  "preview_files": ["preview/animation.gif"],
  "runtime_candidates": [
    {
      "path": "assets/runtime_candidates/sprites/warrior/run-sheet.png",
      "state": "accepted_for_runtime",
      "import_role": "SpriteFrames",
      "frame_size": [64, 64],
      "pivot": "bottom_center",
      "fps": 8
    }
  ],
  "qc": {
    "edge_touch": false,
    "frame_count": 4,
    "notes": "mechanical checks passed; human art review pending"
  },
  "human_review": "pending",
  "rights_notes": "AI-assisted candidate; no named artist or copyrighted character references"
}
```

For maps, include `stage_canvas`, `parallax_layers`, `object_metadata`, `collision_metadata`, and `preview_files` when relevant.

## Runtime Import Rules

Godot implementation should only import files that are listed as `accepted_for_runtime` in a manifest or explicitly selected by the user. Do not import these as runtime assets:

- raw image generation outputs
- prompt files and reference handoff images
- layout guides
- rejected outputs
- `dressed-reference`, `stage-reference`, `layered-preview`, GIFs, and other QA previews
- `pipeline-meta.json` unless it is consumed as evidence, not visual art

## Register Rules

Update `docs/ai_asset_register.md` when generated assets are added or changed. Link the register entry to the manifest instead of copying every file path when the bundle is large.

Update `docs/output/final_asset_register.md` only after human review promotes an asset to `human_reviewed_final`.

