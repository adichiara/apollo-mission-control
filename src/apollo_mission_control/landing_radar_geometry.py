"""Landing-radar antenna-axis geometry.

Implements the fixed antenna -> Navigation Base Euler rotation used by the
Apollo 11 LGC landing-radar SETPOS path.

The historical LGC padloads LRALPHA/LRBETA are antenna-to-Navigation-Base
rotation angles. LUMINARY Memo #95 states that the rotations are applied in
the order LRBETA, LRALPHA. With zero Z rotation, this is represented here as

    R_ANT_TO_NB = R_x(LRALPHA) @ R_y(LRBETA)

The three returned columns are the antenna X/Y/Z unit axes expressed in
Navigation Base coordinates.

This module deliberately stops at Navigation Base. The measurement-time
Navigation-Base -> platform/common-frame transform is a separate dynamic
attitude dependency.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, isfinite, pi, sin, sqrt
from typing import Iterable


Vector3 = tuple[float, float, float]
Matrix3 = tuple[Vector3, Vector3, Vector3]


def _finite(value: float, name: str) -> float:
    result = float(value)
    if not isfinite(result):
        raise ValueError(f"{name} must be finite")
    return result


def _text(value: str, name: str) -> str:
    result = str(value).strip()
    if not result:
        raise ValueError(f"{name} must not be empty")
    return result


def _norm(vector: Vector3) -> float:
    return sqrt(sum(component * component for component in vector))


def _dot(left: Vector3, right: Vector3) -> float:
    return sum(a * b for a, b in zip(left, right))


def _cross(left: Vector3, right: Vector3) -> Vector3:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


@dataclass(frozen=True)
class LandingRadarAntennaOrientation:
    lralpha_revolutions: float
    lrbeta_revolutions: float
    position: str = "caller_supplied"
    applicability: str = (
        "landing-radar antenna to Navigation Base geometry; "
        "dynamic Navigation-Base attitude transform remains upstream/downstream"
    )
    provenance: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = (
        "LRALPHA is the LGC antenna-to-Navigation-Base X rotation",
        "LRBETA is the LGC antenna-to-Navigation-Base Y rotation",
        "the LGC applies LRBETA then LRALPHA with zero Z rotation",
        "angles are LGC padload values, not the opposite-sense R-567 alpha/beta definition",
    )

    def validated(self) -> "LandingRadarAntennaOrientation":
        return LandingRadarAntennaOrientation(
            lralpha_revolutions=_finite(
                self.lralpha_revolutions,
                "lralpha_revolutions",
            ),
            lrbeta_revolutions=_finite(
                self.lrbeta_revolutions,
                "lrbeta_revolutions",
            ),
            position=_text(self.position, "position"),
            applicability=_text(self.applicability, "applicability"),
            provenance=tuple(self.provenance),
            assumptions=tuple(self.assumptions),
        )


@dataclass(frozen=True)
class LandingRadarAntennaGeometry:
    position: str
    lralpha_revolutions: float
    lrbeta_revolutions: float
    lralpha_radians: float
    lrbeta_radians: float
    antenna_to_navigation_base: Matrix3
    x_axis_navigation_base: Vector3
    y_axis_navigation_base: Vector3
    z_axis_navigation_base: Vector3
    applicability: str
    provenance: tuple[str, ...]
    assumptions: tuple[str, ...]

    def axis(self, name: str) -> Vector3:
        key = str(name).strip().lower()
        if key in {"x", "vx", "x_axis"}:
            return self.x_axis_navigation_base
        if key in {"y", "vy", "y_axis"}:
            return self.y_axis_navigation_base
        if key in {"z", "vz", "z_axis"}:
            return self.z_axis_navigation_base
        raise ValueError(f"unknown landing-radar antenna axis: {name}")

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "landing_radar_antenna_navigation_base_geometry",
            "position": self.position,
            "lralpha_revolutions": self.lralpha_revolutions,
            "lrbeta_revolutions": self.lrbeta_revolutions,
            "lralpha_radians": self.lralpha_radians,
            "lrbeta_radians": self.lrbeta_radians,
            "antenna_to_navigation_base": [
                list(row) for row in self.antenna_to_navigation_base
            ],
            "axes_navigation_base": {
                "x": list(self.x_axis_navigation_base),
                "y": list(self.y_axis_navigation_base),
                "z": list(self.z_axis_navigation_base),
            },
            "applicability": self.applicability,
            "provenance": list(self.provenance),
            "assumptions": list(self.assumptions),
        }


def compute_landing_radar_antenna_geometry(
    orientation: LandingRadarAntennaOrientation,
) -> LandingRadarAntennaGeometry:
    """Compute antenna X/Y/Z axes in Navigation Base coordinates."""

    checked = orientation.validated()
    alpha = checked.lralpha_revolutions * 2.0 * pi
    beta = checked.lrbeta_revolutions * 2.0 * pi

    ca, sa = cos(alpha), sin(alpha)
    cb, sb = cos(beta), sin(beta)

    # R_x(alpha) @ R_y(beta): beta is applied first, then alpha.
    matrix: Matrix3 = (
        (cb, 0.0, sb),
        (sa * sb, ca, -sa * cb),
        (-ca * sb, sa, ca * cb),
    )

    # Columns of the antenna -> NB rotation matrix are antenna unit axes in NB.
    x_axis: Vector3 = (matrix[0][0], matrix[1][0], matrix[2][0])
    y_axis: Vector3 = (matrix[0][1], matrix[1][1], matrix[2][1])
    z_axis: Vector3 = (matrix[0][2], matrix[1][2], matrix[2][2])

    # Guard against accidental convention/matrix corruption.
    tolerance = 1.0e-12
    for label, axis in (("x", x_axis), ("y", y_axis), ("z", z_axis)):
        if abs(_norm(axis) - 1.0) > tolerance:
            raise ValueError(f"computed {label} axis is not unit length")
    for left, right in ((x_axis, y_axis), (x_axis, z_axis), (y_axis, z_axis)):
        if abs(_dot(left, right)) > tolerance:
            raise ValueError("computed landing-radar axes are not orthogonal")
    cross_xy = _cross(x_axis, y_axis)
    if any(abs(a - b) > tolerance for a, b in zip(cross_xy, z_axis)):
        raise ValueError("computed landing-radar axes are not right-handed")

    return LandingRadarAntennaGeometry(
        position=checked.position,
        lralpha_revolutions=checked.lralpha_revolutions,
        lrbeta_revolutions=checked.lrbeta_revolutions,
        lralpha_radians=alpha,
        lrbeta_radians=beta,
        antenna_to_navigation_base=matrix,
        x_axis_navigation_base=x_axis,
        y_axis_navigation_base=y_axis,
        z_axis_navigation_base=z_axis,
        applicability=checked.applicability,
        provenance=checked.provenance,
        assumptions=checked.assumptions,
    )
