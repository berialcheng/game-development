# Media Analysis

Use this reference for official screenshots, trailers, videos, GIFs, and image galleries.

## Screenshot Checklist

For each important image, record:

- Source URL and whether it is official or community/UGC.
- Game state: menu, onboarding, combat, shop, build mode, inventory, map, upgrade, result, late game.
- Camera/framing: top-down, side view, isometric, board/table, grid, free camera, fixed arena.
- Main player action visible.
- UI regions: top bar, side panel, bottom hotbar, contextual tooltip, modal, inventory, minimap.
- Resource displays: health, coins, food, cards, time, XP, deck, population, cooldowns.
- Feedback: damage numbers, highlights, outlines, particles, screen shake indicators, warnings, progress bars.
- Density: approximate count of units, cards, enemies, items, panels, or text blocks.
- Readability risks: overlapping text, tiny icons, low contrast, hidden danger, excessive effects.

## Trailer/Video Checklist

Screenshots show states; video shows transitions. Inspect video when the research question involves interaction or feel.

Record:

- Input model: click, drag, keyboard movement, radial menu, card stacking, auto-battle, direct control.
- Timing: cooldowns, production timers, day/night cycles, wave pacing, turn structure.
- Transitions: level-up, shop open, reward choice, card pack opening, combat start/end, failure.
- Animation and feedback: hit timing, pickup motion, telegraphs, UI confirmation, error states.
- Onboarding: first action shown, tutorial prompts, tooltip density, first reward.

## Inference Discipline

- Say "visible in screenshot" for direct observations.
- Say "likely" only when inferring from repeated visual patterns.
- Do not infer economy or progression depth from UI alone; confirm with store text, achievements, wiki, or hands-on play.
- Do not infer moment-to-moment controls from still images unless the UI explicitly shows controls.

## Capture Organization

For a local research folder, prefer:

```text
research/<game-slug>/
  sources.json
  media/
    official_00.jpg
    official_01.jpg
  notes.md
```

Keep source URLs in `sources.json` or notes. Do not strip provenance from downloaded media.
