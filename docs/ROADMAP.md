# Roadmap

This roadmap deliberately separates historical reconstruction from software simplification.

## Phase 0 — Foundation and provenance

**Goal:** establish project rules and a research trail before simulation code.

- [x] Create project/repository baseline
- [x] Record authenticity and simplification policy
- [x] Create source catalog
- [x] Create research-note structure
- [x] Record initial high-level simulation architecture
- [ ] Decide how primary-source files themselves will be archived in-repo versus linked externally
- [ ] Define source citation format for implementation/code comments

## Phase 1 — Reconstruct Apollo Mission Control

**Status:** **research-sufficient to proceed; not historically exhaustive**

Core Apollo 13 front-room positions are at B or better, with EECOM at A. Exact display/console reconstruction remains incomplete for many stations but is no longer a prerequisite when missing detail does not affect the selected scenario.

Further historical work is demand-driven by the PC+2 slice or unusually high-value sources.

## Phase 2 — First playable mission/scenario

**Status:** **selected and initialized — Apollo 13 PC+2 preparation/execution**

Selected slice: Apollo 13 PC+2, starting at **77:55:00 GET** and running through immediate post-burn verification/power-down around 79:34–80:00 GET.

Key research chain:

- `resources/research/048_first_vertical_slice_candidate_assessment.md`
- `049_pc2_controller_action_and_rule_matrix.md`
- `050_pc2_initialization_and_nominal_validation.md`
- `051_pc2_ullage_and_throttle_profile.md`
- `052_pc2_controller_product_projection.md`
- `053_pc2_shutdown_rule_evaluation.md`
- `054_pc2_iss_warning_observation_path.md`
- `055_pc2_dps_chamber_pressure_observation_path.md`
- `056_pc2_scenario_injection_architecture.md`
- `057_pc2_dps_inlet_pressure_observation_path.md`
- `058_pc2_fuel_oxidizer_delta_p_observation_path.md`
- `059_pc2_inverter_warning_after_switch.md`
- `060_pc2_inverter_contingency_action_report_loop.md`
- `061_pc2_onboard_thrust_monitor_observation_path.md`
- `062_pc2_attitude_error_rate_shutdown_path.md`
- `063_pc2_attitude_projection_and_rule_integration.md`
- `064_pc2_observation_age_and_freshness.md`
- `065_apollo13_ground_product_integrity_failure.md`
- `066_controller_product_rejection_decision_event.md`
- `067_pc2_premature_shutdown_restart_branch.md`
- `068_pc2_delta_p_ground_callout_shutdown_loop.md`

Deliverables:

- [x] mission/profile selected
- [x] mission interval selected
- [x] nominal start frozen at 77:55 GET
- [x] minimum initialization defined
- [x] nominal event timeline through immediate power-down
- [x] core scenario-specific primary-source package
- [ ] full-fidelity player-position set and later low-player-count aggregation

## Phase 3 — Display and console reconstruction

**Goal:** reproduce controller information presentation where source evidence permits it.

Current PC+2 checkpoint:

- [x] mission-specific MSK 1123/1137 layouts identified and inspected
- [x] LGC/PCM/AEA/AGS/ground-derived source classes separated
- [x] minimum PC+2 product set identified for GUIDO, CONTROL, FIDO/RETRO, TELMU, INCO, FLIGHT, CAPCOM
- [x] products mapped to station-specific projections with validity/source/provenance metadata
- [x] ISS warning established as a distinct onboard warning signal; exact LM-7 telemetry word/CRT placement unresolved
- [x] LM-7-family `GQ6510P` established as DPS thrust-chamber-pressure measurement; exact Apollo 13 ground/display routing unresolved
- [x] LM-7-family `GQ3611P` and `GQ4111P` established as separate fuel/oxidizer engine-interface pressure measurements
- [x] PC+2 fuel/oxidizer ΔP established as a distinct ground-only CONTROL rule product; exact computation/display routing remains unresolved
- [x] inverter caution narrowed to processed AC voltage/frequency quality; exact PC+2 telemetry/display route unresolved
- [x] onboard 77-percent thrust rule separated from both P47 and the thrust-to-weight indicator; exact percent-thrust readout/source remains unresolved
- [x] attitude-error and angular-rate observations established as separate PC+2 CONTROL monitoring families; exact LM-7 PCM/display routing remains unresolved
- [x] observation/sample time separated from later display/evaluation time; no unsupported generic stale threshold applied
- [ ] determine singular PC+2 150-psi engine-inlet-pressure ground selection logic only if a direct source becomes readily available
- [ ] map required products into first-pass station screens, using exact Apollo formats where available and explicitly labeled project renderings elsewhere
- [ ] recover additional MCC/RTCC transforms only when PC+2 station behavior requires them

Non-PC+2 display reconstruction remains deferred.

## Phase 4 — Authoritative simulation model

**Status:** **nominal event model + controller products + partial rules + failure/action/communication layers + restart and ground-callout branches implemented**

