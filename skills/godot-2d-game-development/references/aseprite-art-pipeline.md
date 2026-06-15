# Aseprite Art Pipeline Reference

Use this reference for 2D pixel-art assets, Aseprite source files, AI candidate images, SpriteFrames, and Godot imports.

## Source Asset Contract

- Treat `.aseprite` files as source assets.
- Treat exported PNG/JSON files as runtime outputs.
- Treat AI-generated images as candidates, not final runtime assets.
- Put bulk candidate folders behind `.gdignore` when Godot should not import them.

## Asset Spec Checklist

Define these before generating or editing character, UI, or VFX assets:

- Canvas size and frame size.
- Pixel scale and target gameplay zoom.
- Origin/pivot.
- Palette.
- Layer names.
- Animation tags.
- Frame count per tag.
- FPS and loop flags.
- Silhouette/readability notes.
- Shadow, weapon, FX, and foreground layer rules.
- Socket, hitbox, hurtbox, or anchor expectations.

## Repeatable Export

Prefer scripted or CLI export:

```powershell
& $ASEPRITE -b character.aseprite --sheet character.png --data character.json --list-tags
```

Do not trust the Aseprite process exit code by itself. Some local installs or wrappers can return success without running scripts or producing exports. After every CLI/script run, check expected output paths, file sizes, modification times, and JSON tag/frame content.

Source validation:

- `.aseprite` source file exists and has the expected canvas size, color depth, frame count, layers, cels, and tags.
- Tags are present and named as Godot expects.
- Frame counts match the spec.
- PNG dimensions match frame size and layout.
- JSON frame metadata can be consumed by the importer.
- Palette and layer constraints are preserved where the workflow requires them.

Runtime validation:

- Godot can load or regenerate `SpriteFrames`/`.tres` resources.
- Texture import uses pixel-art-safe filtering, usually nearest.
- Pivot/origin aligns with controller movement and collisions.
- Hitbox/hurtbox or weapon socket aligns on key frames.
- Animation FPS matches gameplay timing.
- Directional animation names follow the project convention.
- UI icons and world sprites do not share incompatible scale or padding assumptions.

## CLI Discovery And Fallbacks

- Search common install locations before assuming Aseprite is missing: PATH, `C:\opt`, Program Files, Steam libraries, Start Menu shortcuts, Scoop, Chocolatey, and WinGet locations.
- If a Steam shortcut points to `steam://rungameid/<id>`, use Steam `appmanifest_<id>.acf` and `libraryfolders.vdf` to find the real install folder.
- If Aseprite CLI is present but non-interactive script/export commands produce no output, keep a repeatable script in the project and report the CLI behavior. Use a lower-level source validator only when it actually proves the `.aseprite` structure needed by the task.
- Never claim an Aseprite export succeeded unless the exported PNG/JSON and source validation prove it.

## AI Candidate Intake

Use AI images only after defining the target spec. Reject candidates that fail:

- Stable silhouette at gameplay zoom.
- Consistent palette.
- Clean frame alignment.
- Matching facing direction.
- No stray pixels or merged layers that block editing.
- No unreadable pose when placed next to real enemies, UI, and effects.

When a candidate is promising, import it into a structured `.aseprite` template, then repair layers, palette, timing, pivot, and tags.
