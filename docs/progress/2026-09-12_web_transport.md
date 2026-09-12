# Progress — first playable web transport

Date: 2026-09-12

## Completed

- Selected **FastAPI + Uvicorn** as the first playable transport shell while keeping the simulation/session domain framework-neutral.
- Added `src/apollo_mission_control/web_app.py` and a phone-first dependency-free client at `web/index.html`.
- Added `requirements.txt`, `.python-version`, `render.yaml`, and API tests.
- Recorded transport decision **D-014**.
- Exposed JSON operations for session creation/status, station join, lifecycle, GET advancement, station-scoped snapshots, readiness, FLIGHT decision, CAPCOM queue/transmission, and prototype audit access.
- Added idempotent same-player/same-station rejoin while preserving station-assignment protection.
- Resolved the mission-clock/decision-gate boundary in research note 081: blocking decision gates explicitly pause the simulation; this is not a claim that historical Apollo GET stopped.

## Browser rejoin checkpoint — completed

The phone client now:

- stores only the prototype `player_id` and station in browser `localStorage`;
- restores those form values after reload;
- attempts the existing idempotent same-player/same-station rejoin automatically when a server session exists;
- restarts station polling after successful rejoin;
- clears the stored identity when the local prototype creates/resets the server session.

This remains convenience identity only, not authentication or durable server persistence.

## First nonnominal web/session path — completed through CAPCOM transmission

Primary-source review was kept ahead of integration. The Apollo 13 Flight Control Division *Mission Operations Report* and Technical Air-To-Ground Voice Transcription establish the PC+2 fuel/oxidizer differential-pressure criterion as **>25 psi, ground callout**. They do not establish exact internal CONTROL→FLIGHT→CAPCOM routing, exact call wording, or an actual Apollo 13 exceedance.

The authoritative session/API can now exercise a synthetic source-bounded threshold case through:

1. explicit SimSup/source injection of `dps_fuel_oxidizer_delta_p_psi`;
2. normal CONTROL projection/presentation;
3. existing common shutdown-rule evaluation;
4. explicit CONTROL `CALL_OUT_SHUTDOWN_CRITERION` decision;
5. CAPCOM queue item marked `requested_by=CONTROL`;
6. explicit CAPCOM transmission.

The CAPCOM queue is explicitly a **project routing abstraction**, not a claim that the reviewed sources prove a particular internal Apollo voice-loop/approval sequence.

Separation remains strict:

- injection does not announce a diagnosis;
- triggered rule does not automatically create a controller decision;
- CONTROL callout does not automatically transmit;
- CAPCOM transmission does not automatically create crew compliance;
- no engine shutdown is forced by the communication path.

Added:

- `resources/research/082_pc2_delta_p_session_integration_boundary.md`;
- updated `PC2_DELTA_P_CALLOUT_SOURCES.md`;
- `tests/test_pc2_session_delta_p_integration.py`;
- `tests/test_web_delta_p_integration.py`;
- CONTROL browser callout control;
- prototype `/api/session/admin/injection` endpoint for scenario-authoring/validation only;
- `/api/session/control/{player_id}/delta-p-callout` player action.

The synthetic 26-psi test value is explicitly non-historical and exists only to cross the documented >25-psi boundary.

## Deployment boundary

The current server still holds one authoritative session in process memory. One worker is required; restart/redeploy/spin-down loses a live game; durable persistence and multiple concurrent sessions remain deferred.

## Test status

The new domain/API tests are committed. A full-suite execution is still not recorded as passing because this automation environment does not provide a checked-out repository runtime for executing the suite.

## Current stopping point

The browser-rejoin item and first nonnominal session/API path are now implemented.

The next source-sensitive integration boundary is **crew response after a transmitted ground shutdown callout**:

1. represent explicit crew receipt/response as a communication/operational event rather than automatic compliance;
2. route an explicit crew DPS shutdown command into the already-modeled command → physical DPS response → controller-evidence chain;
3. do not invent exact response delay, cockpit sequence, or physical shutdown timing;
4. then perform runnable HTTP/mobile smoke validation when an executable environment is available;
5. introduce a realtime driver only after this path is stable.
