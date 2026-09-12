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

**Exit criterion:** every future Apollo-specific implementation can point to a source or an explicitly logged project decision.

## Phase 1 — Reconstruct Apollo Mission Control

**Status:** **research-sufficient to proceed; not historically exhaustive**

**Goal:** understand the actual organization and information flow before assigning game roles.

Research includes MOCR/SSR organization, controller positions, console equipment, voice loops, display/request mechanisms, RTCC/CCATS/MSFN information flow, mission-phase staffing, and handover practice.

**Current interpretation:** Apollo 13 core front-room positions are at B or better, with EECOM at A, and the common telemetry/ground-processing/display architecture is sufficiently established to support a bounded vertical slice. Exact console/display reconstruction remains incomplete for many stations but is no longer a prerequisite when missing detail does not affect the selected scenario.

Research follows the sufficiency rule in `docs/PROJECT_PRINCIPLES.md`: inaccessible or low-impact gaps are logged and deferred rather than allowed to block broader progress.

## Phase 2 — Select the first playable mission/scenario

**Status:** **selected and initialized — Apollo 13 PC+2 preparation/execution**

The reusable technical platform uses the Apollo 13-era MCC as its default research/implementation baseline, with mission-specific historical profiles layered over it.

### Selected vertical slice

**Apollo 13 PC+2 preparation and execution**, starting at **77:55:00 GET** and running through immediate post-burn verification/power-down around 79:34–80:00 GET.

The start is source-driven: communications are weak after AOS and the final P30 LM maneuver PAD begins at 77:55:24, leaving target transfer, final updates, burn power-up, readiness work, and the burn live for players.

Key records:

- `resources/research/048_first_vertical_slice_candidate_assessment.md`
- `resources/research/049_pc2_controller_action_and_rule_matrix.md`
- `resources/research/050_pc2_initialization_and_nominal_validation.md`
- `resources/research/051_pc2_ullage_and_throttle_profile.md`
- `resources/research/052_pc2_controller_product_projection.md`
- `resources/research/053_pc2_shutdown_rule_evaluation.md`
- `resources/research/054_pc2_iss_warning_observation_path.md`
- `resources/research/055_pc2_dps_chamber_pressure_observation_path.md`
- `docs/scenarios/APOLLO13_PC2_PARAMETERS.md`

### Phase 2 deliverables

- [x] selected mission and mission-era profile
- [x] selected mission interval
- [x] freeze nominal scenario start at 77:55:00 GET
- [x] define minimum spacecraft/ground-system initialization
- [x] create source-backed nominal event timeline through immediate post-burn power-down
- [x] assemble core scenario-specific primary-source package
- [ ] identify controller positions required for first full-fidelity multiplayer run and later low-player-count aggregation

## Phase 3 — Display and console reconstruction

**Goal:** reproduce controller information presentation where source evidence permits it.

Research/catalog scope includes operational display formats, typography/geometry, field layout, update rates, display selection, provenance, ground calculations, plots/tables, console controls, and hard-copy products.

### Current research checkpoint — Apollo 13 LM guidance/control displays

- [x] Mission-specific MSK 1123 and 1137 layouts identified and inspected.
- [x] Major LGC, PCM, AEA/AGS, and ground-derived source classes separated.
- [x] AEA Table 2.1-7 telemetry structure and engineering definitions recovered from later contemporary handbook configuration.
- [x] Handbook chronology corrected: Apollo 13 LM-7 versus later searchable LM-10 configuration is explicitly tracked.
- [x] AGS ullage qualification narrowed to a two-second accumulated +X velocity-increment test.
- [x] PC+2-critical information families separated into physical, onboard, telemetry/link, ground-derived, and crew-report layers.
- [x] Minimum historical product set identified for GUIDO, CONTROL, FIDO/RETRO, TELMU, INCO, FLIGHT, and CAPCOM.
- [x] Current modeled products mapped into station-specific projection sets with validity/source/provenance metadata.
- [x] ISS warning established as a distinct onboard warning signal with an instrumentation path; exact Apollo 13 LM-7 telemetry word and GUIDO CRT placement remain unresolved.
- [x] LM-7-family `GQ6510P` established as the DPS thrust-chamber-pressure measurement used by the first analog CONTROL rule path; exact MSK 1137 `TCP` routing/ground conversion remains provisional.
- [ ] Map products into first-pass station screens, using exact Apollo formats where available and explicitly labeled project renderings where presentation evidence is incomplete.
- [ ] Compare Apollo 13 LM-7 Table 2.1-7 directly with later searchable LM-10 table only if a PC+2 dependency makes it worthwhile.
- [ ] Recover MCC/RTCC transformation rules only where PC+2 station behavior requires them.