Completed:

- [x] initialization contract and parameter dictionary
- [x] LVLH target / PGNS IMU Vg / physical result / residual separation
- [x] nominal validation fixture for TIG, duration, cutoff, Vg, residuals
- [x] nominal state-transition model through post-burn power-down
- [x] framework-neutral Python prototype/tests
- [x] two-jet ullage and minimum/40-percent/maximum commanded throttle phases
- [x] crew throttle reports separated from command/physical event timing
- [x] source/sample/receive/process/display metadata
- [x] station-specific controller-product projection layer
- [x] shutdown-rule evaluator that never creates a generic `burn_abort`
- [x] ISS-warning + program-alarm rule path
- [x] chamber-pressure analog rule path using LM-7-family `GQ6510P`
- [x] generic timed scenario-injection object
- [x] source-bounded chamber-pressure and ΔP boundary tests
- [x] inlet-pressure source-state research bounded without inventing singular aggregation
- [x] fuel/oxidizer ΔP modeled as optional ground-derived observation
- [x] inverter caution, operational switch action, CAPCOM instruction, crew completion report, and distinct post-switch re-observation
- [x] onboard 77-percent thrust-monitor research bounded without fabricating a display/source
- [x] attitude-error/rate conflict researched; implementation follows contemporaneous crew-facing rule while preserving contradictory postflight wording
- [x] attitude-error/rate observations integrated into common CONTROL rule path
- [x] observation age preserved without invented stale timeout
- [x] source-backed wrong-but-present ground-product integrity path
- [x] hidden product integrity separated from player-visible validity/availability
- [x] explicit controller product-rejection decision events
- [x] premature DPS shutdown restart eligibility separated from rule-caused shutdown
- [x] PC+2 restart procedure represented as crew-facing PRO → manual ullage → Engine Start → command override sequence
- [x] restart actions recorded without forcing `engine_running=True`
- [x] failure-to-ignite backup kept distinct from in-burn premature shutdown/restart
- [x] ground-only fuel/oxidizer ΔP >25 psi path implemented as CONTROL decision → CAPCOM callout → crew shutdown command
- [x] crew shutdown command recorded without forcing `engine_running=False`
- [x] exact CONTROL→FLIGHT→CAPCOM approval sequence deliberately left unresolved rather than invented

### Immediate next work

- [ ] research the **crew DPS shutdown command → physical engine shutdown/confirmation** boundary using primary LM/DPS sources; implement only if the response/indication chain is recoverable without deep low-value hardware archaeology
- [ ] if that boundary is not cheaply recoverable, move to the next PC+2 controller decision path rather than infer it
- [ ] keep `crew_thrust_monitor` `NOT_EVALUABLE` unless a direct LM-7 source identifies the percent-thrust indication
- [ ] keep singular 150-psi inlet-pressure aggregation deferred unless a direct source becomes cheaply available
- [ ] add broader failure-propagation tests only where subsystem behavior is source-backed
- [ ] determine minimum trajectory-state representation when propagating trajectory implementation becomes necessary

Important constraints:

- exact RTCC Cartesian state vector at 77:55 remains intentionally unfrozen;
- exact nominal PC+2 chamber-pressure and ΔP traces are not invented;
- singular ground inlet pressure is not synthesized from GQ3611P/GQ4111P;
- fuel/oxidizer ΔP is not computed from those transducers until the historical transformation/sign convention is sourced;
- onboard 77-percent thrust is not aliased to P47, thrust-to-weight indication, or ground chamber pressure;
- no inverter persistence timer or exact alternate-inverter identity is invented;
- startup-transient duration is not inferred from throttle timing;
- conflicting primary wording on attitude-rate/error exception remains recorded;
- exact LM-7 attitude-error/rate PCM assignments and CONTROL CRT fields remain unresolved;
- no generic stale-data timeout is invented;
- detailed DPS restart/transient dynamics remain deferred;
- Noun 97 is retained as a procedural cue without inventing a detailed LGC state machine;
- restart eligibility does not imply restart success;
- exact ΔP ground-call wording, internal voice-loop approval sequence, and cockpit shutdown control are not invented;
- crew shutdown command does not imply physical engine shutdown until a source-backed vehicle-response path is modeled;
- synthetic boundary-test values/times are labeled non-historical;
- scenario injection changes source state/observations, operational actions record crew/controller actions, procedural communications record instructions/reports, and controller decisions record interpretations; none directly scripts diagnosis/outcome.

## Phase 5 — Mission Control data path

**Goal:** preserve spacecraft state → instrumentation/telemetry → communications/ground processing → controller products → controller interpretation.

Current checkpoint:

