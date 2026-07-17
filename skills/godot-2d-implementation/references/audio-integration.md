# Godot Audio Integration

## Contents

- Intake Gate
- Preserve Project Conventions
- Player And Bus Roles
- Event Contract
- Loops And Music Families
- Runtime Validation
- Handoff Result

Use this reference after an audio candidate has been selected. Generate or revise the source asset with `$generate-game-audio`; keep this skill responsible for Godot import, playback architecture, event wiring, mix behavior, and runtime evidence.

## Intake Gate

Require:

- `asset-manifest.json` with `source_skill: generate-game-audio` and `lifecycle_state: accepted_for_runtime`
- non-empty `runtime_candidates` backed by passing candidate records and an accountable `selection_history` entry
- `event_id` or `zone_id`, `bus_role`, and intended event/scene
- target sample rate/channels plus each member's ID, role, duration, loop flag, and variation count
- family ID and BPM/key/meter/phrase/sync metadata for music families
- unresolved seam, listening, similarity, or rights risks

Reject a handoff that names an arbitrary processed file but does not list it in `runtime_candidates`. Do not import an entire generation bundle. Copy only accepted runtime candidates into the project's established audio path and keep source, prompts, previews, rejected candidates, and the evidence manifest outside Godot imports unless the project explicitly stores manifests.

`accepted_for_runtime` is sufficient for prototype integration but is not `human_reviewed_final`. Preserve `human_review: pending` and rights gaps in the implementation result.

## Preserve Project Conventions

Inspect before changing:

- existing audio folders, naming, import defaults, and runtime codec
- autoloads/audio managers and ownership boundaries
- buses, effects, volume settings, mute/pause behavior, and accessibility controls
- signal/event flow and scene-local versus global playback
- current sample rate, loudness relationships, and polyphony limits

Extend established architecture when it works. Do not add an audio manager, middleware layer, or new bus hierarchy for one local sound.

## Player And Bus Roles

Use the lightest fitting node:

- `AudioStreamPlayer`: non-positional music, UI, narration, and global feedback
- `AudioStreamPlayer2D`: positional 2D world sounds with deliberate attenuation
- project-native wrapper/pool: only when it already exists or repeated playback needs it

Prefer existing buses. When the project has no convention and the scope justifies separation, typical roles are `Music`, `SFX`, `UI`, and `Ambience`. Route first, then tune relative levels in context; do not bake all mix decisions destructively into source files.

## Event Contract

For each sound, define:

```text
gameplay event -> owner -> playback call -> stream/variation -> bus -> stop/fade rule
```

Avoid coupling unrelated systems directly to an audio node. Reuse signals or the project's event boundary. Specify retrigger, overlap, cooldown, maximum voices, and cleanup for frequently fired sounds.

Use manifest IDs as handoff keys when they match project conventions; map them explicitly when the project uses a different event or bus registry. Do not infer a gameplay event from a filename when `event_id` or `zone_id` is present.

For variation banks:

- use only mechanically and semantically accepted variants
- avoid immediate repetition when the bank has alternatives
- keep random choice reproducible in deterministic tests
- constrain pitch/volume jitter; it should not replace real variants
- cap simultaneous voices for spam-prone events

## Loops And Music Families

For loops:

- verify Godot's imported stream and loop setting, not only source metadata
- test several real loop boundaries at runtime
- preserve authored loop points when the chosen format/import path supports them
- use an intentional crossfade or edited boundary when it does not
- confirm pause, scene change, and stop behavior do not click or leak playback

For intro/loop/outro, stems, or intensity layers:

- keep streams aligned to the same sample rate and render origin
- schedule transitions at explicit musical boundaries
- crossfade with one owner; do not let scene changes start competing players
- test rapid state changes, interruption, resume, and fallback when a stream is missing
- escalate broad adaptive-music design to `$game-production-orchestrator`

## Runtime Validation

Minimum useful evidence combines mechanical and audible behavior:

1. Godot imports and loads the selected runtime file without errors.
2. The intended event triggers the intended player and bus.
3. Looping, stop/fade, pause, and scene transitions behave as specified.
4. Variation/retrigger/polyphony behavior survives a deterministic stress scenario.
5. A representative runtime recording or direct listening pass checks semantic fit, seam, balance, masking, and repetition fatigue.

A screenshot proves node/layout state, not sound. Headless startup proves import/load only. Record the Godot version, scenario, event counts when relevant, and the human listening status.

## Handoff Result

Report:

- source manifest, selection record, and accepted `runtime_candidates`
- runtime export/import path and encoding
- nodes/resources/scripts/settings changed
- manifest-to-project event, zone, family, member, and bus mapping
- deterministic checks and runtime scenario
- what was actually listened to or recorded
- unresolved mix, seam, rights, or accessibility risk
