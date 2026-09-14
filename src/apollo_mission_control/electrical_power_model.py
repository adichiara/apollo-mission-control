"""Mission-neutral coarse electrical-power model.

This module provides decision-relevant causal power availability without
attempting battery chemistry, wiring-level circuit analysis, breaker arcing,
or Apollo-specific bus topology.

The model evaluates one electrical bus at a time:
available sources -> bus capacity -> commanded loads -> equipment availability.

Converters/inverters are represented separately as caller-supplied sources in
this first proof. A later converter model can derive those source states from
upstream buses without changing the bus/load contract.
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
class ElectricalSourceSpec:
    source_id: str
    max_power_w: float

    def validated(self) -> "ElectricalSourceSpec":
        max_power = _finite(self.max_power_w, f"{self.source_id}.max_power_w")
        if max_power < 0.0:
            raise ValueError("source max_power_w must be non-negative")
        return ElectricalSourceSpec(
            source_id=_text(self.source_id, "source_id"),
            max_power_w=max_power,
        )


@dataclass(frozen=True)
class ElectricalLoadSpec:
    load_id: str
    power_w: float
    priority: int = 0

    def validated(self) -> "ElectricalLoadSpec":
        power = _finite(self.power_w, f"{self.load_id}.power_w")
        if power < 0.0:
            raise ValueError("load power_w must be non-negative")
        if isinstance(self.priority, bool) or not isinstance(self.priority, int):
            raise ValueError("load priority must be an integer")
        return ElectricalLoadSpec(
            load_id=_text(self.load_id, "load_id"),
            power_w=power,
            priority=int(self.priority),
        )


@dataclass(frozen=True)
class ElectricalBusConfig:
    bus_id: str
    sources: tuple[ElectricalSourceSpec, ...]
    loads: tuple[ElectricalLoadSpec, ...]
    applicability: str = "generic electrical bus model proof; not mission validated"
    provenance: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = (
        "source capacities are caller supplied and additive on this bus",
        "load power demands are caller supplied constant values for this evaluation",
        "load shedding uses explicit integer priority with lower values served first",
        "equal-priority loads are all-or-none as a group",
        "no voltage-drop, wiring, breaker, transient, or battery-chemistry model",
        "converter/inverter availability is supplied upstream in this first proof",
    )

    def validated(self) -> "ElectricalBusConfig":
        bus_id = _text(self.bus_id, "bus_id")
        sources = tuple(source.validated() for source in self.sources)
        loads = tuple(load.validated() for load in self.loads)
        if not sources:
            raise ValueError("electrical bus requires at least one source")

        source_ids = [source.source_id for source in sources]
        if len(source_ids) != len(set(source_ids)):
            raise ValueError("duplicate electrical source_id")

        load_ids = [load.load_id for load in loads]
        if len(load_ids) != len(set(load_ids)):
            raise ValueError("duplicate electrical load_id")

        return ElectricalBusConfig(
            bus_id=bus_id,
            sources=sources,
            loads=loads,
            applicability=_text(self.applicability, "applicability"),
            provenance=tuple(self.provenance),
            assumptions=tuple(self.assumptions),
        )


@dataclass(frozen=True)
class ElectricalBusState:
    source_available: Mapping[str, bool]
    load_commanded_on: Mapping[str, bool]
    bus_enabled: bool = True

    def validated(self, config: ElectricalBusConfig) -> "ElectricalBusState":
        source_ids = {source.source_id for source in config.sources}
        load_ids = {load.load_id for load in config.loads}

        unknown_sources = sorted(set(self.source_available) - source_ids)
        if unknown_sources:
            raise ValueError(f"unknown electrical source state: {unknown_sources[0]}")
        unknown_loads = sorted(set(self.load_commanded_on) - load_ids)
        if unknown_loads:
            raise ValueError(f"unknown electrical load state: {unknown_loads[0]}")

        return ElectricalBusState(
            source_available={
                source_id: bool(self.source_available.get(source_id, False))
                for source_id in source_ids
            },
            load_commanded_on={
                load_id: bool(self.load_commanded_on.get(load_id, False))
                for load_id in load_ids
            },
            bus_enabled=bool(self.bus_enabled),
        )


@dataclass(frozen=True)
class ElectricalLoadResult:
    load_id: str
    commanded_on: bool
    supplied: bool
    power_w: float
    priority: int
    reason: str

    def to_dict(self) -> dict[str, object]:
        return {
            "load_id": self.load_id,
            "commanded_on": self.commanded_on,
            "supplied": self.supplied,
            "power_w": self.power_w,
            "priority": self.priority,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class ElectricalBusResult:
    bus_id: str
    bus_enabled: bool
    available_source_ids: tuple[str, ...]
    available_capacity_w: float
    commanded_demand_w: float
    supplied_demand_w: float
    overload_w: float
    loads: tuple[ElectricalLoadResult, ...]
    applicability: str
    provenance: tuple[str, ...]
    assumptions: tuple[str, ...]

    @property
    def bus_power_available(self) -> bool:
        return self.bus_enabled and self.available_capacity_w > 0.0

    def load(self, load_id: str) -> ElectricalLoadResult:
        for item in self.loads:
            if item.load_id == load_id:
                return item
        raise ValueError(f"unknown electrical load result: {load_id}")

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "electrical_bus_model_proof_not_historically_validated",
            "bus_id": self.bus_id,
            "bus_enabled": self.bus_enabled,
            "bus_power_available": self.bus_power_available,
            "available_source_ids": list(self.available_source_ids),
            "available_capacity_w": self.available_capacity_w,
            "commanded_demand_w": self.commanded_demand_w,
            "supplied_demand_w": self.supplied_demand_w,
            "overload_w": self.overload_w,
            "loads": [item.to_dict() for item in self.loads],
            "applicability": self.applicability,
            "provenance": list(self.provenance),
            "assumptions": list(self.assumptions),
        }


def evaluate_electrical_bus(
    config: ElectricalBusConfig,
    state: ElectricalBusState,
) -> ElectricalBusResult:
    """Evaluate source capacity, explicit load priority, and equipment supply.

    When commanded demand exceeds capacity, priority groups are considered in
    ascending integer order. A whole equal-priority group is supplied only when
    sufficient remaining capacity exists for the entire group. This avoids
    silently inventing an ordering among loads the caller declared equivalent.
    """

    cfg = config.validated()
    checked = state.validated(cfg)

    available_sources = tuple(
        source
        for source in cfg.sources
        if checked.bus_enabled and checked.source_available[source.source_id]
    )
    capacity = sum(source.max_power_w for source in available_sources)

    commanded = tuple(
        load for load in cfg.loads if checked.load_commanded_on[load.load_id]
    )
    commanded_demand = sum(load.power_w for load in commanded)

    supplied_ids: set[str] = set()
    remaining = capacity

    if checked.bus_enabled and capacity > 0.0:
        priorities = sorted({load.priority for load in commanded})
        for priority in priorities:
            group = tuple(load for load in commanded if load.priority == priority)
            group_demand = sum(load.power_w for load in group)
            if group_demand <= remaining + 1e-12:
                supplied_ids.update(load.load_id for load in group)
                remaining -= group_demand

    load_results: list[ElectricalLoadResult] = []
    for load in cfg.loads:
        commanded_on = checked.load_commanded_on[load.load_id]
        supplied = load.load_id in supplied_ids
        if not commanded_on:
            reason = "commanded_off"
        elif not checked.bus_enabled:
            reason = "bus_disabled"
        elif capacity <= 0.0:
            reason = "no_available_source"
        elif supplied:
            reason = "supplied"
        else:
            reason = "insufficient_capacity_at_priority"

        load_results.append(
            ElectricalLoadResult(
                load_id=load.load_id,
                commanded_on=commanded_on,
                supplied=supplied,
                power_w=load.power_w,
                priority=load.priority,
                reason=reason,
            )
        )

    supplied_demand = sum(
        item.power_w for item in load_results if item.supplied
    )

    return ElectricalBusResult(
        bus_id=cfg.bus_id,
        bus_enabled=checked.bus_enabled,
        available_source_ids=tuple(source.source_id for source in available_sources),
        available_capacity_w=capacity,
        commanded_demand_w=commanded_demand,
        supplied_demand_w=supplied_demand,
        overload_w=max(0.0, commanded_demand - capacity),
        loads=tuple(load_results),
        applicability=cfg.applicability,
        provenance=cfg.provenance,
        assumptions=cfg.assumptions,
    )
