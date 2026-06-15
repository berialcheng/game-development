# Playtest Observability Reference

Use this reference for deterministic playtest runs, structured logs, run manifests, metrics, counters, and regression evidence.

## Purpose

Unattended optimization needs evidence. A passing startup command proves the project loads; it does not prove the game is readable, stable, fair, or still fun. Prefer structured run output whenever behavior, balance, effects, UI, or performance changes.

## Run Manifest Contract

When a project supports automation, each run should write a JSON manifest with:

```json
{
  "schema_version": 1,
  "project": "game",
  "scenario": "combat_baseline",
  "seed": 12345,
  "godot_version": "4.x",
  "started_at": "ISO-8601",
  "duration_seconds": 30.0,
  "result": "pass",
  "captures": [
    {
      "label": "combat_10s",
      "path": "screenshot/automation/combat_10s.png",
      "absolute_path": "C:/repo/game/screenshot/automation/combat_10s.png",
      "requested": true,
      "saved": true,
      "error": 0,
      "time_seconds": 10.0
    }
  ],
  "events": {
    "enemy_spawned": 30,
    "enemy_killed": 22,
    "player_hit": 2,
    "level_up": 1,
    "effect_spawned": 80,
    "damage_number_spawned": 45
  },
  "metrics": {
    "player_hp_end": 72,
    "xp_gained": 40,
    "coins_gained": 12,
    "max_enemies_alive": 18,
    "max_projectiles_alive": 35,
    "max_effects_alive": 24,
    "max_damage_numbers_alive": 14
  },
  "warnings": [],
  "errors": []
}
```

Use the repository's existing schema if one exists. Do not introduce a competing schema without a clear migration reason.

## Metrics To Prefer

Gameplay:

- player damage taken
- enemies spawned/killed/alive
- level-ups
- pickups collected/missed
- wave duration
- ability casts and cooldown failures

Readability/effects:

- max active effects
- max active damage numbers
- telegraph events shown before attacks
- camera shake events and duration
- screenshot capture labels

Economy/progression:

- XP gained
- coins gained
- shop refreshes
- item choices offered
- drop counts by rarity

Stability/performance proxies:

- run duration
- warnings/errors
- object counts
- effect spawn counts
- dropped or missing captures
- frame-time or FPS if the project already records it

Screenshot/capture reliability:

- capture requested
- capture saved
- save error code
- absolute path used for saving
- nonzero file size if the verifier checks files

## Regression Rules

Compare against a baseline when available:

- Missing screenshot label: fail.
- Screenshot requested but not saved: fail.
- Screenshot manifest says saved but the PNG is missing or empty: fail.
- Missing manifest key used by tests: fail.
- New load error or script error: fail.
- Event count unexpectedly zero for the feature under test: fail.
- Effect/object count exceeds budget: warn or fail based on project policy.
- Gameplay metric drift outside accepted tolerance: warn or fail.

Do not fail a run for subjective visual taste unless a human-approved baseline or explicit threshold exists.

## Reporting

When using automation evidence, report:

- scenario and seed
- command run
- captures produced
- key metric deltas
- warnings/errors
- what still requires human review

If no automation exists, state the missing instrumentation that would make the next iteration safer.
