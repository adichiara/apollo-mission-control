# Apollo Mission Control

A cooperative, historically grounded simulation of Apollo-era Mission Control.

Players sit together as flight controllers. Each player uses a phone as the display/interface for a controller station and uses printed station documentation such as flight rules and procedures. A central server maintains the live mission simulation.

## Project standard

This project is **research first**. Apollo operations, terminology, displays, roles, procedures, telemetry, mission timelines, failure behavior, and simulator scenarios are implemented from historical documentation wherever documentation exists.

If a required detail is not documented or has not yet been found, it is recorded as unresolved. It is not silently invented.

See:

- [Project principles](docs/PROJECT_PRINCIPLES.md)
- [Roadmap](docs/ROADMAP.md)
- [Current first-playable integration roadmap addendum](docs/roadmap/2026-09-12_first_playable_integration.md)
- [Simulation architecture](docs/SIMULATION_ARCHITECTURE.md)
- [Controller information workflow](docs/CONTROLLER_INFORMATION_WORKFLOW.md)
- [Apollo 13 station baseline](docs/APOLLO13_STATION_BASELINE.md)
- [Station research status](docs/STATION_RESEARCH_STATUS.md)
- [Latest station/session status](docs/station-status/2026-09-12_first_playable_session.md)
- [Progress log](docs/PROGRESS.md)
- [Latest first-playable session progress](docs/progress/2026-09-12_first_playable_session.md)
- [Research resources](resources/README.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

The first implementation-oriented vertical slice is **Apollo 13 PC+2 preparation and execution**.

The framework-neutral Python prototype now includes:

- source-backed nominal PC+2 event/state progression;
- station-specific controller-product projections;
- partial shutdown-rule evaluation;
- source-bounded scenario injection/action/communication layers;
- hidden product-integrity handling and explicit controller interpretation events;
- premature-shutdown / restart branches with command, physical-response, and controller-evidence boundaries kept separate;
- first-pass player-facing presentation models for **CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, and CAPCOM**;
- a new **single-process authoritative session layer** for station assignment, synchronized GET, readiness reports, FLIGHT decision gating, CAPCOM handoff, and audit logging.

## Player-facing presentation checkpoint

The minimum first-slice station presentation set is now complete.

Where exact Apollo display evidence is incomplete, each interface is explicitly labeled a **project rendering** of documented controller information rather than a reconstructed historical CRT. Controller-facing values preserve their units, validity, source layer, and provenance. Hidden simulator integrity is not exposed, and unmodeled fields are omitted instead of being presented as failed historical telemetry.

Key fidelity boundaries remain intact:

- historical MSK 1137 `TCP` percent is not silently equated to modeled `GQ6510P` chamber pressure in psi;
- TELMU's documented **38–40 A** burn-configuration figure remains a reference/configuration value rather than fabricated live current telemetry;
- GUIDO residuals are not substituted for a missing FIDO post-burn propagated trajectory solution;
- INCO keeps link quality, voice, telemetry, ranging, and uplink as separate operational products;
- FLIGHT does not receive a consolidated omniscient subsystem-health dashboard;
- CAPCOM remains a communications/procedure role and does not receive direct hidden spacecraft truth.

## First playable session integration

`src/apollo_mission_control/pc2_session.py` now provides the first authoritative playable-session core.

The prototype currently supports:

- one authoritative mission state;
- synchronized mission GET;
- unique logical station assignment;
- station-scoped player views;
- chronological application of the historical PC+2 fixture events;
- controller readiness-report events;
- explicit FLIGHT GO/NO-GO decision gating;
- FLIGHT-approved CAPCOM queue items;
- explicit CAPCOM transmission events;
- pause/resume;
- chronological audit logging.

### Important gameplay correction

The older deterministic nominal model automatically sets `flight_go=True` when the historical final-poll timestamp is reached. That remains useful for nominal validation, but it is not acceptable gameplay behavior.

The new session layer intercepts the approximately **79:17 GET** final poll and stops progression at final readiness. The assigned FLIGHT player must explicitly record GO before the session can advance toward P40. A NO-GO leaves the session blocked at the readiness gate.

This preserves the researched operating principle:

`station observations/reports → FLIGHT decision → CAPCOM crew-facing transmission`

rather than:

`hidden nominal simulation state → automatic GO`.

## Remaining bounded historical gaps

The singular PC+2 150-psi ground “engine inlet pressure” rule remains intentionally `NOT_EVALUABLE`: separate LM-7 fuel (`GQ3611P`) and oxidizer (`GQ4111P`) interface-pressure measurements are known, but the historical ground selection/aggregation rule has not been established.

The onboard **77-percent thrust-monitor** criterion also remains `NOT_EVALUABLE`; primary sources confirm the rule but do not yet identify the exact percent-thrust crew display/signal.

Exact console layouts, field coordinates, display-selection behavior, several routing/cadence details, detailed DPS transients, and a post-burn FIDO trajectory propagator remain unresolved where they do not yet affect a required player decision.

## Immediate priority

The project has now crossed the planned research-to-integration transition.

Next work is **not another station-display pass**. The current priorities are:

1. add a serializable session/player snapshot suitable for a future web/mobile client;
2. surface readiness reports directly in the FLIGHT player view;
3. surface pending/transmitted queue items in the CAPCOM view;
4. add a deterministic scripted multi-station nominal playthrough through the session layer;
5. then choose and implement the thin web/session transport and mobile presentation shell.

Further historical/subsystem research should be opened only when integration exposes a concrete player-information, decision, or validation gap.

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
