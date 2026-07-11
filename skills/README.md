# Skills Catalog

This directory is the install surface for the repository. Each child directory is a standalone Codex skill.

## Installable Skills

| Skill | Path | Role |
| --- | --- | --- |
| `game-reference-research` | `skills/game-reference-research` | Research reference games, Steam pages, media, community feedback, UX patterns, mechanics, and production implications. |
| `game-production-orchestrator` | `skills/game-production-orchestrator` | Coordinate managed multi-stage work when scope, acceptance, handoffs, playtest, promotion, or milestone decisions are needed. |
| `godot-2d-implementation` | `skills/godot-2d-implementation` | Implement concrete scoped Godot 4 2D changes with risk-appropriate tests and captures. |
| `generate2dsprite` | `skills/generate2dsprite` | Generate sprites, animation sheets, transparent props, FX, portraits, and cutout-character parts with deterministic cleanup and QC. |
| `generate2dmap` | `skills/generate2dmap` | Generate the lightest fitting 2D map bundle with visual layers, map-local objects, placement, collision, scene hooks, and preview. |

## Routing

Standalone asset work goes directly to `generate2dmap` or `generate2dsprite`. Scoped Godot changes go directly to `godot-2d-implementation`. Use `game-production-orchestrator` only for managed multi-stage work, and use research only when an external decision needs evidence.

## Installation Paths

Use these paths when installing from this repository:

```text
skills/game-reference-research
skills/game-production-orchestrator
skills/godot-2d-implementation
skills/generate2dsprite
skills/generate2dmap
```

For Codex's GitHub installer helper:

```powershell
python C:\Users\beria\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo <owner>/<repo> --path skills/game-reference-research skills/game-production-orchestrator skills/godot-2d-implementation skills/generate2dsprite skills/generate2dmap
```

Replace `<owner>/<repo>` with the published GitHub repository.

## Maintenance

- Keep this catalog and `../skill-repo.json` in sync.
- Run `..\tools\validate-skill-repo.ps1`; use `quick_validate.py` only to isolate one structural failure.
- Do not add README files inside individual skill folders.
