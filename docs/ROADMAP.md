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
- `075_pc2_telmu_player_presentation_boundary.md`
- `076_pc2_fido_retro_player_presentation_boundary.md`
- `077_pc2_inco_player_presentation_boundary.md`
- `078_pc2_flight_capcom_player_presentation_boundary.md`
- `079_pc2_first_playable_session_boundary.md`

Deliverables:

- [x] mission/profile selected
- [x] mission interval selected
- [x] nominal start frozen at 77:55 GET
- [x] minimum initialization defined
- [x] nominal event timeline through immediate power-down
- [x] core scenario-specific primary-source package
- [x] minimum first-slice player-facing station set
- [ ] low-player-count station aggregation

## Phase 3 — Display and console reconstruction

**Goal:** reproduce controller information presentation where source evidence permits it.

**Status:** **minimum PC+2 first-slice presentation checkpoint complete**

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
- [x] first-pass player-facing **GUIDO** presentation implemented from controller-visible PC+2 products
- [x] first-pass player-facing **TELMU** presentation implemented from PC+2 power/configuration and inverter-contingency products
- [x] documented 38–40 A burn-configuration load explicitly rendered as a reference value, not fabricated live current telemetry
- [x] first-pass player-facing **FIDO/RETRO** presentation implemented from the final maneuver PAD, return-plan monitor PAD, and ground-solution status
- [x] final PC+2 target/return products kept distinct from earlier preliminary alternatives
- [x] deferred RTCC Cartesian state and post-burn propagated trajectory omitted rather than fabricated
- [x] first-pass player-facing **INCO** presentation implemented from separate link-quality, voice, telemetry, ranging, and uplink products
- [x] first-pass player-facing **FLIGHT** decision view implemented without an omniscient subsystem-health dashboard
- [x] first-pass player-facing **CAPCOM** communications/procedure view implemented without direct hidden subsystem truth
- [ ] determine singular PC+2 150-psi engine-inlet-pressure ground selection logic only if a direct source becomes readily available
- [ ] recover additional MCC/RTCC transforms only when player decisions require them

**Research stop rule:** further display reconstruction is demand-driven by integration/usability/decision requirements. Do not expand CRT archaeology merely for completeness.

## Phase 4 — Authoritative simulation model

**Status:** **nominal event model + controller products + partial rules + failure/action/communication layers + shutdown/restart physical-response/evidence paths + minimum station presentation set + first authoritative session core implemented**

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
- [x] minimum player-facing presentation set implemented for CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, and CAPCOM
- [x] single-process authoritative `PC2Session` owns state, GET, historical event progression, station assignment, station-scoped views, readiness reports, FLIGHT GO gating, CAPCOM handoff, pause/resume, and audit events
- [x] playable session intercepts the historical final-poll fixture event instead of auto-setting FLIGHT GO
- [x] NO-GO holds progression at final readiness; explicit FLIGHT GO clears the gate

### Immediate next work

- [ ] add a serializable **session/player snapshot DTO** suitable for a future web/mobile client
- [ ] surface controller readiness reports directly in the FLIGHT player view
- [ ] surface pending/transmitted CAPCOM queue items in the CAPCOM player view
- [ ] add a deterministic scripted **multi-station nominal playthrough** through the session layer
- [ ] validate station information isolation and audit-event ordering end-to-end
- [ ] then select/implement the thin web/session transport and mobile presentation shell
- [ ] do not create a post-burn FIDO trajectory solution merely to make the screen complete
- [ ] keep `crew_thrust_monitor` `NOT_EVALUABLE` unless a direct LM-7 source identifies the percent-thrust indication
- [ ] keep singular 150-psi inlet-pressure aggregation deferred unless a direct source becomes cheaply available
- [ ] determine minimum trajectory-state representation only when integrated trajectory behavior actually requires it

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
- TELMU 38–40 A burn-configuration figure is a reference/planning value, not live measured current;
- GUIDO residuals are not substituted for a FIDO post-burn propagated trajectory solution;
- INCO communications subchannels are not collapsed into a hidden communications-health verdict;
- FLIGHT GO is a player/controller decision in session play, not a consequence of hidden nominal state;
- CAPCOM queued/transmitted messages do not directly mutate authoritative vehicle state;
- exact player display coordinates/routing are not invented where source coverage is incomplete;
- synthetic boundary-test values/times are labeled non-historical;
- injections, actions, communications, controller decisions, physical responses, controller products, player presentation, and session orchestration remain separate layers.

## Phase 5 — Mission Control data path

**Goal:** preserve spacecraft state → instrumentation/telemetry → communications/ground processing → controller products → controller interpretation → player presentation → session decisions/communications.

Current checkpoint:

- station projections enforce information boundaries for the modeled PC+2 subset;
- source injections alter observations without special-case scenario diagnoses;
- validity/integrity degradation remains independent from observation age;
- controller suspicion/rejection is explicit and never inferred automatically from hidden integrity;
- shutdown/restart actions, physical responses, and controller evidence remain separate;
- all minimum station presentation models consume only controller-visible products and preserve provenance;
- hidden product-integrity annotations do not leak into presentation;
- deferred implementation gaps do not masquerade as telemetry failures;
- session station assignment selects only the assigned station's projection/presentation;
- controller readiness reports and FLIGHT decisions are session events, not spacecraft state;
- FLIGHT→CAPCOM queueing and CAPCOM transmission are separate audit events;
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
- [x] final GO/NO-GO decision is now represented as an explicit playable-session FLIGHT gate
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
- [x] nominal timed scenario events now run inside an authoritative session that can pause at player decision gates
- [ ] documented nonnominal Apollo training case reconstructed only when source detail is sufficient
- [ ] historical SimSup/operator interface deferred

Scenario implementation rule: inject underlying conditions; do not announce diagnoses or set outcomes directly.

## Phase 8 — Multi-player session layer

**Status:** **single-process authoritative prototype implemented; network/web layer pending**

**Goal:** central authoritative server, session/join, station assignment, phone clients, synchronized GET/state, reconnection, and server-controlled scenario state.

Completed first prototype:

- [x] authoritative session state and synchronized GET
- [x] unique player→station assignment
- [x] station-scoped presentation dispatch
- [x] readiness-report events
- [x] explicit FLIGHT GO/NO-GO gate at the historical final poll
- [x] FLIGHT→CAPCOM approved-message queue
- [x] explicit CAPCOM transmission event
- [x] pause/resume
- [x] chronological audit log

Immediate next integration:

- [ ] serializable session/player snapshot DTO
- [ ] readiness reports visible in FLIGHT presentation
- [ ] CAPCOM queue visible in CAPCOM presentation
- [ ] scripted multi-station nominal playthrough
- [ ] framework/transport selection
- [ ] session creation/join endpoint
- [ ] reconnection semantics
- [ ] phone/mobile shell

Role aggregation remains deferred until the seven-station first-slice workflow has been validated.

## Phase 9 — Communications

**Goal:** reproduce enough Flight/discipline/air-ground communication structure to affect controller work.

Established requirements include weak-link effects on PAD/readback, inverter contingency instructions/reports, crew-facing Mission Rules read-up/readback, restart procedure briefing, ground-only ΔP callout, separation of crew reports from physical/telemetry truth, and explicit FLIGHT→CAPCOM handoff.

Exact hypothetical internal voice-loop routing is not asserted without stronger evidence.

## Phase 10 — Post-simulation review

**Goal:** support replay/learning without an in-play score layer.

Potential outputs: objective outcome, commands/decisions, system evolution, rules/procedures, communications timeline, historical comparison.

The session audit log is now the initial implementation substrate for this phase.

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
