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
- one authoritative session layer with station assignment, synchronized GET, readiness reports, FLIGHT decision gating, CAPCOM handoff, player-scoped snapshots, explicit pause reasons, and audit logging;
- a scripted seven-station nominal integration playthrough through post-burn power-down.

## Phone-accessible first playable shell

The repository contains a thin **FastAPI + Uvicorn** transport and a dependency-free phone-first browser interface.

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

## Critical gameplay boundary: FLIGHT GO and mission time

The playable session does not auto-authorize the PC+2 burn from hidden nominal state.

Primary-source review also resolved the ambiguity in what should happen to mission timing while FLIGHT deliberates:

- Apollo GET is a mission time reference; the reviewed sources do not say it stopped for a pending controller decision.
- The Apollo 13 Flight Control Division report says PC+2 ignition time was **not time critical**, but provides no numeric allowable delay.

The deterministic first playable slice therefore uses an explicit **simulation pause** at the blocking FLIGHT decision gate. At approximately **79:17 GET**:

- session status becomes `paused`;
- `pause_reason` becomes `decision_gate:flight_go`;
- controller readiness reports may still be submitted;
- manual resume cannot bypass the gate;
- FLIGHT GO clears the gate and resumes the simulation;
- NO-GO keeps the pause active;
- later historical events are not applied retroactively while the gate is unresolved.

This is a project playability policy, **not** a claim that historical Apollo GET stopped. No delay tolerance or retargeting rule is invented from “not time critical.” See `resources/research/081_pc2_mission_clock_and_decision_gate_semantics.md`.

CAPCOM continues to see an approved communication queue rather than direct authoritative subsystem truth.

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

The mission-clock/gate ambiguity is resolved for the deterministic first slice. The next practical integration items are:

1. persist player ID/station in the browser and automatically attempt same-player/same-station rejoin after reload;
2. run the full domain/session/API suite and multi-client HTTP/mobile smoke path in a runnable checked-out environment;
3. exercise one already-modeled nonnominal branch through the HTTP/session path;
4. add realtime pacing only after smoke validation, using the explicit simulation-pause policy;
5. reopen historical research only when one of those steps exposes a concrete information or decision gap.

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
