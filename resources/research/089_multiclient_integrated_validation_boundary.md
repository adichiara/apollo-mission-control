# 089 — Multi-client integrated validation boundary

Date: 2026-09-12  
Status: **IMPLEMENTED AS AUTOMATED/NETWORK VALIDATION ARTIFACTS — live deployed smoke execution still pending**

## Question

What should the next validation layer test now that the first playable PC+2 slice has one authoritative session, station-scoped player views, a separate facilitator/SimSup authority path, and one complete source-bounded nonnominal branch?

## Primary-source basis

### Harold G. Miller — Simulation Training for Flight Control Decisionmaking

NASA SP-209 / NTRS `19700013438` describes Mercury/Gemini/Apollo flight controllers manning consoles to monitor and control crew/spacecraft activity, and describes simulation training in a mission environment as the culminating preparation for contingency handling, decision making, procedure verification, and mission-facility readiness.

Implementation implication:

- validation should exercise the simulation as an integrated operational system rather than only as isolated station/unit functions;
- several controller roles should observe and act through their own station interfaces against one shared mission state;
- contingency validation should verify information flow and decision/action sequencing, not merely final hidden state.

The source does **not** specify HTTP transport, phones, browser polling cadence, modern concurrency primitives, or software-authentication mechanics.

### NASA Apollo Mission Control Center restoration documentation

NASA's Apollo MCC restoration record identifies the Simulation Control Room as a support room adjacent to the Mission Operations Control Room.

Implementation implication:

- it remains appropriate for the project to validate controller clients and facilitator/simulation-control functions as separate operational surfaces sharing the same exercise.

This source does **not** imply the project's exact `/admin` UI or token mechanism.

## Validation architecture

Two complementary artifacts are now defined.

### 1. In-process multi-client contract test

`tests/test_web_multiclient_integration.py` creates independent FastAPI `TestClient` instances for:

- FLIGHT;
- CONTROL;
- CAPCOM;
- GUIDO;
- facilitator/SimSup.

The test verifies:

1. one authoritative session is shared by all clients;
2. station snapshots remain station-specific;
3. a fresh browser/client can rejoin the same player/station assignment;
4. a player cannot silently change stations or take an occupied station;
5. facilitator operations are rejected from ordinary station clients when authorization is configured;
6. explicit facilitator pause freezes GET;
7. the synthetic ΔP branch crosses CONTROL → CAPCOM → facilitator-modeled crew/vehicle response → CONTROL evidence without hidden shortcuts;
8. audit ordering preserves communication, command, physical-response, and evidence-layer separation;
9. fresh pressure evidence still does not become an `engine_off_confirmed` verdict.

This test is intentionally transport/integration coverage. It is not evidence that real browsers or a deployed network have been exercised.

### 2. Real-network smoke runner

`scripts/pc2_multiclient_smoke.py` is a destructive validation tool for a local or dedicated deployment.

It:

- resets one clean session;
- joins multiple stations;
- performs simultaneous HTTP polling from station identities;
- verifies rejoin;
- checks facilitator/player authority isolation when a token is configured;
- checks explicit pause/resume;
- executes the full synthetic ΔP branch;
- checks CONTROL evidence and audit ordering.

The script deliberately requires the operator to target a validation server because it resets and manipulates the active session.

## Defects found during this validation pass

The integration review exposed two pre-existing contract mismatches:

1. `tests/test_web_client_role_separation.py` still expected the superseded text `not an authentication boundary` after facilitator authorization had been implemented.
2. `/admin` offered evidence-class strings (`synthetic_boundary`, `documented_historical`, `source_bounded_hypothetical`) that were not members of the server's `EvidenceClass` enum.

The UI now presents the actual enum values:

- `historical_event`;
- `documented_simulation_case`;
- `source_bounded_test`;
- `project_hypothetical`.

Contract tests now protect that mapping.

## Historical guardrails

This work adds no new Apollo operational claims.

- Multi-client HTTP behavior is modern implementation infrastructure.
- The synthetic 26 psi ΔP case remains explicitly non-historical.
- The synthetic post-command 100 psi chamber-pressure observation remains deliberately non-historical and is used only to prove that freshness is not a binary shutdown threshold.
- Facilitator authorization remains a modern safety boundary, not an Apollo authentication reconstruction.

## Execution status

The new artifacts are committed, but this automation environment still cannot resolve `github.com` for a repository checkout and therefore cannot execute the full suite or the network smoke runner here.

No passing-test or successful-live-deployment claim is made.

## Next boundary

The next required step is actual execution rather than more architecture:

1. run the full repository test suite in a checked-out environment;
2. run `scripts/pc2_multiclient_smoke.py` against a dedicated local/Render instance;
3. exercise real phone browsers for station UI/rejoin/readability;
4. repair any runtime/usability defects found;
5. reopen historical research only if that live exercise reveals a specific missing operational dependency.
