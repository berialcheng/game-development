# Asset Lifecycle

## Contents

- Standalone And Managed Assets
- Lifecycle States
- Suggested Folder Contract
- Prompt And Source Provenance
- Minimal Manifest
- Runtime Import
- Candidate Replacement
- AI Asset Governance
- Cost Controls

Use this reference to establish or review a target project's generated/imported visual asset contract. Standalone asset requests should not inherit a release-grade process by default.

## Standalone And Managed Assets

### Standalone

Return the requested asset, exact prompt/source provenance, minimal QC, and a useful preview. Do not create a project register or final-art approval workflow unless requested.

### Managed project

Use the project's existing equivalent or establish a small contract that separates source/provenance, processed candidates, previews, accepted runtime files, and final art.

## Lifecycle States

```text
raw_generated -> processed_candidate -> accepted_for_runtime -> human_reviewed_final
                  \-> rejected
```

- `raw_generated`: original model output, prompt, layout/reference input, or imported source.
- `processed_candidate`: cleaned, extracted, normalized, assembled, or mechanically checked output.
- `accepted_for_runtime`: a file explicitly selected for the current prototype/milestone runtime.
- `human_reviewed_final`: a human-approved release asset with quality and rights decisions complete.
- `rejected`: retained only for provenance or failure evidence.

Runtime acceptance is not final-art approval.

## Suggested Folder Contract

Use only when the project has no equivalent:

```text
assets/
  generated_placeholders/<asset-or-run-id>/
    source/
    processed/
    preview/
    asset-manifest.json
    .gdignore
  runtime_candidates/
  final/
```

Keep bulk source and preview folders outside engine imports or behind `.gdignore`. Never write generated candidates directly to `final`.

## Prompt And Source Provenance

For newly generated visual art:

- save the exact prompt before generation
- record source/reference files and generation tool/run when available
- keep prompt/reference/layout files outside runtime imports
- do not promote a candidate with missing provenance unless the user explicitly accepts the gap

## Minimal Manifest

A managed asset run needs enough information for the next step to work without guessing:

```json
{
  "schema_version": 1,
  "asset_id": "example_v001",
  "source_skill": "generate2dsprite",
  "lifecycle_state": "processed_candidate",
  "intended_use": "player idle candidate",
  "prompt_files": ["source/prompt-used.txt"],
  "source_files": ["source/raw.png"],
  "processed_files": ["processed/idle.png"],
  "preview_files": ["preview/idle.gif"],
  "runtime_candidates": [],
  "qc": {},
  "human_review": "pending",
  "rights_notes": "pending"
}
```

Add map fields, frame/part/pivot data, sockets, collision, or engine import roles only when the asset needs them.

## Runtime Import

Import only files explicitly selected by the user or listed as `accepted_for_runtime`. Do not import as runtime visuals:

- raw image outputs or prompt/reference files
- layout guides
- rejected generations
- dressed/stage references
- GIFs, review boards, or QA composites
- pipeline metadata that is evidence rather than runtime data

## Candidate Replacement

When replacing an accepted runtime asset:

```text
accepted_v1 -> isolated candidate_v2 -> in-engine review -> explicit promotion -> rollback retained
```

- Keep the current accepted asset working while the candidate is reviewed.
- Review the candidate in the real engine state and at gameplay scale; neutral/offline assembly alone is insufficient.
- Record mechanical results separately from human visual/rights approval.
- Prepare a dry-run copy/update plan and rollback point before promotion.
- Promote explicitly; do not let generation or validation scripts overwrite the accepted baseline automatically.
- Revalidate the promoted runtime path after the change.

A fingerprinted approval page is optional, not a default requirement for a personal prototype.

## AI Asset Governance

Require stricter review when generated art may ship, imitate protected characters/styles, include third-party sources, or create platform disclosure/licensing risk. Keep final art direction, rights posture, and disclosure decisions with the user.

For prototypes, record provenance and keep candidates out of final folders; defer release-only paperwork until release work begins.

## Cost Controls

- One manifest per coherent bundle, not one per screenshot.
- Keep one useful preview unless several views answer different acceptance questions.
- Retain failed output only when it explains a decision or prevents repeat work.
- Let the target project define retention and archive policy.
- Do not require all optional fields for a standalone or low-risk prototype asset.
