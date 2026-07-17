# Review

Use this reference when a managed change needs an explicit UX, implementation, asset, or playtest review. Review the smallest evidence set that can answer the current question.

Use `$synthetic-gameplay-review` for a dedicated direct-play or runtime-evidence pass. Use `$synthesize-playtest-feedback` for supplied first-party human sessions, notes, recordings, or private feedback. This reference is for lightweight review inside an already managed outcome.

Use source context only to avoid mixing claims: first-party human feedback, synthetic/current-build evidence, and public external research. Keep this orchestrator active only when those lanes must inform the same decision.

## Evidence Selection

| Question | Prefer |
| --- | --- |
| Does behavior work? | Focused scenario, state/result metrics, or gameplay recording. |
| Is UI readable? | Actual target-state capture and input/navigation path. |
| Is animation/VFX/camera convincing? | Short rendered sequence at gameplay scale. |
| Is an asset mechanically usable? | Alpha/frame/part/import checks plus one in-engine view. |
| Is audio mechanically and contextually usable? | Format/duration/loop/loudness QC plus intended-event playback in the gameplay mix. |
| Is code safe to keep? | Diff, targeted tests, ownership boundaries, and rollback. |
| Is a milestone ready? | Core smoke, representative captures/playtest, open-risk list. |

Do not create a new dashboard or review panel when an existing capture, test, or playable path answers the question.

## UX Review

Check only relevant categories:

- first action and next-action clarity
- information hierarchy and visual clutter
- input discoverability and navigation/focus
- readable game state, feedback, and failure recovery
- target viewport/resolution and accessibility needs
- gameplay HUD versus review/debug UI

Treat visible pixels as stronger evidence than node names or manifest visibility flags for layout questions.

## Implementation Review

Inspect:

- scope drift and unrelated rewrites
- scene/script/data ownership
- input, pause, focus, and state transitions
- resource/import paths and asset lifecycle
- deterministic behavior and cleanup
- relevant tests/captures actually covering the change
- performance/accessibility risks only when affected

Do not require a separate reviewer agent for every personal-project change. A deliberate second pass with fresh evidence is enough unless independence is materially important.

## Asset Review

Separate visual and audio claims:

- mechanical validity: files, alpha/audio format, dimensions/duration, frames/parts/loops, pivots, references, import
- runtime validity: correct scene/event/state, scale or mix level, draw order or bus route, sockets/collision, animation/playback
- subjective decision: identity, readability or semantic fit, style/timbre, motion/rhythm, final quality, similarity, rights

Mechanical checks cannot answer subjective quality. A screenshot cannot prove audio behavior; use a runtime recording or direct listening pass. Make the practical choice when direction is clear; present alternatives only when taste materially changes the project.

Synthetic playback can reveal defects and compare candidates, but it cannot satisfy `human_reviewed_final` or a human rights decision.

## Playtest Review

Convert observations into a small decision list:

1. blocker or repeated high-cost failure
2. player-visible regression
3. low-cost/high-impact improvement
4. hypothesis needing another focused test
5. optional polish

Prefer a clear next change over a complete issue inventory.

Keep participant, synthetic-run, public-comment, and telemetry counts separate when they influence the decision. If lanes disagree, compare their relevance to the current build and question instead of voting across them.

## Output

Report the question, useful evidence, player impact, keep/tweak/revert/split/promote/package/stop decision, and smallest next action. Add missing evidence or rollback detail only when it affects that decision.
