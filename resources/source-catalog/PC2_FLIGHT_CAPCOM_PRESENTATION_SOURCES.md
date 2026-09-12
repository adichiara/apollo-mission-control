# Apollo 13 PC+2 FLIGHT/CAPCOM Presentation Sources

Status: active source supplement for the first-pass FLIGHT and CAPCOM player renderings.

## 1. Apollo 13 Mission Operations Report

- **Organization:** NASA Manned Spacecraft Center / Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** Establishes Flight Director integration/decision responsibility and controller chronology around PC+2.
- **Implementation consequence:** Supports keeping FLIGHT as a decision-integration station rather than an omniscient subsystem dashboard.

## 2. Apollo 13 Technical Air-to-Ground Voice Transcription

- **Source class:** PRIMARY, contemporaneous mission communications
- **Relevant interval:** final PC+2 preparation, burn, and immediate post-burn activity
- **Use:** Establishes CAPCOM as the normal crew-facing Mission Control voice path for final PAD/procedure transmission, readback, burn-status exchanges, and crew reports.
- **Implementation consequence:** Supports CAPCOM presentation around communications, PAD/procedure material, and crew reports rather than direct subsystem truth.

## Repository implementation record

- `resources/research/078_pc2_flight_capcom_player_presentation_boundary.md`
- `src/apollo_mission_control/flight_presentation.py`
- `src/apollo_mission_control/capcom_presentation.py`
- `tests/test_flight_capcom_presentations.py`

## Evidence rule

Do not add a FLIGHT consolidated health flag or CAPCOM subsystem dashboard unless a future source/workflow explicitly supports the product.

Readiness reports and callout queues belong in the common session/communication layer because they are controller communications/decisions, not hidden spacecraft state.
