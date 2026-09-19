"""Apollo landing-radar beam/frame transforms.

The rotation sequence and signs are ported from the original AGC SMNB/NBSM
AXISROT algorithm, independently preserved in Sunburst37 and superseded by
AX*SR*T in LUMINARY 099. Angles are radians; vectors are ordinary unscaled
floating-point triples. This module does not model AGC fixed-point rounding.
"""

from __future__ import annotations

from math import cos, isfinite, sin, sqrt
from typing import Iterable

Vector3 = tuple[float, float, float]


def _vector(value: Iterable[float]) -> Vector3:
    v = tuple(float(x) for x in value)
    if len(v) != 3 or not all(isfinite(x) for x in v):
        raise ValueError("vector must contain exactly three finite components")
    return v  # type: ignore[return-value]


def _angle(value: float) -> float:
    a = float(value)
    if not isfinite(a):
        raise ValueError("angle must be finite")
    return a


def _rotate(v: Vector3, axis: str, angle: float) -> Vector3:
    """AXISROT SMNB sense: positive right-handed coordinate rotation."""
    c, s = cos(angle), sin(angle)
    x, y, z = v
    if axis == "x":
        return (x, c * y - s * z, s * y + c * z)
    if axis == "y":
        return (c * x + s * z, y, -s * x + c * z)
    if axis == "z":
        return (c * x - s * y, s * x + c * y, z)
    raise ValueError("axis must be x, y, or z")


def stable_member_to_navigation_base(
    vector: Iterable[float], *, cdu_y_rad: float, cdu_z_rad: float, cdu_x_rad: float
) -> Vector3:
    """SM→NB: original SMNB sequence Y then Z then X."""
    v = _vector(vector)
    for axis, angle in (("y", cdu_y_rad), ("z", cdu_z_rad), ("x", cdu_x_rad)):
        v = _rotate(v, axis, _angle(angle))
    return v


def navigation_base_to_stable_member(
    vector: Iterable[float], *, cdu_y_rad: float, cdu_z_rad: float, cdu_x_rad: float
) -> Vector3:
    """NB→SM: inverse original NBSM sequence X then Z then Y."""
    v = _vector(vector)
    for axis, angle in (("x", -cdu_x_rad), ("z", -cdu_z_rad), ("y", -cdu_y_rad)):
        v = _rotate(v, axis, _angle(angle))
    return v


def antenna_to_navigation_base(
    vector: Iterable[float], *, beta_rad: float, alpha_rad: float
) -> Vector3:
    """SETPOS/Memo-95 antenna→NB convention: beta about Y, then alpha about X."""
    v = _rotate(_vector(vector), "y", _angle(beta_rad))
    return _rotate(v, "x", _angle(alpha_rad))


def landing_radar_velocity_beams_navigation_base(
    *, beta_rad: float, alpha_rad: float
) -> tuple[Vector3, Vector3, Vector3]:
    """Construct the three SETPOS velocity beams from antenna UNITX/UNITY.

    LUMINARY 099 transforms antenna UNITY and UNITX and forms the third beam by
    cross product. Returned order is X, Y, Z for model-facing component lookup.
    """
    x = antenna_to_navigation_base((1.0, 0.0, 0.0), beta_rad=beta_rad, alpha_rad=alpha_rad)
    y = antenna_to_navigation_base((0.0, 1.0, 0.0), beta_rad=beta_rad, alpha_rad=alpha_rad)
    z = (
        x[1] * y[2] - x[2] * y[1],
        x[2] * y[0] - x[0] * y[2],
        x[0] * y[1] - x[1] * y[0],
    )
    return x, y, z


def norm(vector: Iterable[float]) -> float:
    return sqrt(sum(x * x for x in _vector(vector)))
