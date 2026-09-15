"""Mission-neutral source-state to measurement/output mapping.

This module makes one simulator boundary explicit:

    authoritative source/model state
        -> inspectable measurement definition
        -> exposed measurement value + availability/validity

Definitions are caller/profile supplied. Channel faults act only at the output
boundary and never mutate upstream source state. No Apollo measurement IDs,
channel inventories, redundant-channel combining rules, scaling laws, or
mission constants are embedded here.

The architecture is informed by the 1971 LMS Console Directory's explicit
measurement/output dictionary and separate telemetry-console malfunction
handling, plus independent AMS evidence for telemetry-layer faults. Historical
mission applicability still requires mission/vehicle-specific source evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import isfinite
from typing import Any, Mapping


class MeasurementKind(str, Enum):
    """Generic exposed representation; not an LMS numeric encoding."""

    ANALOG = "analog"
    EVENT = "event"


class MeasurementSourceKind(str, Enum):
    """Generic source-selection modes supported by this proof layer."""

    VARIABLE = "variable"
    FIXED = "fixed"


def _text(value: str, name: str) -> str:
    result = str(value).strip()
    if not result:
        raise ValueError(f"{name} must not be empty")
    return result


def _measurement_value(value: Any, kind: MeasurementKind, name: str) -> float | bool:
    if kind == MeasurementKind.ANALOG:
        if isinstance(value, bool):
            raise ValueError(f"{name} analog value must be numeric, not bool")
        try:
            number = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{name} analog value must be numeric") from exc
        if not isfinite(number):
            raise ValueError(f"{name} analog value must be finite")
        return number

    if kind == MeasurementKind.EVENT:
        if not isinstance(value, bool):
            raise ValueError(f"{name} event value must be bool")
        return value

    raise ValueError(f"unsupported measurement kind: {kind}")


@dataclass(frozen=True)
class MeasurementDefinition:
    """Inspectable profile-supplied mapping from one source to one output.

    applicable_profiles is intentionally generic. Empty means the caller
    has not restricted the definition by profile. A non-empty tuple requires
    active_profile to match one of the listed identifiers.

    Redundant-channel selection/combining is intentionally not implemented;
    it remains a separately sourced policy.
    """

    measurement_id: str
    description: str
    kind: MeasurementKind
    source_kind: MeasurementSourceKind
    source_key: str | None = None
    fixed_value: float | bool | None = None
    unit: str | None = None
    applicable_profiles: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()

    def validated(self) -> "MeasurementDefinition":
        measurement_id = _text(self.measurement_id, "measurement_id")
        description = _text(self.description, "description")
        kind = MeasurementKind(self.kind)
        source_kind = MeasurementSourceKind(self.source_kind)
        unit = None if self.unit is None else _text(self.unit, "unit")
        applicable_profiles = tuple(
            _text(value, "applicable profile") for value in self.applicable_profiles
        )
        if len(applicable_profiles) != len(set(applicable_profiles)):
            raise ValueError(
                f"measurement {measurement_id} contains duplicate applicable profiles"
            )

        if source_kind == MeasurementSourceKind.VARIABLE:
            if self.source_key is None:
                raise ValueError(
                    f"measurement {measurement_id} variable source requires source_key"
                )
            source_key = _text(self.source_key, "source_key")
            if self.fixed_value is not None:
                raise ValueError(
                    f"measurement {measurement_id} variable source must not set fixed_value"
                )
            fixed_value = None
        else:
            if self.source_key is not None:
                raise ValueError(
                    f"measurement {measurement_id} fixed source must not set source_key"
                )
            if self.fixed_value is None:
                raise ValueError(
                    f"measurement {measurement_id} fixed source requires fixed_value"
                )
            source_key = None
            fixed_value = _measurement_value(
                self.fixed_value,
                kind,
                f"measurement {measurement_id}.fixed_value",
            )

        if kind == MeasurementKind.ANALOG and unit is None:
            raise ValueError(f"measurement {measurement_id} analog output requires unit")
        if kind == MeasurementKind.EVENT and unit is not None:
            raise ValueError(f"measurement {measurement_id} event output must not set unit")

        return MeasurementDefinition(
            measurement_id=measurement_id,
            description=description,
            kind=kind,
            source_kind=source_kind,
            source_key=source_key,
            fixed_value=fixed_value,
            unit=unit,
            applicable_profiles=applicable_profiles,
            provenance=tuple(
                str(item).strip() for item in self.provenance if str(item).strip()
            ),
        )


@dataclass(frozen=True)
class MeasurementFault:
    """Explicit output-layer fault policy supplied by simulator/exercise control.

    This object does not describe a historical LMS malfunction code. It merely
    applies explicit caller choices at the measurement boundary.
    """

    measurement_id: str
    available: bool | None = None
    valid: bool | None = None
    replacement_value: float | bool | None = None
    provenance: str = "caller-supplied measurement fault"

    def validated(self) -> "MeasurementFault":
        return MeasurementFault(
            measurement_id=_text(self.measurement_id, "measurement_id"),
            available=None if self.available is None else bool(self.available),
            valid=None if self.valid is None else bool(self.valid),
            replacement_value=self.replacement_value,
            provenance=_text(self.provenance, "provenance"),
        )


@dataclass(frozen=True)
class MeasurementOutput:
    measurement_id: str
    description: str
    kind: MeasurementKind
    unit: str | None
    source_kind: MeasurementSourceKind
    source_key: str | None
    active_profile: str | None
    applicable: bool
    available: bool
    valid: bool
    value: float | bool | None
    fault_applied: bool
    fault_provenance: str | None
    provenance: tuple[str, ...]
    reasons: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "measurement_id": self.measurement_id,
            "description": self.description,
            "kind": self.kind.value,
            "unit": self.unit,
            "source_kind": self.source_kind.value,
            "source_key": self.source_key,
            "active_profile": self.active_profile,
            "applicable": self.applicable,
            "available": self.available,
            "valid": self.valid,
            "value": self.value,
            "fault_applied": self.fault_applied,
            "fault_provenance": self.fault_provenance,
            "provenance": list(self.provenance),
            "reasons": list(self.reasons),
        }


@dataclass(frozen=True)
class MeasurementOutputSet:
    outputs: tuple[MeasurementOutput, ...]
    active_profile: str | None
    applicability: str
    provenance: tuple[str, ...] = ()

    def measurement(self, measurement_id: str) -> MeasurementOutput:
        key = _text(measurement_id, "measurement_id")
        for output in self.outputs:
            if output.measurement_id == key:
                return output
        raise ValueError(f"unknown measurement output: {key}")

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": (
                "measurement_output_mapping_proof_not_historically_validated"
            ),
            "active_profile": self.active_profile,
            "applicability": self.applicability,
            "provenance": list(self.provenance),
            "outputs": [output.to_dict() for output in self.outputs],
            "mutates_source_state": False,
            "redundant_channel_combining_implemented": False,
        }


def evaluate_measurement_outputs(
    source_state: Mapping[str, Any],
    definitions: tuple[MeasurementDefinition, ...] | list[MeasurementDefinition],
    *,
    active_profile: str | None = None,
    faults: tuple[MeasurementFault, ...] | list[MeasurementFault] = (),
    applicability: str = "generic measurement/output mapping; not mission validated",
    provenance: tuple[str, ...] = (),
) -> MeasurementOutputSet:
    """Evaluate profile-driven measurements without modifying source state."""

    checked_definitions = tuple(item.validated() for item in definitions)
    if not checked_definitions:
        raise ValueError("at least one measurement definition is required")

    ids = [item.measurement_id for item in checked_definitions]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate measurement_id values")

    profile = None if active_profile is None else _text(active_profile, "active_profile")
    applicability_text = _text(applicability, "applicability")

    checked_faults = tuple(item.validated() for item in faults)
    fault_map: dict[str, MeasurementFault] = {}
    for fault in checked_faults:
        if fault.measurement_id in fault_map:
            raise ValueError(f"duplicate measurement fault: {fault.measurement_id}")
        fault_map[fault.measurement_id] = fault

    unknown_faults = sorted(set(fault_map) - set(ids))
    if unknown_faults:
        raise ValueError(
            f"measurement fault references unknown measurement: {unknown_faults[0]}"
        )

    outputs: list[MeasurementOutput] = []
    for definition in checked_definitions:
        reasons: list[str] = []
        applicable = (
            not definition.applicable_profiles
            or (
                profile is not None
                and profile in definition.applicable_profiles
            )
        )

        if not applicable:
            outputs.append(
                MeasurementOutput(
                    measurement_id=definition.measurement_id,
                    description=definition.description,
                    kind=definition.kind,
                    unit=definition.unit,
                    source_kind=definition.source_kind,
                    source_key=definition.source_key,
                    active_profile=profile,
                    applicable=False,
                    available=False,
                    valid=False,
                    value=None,
                    fault_applied=False,
                    fault_provenance=None,
                    provenance=definition.provenance,
                    reasons=("profile_not_applicable",),
                )
            )
            continue

        if definition.source_kind == MeasurementSourceKind.VARIABLE:
            assert definition.source_key is not None
            if definition.source_key not in source_state:
                raise ValueError(
                    f"measurement {definition.measurement_id} references missing "
                    f"source variable: {definition.source_key}"
                )
            raw_value = source_state[definition.source_key]
        else:
            raw_value = definition.fixed_value

        value = _measurement_value(
            raw_value,
            definition.kind,
            f"measurement {definition.measurement_id}",
        )
        available = True
        valid = True
        fault = fault_map.get(definition.measurement_id)
        fault_applied = fault is not None
        fault_provenance = None

        if fault is not None:
            fault_provenance = fault.provenance
            if fault.replacement_value is not None:
                value = _measurement_value(
                    fault.replacement_value,
                    definition.kind,
                    (
                        f"measurement fault "
                        f"{definition.measurement_id}.replacement_value"
                    ),
                )
                reasons.append("fault_replacement_value")
            if fault.available is not None:
                available = fault.available
                reasons.append("fault_availability_override")
            if fault.valid is not None:
                valid = fault.valid
                reasons.append("fault_validity_override")

        if not available:
            value = None
            valid = False
            reasons.append("measurement_unavailable")

        outputs.append(
            MeasurementOutput(
                measurement_id=definition.measurement_id,
                description=definition.description,
                kind=definition.kind,
                unit=definition.unit,
                source_kind=definition.source_kind,
                source_key=definition.source_key,
                active_profile=profile,
                applicable=True,
                available=available,
                valid=valid,
                value=value,
                fault_applied=fault_applied,
                fault_provenance=fault_provenance,
                provenance=definition.provenance,
                reasons=tuple(reasons),
            )
        )

    return MeasurementOutputSet(
        outputs=tuple(outputs),
        active_profile=profile,
        applicability=applicability_text,
        provenance=tuple(
            str(item).strip() for item in provenance if str(item).strip()
        ),
    )
