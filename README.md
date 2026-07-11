# Game Development Skills

Reusable agent skills for game research, production planning, image-generated 2D assets, and scoped Godot 4 2D implementation.

This repository is a skill collection. The installable surface is:

```text
skills/game-reference-research
skills/game-production-orchestrator
skills/generate2dmap
skills/generate2dsprite
skills/godot-2d-implementation
```

## Skills

| Skill | Role | Use When |
| --- | --- | --- |
| [`game-reference-research`](skills/game-reference-research/SKILL.md) | Researcher | Research Steam pages, screenshots, videos, community feedback, mechanics, UX patterns, visual references, and production handoff notes. |
| [`game-production-orchestrator`](skills/game-production-orchestrator/SKILL.md) | Producer / iteration manager | Coordinate managed, multi-stage work when scope, acceptance, handoffs, asset promotion, playtest, or milestone decisions are needed. |
| [`generate2dmap`](skills/generate2dmap/SKILL.md) | 2D map producer | Create the lightest playable map bundle with only the needed visual layers, object data, collision, scene hooks, and preview. |
| [`generate2dsprite`](skills/generate2dsprite/SKILL.md) | 2D asset producer | Create sprites, animation sheets, transparent props, FX, portraits, and cutout-character parts with deterministic cleanup and QC. |
| [`godot-2d-implementation`](skills/godot-2d-implementation/SKILL.md) | Godot implementer | Execute scoped Godot 4 2D changes: scenes, scripts, UI, gameplay, effects, imported assets, tests, and captures. |

Recommended workflow:

```text
game-reference-research (only when external evidence is needed)
-> game-production-orchestrator (only for managed, multi-stage work)
-> generate2dmap and/or generate2dsprite (only for needed visual assets)
-> godot-2d-implementation
-> game-production-orchestrator milestone review
```

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
