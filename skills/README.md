# Skills Catalog

This directory is the install surface for the repository. Each child directory is a standalone Codex skill.

## Installable Skills

| Skill | Path | Role |
| --- | --- | --- |
| `game-reference-research` | `skills/game-reference-research` | Research reference games, Steam pages, media, community feedback, UX patterns, mechanics, and production implications. |
| `game-production-orchestrator` | `skills/game-production-orchestrator` | Coordinate iterative game production: docs, phase plans, handoffs, review, playtest feedback, validation, and milestone output. |
| `godot-2d-implementation` | `skills/godot-2d-implementation` | Implement and validate scoped Godot 4 2D phases, including scenes, scripts, UI, gameplay, sprites, tests, screenshots, and manifests. |

## Installation Paths

Use these paths when installing from this repository:

```text
skills/game-reference-research
skills/game-production-orchestrator
skills/godot-2d-implementation
```

For Codex's GitHub installer helper:

```powershell
python C:\Users\beria\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo <owner>/<repo> --path skills/game-reference-research skills/game-production-orchestrator skills/godot-2d-implementation
```

Replace `<owner>/<repo>` with the published GitHub repository.

## Maintenance

- Keep this catalog and `../skill-repo.json` in sync.
- Validate changed skills with `quick_validate.py`.
- Do not add README files inside individual skill folders.
