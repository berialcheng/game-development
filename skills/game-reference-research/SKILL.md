---
name: game-reference-research
description: "Game reference and competitor research workflow. Use when researching Steam pages, trailers, screenshots, community feedback, reference games, UX patterns, mechanics, visual direction, and prototype implications before production planning."
---

# Game Research

## Overview

Use this skill to turn public game pages, media, and player-facing text into actionable game design research. Prefer evidence-backed conclusions over guesses from screenshots alone.

## Workflow

1. Define the research target.
   - Identify game name, app id or store URL, platform, genre, and the user's design question.
   - Separate goals such as "understand core loop", "collect UI references", "compare competitors", or "find mechanics for a prototype".

2. Gather source layers.
   - Steam/store structured data and official page text: read `references/steam-sources.md`.
   - Screenshots, trailers, and interaction evidence: read `references/media-analysis.md`.
   - Reviews, community screenshots, discussions, and player sentiment: read `references/player-sources.md`.

3. Extract design facts.
   - Record source URL, source type, and confidence for each claim.
   - Distinguish confirmed mechanics from inferred patterns.
   - Use official text for mechanics and goals; use screenshots/video for UI, visual hierarchy, pacing, and feedback.

4. Convert facts into a design matrix.
   - Use `references/design-breakdown.md` for the analysis fields.
   - Include core loop, player verbs, resources, progression, failure states, UI states, feedback, session structure, and production implications.

5. Report with provenance.
   - Lead with useful findings, not raw links.
   - Attach screenshot/media links only when needed and label official vs community/UGC sources.
   - State gaps that require trailer review, hands-on play, or human visual judgment.

## Evidence Rules

- Official store text can support claims about intended mechanics, features, genre positioning, and marketing promises.
- Official screenshots can support claims about visible UI, art direction, camera, screen density, and likely game states.
- Trailers and gameplay videos can support claims about timing, interactions, animation, feedback, transitions, and pacing.
- Reviews and discussions can support claims about player-perceived pain points or delight, not the exact implementation.
- Community screenshots are useful for real play states and late-game complexity, but label them as UGC.
- Do not copy assets into a project as runtime art unless the user explicitly has rights. Use them as references and cite their source.

## Output Shapes

For a single game, prefer:

```text
Game:
Sources checked:
Core loop:
Primary player verbs:
Interaction model:
UI states:
Progression/economy:
Combat/challenge:
Feedback/readability:
Visual direction:
Design takeaways:
Unverified gaps:
```

For competitor research, use a table with one row per game:

```text
Game | Sources | Core loop | Distinct mechanic | UI reference | Progression | Risk/lesson
```

## Output Contract For Game Production

When research feeds `$game-production-orchestrator` or implementation planning, output:

- Research summary.
- Source list with official/community labels.
- Reference games and what was observed.
- Confirmed mechanics vs inferred patterns.
- UX/design takeaways.
- Sprite/art-direction takeaways.
- Interaction and feedback takeaways.
- Risky assumptions that require trailer review, hands-on play, or human judgment.
- Prototype implications.
- Suggested docs to update:
  - `docs/vision/game_vision.md`
  - `docs/working/ux_principles.md`
  - `docs/working/sprite_style_bible.md`
  - `docs/working/implementation.md`
  - `docs/iteration_log.md`

Do not treat competitor patterns as final design decisions. Mark them as evidence, inspiration, or hypothesis.

## Validation

- Verify app id, game title, and source URLs before summarizing.
- Check that media links return a real image/video response when collecting assets.
- For Steam `appdetails`, confirm `success=true` and record screenshot/movie counts.
- If an endpoint fails, fall back to the rendered store page and report the failed endpoint.
- Avoid treating "could not find evidence" as proof that a feature does not exist.
