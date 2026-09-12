# Apollo Mission Control

A cooperative, historically grounded simulation of Apollo-era Mission Control.

Players sit together as flight controllers. Each player uses a phone as the display/interface for a controller station and uses printed station documentation such as flight rules and procedures. A central server maintains the live mission simulation.

## Project standard

This project is **research first**. Apollo operations, terminology, displays, roles, procedures, telemetry, mission timelines, failure behavior, and simulator scenarios are implemented from historical documentation wherever documentation exists.

If a required detail is not documented or has not yet been found, it is recorded as unresolved. It is not silently invented.

See:

- [Project principles](docs/PROJECT_PRINCIPLES.md)
- [Roadmap](docs/ROADMAP.md)
- [PC+2 restart-response roadmap addendum](docs/roadmap/2026-09-12_pc2_restart_response.md)
- [Ground-product integrity roadmap addendum](docs/roadmap/2026-09-12_ground_product_integrity.md)
- [Simulation architecture](docs/SIMULATION_ARCHITECTURE.md)
- [Flight-control organization baseline](docs/FLIGHT_CONTROL_ORGANIZATION.md)
- [Display-system baseline](docs/DISPLAY_SYSTEM_BASELINE.md)
- [Display reconstruction status](docs/DISPLAY_RECONSTRUCTION_STATUS.md)
- [Controller information workflow](docs/CONTROLLER_INFORMATION_WORKFLOW.md)
- [Voice communications baseline](docs/VOICE_COMMUNICATIONS_BASELINE.md)
- [Apollo 13 station baseline](docs/APOLLO13_STATION_BASELINE.md)
- [Station research status](docs/STATION_RESEARCH_STATUS.md)
- [PC+2 CONTROL presentation station-status addendum](docs/station-status/2026-09-12_pc2_control_presentation.md)
- [Mission profile model](docs/MISSION_PROFILE_MODEL.md)
- [Simulation scenario research](docs/SIMULATION_SCENARIO_RESEARCH.md)
- [Simulation validation strategy](docs/SIMULATION_VALIDATION.md)
- [Decisions](docs/DECISIONS.md)
- [Open questions](docs/OPEN_QUESTIONS.md)
- [Progress log](docs/PROGRESS.md)
- [PC+2 CONTROL presentation progress](docs/progress/2026-09-12_pc2_control_presentation.md)
- [Research resources](resources/README.md)
- [PC+2 implementation source catalog](resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md)
- [PC+2 CONTROL presentation source catalog](resources/source-catalog/PC2_CONTROL_PRESENTATION_SOURCES.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

The first implementation-oriented vertical slice is **Apollo 13 PC+2 preparation and execution**.

The framework-neutral Python prototype now includes the source-backed nominal event/state model, station-specific product projections, partial shutdown-rule evaluation, scenario injection/action/communication layers, product-integrity handling, premature-shutdown/restart response paths, and the first player-facing CONTROL presentation model.

### First-pass CONTROL presentation

The mission-specific Apollo 13 AC Electronics source directly documents **MSK 1123 — LM GUID, CONTROL AND PROP RT** and **MSK 1137 — LM powered-descent/control**. These sources now constrain the first player-facing CONTROL display, but the executable screen is deliberately labeled as a **project rendering**, not an exact Apollo CRT transcription.

A critical fidelity boundary is preserved: Apollo 13 MSK 1137 defines `TCP` as chamber pressure in **percent**, while the implemented PC+2 measurement path uses LM-7-family `GQ6510P` thrust-chamber pressure in **psi**. The player view therefore shows the sourced psi quantity as `CHAMBER P`; it does not falsely relabel or convert it to historical `TCP`.

The first CONTROL rendering groups already-modeled information into:

- burn / propulsion;
- attitude / control;
- ullage.

Per-field value, units, validity, source layer, and provenance are retained. Deferred project gaps such as the unresolved singular inlet-pressure product are omitted rather than shown as historical telemetry failures. Hidden integrity metadata is likewise not exposed to the player.

### Remaining bounded gaps

The singular PC+2 150-psi ground “engine inlet pressure” rule remains intentionally `NOT_EVALUABLE`: separate LM-7 fuel (`GQ3611P`) and oxidizer (`GQ4111P`) interface-pressure measurements are known, but the historical ground selection/aggregation rule has not been established.

The onboard **77-percent thrust-monitor** criterion also remains `NOT_EVALUABLE`; primary sources confirm the rule but do not yet identify the exact percent-thrust crew display/signal.

Exact CONTROL CRT selection behavior, field coordinates, GQ6510P-to-`TCP` engineering conversion, refresh cadence, and exact display placement for several modeled PC+2 rule products remain unresolved and are not invented.

The next implementation target is the **first-pass player-facing GUIDO presentation**, applying the same evidence discipline while taking advantage of the stronger LGC/PGNS provenance already recovered for MSK 1123/1137.

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
