"""Controller-observable DPS shutdown evidence for the PC+2 prototype.

This module aggregates evidence channels without inventing a historical
engine-off telemetry threshold or turning evidence into authoritative truth.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .pc2_nominal import Product


class ShutdownEvidenceState(str, Enum):
    NONE = "none"
    CREW_REPORTED = "crew_reported"
    GROUND_PRESSURE_OBSERVED = "ground_pressure_observed"
    CORROBORATED = "corroborated"


@dataclass(frozen=True)
class DPSShutdownEvidence:
    state: ShutdownEvidenceState
    command_get_s: float
    crew_report_get_s: float | None = None
    chamber_pressure_psi: float | None = None
    chamber_pressure_observed_get_s: float | None = None
    note: str = ""


def assess_dps_shutdown_evidence(
    *,
    command_get_s: float,
    crew_report_get_s: float | None = None,
    chamber_pressure_product: Product | None = None,
) -> DPSShutdownEvidence:
    """Aggregate controller-observable evidence after a shutdown command.

    A chamber-pressure value only counts as response evidence if its source or
    sample time is later than the shutdown command. No pressure threshold is
    interpreted as an `engine off` definition.
    """
    command_get_s = float(command_get_s)

    crew_reported = (
        crew_report_get_s is not None and float(crew_report_get_s) >= command_get_s
    )

    pressure_value: float | None = None
    pressure_observed_get_s: float | None = None
    ground_observed = False

    if chamber_pressure_product is not None:
        observed = chamber_pressure_product.sample_time_get
        if observed is None:
            observed = chamber_pressure_product.source_time_get
        if observed is not None and float(observed) > command_get_s:
            ground_observed = True
            pressure_observed_get_s = float(observed)
            if chamber_pressure_product.value is not None:
                pressure_value = float(chamber_pressure_product.value)

    if crew_reported and ground_observed:
        state = ShutdownEvidenceState.CORROBORATED
    elif crew_reported:
        state = ShutdownEvidenceState.CREW_REPORTED
    elif ground_observed:
        state = ShutdownEvidenceState.GROUND_PRESSURE_OBSERVED
    else:
        state = ShutdownEvidenceState.NONE

    return DPSShutdownEvidence(
        state=state,
        command_get_s=command_get_s,
        crew_report_get_s=None if crew_report_get_s is None else float(crew_report_get_s),
        chamber_pressure_psi=pressure_value,
        chamber_pressure_observed_get_s=pressure_observed_get_s,
        note=(
            "Evidence availability only; no historical chamber-pressure "
            "threshold is interpreted as a binary engine-off confirmation."
        ),
    )