- station projections enforce information boundaries for the modeled PC+2 subset;
- source injections can alter observations without special-case scenario diagnoses;
- ΔP is intentionally a ground-derived product because its exact LM-measurement transformation remains unresolved;
- crew-visible and ground-only rule paths remain distinct;
- inverter warning is distinct from crew switch action and communications;
- attitude error/rate are separate CONTROL observations;
- source/sample time remains distinct from receive/process/display time;
- validity/integrity degradation is independent from observation age;
- controller suspicion/rejection is explicit and never inferred automatically from hidden integrity;
- premature shutdown restart eligibility is derived from rule state but crew restart actions do not force physical engine response;
- the ground-only ΔP path now crosses CONTROL decision, CAPCOM communication, and crew command without collapsing those layers;
- the next data-path refinement is physical response/confirmation after a crew DPS shutdown command, if source support is economical;
- network transport and exact display cadence remain future work where documented.

## Phase 6 — Procedures and flight rules

**Goal:** make controller documentation operational.

PC+2 checkpoint:

- [x] rule ownership and core shutdown criteria mapped
- [x] conjunctive ISS-warning/program-alarm criterion evaluable
- [x] ground chamber-pressure criterion evaluable when a numerical source observation is supplied
- [x] fuel/oxidizer ΔP >25 psi criterion evaluable when an explicit ground-derived product is supplied
- [x] fuel/oxidizer ΔP ground-only callout propagated to a crew shutdown-command action
- [x] inverter-warning-after-switch criterion evaluable only from a distinct post-switch observation
- [x] bounded inverter contingency action/report order recovered
- [x] 77-percent onboard thrust criterion researched and deliberately left `NOT_EVALUABLE`
- [x] attitude-error/rate thresholds and operational exception allocation resolved for implementation from contemporaneous read-up/readback
- [x] analog-observation freshness question researched; no generic PC+2 time threshold found
- [x] premature-shutdown restart rule recovered and implemented as a separate branch
- [x] contemporaneous restart sequence recovered: flashing Noun 97 → PRO → ullage → Engine Start → Descent Engine Command Override
- [ ] exact startup-transient time boundary remains unresolved
- [ ] exact alternate-inverter identity, switch/circuit-breaker positions, crew member, and dwell time remain unresolved
- [ ] singular 150-psi ground inlet-pressure rule remains `NOT_EVALUABLE`
- [ ] crew inlet indication remains deferred
- [ ] exact cockpit DPS shutdown control sequence for the ground-only ΔP criterion remains unresolved

## Phase 7 — Simulation scenarios / SimSup

**Goal:** reproduce training/scenario behavior from documented practice where evidence permits it.

Current checkpoint:

- [x] scenario evidence levels defined
- [x] source-condition → dependent-effects architecture established
- [x] generic timed injection contract implemented for researched source/ground-product state
- [x] operational actions separated from malfunction injections
- [x] procedural communications separated from injections/actions
- [x] controller decisions separated from hidden integrity metadata
- [x] synthetic rule-boundary fixtures clearly distinguished from historical Apollo cases
- [x] first source-bounded multi-layer contingency loop implemented for inverter warning
- [x] premature-shutdown restart branch modeled without scripting restart success
- [x] first ground-only shutdown callout loop implemented for ΔP >25 psi without scripting physical engine response
- [ ] documented nonnominal Apollo training case reconstructed only when source detail is sufficient
- [ ] historical SimSup/operator interface deferred

Scenario implementation rule: inject underlying conditions; do not announce diagnoses or set outcomes directly.

## Phase 8 — Multi-player session layer

**Goal:** central authoritative server, session/join, station assignment, phone clients, synchronized GET/state, reconnection, and server-controlled scenario state.

Role aggregation remains deferred until station research supports it.

## Phase 9 — Communications

**Goal:** reproduce enough Flight/discipline/air-ground communication structure to affect controller work.

Established requirements:

- weak-but-usable link can interfere with final PAD/readback before improving;
- inverter contingency instructions/reports remain distinct from telemetry and action state;
- crew-facing Mission Rules read-up/readback is operational evidence;
- premature-shutdown restart procedure can be pre-briefed before ignition rather than invented as an emergency ground decision;
- fuel/oxidizer ΔP >25 psi requires a ground-to-crew callout before the crew shutdown response;
- exact hypothetical internal CONTROL→FLIGHT→CAPCOM routing is not asserted without stronger evidence.

## Phase 10 — Post-simulation review

**Goal:** support replay/learning without an in-play score layer.

Potential outputs: objective outcome, commands/decisions, system evolution, rules/procedures, communications timeline, historical comparison.

## Phase 11 — Expansion

After vertical-slice validation:

- Apollo 13 oxygen-tank accident / stabilization
- Apollo 11 powered descent as mission-profile portability test
- additional mission phases/missions
- larger controller complements/backrooms where practical
- documented simulation cases
- deeper ground-system fidelity

## Validation approach

1. component/source fidelity;
2. subsystem closed-loop validation;
3. onboard-computer / RTCC integration;
4. procedure validation;
5. documented boundary/anomaly tests;
6. integrated controller simulation.

See `docs/SIMULATION_VALIDATION.md`.
