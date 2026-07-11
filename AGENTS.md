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
- Route standalone asset work and scoped Godot work directly to the owning skill. Use the production orchestrator only when scope, acceptance, cross-skill handoffs, promotion, playtest, or milestone decisions must be managed.
- Prefer the lightest workflow that can produce a testable result. Make release-grade manifests, provenance detail, and broad review passes conditional rather than default.
- Keep project-specific commands, timeouts, thresholds, and content facts in the target project's `AGENTS.md` or docs, not in shared skills.
- Keep core skill bodies within the line budgets enforced by `tools/validate-skill-repo.ps1`. When a reference exceeds 100 lines, add a compact contents section.
- Update `agents/openai.yaml` when a skill is renamed or its trigger behavior changes.
- Update `skill-repo.json` and `skills/README.md` whenever adding, removing, or renaming a skill.

## Validation

Validate the whole repository with:

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-skill-repo.ps1
```

Use the individual structural check only to isolate a failure:

```powershell
python C:\Users\beria\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\<skill-name>
```

Treat validation failures as blocking before publishing or installing from this repo. After syncing user-level skills, rerun the repository validator with `-CheckInstalled`.

## Local Demo Rules

- Do not move demo game projects into `skills/`.
- Do not make generated Godot caches or screenshots part of the skill install surface.
