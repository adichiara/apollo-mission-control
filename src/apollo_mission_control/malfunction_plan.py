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
