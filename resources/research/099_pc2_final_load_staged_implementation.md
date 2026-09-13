# 099 — PC+2 staged final-load implementation boundary

Date: 2026-09-13  
Status: **IMPLEMENTED — source-bounded staging added; exact RTCC/CCATS internals remain deferred**

## Question

Research note 098 established that the final PC+2 state-vector/target-load workflow should not remain one generic `pending_final_verification` flag. The next unresolved repository item was to convert that evidence into executable state without inventing unsupported controller-keying, vector contents, or transmission timing.

## Primary-source check

The implementation remains bounded by the same mission-specific primary sources:

1. NASA Flight Control Division, *Mission Operations Report — Apollo 13* (28 April 1970): records a PC+2 Maneuver PAD update and state-vector/target-load uplink at approximately 75:35 GET, a later final maneuver-pad update near 78:00 GET, and the PC+2 execution chronology.
2. NASA, *Apollo 13 Technical Air-To-Ground Voice Transcription* (NTRS 20160014370): supports crew configuration for an uplink using P00, DATA/ACCEPT, and the UPDATA LINK path, followed by return of the computer to the crew and ranging verification in the final-preparation window.
3. NASA JSC Mission Control loop audio, preserved through the Apollo 13 in Real Time access layer: supports the cross-station FLIGHT/GUIDO/INCO dependency documented in note 098.

No new claim is made for exact RTCC Cartesian components, CCATS commands, controller keystrokes, or byte/word load contents.

## Executable model change

The authoritative `PC2State` now carries explicit workflow state:

- `pc2_solution_stage`: `preliminary` → `final_ready` → `final_stable`;
- `state_vector_load_status`: `preliminary_loaded` → `final_pending` → `transmitting` → `final_loaded`;
- `target_load_status`: same sequence;
- `uplink_configuration_ready`;
- `final_load_requested`;
- `final_load_transmission_started`;
- `final_load_complete`.

The nominal fixture now marks the earlier 75:35 load as already completed historical context and adds approximate final-preparation milestones. Approximate `~` event times are chronology anchors, not claims of second-level historical timing.

## Station information boundary

The staged workflow is projected without creating an omniscient combined view:

- **FIDO/RETRO:** final ground-solution stage / validity;
- **GUIDO:** solution stage plus state-vector and target-load status;
- **INCO:** uplink-configuration readiness and transmission-active state;
- **CAPCOM:** final-load requested/completed status alongside the existing crew-facing path;
- **FLIGHT:** final-solution stage and final-load completion.

This is an information/workflow model. It does not assert exact Apollo CRT placement for these project fields.

## Validation

Regression coverage now checks:

- all staged transitions;
- cross-station product separation;
- nominal completion at `final_stable` / `final_loaded`.

Physical human/device validation remains separate and unclaimed.

## Remaining boundary

Do not add exact transmission duration, vector contents, RTCC/CCATS command strings, or hidden verification semantics unless a primary source establishes them or a future exact-console/trajectory implementation requires them.

## Sources

- NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- NASA, *Apollo 13 Technical Air-To-Ground Voice Transcription*, NTRS 20160014370: https://ntrs.nasa.gov/citations/20160014370
- NASA JSC Mission Control audio via Apollo 13 in Real Time: https://apollo13realtime.org/

See `resources/source-catalog/PC2_FINAL_LOAD_UPLINK_SOURCES.md`.