The telemetry evidence narrows source candidates but does not certify every telemetry-word-to-CRT-field mapping. Non-PC+2 display details remain deferred.

## Phase 4 — Authoritative simulation model

**Status:** **nominal event + controller-product + partial rule/non-nominal validation model in progress**

**Goal:** produce mission state from which historically appropriate telemetry/products can be derived while preserving subsystem boundaries.

### Completed first-slice model work

- [x] research-derived initialization contract at 77:55 GET
- [x] stable implementation-oriented PC+2 parameter names and units
- [x] separation of PAD LVLH target, PGNS IMU Vg, physical burn result, and guidance residuals
- [x] nominal historical validation fixture including TIG, duration, cutoff, Vg, and residuals
- [x] explicit stop conditions for unavailable low-impact numeric detail
- [x] nominal state-transition model through post-burn power-down
- [x] source-level failure-transition hooks without speculative failure scripts
- [x] framework-neutral Python nominal event prototype and validation tests
- [x] two-jet ullage and minimum/40-percent/maximum commanded throttle phases separated from crew throttle reports
- [x] station-specific controller-product projection layer with timing, validity, source layer, and provenance
- [x] independent source-backed shutdown-rule audit evaluator without a generic `burn_abort` state
- [x] first deferred shutdown-rule observation path modeled: distinct ISS warning signal projected to GUIDO
- [x] first source-backed nonnominal rule-path validation case: ISS warning + program alarm triggers the documented conjunctive criterion without automatically commanding shutdown
- [x] first analog propulsion observation path modeled: LM-7-family `GQ6510P` chamber pressure projected to CONTROL when a numerical value is explicitly supplied
- [x] second source-backed nonnominal rule-path validation case: modeled chamber pressure at/below the documented 85-psi ground threshold triggers the audit without automatically commanding shutdown

### Immediate next work

- [x] define subsystem dependencies; derived equations remain limited to sourced/required behavior
- [ ] determine minimum trajectory-state representation required for the first propagating implementation
- [x] define update/sample semantics for minimum player-facing products; exact CRT cadence remains unresolved where unsupported
- [x] convert nominal state machine/parameter contract into first implementation schema/data fixture
- [x] add controller-product projections from authoritative state with validity/provenance metadata
- [x] implement independent shutdown-rule evaluation limited to modeled observations
- [x] model first deferred shutdown-rule observation path from defensible primary-source evidence
- [x] add first source-backed nonnominal validation case at the rule-path level
- [x] research and model one propulsion-pressure observation path from primary/mission-era evidence without inventing nominal values
- [ ] introduce a minimal generic scenario/failure-injection object that perturbs underlying state/observations rather than setting diagnoses; keep synthetic rule-boundary fixtures explicitly non-historical
- [ ] research another deferred rule path only when needed by that injection architecture or first playable CONTROL workflow; likely candidates are the separate onboard thrust indication, inlet/differential pressure, or inverter-after-switch logic

The exact Cartesian RTCC state vector at 77:55 is deliberately not reverse-engineered from the maneuver PAD. It becomes an active target only when the propagator requires it.

Detailed DPS engine-response/ramp dynamics remain deferred. The prototype models the source-backed commanded throttle profile and separate crew reports.

The projection implementation does not expose required-but-unmodeled values as simulated `unavailable` telemetry. They remain implementation gaps.

The ISS-warning work resolves the positive ISS+program-alarm observation path while preserving two important limits: no exact LM-7 telemetry word or GUIDO CRT field is claimed, and no hypothetical failure mechanism/program-alarm number is invented. See research note 054.

The chamber-pressure work similarly resolves a real LM-7-family measurement identity and CONTROL rule path without inventing the nominal PC+2 pressure trace, exact MSK 1137 routing, or a malfunction mechanism. See research note 055.

