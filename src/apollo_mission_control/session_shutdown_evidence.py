"""Session integration for controller-observable DPS shutdown evidence.

Evidence availability is kept separate from authoritative physical engine state.
No chamber-pressure value is interpreted as a binary engine-off threshold.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from .controller_products import project_controller_products
from .pc2_nominal import CrewReport
from .pc2_session import PC2Session
from .shutdown_confirmation import assess_dps_shutdown_evidence


def record_crew_shutdown_report(
    session: PC2Session,
    *,
    crew_id: str = "CREW",
) -> dict[str, Any]:
    """Record an explicit crew shutdown report at current authoritative GET.

    The stored ``shutdown`` label is a semantic report category for the model,
    not a claim that this hypothetical nonnominal response used exact wording.
    """
    if not session.state.crew_dps_shutdown_commanded:
        raise ValueError("Crew shutdown report requires a prior crew shutdown command")

    report = CrewReport(get_s=float(session.state.get_s), report="shutdown")
    session.state.crew_reports.append(report)
    event = session._audit(
        "crew_dps_shutdown_reported",
        crew_id,
        report_category="shutdown",
    )
    return asdict(event)


def assess_session_shutdown_evidence(session: PC2Session) -> dict[str, Any]:
    """Aggregate available post-command evidence for CONTROL.

    This helper does not consult ``engine_running`` and therefore cannot leak
    authoritative physical truth into controller evidence.
    """
    command_get_s = session.state.crew_dps_shutdown_command_get_s
    if command_get_s is None:
        raise ValueError("Shutdown evidence assessment requires a crew shutdown command")

    crew_report_get_s: float | None = None
    for event in reversed(session.audit_log):
        if event.kind == "crew_dps_shutdown_reported" and event.get_s >= command_get_s:
            crew_report_get_s = float(event.get_s)
            break

    projections = project_controller_products(session.state, session.fixture)
    pressure = projections["CONTROL"].products.get("dps.chamber_pressure_psi")

    evidence = assess_dps_shutdown_evidence(
        command_get_s=float(command_get_s),
        crew_report_get_s=crew_report_get_s,
        chamber_pressure_product=pressure,
    )
    return asdict(evidence)
