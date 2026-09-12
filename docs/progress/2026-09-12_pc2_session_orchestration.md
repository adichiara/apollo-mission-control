# Progress — PC+2 session orchestration

Date: 2026-09-12

## Completed in this pass

- Confirmed that the minimum player-facing station set has reached its display-expansion stop condition: CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, and CAPCOM all have first-pass project renderings.
- Researched the next integration boundary against the contemporaneous Apollo 13 PC+2 record.
- Preserved the documented sequence of controller readiness -> FLIGHT decision -> CAPCOM crew-facing GO rather than computing or transmitting GO automatically.
- Added `src/apollo_mission_control/session_orchestration.py`.
- Added `tests/test_session_orchestration.py`.
- Added research note `079_pc2_session_orchestration_boundary.md`.
- Added `PC2_SESSION_ORCHESTRATION_SOURCES.md`.

## Implemented session behavior

- authoritative monotonic session GET;
- station/player assignment;
- per-station current readiness report plus retained history;
- explicit FLIGHT GO/NO-GO decision event;
- controller/FLIGHT callout queue;
- distinct CAPCOM-to-crew transmission event;
- monotonically sequenced audit/replay record.

## Critical boundaries retained

- all controllers reporting GO does not automatically set FLIGHT GO;
- a FLIGHT decision does not automatically reach the crew;
- a queued callout requires a separate CAPCOM transmission;
- crew-facing communication is not treated as physical spacecraft response;
- no exact undocumented internal voice-loop routing is invented;
- the session module is project architecture, not a historical MCC software reconstruction.

## Test status

The new tests are committed. No successful runtime execution is recorded in this pass.

## Next work

Connect session state to the existing controller product/presentation layer:

1. expose readiness reports to FLIGHT as session products;
2. make the explicit session FLIGHT decision drive the FLIGHT product rather than a separate disconnected flag;
3. expose pending callouts to CAPCOM without exposing hidden subsystem state;
4. record CAPCOM transmission through the existing procedural communication boundary;
5. provide assigned-station view selection from one synchronized session snapshot.

Network transport, persistence, reconnect, and phone UI should follow after this domain integration is stable.
