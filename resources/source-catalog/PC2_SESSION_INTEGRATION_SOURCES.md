# Apollo 13 PC+2 Session Integration Sources

Status: active source supplement for the first playable session orchestration layer.

## 1. Apollo 13 Mission Operations Report

- **Organization:** NASA Manned Spacecraft Center / Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** Provides the controller/Flight Director chronology, PC+2 preparation sequence, controller responsibilities, and final readiness/GO context used by the session model.

## 2. Apollo 13 Technical Air-to-Ground Voice Transcription

- **Source class:** PRIMARY, contemporaneous mission communications
- **Use:** Establishes CAPCOM/crew information transfer, readbacks, procedural communication, burn-status reports, and timing anchors used by the session and communications layers.

## 3. Repository state-machine specification

- `docs/scenarios/APOLLO13_PC2_STATE_MACHINE.md`
- **Use:** Current normalized implementation contract for the historical interval.
- **Critical rule:** FLIGHT GO must be a controller decision, not an automatic consequence of nominal authoritative state.

## 4. Repository player-product specification

- `docs/scenarios/APOLLO13_PC2_PLAYER_PRODUCTS.md`
- **Use:** Defines station information boundaries and minimum first-slice player products.

## Implementation record

- `resources/research/079_pc2_first_playable_session_boundary.md`
- `src/apollo_mission_control/pc2_session.py`
- `tests/test_pc2_session.py`

## Evidence rule

The session layer may orchestrate documented controller decisions and communications, but it must not invent hidden readiness judgments or collapse controller reports into an automatic GO/NO-GO result.

Session/audit events are implementation objects. They should preserve the historical workflow boundaries rather than claim to be literal Apollo software records.
