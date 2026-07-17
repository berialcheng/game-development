---
name: game-reference-research
description: "Research public games, store pages, media, reviews, and community discussions to answer a concrete design question and produce practical prototype implications. Use for external references or public player commentary; prefer the smallest useful source set. Do not use for current-build review or first-party feedback."
---

# Game Research

## Overview

Turn public external evidence into a faster design decision for a solo developer. Research only as far as needed to choose, prototype, or avoid a mistake.

## Solo-Developer Defaults

- Start with one question, not a broad market report.
- Use the smallest credible source mix that can answer it.
- Prefer findings that change a prototype, UI, mechanic, or production choice.
- Cite decision-driving claims; do not turn link collection into the deliverable.
- Stop when additional sources are unlikely to change the next action.

## Routing

- Continue here for public store pages, reviews, forums, social posts, streams, guides, and community media.
- Send user-supplied first-party or private human feedback to `$synthesize-playtest-feedback`.
- Send current-build synthetic or non-participant runtime review to `$synthetic-gameplay-review`.
- Ask about uncertain origin only when it changes attribution or routing; otherwise proceed with a caveat.
- If the user supplies a fixed set of public comments, analyze that set first. Expand the search only when requested or needed to answer the question.

## Workflow

1. **Frame the decision.** Identify the game/reference, platform when relevant, the design question, and the next choice this research should unlock.

2. **Gather only useful layers.**
   - Steam/store structured data and official page text: read `references/steam-sources.md`.
   - Screenshots, trailers, and interaction evidence: read `references/media-analysis.md`.
   - Reviews, community screenshots, discussions, and player sentiment: read `references/player-sources.md`.

3. **Extract decision-driving facts.** Use official sources for intended mechanics, rendered media for visible interaction and presentation, and public comments for reported experiences. Distinguish observation from inference where it matters.

4. **Translate to the project.** State what to borrow as a principle, what not to copy, likely production cost, and the cheapest prototype or comparison that would test the idea. Use `references/design-breakdown.md` only for broad or multi-game work.

5. **Stop with a decision.** Lead with useful findings, provide the few sources that support them, and name the next action or remaining uncertainty.

## Evidence Rules

- Official store text can support claims about intended mechanics, features, genre positioning, and marketing promises.
- Official screenshots can support claims about visible UI, art direction, camera, screen density, and likely game states.
- Trailers and gameplay videos can support claims about timing, interactions, animation, feedback, transitions, and pacing.
- Reviews and discussions can support claims about player-perceived pain points or delight, not the exact implementation.
- Public comments can reveal themes and examples, not population prevalence. Use wording such as `several reviewed comments`, not a player percentage, unless a valid denominator exists.
- Do not infer that separate posts represent separate people when identity is unclear.
- Community screenshots are useful for real play states and late-game complexity, but label them as UGC.
- Do not copy assets into a project as runtime art unless the user explicitly has rights. Use them as references and cite their source.

## Output Shapes

For a single game, use only the fields relevant to the question:

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

For an actual multi-game comparison, use a compact table:

```text
Game | Sources | Core loop | Distinct mechanic | UI reference | Progression | Risk/lesson
```

For implementation or managed production, finish with `finding -> project implication -> cheapest test`. Do not create or update planning documents unless they already exist and would otherwise become misleading.

## Validation

- Verify identity, version, and source only to the degree the claim depends on them.
- When using Steam APIs, confirm the app id and successful response; fall back to the rendered page if needed.
- Check media links only when they are part of the evidence or intended reference set.
- Avoid treating "could not find evidence" as proof that a feature does not exist.
