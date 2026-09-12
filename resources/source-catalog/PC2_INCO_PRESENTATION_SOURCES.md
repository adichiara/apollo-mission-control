# Apollo 13 PC+2 INCO Presentation Sources

Status: active source supplement for the first-pass INCO player rendering.

## 1. Apollo 13 Technical Air-to-Ground / Flight Journal chronology

- **Source class:** PRIMARY / contemporaneous mission communications and transcript-derived chronology
- **Relevant interval:** approximately 77:55–78:23 GET
- **Use:** Establishes weak communications during final preburn work, later clear communications, the 78:21:54 request to verify LM Ranging Function in Ranging, crew confirmation at approximately 78:22:14, and return of the computer to the crew at 78:23:05.
- **Implementation consequence:** Supports separate player-visible link-quality and ranging-state products.
- **Limitation:** Does not establish exact INCO CRT labels/coordinates or the detailed RF cause behind each quality state.

## 2. Apollo 13 Mission Report — Section 6.3, Communications Equipment

- **Organization:** NASA Manned Spacecraft Center
- **Date:** September 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** Establishes LM S-band communications, low-power/low-bit-rate operating configurations, separate voice/telemetry characteristics, and nominal use of the updata/uplink path when required.
- **Implementation consequence:** Supports keeping voice, telemetry, uplink, and overall link state as separate products.
- **Limitation:** Does not provide an exact PC+2 INCO console rendering.

## 3. Apollo 13 Mission Operations Report

- **Organization:** NASA Manned Spacecraft Center / Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** Controller/communications chronology and INCO operational context already incorporated into repository station research.
- **Repository cross-reference:** `docs/stations/APOLLO13_INCO.md`.

## Repository implementation record

- `resources/research/077_pc2_inco_player_presentation_boundary.md`
- `src/apollo_mission_control/inco_presentation.py`
- `tests/test_inco_presentation.py`

## Evidence rule

The first INCO interface is a **project rendering**, not a claimed Apollo CRT reconstruction.

Do not infer or add:

- exact INCO CRT fields/coordinates;
- antenna geometry not required by the slice;
- RF diagnosis from a link-quality state;
- a binary communications `GO` combining voice, telemetry, ranging, and uplink;
- hidden simulator integrity metadata.
