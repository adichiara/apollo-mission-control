"""First-pass player-facing CAPCOM presentation for Apollo 13 PC+2.

CAPCOM is the normal operational air-ground voice path. This project rendering
shows only crew-facing procedure/PAD material and received crew reports already
represented in the common PC+2 projection layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .controller_products import ProjectionSet
from .pc2_nominal import Product


PROJECT_RENDERING_NOTICE = (
    "PROJECT RENDERING — documented PC+2 CAPCOM information; "
    "not an exact historical console transcription"
)


@dataclass(frozen=True)
class CapcomDisplayField:
    key: str
    label: str
    value: Any
    units: str | None
    validity: str
    source_layer: str
    provenance: str
    historical_analogue: str | None = None


@dataclass(frozen=True)
class CapcomPresentation:
    title: str
    notice: str
    source_basis: tuple[str, ...]
    fields: tuple[CapcomDisplayField, ...]


def _field(
    projection: ProjectionSet,
    key: str,
    label: str,
    *,
    historical_analogue: str | None = None,
) -> CapcomDisplayField | None:
    product: Product | None = projection.products.get(key)
    if product is None:
        return None
    return CapcomDisplayField(
        key=key,
        label=label,
        value=product.value,
        units=product.units,
        validity=product.validity.value,
        source_layer=product.source_layer,
        provenance=product.provenance,
        historical_analogue=historical_analogue,
    )


def build_pc2_capcom_presentation(projection: ProjectionSet) -> CapcomPresentation:
    """Build the minimum PC+2 CAPCOM communication/procedure view.

    CAPCOM should not receive direct authoritative subsystem truth merely for UI
    convenience. The view therefore contains the air-ground condition, final PAD
    material, and crew-report stream. Controller callout queues can be added when
    common session orchestration exposes them explicitly.
    """
    if projection.station != "CAPCOM":
        raise ValueError("PC+2 CAPCOM presentation requires a CAPCOM projection")

    fields = tuple(
        field
        for field in (
            _field(
                projection,
                "comm.air_ground_quality",
                "AIR-GROUND",
                historical_analogue="PC+2 final PAD/readback was affected by weak communications before the link improved",
            ),
            _field(
                projection,
                "ground.pc2.final_pad",
                "FINAL PC+2 PAD",
                historical_analogue="CAPCOM transmitted the final maneuver PAD and related burn/procedure information to the crew",
            ),
            _field(
                projection,
                "crew.report_stream",
                "CREW REPORTS",
                historical_analogue="Crew readbacks and burn-status reports are communications evidence, distinct from authoritative vehicle state",
            ),
        )
        if field is not None
    )

    return CapcomPresentation(
        title="CAPCOM — PC+2 AIR-GROUND / PROCEDURE",
        notice=PROJECT_RENDERING_NOTICE,
        source_basis=(
            "Apollo 13 Technical Air-to-Ground Voice Transcription",
            "Apollo 13 Mission Operations Report — PC+2 chronology",
        ),
        fields=fields,
    )
