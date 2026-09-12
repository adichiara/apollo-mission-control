# Apollo 13 PC+2 Session Integration Sources

Status: active source supplement for the first playable session orchestration layer.

## 1. Apollo 13 Mission Operations Report

- **Organization:** NASA Manned Spacecraft Center / Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **NTRS:** https://ntrs.nasa.gov/citations/19710010485
- **Use:** Provides the controller/Flight Director chronology, PC+2 preparation sequence, controller responsibilities, final readiness/GO context, and mission-clock boundary used by the session model.
- **Clock-specific evidence:** LM power-up around 78+12 GET; PC+2 ignition explicitly described as not time critical; final burn attitude / GO around 79:17 GET; actual ignition 79:27:38.30 GET; power-down around 79+34 GET.
- **Constraint:** the report does not specify a numeric allowable delay and does not state that GET stops while a controller decision is pending.

## 2. Apollo 13 Technical Air-to-Ground Voice Transcription

- **Source class:** PRIMARY, contemporaneous mission communications
- **NTRS:** https://ntrs.nasa.gov/citations/20160014370
- **Use:** Establishes CAPCOM/crew information transfer, readbacks, procedural communication, burn-status reports, and timing anchors used by the session and communications layers.

## 3. Apollo 13 GNC technical chronology

- **Organization:** NASA / Apollo technical-history record
- **NTRS:** https://ntrs.nasa.gov/citations/20090026451
- **Source class:** OFFICIAL NASA TECHNICAL SUPPORT, retrospective
- **Use:** Explicitly defines GET as starting at the integral second before liftoff/range zero. Used only to clarify the time-coordinate concept, not to invent Apollo 13 operational decisions.

## 4. Repository state-machine specification

- `docs/scenarios/APOLLO13_PC2_STATE_MACHINE.md`
- **Use:** Current normalized implementation contract for the historical interval.
- **Critical rule:** FLIGHT GO must be a controller decision, not an automatic consequence of nominal authoritative state.

## 5. Repository player-product specification

- `docs/scenarios/APOLLO13_PC2_PLAYER_PRODUCTS.md`
- **Use:** Defines station information boundaries and minimum first-slice player products.

## Implementation record

- `resources/research/079_pc2_first_playable_session_boundary.md`
- `resources/research/081_pc2_mission_clock_and_decision_gate_semantics.md`
- `src/apollo_mission_control/pc2_session.py`
- `tests/test_pc2_session.py`

## Evidence rule

The session layer may orchestrate documented controller decisions and communications, but it must not invent hidden readiness judgments or collapse controller reports into an automatic GO/NO-GO result.

A blocking gameplay gate may explicitly pause the **simulation**, but documentation and UI must not imply that historical Apollo GET itself stopped. No numeric PC+2 delay tolerance is introduced from the statement that TIG was not time critical.

Session/audit events are implementation objects. They should preserve the historical workflow boundaries rather than claim to be literal Apollo software records.
