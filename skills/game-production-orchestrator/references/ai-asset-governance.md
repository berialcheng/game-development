# AI Asset Governance

Use this reference when Codex or an image model helps create art, audio, icons, banners, sprite sheets, copy, or other player-facing content.

## Register Fields

Track AI-assisted assets in `docs/ai_asset_register.md`:

```text
Date:
Asset path:
Source/tool/model:
Prompt or brief:
Reference sources:
Intended use:
Placeholder or final candidate:
Human review status:
Human edits/redraw:
License/rights notes:
Platform disclosure relevance:
Release decision:
```

## Folder Rules

```text
assets/
  generated_placeholders/
  runtime_candidates/
  raw/
  final/
```

- Generated bundles start in `generated_placeholders/<asset_id-or-run_id>` with source, processed, preview, and `asset-manifest.json`.
- Runtime imports may use copies in `runtime_candidates` only when the manifest marks them `accepted_for_runtime`.
- Raw references go in `raw` when the project has rights to store them.
- Final art moves to `final` only after human review and rights/disclosure review.
- Do not overwrite final assets automatically.

## Risk Rules

- Do not imitate named living artists.
- Do not use copyrighted characters or unlicensed references as style/source targets.
- Do not claim generated art is final unless a human has accepted quality and rights risk.
- Keep provenance for platform content surveys, team handoff, and future audits.
- For runtime-generated AI content, require explicit human policy decisions and safety controls before implementation.

## Reporting

When adding or changing AI-assisted assets, report:

- Asset paths and manifest paths.
- Lifecycle state: raw generated, processed candidate, accepted runtime candidate, rejected, or human-reviewed final.
- Register entries updated.
- Validation performed.
- Human review still required.
