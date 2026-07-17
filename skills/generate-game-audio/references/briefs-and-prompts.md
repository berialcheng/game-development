# Briefs And Prompts

## Contents

- SFX Brief
- Music Brief
- Music Families
- Variation Banks
- Prompt Safety
- Acceptance Before Generation

Write a structured brief before a prose prompt. The brief is the stable contract; provider-specific prompt wording is replaceable.

## SFX Brief

```yaml
asset_id: sfx_coin_pickup_v001
mode: sfx_variation_bank
event_id: player.coin_collected
bus_role: SFX
event: player collects a common coin
function: fast positive confirmation without masking combat
source: small bronze coin
action: lands on polished stone with two decreasing bounces
perspective: close
space: dry, minimal reverb
duration_seconds: 0.65
variations: 6
loop: false
target_sample_rate_hz: 48000
target_channels: 1
exclude: [music, speech, crowd, long_reverb, distortion]
```

Describe the physical cause, material, action, distance, space, envelope, gameplay function, and exclusions. For repeated events, specify what remains invariant and what may vary.

Prompt pattern:

```text
<duration> game sound effect: <source> <action> on/through <material>,
<perspective>, <space>, <attack/decay>, suitable for <game function>.
No <unwanted content>.
```

## Music Brief

```yaml
asset_id: music_cave_explore_v001
mode: music_loop
zone_id: cave_observatory
bus_role: Music
scene: safe but mysterious underground observatory
function: sustain exploration without masking UI or hazards
duration_seconds: 90
loop: true
bpm: 96
key_mode: D Dorian
meter: 4/4
phrase_bars: 8
sync_anchor: bar_1_beat_1
target_sample_rate_hz: 48000
target_channels: 2
instrumentation: [muted_plucked_strings, soft_analog_pulse, sparse_percussion]
structure: stable loop, no intro, no outro, no climax
exclude: [vocals, spoken_words, recognizable_melody]
```

Describe function, duration, loop behavior, tempo, key/mode, meter, mood, instrumentation, density, structure, mix space, and exclusions.

Prompt pattern:

```text
<duration> seamless instrumental <game function> loop, <BPM>, <key/mode>, <meter>.
<scene and emotion>. <instrumentation and density>. <structure>.
Leave space for <important gameplay audio>. No <unwanted content>.
```

## Music Families

Use one shared musical contract plus explicit per-member constraints. Do not give an intro, loop, and outro one global duration or loop flag.

Example `members.json`:

```json
[
  {
    "id": "intro",
    "role": "intro",
    "target_duration_seconds": 8,
    "loop": false,
    "variations": 1
  },
  {
    "id": "explore_loop",
    "role": "loop",
    "target_duration_seconds": 64,
    "loop": true,
    "variations": 1
  },
  {
    "id": "danger_layer",
    "role": "intensity_layer",
    "target_duration_seconds": 64,
    "loop": true,
    "variations": 1
  }
]
```

The same structure is available as [music-family-members.example.json](music-family-members.example.json).

Pair it with `family_id`, BPM, key/mode, meter, phrase bars, sync anchor, sample rate, and channel count in the manifest.

For intro/loop/outro, layers, stems, or intensity variants, keep these shared unless the design explicitly calls for change:

- BPM, sample rate, key/mode, tuning, and meter
- bar count and phrase boundaries
- downbeat alignment and tail policy
- harmonic rhythm and transition chord
- instrumentation roles and stem naming
- render start point and silence/pre-roll policy

Generation can propose related assets, but phase alignment and transition quality require deterministic editing and runtime listening.

## Variation Banks

For footsteps, impacts, pickups, attacks, and other repeated events:

- keep semantic identity, loudness family, perspective, and duration range coherent
- vary micro-timing, pitch/timbre, transient shape, and detail within a bounded range
- reject variants with different room tone, hidden speech/music, or a different perceived material
- plan runtime anti-repetition separately; the asset Skill does not implement randomization

## Prompt Safety

- Describe audio properties rather than naming an artist, composer, game, film, or protected character.
- Use only reference audio the user owns or is authorized to process.
- Treat negative prompts as requests, not guarantees; verify the rendered audio.
- Do not hide known provenance or similarity concerns in a rewritten prompt.

## Acceptance Before Generation

Define:

- candidate count and retry ceiling
- hard constraints: duration, loop, format, family alignment, or maximum tail
- stable runtime identity: `event_id`, `zone_id`, `bus_role`, and `family_id` when applicable
- listening criteria in the actual game context
- what would cause a provider switch
- whether the result is a placeholder, runtime candidate, or potential shipping asset
