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

## Phase 2 — Select the first playable mission/scenario

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
- [x] inverter caution narrowed to processed AC voltage/frequency quality with LM-5-and-later selection-transient inhibit behavior; exact PC+2 telemetry/display route unresolved
- [ ] determine the exact CONTROL ground product/selection logic behind the singular PC+2 150-psi “engine inlet pressure” criterion only if a direct source becomes readily available
- [ ] map required products into first-pass station screens, using exact Apollo formats where available and explicitly labeled project renderings elsewhere
- [ ] recover additional MCC/RTCC transforms only when PC+2 station behavior requires them

Non-PC+2 display reconstruction remains deferred.

## Phase 4 — Authoritative simulation model

**Status:** **nominal event + product projection + partial rules + source injections + first controller/crew action-report loop implemented**

Completed:

- [x] initialization contract and parameter dictionary
- [x] LVLH target / PGNS IMU Vg / physical result / residual separation
- [x] nominal validation fixture for TIG, duration, cutoff, Vg, residuals
- [x] nominal state-transition model through post-burn power-down
- [x] framework-neutral Python prototype/tests
- [x] two-jet ullage and minimum/40-percent/maximum commanded throttle phases
- [x] crew throttle reports separated from command/physical event timing
- [x] update/sample semantics with explicit source/sample/receive/process/display metadata
- [x] station-specific controller-product projection layer
- [x] shutdown-rule evaluator that never creates a generic `burn_abort`
- [x] ISS-warning + program-alarm rule path
- [x] chamber-pressure analog rule path using LM-7-family `GQ6510P`
- [x] generic timed scenario-injection object
- [x] timed source-bounded chamber-pressure test: synthetic 80 psi flows through CONTROL and the historical 85-psi rule without commanding cutoff/abort
- [x] inlet-pressure source-state research: two LM-7 interface measurements identified, unsupported singular ground aggregation deliberately left unresolved
- [x] fuel/oxidizer ΔP rule path modeled as an optional **ground-derived** observation without inventing a GQ3611P/GQ4111P subtraction or sign convention
- [x] source-bounded ΔP boundary tests defined at 26 psi (triggered) and exactly 25 psi (clear)
- [x] inverter caution and inverter-switch action represented as separate state/event classes
- [x] first generic operational-action object implemented with `switch_lm_inverter`
- [x] CAPCOM instruction and crew completion-report events represented separately from the inverter action and telemetry state
- [x] inverter rule now requires a distinct post-switch warning observation; a pre-switch warning carried through the action is not enough
- [x] first small end-to-end source-bounded decision/action loop implemented: warning → CAPCOM instruction → crew switch → completion report → post-switch warning → rule trigger, with no automatic cutoff/abort

Immediate next work:

- [ ] research the **onboard thrust-monitor observation path for the 77-percent criterion** using primary LM crew/display documentation first; implement only if the indication semantics are defensible
- [ ] if the thrust-monitor path cannot be resolved efficiently, research the attitude/rate criteria and the Mission Operations Report vs crew-readback startup-transient wording conflict
- [ ] keep singular 150-psi inlet-pressure aggregation deferred unless a direct CONTROL/procedure/display source becomes cheaply available
- [ ] add broader failure-propagation tests only where subsystem behavior is source-backed
- [ ] determine minimum trajectory-state representation when a propagating trajectory implementation becomes necessary

Important constraints:

- exact RTCC Cartesian state vector at 77:55 remains intentionally unfrozen;
- exact nominal PC+2 chamber-pressure and ΔP traces are not invented;
- singular ground `dps_inlet_pressure_psi` is **not** invented from the two interface-pressure transducers;
- fuel/oxidizer ΔP is not computed from those transducers until the historical ground transformation/sign convention is sourced;
- no inverter persistence timer or exact alternate-inverter identity is invented;
- the surviving LM-7 contingency-checklist catalog record does not by itself establish the missing inverter switch details;
- detailed DPS ramp dynamics remain deferred;
- synthetic boundary-test values/times are labeled non-historical;
- scenario injection changes source state/observations, operational actions record what crew/controllers do, and procedural communications record instructions/reports; none directly sets diagnoses or outcomes.

## Phase 5 — Mission Control data path

**Goal:** preserve spacecraft state → instrumentation/telemetry → communications/ground processing → controller products.

Current checkpoint:

- station projections enforce information boundaries for the modeled PC+2 subset;
- source injections prove that changed observations can flow through CONTROL and the rule evaluator without special-case scenario logic;
- inlet-pressure research exposes a concrete unresolved selection/aggregation problem rather than hiding it behind one generic value;
- ΔP is intentionally represented as a ground-derived product because its exact LM-measurement transformation remains unresolved;
- inverter warning is kept distinct from the crew switch action and from CAPCOM/crew procedural communications;
- inverter rule evaluation now distinguishes pre-switch warning information from a genuinely later post-switch observation;
- stale/missing/invalid behavior, network transport, and exact display cadence remain future work where documented.

## Phase 6 — Procedures and flight rules

**Goal:** make controller documentation operational.

PC+2 checkpoint:

- [x] rule ownership and core shutdown criteria mapped
- [x] conjunctive ISS-warning/program-alarm criterion evaluable
- [x] ground chamber-pressure criterion evaluable when a numerical source observation is supplied
- [x] fuel and oxidizer LM-7 engine-interface pressure measurement identities established
- [x] fuel/oxidizer ΔP >25 psi criterion evaluable when an explicit ground-derived product is supplied
- [x] inverter-warning-after-switch criterion evaluable only from a distinct post-switch observation
- [x] bounded inverter contingency action/report order recovered from the mission rule read-up and crew readback
- [ ] exact alternate-inverter identity, switch/circuit-breaker positions, crew member, and any dwell time remain unresolved and are not invented
- [ ] singular 150-psi ground inlet-pressure rule remains `NOT_EVALUABLE` until selection/aggregation semantics are sourced
- [ ] crew analog thrust/inlet indications and attitude/rate criteria remain deferred
- [ ] startup-transient wording conflict remains unresolved rather than silently normalized

## Phase 7 — Simulation scenarios / SimSup

**Goal:** reproduce training/scenario behavior from documented practice where evidence permits it.

Current checkpoint:

- [x] scenario evidence levels defined
- [x] primary-source simulator evidence supports source-condition → dependent-effects architecture
- [x] generic timed injection contract implemented for researched source/ground-product state
- [x] operational actions structurally separated from malfunction injections
- [x] procedural communications structurally separated from both injections and actions
- [x] synthetic rule-boundary fixtures clearly distinguished from historical Apollo training cases
- [x] first source-bounded multi-layer contingency loop exercises injection → communication → action → re-observation → rule evaluation without scripting outcome
- [ ] documented nonnominal Apollo training case reconstructed only when source detail is sufficient
- [ ] historical SimSup/operator interface deferred

Scenario implementation rule: inject underlying conditions; do not announce diagnoses or set outcomes directly.

## Phase 8 — Multi-player session layer

**Goal:** central authoritative server, session/join, station assignment, phone clients, synchronized GET/state, reconnection, and server-controlled scenario state.

Role aggregation remains deferred until station research supports it.

## Phase 9 — Communications

**Goal:** reproduce enough Flight/discipline/air-ground communication structure to affect controller work.

The PC+2 start already requires a weak-but-usable link that interferes with final PAD/readback before improving after the S-band amplifier change.

The inverter contingency now supplies a second concrete communication requirement: an approved crew-facing procedure instruction and crew completion report must remain distinct from spacecraft telemetry and operational action state.

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
