# Game Development Skills

Reusable agent skills for solo-developer-first game research, synthetic gameplay review, first-party player-feedback synthesis, lightweight production coordination, generated 2D assets, and scoped Godot 4 2D implementation.

This repository is a skill collection. The installable surface is:

```text
skills/game-reference-research
skills/synthetic-gameplay-review
skills/synthesize-playtest-feedback
skills/game-production-orchestrator
skills/generate2dmap
skills/generate2dsprite
skills/godot-2d-implementation
```

## Solo Developer Defaults

- Optimize for the shortest path from a question to a better playable build.
- Send clear work directly to the owning specialist; orchestration is optional and must earn its cost.
- Use the cheapest evidence that can support the next decision, then stop.
- Keep outputs compact: what worked, up to three important changes, and the next action.
- Continue from review into a small scoped fix when the user asks; do not add a formal approval stage.
- Increase documentation, counting, review breadth, and release checks only as the cost of being wrong increases.
- Keep only three core evidence guardrails: never present synthetic feedback as human, never merge incompatible populations, and never exceed the user's change authority.

## Skills

| Skill | Role | Use When |
| --- | --- | --- |
| [`game-reference-research`](skills/game-reference-research/SKILL.md) | Public reference researcher | Research external store pages, screenshots, videos, public community commentary, mechanics, UX patterns, and production implications. |
| [`synthetic-gameplay-review`](skills/synthetic-gameplay-review/SKILL.md) | Synthetic player reviewer | Play or inspect a build, trace observable friction and payoff, and produce testable improvements without presenting it as human feedback. |
| [`synthesize-playtest-feedback`](skills/synthesize-playtest-feedback/SKILL.md) | First-party player-feedback analyst | Turn controlled sessions or informal private feedback into a few grounded themes and practical next changes. |
| [`game-production-orchestrator`](skills/game-production-orchestrator/SKILL.md) | Producer / iteration manager | Coordinate only genuinely cross-system, mixed-evidence, asset-promotion, milestone, or release work. |
| [`generate2dmap`](skills/generate2dmap/SKILL.md) | 2D map producer | Create the lightest playable map bundle with only the needed visual layers, object data, collision, scene hooks, and preview. |
| [`generate2dsprite`](skills/generate2dsprite/SKILL.md) | 2D asset producer | Create sprites, animation sheets, transparent props, FX, portraits, and cutout-character parts with deterministic cleanup and QC. |
| [`godot-2d-implementation`](skills/godot-2d-implementation/SKILL.md) | Godot implementer | Execute scoped Godot 4 2D changes: scenes, scripts, UI, gameplay, effects, imported assets, tests, and captures. |

Routing is conditional, not a required production pipeline:

```text
clear task -----------------------> owning specialist
review + small scoped fix --------> review skill -> implementation skill
public external evidence ---------> game-reference-research
synthetic/current-build evidence -> synthetic-gameplay-review
first-party/private feedback -----> synthesize-playtest-feedback
genuine coordination need --------> game-production-orchestrator
```

Ask about source context only when it changes routing, counting, or the conclusion. Use the orchestrator when coordination materially reduces risk, not merely because work has more than one step.

## Install With `npx skills`

This repo uses the common `skills/<skill-name>/SKILL.md` layout supported by the third-party [`vercel-labs/skills`](https://github.com/vercel-labs/skills) CLI.

List local skills:

```powershell
cd C:\Users\beria\workingcopy\game-development
npx skills add . --list
```

Recommended local install for Codex, Claude Code, and OpenCode:

```powershell
npx skills add . --skill '*' --agent codex --agent claude-code --agent opencode --global -y
```

On Windows with `skills@1.5.12`, this creates one shared user-level install under:

```text
%USERPROFILE%\.agents\skills
```

Codex and OpenCode use that shared directory directly. Claude Code gets junctions under `%USERPROFILE%\.claude\skills` that point to the same installed skills. This avoids maintaining separate copies per agent.

Inspect installed skills:

```powershell
npx skills list --global --agent codex
npx skills list --global --agent claude-code
npx skills list --global --agent opencode
```

Install from GitHub:

```powershell
npx skills add berialcheng/game-development --skill '*' --agent codex --agent claude-code --agent opencode --global -y
```

Install one skill:

```powershell
npx skills add berialcheng/game-development --skill godot-2d-implementation --agent codex --agent claude-code --agent opencode --global -y
```

Update installed skills:

```powershell
npx skills update -g -y
```

Use `--copy` only when you explicitly want independent copies or symlink/junction creation fails.

## Repo Files

| Path | Purpose |
| --- | --- |
| [`skills/`](skills/) | Installable skill folders. |
| [`skills/README.md`](skills/README.md) | Human-readable skill catalog. |
| [`skill-repo.json`](skill-repo.json) | Machine-readable skill collection manifest. |
| [`package.json`](package.json) | Lightweight npm-style metadata for skill tooling. |
| [`AGENTS.md`](AGENTS.md) | Maintenance rules for this skill repo. |
| [`godot-2d-agent-template/`](godot-2d-agent-template/) | Reference `AGENTS.md` template for Godot 4 2D projects. |
| [`docs/archive/`](docs/archive/) | Finished research and retrospective notes from past skill iterations, named `YYYY-MM-DD-<slug>.md`. |

Past research and retrospective notes live in [`docs/archive/`](docs/archive/):

```text
docs/archive/2026-06-14-github-skills-research.md
docs/archive/2026-06-14-skill-redesign.md
docs/archive/2026-06-14-godot-codex-learning.md
docs/archive/2026-06-14-skill-review-v1.md
```

## Validate

Validate the repository before publishing:

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-skill-repo.ps1
```

The validator runs every skill's structural check and also audits catalogs, registry metadata, relative links, UI metadata budgets, Python syntax, long-reference contents, and skill line budgets. Use `-CheckInstalled` after syncing user-level skills.

Individual structural commands remain available when isolating one failure:

```powershell
python C:\Users\beria\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\game-reference-research
python C:\Users\beria\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\synthetic-gameplay-review
python C:\Users\beria\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\synthesize-playtest-feedback
python C:\Users\beria\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\game-production-orchestrator
python C:\Users\beria\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\generate2dmap
python C:\Users\beria\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\generate2dsprite
python C:\Users\beria\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\godot-2d-implementation
```

Also check discovery:

```powershell
npx skills add . --list
```

## Notes

- Treat `skills/` as the published install surface.
- Do not put README files inside individual skill folders.
- Do not commit generated local install state such as `skills-lock.json`.
- `balaro-demo/` and `vampire-like/` are ignored local demo workspaces.
