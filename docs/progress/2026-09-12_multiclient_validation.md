# Progress — multi-client integration validation

Date: 2026-09-12

## Completed in this pass

- Rechecked the next integration boundary against primary NASA simulation-training material before adding validation behavior.
- Added `tests/test_web_multiclient_integration.py` using independent clients for FLIGHT, CONTROL, CAPCOM, GUIDO, and facilitator/SimSup against one authoritative FastAPI session.
- Added `scripts/pc2_multiclient_smoke.py` for destructive real-network validation against a dedicated local or deployed server.
- Covered shared authoritative state, station-scoped information, rejoin, occupied-station protection, facilitator/player authority isolation, explicit pause semantics, full synthetic ΔP propagation, CONTROL shutdown evidence, and audit ordering.
- Preserved the synthetic 26 psi and 100 psi test values as explicitly non-historical.
- Added research note 089 and `INTEGRATED_SIMULATION_VALIDATION_SOURCES.md`.

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

Primary sources support integrated mission-environment simulation involving flight controllers at their consoles and a distinct simulation-control function. HTTP clients, browser polling, concurrency primitives, and token authorization are modern implementation infrastructure.

## Validation status

The validation artifacts are committed but **not recorded as executed/passing** in this run.

This automation host still cannot resolve `github.com` from its execution container, so it cannot clone the repository to run the suite. It also has no target deployment URL/credential context from which to run the destructive network smoke script safely.

## Current stopping point

Actual execution is now the blocking validation step:

1. run the full test suite in a checked-out environment;
2. run `scripts/pc2_multiclient_smoke.py` against a dedicated local/Render validation instance;
3. perform real-phone browser checks for readability, reload/rejoin, and simultaneous operation;
4. fix concrete runtime/usability defects revealed by those runs;
5. only then reopen historical research if a specific missing operational dependency appears.
