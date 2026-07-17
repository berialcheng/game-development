---
name: generate-game-audio
description: "Generate and postprocess game music, ambience, stingers, UI sounds, and gameplay sound effects with local or cloud audio models. Use when Codex needs prompt-driven audio candidates, variation banks, loopable cues, deterministic audio QC, provenance, or a managed handoff; keep engine import and runtime wiring separate."
---

# Generate Game Audio

## Purpose

Turn a concrete game-audio need into the smallest useful bundle of generated candidates, exact prompt and provider provenance, deterministic mechanical QC, and a clear engine-integration handoff.

This skill owns audio-asset production. It does not own Godot nodes, buses, event wiring, adaptive-music state machines, or final release approval.

## Entry Gate

- Use this skill directly for music, ambience, stingers, UI sounds, one-shot SFX, and coherent variation banks.
- Use `$godot-2d-implementation` when accepted audio must be imported, routed, triggered, mixed, looped, or tested in Godot.
- Use `$game-production-orchestrator` only when audio depends on several systems, replaces accepted assets, defines an adaptive family, or needs milestone/release coordination.
- Do not invoke an image or map generator for audio work.

## Choose the Audio Mode

| Mode | Deliverable |
| --- | --- |
| `music_loop` | One loopable background cue plus alternate candidates. |
| `music_cue` | A finite menu, cutscene, results, or narrative cue. |
| `music_family` | Related intro/loop/outro, intensity layers, or stems with shared musical constraints. |
| `stinger` | A short transition, success, failure, reveal, or encounter accent. |
| `sfx_one_shot` | A single event sound with several candidates. |
| `sfx_variation_bank` | Interchangeable variants for a frequently repeated event. |
| `ambience_loop` | A loopable environmental bed without foreground musical structure. |

For a mixed request, split it into coherent bundles only when the assets need different providers, prompts, acceptance criteria, or runtime roles.

## Core Rules

- Treat model output as a candidate, never as an accepted or final asset.
- Preserve the exact prompt, model/provider identity, generation settings, inputs, and relevant rights notes.
- Generate several candidates within an explicit retry budget; do not silently iterate without limit.
- Normalize provider output to PCM WAV before deterministic QC. Preserve the untouched original when conversion is required.
- Separate mechanical checks from listening judgments. A clean waveform does not prove musical fit, semantic accuracy, originality, or a good mix.
- Avoid artist names, franchise names, protected melodies, and reference audio the user does not have rights to use.
- Do not download models, install large dependencies, spend API credit, or accept a provider license without user authority.
- Never copy files into a project's runtime or final directories during generation or QC. The bundled `select` command records manifest acceptance only.

## Workflow

1. **Inspect the target.**
   - Read the request, target-project instructions, existing audio conventions, sample rate, runtime format, naming, and asset lifecycle.
   - Reuse established providers and project scripts before introducing another backend.

2. **Write a structured brief.**
   - Choose one audio mode and define `event_id` or `zone_id`, bus role, intended player feedback, duration, loop behavior, variation count, perspective, material or instrumentation, and exclusions.
   - For adaptive families, define a `family_id`, BPM, key/mode, meter, phrase length, sync anchor, transition points, and each member's role, duration, loop behavior, and variation count.
   - Read `references/briefs-and-prompts.md`.

3. **Choose a provider deliberately.**
   - Match music versus SFX, available hardware, license, installation cost, and required control.
   - Prefer a zero-API-cost local backend when it satisfies the request. Read `references/providers.md`.
   - Keep the brief and bundle contract provider-neutral so a backend can be replaced without redesigning the Skill.

4. **Initialize the bundle before generation.**
   - For a single-member bundle, run:

     `python scripts/audio_asset.py init <bundle> --asset-id <id> --mode <mode> --intended-use "<use>" --provider <provider> --model <model> --prompt-file <prompt.txt> --target-duration <seconds> [--variations <n>] [--event-id <id>] [--bus-role <role>]`

   - For `music_family`, replace the global duration/loop options with `--members-file <members.json>` and pass shared musical metadata. Each member must define `id`, `role`, `target_duration_seconds`, `loop`, and `variations`. Use `references/music-family-members.example.json` as the minimal member-file example.
   - Keep prompts, exact provider requests/settings, reference inputs, and untouched provider output under `source/`. Normalize working candidates into `processed/`.
   - For a managed project, place the bundle outside engine imports or behind the project's ignore mechanism.

5. **Generate bounded candidates.**
   - Save the provider command/request, seed when exposed, model revision, settings, and raw output. Pass their paths and values to `init` when available.
   - Stop when the requested candidate count is reached or the retry budget is exhausted.
   - If the backend cannot meet a hard constraint, report it instead of fabricating compliance.

6. **Normalize and run mechanical QC.**
   - Convert non-PCM output to PCM WAV with the project's FFmpeg/SoX workflow while retaining the original.
   - Run:

     `python scripts/audio_asset.py qc <bundle>/asset-manifest.json <bundle>/processed/<file>.wav [--member-id <id>] [--source-file <raw-file>]`

   - QC reads duration, loop, sample-rate, and channel constraints from the selected member and shared audio contract. Review format, clipping, silence, DC offset, and loop-boundary diagnostics. Read `references/bundle-and-qc.md`.

7. **Listen in the intended context.**
   - Audition all passing candidates against representative gameplay, not in isolation only.
   - Check semantic fit, repetition fatigue, unintended speech/music, musical structure, loop seam, mix space, and suspicious similarity.
   - Keep `human_review` pending until a person makes the relevant quality and rights decision.

8. **Select explicitly when runtime use is intended.**
   - Record the responsible selector and reason:

     `python scripts/audio_asset.py select <bundle>/asset-manifest.json <passing.wav> [<passing.wav> ...] --selected-by "<owner>" --reason "<decision>"`

   - Selection requires the declared variation count for every member, writes `runtime_candidates` and `selection_history`, and advances only to `accepted_for_runtime`.
   - It does not copy runtime files or satisfy `human_reviewed_final`.

9. **Return or hand off.**
   - For a standalone request, return the candidates, prompt/provider provenance, QC summary, and a concise audition note.
   - For engine integration, hand the accepted `asset-manifest.json` and its `runtime_candidates` to `$godot-2d-implementation`; do not wire them here.
   - For replacement or release work, follow the project's asset lifecycle and `references/rights-and-release.md`.

## Managed Bundle

```text
<asset-or-run-id>/
  source/
    prompt-used.txt
    provider-request.json
    original-output.*
  processed/
  preview/
  asset-manifest.json
```

Keep original provider files when normalization changes them. Add an audition playlist or waveform preview only when it materially helps comparison.

## Bundled Tool

`scripts/audio_asset.py` is standard-library-only and provides:

- `init`: create a traceable bundle and manifest before generation
- `qc`: inspect one member's PCM WAV candidate and record deterministic measurements
- `select`: record an accountable, complete runtime selection without copying files
- `self-test`: verify the generic manifest, per-member family constraints, QC, and selection guards

The tool does not generate audio, judge taste, claim `human_reviewed_final`, copy runtime assets, or modify engine projects.

## Output Contract

Report:

- audio mode, intended use, provider/model, and candidate count
- bundle and candidate paths
- mechanical QC results and any failed constraints
- listening status and what remains a human judgment
- provenance and rights gaps
- `runtime_candidates`, selection owner/reason, and engine handoff, only when selection was actually recorded
