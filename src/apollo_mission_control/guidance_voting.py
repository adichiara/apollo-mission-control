"""Mission-neutral multi-source guidance consensus analysis.

This module evaluates agreement topology among independently produced guidance
observations. It is designed for cases where Mission Control compares multiple
navigation/guidance sources and uses consistency as evidence.

The model does not declare any source physically correct or failed. A source
outside a consensus group is only outside the caller-defined agreement bounds.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import isfinite
from typing import Iterable, Mapping

from .guidance_crosscheck import GuidanceObservation


@dataclass(frozen=True)
class GuidanceVotingConfig:
    tolerances: Mapping[str, float]
    max_time_separation_s: float
    minimum_agreeing_sources: int = 2
    applicability: str = "generic multi-source guidance consensus; not mission validated"
    provenance: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = (
        "observations are independently produced upstream inputs",
        "comparison fields, tolerances, freshness limits, and quorum are caller supplied",
        "consensus means mutual agreement within configured bounds, not physical truth",
        "sources outside a consensus are not automatically classified as failed",
        "no mission GO/NO-GO or abort/continue decision is generated",
    )

    def validated(self) -> "GuidanceVotingConfig":
        if not self.tolerances:
            raise ValueError("at least one voting tolerance is required")

        tolerances: dict[str, float] = {}
        for raw_field, raw_tolerance in self.tolerances.items():
            field = str(raw_field).strip()
            if not field:
                raise ValueError("voting field must not be empty")
            tolerance = float(raw_tolerance)
            if not isfinite(tolerance):
                raise ValueError(f"tolerance for {field} must be finite")
            if tolerance < 0.0:
                raise ValueError(f"tolerance for {field} must be non-negative")
            tolerances[field] = tolerance

        max_time = float(self.max_time_separation_s)
        if not isfinite(max_time):
            raise ValueError("max_time_separation_s must be finite")
        if max_time < 0.0:
            raise ValueError("max_time_separation_s must be non-negative")

        minimum = int(self.minimum_agreeing_sources)
        if minimum < 2:
            raise ValueError("minimum_agreeing_sources must be at least 2")

        applicability = str(self.applicability).strip()
        if not applicability:
            raise ValueError("applicability must not be empty")

        return GuidanceVotingConfig(
            tolerances=tolerances,
            max_time_separation_s=max_time,
            minimum_agreeing_sources=minimum,
            applicability=applicability,
            provenance=tuple(self.provenance),
            assumptions=tuple(self.assumptions),
        )


@dataclass(frozen=True)
class GuidancePairAgreement:
    first_source: str
    second_source: str
    time_separation_s: float
    difference: float
    absolute_difference: float
    tolerance: float
    time_compatible: bool
    value_compatible: bool
    agrees: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "first_source": self.first_source,
            "second_source": self.second_source,
            "time_separation_s": self.time_separation_s,
            "difference": self.difference,
            "absolute_difference": self.absolute_difference,
            "tolerance": self.tolerance,
            "time_compatible": self.time_compatible,
            "value_compatible": self.value_compatible,
            "agrees": self.agrees,
        }


@dataclass(frozen=True)
class GuidanceFieldConsensus:
    field: str
    status: str
    eligible_sources: tuple[str, ...]
    consensus_sources: tuple[str, ...]
    outside_consensus_sources: tuple[str, ...]
    pairwise: tuple[GuidancePairAgreement, ...]
    reasons: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "field": self.field,
            "status": self.status,
            "eligible_sources": list(self.eligible_sources),
            "consensus_sources": list(self.consensus_sources),
            "outside_consensus_sources": list(self.outside_consensus_sources),
            "pairwise": [item.to_dict() for item in self.pairwise],
            "reasons": list(self.reasons),
        }


@dataclass(frozen=True)
class GuidanceVotingResult:
    sources: tuple[str, ...]
    fields: tuple[GuidanceFieldConsensus, ...]
    applicability: str
    provenance: tuple[str, ...]
    assumptions: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "guidance_multisource_consensus_not_historically_validated",
            "sources": list(self.sources),
            "fields": [field.to_dict() for field in self.fields],
            "applicability": self.applicability,
            "provenance": list(self.provenance),
            "assumptions": list(self.assumptions),
        }


def _largest_mutually_agreeing_groups(
    sources: tuple[str, ...],
    pair_agreement: dict[frozenset[str], bool],
    minimum: int,
) -> tuple[tuple[str, ...], ...]:
    qualifying: list[tuple[str, ...]] = []
    for size in range(len(sources), minimum - 1, -1):
        for group in combinations(sources, size):
            if all(
                pair_agreement.get(frozenset(pair), False)
                for pair in combinations(group, 2)
            ):
                qualifying.append(group)
        if qualifying:
            break
    return tuple(qualifying)


def assess_guidance_consensus(
    observations: Iterable[GuidanceObservation],
    config: GuidanceVotingConfig,
) -> GuidanceVotingResult:
    """Assess field-by-field multi-source agreement without selecting truth."""

    checked_config = config.validated()
    checked = tuple(observation.validated() for observation in observations)
    if len(checked) < checked_config.minimum_agreeing_sources:
        raise ValueError(
            "number of observations is smaller than minimum_agreeing_sources"
        )

    source_names = tuple(observation.source for observation in checked)
    if len(set(source_names)) != len(source_names):
        raise ValueError("guidance observation sources must be unique")

    field_results: list[GuidanceFieldConsensus] = []

    for field, tolerance in checked_config.tolerances.items():
        eligible = tuple(
            observation
            for observation in checked
            if observation.valid and field in observation.values
        )
        eligible_names = tuple(observation.source for observation in eligible)
        reasons: list[str] = []

        for observation in checked:
            if not observation.valid:
                reasons.append(f"{observation.source}_invalid")
            elif field not in observation.values:
                reasons.append(f"{observation.source}_missing_{field}")

        pairwise: list[GuidancePairAgreement] = []
        pair_map: dict[frozenset[str], bool] = {}

        for first, second in combinations(eligible, 2):
            time_separation = abs(first.time_s - second.time_s)
            difference = second.values[field] - first.values[field]
            absolute_difference = abs(difference)
            time_compatible = (
                time_separation <= checked_config.max_time_separation_s
            )
            value_compatible = absolute_difference <= tolerance
            agrees = time_compatible and value_compatible
            pair_map[frozenset((first.source, second.source))] = agrees
            pairwise.append(
                GuidancePairAgreement(
                    first_source=first.source,
                    second_source=second.source,
                    time_separation_s=time_separation,
                    difference=difference,
                    absolute_difference=absolute_difference,
                    tolerance=tolerance,
                    time_compatible=time_compatible,
                    value_compatible=value_compatible,
                    agrees=agrees,
                )
            )

        if len(eligible) < checked_config.minimum_agreeing_sources:
            reasons.append("insufficient_eligible_sources")
            field_results.append(
                GuidanceFieldConsensus(
                    field=field,
                    status="indeterminate",
                    eligible_sources=eligible_names,
                    consensus_sources=(),
                    outside_consensus_sources=(),
                    pairwise=tuple(pairwise),
                    reasons=tuple(reasons),
                )
            )
            continue

        groups = _largest_mutually_agreeing_groups(
            eligible_names,
            pair_map,
            checked_config.minimum_agreeing_sources,
        )

        if not groups:
            reasons.append("no_agreeing_quorum")
            status = "no_consensus"
            consensus_sources: tuple[str, ...] = ()
            outside: tuple[str, ...] = eligible_names
        elif len(groups) > 1:
            reasons.append("multiple_equal_consensus_groups")
            status = "ambiguous"
            consensus_sources = ()
            outside = ()
        else:
            status = "consensus"
            consensus_sources = groups[0]
            outside = tuple(
                source
                for source in eligible_names
                if source not in consensus_sources
            )

        field_results.append(
            GuidanceFieldConsensus(
                field=field,
                status=status,
                eligible_sources=eligible_names,
                consensus_sources=consensus_sources,
                outside_consensus_sources=outside,
                pairwise=tuple(pairwise),
                reasons=tuple(reasons),
            )
        )

    return GuidanceVotingResult(
        sources=source_names,
        fields=tuple(field_results),
        applicability=checked_config.applicability,
        provenance=checked_config.provenance,
        assumptions=checked_config.assumptions,
    )
