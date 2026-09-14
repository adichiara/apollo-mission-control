"""Mission-neutral tracking-observation proof.

This module demonstrates the separation

    authoritative trajectory state
        -> geometric tracking truth
        -> delayed/biased/available observation

without claiming Apollo/MSFN-specific tracking physics or ground processing.

All values are SI. No Earth, Moon, station, Apollo, or scenario constants are
embedded.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, sqrt
from typing import Iterable

from .causal_dps_model import Vector3
from .causal_translational_model import TranslationalState


def _finite(value: float, name: str) -> float:
    number = float(value)
    if not isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


def _vector(value: Iterable[float], name: str) -> Vector3:
    vector = tuple(_finite(component, name) for component in value)
    if len(vector) != 3:
        raise ValueError(f"{name} must have exactly three components")
    return vector  # type: ignore[return-value]


def _subtract(a: Vector3, b: Vector3) -> Vector3:
    return tuple(a[i] - b[i] for i in range(3))  # type: ignore[return-value]


def _dot(a: Vector3, b: Vector3) -> float:
    return sum(a[i] * b[i] for i in range(3))


def _magnitude(vector: Vector3) -> float:
    return sqrt(_dot(vector, vector))


@dataclass(frozen=True)
class TrackingStationState:
    """Caller-supplied inertial station state at the source epoch."""

    position_m: Vector3
    velocity_m_s: Vector3 = (0.0, 0.0, 0.0)

    def validated(self) -> "TrackingStationState":
        return TrackingStationState(
            position_m=_vector(self.position_m, "station.position_m"),
            velocity_m_s=_vector(self.velocity_m_s, "station.velocity_m_s"),
        )


@dataclass(frozen=True)
class GeometricTrackingTruth:
    """Internal geometric truth derived from authoritative states."""

    source_time_s: float
    range_m: float
    range_rate_m_s: float
    line_of_sight_unit: Vector3


@dataclass(frozen=True)
class TrackingObservationConfig:
    """Caller-supplied observation/processing effects.

    Bias and delay are deterministic by design. Random/noise models, signal
    propagation, atmospheric effects, clock error, network routing, and
    historical ground-processing behavior require separate sourced models.
    """

    receive_delay_s: float = 0.0
    range_bias_m: float = 0.0
    range_rate_bias_m_s: float = 0.0
    available: bool = True
    valid: bool = True
    source: str = "generic tracking observation proof"
    provenance: tuple[str, ...] = ()

    def validated(self) -> "TrackingObservationConfig":
        receive_delay_s = _finite(self.receive_delay_s, "receive_delay_s")
        range_bias_m = _finite(self.range_bias_m, "range_bias_m")
        range_rate_bias_m_s = _finite(
            self.range_rate_bias_m_s,
            "range_rate_bias_m_s",
        )
        source = self.source.strip()

        if receive_delay_s < 0.0:
            raise ValueError("receive_delay_s must be non-negative")
        if not source:
            raise ValueError("source must not be empty")

        return TrackingObservationConfig(
            receive_delay_s=receive_delay_s,
            range_bias_m=range_bias_m,
            range_rate_bias_m_s=range_rate_bias_m_s,
            available=bool(self.available),
            valid=bool(self.valid),
            source=source,
            provenance=tuple(self.provenance),
        )


@dataclass(frozen=True)
class TrackingObservation:
    source_time_s: float
    received_time_s: float
    age_s: float
    range_m: float | None
    range_rate_m_s: float | None
    available: bool
    valid: bool
    source: str
    provenance: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "tracking_observation_proof_not_historically_validated",
            "source_time_s": self.source_time_s,
            "received_time_s": self.received_time_s,
            "age_s": self.age_s,
            "range_m": self.range_m,
            "range_rate_m_s": self.range_rate_m_s,
            "available": self.available,
            "valid": self.valid,
            "source": self.source,
            "provenance": list(self.provenance),
        }


def compute_geometric_tracking_truth(
    vehicle_state: TranslationalState,
    station_state: TrackingStationState,
) -> GeometricTrackingTruth:
    """Compute line-of-sight range and range rate from authoritative states."""

    station = station_state.validated()
    vehicle_position = _vector(vehicle_state.position_m, "vehicle.position_m")
    vehicle_velocity = _vector(vehicle_state.velocity_m_s, "vehicle.velocity_m_s")
    source_time_s = _finite(vehicle_state.time_s, "vehicle.time_s")

    relative_position = _subtract(vehicle_position, station.position_m)
    range_m = _magnitude(relative_position)
    if range_m == 0.0:
        raise ValueError("vehicle and station positions must not coincide")

    line_of_sight = tuple(
        component / range_m for component in relative_position
    )
    relative_velocity = _subtract(vehicle_velocity, station.velocity_m_s)
    range_rate_m_s = _dot(relative_velocity, line_of_sight)  # type: ignore[arg-type]

    return GeometricTrackingTruth(
        source_time_s=source_time_s,
        range_m=range_m,
        range_rate_m_s=range_rate_m_s,
        line_of_sight_unit=line_of_sight,  # type: ignore[arg-type]
    )


def produce_tracking_observation(
    truth: GeometricTrackingTruth,
    config: TrackingObservationConfig,
) -> TrackingObservation:
    """Transform internal geometric truth into a controller-eligible observation."""

    checked = config.validated()
    source_time_s = _finite(truth.source_time_s, "truth.source_time_s")
    range_m = _finite(truth.range_m, "truth.range_m")
    range_rate_m_s = _finite(truth.range_rate_m_s, "truth.range_rate_m_s")

    if range_m < 0.0:
        raise ValueError("truth.range_m must be non-negative")

    received_time_s = source_time_s + checked.receive_delay_s

    if checked.available:
        observed_range_m = range_m + checked.range_bias_m
        observed_range_rate_m_s = range_rate_m_s + checked.range_rate_bias_m_s
    else:
        observed_range_m = None
        observed_range_rate_m_s = None

    return TrackingObservation(
        source_time_s=source_time_s,
        received_time_s=received_time_s,
        age_s=checked.receive_delay_s,
        range_m=observed_range_m,
        range_rate_m_s=observed_range_rate_m_s,
        available=checked.available,
        valid=checked.valid,
        source=checked.source,
        provenance=checked.provenance,
    )
