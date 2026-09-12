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

Research:

- MOCR organization by mission/era
- Staff Support Rooms and backroom relationships
- controller positions and responsibilities
- console equipment
- voice loops
- display request mechanisms
- RTCC / CCATS / display-control information flow
- Manned Space Flight Network interfaces
- mission phase changes in staffing/responsibility
- shift/hand-over practices where relevant

Deliverables:

- controller responsibility matrix
- documented MOCR layout(s)
- role-to-data/display map
- role-to-backroom/communications map
- terminology glossary
- unresolved historical questions list

**Current interpretation:** Apollo 13 core front-room positions are at B or better, with EECOM at A, and the common telemetry/ground-processing/display architecture is sufficiently established to support a bounded vertical slice. Exact console/display reconstruction remains incomplete for many stations but is no longer a prerequisite for moving forward when the missing detail does not affect the selected scenario.

Research now follows the sufficiency rule in `docs/PROJECT_PRINCIPLES.md`: inaccessible or low-impact gaps are logged and deferred rather than allowed to block broader progress.

## Phase 2 — Select the first playable mission/scenario

**Status:** **selected and initialized — Apollo 13 PC+2 preparation/execution**

**Goal:** choose a specific mission and phase for the first implementation.

The reusable technical platform uses the Apollo 13-era MCC as its default research/implementation baseline, with mission-specific historical profiles layered over it.

### Selected vertical slice

**Apollo 13 PC+2 preparation and execution**, with the nominal first implementation starting at **77:55:00 GET** and running through immediate post-burn verification/power-down around 79:34–80:00 GET.

Selection basis:

- strong surviving primary documentation;
- explicit mission rules and burn-shutdown criteria;
- meaningful interaction across FLIGHT, FIDO/RETRO, GUIDO, CONTROL, TELMU, INCO, FAO/PROCEDURES and CAPCOM;
- direct compatibility with the Apollo 13-era technical baseline;
- bounded propulsion/guidance event rather than a continuously spreading compound failure;
- sufficient documentation to validate controller information flow without first implementing the entire Apollo 13 accident.

The **77:55:00 GET** start is source-driven: communications are weak after AOS and the final P30 LM maneuver PAD begins at 77:55:24, leaving a real information-transfer problem, final updates, burn power-up, readiness work and the entire burn live for the players.

Decision: `docs/DECISIONS.md`, D-013.  
Research comparison: `resources/research/048_first_vertical_slice_candidate_assessment.md`.  
Initialization/validation: `resources/research/050_pc2_initialization_and_nominal_validation.md`.  
Parameter specification: `docs/scenarios/APOLLO13_PC2_PARAMETERS.md`.

### Phase 2 deliverables

- [x] selected mission and mission-era profile
- [x] selected mission interval
- [x] freeze nominal scenario start at 77:55:00 GET
- [x] define the minimum spacecraft/ground-system configuration required at initialization
- [x] create a source-backed nominal PC+2 event timeline through immediate post-burn power-down
- [x] assemble the core scenario-specific primary-source package
- [ ] identify the controller positions required for the first full-fidelity multiplayer run and later low-player-count aggregation

Phase 2 no longer depends on complete Apollo-wide display reconstruction. Research effort should follow the selected slice.

## Phase 3 — Display and console reconstruction

**Goal:** reproduce the information presentation used by controllers.

Research and catalog:

- operational display formats
- formatting rules
- character sets and typography
- CRT geometry and field layout
- update rates where documented
- display request/selection workflow
- field meaning and display mask/precision, tracked separately from source-path evidence and mission-to-mission continuity
- field provenance (raw telemetry vs onboard-computed vs ground-derived)
- ground transformation/calculation path for derived CRT values
- validation cases for incorrect ground-derived products even when raw telemetry/spacecraft state are valid
- plot/tabular formats
- console controls relevant to play
- hard-copy products where relevant

Deliverables:

- display format specification
- reusable historical display renderer
- controller-specific display catalog for the selected baseline
- authenticity comparison against source photographs/manuals

### Current research checkpoint — Apollo 13 LM guidance/control displays

- [x] Mission-specific MSK 1123 and 1137 layouts identified and inspected.
- [x] Major LGC, PCM, AEA/AGS, and ground-derived source classes separated.
- [x] AEA Table 2.1-7 telemetry structure and engineering definitions recovered from a later contemporary handbook configuration, including distinct present-velocity, short-interval delta-V, sensed body-axis velocity-increment, DEDA, direction-cosine, and ullage-counter products.
- [x] Handbook chronology corrected: Apollo 13 LM-7 is Basic Date 15 Dec 1968 / Change Date 1 Feb 1970; searchable LM-10 is Basic Date 1 Feb 1970 / Change Date 15 Jun 1970.
- [x] AGS ullage qualification narrowed to a two-second accumulated +X velocity-increment test; equivalent later handbook wording expresses the same threshold as average acceleration over the cycle.
- [x] PC+2-critical information families separated into physical, onboard, telemetry/link, ground-derived and crew-report layers.
- [ ] Identify the **smallest historical display/product set actually needed for PC+2** at GUIDO, CONTROL, FIDO/RETRO, TELMU, INCO, FLIGHT and CAPCOM.
- [ ] Map only those PC+2-required products to the implementation parameter specification.
- [ ] Directly compare the Apollo 13 LM-7 Table 2.1-7 page against the later searchable LM-10 table **only if it becomes necessary for a PC+2-required field and remains reasonably accessible**.
- [ ] Recover MCC/RTCC rules for specific AEA-to-display transformations **only where required by PC+2 station behavior**.

The telemetry evidence narrows source candidates but does not certify every telemetry-word-to-CRT-field mapping. Non-PC+2 display details are explicitly deferred.

## Phase 4 — Authoritative simulation model

**Status:** **parameter contract begun**

**Goal:** produce the mission state from which historically appropriate telemetry can be derived.

Model only what the selected scenario requires initially, but preserve subsystem boundaries.

### First-slice model priorities — PC+2

- mission clock / PC+2 event timeline
- docked CSM/LM/SM configuration relevant to the burn
- trajectory state and target solution
- LM DPS thrust/chamber/inlet/propellant state
- LM RCS / attitude-control state
- PGNS/LGC guidance state and AGS backup/cross-check state
- alignment / attitude-error state
- electrical state needed for burn readiness and post-burn power-down
- communications/uplink/ranging availability required for maneuver updates
- telemetry/measurement state for documented shutdown criteria
- crew readback/report events as a separate information source

### Completed first-slice model work

- [x] research-derived initialization contract at 77:55 GET
- [x] stable implementation-oriented PC+2 parameter names and units
- [x] explicit separation of PAD LVLH target, PGNS IMU Vg, physical burn result and guidance residuals
- [x] nominal historical validation fixture including TIG, duration, cutoff, Vg and residuals
- [x] explicit stop conditions for unavailable low-impact numeric detail

### Immediate next work

- [ ] define nominal event/state transitions from 77:55 through 79:34
- [ ] define subsystem dependencies and derived-value equations only where the selected slice needs them
- [ ] determine the minimum trajectory-state representation required for the first propagating implementation
- [ ] add failure-propagation hooks without yet authoring speculative failure scenarios

The exact Cartesian RTCC state vector at 77:55 is deliberately **not** being reverse-engineered from the maneuver PAD. It becomes an active research target only when the trajectory propagator requires it.

Workstreams:

- mission clock and event timeline
- spacecraft configuration/state
- trajectory/navigation state
- propulsion
- electrical power
- environmental/consumables
- guidance/navigation/control
- communications/instrumentation
- crew state where required
- ground network state where required
- sensor/instrumentation behavior
- telemetry generation and processing

Deliverables:

- [x] first-slice documented parameter dictionary
- [x] first-slice units and ownership/source layers
- [x] nominal-state validation targets
- [ ] update/sample behavior for each player-facing product
- [ ] subsystem dependencies
- [ ] failure propagation tests

## Phase 5 — Mission Control data path

**Goal:** separate physical state from what controllers actually receive.

High-level path to research and reproduce:

spacecraft state → instrumentation/telemetry → communications/network → ground processing → controller-accessible displays/products

Deliverables:

- telemetry channel model
- stale/missing/invalid-data behavior where documented
- controller-specific parameter availability
- ground-computed values where documented
- display refresh behavior

**PC+2 requirement:** the nominal implementation must already preserve source layer, sample/receive time, validity and data age structurally, even if some nominal transport errors are initially zero.

## Phase 6 — Procedures and flight rules

**Goal:** make controller documentation operational.

- identify rules applicable to selected mission interval
- map rules to responsible positions
- identify supporting procedures/tables
- produce print-oriented controller packets
- distinguish verbatim historical material from project-produced indexes/guides
- validate that the simulation exposes enough information for a controller to apply each implemented rule

**Immediate priority:** PC+2 shutdown criteria, final maneuver PAD/readback, alignment state, maneuver update/uplink procedure, DPS/RCS readiness, burn monitoring, GO/NO-GO polling, and immediate post-burn power-down handoff.

## Phase 7 — Simulation scenarios / SimSup

**Goal:** reproduce training behavior from documented simulation practice.

Research before authoring:

- Apollo simulator integration with MCC
- Simulation Supervisor responsibilities
- documented malfunction insertion methods
- documented training cases/exercises
- mission-specific simulation records where available

Scenario implementation should inject underlying conditions/failures rather than simply announce diagnoses.

Deliverables:

- scenario format
- failure injection interface
- nominal run
- documented nonnominal run(s)
- SimSup/operator interface if appropriate

## Phase 8 — Multi-player session layer

**Goal:** support in-person cooperative operation without changing historical information unnecessarily.

Required capabilities:

- central authoritative server
- session/join mechanism
- station assignment
- phone-based station clients
- synchronized mission time/state
- reconnection handling
- server-controlled scenario state

Then determine, from the controller research:

- minimum viable player count
- role aggregation for each supported player count
- which positions should never be combined
- which responsibilities can be omitted only for certain mission phases

## Phase 9 — Communications

**Goal:** reproduce enough of the voice structure to affect controller work.

Potential scope is intentionally undecided until researched:

- Flight loop
- discipline/backroom loops
- air-to-ground/CAPCOM path
- recorded/simulated crew voice
- headset/earbud support
- loop selection behavior

The PC+2 nominal start establishes one concrete communications requirement: a weak-but-usable air-ground link must be able to interfere with the final PAD/readback before improving after the S-band power-amplifier change.

## Phase 10 — Post-simulation review

**Goal:** support learning/replay without adding a game layer during operation.

Possible review material, only where objectively derivable:

- mission outcome
- timeline of commands/decisions
- system evolution
- flight-rule/procedure references
- communications timeline
- comparison with historical case where applicable

Do not introduce an arbitrary numerical score unless there is a later explicit project decision to do so.

## Phase 11 — Expansion

After the vertical slice is validated:

- Apollo 13 oxygen-tank accident / immediate stabilization
- Apollo 11 powered descent as a mission-profile portability test
- additional mission phases
- additional Apollo missions/configurations
- larger controller complements
- Staff Support Room roles if practical
- additional documented simulation cases
- deeper ground-system fidelity

## Validation approach

Apollo 13 readiness documentation shows a layered verification process rather than reliance on one end-to-end exercise. The project will follow the same broad pattern:

1. component/source fidelity;
2. subsystem closed-loop validation;
3. onboard-computer / RTCC integration;
4. procedure validation;
5. documented boundary/anomaly tests;
6. integrated controller simulation.

See `docs/SIMULATION_VALIDATION.md`.
