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
- [PC+2 CONTROL/inlet-pressure station-status addendum](docs/station-status/2026-09-12_pc2_inlet_pressure.md)
- [PC+2 CONTROL/delta-P station-status addendum](docs/station-status/2026-09-12_pc2_delta_p.md)
- [PC+2 TELMU/CONTROL/CAPCOM inverter-warning addendum](docs/station-status/2026-09-12_pc2_inverter_warning.md)
- [PC+2 CONTROL/CAPCOM thrust-monitor addendum](docs/station-status/2026-09-12_pc2_thrust_monitor.md)
- [PC+2 CONTROL/GUIDO/CAPCOM attitude-monitoring addendum](docs/station-status/2026-09-12_pc2_attitude_monitoring.md)
- [PC+2 attitude-integration station-status addendum](docs/station-status/2026-09-12_pc2_attitude_integration.md)
- [Mission profile model](docs/MISSION_PROFILE_MODEL.md)
- [Simulation scenario research](docs/SIMULATION_SCENARIO_RESEARCH.md)
- [Simulation validation strategy](docs/SIMULATION_VALIDATION.md)
- [Decisions](docs/DECISIONS.md)
- [Open questions](docs/OPEN_QUESTIONS.md)
- [Progress log](docs/PROGRESS.md)
- [PC+2 product/rule progress continuation](docs/progress/2026-09-12_pc2_product_projection_and_rules.md)
- [PC+2 scenario-injection progress continuation](docs/progress/2026-09-12_pc2_scenario_injection.md)
- [PC+2 inlet-pressure progress continuation](docs/progress/2026-09-12_pc2_inlet_pressure.md)
- [PC+2 delta-P/inverter progress continuation](docs/progress/2026-09-12_pc2_delta_p_and_inverter.md)
- [PC+2 inverter action/report loop progress](docs/progress/2026-09-12_pc2_inverter_action_report_loop.md)
- [PC+2 thrust-monitor research progress](docs/progress/2026-09-12_pc2_thrust_monitor_research.md)
- [PC+2 attitude-monitoring progress](docs/progress/2026-09-12_pc2_attitude_monitoring.md)
- [PC+2 attitude-integration progress](docs/progress/2026-09-12_pc2_attitude_integration.md)
- [Research resources](resources/README.md)
- [PC+2 implementation source catalog](resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md)
- [PC+2 inlet-pressure source addendum](resources/source-catalog/PC2_INLET_PRESSURE_SOURCES.md)
- [PC+2 inverter-warning source addendum](resources/source-catalog/PC2_INVERTER_WARNING_SOURCES.md)
- [PC+2 thrust-monitor source addendum](resources/source-catalog/PC2_THRUST_MONITOR_SOURCES.md)
- [PC+2 attitude source addendum](resources/source-catalog/PC2_ATTITUDE_SOURCES.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

The first implementation-oriented vertical slice is **Apollo 13 PC+2 preparation and execution**.

The framework-neutral Python prototype now includes:

- source-backed nominal event/state progression;
- station-specific controller-product projections;
- partial shutdown-rule evaluation;
- a distinct ISS-warning + program-alarm rule path;
- an LM-7-family `GQ6510P` chamber-pressure observation path for CONTROL;
- a fuel/oxidizer ΔP ground-product rule path that deliberately does not invent the unresolved LM-to-ground transformation;
- a minimal timed scenario-injection layer that changes modeled source state/observations rather than diagnoses/outcomes;
- a separate operational-action layer for crew/controller actions;
- a minimal procedural-communication layer separating CAPCOM instructions and crew completion reports from telemetry and physical state;
- the first small end-to-end source-bounded contingency loop: inverter warning → CAPCOM instruction → crew switch action → completion report → distinct post-switch warning observation → rule evaluation;
- source-bounded attitude-error/rate observations integrated through the common CONTROL projection into the shutdown-rule audit.

The source-bounded nonnominal validation paths remain deliberately narrow. Synthetic chamber-pressure, differential-pressure, inverter-warning, and attitude/rate observations test documented rule boundaries and information flow but are not asserted Apollo 13 failures.

The singular PC+2 150-psi ground “engine inlet pressure” rule remains intentionally `NOT_EVALUABLE`: the project knows the separate LM-7 fuel (`GQ3611P`) and oxidizer (`GQ4111P`) interface-pressure measurements but has not found enough primary evidence to choose a historical ground selection/aggregation rule.

For the inverter criterion, the mission-specific air-ground rule read-up and crew readback establish the action ordering but not an inverter identity or dwell time. The evaluator requires a **distinct post-switch warning observation**; carrying the original pre-switch warning through the switch action is not enough. The implementation does not invent an alternate-inverter number, switch/circuit-breaker sequence, or persistence timer.

The onboard **77-percent thrust-monitor** criterion has been researched and deliberately remains `NOT_EVALUABLE`. Primary sources confirm the rule but do not yet identify the exact percent-thrust crew display/signal. The project does not map it to LGC P47 merely because P47 is named “Thrust Monitor,” does not convert the LM thrust-to-weight indicator into percent thrust, and does not alias the crew indication to the ground `GQ6510P` chamber-pressure product.

For the **attitude-error / attitude-rate** criteria, the project preserves a primary-source discrepancy explicitly. The postflight Mission Operations Report and Apollo 13 Review Board appendices place the startup-transient exception on attitude rate, while CAPCOM's contemporaneous read-up and Fred Haise's readback place it on attitude error. The operational implementation follows the rule actually transmitted to and confirmed by the crew: ±10° attitude error except for startup transient, and ±10°/s rate without a stated exception. The exact duration of “startup transient” remains unresolved and is not inferred from throttle timing. CONTROL's postflight report supplies nominal validation bounds of approximately 7° maximum roll error and rates below 1°/s.

The project does **not** yet claim full spacecraft physics, RTCC dynamics, exact historical CRT timing, complete Apollo 13 telemetry/display routing, or historically reconstructed SimSup malfunction-command syntax.

The next implementation target is **observation age/freshness**. Primary-source research will first check whether PC+2 rules or procedures define an explicit freshness/confirmation requirement for analog shutdown observations. If no such requirement is found, the simulator will preserve observation timestamps/age without inventing a historical stale threshold.

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
