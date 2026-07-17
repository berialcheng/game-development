#!/usr/bin/env python3
"""Create traceable game-audio bundles and mechanically inspect PCM WAV candidates."""

from __future__ import annotations

import argparse
import array
import hashlib
import json
import math
import re
import shutil
import struct
import sys
import tempfile
import wave
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MODES = (
    "music_loop",
    "music_cue",
    "music_family",
    "stinger",
    "sfx_one_shot",
    "sfx_variation_bank",
    "ambience_loop",
)
ASSET_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
EDITABLE_STATES = {"raw_generated", "processed_candidate"}
SELECTABLE_STATES = {"processed_candidate", "accepted_for_runtime"}
LOOP_MODES = {"music_loop", "ambience_loop"}
DEFAULT_MEMBER_ROLES = {
    "music_loop": "loop",
    "music_cue": "cue",
    "stinger": "stinger",
    "sfx_one_shot": "one_shot",
    "sfx_variation_bank": "variation",
    "ambience_loop": "ambience",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, payload: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return value


def relative_bundle_path(path: Path, root: Path, label: str) -> str:
    resolved = path.resolve()
    try:
        relative = resolved.relative_to(root.resolve())
    except ValueError as error:
        raise ValueError(f"{label} must be inside {root}") from error
    return f"{root.name}/{relative.as_posix()}"


def optional_text(value: str | None) -> str | None:
    if value is None:
        return None
    stripped = value.strip()
    return stripped or None


def validate_positive(value: int | float | None, label: str) -> None:
    if value is not None and (
        not isinstance(value, (int, float))
        or isinstance(value, bool)
        or value <= 0
    ):
        raise ValueError(f"{label} must be greater than zero")


def normalize_members(
    *,
    mode: str,
    members: list[dict[str, Any]] | None,
    target_duration: float | None,
    loop: bool,
    variations: int,
) -> list[dict[str, Any]]:
    if mode == "music_family":
        if members is None:
            raise ValueError("music_family requires --members-file")
        if target_duration is not None or loop or variations != 1:
            raise ValueError(
                "music_family uses per-member duration, loop, and variations; "
                "remove global --target-duration/--loop/--variations"
            )
        raw_members = members
    else:
        if members is not None:
            raise ValueError("--members-file is only valid for music_family")
        validate_positive(target_duration, "target duration")
        if variations < 1:
            raise ValueError("variations must be at least one")
        raw_members = [
            {
                "id": "main",
                "role": DEFAULT_MEMBER_ROLES[mode],
                "target_duration_seconds": target_duration,
                "loop": bool(loop or mode in LOOP_MODES),
                "variations": variations,
            }
        ]

    if not raw_members:
        raise ValueError("audio members cannot be empty")

    normalized: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for index, member in enumerate(raw_members):
        if not isinstance(member, dict):
            raise ValueError(f"member {index} must be a JSON object")
        member_id = member.get("id")
        role = member.get("role")
        duration = member.get("target_duration_seconds")
        member_loop = member.get("loop")
        member_variations = member.get("variations", 1)
        if not isinstance(member_id, str) or not ASSET_ID_RE.fullmatch(member_id):
            raise ValueError(f"member {index} has an invalid id")
        if member_id in seen_ids:
            raise ValueError(f"duplicate member id: {member_id}")
        if not isinstance(role, str) or not role.strip():
            raise ValueError(f"member {member_id} requires a non-empty role")
        validate_positive(duration, f"member {member_id} target duration")
        if not isinstance(member_loop, bool):
            raise ValueError(f"member {member_id} loop must be true or false")
        if (
            not isinstance(member_variations, int)
            or isinstance(member_variations, bool)
            or member_variations < 1
        ):
            raise ValueError(f"member {member_id} variations must be at least one")
        normalized.append(
            {
                "id": member_id,
                "role": role.strip(),
                "target_duration_seconds": round(float(duration), 6),
                "loop": member_loop,
                "variations": member_variations,
            }
        )
        seen_ids.add(member_id)
    return normalized


def read_members_file(path: Path | None) -> list[dict[str, Any]] | None:
    if path is None:
        return None
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list):
        raise ValueError("members file must contain a JSON array")
    return value


def copy_provenance_file(
    source: Path | None,
    bundle: Path,
    stem: str,
) -> str | None:
    if source is None:
        return None
    source = source.resolve()
    if not source.is_file():
        raise FileNotFoundError(f"provenance file not found: {source}")
    suffix = source.suffix or ".txt"
    destination = bundle / "source" / f"{stem}{suffix}"
    shutil.copy2(source, destination)
    return relative_bundle_path(destination, bundle / "source", "provenance file")


def read_prompt(prompt: str | None, prompt_file: Path | None) -> str:
    if prompt_file is not None:
        value = prompt_file.read_text(encoding="utf-8")
    elif prompt is not None:
        value = prompt
    else:
        raise ValueError("provide --prompt or --prompt-file")
    if not value.strip():
        raise ValueError("prompt cannot be empty")
    return value


