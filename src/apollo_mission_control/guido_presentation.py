"""First-pass player-facing GUIDO presentation for Apollo 13 PC+2.

This is a project rendering of documented guidance/computer information, not an
exact transcription of an Apollo CRT. Historical terminology is used only where
the modeled product has matching semantics; otherwise descriptive project labels
are retained.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .controller_products import ProjectionSet
from .pc2_nominal import Product


PROJECT_RENDERING_NOTICE = (
    "PROJECT RENDERING — documented PC+2 GUIDO information; "
    "not an exact historical CRT transcription"
)


@dataclass(frozen=True)
class GuidoDisplayField:
    key: str
    label: str
    value: Any
    units: str | None
    validity: str
    source_layer: str
    provenance: str
    historical_analogue: str | None = None


@dataclass(frozen=True)
class GuidoDisplaySection:
    title: str
    fields: tuple[GuidoDisplayField, ...]


@dataclass(frozen=True)
class GuidoPresentation:
    title: str
    notice: str
    source_basis: tuple[str, ...]
    sections: tuple[GuidoDisplaySection, ...]


def _field(
    projection: ProjectionSet,
    key: str,
    label: str,
    *,
    historical_analogue: str | None = None,
) -> GuidoDisplayField | None:
    product: Product | None = projection.products.get(key)
    if product is None:
        return None
    return GuidoDisplayField(
        key=key,
        label=label,
        value=product.value,
        units=product.units,
        validity=product.validity.value,
        source_layer=product.source_layer,
        provenance=product.provenance,
        historical_analogue=historical_analogue,
    )


def _section(title: str, *fields: GuidoDisplayField | None) -> GuidoDisplaySection:
    return GuidoDisplaySection(title=title, fields=tuple(field for field in fields if field is not None))


def build_pc2_guido_presentation(projection: ProjectionSet) -> GuidoPresentation:
    """Build the minimum PC+2 GUIDO view from controller-visible products.

    Apollo 13 MSK 1123/1137 and LUMINARY 1C data-link documentation establish
    that GUIDO had program/computer, warning/alarm, guidance/update, and
    velocity-related information available through mission-control processing.
    The current model does not reproduce exact field positions or assert that
    every project product appeared verbatim on a particular CRT.

    Deferred fields and hidden integrity annotations are intentionally omitted.
    """
    if projection.station != "GUIDO":
        raise ValueError("PC+2 GUIDO presentation requires a GUIDO projection")

    sections = (
        _section(
            "LGC / GUIDANCE STATUS",
            _field(
                projection,
                "pg_ns.lgc.operating",
                "LGC",
                historical_analogue="Apollo 13 GUIDO monitored LGC state; no exact binary OPERATING CRT field is asserted",
            ),
            _field(
                projection,
                "pg_ns.lgc.program",
                "PROGRAM",
                historical_analogue="Apollo 13 MSK 1137 includes program/verb/noun information; exact PC+2 field routing is not asserted",
            ),
            _field(
                projection,
                "pg_ns.lgc.program_alarm",
                "PROGRAM ALARM",
                historical_analogue="Apollo 13 MSK 1137 includes alarm-code information",
            ),
            _field(
                projection,
                "pg_ns.iss.warning",
                "ISS WARNING",
                historical_analogue="PC+2 Mission Rule uses ISS warning with program alarm; exact GUIDO CRT field remains unresolved",
            ),
            _field(
                projection,
                "pg_ns.lgc.warning",
                "LGC WARNING",
                historical_analogue="LGC failure/status information is present in LUMINARY downlists; exact presentation remains unresolved",
            ),
        ),
        _section(
            "ALIGNMENT / LOAD STATUS",
            _field(
                projection,
                "pg_ns.alignment.accepted",
                "ALIGNMENT",
                historical_analogue="GUIDO owned alignment verification; this is a project assessment product, not an asserted CRT literal",
            ),
            _field(
                projection,
                "pg_ns.state_vector_load_status",
                "STATE VECTOR LOAD",
                historical_analogue="LUMINARY P27/update downlink supports ground verification of uploaded data",
            ),
            _field(
                projection,
                "pg_ns.target_load_status",
                "TARGET LOAD",
                historical_analogue="LUMINARY P27/update downlink supports ground verification of uploaded data",
            ),
        ),
        _section(
            "MANEUVER / RESIDUAL",
            _field(
                projection,
                "pg_ns.vg_imu_planned",
                "PLANNED VG",
                historical_analogue="LUMINARY maneuver/downlink data include TIG and velocity-change/guidance quantities; exact display field is not asserted",
            ),
            _field(
                projection,
                "pg_ns.postburn_residual",
                "POSTBURN RESIDUAL",
                historical_analogue="Apollo 13 Mission Operations Report records PGNS residuals after PC+2; no exact CRT label/format is asserted",
            ),
        ),
    )

    return GuidoPresentation(
        title="GUIDO — PC+2 GUIDANCE MONITOR",
        notice=PROJECT_RENDERING_NOTICE,
        source_basis=(
            "Apollo 13 Guidance & Navigation Summary — MSK 1123/1137",
            "MIT R-567 LUMINARY 1C Section 2 — Data Links, Rev. 8",
            "Apollo 13 Mission Operations Report — GUIDO / PC+2 chronology",
        ),
        sections=sections,
    )
