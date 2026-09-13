# Progress — multi-client integration validation

Date: 2026-09-12

## Completed in this pass

- Rechecked the next integration boundary against primary NASA simulation-training material before adding validation behavior.
- Added `tests/test_web_multiclient_integration.py` using independent clients for FLIGHT, CONTROL, CAPCOM, GUIDO, and facilitator/SimSup against one authoritative FastAPI session.
- Added `scripts/pc2_multiclient_smoke.py` for destructive real-network validation against a dedicated local or deployed server.
- Covered shared authoritative state, station-scoped information, rejoin, occupied-station protection, facilitator/player authority isolation, explicit pause semantics, full synthetic ΔP propagation, CONTROL shutdown evidence, and audit ordering.
- Preserved the synthetic 26 psi and 100 psi test values as explicitly non-historical.
- Added research note 089 and `INTEGRATED_SIMULATION_VALIDATION_SOURCES.md`.
- Added the real-network smoke runner to GitHub Actions using a dedicated ephemeral localhost Uvicorn process with facilitator authorization enabled.
- Executed the complete unit/integration suite and the real TCP/HTTP multi-client smoke successfully in CI.
- Kept documentation auditing in the same CI job so validation-state claims are checked with the code path they describe.

## Defects found and repaired

### Stale UI-role contract test

`tests/test_web_client_role_separation.py` still asserted the old pre-authorization phrase `not an authentication boundary` even though facilitator authorization is now implemented.

The test now expects the facilitator-authority/token UI and verifies the player page does not expose facilitator-token controls.

### Invalid admin evidence-class options

`web/admin.html` offered evidence-class values not accepted by `scenario_injection.EvidenceClass`.

The admin UI now uses exactly:

- `historical_event`;
- `documented_simulation_case`;
- `source_bounded_test`;
- `project_hypothetical`.

The client-role contract test now protects this mapping.

## Historical boundary

No new Apollo procedure is introduced by these changes.

Primary sources support integrated mission-environment simulation involving flight controllers at their consoles and a distinct simulation-control function. HTTP clients, browser polling, concurrency primitives, token authorization, localhost CI execution, and GitHub Actions are modern implementation infrastructure.

## Validation status

**Executed and passing in GitHub Actions as of 2026-09-12.**

The CI job now successfully completes:

1. dependency installation and `pip check`;
2. the complete `unittest` unit/integration suite;
3. a real-network Uvicorn server bound to `127.0.0.1:8000` with facilitator authorization enabled;
4. `scripts/pc2_multiclient_smoke.py` over actual TCP/HTTP against that server;
5. the documentation audit.

The network smoke therefore validates actual HTTP serialization/routing, concurrent client polling, rejoin, pause semantics, authority isolation, the synthetic ΔP path, CONTROL shutdown evidence, and audit ordering beyond the in-process TestClient contract.

This is **not** yet evidence of deployed internet behavior, mobile-browser behavior, or multi-device usability.

## Current stopping point

Automated runnable validation is no longer the blocker. The next integration boundary is live-device validation:

1. run several real phone/browser station clients plus one facilitator console against a dedicated server;
2. verify readability, continuous GET, reload/rejoin, simultaneous operation, and station information isolation under real browser/network conditions;
3. exercise FLIGHT/CAPCOM handoff and the nominal PC+2 path with human operators;
4. repair concrete runtime/usability defects exposed by that play;
5. reopen historical research only if a specific missing operational dependency appears.