def init_bundle(
    bundle: Path,
    *,
    asset_id: str,
    mode: str,
    intended_use: str,
    provider: str,
    model: str,
    prompt_text: str,
    members: list[dict[str, Any]] | None,
    target_duration: float | None,
    loop: bool,
    variations: int,
    rights_notes: str,
    model_revision: str = "unspecified",
    seed: int | None = None,
    request_file: Path | None = None,
    settings_file: Path | None = None,
    event_id: str | None = None,
    zone_id: str | None = None,
    bus_role: str | None = None,
    family_id: str | None = None,
    bpm: float | None = None,
    key_mode: str | None = None,
    meter: str | None = None,
    phrase_bars: int | None = None,
    sync_anchor: str | None = None,
    target_sample_rate: int | None = None,
    target_channels: int | None = None,
    force: bool = False,
) -> Path:
    if not ASSET_ID_RE.fullmatch(asset_id):
        raise ValueError(
            "asset ID must start with an alphanumeric character and contain only "
            "letters, numbers, dot, underscore, or hyphen"
        )
    if mode not in MODES:
        raise ValueError(f"unsupported mode: {mode}")
    if not intended_use.strip():
        raise ValueError("intended use cannot be empty")
    if not provider.strip():
        raise ValueError("provider cannot be empty")
    validate_positive(bpm, "BPM")
    validate_positive(phrase_bars, "phrase bars")
    validate_positive(target_sample_rate, "target sample rate")
    validate_positive(target_channels, "target channels")
    normalized_members = normalize_members(
        mode=mode,
        members=members,
        target_duration=target_duration,
        loop=loop,
        variations=variations,
    )

    bundle = bundle.resolve()
    manifest_path = bundle / "asset-manifest.json"
    prompt_path = bundle / "source" / "prompt-used.txt"
    if not force and (manifest_path.exists() or prompt_path.exists()):
        raise FileExistsError(
            f"bundle metadata already exists: {bundle}; use --force only when "
            "you intentionally want to reinitialize it"
        )
    if force and bundle.exists():
        replaceable = {manifest_path.resolve(), prompt_path.resolve()}
        protected_files = [
            path
            for path in bundle.rglob("*")
            if path.is_file() and path.resolve() not in replaceable
        ]
        if protected_files:
            names = ", ".join(
                path.relative_to(bundle).as_posix() for path in protected_files[:3]
            )
            raise FileExistsError(
                "refusing to reinitialize a bundle with source/processed/preview "
                f"files ({names}); create a new bundle or preserve the manifest"
            )

    for child in ("source", "processed", "preview"):
        (bundle / child).mkdir(parents=True, exist_ok=True)
    prompt_path.write_text(prompt_text, encoding="utf-8")
    request_relative = copy_provenance_file(
        request_file,
        bundle,
        "provider-request",
    )
    settings_relative = copy_provenance_file(
        settings_file,
        bundle,
        "provider-settings",
    )
    source_files = sorted(
        path
        for path in (request_relative, settings_relative)
        if path is not None
    )
    now = utc_now()

    manifest: dict[str, Any] = {
        "schema_version": 1,
        "media_type": "audio",
        "asset_id": asset_id,
        "source_skill": "generate-game-audio",
        "lifecycle_state": "raw_generated",
        "intended_use": intended_use,
        "generation": {
            "provider": provider.strip(),
            "model": optional_text(model) or "unspecified",
            "revision": optional_text(model_revision) or "unspecified",
            "seed": seed,
            "request_file": request_relative,
            "settings_file": settings_relative,
        },
        "audio": {
            "mode": mode,
            "event_id": optional_text(event_id),
            "zone_id": optional_text(zone_id),
            "bus_role": optional_text(bus_role),
            "family_id": (
                optional_text(family_id)
                or (asset_id if mode == "music_family" else None)
            ),
            "bpm": bpm,
            "key_mode": optional_text(key_mode),
            "meter": optional_text(meter),
            "phrase_bars": phrase_bars,
            "sync_anchor": optional_text(sync_anchor),
            "target_sample_rate_hz": target_sample_rate,
            "target_channels": target_channels,
            "members": normalized_members,
        },
        "prompt_files": ["source/prompt-used.txt"],
        "source_files": source_files,
        "processed_files": [],
        "preview_files": [],
        "runtime_candidates": [],
        "candidates": {},
        "selection_history": [],
        "qc": {
            "last_checked_utc": None,
            "passed": 0,
            "failed": 0,
        },
        "human_review": "pending",
        "rights_notes": rights_notes or "pending",
        "created_utc": now,
        "updated_utc": now,
    }
    write_json(manifest_path, manifest)
    return manifest_path


def pcm_values(data: bytes, sample_width: int) -> list[float]:
    if sample_width not in (1, 2, 3, 4):
        raise ValueError(f"unsupported PCM sample width: {sample_width} bytes")
    if len(data) % sample_width:
        raise ValueError("PCM payload is not aligned to the sample width")

    if sample_width == 1:
        result8: list[float] = []
        for value in data:
            signed = value - 128
            result8.append(signed / (128.0 if signed < 0 else 127.0))
        return result8

    if sample_width == 2:
        values = array.array("h")
        values.frombytes(data)
        if sys.byteorder != "little":
            values.byteswap()
        return [value / 32768.0 for value in values]

    if sample_width == 3:
        result: list[float] = []
        for offset in range(0, len(data), 3):
            value = int.from_bytes(data[offset : offset + 3], "little", signed=True)
            result.append(value / 8388608.0)
        return result

    values32 = array.array("i")
    values32.frombytes(data)
    if sys.byteorder != "little":
        values32.byteswap()
    return [value / 2147483648.0 for value in values32]


