"""First-pass player-facing INCO presentation for Apollo 13 PC+2.

This is a project rendering of documented communications information, not an
exact transcription of an Apollo INCO CRT. It exposes only controller-visible
communications products already represented in the PC+2 projection layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .controller_products import ProjectionSet
from .pc2_nominal import Product


PROJECT_RENDERING_NOTICE = (
    "PROJECT RENDERING — documented PC+2 INCO information; "
    "not an exact historical CRT transcription"
)


@dataclass(frozen=True)
class IncoDisplayField:
    key: str
    label: str
    value: Any
    units: str | None
    validity: str
    source_layer: str
    provenance: str
    historical_analogue: str | None = None


@dataclass(frozen=True)
class IncoDisplaySection:
    title: str
    fields: tuple[IncoDisplayField, ...]


@dataclass(frozen=True)
class IncoPresentation:
    title: str
    notice: str
    source_basis: tuple[str, ...]
    sections: tuple[IncoDisplaySection, ...]


def _field(
    projection: ProjectionSet,
    key: str,
    label: str,
    *,
    historical_analogue: str | None = None,
) -> IncoDisplayField | None:
    product: Product | None = projection.products.get(key)
    if product is None:
        return None
    return IncoDisplayField(
        key=key,
        label=label,
        value=product.value,
        units=product.units,
        validity=product.validity.value,
        source_layer=product.source_layer,
        provenance=product.provenance,
        historical_analogue=historical_analogue,
    )


def _section(title: str, *fields: IncoDisplayField | None) -> IncoDisplaySection:
    return IncoDisplaySection(title=title, fields=tuple(field for field in fields if field is not None))


def build_pc2_inco_presentation(projection: ProjectionSet) -> IncoPresentation:
    """Build the minimum PC+2 INCO view from controller-visible products.

    The PC+2 interval begins with weak air-ground communications, improves after
    a configuration change, and includes a specific request to verify that the
    LM ranging function is enabled before final burn support. Exact Apollo INCO
    CRT routing and antenna-geometry presentation remain outside this first pass.

    Deferred implementation fields and hidden integrity annotations are omitted.
    """
    if projection.station != "INCO":
        raise ValueError("PC+2 INCO presentation requires an INCO projection")

    sections = (
        _section(
            "AIR-GROUND LINK",
            _field(
                projection,
                "comm.air_ground_quality",
                "LINK QUALITY",
                historical_analogue="PC+2 chronology records weak communications before later becoming loud and clear; this project quality state is not asserted as an Apollo CRT literal",
            ),
            _field(projection, "comm.voice_available", "VOICE"),
            _field(projection, "comm.telemetry_available", "TELEMETRY"),
        ),
        _section(
            "NAV / COMMAND SUPPORT",
            _field(
                projection,
                "comm.ranging_enabled",
                "RANGING",
                historical_analogue="At 78:21:54 GET CAPCOM requested verification of the LM Ranging Function switch in Ranging; crew confirmed at 78:22:14",
            ),
            _field(
                projection,
                "comm.uplink_state",
                "UPLINK",
                historical_analogue="Apollo 13 communications documentation reports updata/uplink use when required; exact first-pass INCO status wording is project-rendered",
            ),
        ),
    )

    return IncoPresentation(
        title="INCO — PC+2 COMMUNICATIONS SUPPORT",
        notice=PROJECT_RENDERING_NOTICE,
        source_basis=(
            "Apollo 13 PC+2 chronology / technical air-ground communications",
            "Apollo 13 Mission Report — Communications Equipment",
            "Apollo 13 INCO station research specification",
        ),
        sections=sections,
    )
