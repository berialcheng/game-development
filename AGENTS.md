# Game Development Skill Repo

This repository is a collection of Codex skills for iterative game development.

## Scope

- Installable skills live under `skills/<skill-name>/`.
- Each installable skill must contain `SKILL.md`.
- Keep repo-level documentation in `docs/` or `skills/README.md`, not inside individual skill folders.
- The repository's own research notes and retrospectives live under `docs/archive/`, named `YYYY-MM-DD-<slug>.md`. Do not confuse this `docs/` with the target Godot project's `docs/` that the skills reference.
- Demo projects and research notes are examples/reference material, not installable skills.

## Skill Maintenance

- Use lowercase hyphenated skill names.
- Keep `SKILL.md` frontmatter to `name` and `description`.
- Keep `SKILL.md` compact and route details to `references/`.
- Update `agents/openai.yaml` when a skill is renamed or its trigger behavior changes.
- Update `skill-repo.json` and `skills/README.md` whenever adding, removing, or renaming a skill.

## Validation

Validate each changed skill with:

```powershell
python C:\Users\beria\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\<skill-name>
```

Treat validation failures as blocking before publishing or installing from this repo.

## Local Demo Rules

- Do not move demo game projects into `skills/`.
- Do not make generated Godot caches or screenshots part of the skill install surface.
