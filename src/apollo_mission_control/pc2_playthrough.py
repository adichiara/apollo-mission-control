"""Scripted nominal integration playthrough for the PC+2 session prototype.

This is an implementation validation harness, not a reconstruction of the exact
historical GO-poll wording or controller call sequence. It exercises the same
session interfaces future human players/clients will use.
"""

from __future__ import annotations

from typing import Any

from .pc2_nominal import hms_to_seconds
from .pc2_session import PC2Session


DEFAULT_PLAYERS = {
    "control_player": "CONTROL",
    "guido_player": "GUIDO",
    "telmu_player": "TELMU",
    "fido_retro_player": "FIDO_RETRO",
    "inco_player": "INCO",
    "flight_player": "FLIGHT",
    "capcom_player": "CAPCOM",
}


def run_scripted_nominal_playthrough(fixture: dict[str, Any]) -> PC2Session:
    """Exercise the nominal PC+2 session end-to-end through player interfaces.

    The readiness submissions below are a software integration fixture. They are
    intentionally not presented as the exact historical spoken poll roster or
    wording. Historical scenario timing still comes from the source-backed PC+2
    fixture.
    """
    session = PC2Session.create(fixture)
    for player_id, station in DEFAULT_PLAYERS.items():
        session.assign_station(player_id, station)

    session.start()

    # Advance beyond the historical final-poll time; the playable session must
    # continue through the FLIGHT decision gate rather than automatically setting GO.
    session.advance_to(hms_to_seconds("79:20:00"))

    for player_id in (
        "control_player",
        "guido_player",
        "telmu_player",
        "fido_retro_player",
        "inco_player",
    ):
        session.submit_readiness(
            player_id,
            ready=True,
            note="scripted nominal integration readiness; not historical poll wording",
        )

    session.record_flight_go(
        "flight_player",
        go=True,
        basis="scripted nominal integration: modeled controller reports ready",
    )

    item = session.queue_capcom_instruction(
        "flight_player",
        action="continue_pc2_burn_sequence",
        parameters={"decision": "go"},
        basis="scripted nominal integration after explicit FLIGHT GO",
    )
    session.transmit_capcom_item("capcom_player", item.item_id)

    # Note 101 extends the first-playable closure past initial LM powerdown to
    # the source-backed PTC-preparation transition at about 79:52 GET. No PTC
    # dynamics or switch-by-switch procedure is implied by this validation step.
    session.advance_to(hms_to_seconds("79:53:00"))
    return session
