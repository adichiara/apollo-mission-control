# Progress — PC+2 crew response integration

Date: 2026-09-12

## Completed domain boundary

- Researched the boundary after CAPCOM transmission using the Apollo 13 Mission Operations Report, Apollo 13 technical air-ground transcript, and contemporary LM operations research.
- Confirmed that the >25 psi fuel/oxidizer differential-pressure rule was a ground-call shutdown criterion briefed to the crew before PC+2.
- Confirmed that the sources do not justify automatic crew compliance, an exact response delay, exact hypothetical response wording, or a unique cockpit choreography.
- Added `src/apollo_mission_control/crew_response.py`.
- Added explicit crew receipt as a communication/operational event.
- Reused the existing `OperationalAction(action="command_dps_shutdown")` path for crew shutdown command.
- Preserved crew command as distinct from physical DPS response.
- Reused `dps_response.apply_engine_off_response(...)` for the explicit vehicle response; response GET must be the current authoritative GET rather than an invented delay.
- Preserved chamber-pressure/controller evidence as a separate downstream layer.
- Added `tests/test_pc2_session_crew_response.py` covering transmission, receipt, command, response, and audit ordering.
- Added research note 083 and `PC2_CREW_RESPONSE_SOURCES.md`.

## HTTP integration — completed

The same chain is now exposed through the validation transport without adding automation between layers:

- `POST /api/session/crew/receipt/{item_id}` records explicit crew receipt of an already-transmitted DPS shutdown callout;
- `POST /api/session/crew/shutdown/{item_id}` records the explicit crew shutdown command and requires prior receipt;
- `POST /api/session/admin/vehicle/dps-engine-off` applies the explicit physical response at synchronized current GET and requires the prior crew command.

The default receipt string `received` is semantic test metadata, not historical wording.

`tests/test_web_crew_response.py` covers endpoint guardrails and audit ordering.

Research note 085 documents this transport boundary.

## Fidelity decisions

The authoritative nonnominal chain is now:

`source injection → CONTROL product/rule → CONTROL decision → CAPCOM queue → CAPCOM transmission → crew receipt → crew shutdown command → physical DPS response`

No stage silently implies the next.

The synthetic 26 psi case remains explicitly non-historical.

## Not claimed

- No historical ΔP exceedance during Apollo 13 PC+2 is asserted.
- No response latency is claimed.
- No exact crew readback wording is claimed.
- No exact hypothetical crewmember/control choreography is claimed beyond the generic source-supported DPS off-command architecture.
- No engine-off transient duration or chamber-pressure tailoff is fabricated.
- No telemetry value is treated as an automatic binary shutdown confirmation.

## Validation status

The tests are committed but the full suite is **not recorded as executed/passing** because this automation environment does not provide a checked-out runnable repository through the GitHub connector.

## Next stopping point

Connect the physical engine-off response to the existing source-bounded controller-evidence architecture:

- explicit crew shutdown report as one evidence channel;
- fresh post-command `GQ6510P` chamber-pressure observation as an independent channel;
- evidence aggregation through `shutdown_confirmation.py` without inventing a pressure threshold or automatic `engine_off_confirmed` state.
