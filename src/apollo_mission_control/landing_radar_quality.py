"""Mission-neutral landing-radar measurement qualification.

Separates raw radar/data-good state from downstream guidance-update eligibility.
No Apollo constants are embedded; callers supply persistence and residual rules.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Mapping


def _finite(value: float, name: str) -> float:
    number = float(value)
    if not isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


def _text(value: str, name: str) -> str:
    result = str(value).strip()
    if not result:
        raise ValueError(f"{name} must not be empty")
    return result


@dataclass(frozen=True)
class RadarScalarChannel:
    measured_value: float
    reference_value: float
    unit: str
    valid: bool = True

    def validated(self) -> "RadarScalarChannel":
        return RadarScalarChannel(
            measured_value=_finite(self.measured_value, "measured_value"),
            reference_value=_finite(self.reference_value, "reference_value"),
            unit=_text(self.unit, "unit"),
            valid=bool(self.valid),
        )


@dataclass(frozen=True)
class AffineResidualRule:
    fixed_tolerance: float
    proportional_tolerance: float = 0.0

    def validated(self) -> "AffineResidualRule":
        fixed = _finite(self.fixed_tolerance, "fixed_tolerance")
        proportional = _finite(
            self.proportional_tolerance,
            "proportional_tolerance",
        )
        if fixed < 0.0 or proportional < 0.0:
            raise ValueError("residual tolerances must be non-negative")
        return AffineResidualRule(
            fixed_tolerance=fixed,
            proportional_tolerance=proportional,
        )

    def threshold(self, reference_value: float) -> float:
        checked = self.validated()
        return checked.fixed_tolerance + (
            checked.proportional_tolerance * abs(float(reference_value))
        )


@dataclass(frozen=True)
class LandingRadarQualityInput:
    time_s: float
    data_good: bool
    data_good_since_s: float | None
    channels: Mapping[str, RadarScalarChannel]
    range_scale_last_changed_s: float | None = None
    source: str = "caller_supplied"

    def validated(self) -> "LandingRadarQualityInput":
        time_s = _finite(self.time_s, "time_s")
        good_since = (
            None
            if self.data_good_since_s is None
            else _finite(self.data_good_since_s, "data_good_since_s")
        )
        if good_since is not None and good_since > time_s:
            raise ValueError("data_good_since_s cannot be after time_s")
        scale_changed = (
            None
            if self.range_scale_last_changed_s is None
            else _finite(
                self.range_scale_last_changed_s,
                "range_scale_last_changed_s",
            )
        )
        if scale_changed is not None and scale_changed > time_s:
            raise ValueError("range_scale_last_changed_s cannot be after time_s")

        channels: dict[str, RadarScalarChannel] = {}
        for raw_name, raw_channel in self.channels.items():
            name = _text(raw_name, "channel name")
            channels[name] = raw_channel.validated()

        return LandingRadarQualityInput(
            time_s=time_s,
            data_good=bool(self.data_good),
            data_good_since_s=good_since,
            channels=channels,
            range_scale_last_changed_s=scale_changed,
            source=_text(self.source, "source"),
        )


@dataclass(frozen=True)
class LandingRadarQualityConfig:
    min_data_good_duration_s: float = 0.0
    min_range_scale_stable_s: float | None = None
    scale_stability_channels: tuple[str, ...] = ()
    residual_rules: Mapping[str, AffineResidualRule] = None  # type: ignore[assignment]
    applicability: str = "generic landing-radar quality model; not mission validated"
    provenance: tuple[str, ...] = ()

    def validated(self) -> "LandingRadarQualityConfig":
        min_good = _finite(
            self.min_data_good_duration_s,
            "min_data_good_duration_s",
        )
        if min_good < 0.0:
            raise ValueError("min_data_good_duration_s must be non-negative")

        stable = (
            None
            if self.min_range_scale_stable_s is None
            else _finite(
                self.min_range_scale_stable_s,
                "min_range_scale_stable_s",
            )
        )
        if stable is not None and stable < 0.0:
            raise ValueError("min_range_scale_stable_s must be non-negative")

        channels = tuple(
            _text(name, "scale stability channel")
            for name in self.scale_stability_channels
        )
        rules = {
            _text(name, "residual rule channel"): rule.validated()
            for name, rule in dict(self.residual_rules or {}).items()
        }
        if not rules:
            raise ValueError("at least one residual rule is required")

        return LandingRadarQualityConfig(
            min_data_good_duration_s=min_good,
            min_range_scale_stable_s=stable,
            scale_stability_channels=channels,
            residual_rules=rules,
            applicability=_text(self.applicability, "applicability"),
            provenance=tuple(self.provenance),
        )


@dataclass(frozen=True)
class RadarChannelQualityResult:
    channel: str
    unit: str
    residual: float
    absolute_residual: float
    threshold: float
    accepted: bool
    reasons: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "channel": self.channel,
            "unit": self.unit,
            "residual": self.residual,
            "absolute_residual": self.absolute_residual,
            "threshold": self.threshold,
            "accepted": self.accepted,
            "reasons": list(self.reasons),
        }


@dataclass(frozen=True)
class LandingRadarQualityResult:
    data_good_qualified: bool
    data_good_duration_s: float | None
    channels: tuple[RadarChannelQualityResult, ...]
    applicability: str
    provenance: tuple[str, ...]

    def channel(self, name: str) -> RadarChannelQualityResult:
        for item in self.channels:
            if item.channel == name:
                return item
        raise ValueError(f"unknown qualified radar channel: {name}")

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "landing_radar_quality_not_historically_validated",
            "data_good_qualified": self.data_good_qualified,
            "data_good_duration_s": self.data_good_duration_s,
            "channels": [item.to_dict() for item in self.channels],
            "applicability": self.applicability,
            "provenance": list(self.provenance),
        }


def qualify_landing_radar_measurements(
    observation: LandingRadarQualityInput,
    config: LandingRadarQualityConfig,
) -> LandingRadarQualityResult:
    checked = observation.validated()
    cfg = config.validated()

    good_duration = (
        None
        if not checked.data_good or checked.data_good_since_s is None
        else checked.time_s - checked.data_good_since_s
    )
    data_good_qualified = (
        checked.data_good
        and good_duration is not None
        and good_duration >= cfg.min_data_good_duration_s
    )

    results: list[RadarChannelQualityResult] = []
    for name, rule in cfg.residual_rules.items():
        channel = checked.channels.get(name)
        if channel is None:
            results.append(
                RadarChannelQualityResult(
                    channel=name,
                    unit="unknown",
                    residual=0.0,
                    absolute_residual=0.0,
                    threshold=0.0,
                    accepted=False,
                    reasons=("measurement_missing",),
                )
            )
            continue

        reasons: list[str] = []
        if not data_good_qualified:
            reasons.append("data_good_persistence_not_satisfied")
        if not channel.valid:
            reasons.append("channel_invalid")

        if (
            name in cfg.scale_stability_channels
            and cfg.min_range_scale_stable_s is not None
        ):
            if checked.range_scale_last_changed_s is None:
                reasons.append("range_scale_change_time_unknown")
            elif (
                checked.time_s - checked.range_scale_last_changed_s
                < cfg.min_range_scale_stable_s
            ):
                reasons.append("range_scale_not_stable_long_enough")

        residual = channel.measured_value - channel.reference_value
        threshold = rule.threshold(channel.reference_value)
        if abs(residual) > threshold:
            reasons.append("residual_outside_limit")

        results.append(
            RadarChannelQualityResult(
                channel=name,
                unit=channel.unit,
                residual=residual,
                absolute_residual=abs(residual),
                threshold=threshold,
                accepted=not reasons,
                reasons=tuple(reasons),
            )
        )

    return LandingRadarQualityResult(
        data_good_qualified=data_good_qualified,
        data_good_duration_s=good_duration,
        channels=tuple(results),
        applicability=cfg.applicability,
        provenance=cfg.provenance,
    )