### Phase 4 deliverables

- [x] first-slice documented parameter dictionary
- [x] units and ownership/source layers
- [x] nominal-state validation targets
- [x] update/sample behavior contract
- [x] subsystem dependency contract
- [x] executable nominal event fixture/state model
- [x] controller-product projection layer
- [x] partial shutdown-rule evaluation + validation tests
- [x] first source-backed nonnominal rule-path validation case
- [x] first source-backed analog propulsion rule-path validation case
- [ ] broader failure propagation tests

## Phase 5 — Mission Control data path

**Goal:** separate physical state from what controllers actually receive.

Conceptual path:

spacecraft state → instrumentation/telemetry → communications/network → ground processing → controller-accessible displays/products

Deliverables:

- telemetry channel model
- stale/missing/invalid-data behavior where documented
- controller-specific parameter availability
- ground-computed values where documented
- display refresh behavior

**Current checkpoint:** `controller_products.py` enforces station boundaries for the modeled PC+2 subset. It is an information-projection layer, not yet a complete telemetry/network simulator. The ISS-warning path supplies a researched discrete warning; the chamber-pressure path now supplies the first explicitly researched analog propulsion measurement that becomes a CONTROL product only when numerically modeled.

## Phase 6 — Procedures and flight rules

**Goal:** make controller documentation operational.

- identify rules applicable to selected mission interval
- map rules to responsible positions
- identify supporting procedures/tables
- produce print-oriented controller packets
- distinguish verbatim historical material from project-created guides
- validate that simulation exposes enough information for each implemented rule

**PC+2 checkpoint:** the evaluator can audit modeled discrete warning criteria without issuing a shutdown command. ISS warning + program alarm is fully evaluable as a conjunction. Ground chamber pressure is now evaluable whenever a modeled CONTROL measurement is present and remains `not_evaluable` when the project has not supplied a numerical value. Inlet/differential pressure, attitude/rate, crew analog indications, and positive inverter-after-switch remain deferred. The startup-transient wording conflict remains unresolved.

## Phase 7 — Simulation scenarios / SimSup

**Goal:** reproduce training behavior from documented simulation practice.

Research before authoring includes simulator/MCC integration, Simulation Supervisor responsibilities, malfunction insertion, and documented training cases.

Scenario implementation should inject underlying conditions/failures rather than announce diagnoses.

Deliverables:

- scenario format
- failure injection interface
- nominal run
- documented nonnominal run(s)
- SimSup/operator interface if appropriate

The current ISS-warning + program-alarm and low-chamber-pressure tests are **rule-path validation fixtures**, not narrative/documented Apollo training scenarios. Synthetic boundary values are explicitly labeled as test data and do not imply historical Apollo 13 malfunctions.

## Phase 8 — Multi-player session layer

**Goal:** support in-person cooperative operation without changing historical information unnecessarily.

Required capabilities include central authoritative server, session/join, station assignment, phone clients, synchronized mission time/state, reconnection, and server-controlled scenario state.

Role aggregation decisions remain deferred until station research supports them.

## Phase 9 — Communications

**Goal:** reproduce enough voice structure to affect controller work.

Potential scope includes Flight loop, discipline/backroom loops, air-to-ground/CAPCOM path, crew voice, and headset/loop behavior.

The PC+2 nominal start already requires a weak-but-usable air-ground link that can interfere with final PAD/readback before improving after the S-band power-amplifier change.

## Phase 10 — Post-simulation review

**Goal:** support learning/replay without an in-play score layer.

Potential outputs include mission outcome, command/decision timeline, system evolution, rule/procedure references, communications timeline, and historical comparison.

## Phase 11 — Expansion

After the vertical slice is validated:

- Apollo 13 oxygen-tank accident / immediate stabilization
- Apollo 11 powered descent as mission-profile portability test
- additional mission phases/missions/configurations
- larger controller complements
- Staff Support Room roles if practical
- additional documented simulation cases
- deeper ground-system fidelity

## Validation approach

The project uses layered verification:

1. component/source fidelity;
2. subsystem closed-loop validation;
3. onboard-computer / RTCC integration;
4. procedure validation;
5. documented boundary/anomaly tests;
6. integrated controller simulation.

See `docs/SIMULATION_VALIDATION.md`.
