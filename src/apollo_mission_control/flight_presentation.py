"""First-pass player-facing FLIGHT presentation for Apollo 13 PC+2.

FLIGHT integrates discipline reports and makes mission decisions. This project
rendering therefore remains deliberately sparse and never exposes a hidden
consolidated subsystem-health verdict.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .controller_products import ProjectionSet
from .pc2_nominal import Product


PROJECT_RENDERING_NOTICE = (
    "PROJECT RENDERING — documented PC+2 FLIGHT information; "
    "not an exact historical console transcription"
)


@dataclass(frozen=True)
class FlightDisplayField:
    key: str
    label: str
    value: Any
    units: str | None
    validity: str
    source_layer: str
    provenance: str
    historical_analogue: str | None = None


@dataclass(frozen=True)
class FlightPresentation:
    title: str
    notice: str
    source_basis: tuple[str, ...]
    fields: tuple[FlightDisplayField, ...]


def _field(
    projection: ProjectionSet,
    key: str,
    label: str,
    *,
    historical_analogue: str | None = None,
) -> FlightDisplayField | None:
    product: Product | None = projection.products.get(key)
    if product is None:
        return None
    return FlightDisplayField(
        key=key,
        label=label,
        value=product.value,
        units=product.units,
        validity=product.validity.value,
        source_layer=product.source_layer,
        provenance=product.provenance,
        historical_analogue=historical_analogue,
    )


def build_pc2_flight_presentation(projection: ProjectionSet) -> FlightPresentation:
    """Build the minimum PC+2 FLIGHT decision view.

    The historical workflow has FLIGHT integrate controller readiness and make
    the GO/NO-GO decision. The current common projection does not yet model the
    individual readiness-report stream, so that deferred implementation field is
    omitted rather than replaced with an omniscient readiness summary.
    """
    if projection.station != "FLIGHT":
        raise ValueError("PC+2 FLIGHT presentation requires a FLIGHT projection")

    fields = tuple(
        field
        for field in (
            _field(
                projection,
                "mission.phase",
                "MISSION PHASE",
                historical_analogue="Project session/state orientation; not asserted as a literal Apollo FLIGHT display field",
            ),
            _field(
                projection,
                "flight.go_for_burn",
                "GO FOR BURN",
                historical_analogue="PC+2 final readiness culminated in a Flight Director GO decision; this field represents that decision state, not an automatic system-health result",
            ),
        )
        if field is not None
    )

    return FlightPresentation(
        title="FLIGHT — PC+2 DECISION STATUS",
        notice=PROJECT_RENDERING_NOTICE,
        source_basis=(
            "Apollo 13 Mission Operations Report — Flight Director / PC+2 chronology",
            "Apollo 13 PC+2 state-machine research",
        ),
        fields=fields,
    )
