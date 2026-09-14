"""Mission-neutral independent-guidance observation cross-check.

The model compares two independently produced guidance observations using
caller-supplied fields, tolerances, and freshness limits.

It intentionally does not designate either source as hidden truth and does not
produce an abort/continue recommendation.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Mapping


def _finite(value: float, name: str) -> float:
    number = float(value)
    if not isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


def _text(value: str, name: str) -> str:
    result = str(value).strip()
    if not result:
        raise ValueError(f"{name} must not be empty")
    return result


@dataclass(frozen=True)
class GuidanceObservation:
    source: str
    time_s: float
    valid: bool
    values: Mapping[str, float]
    provenance: tuple[str, ...] = ()

    def validated(self) -> "GuidanceObservation":
        source = _text(self.source, "guidance observation source")
        values: dict[str, float] = {}
        for raw_name, raw_value in self.values.items():
            name = _text(raw_name, "guidance observation field")
            values[name] = _finite(raw_value, f"{source}.{name}")
        return GuidanceObservation(
            source=source,
            time_s=_finite(self.time_s, "guidance observation time_s"),
            valid=bool(self.valid),
            values=values,
            provenance=tuple(self.provenance),
        )


@dataclass(frozen=True)
class GuidanceCrosscheckConfig:
    tolerances: Mapping[str, float]
    max_time_separation_s: float
    applicability: str = "generic independent-guidance cross-check; not mission validated"
    provenance: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = (
        "both observations are independently produced upstream inputs",
        "comparison fields and tolerances are caller supplied",
        "neither observation is treated as authoritative hidden truth",
        "invalid, stale, or incomplete inputs produce an indeterminate comparison",
        "agreement does not itself imply a mission GO decision",
    )

    def validated(self) -> "GuidanceCrosscheckConfig":
        if not self.tolerances:
            raise ValueError("at least one cross-check tolerance is required")
        tolerances: dict[str, float] = {}
        for raw_name, raw_tolerance in self.tolerances.items():
            name = _text(raw_name, "cross-check field")
            tolerance = _finite(raw_tolerance, f"tolerance for {name}")
            if tolerance < 0.0:
                raise ValueError(f"tolerance for {name} must be non-negative")
            tolerances[name] = tolerance

        max_time = _finite(self.max_time_separation_s, "max_time_separation_s")
        if max_time < 0.0:
            raise ValueError("max_time_separation_s must be non-negative")

        applicability = _text(self.applicability, "applicability")
        return GuidanceCrosscheckConfig(
            tolerances=tolerances,
            max_time_separation_s=max_time,
            applicability=applicability,
            provenance=tuple(self.provenance),
            assumptions=tuple(self.assumptions),
        )


@dataclass(frozen=True)
class GuidanceFieldComparison:
    field: str
    first_value: float
    second_value: float
    difference: float
    absolute_difference: float
    tolerance: float
    within_tolerance: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "field": self.field,
            "first_value": self.first_value,
            "second_value": self.second_value,
            "difference": self.difference,
            "absolute_difference": self.absolute_difference,
            "tolerance": self.tolerance,
            "within_tolerance": self.within_tolerance,
        }


@dataclass(frozen=True)
class GuidanceCrosscheckResult:
    first_source: str
    second_source: str
    time_separation_s: float
    comparable: bool
    agreement: bool | None
    comparisons: tuple[GuidanceFieldComparison, ...]
    reasons: tuple[str, ...]
    applicability: str
    provenance: tuple[str, ...]
    assumptions: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "guidance_crosscheck_model_not_historically_validated",
            "first_source": self.first_source,
            "second_source": self.second_source,
            "time_separation_s": self.time_separation_s,
            "comparable": self.comparable,
            "agreement": self.agreement,
            "comparisons": [item.to_dict() for item in self.comparisons],
            "reasons": list(self.reasons),
            "applicability": self.applicability,
            "provenance": list(self.provenance),
            "assumptions": list(self.assumptions),
        }


def compare_guidance_observations(
    first: GuidanceObservation,
    second: GuidanceObservation,
    config: GuidanceCrosscheckConfig,
) -> GuidanceCrosscheckResult:
    """Compare independent guidance observations without selecting a truth source."""

    first_checked = first.validated()
    second_checked = second.validated()
    checked_config = config.validated()

    time_separation = abs(first_checked.time_s - second_checked.time_s)
    reasons: list[str] = []

    if not first_checked.valid:
        reasons.append(f"{first_checked.source}_invalid")
    if not second_checked.valid:
        reasons.append(f"{second_checked.source}_invalid")
    if time_separation > checked_config.max_time_separation_s:
        reasons.append("observations_too_far_apart_in_time")

    comparisons: list[GuidanceFieldComparison] = []
    for field, tolerance in checked_config.tolerances.items():
        if field not in first_checked.values:
            reasons.append(f"{first_checked.source}_missing_{field}")
            continue
        if field not in second_checked.values:
            reasons.append(f"{second_checked.source}_missing_{field}")
            continue

        first_value = first_checked.values[field]
        second_value = second_checked.values[field]
        difference = second_value - first_value
        absolute_difference = abs(difference)
        comparisons.append(
            GuidanceFieldComparison(
                field=field,
                first_value=first_value,
                second_value=second_value,
                difference=difference,
                absolute_difference=absolute_difference,
                tolerance=tolerance,
                within_tolerance=absolute_difference <= tolerance,
            )
        )

    comparable = (
        not reasons
        and len(comparisons) == len(checked_config.tolerances)
    )
    agreement = (
        all(item.within_tolerance for item in comparisons)
        if comparable
        else None
    )

    return GuidanceCrosscheckResult(
        first_source=first_checked.source,
        second_source=second_checked.source,
        time_separation_s=time_separation,
        comparable=comparable,
        agreement=agreement,
        comparisons=tuple(comparisons),
        reasons=tuple(reasons),
        applicability=checked_config.applicability,
        provenance=checked_config.provenance,
        assumptions=checked_config.assumptions,
    )
