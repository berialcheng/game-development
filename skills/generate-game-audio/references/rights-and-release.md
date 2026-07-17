# Rights And Release

This is a production checklist, not legal advice. Licenses and hosted terms change; save the exact terms/model-card version used for any candidate that may ship.

## Four Separate Questions

Check all four:

1. May the code and model weights be used for this purpose?
2. Do hosted-service terms allow the output in this game and distribution model?
3. Does the user have rights to every prompt/reference/input?
4. Is the specific output sufficiently original and non-infringing for the intended release?

A permissive code license does not answer model-weight or output questions.

## Current Local-Model Starting Points

At the time this Skill was authored (2026-07-18):

- ACE-Step 1.5 advertised an MIT-licensed local music stack.
- MOSS-SoundEffect advertised Apache-2.0 project/model licensing.
- Stable Audio 3 used the Stability AI Community License, with eligibility conditions rather than unconditional permissive use.

Treat those as routing clues only. Recheck the exact repository, model revision, weight license, and current eligibility before promotion. Do not use a non-commercial weight for a shipping commercial asset merely because its surrounding code is MIT or Apache.

## Hosted Providers

Before any paid or free-tier API call, confirm:

- the user's account/tier covers commercial game use
- music and sound-effect terms are checked separately
- platform count, game/studio definitions, attribution, redistribution, and training clauses
- whether generated files may be embedded but not resold as an audio library
- retention/privacy terms for uploaded references
- the effective date and a saved link or snapshot

Free credits rarely prove shipping rights.

## Prompt And Similarity Controls

- Do not request imitation of a living artist, named composer, franchise, or recognizable theme.
- Do not upload reference music/recordings without documented authority.
- Use musical/audio properties: tempo, mode, meter, instrumentation, material, perspective, space, envelope, density, and function.
- Listen for recognizable melodic, lyrical, voice, or recording similarity before promotion.
- Escalate ambiguity to the user; do not convert uncertainty into a definitive rights claim.

## Asset Record

For a potential shipping asset preserve:

- asset ID and lifecycle state
- exact prompt and negative constraints
- provider, model, revision, seed/settings, generation time, and account/tier when relevant
- input/reference ownership
- raw and processed SHA-256
- normalization/editing history
- license/terms links or snapshot and effective date
- human listening/similarity review
- release decision, reviewer, and date

## Platform Disclosure

When preparing a Steam release, review the current Steamworks content survey and AI-content disclosure requirements. Pre-generated audio bundled with the game and live-generated audio may create different disclosure and safety obligations.

Prefer development-time generation for ordinary game assets. Do not add runtime generation unless the user explicitly requests it and the project has addressed latency, determinism, moderation, privacy, cost, offline behavior, and platform policy.

## Promotion Gate

Do not mark `human_reviewed_final` until:

- intended-context listening is complete
- model/provider/input rights are documented
- similarity concerns are resolved
- runtime export and loop/transition behavior are validated
- current platform disclosures have been reviewed
