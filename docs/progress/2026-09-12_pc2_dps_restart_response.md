# Progress — PC+2 DPS restart physical response

Date: 2026-09-12

## Completed

- Continued from the documented restart-command → physical-response boundary.
- Reconfirmed the Apollo 13 PC+2 Mission Rules restart contingency and contemporaneous crew-facing restart sequence.
- Used contemporary LM DPS documentation to bound the successful physical engine-on path: engine-on command → pilot valves open → propellant shutoff valves open → propellant flow/combustion.
- Added `resources/research/071_pc2_dps_restart_physical_response.md`.
- Added `resources/source-catalog/PC2_DPS_RESTART_RESPONSE_SOURCES.md`.
- Added `src/apollo_mission_control/dps_restart_response.py`.
- Added `tests/test_pc2_restart_response.py`.
- Kept restart eligibility, crew action sequence, physical response, and controller confirmation as separate concepts.
- Explicitly blocked physical restart response for rule-caused shutdowns or incomplete restart-action sequences.
- Left restart thrust level unresolved rather than aliasing it to minimum, 40-percent, or maximum thrust.
- Did not generate a chamber-pressure observation or restart transient.

## Historical boundary

The source base supports restartability and the valve/control chain but does not establish exact LM-7 restart timing, thrust level after contingency restart, GQ6510P buildup, or guaranteed success.

## Test status

New tests are committed. No successful execution is recorded in this pass.

## Next work

Return to the unresolved PC+2 controller-facing dependencies and select the next high-value item that materially affects player decisions. Keep low-value propulsion transient detail deferred unless later scenario work requires it.