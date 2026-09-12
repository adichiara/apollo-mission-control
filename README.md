# Apollo Mission Control

A cooperative, historically grounded simulation of Apollo-era Mission Control.

Players sit together as flight controllers. Each player uses a phone as the display/interface for a controller station and uses printed station documentation such as flight rules and procedures. A central server maintains the live mission simulation.

## Project standard

This project is **research first**. Apollo operations, terminology, displays, roles, procedures, telemetry, mission timelines, failure behavior, and simulator scenarios are implemented from historical documentation wherever documentation exists.

If a required detail is not documented or has not yet been found, it is recorded as unresolved. It is not silently invented.

See:

- [Project principles](docs/PROJECT_PRINCIPLES.md)
- [Roadmap](docs/ROADMAP.md)
- [Ground-product integrity roadmap addendum](docs/roadmap/2026-09-12_ground_product_integrity.md)
- [Simulation architecture](docs/SIMULATION_ARCHITECTURE.md)
- [Flight-control organization baseline](docs/FLIGHT_CONTROL_ORGANIZATION.md)
- [Display-system baseline](docs/DISPLAY_SYSTEM_BASELINE.md)
- [Display reconstruction status](docs/DISPLAY_RECONSTRUCTION_STATUS.md)
- [Controller information workflow](docs/CONTROLLER_INFORMATION_WORKFLOW.md)
- [Voice communications baseline](docs/VOICE_COMMUNICATIONS_BASELINE.md)
- [Apollo 13 station baseline](docs/APOLLO13_STATION_BASELINE.md)
- [Station research status](docs/STATION_RESEARCH_STATUS.md)
- [PC+2 restart station-status addendum](docs/station-status/2026-09-12_pc2_restart_branch.md)
- [Mission profile model](docs/MISSION_PROFILE_MODEL.md)
- [Simulation scenario research](docs/SIMULATION_SCENARIO_RESEARCH.md)
- [Simulation validation strategy](docs/SIMULATION_VALIDATION.md)
- [Decisions](docs/DECISIONS.md)
- [Open questions](docs/OPEN_QUESTIONS.md)
- [Progress log](docs/PROGRESS.md)
- [PC+2 restart progress](docs/progress/2026-09-12_pc2_restart_branch.md)
- [Research resources](resources/README.md)
- [PC+2 implementation source catalog](resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md)
- [PC+2 restart source catalog](resources/source-catalog/PC2_RESTART_SOURCES.md)
- [Apollo 13 ground-product integrity sources](resources/source-catalog/APOLLO13_GROUND_PRODUCT_INTEGRITY_SOURCES.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

The first implementation-oriented vertical slice is **Apollo 13 PC+2 preparation and execution**.

The framework-neutral Python prototype includes source-backed nominal event/state progression, station-specific product projections, partial shutdown-rule evaluation, narrow source-bounded scenario injections, controller/crew action and communication layers, the inverter contingency loop, integrated attitude-error/rate monitoring, explicit observation-age semantics, hidden ground-product integrity, and explicit controller product-rejection events.

### Premature shutdown / restart branch

The latest PC+2 pass implements the documented distinction between a **rule-caused shutdown** and an **unexplained premature DPS stop**.

Primary mission documentation states that if an early shutdown occurred for a reason other than the listed PC+2 shutdown criteria, the engine was to be restarted. The contemporaneous crew read-up gives the sequence as flashing Noun 97 → PRO → manual ullage → Engine Start push → Descent Engine Command Override on.

The implementation therefore now:

- evaluates whether an observed premature stop is restart-eligible based on the already-modeled shutdown-rule audit;
- blocks the generic restart branch when a listed shutdown criterion is triggered;
- records the crew restart actions separately from physical engine response;
- does **not** set `engine_running=True` merely because Engine Start or command override was selected;
- keeps the in-burn restart branch distinct from the earlier backup procedure for failure to ignite at TIG;
- does not invent a new FLIGHT-authorization step because the contingency was already passed to and read back by the crew before the maneuver.

### Ground-product integrity

A separate Apollo 13 post-MCC-5 case established that RTCC could incorrectly process AGS body angles while the spacecraft attitude was satisfactory. The reusable data path therefore distinguishes visible product validity/availability, hidden simulator integrity, and explicit controller detection/rejection. Hidden integrity never auto-diagnoses a product for the player.

### Remaining bounded gaps

The singular PC+2 150-psi ground “engine inlet pressure” rule remains intentionally `NOT_EVALUABLE`: the project knows the separate LM-7 fuel (`GQ3611P`) and oxidizer (`GQ4111P`) interface-pressure measurements but has not found enough primary evidence to choose a historical ground selection/aggregation rule.

The onboard **77-percent thrust-monitor** criterion also remains `NOT_EVALUABLE`; primary sources confirm the rule but do not yet identify the exact percent-thrust crew display/signal.

For the **attitude-error / attitude-rate** criteria, the project preserves the primary-source discrepancy between the contemporaneous crew-facing read-up and the postflight wording. The operational implementation follows the rule actually transmitted and confirmed by the crew, while the exact duration of “startup transient” remains unresolved and is not inferred from throttle timing.

The project does **not** yet claim full spacecraft physics, RTCC dynamics, exact historical CRT timing, complete Apollo 13 telemetry/display routing, a generic historical stale-data timeout, detailed DPS restart transients, or historically reconstructed SimSup malfunction-command syntax.

The next implementation target is the first **ground-only shutdown callout → crew action** path. Fuel/oxidizer ΔP >25 psi is the strongest candidate because the PC+2 rule explicitly made it a ground callout only and the corresponding ground-derived CONTROL product is already modeled.

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
