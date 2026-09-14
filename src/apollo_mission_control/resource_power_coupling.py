"""Explicit resource-to-electrical-source coupling.

This small adapter converts finite resource inventory state into electrical
source availability using caller-supplied threshold rules and optional upstream
hardware availability.

It exists to make cross-model causality explicit:
resource quantity -> source availability -> electrical bus/load state.

No mission constants or battery chemistry are embedded.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Mapping

from .resource_inventory_model import ResourceInventoryState


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
class ResourceElectricalSourceRule:
    source_id: str
    resource_id: str
    minimum_operating_quantity: float = 0.0
    available_at_threshold: bool = False
    provenance: str = "caller-supplied resource/power coupling"

    def validated(self) -> "ResourceElectricalSourceRule":
        return ResourceElectricalSourceRule(
            source_id=_text(self.source_id, "source_id"),
            resource_id=_text(self.resource_id, "resource_id"),
            minimum_operating_quantity=_finite(
                self.minimum_operating_quantity,
                "minimum_operating_quantity",
            ),
            available_at_threshold=bool(self.available_at_threshold),
            provenance=_text(self.provenance, "provenance"),
        )


@dataclass(frozen=True)
class ResourceElectricalSourceResult:
    source_id: str
    resource_id: str
    quantity: float
    minimum_operating_quantity: float
    resource_sufficient: bool
    upstream_available: bool
    available: bool
    provenance: str

    def to_dict(self) -> dict[str, object]:
        return {
            "source_id": self.source_id,
            "resource_id": self.resource_id,
            "quantity": self.quantity,
            "minimum_operating_quantity": self.minimum_operating_quantity,
            "resource_sufficient": self.resource_sufficient,
            "upstream_available": self.upstream_available,
            "available": self.available,
            "provenance": self.provenance,
        }


def derive_electrical_source_availability(
    resource_state: ResourceInventoryState,
    rules: tuple[ResourceElectricalSourceRule, ...] | list[ResourceElectricalSourceRule],
    *,
    upstream_availability: Mapping[str, bool] | None = None,
) -> tuple[ResourceElectricalSourceResult, ...]:
    """Derive source availability without mutating either resource or bus state."""

    upstream = dict(upstream_availability or {})
    results: list[ResourceElectricalSourceResult] = []
    seen_sources: set[str] = set()

    for raw_rule in rules:
        rule = raw_rule.validated()
        if rule.source_id in seen_sources:
            raise ValueError(f"duplicate resource/power source rule: {rule.source_id}")
        seen_sources.add(rule.source_id)

        if rule.resource_id not in resource_state.quantities:
            raise ValueError(
                f"resource/power rule references missing resource: {rule.resource_id}"
            )
        quantity = _finite(
            resource_state.quantities[rule.resource_id],
            f"{rule.resource_id}.quantity",
        )
        if rule.available_at_threshold:
            sufficient = quantity >= rule.minimum_operating_quantity
        else:
            sufficient = quantity > rule.minimum_operating_quantity

        upstream_ok = bool(upstream.get(rule.source_id, True))
        results.append(
            ResourceElectricalSourceResult(
                source_id=rule.source_id,
                resource_id=rule.resource_id,
                quantity=quantity,
                minimum_operating_quantity=rule.minimum_operating_quantity,
                resource_sufficient=sufficient,
                upstream_available=upstream_ok,
                available=sufficient and upstream_ok,
                provenance=rule.provenance,
            )
        )

    unknown_upstream = sorted(set(upstream) - seen_sources)
    if unknown_upstream:
        raise ValueError(
            f"upstream availability references uncoupled source: {unknown_upstream[0]}"
        )

    return tuple(results)
