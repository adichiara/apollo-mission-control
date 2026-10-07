"""Historical powered-descent phase-profile catalog."""

from __future__ import annotations

from pathlib import Path
import json
from typing import Any

from .powered_descent_phase import (
    FlownPropulsionObservation,
    PoweredDescentAnchor,
    PoweredDescentPhase,
    PoweredDescentPhaseConfig,
)

ROOT = Path(__file__).resolve().parents[2]
POWERED_DESCENT_PROFILE_ROOT = ROOT / "data" / "powered_descent_profiles"


def _text(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(
            f"powered-descent profile {key!r} must be a non-empty string"
        )
    return value.strip()


def _number(data: dict[str, Any], key: str) -> float:
    value = data.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"powered-descent profile {key!r} must be numeric")
    return float(value)


def _anchor(payload: Any) -> PoweredDescentAnchor:
    if not isinstance(payload, dict):
        raise ValueError("powered-descent anchor must be an object")
    altitude = payload.get("nominal_altitude_ft")
    if altitude is not None and (
        isinstance(altitude, bool) or not isinstance(altitude, (int, float))
    ):
        raise ValueError("nominal_altitude_ft must be numeric or null")
    try:
        phase = PoweredDescentPhase(_text(payload, "phase_after"))
    except ValueError as exc:
        raise ValueError(
            f"unknown powered-descent phase: {payload.get('phase_after')!r}"
        ) from exc
    return PoweredDescentAnchor(
        event_id=_text(payload, "event_id"),
        tfi_s=_number(payload, "tfi_s"),
        phase_after=phase,
        nominal_altitude_ft=None if altitude is None else float(altitude),
        evidence_basis=_text(payload, "evidence_basis"),
    ).validated()


def _observation(payload: Any) -> FlownPropulsionObservation:
    if not isinstance(payload, dict):
        raise ValueError("flown propulsion observation must be an object")
    return FlownPropulsionObservation(
        key=_text(payload, "key"),
        value=_number(payload, "value"),
        unit=_text(payload, "unit"),
        qualifier=_text(payload, "qualifier"),
        evidence_basis=str(
            payload.get("evidence_basis", "flown_postflight")
        ).strip()
        or "flown_postflight",
    ).validated()


def load_powered_descent_phase_profile(
    path: str | Path,
) -> PoweredDescentPhaseConfig:
    profile_path = Path(path)
    try:
        data = json.loads(profile_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(
            f"cannot load powered-descent profile {profile_path}: {exc}"
        ) from exc
    if not isinstance(data, dict):
        raise ValueError("powered-descent profile must contain a JSON object")

    raw_anchors = data.get("planned_anchors")
    if not isinstance(raw_anchors, list) or not raw_anchors:
        raise ValueError("powered-descent profile planned_anchors must be a list")

    raw_observations = data.get("flown_observations", [])
    if not isinstance(raw_observations, list):
        raise ValueError(
            "powered-descent profile flown_observations must be a list"
        )

    raw_untimed = data.get("untimed_nominal_events", [])
    if not isinstance(raw_untimed, list) or not all(
        isinstance(item, str) and item.strip() for item in raw_untimed
    ):
        raise ValueError(
            "powered-descent profile untimed_nominal_events must be strings"
        )

    raw_provenance = data.get("provenance", [])
    if not isinstance(raw_provenance, list) or not all(
        isinstance(item, str) and item.strip() for item in raw_provenance
    ):
        raise ValueError("powered-descent profile provenance must be strings")

    raw_unresolved = data.get("unresolved", [])
    if not isinstance(raw_unresolved, list) or not all(
        isinstance(item, str) and item.strip() for item in raw_unresolved
    ):
        raise ValueError("powered-descent profile unresolved must be strings")

    return PoweredDescentPhaseConfig(
        profile_id=_text(data, "profile_id"),
        mission_profile_id=_text(data, "mission_profile_id"),
        anchors=tuple(_anchor(item) for item in raw_anchors),
        flown_observations=tuple(
            _observation(item) for item in raw_observations
        ),
        untimed_nominal_events=tuple(item.strip() for item in raw_untimed),
        applicability=_text(data, "applicability"),
        provenance=tuple(item.strip() for item in raw_provenance),
        unresolved=tuple(item.strip() for item in raw_unresolved),
    ).validated()


def discover_powered_descent_phase_profiles(
    root: str | Path = POWERED_DESCENT_PROFILE_ROOT,
) -> tuple[PoweredDescentPhaseConfig, ...]:
    records = tuple(
        load_powered_descent_phase_profile(path)
        for path in sorted(Path(root).glob("*.json"))
    )
    ids = [record.profile_id for record in records]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate powered-descent profile_id")
    return records


def get_powered_descent_phase_profile(
    profile_id: str,
    root: str | Path = POWERED_DESCENT_PROFILE_ROOT,
) -> PoweredDescentPhaseConfig:
    requested = str(profile_id).strip()
    if not requested:
        raise ValueError("profile_id must not be empty")
    for record in discover_powered_descent_phase_profiles(root):
        if record.profile_id == requested:
            return record
    raise ValueError(f"unknown powered-descent profile_id: {requested}")
