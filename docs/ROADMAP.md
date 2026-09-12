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

Core Apollo 13 front-room positions are at B or better, with EECOM at A. Exact display/console reconstruction remains incomplete for many stations but is no longer a prerequisite where missing detail does not affect the selected scenario.

Further historical work is demand-driven by the PC+2 slice or unusually high-value sources.

## Phase 2 — First playable mission/scenario

**Status:** **selected and initialized — Apollo 13 PC+2 preparation/execution**

Selected slice: Apollo 13 PC+2, starting at **77:55:00 GET** and running through immediate post-burn verification/power-down around 79:34–80:00 GET.

Key research chain:

- `048_first_vertical_slice_candidate_assessment.md`
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
- `069_pc2_dps_shutdown_command_and_physical_response.md`
- `070_pc2_dps_shutdown_confirmation_evidence.md`
- `071_pc2_dps_restart_physical_response.md`
- `072_pc2_restart_controller_evidence.md`
- `073_pc2_control_player_presentation_boundary.md`
- `074_pc2_guido_player_presentation_boundary.md`

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
- [x] LM-7-family `GQ6510P` established as DPS thrust-chamber-pressure measurement; exact Apollo 13 ground/display conversion remains unresolved
- [x] LM-7-family `GQ3611P` and `GQ4111P` established as separate fuel/oxidizer engine-interface pressure measurements
- [x] PC+2 fuel/oxidizer ΔP established as a distinct ground-only CONTROL rule product; exact computation/display routing remains unresolved
- [x] onboard 77-percent thrust rule separated from P47, thrust-to-weight indication, and ground chamber pressure
- [x] attitude-error and angular-rate observations established as separate PC+2 CONTROL monitoring families
- [x] observation/sample time separated from later display/evaluation time; no unsupported generic stale threshold applied
- [x] minimum shutdown/restart evidence channels bounded without invented binary confirmation thresholds
- [x] first-pass player-facing **CONTROL** presentation implemented as an explicitly labeled project rendering
- [x] Apollo 13 MSK 1137 `TCP` percent semantics kept distinct from modeled `GQ6510P` psi; no unsupported conversion/alias
- [x] deferred CONTROL fields omitted rather than presented as historical telemetry failures
- [x] first-pass player-facing **GUIDO** presentation implemented from controller-visible PC+2 products
- [x] GUIDO presentation preserves exact Apollo terminology only where semantics are supportable and labels assessment/load products as project renderings rather than asserted CRT literals
- [x] deferred GUIDO `vg_remaining` / `dv_gained` fields remain implementation gaps rather than simulated telemetry failures
- [ ] build first-pass **TELMU** player presentation around PC+2 power/configuration and inverter contingency products
- [ ] determine singular PC+2 150-psi engine-inlet-pressure ground selection logic only if a direct source becomes readily available
- [ ] map remaining required station products into first-pass player screens, using exact Apollo formats where available and explicitly labeled project renderings elsewhere
- [ ] recover additional MCC/RTCC transforms only when player decisions require them

Non-PC+2 display reconstruction remains deferred.

## Phase 4 — Authoritative simulation model

**Status:** **nominal event model + controller products + partial rules + failure/action/communication layers + shutdown/restart physical-response/evidence paths + CONTROL/GUIDO presentation models implemented**

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
- [x] timed scenario-injection architecture and source-bounded pressure/ΔP boundary tests
- [x] fuel/oxidizer ΔP modeled as an optional ground-derived observation
- [x] inverter contingency communication/action/re-observation loop
- [x] attitude-error/rate observations integrated into common CONTROL rule path
- [x] observation age preserved without invented stale timeout
- [x] wrong-but-present ground-product integrity separated from player-visible validity
- [x] explicit controller product-rejection decision events
- [x] premature DPS shutdown restart eligibility separated from rule-caused shutdown
- [x] PC+2 restart procedure represented as PRO → manual ullage → Engine Start → command override
- [x] restart actions separated from successful physical re-ignition
- [x] physical DPS restart response modeled without invented restart timing/thrust trace
- [x] fresh post-restart chamber pressure reuses common CONTROL evidence path; no special restart-confirmed flag invented
- [x] ground-only fuel/oxidizer ΔP >25 psi path implemented as CONTROL decision → CAPCOM callout → crew shutdown command
- [x] crew STOP input separated from physical engine-off response
- [x] shutdown evidence keeps crew report and fresh GQ6510P observation distinct from authoritative physical state
- [x] first-pass CONTROL presentation preserves source/provenance/validity and hides internal integrity metadata
- [x] first-pass GUIDO presentation preserves LGC/PGNS source boundaries, project-assessment semantics, and hidden-integrity separation

### Immediate next work

