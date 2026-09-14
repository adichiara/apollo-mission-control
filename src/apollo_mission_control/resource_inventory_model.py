"""Mission-neutral resource inventory/depletion model.

This module tracks finite quantities under caller-supplied piecewise-constant
flow rates. It is intended for batteries/energy, propellant-like inventories,
oxygen, water, cooling consumables, or other scenario-relevant resources.

The model contains no Apollo constants and no hidden subsystem behavior.

Sign convention:
- positive rate consumes/depletes a resource;
- negative rate replenishes/increases a resource.

Units are caller-defined per resource and must remain internally consistent.
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
class ResourceSpec:
    resource_id: str
    unit: str
    minimum_quantity: float = 0.0
    maximum_quantity: float | None = None

    def validated(self) -> "ResourceSpec":
        minimum = _finite(self.minimum_quantity, f"{self.resource_id}.minimum_quantity")
        maximum = (
            None
            if self.maximum_quantity is None
            else _finite(self.maximum_quantity, f"{self.resource_id}.maximum_quantity")
        )
        if maximum is not None and maximum < minimum:
            raise ValueError("resource maximum_quantity must be >= minimum_quantity")
        return ResourceSpec(
            resource_id=_text(self.resource_id, "resource_id"),
            unit=_text(self.unit, "unit"),
            minimum_quantity=minimum,
            maximum_quantity=maximum,
        )


@dataclass(frozen=True)
class ResourceInventoryConfig:
    resources: tuple[ResourceSpec, ...]
    applicability: str = "generic resource inventory model proof; not mission validated"
    provenance: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = (
        "flow rates are caller-supplied and piecewise constant within each segment",
        "positive flow consumes and negative flow replenishes",
        "inventory is clamped at configured minimum/maximum bounds",
        "shortfall/overflow is reported rather than silently creating negative or excess inventory",
        "no pressure, chemistry, thermal, tank, battery-voltage, or transfer-loss physics",
    )

    def validated(self) -> "ResourceInventoryConfig":
        resources = tuple(resource.validated() for resource in self.resources)
        if not resources:
            raise ValueError("at least one resource is required")
        ids = [resource.resource_id for resource in resources]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate resource_id")
        return ResourceInventoryConfig(
            resources=resources,
            applicability=_text(self.applicability, "applicability"),
            provenance=tuple(self.provenance),
            assumptions=tuple(self.assumptions),
        )


@dataclass(frozen=True)
class ResourceInventoryState:
    time_s: float
    quantities: Mapping[str, float]

    def validated(self, config: ResourceInventoryConfig) -> "ResourceInventoryState":
        time_s = _finite(self.time_s, "time_s")
        specs = {resource.resource_id: resource for resource in config.resources}
        unknown = sorted(set(self.quantities) - set(specs))
        if unknown:
            raise ValueError(f"unknown resource quantity: {unknown[0]}")

        quantities: dict[str, float] = {}
        for resource_id, spec in specs.items():
            if resource_id not in self.quantities:
                raise ValueError(f"missing initial quantity for resource: {resource_id}")
            value = _finite(self.quantities[resource_id], f"{resource_id}.quantity")
            if value < spec.minimum_quantity:
                raise ValueError(
                    f"initial quantity for {resource_id} is below minimum_quantity"
                )
            if spec.maximum_quantity is not None and value > spec.maximum_quantity:
                raise ValueError(
                    f"initial quantity for {resource_id} exceeds maximum_quantity"
                )
            quantities[resource_id] = value

        return ResourceInventoryState(time_s=time_s, quantities=quantities)


@dataclass(frozen=True)
class ResourceFlowSegment:
    duration_s: float
    rates_per_s: Mapping[str, float]
    label: str = "flow"

    def validated(self, config: ResourceInventoryConfig) -> "ResourceFlowSegment":
        duration = _finite(self.duration_s, "duration_s")
        if duration < 0.0:
            raise ValueError("duration_s must be non-negative")

        resource_ids = {resource.resource_id for resource in config.resources}
        unknown = sorted(set(self.rates_per_s) - resource_ids)
        if unknown:
            raise ValueError(f"unknown resource flow: {unknown[0]}")

        rates = {
            resource_id: _finite(
                self.rates_per_s.get(resource_id, 0.0),
                f"{resource_id}.rate_per_s",
            )
            for resource_id in resource_ids
        }
        return ResourceFlowSegment(
            duration_s=duration,
            rates_per_s=rates,
            label=_text(self.label, "flow label"),
        )


@dataclass(frozen=True)
class ResourceBoundaryEvent:
    resource_id: str
    time_s: float
    boundary: str
    quantity: float
    segment_label: str

    def to_dict(self) -> dict[str, object]:
        return {
            "resource_id": self.resource_id,
            "time_s": self.time_s,
            "boundary": self.boundary,
            "quantity": self.quantity,
            "segment_label": self.segment_label,
        }


@dataclass(frozen=True)
class ResourceInventoryResult:
    initial_state: ResourceInventoryState
    final_state: ResourceInventoryState
    elapsed_s: float
    consumed: Mapping[str, float]
    replenished: Mapping[str, float]
    unsatisfied_consumption: Mapping[str, float]
    overflow: Mapping[str, float]
    boundary_events: tuple[ResourceBoundaryEvent, ...]
    units: Mapping[str, str]
    applicability: str
    provenance: tuple[str, ...]
    assumptions: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "resource_inventory_model_proof_not_historically_validated",
            "initial_state": {
                "time_s": self.initial_state.time_s,
                "quantities": dict(self.initial_state.quantities),
            },
            "final_state": {
                "time_s": self.final_state.time_s,
                "quantities": dict(self.final_state.quantities),
            },
            "elapsed_s": self.elapsed_s,
            "consumed": dict(self.consumed),
            "replenished": dict(self.replenished),
            "unsatisfied_consumption": dict(self.unsatisfied_consumption),
            "overflow": dict(self.overflow),
            "boundary_events": [event.to_dict() for event in self.boundary_events],
            "units": dict(self.units),
            "applicability": self.applicability,
            "provenance": list(self.provenance),
            "assumptions": list(self.assumptions),
        }


def simulate_resource_inventory(
    initial_state: ResourceInventoryState,
    segments: tuple[ResourceFlowSegment, ...] | list[ResourceFlowSegment],
    config: ResourceInventoryConfig,
) -> ResourceInventoryResult:
    """Integrate finite resource quantities exactly for piecewise-constant flows."""

    cfg = config.validated()
    state = initial_state.validated(cfg)
    checked_segments = tuple(segment.validated(cfg) for segment in segments)
    if not checked_segments:
        raise ValueError("at least one resource flow segment is required")

    specs = {resource.resource_id: resource for resource in cfg.resources}
    quantities = dict(state.quantities)
    consumed = {resource_id: 0.0 for resource_id in specs}
    replenished = {resource_id: 0.0 for resource_id in specs}
    unsatisfied = {resource_id: 0.0 for resource_id in specs}
    overflow = {resource_id: 0.0 for resource_id in specs}
    events: list[ResourceBoundaryEvent] = []
    current_time = state.time_s

    hit_min: set[str] = {
        resource_id
        for resource_id, spec in specs.items()
        if quantities[resource_id] <= spec.minimum_quantity
    }
    hit_max: set[str] = {
        resource_id
        for resource_id, spec in specs.items()
        if spec.maximum_quantity is not None
        and quantities[resource_id] >= spec.maximum_quantity
    }

    for segment in checked_segments:
        if segment.duration_s == 0.0:
            continue

        segment_start = current_time
        for resource_id, spec in specs.items():
            rate = segment.rates_per_s[resource_id]
            if rate == 0.0:
                continue

            start_quantity = quantities[resource_id]
            requested_change = rate * segment.duration_s

            if rate > 0.0:
                available = max(0.0, start_quantity - spec.minimum_quantity)
                actual = min(requested_change, available)
                quantities[resource_id] = start_quantity - actual
                consumed[resource_id] += actual
                shortfall = requested_change - actual
                unsatisfied[resource_id] += shortfall

                if requested_change >= available and resource_id not in hit_min:
                    boundary_offset = 0.0 if rate == 0.0 else available / rate
                    events.append(
                        ResourceBoundaryEvent(
                            resource_id=resource_id,
                            time_s=segment_start + boundary_offset,
                            boundary="minimum",
                            quantity=spec.minimum_quantity,
                            segment_label=segment.label,
                        )
                    )
                    hit_min.add(resource_id)
                if quantities[resource_id] > spec.minimum_quantity:
                    hit_min.discard(resource_id)

            else:
                requested_addition = -requested_change
                capacity = (
                    float("inf")
                    if spec.maximum_quantity is None
                    else max(0.0, spec.maximum_quantity - start_quantity)
                )
                actual = min(requested_addition, capacity)
                quantities[resource_id] = start_quantity + actual
                replenished[resource_id] += actual
                excess = requested_addition - actual
                overflow[resource_id] += excess

                if (
                    spec.maximum_quantity is not None
                    and requested_addition >= capacity
                    and resource_id not in hit_max
                ):
                    boundary_offset = 0.0 if -rate == 0.0 else capacity / (-rate)
                    events.append(
                        ResourceBoundaryEvent(
                            resource_id=resource_id,
                            time_s=segment_start + boundary_offset,
                            boundary="maximum",
                            quantity=spec.maximum_quantity,
                            segment_label=segment.label,
                        )
                    )
                    hit_max.add(resource_id)
                if (
                    spec.maximum_quantity is None
                    or quantities[resource_id] < spec.maximum_quantity
                ):
                    hit_max.discard(resource_id)

        current_time += segment.duration_s

    final_state = ResourceInventoryState(
        time_s=current_time,
        quantities=quantities,
    )
    return ResourceInventoryResult(
        initial_state=state,
        final_state=final_state,
        elapsed_s=current_time - state.time_s,
        consumed=consumed,
        replenished=replenished,
        unsatisfied_consumption=unsatisfied,
        overflow=overflow,
        boundary_events=tuple(events),
        units={resource.resource_id: resource.unit for resource in cfg.resources},
        applicability=cfg.applicability,
        provenance=cfg.provenance,
        assumptions=cfg.assumptions,
    )
