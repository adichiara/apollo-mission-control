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
- [PC+2 DPS restart-response station-status addendum](docs/station-status/2026-09-12_pc2_dps_restart_response.md)
- [Mission profile model](docs/MISSION_PROFILE_MODEL.md)
- [Simulation scenario research](docs/SIMULATION_SCENARIO_RESEARCH.md)
- [Simulation validation strategy](docs/SIMULATION_VALIDATION.md)
- [Decisions](docs/DECISIONS.md)
- [Open questions](docs/OPEN_QUESTIONS.md)
- [Progress log](docs/PROGRESS.md)
- [PC+2 DPS restart-response progress](docs/progress/2026-09-12_pc2_dps_restart_response.md)
- [Research resources](resources/README.md)
- [PC+2 implementation source catalog](resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md)
- [PC+2 restart source catalog](resources/source-catalog/PC2_RESTART_SOURCES.md)
- [PC+2 DPS restart-response source catalog](resources/source-catalog/PC2_DPS_RESTART_RESPONSE_SOURCES.md)
- [PC+2 ΔP callout source catalog](resources/source-catalog/PC2_DELTA_P_CALLOUT_SOURCES.md)
- [PC+2 DPS shutdown-response source catalog](resources/source-catalog/PC2_DPS_SHUTDOWN_RESPONSE_SOURCES.md)
- [PC+2 DPS shutdown-confirmation source catalog](resources/source-catalog/PC2_DPS_SHUTDOWN_CONFIRMATION_SOURCES.md)
- [Apollo 13 ground-product integrity sources](resources/source-catalog/APOLLO13_GROUND_PRODUCT_INTEGRITY_SOURCES.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

The first implementation-oriented vertical slice is **Apollo 13 PC+2 preparation and execution**.

The framework-neutral Python prototype includes source-backed nominal event/state progression, station-specific product projections, partial shutdown-rule evaluation, narrow source-bounded scenario injections, controller/crew action and communication layers, the inverter contingency loop, integrated attitude-error/rate monitoring, explicit observation-age semantics, hidden ground-product integrity, explicit controller product-rejection events, the premature-shutdown restart branch, the ground-only ΔP shutdown branch through physical DPS engine-off response and controller-observable evidence channels, and a separate successful DPS restart physical-response event.

### Premature shutdown / physical restart response

The PC+2 restart path now preserves four separate concepts:

- restart eligibility;
- crew execution of PRO / manual ullage / Engine Start / Descent Engine Command Override;
- actual physical engine restart;
- later controller-observable confirmation.

Contemporary LM subsystem documentation supports the physical engine-on chain: engine-on command → pilot valves open → propellant shutoff valves open → propellant flow/combustion. The physical-response helper therefore may set `engine_running=True` only after a `RESTART_ELIGIBLE` classification and completion of the modeled restart actions.

It deliberately does **not** invent an LM-7 restart delay, restart thrust setting, chamber-pressure rise curve, restart success probability, or automatic ground confirmation. The crew commands alone still do not start the engine.

### DPS shutdown confirmation evidence

The minimum Mission Control evidence after DPS shutdown remains bounded without inventing an `ENGINE OFF` telemetry flag. The model keeps independent crew-report and fresh post-command `GQ6510P` chamber-pressure channels and does not convert any pressure value into an authoritative binary engine-off threshold.

### Ground-only ΔP shutdown callout

Fuel/oxidizer differential pressure greater than **25 psi** is represented as a PC+2 ground-only shutdown criterion requiring a ground callout before crew action. Exactly 25 psi remains clear; synthetic values above the threshold are labeled non-historical test fixtures.

### Ground-product integrity

A separate Apollo 13 post-MCC-5 case established that RTCC could incorrectly process AGS body angles while spacecraft attitude was satisfactory. The reusable data path therefore distinguishes visible product validity/availability, hidden simulator integrity, and explicit controller detection/rejection. Hidden integrity never auto-diagnoses a product for the player.

### Remaining bounded gaps

The singular PC+2 150-psi ground “engine inlet pressure” rule remains intentionally `NOT_EVALUABLE`: separate LM-7 fuel (`GQ3611P`) and oxidizer (`GQ4111P`) interface-pressure measurements are known, but the historical ground selection/aggregation rule has not been established.

The onboard **77-percent thrust-monitor** criterion also remains `NOT_EVALUABLE`; primary sources confirm the rule but do not yet identify the exact percent-thrust crew display/signal.

For the **attitude-error / attitude-rate** criteria, the project preserves the primary-source discrepancy between the contemporaneous crew-facing read-up and postflight wording. The operational implementation follows the rule actually transmitted and confirmed by the crew, while the exact duration of “startup transient” remains unresolved.

The project does **not** yet claim full spacecraft physics, RTCC dynamics, exact historical CRT timing, complete Apollo 13 telemetry/display routing, a generic historical stale-data timeout, detailed DPS restart/shutdown transients, or historically reconstructed SimSup malfunction-command syntax.

The next implementation target is the minimum source-backed **controller-observable evidence of successful restart**. Existing chamber-pressure paths may be reused where justified, but no restart-specific pressure threshold or crew report will be invented. If a mission-specific confirmation rule cannot be recovered economically, the project will preserve fresh GQ6510P as generic propulsion evidence and move to the next player-relevant PC+2 dependency.

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
