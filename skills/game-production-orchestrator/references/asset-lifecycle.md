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

Use this reference to establish or review a target project's generated/imported visual or audio asset contract. Standalone asset requests should not inherit a release-grade process by default.

## Standalone And Managed Assets

### Standalone

Return the requested asset, exact prompt/source provenance, minimal QC, and a useful preview. Do not create a project register or final-art approval workflow unless requested.

### Managed project

Use the project's existing equivalent or establish a small contract that separates source/provenance, processed candidates, previews, accepted runtime files, and final assets.

## Lifecycle States

```text
raw_generated -> processed_candidate -> accepted_for_runtime -> human_reviewed_final
                  \-> rejected
```

- `raw_generated`: original model output, prompt, layout/reference input, audio reference, or imported source.
- `processed_candidate`: cleaned, extracted, normalized, assembled, converted, or mechanically checked output.
- `accepted_for_runtime`: a file explicitly selected for the current prototype/milestone runtime.
- `human_reviewed_final`: a human-approved release asset with visual/listening quality and rights decisions complete.
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

For newly generated visual art or audio:

- save the exact prompt before generation
- record source/reference files and generation tool/run when available
- keep prompt/reference/layout files outside runtime imports
- do not promote a candidate with missing provenance unless the user explicitly accepts the gap

## Minimal Manifest

A managed asset run needs enough information for the next step to work without guessing:

```json
{
  "schema_version": 1,
  "media_type": "audio",
  "asset_id": "example_v001",
  "source_skill": "generate-game-audio",
  "lifecycle_state": "processed_candidate",
  "intended_use": "exploration music loop candidate",
  "prompt_files": ["source/prompt-used.txt"],
  "source_files": ["source/original.wav"],
  "processed_files": ["processed/music_loop.wav"],
  "preview_files": [],
  "runtime_candidates": [],
  "candidates": {},
  "selection_history": [],
  "qc": {},
  "human_review": "pending",
  "rights_notes": "pending"
}
```

Keep this envelope stable across asset skills. Add map fields, frame/part/pivot data, sockets, collision, or engine import roles only when needed.

Generated audio uses two extensions:

- `generation`: provider, model, revision, seed, and copied request/settings provenance
- `audio`: mode, event/zone/bus/family IDs, shared musical sync and format fields, and `members`

Every audio member owns its own role, target duration, loop flag, and variation count. An intro and loop must not inherit one global duration/loop constraint. `generate-game-audio select` may populate `runtime_candidates` and `selection_history` only after all declared members have the required number of passing candidates.

## Runtime Import

Import only files named in `runtime_candidates` when the manifest lifecycle is `accepted_for_runtime` (or the project's documented equivalent). Selection must identify an owner and reason. Do not import as runtime assets:

- raw image/audio outputs or prompt/reference files
- layout guides
- rejected generations
- dressed/stage references
- GIFs, audition playlists, waveform previews, review boards, or QA composites
- pipeline metadata that is evidence rather than runtime data

## Candidate Replacement

When replacing an accepted runtime asset:

```text
accepted_v1 -> isolated candidate_v2 -> in-engine review -> explicit promotion -> rollback retained
```

- Keep the current accepted asset working while the candidate is reviewed.
- Review the candidate in the real engine state at gameplay scale and, for audio, in the actual gameplay mix; neutral/offline assembly or isolated audition alone is insufficient.
- Record mechanical results separately from human visual/listening/rights approval.
- Prepare a dry-run copy/update plan and rollback point before promotion.
- Promote explicitly; do not let generation or validation scripts overwrite the accepted baseline automatically.
- For generated audio, use the manifest `select --replace` path or the project's equivalent so the previous runtime list remains auditable.
- Revalidate the promoted runtime path after the change.

A fingerprinted approval page is optional, not a default requirement for a personal prototype.

## AI Asset Governance

Require stricter review when generated art/audio may ship, imitate protected characters/styles/voices/music, include third-party sources, or create platform disclosure/licensing risk. Keep final direction, rights posture, and disclosure decisions with the user.

For prototypes, record provenance and keep candidates out of final folders; defer release-only paperwork until release work begins.

## Cost Controls

- One manifest per coherent bundle, not one per screenshot.
- Keep one useful preview unless several views answer different acceptance questions.
- Retain failed output only when it explains a decision or prevents repeat work.
- Let the target project define retention and archive policy.
- Do not require all optional fields for a standalone or low-risk prototype asset.