def dbfs(amplitude: float) -> float | None:
    if amplitude <= 0:
        return None
    return round(20.0 * math.log10(amplitude), 6)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def analyze_wav(
    path: Path,
    *,
    silence_threshold_dbfs: float,
    seam_ms: float,
    clip_threshold: float = 0.999,
) -> dict[str, Any]:
    if seam_ms <= 0:
        raise ValueError("seam window must be greater than zero")
    silence_amplitude = 10.0 ** (silence_threshold_dbfs / 20.0)

    with wave.open(str(path), "rb") as wav_file:
        if wav_file.getcomptype() != "NONE":
            raise ValueError("only uncompressed PCM WAV is supported")
        channels = wav_file.getnchannels()
        sample_rate = wav_file.getframerate()
        sample_width = wav_file.getsampwidth()
        frame_count = wav_file.getnframes()
        if channels < 1 or sample_rate < 1 or frame_count < 1:
            raise ValueError("WAV must contain at least one channel and one frame")

        seam_frames = max(1, round(sample_rate * seam_ms / 1000.0))
        seam_samples = seam_frames * channels
        first_samples: list[float] = []
        last_samples: deque[float] = deque(maxlen=seam_samples)

        sample_count = 0
        peak = 0.0
        sum_square = 0.0
        sum_value = 0.0
        clipped = 0
        silent = 0

        while True:
            payload = wav_file.readframes(65536)
            if not payload:
                break
            values = pcm_values(payload, sample_width)
            needed = seam_samples - len(first_samples)
            if needed > 0:
                first_samples.extend(values[:needed])
            last_samples.extend(values)
            for value in values:
                absolute = abs(value)
                sample_count += 1
                peak = max(peak, absolute)
                sum_square += value * value
                sum_value += value
                if absolute >= clip_threshold:
                    clipped += 1
                if absolute <= silence_amplitude:
                    silent += 1

    if sample_count != frame_count * channels:
        raise ValueError("decoded sample count does not match WAV metadata")

    rms = math.sqrt(sum_square / sample_count)
    last_list = list(last_samples)
    first_rms = math.sqrt(sum(value * value for value in first_samples) / len(first_samples))
    last_rms = math.sqrt(sum(value * value for value in last_list) / len(last_list))

    boundary_differences = []
    for channel in range(channels):
        first_value = first_samples[channel]
        last_value = last_list[len(last_list) - channels + channel]
        boundary_differences.append(abs(first_value - last_value))
    boundary_jump = sum(boundary_differences) / len(boundary_differences)

    first_db = dbfs(first_rms)
    last_db = dbfs(last_rms)
    seam_rms_delta = (
        round(abs(first_db - last_db), 6)
        if first_db is not None and last_db is not None
        else None
    )

    return {
        "sha256": file_sha256(path),
        "bytes": path.stat().st_size,
        "format": "PCM_WAV",
        "channels": channels,
        "sample_rate_hz": sample_rate,
        "bit_depth": sample_width * 8,
        "frame_count": frame_count,
        "duration_seconds": round(frame_count / sample_rate, 6),
        "peak_dbfs": dbfs(peak),
        "rms_dbfs": dbfs(rms),
        "clipped_samples": clipped,
        "clipped_ratio": round(clipped / sample_count, 9),
        "silence_threshold_dbfs": silence_threshold_dbfs,
        "near_silence_ratio": round(silent / sample_count, 9),
        "dc_offset": round(sum_value / sample_count, 9),
        "seam_window_ms": seam_ms,
        "seam_first_rms_dbfs": first_db,
        "seam_last_rms_dbfs": last_db,
        "seam_rms_delta_db": seam_rms_delta,
        "boundary_jump": round(boundary_jump, 9),
        "boundary_jump_to_peak_ratio": (
            round(boundary_jump / peak, 9) if peak > 0 else None
        ),
    }


