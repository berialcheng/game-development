# Playtest Feedback Method

Use this reference when supplied human feedback needs more than the default quick synthesis, especially for recordings, surveys, repeated sessions, or quantitative claims.

## Contents

- Quick Pass
- Source Context And Evidence Kind
- Recordings And Transcripts
- Surveys
- Counting
- Themes And Priorities
- Optional Report

## Quick Pass

For a few notes or comments, do not build a research database. Record the decision, identify what worked and what hurt, preserve meaningful disagreement, and return at most three changes or tests.

## Source Context And Evidence Kind

Keep two lightweight dimensions separate:

- **source context**: controlled session, private/informal first-party feedback, or uncertain
- **evidence kind**: exact quote, paraphrase, behavior observation, developer/moderator note, session log, survey response, telemetry, or interpretation

Use participant/session IDs and timestamps only when available and useful for tracing or counting. Unknown context is a caveat, not an evidence kind. Do not reconstruct missing quotes.

Treat one event repeated in a recording, transcript, and moderator note as one underlying event with several supporting artifacts. Keep participant suggestions separate from the need they may reveal.

## Recordings And Transcripts

- Review the portions relevant to the question. State skipped or missing coverage only when it weakens the conclusion.
- Use a timestamp for any recording moment that drives a finding.
- Separate visible behavior, participant speech, and moderator/developer prompting.
- Treat unverified automatic transcription as a paraphrase. Label translated wording and retain the original when wording matters.
- Do not infer identity, sensitive traits, or inner emotion from face, voice, or behavior.

## Surveys

- Record the question, answer scale/options, number of responses, and missing responses when known.
- Prefer response counts and the distribution itself. Avoid false precision or inferential statistics for a small convenience sample.
- Treat free-text responses as comments and deduplicate them from matching interview or session notes.

## Counting

Use counts only when they change confidence or priority:

- `participant_count`: distinct participants supporting or encountering a finding.
- `session_count`: distinct sessions containing the evidence.
- `occurrence_count`: repeated events, including multiple events within one session.
- `telemetry_population`: events, runs, accounts, or another explicitly defined population.

Pair a participant frequency with the eligible denominator when known, for example `3/8 participants`. If identity is unavailable, report comment or event counts rather than inventing distinct people. Do not pool different builds or scenarios when eligibility differs.

Never:

- count several notes from one person as several participants
- treat silence as agreement
- convert a moderator summary into participant-level counts without source records
- combine synthetic lenses, public comments, or telemetry populations with participant counts

## Themes And Priorities

For each decision-relevant theme, retain only:

- what worked or failed
- the best supporting example
- affected people/sessions when known
- meaningful contradiction
- likely need and smallest change or test

Use short participant quotes only when wording materially matters. Prefer attributed observations for behavior.

Prioritize by player cost, repeatability, and implementation cost. Frequency does not determine severity: one progression blocker or access need may deserve action. Use formal severity/confidence labels only for a larger study or milestone.

## Optional Report

```markdown
# Playtest Feedback Synthesis - <study/build>

Decision / build when relevant:
Evidence reviewed:

## What Worked
- behavior or comment -> value -> source

## Top Themes
| Theme | Best evidence | People/sessions when known | Interpretation | Change or test |
| --- | --- | --- | --- | --- |

Meaningful disagreement or missing evidence:
Recommended next action:
```
