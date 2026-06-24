# UX Review

Use this reference for game HUD, menus, onboarding, accessibility, and interaction audits.

## UX Audit Checklist

Player clarity:

- Does the player know the current goal quickly?
- Is the next useful action visible?
- Are dangerous states communicated before punishment?
- Are reward and failure causes clear?

Feedback:

- Does every action have response: visual, audio, haptic, animation, text, or state change?
- Is damage, healing, pickup, cooldown, invalid input, and confirmation visible?
- Are feedback layers readable under combat/effect load?

UI flow:

- Can the player enter and exit each screen predictably?
- What happens to gameplay while a panel is open?
- Does ESC/back/controller cancel behave consistently?
- Are empty, disabled, loading, error, pause, shop, level-up, and game-over states covered?

Input:

- Does keyboard/mouse work?
- Does controller focus work if supported?
- Are controls remappable or at least documented?
- Are hover-only interactions mirrored for controller/touch when needed?

Accessibility:

- Is text large enough at target resolution?
- Is contrast adequate?
- Is information conveyed by more than color?
- Can shake/flashing be reduced?
- Are subtitles/text speed/settings needed?
- Are audio cues backed by visual cues?

## Screenshot Review Prompt

```text
Review this HUD/menu screenshot against docs/working/ux_principles.md.

Output:
1. What the interface is trying to make the player do.
2. Top player confusions, ordered by severity.
3. Misclick or navigation risks.
4. Feedback gaps.
5. Keyboard/controller risks.
6. Accessibility risks.
7. Low-cost fixes.
8. Higher-cost design/art fixes.
9. Implementation tasks and acceptance criteria.

Do not modify code.
```

## Onboarding Review Prompt

```text
Review the first 3 minutes of onboarding.

The player must learn:
- Move.
- Attack/interact.
- Avoid danger.
- Collect/use rewards.
- Understand current goal.

Output:
- Onboarding breakpoints.
- What can be taught through level design.
- What needs UI hints.
- What needs animation/audio feedback.
- Low-disruption hints.
- Reboarding after failure.
- Implementation tasks.
```

## Reporting

Classify findings:

- `P0`: blocks play or traps the player.
- `P1`: likely causes failure/confusion for many players.
- `P2`: polish or accessibility improvement with clear value.
- `P3`: optional or subjective.

Always state what requires human playtest or art-direction judgment.
