"""First-pass player-facing FIDO/RETRO presentation for Apollo 13 PC+2.

This is a project rendering of documented maneuver-target and return-plan
information. It is not an exact Apollo Flight Dynamics/RETRO CRT transcription
and does not invent a propagated post-burn trajectory solution.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .controller_products import ProjectionSet
from .pc2_nominal import Product


PROJECT_RENDERING_NOTICE = (
    "PROJECT RENDERING — documented PC+2 FIDO/RETRO information; "
    "not an exact historical CRT transcription"
)


@dataclass(frozen=True)
class FidoRetroDisplayField:
    key: str
    label: str
    value: Any
    units: str | None
    validity: str
    source_layer: str
    provenance: str
    historical_analogue: str | None = None


@dataclass(frozen=True)
class FidoRetroDisplaySection:
    title: str
    fields: tuple[FidoRetroDisplayField, ...]


@dataclass(frozen=True)
class FidoRetroPresentation:
    title: str
    notice: str
    source_basis: tuple[str, ...]
    sections: tuple[FidoRetroDisplaySection, ...]


def _field(
    projection: ProjectionSet,
    key: str,
    label: str,
    *,
    historical_analogue: str | None = None,
) -> FidoRetroDisplayField | None:
    product: Product | None = projection.products.get(key)
    if product is None:
        return None
    return FidoRetroDisplayField(
        key=key,
        label=label,
        value=product.value,
        units=product.units,
        validity=product.validity.value,
        source_layer=product.source_layer,
        provenance=product.provenance,
        historical_analogue=historical_analogue,
    )


def _section(title: str, *fields: FidoRetroDisplayField | None) -> FidoRetroDisplaySection:
    return FidoRetroDisplaySection(title=title, fields=tuple(field for field in fields if field is not None))


def build_pc2_fido_retro_presentation(projection: ProjectionSet) -> FidoRetroPresentation:
    """Build the minimum PC+2 FIDO/RETRO view from modeled ground products.

    The final PC+2 maneuver PAD and monitor PAD are directly documented in the
    Apollo 13 air-ground record. Exact historical FIDO/RETRO CRT routing is not.
    Deferred RTCC Cartesian state and post-burn propagated trajectory products
    are omitted rather than fabricated or shown as failed telemetry.
    """
    if projection.station != "FIDO_RETRO":
        raise ValueError("PC+2 FIDO/RETRO presentation requires a FIDO_RETRO projection")

    sections = (
        _section(
            "MANEUVER TARGET",
            _field(
                projection,
                "ground.pc2.tig_get_s",
                "TIG",
                historical_analogue="Final PC+2 P30 LM maneuver PAD Noun 33: 79:27:38.30 GET",
            ),
            _field(
                projection,
                "ground.pc2.pad_dv_lvlh",
                "PAD DV LVLH",
                historical_analogue="Final PC+2 maneuver PAD Noun 81 LVLH components; project field preserves the documented vector as one product",
            ),
            _field(
                projection,
                "ground.pc2.expected_perigee_nmi",
                "EXPECTED PERIGEE",
                historical_analogue="Final PC+2 maneuver PAD expected perigee 20.5 nmi",
            ),
        ),
        _section(
            "RETURN PLAN",
            _field(
                projection,
                "ground.return.plan",
                "PC+2 MONITOR PAD",
                historical_analogue="Final monitor PAD read at 78:00:58 GET: Noun 61 landing coordinates plus range-to-go, entry-interface velocity, and 0.05-g GET",
            ),
        ),
        _section(
            "GROUND SOLUTION",
            _field(
                projection,
                "ground.rtcc.solution_valid",
                "SOLUTION STATUS",
                historical_analogue="Project ground-solution status; FIDO historically owned trajectory-data/vector quality, but no exact PC+2 CRT literal is asserted",
            ),
        ),
    )

    return FidoRetroPresentation(
        title="FIDO / RETRO — PC+2 TARGET / RETURN",
        notice=PROJECT_RENDERING_NOTICE,
        source_basis=(
            "Apollo 13 final P30 LM maneuver PAD around 77:52 GET",
            "Apollo 13 PC+2 monitor PAD at 78:00:58 GET",
            "Apollo 13 Mission Operations Report — FIDO and RETRO post-mission reports",
        ),
        sections=sections,
    )
