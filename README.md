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
- one authoritative session layer with station assignment, continuous GET, readiness reports, FLIGHT decision requirements, CAPCOM handoff, player-scoped snapshots, explicit game pause, and audit logging;
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

## Core engine rule: mission time is continuous

The engine is a **continuously evolving mission**, not a sequence of scenes waiting for player input.

Apollo GET and controller-decision state are independent:

- GET advances whenever the session is running;
- pending controller decisions do not stop GET;
- missing authorization/procedure prerequisites may make a nominal event ineligible when its time arrives;
- missed nominal events are recorded and are not replayed retroactively;
- only an explicit game/session pause stops simulated mission time.

For the PC+2 final readiness sequence, the approximately **79:17 GET** FLIGHT poll opens a `flight_go` requirement while the clock continues. If GO is recorded before P40, the nominal preparation sequence can continue. If P40 time arrives first, that nominal milestone is missed; a later GO does not rewind the mission and activate it afterward.

The same dependency principle applies downstream to ullage, ignition, throttle milestones, cutoff, residual review, and post-burn transitions.

This deliberately avoids inventing a numeric PC+2 delay tolerance or automatic retargeting procedure from the source statement that ignition time was “not time critical.” Late recovery behavior must be represented by explicit procedures/actions when supported.

See:

- `resources/research/081_pc2_mission_clock_and_decision_gate_semantics.md` for the source findings and superseded provisional pause policy;
- `resources/research/084_continuous_mission_clock_architecture.md` for the current architecture;
- D-016 in `docs/DECISIONS.md`.

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

The continuous-clock architecture is resolved. The next integration items are:

1. generalize nominal-event prerequisites so scenario dependencies are declarative rather than hard-coded in PC+2 session logic;
2. expose crew receipt, crew shutdown command, and explicit physical response through the HTTP validation interface;
3. reconnect physical shutdown to the existing fresh controller-evidence path without inventing a confirmation threshold;
4. run the full domain/session/API suite and multi-client HTTP/mobile smoke path in a runnable checked-out environment;
5. replace manual GET advancement with a realtime pacing driver while preserving explicit game pause as the only clock stop.

Further historical research should reopen only when those integration steps expose a concrete information, procedure, or decision gap.

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
