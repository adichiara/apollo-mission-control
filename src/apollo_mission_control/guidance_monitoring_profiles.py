"""Historical guidance-monitoring profile catalog.

Generic guidance comparison code stays mission-neutral. This module stores the
historical configuration boundary around *which* independently produced
observations were compared, *which* fields/limits are source-backed, and
whether freshness/cadence is sufficiently known to make the comparison
historically executable.

A profile with unresolved freshness may be inspected and exposed as evidence
metadata, but cannot be converted into an executable GuidanceCrosscheckConfig.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

from .guidance_crosscheck import GuidanceCrosscheckConfig

ROOT = Path(__file__).resolve().parents[2]
GUIDANCE_MONITORING_PROFILE_ROOT = ROOT / "data" / "guidance_monitoring_profiles"


def _text(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"guidance monitoring profile {key!r} must be a non-empty string")
    return value.strip()


def _optional_nonnegative_number(data: dict[str, Any], key: str) -> float | None:
    value = data.get(key)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(
            f"guidance monitoring profile {key!r} must be numeric or null"
        )
    number = float(value)
    if number < 0.0:
        raise ValueError(
            f"guidance monitoring profile {key!r} must be non-negative"
        )
    return number


@dataclass(frozen=True)
class GuidanceMonitoringTimingEvidence:
    """Source-backed processor/update timing that is not a freshness rule."""

    tracking_input_rate_hz: float | None
    processor_interval_s_options: tuple[float, ...]
    observation_time_quantization_s_options: tuple[float, ...]
    real_time_lag_s: float | None
    provenance: tuple[str, ...]
    evidence_note: str

    def to_public_dict(self) -> dict[str, object]:
        return {
            "tracking_input_rate_hz": self.tracking_input_rate_hz,
            "processor_interval_s_options": list(self.processor_interval_s_options),
            "observation_time_quantization_s_options": list(
                self.observation_time_quantization_s_options
            ),
            "real_time_lag_s": self.real_time_lag_s,
            "provenance": list(self.provenance),
            "evidence_note": self.evidence_note,
            "is_comparison_freshness_rule": False,
        }


@dataclass(frozen=True)
class GuidanceMonitoringComparisonRecord:
    comparison_id: str
    first_source: str
    second_source: str
    purpose: str
    tolerances: dict[str, float]
    max_time_separation_s: float | None
    provenance: tuple[str, ...]
    evidence_note: str

    @property
    def historically_executable(self) -> bool:
        return self.max_time_separation_s is not None

    def to_public_dict(self) -> dict[str, object]:
        return {
            "comparison_id": self.comparison_id,
            "first_source": self.first_source,
            "second_source": self.second_source,
            "purpose": self.purpose,
            "tolerances": dict(self.tolerances),
            "max_time_separation_s": self.max_time_separation_s,
            "historically_executable": self.historically_executable,
            "provenance": list(self.provenance),
            "evidence_note": self.evidence_note,
        }

    def to_crosscheck_config(self) -> GuidanceCrosscheckConfig:
        if self.max_time_separation_s is None:
            raise ValueError(
                f"historical freshness is unresolved for comparison "
                f"{self.comparison_id!r}; refusing to invent max_time_separation_s"
            )
        return GuidanceCrosscheckConfig(
            tolerances=self.tolerances,
            max_time_separation_s=self.max_time_separation_s,
            applicability=(
                f"historical guidance monitoring profile comparison "
                f"{self.comparison_id}"
            ),
            provenance=self.provenance,
            assumptions=(
                "comparison fields and tolerances come from the selected historical profile",
                "observation production remains upstream of this comparison",
                "neither source is treated as hidden truth",
                "agreement does not itself imply GO, abort, or switchover",
            ),
        )


@dataclass(frozen=True)
class GuidanceMonitoringProfileRecord:
    profile_id: str
    mission_profile_id: str
    status: str
    applicability: str
    comparisons: tuple[GuidanceMonitoringComparisonRecord, ...]
    timing_evidence: GuidanceMonitoringTimingEvidence | None
    unresolved: tuple[str, ...]
    source_count: int
    profile_path: Path

    def comparison(self, comparison_id: str) -> GuidanceMonitoringComparisonRecord:
        requested = str(comparison_id).strip()
        for record in self.comparisons:
            if record.comparison_id == requested:
                return record
        raise ValueError(
            f"unknown comparison_id {requested!r} in guidance profile {self.profile_id}"
        )

    def to_public_dict(self) -> dict[str, object]:
        return {
            "profile_id": self.profile_id,
            "mission_profile_id": self.mission_profile_id,
            "status": self.status,
            "applicability": self.applicability,
            "comparisons": [record.to_public_dict() for record in self.comparisons],
            "timing_evidence": (
                None if self.timing_evidence is None else self.timing_evidence.to_public_dict()
            ),
            "unresolved": list(self.unresolved),
            "source_count": self.source_count,
        }


def _comparison(payload: Any) -> GuidanceMonitoringComparisonRecord:
    if not isinstance(payload, dict):
        raise ValueError("guidance monitoring comparison must be an object")

    raw_tolerances = payload.get("tolerances")
    if not isinstance(raw_tolerances, dict) or not raw_tolerances:
        raise ValueError("guidance monitoring comparison tolerances must be a non-empty object")

    tolerances: dict[str, float] = {}
    for raw_name, raw_value in raw_tolerances.items():
        if not isinstance(raw_name, str) or not raw_name.strip():
            raise ValueError("guidance monitoring tolerance field must be non-empty")
        if isinstance(raw_value, bool) or not isinstance(raw_value, (int, float)):
            raise ValueError(
                f"guidance monitoring tolerance for {raw_name!r} must be numeric"
            )
        value = float(raw_value)
        if value < 0.0:
            raise ValueError(
                f"guidance monitoring tolerance for {raw_name!r} must be non-negative"
            )
        tolerances[raw_name.strip()] = value

    raw_provenance = payload.get("provenance", [])
    if not isinstance(raw_provenance, list) or not all(
        isinstance(item, str) and item.strip() for item in raw_provenance
    ):
        raise ValueError("guidance monitoring comparison provenance must be strings")

    return GuidanceMonitoringComparisonRecord(
        comparison_id=_text(payload, "comparison_id"),
        first_source=_text(payload, "first_source"),
        second_source=_text(payload, "second_source"),
        purpose=_text(payload, "purpose"),
        tolerances=tolerances,
        max_time_separation_s=_optional_nonnegative_number(
            payload, "max_time_separation_s"
        ),
        provenance=tuple(item.strip() for item in raw_provenance),
        evidence_note=_text(payload, "evidence_note"),
    )


def _timing_evidence(payload: Any) -> GuidanceMonitoringTimingEvidence | None:
    if payload is None:
        return None
    if not isinstance(payload, dict):
        raise ValueError("guidance monitoring timing_evidence must be an object or null")

    def optional_positive(key: str) -> float | None:
        value = payload.get(key)
        if value is None:
            return None
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"guidance monitoring timing {key!r} must be numeric or null")
        number = float(value)
        if number <= 0.0:
            raise ValueError(f"guidance monitoring timing {key!r} must be positive")
        return number

    def positive_options(key: str) -> tuple[float, ...]:
        raw = payload.get(key, [])
        if not isinstance(raw, list):
            raise ValueError(f"guidance monitoring timing {key!r} must be a list")
        values: list[float] = []
        for value in raw:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError(
                    f"guidance monitoring timing {key!r} entries must be numeric"
                )
            number = float(value)
            if number <= 0.0:
                raise ValueError(
                    f"guidance monitoring timing {key!r} entries must be positive"
                )
            values.append(number)
        return tuple(values)

    raw_provenance = payload.get("provenance", [])
    if not isinstance(raw_provenance, list) or not all(
        isinstance(item, str) and item.strip() for item in raw_provenance
    ):
        raise ValueError("guidance monitoring timing provenance must be strings")

    return GuidanceMonitoringTimingEvidence(
        tracking_input_rate_hz=optional_positive("tracking_input_rate_hz"),
        processor_interval_s_options=positive_options(
            "processor_interval_s_options"
        ),
        observation_time_quantization_s_options=positive_options(
            "observation_time_quantization_s_options"
        ),
        real_time_lag_s=optional_positive("real_time_lag_s"),
        provenance=tuple(item.strip() for item in raw_provenance),
        evidence_note=_text(payload, "evidence_note"),
    )


def load_guidance_monitoring_profile(
    path: str | Path,
) -> GuidanceMonitoringProfileRecord:
    profile_path = Path(path)
    try:
        data = json.loads(profile_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(
            f"cannot load guidance monitoring profile {profile_path}: {exc}"
        ) from exc
    if not isinstance(data, dict):
        raise ValueError("guidance monitoring profile must contain a JSON object")

    raw_comparisons = data.get("comparisons")
    if not isinstance(raw_comparisons, list) or not raw_comparisons:
        raise ValueError("guidance monitoring profile comparisons must be a non-empty list")

    comparisons = tuple(_comparison(item) for item in raw_comparisons)
    seen: set[str] = set()
    for record in comparisons:
        if record.comparison_id in seen:
            raise ValueError(
                f"duplicate guidance monitoring comparison_id: {record.comparison_id}"
            )
        seen.add(record.comparison_id)

    raw_unresolved = data.get("unresolved", [])
    if not isinstance(raw_unresolved, list) or not all(
        isinstance(item, str) and item.strip() for item in raw_unresolved
    ):
        raise ValueError("guidance monitoring profile unresolved must be strings")

    raw_sources = data.get("sources", [])
    if not isinstance(raw_sources, list) or not all(
        isinstance(item, str) and item.strip() for item in raw_sources
    ):
        raise ValueError("guidance monitoring profile sources must be strings")

    return GuidanceMonitoringProfileRecord(
        profile_id=_text(data, "profile_id"),
        mission_profile_id=_text(data, "mission_profile_id"),
        status=_text(data, "status"),
        applicability=_text(data, "applicability"),
        comparisons=comparisons,
        timing_evidence=_timing_evidence(data.get("timing_evidence")),
        unresolved=tuple(item.strip() for item in raw_unresolved),
        source_count=len(raw_sources),
        profile_path=profile_path,
    )


def discover_guidance_monitoring_profiles(
    root: str | Path = GUIDANCE_MONITORING_PROFILE_ROOT,
) -> tuple[GuidanceMonitoringProfileRecord, ...]:
    profile_root = Path(root)
    records = tuple(
        load_guidance_monitoring_profile(path)
        for path in sorted(profile_root.glob("*.json"))
    )
    seen: set[str] = set()
    for record in records:
        if record.profile_id in seen:
            raise ValueError(f"duplicate guidance monitoring profile_id: {record.profile_id}")
        seen.add(record.profile_id)
    return records


def get_guidance_monitoring_profile(
    profile_id: str,
    root: str | Path = GUIDANCE_MONITORING_PROFILE_ROOT,
) -> GuidanceMonitoringProfileRecord:
    requested = str(profile_id).strip()
    if not requested:
        raise ValueError("profile_id must not be empty")
    for record in discover_guidance_monitoring_profiles(root):
        if record.profile_id == requested:
            return record
    raise ValueError(f"unknown guidance monitoring profile_id: {requested}")
