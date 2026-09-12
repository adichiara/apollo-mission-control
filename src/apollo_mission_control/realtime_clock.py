"""Wall-clock pacing adapter for an authoritative Mission Control session.

The domain session remains deterministic and advances to an explicit GET. This
adapter maps monotonic wall-clock elapsed time onto that domain API while keeping
pause semantics and event eligibility inside the session.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from time import monotonic
from typing import Callable

from .pc2_session import PC2Session, SessionStatus


@dataclass
class RealtimeSessionClock:
    session: PC2Session
    rate: float = 1.0
    now_fn: Callable[[], float] = monotonic
    _wall_anchor: float = field(init=False)
    _get_anchor: float = field(init=False)

    def __post_init__(self) -> None:
        if self.rate <= 0:
            raise ValueError("Realtime clock rate must be positive")
        self.reanchor()

    def reanchor(self) -> None:
        """Anchor wall time to the session's current authoritative GET."""
        self._wall_anchor = float(self.now_fn())
        self._get_anchor = float(self.session.state.get_s)

    def sync(self) -> float:
        """Advance the session to the GET implied by elapsed monotonic time.

        Only RUNNING sessions accrue GET. Explicit PAUSED/CREATED/COMPLETE
        sessions remain fixed. The current first-slice driver is capped at the
        final fixture event so a late HTTP poll does not advance beyond the
        modeled scenario interval.
        """
        if self.session.status != SessionStatus.RUNNING:
            return float(self.session.state.get_s)

        elapsed = max(0.0, float(self.now_fn()) - self._wall_anchor)
        target = self._get_anchor + elapsed * self.rate
        if self.session.events:
            target = min(target, float(self.session.events[-1].get_s))

        if target > self.session.state.get_s:
            self.session.advance_to(target)
        return float(self.session.state.get_s)