- [ ] implement the **first-pass TELMU player-facing presentation** from the existing PC+2 product projection
- [ ] prioritize burn-configuration power mode/current reference, inverter warning/action state, and post-burn power-down transition
- [ ] use exact Apollo display terminology only where modeled semantics and units match the source evidence
- [ ] do not expose hidden integrity metadata or convert implementation gaps into simulated telemetry failures
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
- no generic stale-data timeout is invented;
- detailed DPS shutdown/restart transient timing remains deferred;
- restart eligibility does not imply restart success;
- crew STOP action does not imply physical shutdown until an explicit vehicle-response event occurs;
- physical response does not automatically fabricate telemetry evidence;
- no chamber-pressure value is treated as a formal binary engine-on/off threshold without direct evidence;
- MSK 1137 `TCP` percent is not aliased to GQ6510P psi without a sourced conversion;
- GUIDO project assessment/load-status products are not claimed as verbatim CRT literals;
- exact player display coordinates/routing are not invented where source coverage is incomplete;
- synthetic boundary-test values/times are labeled non-historical;
- injections, actions, communications, controller decisions, physical responses, controller products, and player presentation remain separate layers.

## Phase 5 — Mission Control data path

**Goal:** preserve spacecraft state → instrumentation/telemetry → communications/ground processing → controller products → controller interpretation → player presentation.

Current checkpoint:

- station projections enforce information boundaries for the modeled PC+2 subset;
- source injections alter observations without special-case scenario diagnoses;
- validity/integrity degradation remains independent from observation age;
- controller suspicion/rejection is explicit and never inferred automatically from hidden integrity;
- shutdown/restart actions, physical responses, and controller evidence remain separate;
- CONTROL and GUIDO presentation models consume only controller-visible products and preserve provenance;
- hidden product-integrity annotations do not leak into presentation;
- deferred implementation gaps do not masquerade as telemetry failures;
- network transport and exact display cadence remain future work where documented.

## Phase 6 — Procedures and flight rules

**Goal:** make controller documentation operational.

PC+2 checkpoint:

- [x] rule ownership and core shutdown criteria mapped
- [x] conjunctive ISS-warning/program-alarm criterion evaluable
- [x] ground chamber-pressure criterion evaluable when a numerical source observation is supplied
- [x] fuel/oxidizer ΔP >25 psi criterion evaluable from an explicit ground-derived product
- [x] ground-only ΔP callout propagated to crew shutdown-command action
- [x] contemporary LM manual shutdown control identified as either crew STOP pushbutton
- [x] minimum shutdown/restart evidence represented without invented binary thresholds
- [x] inverter-warning-after-switch criterion requires a distinct post-switch observation
- [x] premature-shutdown restart rule and contemporaneous restart sequence recovered
- [x] 77-percent onboard thrust criterion deliberately remains `NOT_EVALUABLE`
- [x] attitude-error/rate thresholds and operational exception allocation resolved from contemporaneous read-up/readback
- [ ] exact startup-transient time boundary remains unresolved
- [ ] exact alternate-inverter identity/switch details remain unresolved
- [ ] singular 150-psi ground inlet-pressure rule remains `NOT_EVALUABLE`
- [ ] crew inlet indication remains deferred

## Phase 7 — Simulation scenarios / SimSup

**Goal:** reproduce training/scenario behavior from documented practice where evidence permits it.

Current checkpoint:

- [x] scenario evidence levels defined
- [x] source-condition → dependent-effects architecture established
- [x] timed injection contract implemented for researched source/ground-product state
- [x] operational actions separated from malfunction injections
- [x] procedural communications separated from injections/actions
- [x] controller decisions separated from hidden integrity metadata
- [x] synthetic rule-boundary fixtures distinguished from historical Apollo cases
- [x] inverter contingency loop implemented
- [x] premature-shutdown restart branch modeled without scripting restart success
- [x] ground-only ΔP shutdown callout loop implemented
- [x] command/physical-response/evidence boundaries established for DPS shutdown and restart
- [ ] documented nonnominal Apollo training case reconstructed only when source detail is sufficient
- [ ] historical SimSup/operator interface deferred

Scenario implementation rule: inject underlying conditions; do not announce diagnoses or set outcomes directly.

## Phase 8 — Multi-player session layer

**Goal:** central authoritative server, session/join, station assignment, phone clients, synchronized GET/state, reconnection, and server-controlled scenario state.

Role aggregation remains deferred until station research supports it.

## Phase 9 — Communications

**Goal:** reproduce enough Flight/discipline/air-ground communication structure to affect controller work.

Established requirements include weak-link effects on PAD/readback, inverter contingency instructions/reports, crew-facing Mission Rules read-up/readback, restart procedure briefing, ground-only ΔP callout, and separation of crew reports from physical/telemetry truth.

Exact hypothetical internal voice-loop routing is not asserted without stronger evidence.

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
