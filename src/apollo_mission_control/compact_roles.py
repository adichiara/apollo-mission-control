"""Project-defined low-player-count ownership bundles for Apollo 13 PC+2.

These labels are simulator conveniences, not historical Apollo controller
positions.  Each value contains only original station identities; the domain
model continues to authorize and audit actions by those identities.
"""

from __future__ import annotations

COMPACT_FIVE_PLAYER_ROLES: dict[str, tuple[str, ...]] = {
    "FLIGHT": ("FLIGHT",),
    "CAPCOM": ("CAPCOM",),
    "LM_SYSTEMS": ("TELMU", "CONTROL"),
    "FLIGHT_DYNAMICS": ("GUIDO", "FIDO_RETRO"),
    "INCO": ("INCO",),
}


def compact_five_player_station_sets() -> tuple[tuple[str, ...], ...]:
    """Return the approved five-player ownership sets in presentation order."""
    return tuple(COMPACT_FIVE_PLAYER_ROLES.values())
