# Apollo Mission Control

A cooperative, historically grounded simulation of Apollo-era Mission Control.

Players sit together as flight controllers. Each player uses a phone as the display/interface for a controller station and printed controller material as needed. A central authoritative server owns the live mission simulation.

## Project standard

This project is **research first**. Apollo operations, terminology, displays, roles, procedures, telemetry, mission timelines, failure behavior, and simulator scenarios are implemented from historical documentation wherever documentation exists.

If a required detail is not documented or has not yet been found, it is recorded as unresolved. It is not silently invented.

See:

- [Project principles](docs/PROJECT_PRINCIPLES.md)
- [Roadmap](docs/ROADMAP.md)
- [Current first-playable integration roadmap](docs/roadmap/2026-09-12_first_playable_integration.md)
- [Decisions](docs/DECISIONS.md)
- [Simulation architecture](docs/SIMULATION_ARCHITECTURE.md)
- [PC+2 player products](docs/scenarios/APOLLO13_PC2_PLAYER_PRODUCTS.md)
- [Latest session progress](docs/progress/2026-09-12_first_playable_session.md)
- [Latest web-transport progress](docs/progress/2026-09-12_web_transport.md)
- [Research resources](resources/README.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

The first implementation-oriented vertical slice is **Apollo 13 PC+2 preparation and execution**.

The framework-neutral domain model now includes:

- source-backed nominal PC+2 event/state progression;
- station-specific controller-product projections;
- partial shutdown-rule evaluation;
- source-bounded scenario injection/action/communication layers;
- hidden product-integrity handling and explicit controller interpretation events;
- premature-shutdown/restart branches with command, physical-response, and controller-evidence boundaries kept separate;
- first-pass presentation models for **CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, and CAPCOM**;
- one authoritative session layer with station assignment, synchronized GET, readiness reports, FLIGHT decision gating, CAPCOM handoff, player-scoped snapshots, and audit logging;
- a scripted seven-station nominal integration playthrough through post-burn power-down.

## Phone-accessible first playable shell

The repository now also contains a thin **FastAPI + Uvicorn** transport and a dependency-free phone-first browser interface.

Implemented transport operations include:

- create/reset PC+2 session;
- join or rejoin a logical station;
- start/pause/resume;
- retrieve station-scoped player snapshots;
- submit readiness reports;
- record FLIGHT GO/NO-GO;
- queue FLIGHT-approved CAPCOM items;
- transmit those items as CAPCOM;
- manually advance GET for integration testing;
- inspect a prototype audit endpoint.

Deployment scaffolding is included for Render via `render.yaml`, with Python pinned through `.python-version`.

The first server is deliberately **single-process and in-memory**. Restart, redeploy, or service spin-down loses the current live session, and multiple workers would create conflicting authoritative state. That is acceptable for the first workflow/playability milestone, not for durable production games.

### Rejoin behavior

A browser/client may repeat the same player ID + station assignment to rejoin its existing station without modifying the mission state. The same player ID cannot silently switch stations, and a different player cannot take an occupied station.

This is lightweight prototype identity, not authentication.

## Critical gameplay boundary: FLIGHT GO

The older deterministic nominal validator automatically reaches historical GO at the final-poll timestamp. The playable session does not.

At approximately **79:17 GET**, session progression reaches the final readiness gate. The assigned FLIGHT player must explicitly record GO before the scenario can proceed toward P40. FLIGHT sees explicit controller readiness reports rather than a hidden consolidated subsystem-health verdict.

CAPCOM likewise sees an approved communication queue rather than direct authoritative subsystem truth.

## Historical/presentation boundaries retained

- Apollo 13 MSK 1137 `TCP` percent is not silently equated to modeled `GQ6510P` chamber pressure in psi.
- TELMU's documented **38–40 A** PC+2 burn-configuration figure remains a reference/configuration value, not fabricated live current telemetry.
- GUIDO post-burn residuals are not substituted for a missing FIDO propagated trajectory solution.
- INCO keeps link quality, voice, telemetry, ranging, and uplink as separate operational products.
- Hidden product integrity never appears automatically in a player view.
- Exact CRT/console layouts are not invented where the historical evidence is incomplete.

## Remaining bounded historical gaps

The singular PC+2 150-psi ground **engine inlet pressure** criterion remains intentionally `NOT_EVALUABLE`: separate LM-7 fuel (`GQ3611P`) and oxidizer (`GQ4111P`) interface-pressure measurements are known, but the historical ground selection/aggregation rule has not been established.

The onboard **77-percent thrust-monitor** criterion also remains `NOT_EVALUABLE`; the rule is documented but the exact crew percent-thrust indication/source remains unresolved.

Detailed DPS transients, exact display routing/cadence, and a post-burn FIDO trajectory propagator remain deferred until a concrete player/integration dependency requires them.

## Immediate priority

The project is now firmly in **playable integration**, not subsystem expansion.

The next architecture question is mission time. The current decision gate holds the session GET at the final-poll point until FLIGHT decides. Historical GET, however, did not stop. Before adding a real-time server clock, the implementation must explicitly define the relationship among:

- mission GET;
- scenario-event eligibility;
- player decision gates;
- explicit simulation pause;
- any future time acceleration.

The next practical integration items are:

1. resolve that mission-clock/gate policy rather than silently choosing one;
2. add browser-side reconnect persistence or a lightweight reconnect credential;
3. run the full domain/session/API suite when a runnable environment is available;
4. exercise one already-modeled nonnominal branch through the HTTP/session path;
5. only reopen historical research when one of those integration steps exposes a concrete information or decision gap.

## Apollo 13 station specifications

Detailed research specifications are under `docs/stations/`:

- [EECOM](docs/stations/APOLLO13_EECOM.md)
- [GNC](docs/stations/APOLLO13_GNC.md)
- [GUIDO](docs/stations/APOLLO13_GUIDO.md)
- [TELMU](docs/stations/APOLLO13_TELMU.md)
- [CONTROL](docs/stations/APOLLO13_CONTROL.md)
- [INCO](docs/stations/APOLLO13_INCO.md)
- [FIDO](docs/stations/APOLLO13_FIDO.md)
- [RETRO](docs/stations/APOLLO13_RETRO.md)
