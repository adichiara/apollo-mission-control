# Progress — PC+2 DPS shutdown command / physical response

Date: 2026-09-12

## Completed

- Continued directly from the ground-only ΔP shutdown-callout loop.
- Recovered contemporary LM control evidence showing that either crew STOP pushbutton initiates the descent-engine off command.
- Recovered the control-chain evidence that engine on/off commands actuate the descent-engine pilot valves, which hydraulically open/close the fuel and oxidizer shutoff valves.
- Added `resources/research/069_pc2_dps_shutdown_command_and_physical_response.md`.
- Added `resources/source-catalog/PC2_DPS_SHUTDOWN_RESPONSE_SOURCES.md`.
- Added exact operational action `press_engine_stop` while preserving the separation between crew input and physical response.
- Added `src/apollo_mission_control/dps_response.py` with explicit engine-off response semantics.
- Added `tests/test_pc2_dps_shutdown_response.py`.

## Architecture consequence

The shutdown chain now separates:

`ground callout → crew STOP pushbutton → engine-off physical response → later controller confirmation`

The STOP pushbutton action alone does not change `engine_running`.

The explicit physical-response event changes engine state and records engine-off/pilot-valve/shutoff-valve response, but it does not synthesize a chamber-pressure decay curve or controller confirmation.

## Evidence boundary

The exact LM-7 shutdown transient time remains unresolved. LM10-and-subsequent handbook material plus contemporary LM continuity documentation support the control architecture, but this pass does not claim a line-by-line LM-7 handbook certification.

## Test status

New tests are committed. Test execution remains unverified because the available container could not resolve `github.com` when attempting to clone the current repository.

## Next work

Determine the minimum source-backed **controller-observable engine-shutdown confirmation** path. Prefer already-documented GQ6510P chamber pressure or a directly sourced engine-thrusting discrete. Do not invent a shutdown timing/pressure trace; if confirmation routing cannot be recovered cheaply, stop and move to another PC+2 decision dependency.
