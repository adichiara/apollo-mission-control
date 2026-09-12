# Apollo Mission Control

A cooperative, historically grounded simulation of Apollo-era Mission Control.

Players sit together as flight controllers. Each player uses a phone as the display/interface for a controller station and uses printed station documentation such as flight rules and procedures. A central server maintains the live mission simulation.

## Project standard

This project is **research first**. Apollo operations, terminology, displays, roles, procedures, telemetry, mission timelines, failure behavior, and simulator scenarios are to be implemented from historical documentation wherever documentation exists.

If a required detail is not documented or has not yet been found, it is recorded as unresolved. It is not silently invented.

See:

- [Project principles](docs/PROJECT_PRINCIPLES.md)
- [Roadmap](docs/ROADMAP.md)
- [Simulation architecture](docs/SIMULATION_ARCHITECTURE.md)
- [Flight-control organization baseline](docs/FLIGHT_CONTROL_ORGANIZATION.md)
- [Display-system baseline](docs/DISPLAY_SYSTEM_BASELINE.md)
- [Display reconstruction status](docs/DISPLAY_RECONSTRUCTION_STATUS.md)
- [Controller information workflow](docs/CONTROLLER_INFORMATION_WORKFLOW.md)
- [Physical document workflow](docs/PHYSICAL_DOCUMENT_WORKFLOW.md)
- [Voice communications baseline](docs/VOICE_COMMUNICATIONS_BASELINE.md)
- [Apollo 13 station baseline](docs/APOLLO13_STATION_BASELINE.md)
- [Station research status](docs/STATION_RESEARCH_STATUS.md)
- [PC+2 GUIDO/ISS-warning station-status addendum](docs/station-status/2026-09-12_pc2_iss_warning.md)
- [Apollo 13 EECOM station specification](docs/stations/APOLLO13_EECOM.md)
- [Apollo 13 GNC station specification](docs/stations/APOLLO13_GNC.md)
- [Apollo 13 CONTROL station specification](docs/stations/APOLLO13_CONTROL.md)
- [Apollo 13 TELMU station specification](docs/stations/APOLLO13_TELMU.md)
- [Mission profile model](docs/MISSION_PROFILE_MODEL.md)
- [Simulation scenario research](docs/SIMULATION_SCENARIO_RESEARCH.md)
- [Simulation validation strategy](docs/SIMULATION_VALIDATION.md)
- [Decisions](docs/DECISIONS.md)
- [Open questions](docs/OPEN_QUESTIONS.md)
- [Progress log](docs/PROGRESS.md)
- [Current progress continuation — PC+2 product projection and rules](docs/progress/2026-09-12_pc2_product_projection_and_rules.md)
- [Research resources](resources/README.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

Research has progressed into the first implementation-oriented vertical slice: **Apollo 13 PC+2 preparation and execution**. The framework-neutral Python prototype includes the nominal event model, station-specific controller-product projections, and a partial source-backed shutdown-rule audit layer. The first deferred positive rule path is now modeled from primary evidence: a distinct ISS warning observation combined with a program alarm can trigger the documented conjunctive PC+2 criterion without automatically commanding a shutdown. Required-but-unmodeled analog observations remain explicit implementation gaps rather than fabricated telemetry or assumed-safe values.

The project still does **not** claim full spacecraft physics, RTCC dynamics, exact historical CRT timing, exact Apollo 13 LM-7 ISS-warning telemetry-word/CRT placement, or complete rule-path coverage.

## Apollo 13 station specifications

Detailed research specifications are being built under `docs/stations/`:

- [EECOM](docs/stations/APOLLO13_EECOM.md)
- [GNC](docs/stations/APOLLO13_GNC.md)
- [GUIDO](docs/stations/APOLLO13_GUIDO.md)
- [TELMU](docs/stations/APOLLO13_TELMU.md)
- [CONTROL](docs/stations/APOLLO13_CONTROL.md)
- [INCO](docs/stations/APOLLO13_INCO.md)
- [FIDO](docs/stations/APOLLO13_FIDO.md)
- [RETRO](docs/stations/APOLLO13_RETRO.md)
