"""Historical landing-radar profile catalog."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

from .landing_radar_velocity_update import LandingRadarVelocityWeightConfig


ROOT = Path(__file__).resolve().parents[2]
LANDING_RADAR_PROFILE_ROOT = ROOT / "data" / "landing_radar_profiles"
FT_TO_M = 0.3048


def _text(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"landing-radar profile {key!r} must be a non-empty string")
    return value.strip()


def _number(data: dict[str, Any], key: str, *, nonnegative: bool = True) -> float:
    value = data.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"landing-radar profile {key!r} must be numeric")
    number = float(value)
    if nonnegative and number < 0.0:
        raise ValueError(f"landing-radar profile {key!r} must be non-negative")
    return number


def _weight_map(data: Any, key: str) -> dict[str, float]:
    if not isinstance(data, dict) or not data:
        raise ValueError(f"landing-radar profile {key!r} must be a non-empty object")
    result: dict[str, float] = {}
    for raw_name, raw_value in data.items():
        if not isinstance(raw_name, str) or not raw_name.strip():
            raise ValueError(f"landing-radar profile {key!r} component must be text")
        if isinstance(raw_value, bool) or not isinstance(raw_value, (int, float)):
            raise ValueError(
                f"landing-radar profile {key!r} weight for {raw_name!r} must be numeric"
            )
        value = float(raw_value)
        if value < 0.0:
            raise ValueError(
                f"landing-radar profile {key!r} weight for {raw_name!r} must be non-negative"
            )
        result[raw_name.strip().lower()] = value
    return result


@dataclass(frozen=True)
class LandingRadarVelocityWeightingProfile:
    maximum_speed_fps: float
    low_speed_threshold_fps: float
    linear_component_weights: dict[str, float]
    low_speed_component_weights: dict[str, float]
    override_programs: tuple[str, ...]
    override_weight: float
    evidence_note: str

    def to_config(self, provenance: tuple[str, ...]) -> LandingRadarVelocityWeightConfig:
        return LandingRadarVelocityWeightConfig(
            maximum_speed_m_s=self.maximum_speed_fps * FT_TO_M,
            low_speed_threshold_m_s=self.low_speed_threshold_fps * FT_TO_M,
            linear_component_weights=self.linear_component_weights,
            low_speed_component_weights=self.low_speed_component_weights,
            override_programs=self.override_programs,
            override_weight=self.override_weight,
            applicability="Apollo 11 LM-5 landing-radar velocity weighting",
            provenance=provenance,
            assumptions=(
                "thresholds and weights are from the LM-5 Mission G LUMINARY 99 erasable load",
                "piecewise selection and P65/P66/P67 override follow flown LUMINARY 099 SERVICER logic",
                "input residual and beam vector are supplied by upstream Apollo landing-radar stages",
            ),
        )

    def to_public_dict(self) -> dict[str, object]:
        return {
            "maximum_speed_fps": self.maximum_speed_fps,
            "low_speed_threshold_fps": self.low_speed_threshold_fps,
            "linear_component_weights": dict(self.linear_component_weights),
            "low_speed_component_weights": dict(self.low_speed_component_weights),
            "override_programs": list(self.override_programs),
            "override_weight": self.override_weight,
            "evidence_note": self.evidence_note,
        }


@dataclass(frozen=True)
class LandingRadarProfileRecord:
    profile_id: str
    mission_profile_id: str
    status: str
    velocity_weighting: LandingRadarVelocityWeightingProfile | None
    unresolved: tuple[str, ...]
    sources: tuple[str, ...]
    profile_path: Path

    def velocity_update_config(self) -> LandingRadarVelocityWeightConfig:
        if self.velocity_weighting is None:
            raise ValueError(
                f"landing-radar profile {self.profile_id!r} has no velocity weighting"
            )
        return self.velocity_weighting.to_config(self.sources)

    def to_public_dict(self) -> dict[str, object]:
        return {
            "profile_id": self.profile_id,
            "mission_profile_id": self.mission_profile_id,
            "status": self.status,
            "velocity_update_weighting": (
                None
                if self.velocity_weighting is None
                else self.velocity_weighting.to_public_dict()
            ),
            "unresolved": list(self.unresolved),
            "sources": list(self.sources),
        }


def _velocity_weighting(payload: Any) -> LandingRadarVelocityWeightingProfile | None:
    if payload is None:
        return None
    if not isinstance(payload, dict):
        raise ValueError("velocity_update_weighting must be an object or null")

    raw_programs = payload.get("override_programs", [])
    if not isinstance(raw_programs, list) or not all(
        isinstance(item, str) and item.strip() for item in raw_programs
    ):
        raise ValueError("override_programs must be a list of non-empty strings")

    return LandingRadarVelocityWeightingProfile(
        maximum_speed_fps=_number(payload, "maximum_speed_fps"),
        low_speed_threshold_fps=_number(payload, "low_speed_threshold_fps"),
        linear_component_weights=_weight_map(
            payload.get("linear_component_weights"),
            "linear_component_weights",
        ),
        low_speed_component_weights=_weight_map(
            payload.get("low_speed_component_weights"),
            "low_speed_component_weights",
        ),
        override_programs=tuple(item.strip().upper() for item in raw_programs),
        override_weight=_number(payload, "override_weight"),
        evidence_note=_text(payload, "evidence_note"),
    )


def load_landing_radar_profile(path: str | Path) -> LandingRadarProfileRecord:
    profile_path = Path(path)
    try:
        data = json.loads(profile_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot load landing-radar profile {profile_path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("landing-radar profile must contain a JSON object")

    raw_unresolved = data.get("unresolved", [])
    if not isinstance(raw_unresolved, list) or not all(
        isinstance(item, str) and item.strip() for item in raw_unresolved
    ):
        raise ValueError("landing-radar profile unresolved must be strings")

    raw_sources = data.get("sources", [])
    if not isinstance(raw_sources, list) or not all(
        isinstance(item, str) and item.strip() for item in raw_sources
    ):
        raise ValueError("landing-radar profile sources must be strings")

    record = LandingRadarProfileRecord(
        profile_id=_text(data, "profile_id"),
        mission_profile_id=_text(data, "mission_profile_id"),
        status=_text(data, "status"),
        velocity_weighting=_velocity_weighting(
            data.get("velocity_update_weighting")
        ),
        unresolved=tuple(item.strip() for item in raw_unresolved),
        sources=tuple(item.strip() for item in raw_sources),
        profile_path=profile_path,
    )
    if record.velocity_weighting is not None:
        record.velocity_update_config().validated()
    return record


def discover_landing_radar_profiles(
    root: str | Path = LANDING_RADAR_PROFILE_ROOT,
) -> tuple[LandingRadarProfileRecord, ...]:
    records = tuple(
        load_landing_radar_profile(path)
        for path in sorted(Path(root).glob("*.json"))
    )
    ids = [record.profile_id for record in records]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate landing-radar profile_id")
    return records


def get_landing_radar_profile(
    profile_id: str,
    root: str | Path = LANDING_RADAR_PROFILE_ROOT,
) -> LandingRadarProfileRecord:
    requested = str(profile_id).strip()
    if not requested:
        raise ValueError("profile_id must not be empty")
    for record in discover_landing_radar_profiles(root):
        if record.profile_id == requested:
            return record
    raise ValueError(f"unknown landing-radar profile_id: {requested}")
