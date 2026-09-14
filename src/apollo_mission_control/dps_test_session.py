"""Isolated manually clocked numerical test session; not a flight crew model."""
from copy import deepcopy
from dataclasses import asdict, replace
from math import ceil, isfinite
from .causal_dps_model import (
    BurnSegment, DPSModelConfig, ManeuverState, simulate_dps_maneuver)


class DPSTestSession:
    """Single-owner domain object. Transport must serialize concurrent access."""

    def __init__(self, initial, config):
        self.config = config.validated()
        self.initial = initial.validated(dry_mass_kg=self.config.dry_mass_kg)
        self.state = self.initial
        self.command = BurnSegment(0, 0, (0, 0, 0))
        self.events = []
        self.impulse_n_s = 0.0

    def _check_revision(self, expected_revision):
        if expected_revision != len(self.events):
            raise ValueError("stale revision")
        if len(self.events) >= 1000:
            raise ValueError("test event limit reached")

    def set_command(self, thrust_n, direction, *, expected_revision):
        self._check_revision(expected_revision)
        candidate = BurnSegment(0, thrust_n, tuple(direction)).validated()
        # Reject finite components whose magnitude overflows normalization.
        if candidate.thrust_n > 0 and not any(candidate.direction):
            raise ValueError("direction magnitude is not representable")
        self.command = candidate
        self.events.append({"kind": "command", "time_s": self.state.time_s,
                            "thrust_n": candidate.thrust_n,
                            "direction": list(candidate.direction)})
        return self.snapshot()

    def advance(self, duration_s, *, expected_revision):
        self._check_revision(expected_revision)
        duration = float(duration_s)
        if not isfinite(duration) or not 0 < duration <= 3600:
            raise ValueError("duration must be finite and in (0, 3600]")
        ratio = duration / self.config.max_step_s
        if not isfinite(ratio) or ceil(ratio) > 100000:
            raise ValueError("integration step budget exceeded")
        result = simulate_dps_maneuver(
            self.state, [replace(self.command, duration_s=duration)], self.config)
        # Commit only after the complete integration succeeds.
        self.state = replace(result.final_state, time_s=self.state.time_s + duration)
        self.impulse_n_s += result.impulse_n_s
        self.events.append({"kind": "advance", "duration_s": duration,
                            "result": result.to_dict()})
        return self.snapshot()

    def snapshot(self):
        return {"revision": len(self.events), "state": asdict(self.state),
                "command": asdict(self.command), "impulse_n_s": self.impulse_n_s}

    def export(self):
        return deepcopy({
            "schema_version": 1, "suite": "dps-stateful-domain-v1",
            "scope": "manual model time; not historical or crew validation",
            "initial": asdict(self.initial), "config": asdict(self.config),
            "events": self.events, "final": self.snapshot()})

    @classmethod
    def replay(cls, report):
        if report.get("schema_version") != 1:
            raise ValueError("unsupported report schema")
        session = cls(ManeuverState(**report["initial"]),
                      DPSModelConfig(**report["config"]))
        for event in report["events"]:
            revision = len(session.events)
            if event["kind"] == "command":
                session.set_command(event["thrust_n"], event["direction"],
                                    expected_revision=revision)
            elif event["kind"] == "advance":
                session.advance(event["duration_s"], expected_revision=revision)
            else:
                raise ValueError("unknown event kind")
        return session
