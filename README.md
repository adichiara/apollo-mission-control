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
- [PC+2 GUIDO presentation station-status addendum](docs/station-status/2026-09-12_pc2_guido_presentation.md)
- [Mission profile model](docs/MISSION_PROFILE_MODEL.md)
- [Simulation scenario research](docs/SIMULATION_SCENARIO_RESEARCH.md)
- [Simulation validation strategy](docs/SIMULATION_VALIDATION.md)
- [Decisions](docs/DECISIONS.md)
- [Open questions](docs/OPEN_QUESTIONS.md)
- [Progress log](docs/PROGRESS.md)
- [PC+2 CONTROL presentation progress](docs/progress/2026-09-12_pc2_control_presentation.md)
- [PC+2 GUIDO presentation progress](docs/progress/2026-09-12_pc2_guido_presentation.md)
- [Research resources](resources/README.md)
- [PC+2 implementation source catalog](resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md)
- [PC+2 CONTROL presentation source catalog](resources/source-catalog/PC2_CONTROL_PRESENTATION_SOURCES.md)
- [PC+2 GUIDO presentation source catalog](resources/source-catalog/PC2_GUIDO_PRESENTATION_SOURCES.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

The first implementation-oriented vertical slice is **Apollo 13 PC+2 preparation and execution**.

The framework-neutral Python prototype now includes the source-backed nominal event/state model, station-specific product projections, partial shutdown-rule evaluation, scenario injection/action/communication layers, product-integrity handling, premature-shutdown/restart response paths, and first-pass player-facing CONTROL and GUIDO presentation models.

### First-pass CONTROL presentation

The mission-specific Apollo 13 AC Electronics source directly documents **MSK 1123 — LM GUID, CONTROL AND PROP RT** and **MSK 1137 — LM powered-descent/control**. These sources constrain the first player-facing CONTROL display, but the executable screen is deliberately labeled as a **project rendering**, not an exact Apollo CRT transcription.

A critical fidelity boundary is preserved: Apollo 13 MSK 1137 defines `TCP` as chamber pressure in **percent**, while the implemented PC+2 measurement path uses LM-7-family `GQ6510P` thrust-chamber pressure in **psi**. The player view therefore shows the sourced psi quantity as `CHAMBER P`; it does not falsely relabel or convert it to historical `TCP`.

### First-pass GUIDO presentation

The GUIDO rendering uses the same discipline. Apollo 13 MSK 1123/1137 plus the mission-era LUMINARY 1C R-567 data-link documentation directly support program/computer state, alarm/status families, upload verification, and guidance/velocity-change information in the Mission Control data path.

The executable view groups modeled products into:

- LGC / guidance status;
- alignment / load status;
- maneuver / residual.

`PROGRAM` and alarm/status families have direct historical analogues. Other items such as project `LGC` operating state, alignment acceptance, load-verification state, planned Vg, and postburn residual are presented as sourced **project products** where exact CRT literal/routing is incomplete. Hidden integrity metadata is not shown, and deferred `vg_remaining` / `dv_gained` implementation gaps are not portrayed as telemetry failures.

### Remaining bounded gaps

The singular PC+2 150-psi ground “engine inlet pressure” rule remains intentionally `NOT_EVALUABLE`: separate LM-7 fuel (`GQ3611P`) and oxidizer (`GQ4111P`) interface-pressure measurements are known, but the historical ground selection/aggregation rule has not been established.

The onboard **77-percent thrust-monitor** criterion also remains `NOT_EVALUABLE`; primary sources confirm the rule but do not yet identify the exact percent-thrust crew display/signal.

Exact CONTROL/GUIDO CRT selection behavior, field coordinates, refresh cadence, GQ6510P-to-`TCP` conversion, and several field-routing details remain unresolved and are not invented.

The next implementation target is the **first-pass player-facing TELMU presentation**, using the already-modeled PC+2 power configuration, expected-current reference, inverter warning/action state, and post-burn power-down transition. Exact Apollo display terminology/formatting will again be used only where primary evidence supports it.

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
