# Apollo Mission Control

A cooperative, historically grounded simulation of Apollo-era Mission Control.

Players sit together as flight controllers. Each player uses a phone as the display/interface for a controller station and uses printed station documentation such as flight rules and procedures. A central server maintains the live mission simulation.

## Project standard

This project is **research first**. Apollo operations, terminology, displays, roles, procedures, telemetry, mission timelines, failure behavior, and simulator scenarios are implemented from historical documentation wherever documentation exists.

If a required detail is not documented or has not yet been found, it is recorded as unresolved. It is not silently invented.

See:

- [Project principles](docs/PROJECT_PRINCIPLES.md)
- [Roadmap](docs/ROADMAP.md)
- [Simulation architecture](docs/SIMULATION_ARCHITECTURE.md)
- [Flight-control organization baseline](docs/FLIGHT_CONTROL_ORGANIZATION.md)
- [Display-system baseline](docs/DISPLAY_SYSTEM_BASELINE.md)
- [Display reconstruction status](docs/DISPLAY_RECONSTRUCTION_STATUS.md)
- [Controller information workflow](docs/CONTROLLER_INFORMATION_WORKFLOW.md)
- [Voice communications baseline](docs/VOICE_COMMUNICATIONS_BASELINE.md)
- [Apollo 13 station baseline](docs/APOLLO13_STATION_BASELINE.md)
- [Station research status](docs/STATION_RESEARCH_STATUS.md)
- [PC+2 GUIDO/ISS-warning station-status addendum](docs/station-status/2026-09-12_pc2_iss_warning.md)
- [PC+2 CONTROL/chamber-pressure station-status addendum](docs/station-status/2026-09-12_pc2_dps_chamber_pressure.md)
- [PC+2 scenario-injection station-status addendum](docs/station-status/2026-09-12_pc2_scenario_injection.md)
- [Mission profile model](docs/MISSION_PROFILE_MODEL.md)
- [Simulation scenario research](docs/SIMULATION_SCENARIO_RESEARCH.md)
- [Simulation validation strategy](docs/SIMULATION_VALIDATION.md)
- [Decisions](docs/DECISIONS.md)
- [Open questions](docs/OPEN_QUESTIONS.md)
- [Progress log](docs/PROGRESS.md)
- [PC+2 product/rule progress continuation](docs/progress/2026-09-12_pc2_product_projection_and_rules.md)
- [PC+2 scenario-injection progress continuation](docs/progress/2026-09-12_pc2_scenario_injection.md)
- [Research resources](resources/README.md)
- [PC+2 implementation source catalog](resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

The first implementation-oriented vertical slice is **Apollo 13 PC+2 preparation and execution**.

The framework-neutral Python prototype now includes:

- source-backed nominal event/state progression;
- station-specific controller-product projections;
- partial shutdown-rule evaluation;
- a distinct ISS-warning + program-alarm rule path;
- an LM-7-family `GQ6510P` chamber-pressure observation path for CONTROL;
- a minimal timed scenario-injection layer that changes modeled source state rather than diagnoses/outcomes.

The first timed nonnominal validation path uses a clearly labeled synthetic 80-psi chamber-pressure injection during the burn. That value/time are implementation test data, not an asserted Apollo 13 malfunction. The changed source observation flows through CONTROL and the documented 85-psi ground criterion without automatically stopping the engine or creating an abort state.

The project does **not** yet claim full spacecraft physics, RTCC dynamics, exact historical CRT timing, complete Apollo 13 telemetry/display routing, or historically reconstructed SimSup malfunction-command syntax.

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
