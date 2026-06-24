# Sprite Pipeline

Use this reference for Codex-assisted sprite, icon, placeholder, atlas, and animation workflows.

## Stable Pipeline

```text
style bible -> placeholder sheet -> human review/cleanup -> validation/import -> in-game screenshot -> final promotion
```

Codex is useful for placeholders, specs, validators, import scripts, atlas automation, and QA. Do not make Codex the sole final art director.

## Sprite Style Bible Fields

```text
Global:
- Camera/view: top-down, side-view, isometric.
- Tile size.
- Character frame size.
- Background: transparent or solid.
- Outline: none / 1px dark / colored.
- Palette: constraints and contrast.
- Shading: flat, 2-tone, painterly, no noisy gradients.
- Pivot: bottom center, center, custom anchor.
- Padding: pixels between frames.
- Export format.

Animation:
- idle: frame count and FPS.
- walk/run: frame count and FPS.
- attack: frame count and FPS.
- hurt/death: frame count and FPS.

Naming:
- enemy_slime_idle_00.png
- enemy_slime_idle_01.png

Restrictions:
- Do not imitate named living artists.
- Do not use copyrighted characters as references.
- Generated assets go to generated placeholder folders.
- Final assets require human review.
```

## Placeholder Prompt Shape

```text
Create a placeholder sprite sheet spec for enemy_slime.

Use docs/working/sprite_style_bible.md.

Requirements:
- 32x32 per frame.
- Transparent background.
- Bottom-center pivot.
- 2px padding.
- idle 4 frames.
- hop/walk 6 frames.
- attack 6 frames.
- hurt 3 frames.
- death 8 frames.
- Readable silhouette at gameplay zoom.
- No copyrighted character references.
- No named living artist style.

Save to assets/generated_placeholders.
Update docs/ai_asset_register.md.
Do not modify assets/final.
```

## Validation Script Checklist

Ask Codex to write validators for:

- File naming convention.
- Transparent background when required.
- Frame dimensions.
- Animation frame counts.
- Padding.
- Duplicate/missing frames.
- Pivot metadata or import settings.
- Wrong folder usage, especially generated art in final folders.
- Atlas grouping and texture bleeding risk.

## Promotion Rules

- Placeholder art can prove gameplay and UI rhythm.
- Final art needs human aesthetic approval and rights review.
- Keep AI/generated provenance in `ai_asset_register.md`.
- Do not hide generated content provenance if it may be relevant to platform disclosure or team handoff.
