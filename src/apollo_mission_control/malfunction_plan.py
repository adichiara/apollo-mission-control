"""Mission-neutral exercise malfunction plans.

A plan identifies one or more explicit causal insertions. This layer schedules
insertions only; it does not apply spacecraft, telemetry, controller, or mission
outcomes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from math import isfinite
from typing import Any


class InsertionMode(str, Enum):
    MANUAL = "manual"
    PREPROGRAMMED = "preprogrammed"
    TIME_DEPENDENT = "time_dependent"


class InsertionLayer(str, Enum):
    DYNAMICS = "dynamics"
    VEHICLE_SYSTEM = "vehicle_system"
    INSTRUMENTATION = "instrumentation"
    TELEMETRY = "telemetry"
    GROUND_INTERFACE = "ground_interface"


@dataclass(frozen=True)
class CausalInsertion:
    insertion_id: str
    layer: InsertionLayer
    target: str
    value: Any
    provenance: str


@dataclass(frozen=True)
class MalfunctionPlan:
    malfunction_id: str
    description: str
    mode: InsertionMode
    insertions: tuple[CausalInsertion, ...]
    provenance: str
    activation_time_s: float | None = None


@dataclass(frozen=True)
class MalfunctionActivation:
    malfunction_id: str
    activation_time_s: float
    mode: InsertionMode
    insertions: tuple[CausalInsertion, ...]
    provenance: str


@dataclass
class MalfunctionScheduler:
    plans: tuple[MalfunctionPlan, ...]
    activated: dict[str, MalfunctionActivation] = field(default_factory=dict)


def _clean(value: str, name: str) -> str:
    result = str(value).strip()
    if not result:
        raise ValueError(f"{name} must not be empty")
    return result


def validate_insertion(item: CausalInsertion) -> CausalInsertion:
    return CausalInsertion(
        insertion_id=_clean(item.insertion_id, "insertion_id"),
        layer=InsertionLayer(item.layer),
        target=_clean(item.target, "target"),
        value=item.value,
        provenance=_clean(item.provenance, "provenance"),
    )


def validate_plan(plan: MalfunctionPlan) -> MalfunctionPlan:
    mode = InsertionMode(plan.mode)
    if mode == InsertionMode.TIME_DEPENDENT:
        if plan.activation_time_s is None:
            raise ValueError("time-dependent malfunction requires activation_time_s")
        activation_time_s = float(plan.activation_time_s)
        if not isfinite(activation_time_s):
            raise ValueError("activation_time_s must be finite")
    else:
        if plan.activation_time_s is not None:
            raise ValueError(
                "activation_time_s is only valid for time-dependent malfunction plans"
            )
        activation_time_s = None

    insertions = tuple(validate_insertion(item) for item in plan.insertions)
    if not insertions:
        raise ValueError("malfunction plan requires at least one causal insertion")
    ids = [item.insertion_id for item in insertions]
    if len(ids) != len(set(ids)):
        raise ValueError("malfunction plan contains duplicate insertion_id values")

    return MalfunctionPlan(
        malfunction_id=_clean(plan.malfunction_id, "malfunction_id"),
        description=_clean(plan.description, "description"),
        mode=mode,
        insertions=insertions,
        provenance=_clean(plan.provenance, "provenance"),
        activation_time_s=activation_time_s,
    )


def activation_to_dict(item: MalfunctionActivation) -> dict[str, Any]:
    return {
        "malfunction_id": item.malfunction_id,
        "activation_time_s": item.activation_time_s,
        "mode": item.mode.value,
        "insertions": [
            {
                "insertion_id": insertion.insertion_id,
                "layer": insertion.layer.value,
                "target": insertion.target,
                "value": insertion.value,
                "provenance": insertion.provenance,
            }
            for insertion in item.insertions
        ],
        "provenance": item.provenance,
        "applies_downstream_effects": False,
    }


def _scheduler_post_init(self: MalfunctionScheduler) -> None:
    normalized = tuple(validate_plan(plan) for plan in self.plans)
    ids = [plan.malfunction_id for plan in normalized]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate malfunction_id values")
    self.plans = normalized


MalfunctionScheduler.__post_init__ = _scheduler_post_init
