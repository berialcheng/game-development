# Design Breakdown

Use this reference to convert gathered evidence into actionable design notes.

## Core Fields

Game identity:

- Title, app id/store URL, developer, publisher, release date.
- Genres/tags and confidence.
- Comparable games suggested by tags or bundles.

Core loop:

- 10-second loop: immediate repeated action.
- 1-minute loop: short-term goal and reward.
- Session loop: what resets, escalates, or concludes.
- Long-term loop: unlocks, meta progression, collection, campaign, mastery.

Player verbs:

- Primary verbs: move, drag, place, stack, aim, shoot, choose, craft, sell, build.
- Secondary verbs: inspect, sort, pause, upgrade, combine, recruit, feed, repair.
- Automation: what happens without player input.

Systems:

- Resources and currencies.
- Units/entities/cards/items.
- Production/conversion rules.
- Combat/challenge model.
- Failure conditions.
- Randomness/drop tables/packs.
- Progression/unlocks/quests.

UI/UX:

- Persistent HUD.
- Contextual panels.
- Modal decisions.
- Inventory/card/grid layout.
- Feedback and error states.
- Input affordances and focus states.

Visual and feedback:

- Art style and palette.
- Camera and scale.
- Readability hierarchy.
- Combat or action feedback.
- Reward feedback.
- Warning/telegraph language.

## Confidence Labels

Use these labels in notes:

- `confirmed`: stated by official text/API or visible directly in official media.
- `observed`: visible in media, but not necessarily explained.
- `inferred`: reasonable interpretation from multiple signals.
- `player-reported`: from reviews/community/discussions.
- `unverified`: needs trailer, hands-on play, or another source.

## Implementation Takeaways

End research with practical implications:

- What to prototype first.
- What UI states must exist.
- What data tables are implied.
- What feedback/camera/audio needs validation.
- What scope should be deferred.
- What should not be copied because it is brand/art/IP-specific.
- Which project docs should receive the finding.
- Whether the takeaway is a design decision, a prototype hypothesis, or only a reference.

## Example Mini Output

```text
Core loop: confirmed by store text. Drag/stack cards to create resources, sell cards for coins, buy packs, expand village.
Interaction model: confirmed/inferred. Drag-and-drop card stacking is the primary input; automatic combat starts when villager and enemy cards collide.
Pressure: confirmed. End-of-Moon feeding requires enough food or villagers starve.
Prototype implication: implement draggable cards, stack recipes, periodic hunger check, coin/card-pack economy, and a small idea/recipe reveal system before adding large content volume.
```

## Production Handoff Template

```text
Research Handoff:
Source game(s):
Strongest evidence:
Confirmed mechanics:
Observed UX/UI patterns:
Useful visual references:
Prototype hypotheses:
Risks and unknowns:
Docs to update:
Suggested first phase:
Validation needed after implementation:
```
