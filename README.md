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
- [PC+2 DPS shutdown-confirmation station-status addendum](docs/station-status/2026-09-12_pc2_dps_shutdown_confirmation.md)
- [Mission profile model](docs/MISSION_PROFILE_MODEL.md)
- [Gameplay model](docs/GAMEPLAY_MODEL.md) — design proposal, not accepted
- [Simulation scenario research](docs/SIMULATION_SCENARIO_RESEARCH.md)
- [Simulation validation strategy](docs/SIMULATION_VALIDATION.md)
- [Decisions](docs/DECISIONS.md)
- [Open questions](docs/OPEN_QUESTIONS.md)
- [Progress log](docs/PROGRESS.md)
- [PC+2 DPS shutdown-confirmation progress](docs/progress/2026-09-12_pc2_dps_shutdown_confirmation.md)
- [Source mirroring policy](docs/SOURCE_MIRRORING.md) — proposed
- [Research resources](resources/README.md)
- [Primary-source mirror manifest](resources/primary-sources/manifest.json)
- [PC+2 implementation source catalog](resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md)
- [PC+2 restart source catalog](resources/source-catalog/PC2_RESTART_SOURCES.md)
- [PC+2 ΔP callout source catalog](resources/source-catalog/PC2_DELTA_P_CALLOUT_SOURCES.md)
- [PC+2 DPS shutdown-response source catalog](resources/source-catalog/PC2_DPS_SHUTDOWN_RESPONSE_SOURCES.md)
- [PC+2 DPS shutdown-confirmation source catalog](resources/source-catalog/PC2_DPS_SHUTDOWN_CONFIRMATION_SOURCES.md)
- [Apollo 13 ground-product integrity sources](resources/source-catalog/APOLLO13_GROUND_PRODUCT_INTEGRITY_SOURCES.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

The first implementation-oriented vertical slice is **Apollo 13 PC+2 preparation and execution**.

The framework-neutral Python prototype includes source-backed nominal event/state progression, station-specific product projections, partial shutdown-rule evaluation, narrow source-bounded scenario injections, controller/crew action and communication layers, the inverter contingency loop, integrated attitude-error/rate monitoring, explicit observation-age semantics, hidden ground-product integrity, explicit controller product-rejection events, the premature-shutdown restart branch, and the ground-only ΔP shutdown branch through physical DPS engine-off response and controller-observable evidence channels.

### DPS shutdown confirmation evidence

The latest research pass bounded the minimum Mission Control evidence available after DPS shutdown without inventing an `ENGINE OFF` telemetry flag.

Primary mission documentation already establishes thrust chamber pressure as a ground-observed PC+2 rule quantity. Contemporary LM documentation identifies `GQ6510P` as thrust chamber pressure, and Apollo 10 raw DPS data show that measurement responding through shutdown. The Apollo 10 trace is used only for measurement-behavior continuity; its timing and numerical values are not imported into Apollo 13.

The actual Apollo 13 PC+2 voice sequence also includes Lovell reporting **“Shutdown”**, immediately acknowledged by CAPCOM. The implementation therefore keeps two independent controller-observable evidence channels:

- the crew shutdown report;
- a fresh, post-command `GQ6510P` chamber-pressure observation when one is supplied.

The new evidence aggregator can report `NONE`, `CREW_REPORTED`, `GROUND_PRESSURE_OBSERVED`, or `CORROBORATED`. It does **not** convert any particular chamber-pressure value into an authoritative `engine_off_confirmed` state because no reviewed source defines such a threshold.

### Ground-only ΔP shutdown callout

Primary mission documentation states that fuel/oxidizer differential pressure greater than **25 psi** was a PC+2 shutdown criterion and specifically required a **ground callout**. The implementation separates the ground-derived ΔP product, CONTROL assessment, CAPCOM callout, crew STOP action, physical engine response, and later evidence.

Exactly 25 psi remains clear; a synthetic 26 psi case exercises the triggered path. The 26 psi value is a software boundary test, not a historical Apollo 13 measurement.

### DPS shutdown command and physical response

Contemporary LM systems documentation establishes that either crew descent-engine STOP pushbutton can initiate the engine-off command. Engine on/off commands actuate the descent-engine pilot valves, which in turn command closure of the fuel and oxidizer shutoff valves.

The STOP input and vehicle response remain separate events. The physical-response helper does not invent an exact LM-7 STOP-to-zero-thrust delay, chamber-pressure tailoff curve, or fresh telemetry value.

### Premature shutdown / restart branch

A separate implemented branch preserves the documented distinction between a **rule-caused shutdown** and an **unexplained premature DPS stop**. Restart applies only when the early shutdown cause is affirmatively outside the listed shutdown criteria; a ΔP-triggered shutdown therefore does not enter the generic restart branch.

### Ground-product integrity

A separate Apollo 13 post-MCC-5 case established that RTCC could incorrectly process AGS body angles while the spacecraft attitude was satisfactory. The reusable data path therefore distinguishes visible product validity/availability, hidden simulator integrity, and explicit controller detection/rejection. Hidden integrity never auto-diagnoses a product for the player.

### Remaining bounded gaps

The singular PC+2 150-psi ground “engine inlet pressure” rule remains intentionally `NOT_EVALUABLE`: the project knows the separate LM-7 fuel (`GQ3611P`) and oxidizer (`GQ4111P`) interface-pressure measurements but has not found enough primary evidence to choose a historical ground selection/aggregation rule.

The onboard **77-percent thrust-monitor** criterion also remains `NOT_EVALUABLE`; primary sources confirm the rule but do not yet identify the exact percent-thrust crew display/signal.

For the **attitude-error / attitude-rate** criteria, the project preserves the primary-source discrepancy between the contemporaneous crew-facing read-up and the postflight wording. The operational implementation follows the rule actually transmitted and confirmed by the crew, while the exact duration of “startup transient” remains unresolved and is not inferred from throttle timing.

The project does **not** yet claim full spacecraft physics, RTCC dynamics, exact historical CRT timing, complete Apollo 13 telemetry/display routing, a generic historical stale-data timeout, detailed DPS restart/shutdown transients, or historically reconstructed SimSup malfunction-command syntax.

The next implementation target is the **restart command → physical DPS re-ignition response** boundary for an eligible unexplained premature shutdown. The existing PC+2 restart procedure and contemporary LM start-control documentation should be used, while restart timing, pressure buildup, or success must remain unresolved unless directly supported.

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
