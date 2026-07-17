# Gameplay Evidence Skill Research

This note records the research behind `synthetic-gameplay-review` and `synthesize-playtest-feedback`. It is not part of the installable skill surface. The original combined design was split on 2026-07-18 so synthetic observations and real participant evidence have independent contracts.

## 2026-07-18 Solo-Developer Revision

The installable skills were subsequently simplified for a personal independent-development workflow. The current goal is decision speed and playable progress, with rigor proportional to the cost of being wrong:

- a review may continue into a small scoped fix when the user requests it
- first-party private beta, Discord, support, survey, and telemetry evidence may use the human-feedback synthesis lane even when it is not a formal controlled study
- missing study metadata or uncertain provenance does not block useful work unless it changes attribution, counting, routing, or the conclusion
- quick passes return what worked, at most three important changes, and one next action; formal IDs, severity scales, complete traces, and broad reports are conditional
- orchestration is reserved for genuine cross-system dependency, mixed-evidence decisions, asset promotion, milestone, or release work
- formal signoff is not a default personal-project stage; the user decides material creative forks and whether to ship

The historical sections below explain the evidence-separation rationale of the first version. The current installable `SKILL.md` files are authoritative where the later solo-developer workflow differs.

## Decision

Create a dedicated evidence-based **synthetic gameplay review**, not a simulated human opinion generator. Keep supplied evidence from real playtest participants in a separate synthesis skill with attribution, counting, disagreement, and privacy rules.

Its useful job is to play or inspect a build, expose observable friction and payoff, preserve a trace, and convert findings into small testable iteration hypotheses. It must not claim that an LLM persona represents a target audience, predicts fun, or replaces real players.

## Role Boundary

| Skill | Owns | Does not own |
| --- | --- | --- |
| `game-reference-research` | External games, stores, media, and community evidence. | Reviewing the current local build as a player. |
| `godot-2d-implementation` | Code, scenes, tests, deterministic scenarios, and captures. | A blind player-perspective experience pass. |
| `game-production-orchestrator` | Scope, acceptance, handoffs, iteration, and milestone decisions. | Conducting a dedicated gameplay session. |
| `synthetic-gameplay-review` | Synthetic direct play/evidence review, trace, friction/payoff findings, and test hypotheses. | Real participant synthesis, implementation, or release readiness. |
| `synthesize-playtest-feedback` | Controlled participant recordings, notes, quotes, interviews, session records, attribution, known frequencies, and disagreements. | Synthetic runs, public-comment research, participant recruitment, or implementation. |

The role is engine-independent and can run without a managed production cycle. Separation also protects the blind-review boundary: implementation knowledge should not leak into player evidence.

## Evidence For The Useful Part

