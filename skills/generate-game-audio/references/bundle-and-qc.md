# Bundle And QC

## Contents

- Bundle Contract
- Lifecycle
- Manifest Contract
- Deterministic Checks
- Listening Review
- Explicit Runtime Selection
- Runtime Handoff
- Failure Policy

Mechanical QC proves that a file is decodable and measures objective properties. It does not prove that the sound fits the event, loops perceptually, mixes well, is original, or is legally safe.

## Bundle Contract

```text
<asset-or-run-id>/
  source/
    prompt-used.txt
    provider-request.json       # optional
    original-output.*          # when normalization changes the file
  processed/
    <asset-id>_c01.wav
  preview/
    audition.*                 # optional
  asset-manifest.json
```

For a managed project, keep the bundle outside engine imports or behind `.gdignore`. Copy only an explicitly accepted runtime export into the project-native audio directory.

## Lifecycle

```text
raw_generated -> processed_candidate -> accepted_for_runtime -> human_reviewed_final
                  \-> rejected
```

- `raw_generated`: provider output plus prompt/request provenance.
- `processed_candidate`: normalized and mechanically checked.
- `accepted_for_runtime`: explicitly selected for the current build.
- `human_reviewed_final`: quality, similarity, rights, and release use reviewed by a human.
- `rejected`: retained only when useful for provenance or failure analysis.

`qc` may advance to `processed_candidate`. `select` may advance a complete, passing selection to `accepted_for_runtime` and records the responsible owner and reason. No bundled command may claim `human_reviewed_final` or copy files into an engine project.

## Manifest Contract

The audio manifest uses the same generic envelope as other managed assets:

```json
{
  "schema_version": 1,
  "media_type": "audio",
  "asset_id": "music_cave_v001",
  "source_skill": "generate-game-audio",
  "lifecycle_state": "processed_candidate",
  "source_files": ["source/original-output.wav"],
  "processed_files": ["processed/intro.wav", "processed/loop.wav"],
  "preview_files": [],
  "runtime_candidates": [],
  "candidates": {},
  "selection_history": [],
  "human_review": "pending",
  "rights_notes": "pending"
}
```

The `audio` extension carries:

- `mode`, `event_id`, `zone_id`, `bus_role`, and `family_id`
- shared `bpm`, `key_mode`, `meter`, `phrase_bars`, and `sync_anchor`
- target sample rate and channels
- `members`, each with its own `id`, `role`, `target_duration_seconds`, `loop`, and `variations`

The `generation` extension records provider, model, revision, seed, and copied request/settings files. Raw provider output remains in `source/`; normalized PCM candidates belong in `processed/`.

## Deterministic Checks

`audio_asset.py qc` accepts uncompressed PCM WAV and records:

- SHA-256, file size, duration, sample rate, channels, bit depth, and frame count
- peak and RMS dBFS
- clipped sample count and ratio
- near-silence ratio at the configured threshold
- normalized DC offset
- first/last-window RMS difference and boundary jump for requested loops
- duration, sample-rate, channel, and clipping constraint results

Use explicit expected values when the project has a contract:

```powershell
python scripts/audio_asset.py qc bundle/asset-manifest.json bundle/processed/c01.wav `
  --member-id main `
  --expected-sample-rate 48000 --expected-channels 2 `
  --duration-tolerance 0.5 --max-clipped-ratio 0.0001
```

When a bundle has multiple members, `--member-id` is required. Duration and loop diagnostics come from that member; sample rate and channels default to the shared audio contract unless explicitly overridden.

Boundary metrics are diagnostics, not a seamless-loop certificate.

## Listening Review

Audition passing candidates:

- with representative gameplay, dialogue, UI, ambience, and important feedback
- repeatedly for high-frequency events
- for at least several loop boundaries when looped
- at the target loudness relationship, not normalized in isolation only
- for unintended speech, vocals, background music, room tone, distortion, and semantic errors
- for suspicious similarity to known recordings or compositions

Record the selection and rejection reason concisely. Keep `human_review: pending` until a relevant person actually listens and resolves rights questions.

Synthetic gameplay review may expose runtime problems or support a candidate comparison, but it cannot satisfy human listening or rights review.

## Explicit Runtime Selection

After listening and QC, record the exact passing files:

```powershell
python scripts/audio_asset.py select bundle/asset-manifest.json `
  bundle/processed/intro.wav bundle/processed/loop.wav `
  --selected-by "developer" --reason "best contextual fit"
```

Selection is atomic: every member must have exactly its declared number of selected variations. Replacing an existing selection requires `--replace` and leaves the previous list in `selection_history`. This is manifest acceptance for integration, not release approval.

## Runtime Handoff

Hand `$godot-2d-implementation`:

- accepted `asset-manifest.json` and its `runtime_candidates`
- `event_id`, `zone_id`, `bus_role`, and intended event/scene
- target sample rate/channels and preferred runtime encoding
- member IDs, roles, durations, loop flags, and variation counts
- family BPM/key/meter/phrase/sync metadata when applicable
- loop/transition notes
- provider/model/revision/seed/request/settings provenance
- loudness relationship, when known
- unresolved listening or rights risks

Do not hand off every generated candidate as runtime content.

## Failure Policy

- Decode/format failure: retain evidence, convert from the untouched source, and rerun.
- Duration or sample-rate failure: regenerate or intentionally normalize; do not relabel.
- Clipping failure: regenerate or repair from an unclipped source.
- High silence or seam diagnostics: inspect and listen before deciding.
- Semantic or musical failure: reject even when every mechanical check passes.