def audio_members(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    required = {
        "schema_version",
        "media_type",
        "asset_id",
        "source_skill",
        "lifecycle_state",
        "intended_use",
        "prompt_files",
        "source_files",
        "processed_files",
        "preview_files",
        "runtime_candidates",
        "candidates",
        "selection_history",
        "qc",
        "human_review",
        "rights_notes",
        "generation",
        "audio",
    }
    missing = sorted(required.difference(manifest))
    if missing:
        raise ValueError(f"manifest is missing generic fields: {', '.join(missing)}")
    if manifest.get("schema_version") != 1:
        raise ValueError("unsupported or missing manifest schema_version")
    if manifest.get("media_type") != "audio":
        raise ValueError("manifest media_type must be audio")
    if manifest.get("source_skill") != "generate-game-audio":
        raise ValueError("manifest source_skill must be generate-game-audio")
    for field in (
        "prompt_files",
        "source_files",
        "processed_files",
        "preview_files",
        "runtime_candidates",
        "selection_history",
    ):
        if not isinstance(manifest.get(field), list):
            raise ValueError(f"manifest {field} field must be an array")
    if not isinstance(manifest.get("candidates"), dict):
        raise ValueError("manifest candidates field must be an object")
    if not isinstance(manifest.get("generation"), dict):
        raise ValueError("manifest generation field must be an object")
    audio = manifest.get("audio")
    if not isinstance(audio, dict):
        raise ValueError("manifest audio field must be an object")
    mode = audio.get("mode")
    if mode not in MODES:
        raise ValueError("manifest audio.mode is unsupported")
    validate_positive(audio.get("target_sample_rate_hz"), "target sample rate")
    validate_positive(audio.get("target_channels"), "target channels")
    members = audio.get("members")
    if not isinstance(members, list) or not members:
        raise ValueError("manifest audio.members must be a non-empty array")
    if mode != "music_family" and len(members) != 1:
        raise ValueError("only music_family may contain multiple members")
    seen_ids: set[str] = set()
    for index, member in enumerate(members):
        if not isinstance(member, dict):
            raise ValueError(f"manifest member {index} must be an object")
        member_id = member.get("id")
        if not isinstance(member_id, str) or not ASSET_ID_RE.fullmatch(member_id):
            raise ValueError(f"manifest member {index} has an invalid id")
        if member_id in seen_ids:
            raise ValueError(f"manifest contains duplicate member id: {member_id}")
        if not isinstance(member.get("role"), str) or not member["role"].strip():
            raise ValueError(f"manifest member {member_id} has an invalid role")
        validate_positive(
            member.get("target_duration_seconds"),
            f"member {member_id} target duration",
        )
        if not isinstance(member.get("loop"), bool):
            raise ValueError(f"manifest member {member_id} loop must be true or false")
        variations = member.get("variations")
        if (
            not isinstance(variations, int)
            or isinstance(variations, bool)
            or variations < 1
        ):
            raise ValueError(
                f"manifest member {member_id} variations must be at least one"
            )
        seen_ids.add(member_id)
    return members


def resolve_member(
    manifest: dict[str, Any],
    member_id: str | None,
) -> dict[str, Any]:
    members = audio_members(manifest)
    if member_id is None:
        if len(members) != 1:
            raise ValueError("--member-id is required when a bundle has multiple members")
        return members[0]
    for member in members:
        if member.get("id") == member_id:
            return member
    raise ValueError(f"unknown member id: {member_id}")


def qc_manifest(
    manifest_path: Path,
    candidate_path: Path,
    *,
    member_id: str | None,
    source_file: Path | None,
    expected_sample_rate: int | None,
    expected_channels: int | None,
    duration_tolerance: float,
    max_clipped_ratio: float,
    silence_threshold_dbfs: float,
    seam_ms: float,
    force_loop_check: bool,
) -> dict[str, Any]:
    if duration_tolerance < 0:
        raise ValueError("duration tolerance cannot be negative")
    if not 0 <= max_clipped_ratio <= 1:
        raise ValueError("max clipped ratio must be between zero and one")
    validate_positive(expected_sample_rate, "expected sample rate")
    validate_positive(expected_channels, "expected channels")

    manifest_path = manifest_path.resolve()
    if not manifest_path.is_file():
        raise FileNotFoundError(f"manifest not found: {manifest_path}")
    bundle = manifest_path.parent
    candidate_path = candidate_path.resolve()
    if not candidate_path.is_file():
        raise FileNotFoundError(f"candidate not found: {candidate_path}")
    manifest_relative = relative_bundle_path(
        candidate_path,
        bundle / "processed",
        "candidate",
    )

    manifest = load_json(manifest_path)
    member = resolve_member(manifest, member_id)
    state = manifest.get("lifecycle_state")
    if state not in EDITABLE_STATES:
        raise ValueError(
            f"refusing to mutate manifest in lifecycle state {state!r}; "
            "QC candidates before explicit runtime selection"
        )
    audio = manifest["audio"]
    if expected_sample_rate is None:
        expected_sample_rate = audio.get("target_sample_rate_hz")
    if expected_channels is None:
        expected_channels = audio.get("target_channels")
    validate_positive(expected_sample_rate, "expected sample rate")
    validate_positive(expected_channels, "expected channels")

    source_relative = None
    if source_file is not None:
        source_file = source_file.resolve()
        if not source_file.is_file():
            raise FileNotFoundError(f"source file not found: {source_file}")
        source_relative = relative_bundle_path(
            source_file,
            bundle / "source",
            "source file",
        )

    metrics = analyze_wav(
        candidate_path,
        silence_threshold_dbfs=silence_threshold_dbfs,
        seam_ms=seam_ms,
    )
    failures: list[str] = []
    warnings: list[str] = []

    target_duration = member.get("target_duration_seconds")
    if isinstance(target_duration, (int, float)):
        delta = abs(metrics["duration_seconds"] - float(target_duration))
        if delta > duration_tolerance:
            failures.append(
                f"duration differs from target by {delta:.6f}s "
                f"(tolerance {duration_tolerance:.6f}s)"
            )
    if (
        expected_sample_rate is not None
        and metrics["sample_rate_hz"] != expected_sample_rate
    ):
        failures.append(
            f"sample rate is {metrics['sample_rate_hz']}Hz; "
            f"expected {expected_sample_rate}Hz"
        )
    if expected_channels is not None and metrics["channels"] != expected_channels:
        failures.append(
            f"channel count is {metrics['channels']}; expected {expected_channels}"
        )
    if metrics["clipped_ratio"] > max_clipped_ratio:
        failures.append(
            f"clipped ratio {metrics['clipped_ratio']:.9f} exceeds "
            f"{max_clipped_ratio:.9f}"
        )
    if metrics["near_silence_ratio"] > 0.5:
        warnings.append("more than half of samples are near silence; listen and inspect")

    loop_requested = bool(member.get("loop")) or force_loop_check
    if loop_requested:
        jump_ratio = metrics["boundary_jump_to_peak_ratio"]
        if jump_ratio is not None and jump_ratio > 0.25:
            warnings.append("large first/last-sample boundary jump; inspect the loop seam")
        seam_delta = metrics["seam_rms_delta_db"]
        if seam_delta is not None and seam_delta > 6.0:
            warnings.append("first/last seam-window RMS differs by more than 6 dB")

    status = "pass" if not failures else "fail"
    record = {
        "path": manifest_relative,
        "member_id": member["id"],
        "member_role": member["role"],
        "source_file": source_relative,
        "status": status,
        "checked_utc": utc_now(),
        "metrics": metrics,
        "constraints": {
            "target_duration_seconds": target_duration,
            "member_variations": member["variations"],
            "duration_tolerance_seconds": duration_tolerance,
            "expected_sample_rate_hz": expected_sample_rate,
            "expected_channels": expected_channels,
            "max_clipped_ratio": max_clipped_ratio,
            "loop_diagnostics_requested": loop_requested,
        },
        "failures": failures,
        "warnings": warnings,
        "listening_review": "pending",
    }

    candidates = manifest.setdefault("candidates", {})
    if not isinstance(candidates, dict):
        raise ValueError("manifest candidates field must be an object")
    candidates[manifest_relative] = record

    processed_files = manifest["processed_files"]
    if not isinstance(processed_files, list):
        raise ValueError("manifest processed_files field must be an array")
    if manifest_relative not in processed_files:
        processed_files.append(manifest_relative)
        processed_files.sort()

    if source_relative is not None:
        source_files = manifest["source_files"]
        if not isinstance(source_files, list):
            raise ValueError("manifest source_files field must be an array")
        if source_relative not in source_files:
            source_files.append(source_relative)
            source_files.sort()

    manifest["lifecycle_state"] = "processed_candidate"
    manifest["human_review"] = "pending"
    manifest["qc"] = {
        "last_checked_utc": utc_now(),
        "passed": sum(
            1 for item in candidates.values() if item.get("status") == "pass"
        ),
        "failed": sum(
            1 for item in candidates.values() if item.get("status") == "fail"
        ),
    }
    manifest["updated_utc"] = utc_now()
    write_json(manifest_path, manifest)
    return record


def select_candidates(
    manifest_path: Path,
    candidate_paths: list[Path],
    *,
    selected_by: str,
    reason: str,
    replace: bool,
) -> dict[str, Any]:
    selected_by = selected_by.strip()
    reason = reason.strip()
    if not selected_by:
        raise ValueError("selected-by cannot be empty")
    if not reason:
        raise ValueError("selection reason cannot be empty")
    if not candidate_paths:
        raise ValueError("provide at least one candidate")

    manifest_path = manifest_path.resolve()
    if not manifest_path.is_file():
        raise FileNotFoundError(f"manifest not found: {manifest_path}")
    bundle = manifest_path.parent
    manifest = load_json(manifest_path)
    members = audio_members(manifest)
    state = manifest.get("lifecycle_state")
    if state not in SELECTABLE_STATES:
        raise ValueError(
            f"cannot select candidates in lifecycle state {state!r}; run QC first"
        )
    if state == "accepted_for_runtime" and not replace:
        raise ValueError(
            "runtime candidates are already selected; use --replace to record "
            "an intentional replacement"
        )

    candidates = manifest.get("candidates")
    if not isinstance(candidates, dict):
        raise ValueError("manifest candidates field must be an object")
    selected: list[str] = []
    selected_records: list[dict[str, Any]] = []
    for candidate_path in candidate_paths:
        candidate_path = candidate_path.resolve()
        if not candidate_path.is_file():
            raise FileNotFoundError(f"candidate not found: {candidate_path}")
        relative = relative_bundle_path(
            candidate_path,
            bundle / "processed",
            "candidate",
        )
        if relative in selected:
            raise ValueError(f"candidate selected more than once: {relative}")
        record = candidates.get(relative)
        if not isinstance(record, dict):
            raise ValueError(f"candidate has not been QC-checked: {relative}")
        if record.get("status") != "pass":
            raise ValueError(f"candidate did not pass QC: {relative}")
        selected.append(relative)
        selected_records.append(record)

    actual_counts: dict[str, int] = {}
    for record in selected_records:
        record_member = record.get("member_id")
        if not isinstance(record_member, str):
            raise ValueError("selected candidate is missing member_id")
        actual_counts[record_member] = actual_counts.get(record_member, 0) + 1

    coverage_errors: list[str] = []
    known_ids = {str(member.get("id")) for member in members}
    unexpected_ids = sorted(set(actual_counts).difference(known_ids))
    if unexpected_ids:
        coverage_errors.append(
            f"unknown selected member ids: {', '.join(unexpected_ids)}"
        )
    for member in members:
        member_id = str(member["id"])
        expected = int(member["variations"])
        actual = actual_counts.get(member_id, 0)
        if actual != expected:
            coverage_errors.append(
                f"member {member_id} requires {expected} selected candidate(s); "
                f"received {actual}"
            )
    if coverage_errors:
        raise ValueError("selection coverage failed: " + "; ".join(coverage_errors))

    previous = manifest.get("runtime_candidates")
    if not isinstance(previous, list):
        raise ValueError("manifest runtime_candidates field must be an array")
    history = manifest.get("selection_history")
    if not isinstance(history, list):
        raise ValueError("manifest selection_history field must be an array")
    selected_utc = utc_now()
    history.append(
        {
            "selected_utc": selected_utc,
            "selected_by": selected_by,
            "reason": reason,
            "runtime_candidates": selected,
            "replaced_runtime_candidates": list(previous) if replace else [],
        }
    )
    manifest["runtime_candidates"] = selected
    manifest["lifecycle_state"] = "accepted_for_runtime"
    manifest["human_review"] = "pending"
    manifest["updated_utc"] = selected_utc
    write_json(manifest_path, manifest)
    return {
        "manifest": str(manifest_path),
        "lifecycle_state": "accepted_for_runtime",
        "runtime_candidates": selected,
        "selection_recorded": True,
        "human_review": "pending",
    }


def write_fixture(
    path: Path,
    *,
    duration_seconds: float,
    clipped: bool,
    frequency_hz: float = 440.0,
) -> None:
    validate_positive(duration_seconds, "fixture duration")
    sample_rate = 44100
    frame_count = max(1, round(sample_rate * duration_seconds))
    payload = bytearray()
    for index in range(frame_count):
        if clipped:
            sample = 32767
        else:
            phase = 2.0 * math.pi * frequency_hz * index / sample_rate
            sample = round(math.sin(phase) * 0.25 * 32767)
        payload.extend(struct.pack("<h", sample))
    with wave.open(str(path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(payload)


def run_self_test(temp_root: Path | None = None) -> dict[str, Any]:
    pcm_cases = {
        1: bytes((0, 128, 255)),
        2: struct.pack("<hhh", -32768, 0, 32767),
        3: b"".join(
            value.to_bytes(3, "little", signed=True)
            for value in (-8388608, 0, 8388607)
        ),
        4: struct.pack("<iii", -2147483648, 0, 2147483647),
    }
    for width, payload in pcm_cases.items():
        decoded = pcm_values(payload, width)
        assert len(decoded) == 3
        assert decoded[0] == -1.0
        assert decoded[1] == 0.0
        assert decoded[2] >= 0.999

    temporary_parent = None
    if temp_root is not None:
        temp_root.mkdir(parents=True, exist_ok=True)
        temporary_parent = str(temp_root.resolve())
    with tempfile.TemporaryDirectory(
        prefix="audio-asset-self-test-",
        dir=temporary_parent,
    ) as temporary:
        bundle = Path(temporary) / "bundle"
        manifest_path = init_bundle(
            bundle,
            asset_id="self_test_audio",
            mode="music_loop",
            intended_use="exercise manifest and positive/negative QC paths",
            provider="self-test",
            model="sine-fixture",
            prompt_text="deterministic local sine fixture",
            members=None,
            target_duration=1.0,
            loop=True,
            variations=1,
            rights_notes="synthetic test fixture",
            model_revision="fixture-v1",
            event_id="music.self_test",
            bus_role="Music",
            target_sample_rate=44100,
            target_channels=1,
        )
        initial = load_json(manifest_path)
        audio_members(initial)
        assert initial["source_skill"] == "generate-game-audio"
        assert initial["media_type"] == "audio"
        assert initial["processed_files"] == []
        assert initial["runtime_candidates"] == []
        assert initial["selection_history"] == []
        assert initial["generation"]["revision"] == "fixture-v1"
        assert initial["audio"]["event_id"] == "music.self_test"
        assert initial["audio"]["bus_role"] == "Music"

        passing = bundle / "processed" / "passing.wav"
        failing = bundle / "processed" / "clipped.wav"
        write_fixture(passing, duration_seconds=1.0, clipped=False)
        write_fixture(failing, duration_seconds=1.0, clipped=True)

        common = {
            "member_id": None,
            "source_file": None,
            "expected_sample_rate": None,
            "expected_channels": None,
            "duration_tolerance": 0.001,
            "max_clipped_ratio": 0.0001,
            "silence_threshold_dbfs": -60.0,
            "seam_ms": 20.0,
            "force_loop_check": False,
        }
        passing_record = qc_manifest(manifest_path, passing, **common)
        failing_record = qc_manifest(manifest_path, failing, **common)
        manifest = load_json(manifest_path)

        assert passing_record["status"] == "pass"
        assert passing_record["metrics"]["clipped_samples"] == 0
        assert passing_record["constraints"]["expected_sample_rate_hz"] == 44100
        assert passing_record["constraints"]["loop_diagnostics_requested"] is True
        assert failing_record["status"] == "fail"
        assert failing_record["metrics"]["clipped_ratio"] > 0.99
        assert manifest["lifecycle_state"] == "processed_candidate"
        assert manifest["human_review"] == "pending"
        assert manifest["qc"] == {
            "last_checked_utc": manifest["qc"]["last_checked_utc"],
            "passed": 1,
            "failed": 1,
        }
        assert (bundle / "source" / "prompt-used.txt").read_text(
            encoding="utf-8"
        ) == "deterministic local sine fixture"

        failed_selection_guard = False
        try:
            select_candidates(
                manifest_path,
                [failing],
                selected_by="self-test",
                reason="must reject failed QC",
                replace=False,
            )
        except ValueError as error:
            failed_selection_guard = "did not pass QC" in str(error)
        assert failed_selection_guard

        selection = select_candidates(
            manifest_path,
            [passing],
            selected_by="self-test",
            reason="deterministic passing fixture",
            replace=False,
        )
        selected_manifest = load_json(manifest_path)
        assert selection["lifecycle_state"] == "accepted_for_runtime"
        assert selected_manifest["runtime_candidates"] == ["processed/passing.wav"]
        assert selected_manifest["human_review"] == "pending"
        assert len(selected_manifest["selection_history"]) == 1
        assert selected_manifest["selection_history"][0]["selected_by"] == "self-test"

        replacement_guard = False
        try:
            select_candidates(
                manifest_path,
                [passing],
                selected_by="self-test",
                reason="must require explicit replacement",
                replace=False,
            )
        except ValueError as error:
            replacement_guard = "already selected" in str(error)
        assert replacement_guard

        force_guard_passed = False
        try:
            init_bundle(
                bundle,
                asset_id="self_test_audio",
                mode="music_loop",
                intended_use="must not overwrite generated candidates",
                provider="self-test",
                model="sine-fixture",
                prompt_text="replacement prompt",
                members=None,
                target_duration=1.0,
                loop=True,
                variations=1,
                rights_notes="synthetic test fixture",
                force=True,
            )
        except FileExistsError:
            force_guard_passed = True
        assert force_guard_passed

        family_members = [
            {
                "id": "intro",
                "role": "intro",
                "target_duration_seconds": 1.0,
                "loop": False,
                "variations": 1,
            },
            {
                "id": "main_loop",
                "role": "loop",
                "target_duration_seconds": 2.0,
                "loop": True,
                "variations": 1,
            },
        ]
        family_global_guard = False
        try:
            normalize_members(
                mode="music_family",
                members=family_members,
                target_duration=2.0,
                loop=False,
                variations=1,
            )
        except ValueError as error:
            family_global_guard = "per-member" in str(error)
        assert family_global_guard

        family_bundle = Path(temporary) / "family"
        family_manifest_path = init_bundle(
            family_bundle,
            asset_id="self_test_family",
            mode="music_family",
            intended_use="prove independent intro and loop constraints",
            provider="self-test",
            model="sine-fixture",
            prompt_text="coherent intro and loop family",
            members=family_members,
            target_duration=None,
            loop=False,
            variations=1,
            rights_notes="synthetic test fixture",
            family_id="self_test_family",
            bpm=120.0,
            key_mode="C minor",
            meter="4/4",
            phrase_bars=4,
            sync_anchor="bar_1_beat_1",
            target_sample_rate=44100,
            target_channels=1,
        )
        intro = family_bundle / "processed" / "intro.wav"
        loop_candidate = family_bundle / "processed" / "main-loop.wav"
        write_fixture(intro, duration_seconds=1.0, clipped=False, frequency_hz=220.0)
        write_fixture(
            loop_candidate,
            duration_seconds=2.0,
            clipped=False,
            frequency_hz=220.0,
        )
        family_common = {
            "source_file": None,
            "expected_sample_rate": None,
            "expected_channels": None,
            "duration_tolerance": 0.001,
            "max_clipped_ratio": 0.0001,
            "silence_threshold_dbfs": -60.0,
            "seam_ms": 20.0,
            "force_loop_check": False,
        }
        intro_record = qc_manifest(
            family_manifest_path,
            intro,
            member_id="intro",
            **family_common,
        )
        loop_record = qc_manifest(
            family_manifest_path,
            loop_candidate,
            member_id="main_loop",
            **family_common,
        )
        assert intro_record["status"] == "pass"
        assert loop_record["status"] == "pass"
        assert intro_record["constraints"]["target_duration_seconds"] == 1.0
        assert loop_record["constraints"]["target_duration_seconds"] == 2.0
        assert intro_record["constraints"]["loop_diagnostics_requested"] is False
        assert loop_record["constraints"]["loop_diagnostics_requested"] is True

        family_coverage_guard = False
        try:
            select_candidates(
                family_manifest_path,
                [intro],
                selected_by="self-test",
                reason="must reject incomplete music family",
                replace=False,
            )
        except ValueError as error:
            family_coverage_guard = "main_loop requires 1" in str(error)
        assert family_coverage_guard
        select_candidates(
            family_manifest_path,
            [intro, loop_candidate],
            selected_by="self-test",
            reason="complete coherent family",
            replace=False,
        )
        family_manifest = load_json(family_manifest_path)
        assert family_manifest["lifecycle_state"] == "accepted_for_runtime"
        assert family_manifest["runtime_candidates"] == [
            "processed/intro.wav",
            "processed/main-loop.wav",
        ]

    return {
        "self_test": "pass",
        "generic_manifest_contract": "pass",
        "music_family_member_constraints": "pass",
        "positive_qc": "pass",
        "negative_qc": "fail_as_expected",
        "failed_candidate_selection_guard": "pass",
        "family_selection_coverage_guard": "pass",
        "replacement_guard": "pass",
        "force_reinitialize_guard": "pass",
        "pcm_widths_tested": [8, 16, 24, 32],
        "promotion_performed": True,
        "lifecycle_state": "accepted_for_runtime",
        "human_review": "pending",
        "human_reviewed_final_claimed": False,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Initialize traceable game-audio bundles, QC PCM WAV candidates, "
            "and record explicit runtime selections."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="initialize an audio bundle")
    init_parser.add_argument("bundle", type=Path)
    init_parser.add_argument("--asset-id", required=True)
    init_parser.add_argument("--mode", required=True, choices=MODES)
    init_parser.add_argument("--intended-use", required=True)
    init_parser.add_argument("--provider", required=True)
    init_parser.add_argument("--model", default="unspecified")
    init_parser.add_argument("--model-revision", default="unspecified")
    init_parser.add_argument("--seed", type=int)
    init_parser.add_argument("--request-file", type=Path)
    init_parser.add_argument("--settings-file", type=Path)
    prompt_group = init_parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt")
    prompt_group.add_argument("--prompt-file", type=Path)
    init_parser.add_argument("--members-file", type=Path)
    init_parser.add_argument("--target-duration", type=float)
    init_parser.add_argument("--loop", action="store_true")
    init_parser.add_argument("--variations", type=int, default=1)
    init_parser.add_argument("--event-id")
    init_parser.add_argument("--zone-id")
    init_parser.add_argument("--bus-role")
    init_parser.add_argument("--family-id")
    init_parser.add_argument("--bpm", type=float)
    init_parser.add_argument("--key-mode")
    init_parser.add_argument("--meter")
    init_parser.add_argument("--phrase-bars", type=int)
    init_parser.add_argument("--sync-anchor")
    init_parser.add_argument("--target-sample-rate", type=int)
    init_parser.add_argument("--target-channels", type=int)
    init_parser.add_argument("--rights-notes", default="pending")
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="reinitialize metadata only when no generated/source/preview files exist",
    )

    qc_parser = subparsers.add_parser("qc", help="inspect one PCM WAV candidate")
    qc_parser.add_argument("manifest", type=Path)
    qc_parser.add_argument("candidate", type=Path)
    qc_parser.add_argument("--member-id")
    qc_parser.add_argument("--source-file", type=Path)
    qc_parser.add_argument("--expected-sample-rate", type=int)
    qc_parser.add_argument("--expected-channels", type=int)
    qc_parser.add_argument("--duration-tolerance", type=float, default=0.5)
    qc_parser.add_argument("--max-clipped-ratio", type=float, default=0.0001)
    qc_parser.add_argument("--silence-threshold-dbfs", type=float, default=-60.0)
    qc_parser.add_argument("--seam-ms", type=float, default=20.0)
    qc_parser.add_argument("--loop", action="store_true", dest="force_loop_check")

    select_parser = subparsers.add_parser(
        "select",
        help="record explicit selection and promote passing candidates",
    )
    select_parser.add_argument("manifest", type=Path)
    select_parser.add_argument("candidates", type=Path, nargs="+")
    select_parser.add_argument("--selected-by", required=True)
    select_parser.add_argument("--reason", required=True)
    select_parser.add_argument("--replace", action="store_true")

    self_test_parser = subparsers.add_parser(
        "self-test",
        help="run deterministic contract, QC, and selection tests",
    )
    self_test_parser.add_argument("--temp-root", type=Path)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "init":
            manifest_path = init_bundle(
                args.bundle,
                asset_id=args.asset_id,
                mode=args.mode,
                intended_use=args.intended_use,
                provider=args.provider,
                model=args.model,
                prompt_text=read_prompt(args.prompt, args.prompt_file),
                members=read_members_file(args.members_file),
                target_duration=args.target_duration,
                loop=args.loop,
                variations=args.variations,
                rights_notes=args.rights_notes,
                model_revision=args.model_revision,
                seed=args.seed,
                request_file=args.request_file,
                settings_file=args.settings_file,
                event_id=args.event_id,
                zone_id=args.zone_id,
                bus_role=args.bus_role,
                family_id=args.family_id,
                bpm=args.bpm,
                key_mode=args.key_mode,
                meter=args.meter,
                phrase_bars=args.phrase_bars,
                sync_anchor=args.sync_anchor,
                target_sample_rate=args.target_sample_rate,
                target_channels=args.target_channels,
                force=args.force,
            )
            print(json.dumps({"manifest": str(manifest_path)}, indent=2))
        elif args.command == "qc":
            record = qc_manifest(
                args.manifest,
                args.candidate,
                member_id=args.member_id,
                source_file=args.source_file,
                expected_sample_rate=args.expected_sample_rate,
                expected_channels=args.expected_channels,
                duration_tolerance=args.duration_tolerance,
                max_clipped_ratio=args.max_clipped_ratio,
                silence_threshold_dbfs=args.silence_threshold_dbfs,
                seam_ms=args.seam_ms,
                force_loop_check=args.force_loop_check,
            )
            print(json.dumps(record, indent=2, ensure_ascii=False))
        elif args.command == "select":
            result = select_candidates(
                args.manifest,
                args.candidates,
                selected_by=args.selected_by,
                reason=args.reason,
                replace=args.replace,
            )
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(json.dumps(run_self_test(args.temp_root), indent=2))
    except (AssertionError, OSError, ValueError, json.JSONDecodeError, wave.Error) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
