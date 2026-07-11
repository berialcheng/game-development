# Skill Simplification Baseline

This note records the one-time rule migration for the solo-developer skill refactor. It is not part of the installable skill surface.

## Goals

- Keep the five current skill roles; reduce automatic chaining between them.
- Make standalone tasks cheap and managed-project workflows explicit.
- Reduce total `SKILL.md` lines by at least 30 percent before adding cutout-character guidance.
- Keep proven failure prevention while removing duplicated explanation and release-only defaults.
- Add cutout-character production and runtime validation only as conditional references.

## Target Budgets

| Skill | Current lines | Target lines | Primary change |
| --- | ---: | ---: | --- |
| `game-reference-research` | 99 | <= 120 | Keep focused; add a research timebox. |
| `game-production-orchestrator` | 138 | <= 130 | Coordinate only multi-stage or unclear work. |
| `generate2dmap` | 390 | <= 200 | Keep routing and workflow; move mode details to references. |
| `generate2dsprite` | 290 | <= 190 | Keep asset workflow; move grid and prompt detail to references. |
| `godot-2d-implementation` | 190 | <= 170 | Implement scoped work directly; move detailed validation to references. |

## Rule Migration

| Rule or content | Current home | Decision | Destination or reason |
| --- | --- | --- | --- |
| Decide phase, acceptance, handoff, and milestone | Orchestrator | Keep | Orchestrator core workflow. |
| Require a full project document tree | Orchestrator | Replace | Use existing equivalents; require only minimal current-state docs for managed projects. |
| Iteration, phase, and playtest loops | Three orchestrator references | Merge | `iteration-loop.md`. |
| UX review and code/release review | Two orchestrator references | Merge | `review.md`. |
| AI rights, provenance, and runtime promotion | Two orchestrator references | Merge | `asset-lifecycle.md`. |
| Detailed sprite production rules in orchestrator | Orchestrator sprite reference | Remove | `generate2dsprite` owns production detail. |
| Map modes and genre routing | Map `SKILL.md` | Move | `map-strategies.md`. |
| Layer separation and reference handoff | Map `SKILL.md` | Move | `layered-map-contract.md`. |
| Prop sheet classification and extraction | Map `SKILL.md` | Move | `prop-pack-contract.md`; sprite owns transparent prop pixels. |
| Raw body sheet, grid, and FX separation detail | Sprite `SKILL.md` | Merge/move | `modes.md` and `prompt-rules.md`. |
| Legacy prompt builder as normal workflow | Sprite script and docs | Deprecate | Keep compatibility temporarily; remove from the preferred path. |
| Project shape template | Godot `SKILL.md` | Move/remove | Managed project scaffold belongs to orchestrator or target `AGENTS.md`. |
| Full verification matrix and run-manifest detail | Godot `SKILL.md` and two references | Merge | One validation reference. |
| Scoped Godot work must stop without a formal phase | Godot `SKILL.md` | Remove | Only broad, cross-system, or outcome-ambiguous work escalates to orchestrator. |
| Project commands and timeouts | Shared skill | Keep out | Target project `AGENTS.md`. |
| Semantic cutout parts, grip families, and portrait separation | Spine demo experience | Add later | Sprite conditional cutout reference. |
| True idle, action extremes, continuous motion, candidate isolation | Spine demo experience | Add later | Godot conditional cutout validation reference. |
| Mage names, weapon count, exact frame count, angle/pixel thresholds | Spine demo experience | Do not generalize | Keep project-specific. |

## Behavioral Baseline

| Request | Expected routing |
| --- | --- |
| Adjust a scoped Godot HUD and capture it | Godot only; no orchestrator. |
| Generate a four-direction raster walk sheet | Sprite plus raster mode/prompt references; no cutout. |
| Generate a paper-doll character with outfits and weapons | Sprite plus cutout production reference. |
| Integrate a candidate paper-doll without replacing the current character | Godot plus cutout validation; preserve accepted runtime. |
| Repair a stiff weapon attack | Godot continuous-motion validation; do not rebuild the whole character. |
| Plan a playable milestone spanning map, character, and integration | Orchestrator, then only the required producer/implementer skills. |

## Final Metrics

| Surface | Before | After | Change |
| --- | ---: | ---: | ---: |
| Five `SKILL.md` bodies | 1107 lines | 552 lines | -50.1% |
| Conditional references | 3389 lines | 2366 lines | -30.2% |
| Orchestrator references | 9 files | 4 files | 5 overlapping files removed/merged |
| Installed-copy warnings before sync | 22 | 0 | Source and user-level install match |

The reduction is structural, not only wording: standalone tasks now bypass orchestration, release-only controls are conditional, overlapping review/iteration/validation references are merged, and the two largest remaining map/sprite references were reduced to routing and failure-prevention rules.

## Behavioral Audit

| Request | Result | Evidence |
| --- | --- | --- |
| Adjust a scoped Godot HUD and capture it | Pass: Godot only | Godot entry gate implements scoped tasks directly; focused validation adds the relevant capture. |
| Generate a four-direction raster walk sheet | Pass: Sprite only | Sprite selects raster sheet mode; prompt rules retain directional rows and containment; cutout reference is conditional. |
| Generate a paper-doll character with outfits and weapons | Pass: Sprite plus cutout reference | Cutout mode owns semantic parts, grip families, neutral assembly, portrait role, and engine handoff. |
| Integrate a candidate paper-doll without replacing the current character | Pass: Godot plus cutout validation | Candidate stays isolated while the accepted baseline remains active; promotion and rollback are explicit. |
| Repair a stiff weapon attack | Pass: focused Godot change | Cutout validation checks true idle, action extremes, interpolation, and continuous playback without requiring a character rebuild. |
| Plan a playable milestone spanning map, character, and integration | Pass: orchestrated | Orchestrator handles acceptance and handoffs, then invokes only the required map, sprite, and Godot skills. |

## Completion Evidence

- `tools/validate-skill-repo.ps1 -CheckInstalled` passes with zero errors and zero warnings.
- All five `quick_validate.py` checks pass.
- The real `skills` CLI discovers all five skills and displays the narrowed trigger descriptions.
- Skill catalog, package metadata, registry metadata, frontmatter, and `agents/openai.yaml` agree.
- Relative Markdown links resolve, long references have contents sections, and four Python scripts parse without creating caches.
- Source and installed file sets and hashes match; stale deleted references are detected by the validator.
- The behavioral baseline routes all six representative requests as intended.