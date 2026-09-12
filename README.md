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
- [PC+2 observation-freshness station-status addendum](docs/station-status/2026-09-12_pc2_observation_freshness.md)
- [Mission profile model](docs/MISSION_PROFILE_MODEL.md)
- [Simulation scenario research](docs/SIMULATION_SCENARIO_RESEARCH.md)
- [Simulation validation strategy](docs/SIMULATION_VALIDATION.md)
- [Decisions](docs/DECISIONS.md)
- [Open questions](docs/OPEN_QUESTIONS.md)
- [Progress log](docs/PROGRESS.md)
- [PC+2 observation-freshness progress](docs/progress/2026-09-12_pc2_observation_freshness.md)
- [Research resources](resources/README.md)
- [PC+2 implementation source catalog](resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md)
- [PC+2 observation-age/freshness source catalog](resources/source-catalog/PC2_FRESHNESS_SOURCES.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

The first implementation-oriented vertical slice is **Apollo 13 PC+2 preparation and execution**.

The framework-neutral Python prototype now includes source-backed nominal event/state progression, station-specific product projections, partial shutdown-rule evaluation, narrow source-bounded scenario injections, controller/crew action and communication layers, the inverter contingency loop, and integrated attitude-error/rate monitoring.

### Observation age and freshness

The latest pass researched whether the PC+2 rules or contemporaneous crew-facing procedure define a generic time-based freshness requirement for analog shutdown observations. No such threshold was found in the reviewed mission-specific primary sources.

The implementation therefore now:

- preserves an observation/sample timestamp separately from receive/process/display time;
- keeps an injected chamber-pressure or differential-pressure value tied to the GET at which it was observed rather than re-stamping it as current on every later projection;
- exposes observation age in the shutdown-rule audit;
- does **not** automatically mark a product stale after an invented number of seconds;
- preserves source-specific confirmation rules where they are actually documented, such as requiring a distinct inverter-warning observation after the crew switch action.

This fixes an important information-model problem without claiming more historical specificity than the sources support.

### Remaining bounded gaps

The singular PC+2 150-psi ground “engine inlet pressure” rule remains intentionally `NOT_EVALUABLE`: the project knows the separate LM-7 fuel (`GQ3611P`) and oxidizer (`GQ4111P`) interface-pressure measurements but has not found enough primary evidence to choose a historical ground selection/aggregation rule.

The onboard **77-percent thrust-monitor** criterion also remains `NOT_EVALUABLE`; primary sources confirm the rule but do not yet identify the exact percent-thrust crew display/signal.

For the **attitude-error / attitude-rate** criteria, the project preserves the primary-source discrepancy between the contemporaneous crew-facing read-up and the postflight wording. The operational implementation follows the rule actually transmitted and confirmed by the crew, while the exact duration of “startup transient” remains unresolved and is not inferred from throttle timing.

The project does **not** yet claim full spacecraft physics, RTCC dynamics, exact historical CRT timing, complete Apollo 13 telemetry/display routing, a generic historical stale-data timeout, or historically reconstructed SimSup malfunction-command syntax.

The next implementation target is a **source-backed data-validity degradation path** relevant to PC+2—preferably a documented Apollo 13 example of lost, frozen, questionable, or incorrectly processed data—so validity can be exercised independently from observation age without inventing behavior.

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
