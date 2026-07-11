# Project Scaffold

Use this reference only when a managed project lacks a usable equivalent. Do not migrate a healthy project to match suggested paths.

## Inspect First

Find existing:

- `AGENTS.md` or project rules
- vision/design/current-work docs
- engine project and entry scene
- tests, smoke, capture, or playtest commands
- asset source/runtime/final boundaries
- version-control and rollback practice

Map these to the required roles before creating files.

## Minimal Managed Shape

```text
AGENTS.md
project/engine files
docs/vision.md
docs/current.md
```

Use equivalent names already present.

### `AGENTS.md`

Record only operational facts that future agents must execute correctly:

- engine/tool paths and versions when important
- startup, focused validation, capture, and full smoke commands
- timeout/watchdog requirements
- forbidden generated/cache/final paths
- project-specific done criteria

Keep command catalogs or complex mode details in project scripts/config when the list becomes hard to scan.

### Vision

Keep player-facing purpose, audience, core loop, differentiators, non-goals, and high-level art/UX intent. Avoid implementation logs.

### Current Work

Keep the active outcome, scope, acceptance, relevant files/docs, validation level, stop condition, current decision, and next step. Replace stale state instead of appending every command run.

## Optional Files

Create only when the project needs them:

- `docs/decisions.md`: durable choices that future work could misunderstand.
- `docs/asset-lifecycle.md`: project-specific source/candidate/final contract.
- `docs/evidence/`: current milestone or regression evidence.
- Detailed UX/art/data docs: only when several features share the same rules.

## Ownership

- Project rules and commands -> `AGENTS.md`.
- Player intent and design constraints -> vision/design/current docs.
- Repeatable checks -> tests or automation.
- Generated run output -> evidence/generated paths, not hand-maintained narrative docs.
- Cross-project workflow -> shared skill references.

## Done Criteria

A scaffold is useful when another agent can identify the current outcome, edit the correct area, run the right validation, avoid forbidden paths, and report remaining risks without inventing a parallel process.