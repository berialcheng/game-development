# Skills Catalog

This directory is the install surface for the repository. Each child directory is a standalone Codex skill.

## Installable Skills

| Skill | Path | Role |
| --- | --- | --- |
| `game-reference-research` | `skills/game-reference-research` | Research public reference games, store pages, media, community commentary, UX patterns, mechanics, and production implications. |
| `synthetic-gameplay-review` | `skills/synthetic-gameplay-review` | Play or inspect a build through explicit synthetic player lenses and produce traceable, testable findings. |
| `synthesize-playtest-feedback` | `skills/synthesize-playtest-feedback` | Turn first-party sessions or informal private player feedback into grounded themes and practical next changes. |
| `game-production-orchestrator` | `skills/game-production-orchestrator` | Coordinate only work that genuinely needs cross-system, mixed-evidence, asset-promotion, milestone, or release management. |
| `godot-2d-implementation` | `skills/godot-2d-implementation` | Implement concrete scoped Godot 4 2D changes with risk-appropriate tests and captures. |
| `generate2dsprite` | `skills/generate2dsprite` | Generate sprites, animation sheets, transparent props, FX, portraits, and cutout-character parts with deterministic cleanup and QC. |
| `generate2dmap` | `skills/generate2dmap` | Generate the lightest fitting 2D map bundle with visual layers, map-local objects, placement, collision, scene hooks, and preview. |

## Routing

Prefer the shortest specialist path. Public external evidence goes to `game-reference-research`, synthetic/current-build evidence to `synthetic-gameplay-review`, and user-supplied first-party or private human feedback to `synthesize-playtest-feedback`. Ask about uncertain source context only when it changes the route or claim. A review followed by a small scoped fix may continue directly to implementation; use `game-production-orchestrator` only when coordination materially helps.

## Installation Paths

Use these paths when installing from this repository:

```text
skills/game-reference-research
skills/synthetic-gameplay-review
skills/synthesize-playtest-feedback
skills/game-production-orchestrator
skills/godot-2d-implementation
skills/generate2dsprite
skills/generate2dmap
```

For Codex's GitHub installer helper:

```powershell
python C:\Users\beria\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo <owner>/<repo> --path skills/game-reference-research skills/synthetic-gameplay-review skills/synthesize-playtest-feedback skills/game-production-orchestrator skills/godot-2d-implementation skills/generate2dsprite skills/generate2dmap
```

Replace `<owner>/<repo>` with the published GitHub repository.

## Maintenance

- Keep this catalog and `../skill-repo.json` in sync.
- Run `..\tools\validate-skill-repo.ps1`; use `quick_validate.py` only to isolate one structural failure.
- Do not add README files inside individual skill folders.
