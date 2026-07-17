---
name: synthesize-playtest-feedback
description: Synthesize user-supplied first-party playtest or private player feedback into useful themes and practical next changes. Use for notes, recordings, quotes, interviews, surveys, closed-beta comments, and related telemetry. Keep synthetic and public evidence separate; may hand off scoped fixes when requested.
---

# Synthesize Playtest Feedback

## Purpose

Turn messy first-party human feedback into a short, useful development decision. Support both controlled playtests and informal private feedback without pretending they have the same research strength.

Analyze only material the user supplied or explicitly placed in scope. Do not recruit, contact, or impersonate participants.

## Solo-Developer Defaults

- Start from the development decision, not from a desire to code every comment.
- Use the lightest organization that reveals what to keep, change, or test next.
- Preserve attribution and counts only to the degree the supplied material supports them.
- Prefer a few grounded themes and one next action over a comprehensive research report.
- Add deeper coverage, counting, or segmentation only when the sample or decision warrants it.

## Routing

- Continue here for user-supplied first-party playtest sessions, interviews, surveys, private beta/Discord/support comments, and related player-behavior telemetry.
- Record whether evidence is controlled-session or informal only when that distinction affects confidence or counting.
- Send AI-controlled or non-participant current-build review to `$synthetic-gameplay-review` and public external commentary to `$game-reference-research`.
- Ask about uncertain origin only when it changes attribution, counting, or routing; otherwise proceed with a caveat.
- A small synthesis followed by a scoped fix does not require orchestration. When the user requests an audio change, classify it before handoff:
  - composition, timbre, semantic identity, source seam/edit, missing variation, or candidate-content mismatch -> `$generate-game-audio`
  - event trigger, stream assignment, bus/mix, playback loop, transition, pause, retrigger, or polyphony behavior -> `$godot-2d-implementation`
  - both asset content and runtime behavior, or an adaptive family spanning gameplay state -> `$game-production-orchestrator`
- Route other small scoped implementation fixes to `$godot-2d-implementation` and continue.
- Use `$game-production-orchestrator` only when multiple evidence lanes, cross-system scope, or competing product directions need one managed decision.

## Fast Synthesis

1. **Frame the decision.** Capture the question, build/scenario when relevant, and what material is available. Do not require missing study metadata for an informal test.
2. **Normalize lightly.** Preserve useful source, participant, session, and timestamp labels when available. Deduplicate the same event repeated across a recording, transcript, and notes.
3. **Separate claims.** Distinguish observed behavior, participant statements, developer/moderator notes, telemetry, and interpretation.
4. **Find signal.** Group what worked, costly friction, disagreement, and surprising behavior around the current decision.
5. **Quantify only when useful.** Count distinct people, sessions, events, or telemetry populations separately when known. Use plain language when a valid denominator is unavailable.
6. **Prioritize.** Return at most three changes or follow-up tests by player impact, repeatability, and implementation cost.
7. **Act or hand off.** If implementation was requested, provide the smallest scoped fix and validation target; otherwise stop once the next decision is clear.

Read [references/feedback-method.md](references/feedback-method.md) for recordings, surveys, multi-session counting, or a deeper report.

## Evidence Guardrails

- Do not count several notes or duplicate artifacts from one person as several participants.
- Do not treat silence as agreement or a moderator summary as participant-level counts.
- Keep people, sessions, events, public comments, synthetic runs, and telemetry populations separate; combine conclusions, not denominators.
- Do not infer motives from telemetry or generalize an informal convenience sample to all players.
- Quote only supplied words. Mark edited, translated, auto-transcribed, or summarized wording as such when exact wording matters.
- Remove unnecessary names, contact details, account identifiers, and other personal data from the output.
- Human feedback about an audio asset is evidence, not automatic `human_reviewed_final` approval. Require an explicit quality/rights decision from the responsible person before changing that lifecycle state.

## Default Output

Keep the response compact:

- decision being informed and evidence reviewed
- what worked and should be preserved
- top themes: evidence -> affected people/sessions when known -> interpretation -> change or test
- meaningful disagreement or missing evidence only when it changes the decision
- one recommended next action, or the scoped change and validation target requested by the user
