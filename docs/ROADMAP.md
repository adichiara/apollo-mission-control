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

**Important:** minimum player count and role aggregation are not decided until this work shows what would actually be combined or lost.

## Phase 2 — Select the first simulation baseline

**Goal:** choose a specific mission and phase for the first implementation.

Candidate selection criteria:

- quality of surviving documentation
- availability of mission rules and procedures
- availability of controller/display information
- availability of transcripts/audio
- availability of simulator or malfunction records
- useful interaction among several controller disciplines
- manageable first implementation scope

Deliverables:

- selected mission/configuration
- exact spacecraft/ground-system baseline
- selected mission interval
- nominal timeline
- source package for that interval

No candidate is considered selected until recorded in `docs/DECISIONS.md`.

## Phase 3 — Display and console reconstruction

**Goal:** reproduce the information presentation used by controllers.

Research and catalog:

- operational display formats
- formatting rules
- character sets and typography
- CRT geometry and field layout
- update rates where documented
- display request/selection workflow
- plot/tabular formats
- console controls relevant to play
- hard-copy products where relevant

Deliverables:

- display format specification
- reusable historical display renderer
- controller-specific display catalog for the selected baseline
- authenticity comparison against source photographs/manuals

## Phase 4 — Authoritative simulation model

**Goal:** produce the mission state from which historically appropriate telemetry can be derived.

Model only what the selected scenario requires initially, but preserve subsystem boundaries.

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

- documented parameter dictionary
- units/ranges/update rates
- subsystem dependencies
- nominal-state validation cases
- failure propagation tests

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

## Phase 6 — Procedures and flight rules

**Goal:** make controller documentation operational.

- identify rules applicable to selected mission interval
- map rules to responsible positions
- identify supporting procedures/tables
- produce print-oriented controller packets
- distinguish verbatim historical material from project-produced indexes/guides
- validate that the simulation exposes enough information for a controller to apply each implemented rule

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

- additional mission phases
- additional Apollo missions/configurations
- larger controller complements
- Staff Support Room roles if practical
- additional documented simulation cases
- deeper ground-system fidelity