- LLM agents were weaker than average humans in Wordle and Slay the Spire, yet their performance correlated strongly with human-indicated difficulty. This supports comparative difficulty probing, not human equivalence: [LLMs May Not Be Human-Level Players, But They Can Be Testers](https://arxiv.org/abs/2410.02829).
- EA researchers used automated agents to explore a mechanics model of The Sims Mobile at scale, finding imbalances, weak rewards, and inconsequential strategic choices that informed design changes: [Exploring Gameplay With AI Agents](https://arxiv.org/abs/1811.06962).
- DeepMind SIMA shows a vision-language agent using screen pixels plus keyboard/mouse actions across 3D games. Its published evaluation focuses on short instruction-following skills, not taste or fun: [A generalist AI agent for 3D virtual environments](https://deepmind.google/blog/sima-generalist-ai-agent-for-3d-virtual-environments/).
- PlaytestArena and Play2Code report that GUI agents can catch interaction-level failures and provide traceable feedback in browser games, while also describing the feedback as idiosyncratic: [GUI Agents for Continual Game Generation](https://arxiv.org/abs/2605.28258).

## Evidence For The Limit

- A 2026 ACL study comparing prompt-based LLM agents with 31,865 real shopping sessions found 11.86 percent next-action accuracy. The domain differs, but it strongly warns against equating believable narration with faithful behavior: [Can LLM Agents Simulate Multi-Turn Human Behavior?](https://aclanthology.org/2026.acl-long.2034/).
- Microsoft Research found that assistant-tuned LMs make poor user simulators and stronger assistants can be worse simulators: [Flipping the Dialogue](https://www.microsoft.com/en-us/research/publication/flipping-the-dialogue-training-and-evaluating-user-language-models/).
- Persona research reports mixed reproduction of explicit factors and failure to model complex interactions and subtleties of human perception: [Modeling Human Subjectivity in LLMs](https://arxiv.org/abs/2406.14462).

## Real Playtesting Still Matters

- Practitioner guidance emphasizes observe, test, and measure, and warns that playtests should refine design intent rather than let testers redesign the game: [Reflections on playtesting and Puzzledorf](https://www.gamedeveloper.com/game-platforms/reflections-on-playtesting-and-puzzledorf).
- A developer postmortem describes watching about 50 streamer sessions as the most valuable activity because visible boredom, laughter, quitting, and theorizing drove edits. This anecdote illustrates lived reactions a synthetic pass cannot supply: [Rose Academy postmortem](https://www.reddit.com/r/gamedev/comments/1sml2qm/i_spent_38000_making_an_visual_novel_so_you_dont/).

## Existing Patterns

GitHub examples cluster into two incomplete patterns:

- report templates that structure supplied notes but do not play or enforce provenance, such as [playtest-report](https://github.com/majiayu000/claude-skill-registry/blob/8df1cb0929bf7df686c85af70ccd25c6668fd57f/skills/gaming/playtest-report/SKILL.md)
- project-specific agents with a real control bridge and a player-only boundary, such as [NeoMud playtester](https://github.com/roomsmith-games/NeoMud/blob/5de4d85c285f20cfc86e75c8d05350aa05aa1e26/.claude/agents/playtester.md)

The reusable design combines report structure with a blind boundary while leaving concrete input bridges in each target project.

## Design Consequences

1. Keep synthetic direct play/evidence review separate from real-participant feedback synthesis.
2. Route by provenance before media type: controlled participant recording, non-participant current-build recording, and public stream have different owners.
3. Keep unresolved sources explicit as `provenance_unknown`; do not infer public status, human attribution, or denominators.
4. Require build, question, scenario, lens, evidence, stop, and cleanup fields.
5. Define personas through behavior-relevant traits; avoid demographic role-play and fictional emotions.
6. Separate observation, interpretation, hypothesis, and next validation.
7. Use severity for player impact and confidence for evidence quality.
8. Never turn repeated prompts or multiple lenses from one model into sample size; count human participants, sessions, and occurrences separately.
9. Handoff scoped fixes to implementation and mixed evidence decisions to orchestration.
10. Require real players for fun, emotion, accessibility lived experience, culture, market fit, retention, and purchase intent.

## First Implementation Scope

The first version is documentation-only: two compact skills, one synthetic session reference, one human-feedback method reference, catalog updates, and orchestrator routing. It has no generic control script because launch, input, timeout, and cleanup are engine- and project-specific.

## Behavioral Audit

| Request | Expected routing | Result |
| --- | --- | --- |
| Review this playable tutorial as a first-time player. | `synthetic-gameplay-review` direct play. | Pass: contract requires build, blind status, controls, trace, and cleanup. |
| Review this recording because the build cannot run here. | `synthetic-gameplay-review` evidence review. | Pass: it cannot claim direct play and must report missing evidence. |
| Review this controlled participant-session recording. | `synthesize-playtest-feedback`. | Pass: recording observations retain participant/session IDs and timestamps. |
| Turn notes from three real testers into priorities. | `synthesize-playtest-feedback`. | Pass: participant/session attribution, known denominators, disagreement, and privacy stay explicit. |
| Analyze recurring Steam review complaints. | `game-reference-research`. | Pass: public comments remain external uncontrolled evidence, not a playtest sample. |
| Summarize these player comments, but their source is not provided. | No count-bearing route until provenance is established. | Pass: mark `provenance_unknown`, request source context, and do not infer public or participant status. |
| Compare two synthetic runs, five controlled sessions, and public reviews. | `game-production-orchestrator`. | Pass: each lane keeps its own owner, provenance, counting unit, and denominator. |
| Fix the confirmed HUD clipping bug. | `godot-2d-implementation`. | Pass: the new skill hands off and does not silently implement. |
| Decide between two cross-system redesigns for a milestone. | `game-production-orchestrator`. | Pass: competing hypotheses escalate to managed production. |
| Run deterministic regression after a code change. | `godot-2d-implementation`. | Pass: automated regression is excluded from the new entry gate. |

The current repository has no playable demo or captured session artifact, so direct-control forward-testing remains a future integration test rather than a prerequisite for the documentation-only skill contract. It should use a real project-documented control surface; a formatting fixture cannot validate player interaction. Feedback synthesis should also be forward-tested against de-identified multi-participant notes containing repeated events, contradictions, missing denominators, and minority experiences.
