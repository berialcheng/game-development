# Synthetic Session Method

Use this reference when the fast loop needs a blind pass, multiple runs, recording review, or a reusable written result.

## Contents

- Quick Pass
- When To Deepen
- Evidence Notes
- Multiple Runs
- Optional Report

## Quick Pass

Use one question and one scenario. Record only:

- build/scenario
- direct play or supplied runtime evidence
- any constraint that changes interpretation
- the point at which the question is answered or the next change becomes clear

Choose the cheapest evidence that answers the question: direct play for interaction, a short recording for timing, a capture for readability, or synthetic telemetry for repeated state patterns.

Use a synthetic lens only when it changes the approach, such as genre familiarity, patience, experimentation style, risk tolerance, or input need. A lens is not a persona document or an independent tester.

For a genuine first-use question, expose only rendered output, normal controls, and player-facing rules until the trace is captured. Otherwise do not pay the cost of manufacturing blindness; state relevant prior knowledge and continue.

Ask about source origin only if a supplied recording or metric might instead belong to first-party human feedback or public external research. Unresolved origin may still support a visible observation, but not a human-audience claim.

## When To Deepen

Use a deeper pass only when one of these is true:

- onboarding blindness is the actual question
- a finding needs repeated reproduction
- several builds or control schemes are being compared
- the evidence is disputed or expensive to act on
- the work is part of a milestone or release review

## Evidence Notes

Record only checkpoints that support a change or protect something that works:

| Field | Meaning |
| --- | --- |
| checkpoint | Timestamp, room, wave, turn, screen, or named state. |
| action/result | What was attempted and what visibly happened. |
| cost/value | Lost time, retry, dead end, clear payoff, or none. |
| evidence | Reproduction step, capture, clip, metric, or short note. |

`Paused for 8 seconds and reopened the menu` is evidence. `Felt bored` is not.

For a small pass, plain-language priority is enough:

- **fix now**: blocks the scenario, creates repeated unrecovered failure, or is a cheap high-impact correction
- **test next**: plausible high-impact issue that needs one focused comparison
- **preserve**: clear payoff, readable feedback, useful tension, or successful recovery
- **later**: local polish that does not affect the current decision

Use formal severity or confidence labels only when comparing many findings or communicating across a longer milestone. A small pass needs only observation, impact, evidence, and next action.

## Multiple Runs

Keep the scenario and relevant conditions stable. Report repeatability as `x/y synthetic runs`, including failures caused by the test environment. Do not treat different lenses from one model as additional samples or convert run counts into player prevalence.

When a small fix is requested, replay only the affected path. Broaden regression only if the change touches shared state or another likely failure.

## Optional Report

```markdown
# Synthetic Gameplay Review - <build/scenario>

Question / mode:
Verdict:

## What Worked
- behavior worth preserving -> evidence

## Top Findings
| Priority | Observation and impact | Evidence | Change or next test |
| --- | --- | --- | --- |

## Action
Change made and replay result, or single best next action:

Needs real players only for:
```
