# Provider Selection

Provider capabilities, model licenses, hosted-service terms, and hardware support change. Recheck the official repository/model card and save the relevant version before a release asset is promoted.

## Default Routing

| Need | Practical first choice | Why | Main gate |
| --- | --- | --- | --- |
| Music without a supported GPU | Stable Audio 3 Small-Music | Local CPU path and one tool family for music/SFX | Generation speed and Community License eligibility |
| Music with a capable local GPU | ACE-Step 1.5 | Music-specific structure, duration, and control | Model/revision availability and hardware |
| Lightweight local SFX | Stable Audio 3 Small-SFX | Small local model and simple initial integration | Semantic quality for the event |
| Higher-quality GPU SFX | MOSS-SoundEffect v2 | Dedicated text-to-SFX path | Heavier setup and hardware |
| Existing approved hosted provider | Project's current API | Avoids another local stack | Credit, output rights, privacy, and service terms |

This is routing guidance, not permission to install, download, call, or accept terms.

## Zero-API-Cost Baseline

Start with:

```text
music -> Stable Audio 3 Small-Music
SFX   -> Stable Audio 3 Small-SFX
```

This gives the Skill one local backend family and keeps the brief, bundle, QC, and engine handoff stable. If music quality is insufficient and suitable hardware exists, replace only the music backend with ACE-Step. Add MOSS only when SFX quality justifies its installation cost.

Local does not mean costless: account for model downloads, disk, compute time, electricity, and manual audition.

## Execution Entry Points

Probe before installing or launching anything: `Get-Command stable-audio, uv, ffmpeg, ffprobe, sox, nvidia-smi -ErrorAction SilentlyContinue` on PowerShell, or the platform equivalent.

For an already installed Stable Audio 3 checkout, the official CLI shape is:

```powershell
stable-audio --model small-music -p "<prompt>" --duration 60 -o source/music_c01.wav
stable-audio --model small-sfx -p "<prompt>" --duration 1 -o source/sfx_c01.wav
```

For ACE-Step, `uv run acestep-api` starts the official local API. Read the API guide from the exact checked-out revision before sending requests and save the request payload. For MOSS-SoundEffect v2, use the commands in the checked-out `moss_soundeffect_v2/README.md`; do not freeze a volatile environment command into this shared Skill.

## Backend Gates

Before choosing a provider, record:

- exact repository or service and model revision
- music/SFX support, duration limits, sample rate, channels, and controllable fields
- expected hardware, storage, and dependency footprint
- whether the target machine has already been validated
- code license, model-weight license, service terms, and output-use terms
- reference-input rights and data sent to a hosted service
- reproducibility controls such as seed and deterministic mode
- whether commercial use and the intended distribution platforms are covered

Do not infer model-weight rights from a repository's code license. Projects such as MusicGen/AudioCraft can have permissive code while published weights use non-commercial terms.

## Provider-Neutral Adapter Contract

Keep provider execution outside the manifest tool. A backend adapter or project command should accept:

```text
prompt
negative constraints, when supported
target duration
candidate count
seed, when supported
mode-specific controls (BPM/key/meter/loop or SFX intensity)
output directory
```

It should return raw files plus the exact request/settings needed for provenance. Always preserve untouched provider output under `source/`. Write only normalized working candidates into `processed/`, then associate each with its raw source through `audio_asset.py qc --source-file`.

## Output Normalization

- Preserve the provider's untouched output.
- Convert a working master to uncompressed PCM WAV under `processed/` before `audio_asset.py qc`.
- Use the project's target sample rate, normally 44.1 or 48 kHz, and do not mix rates accidentally.
- Defer Ogg/Opus runtime export until a candidate is accepted for engine integration.
- Never claim a seamless loop from a text prompt alone; inspect and listen to the rendered boundary.

## Failure And Fallback

- If a provider cannot obey duration or structure, flag the hard constraint and switch only with user authority.
- If local generation is too slow, reduce candidate scope before proposing paid API use.
- If a model's commercial rights are unclear, keep output as non-shipping research/placeholder material.
- If all backends fail the acceptance criteria, return the brief, failed evidence, and the smallest useful fallback: licensed library audio, recording, procedural synthesis, or a sound designer.

## Official Starting Points

- Stable Audio 3: <https://github.com/Stability-AI/stable-audio-3>
- ACE-Step 1.5: <https://github.com/ace-step/ACE-Step-1.5>
- MOSS-SoundEffect v2 code: <https://github.com/OpenMOSS/MOSS-TTS/tree/main/moss_soundeffect_v2>
- MOSS-SoundEffect v2 model card: <https://huggingface.co/OpenMOSS-Team/MOSS-SoundEffect-v2.0>
