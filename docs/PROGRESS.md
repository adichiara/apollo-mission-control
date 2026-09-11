# Progress Log

## 2026-09-11 — Foundation

### Repository

- Confirmed repository: `adichiara/apollo-mission-control`
- Repository was empty at initialization.
- Added project documentation structure.
- No implementation code added yet.

### Project principles recorded

- research/documentation before Apollo-specific design
- no silent invention of undocumented historical details
- simplification only after real complexity is understood
- simulator-style presentation rather than conventional game UI
- mission success first; safe crew return when objectives are lost
- central server with phone-based controller clients
- physical station documentation as part of play

### Initial historical research

Primary/near-primary NASA material identified for:

- Apollo 11 flight mission rules
- Apollo 11 flight plan
- Apollo 11 mission operations/support structure
- Apollo Mission Control organization and controller workflow
- Apollo program mission-control architecture
- MCC operational display-format standards
- flight-rule development and use
- integrated Apollo mission simulation/training

See `resources/PRIMARY_SOURCE_CATALOG.md` and research notes.

### Next work

1. Reconstruct controller organization/responsibilities.
2. Reconstruct MCC console/display architecture.
3. Determine candidate first mission interval from documentation quality and useful controller interaction.
4. Only then begin decisions about player-count aggregation and implementation scope.


## 2026-09-11 — Phase 1: Flight-control organization, pass 1

### Completed

- Reconstructed the documented three-group MOCR structure:
  - Mission Command and Control
  - Systems Operations
  - Flight Dynamics
- Documented the primary front-room responsibilities for FLIGHT, CAPCOM, EECOM, GNC, TELCOM, CONTROL, FIDO, RETRO, GUIDO, Booster, INCO, O&P, NETWORK, SURGEON, FAO, and related positions.
- Documented the major Staff Support Rooms and their functions.
- Documented the CCATS and RTCC support layers and their relationship to controller information.
- Checked the Apollo 11 official flight-control manning memorandum.
- Confirmed that Apollo 11 used the LM call sign **TELCOM** in its official manning list and actual EVA Flight Director loop.
- Recorded evidence that TELCOM later changed to TELMU rather than treating the labels as interchangeable.
- Identified a mission-specific staffing warning: Apollo 11's manning memorandum uses four shift columns, while the Apollo 13 baseline describes three 9-hour shifts.

### New documents

- `docs/FLIGHT_CONTROL_ORGANIZATION.md`
- `resources/research/003_mocr_positions_and_responsibilities.md`
- `resources/research/004_support_rooms_and_ground_processing.md`
- `resources/research/005_apollo11_manning_and_nomenclature.md`

### Architecture consequence

The documented MCC organization reinforces the existing separation between physical spacecraft state, instrumentation/telemetry, ground processing, and controller-visible information. RTCC explicitly generated displays/calculations and CCATS explicitly handled telemetry/command/tracking flow; controller clients should not bypass those logical boundaries where they matter operationally.

### Next research pass

1. Reconstruct physical console/display capabilities and controller display-request workflow.
2. Identify mission-specific display formats for the likely Apollo 11 LM activation/descent interval.
3. Begin mapping controller positions to actual displays, parameters, and support-room inputs.
4. Research voice-loop topology using primary Apollo documentation/audio.
5. Continue searching for integrated-simulation / SimSup scenario documentation.


## 2026-09-11 — Phase 1: Console/display architecture, pass 1

### Completed

- Documented the high-level MCC console display path from RTCC-generated information through the Display and Control System to controller CRTs.
- Confirmed that MCC operational displays combined static/background information with dynamic real-time information.
- Documented that controller displays were requested in preset formats rather than functioning as fixed dashboards.
- Identified Apollo-11-specific Philco-Ford report **PHO-TN401**, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*.
- Recorded its archival location; a public digital copy was not found in this search pass.
- Documented the historical distinction between controller CRT displays, group displays, and hard-copy/pneumatic-tube products.
- Recorded that exact MSK/DRK hardware by Apollo 11 station remains unresolved.

### New documents

- `docs/DISPLAY_SYSTEM_BASELINE.md`
- `resources/research/006_console_display_architecture.md`

### Important implementation constraint

A generic "retro terminal" is no longer an acceptable historical stand-in for the final controller display. The documented MCC system constructed selectable operational display formats from static and dynamic elements. Exact station formats must be reconstructed before the player interface is treated as historically faithful.

### Next research

1. Locate Apollo 11-era console layout and display-format inventories by controller.
2. Locate PHO-FAM001 (1967 MCC Houston Familiarization Manual).
3. Continue search for PHO-TN401.
4. Map controller responsibilities to actual displays/parameters.
5. Begin primary-source voice-loop topology reconstruction.


## 2026-09-11 — Phase 1: Controller information workflow, pass 2

### Completed

- Located and reviewed the Apollo-11-specific **RTCC Operations Support Plan for Mission G**.
- Identified Apollo 11 telemetry-reference MSK display numbers.
- Confirmed mission-specific operational use of display requests, PBI inputs, MED inputs, and hard-copy verification.
- Identified PHO-TR170A and PHO-TR170B as key missing requirements/display-format documents.
- Documented the Apollo TV display distinction between display-request mode and channel-attach mode.
- Recorded that lunar missions used 36 computer-driven TV channels.
- Added a concrete Apollo 13 EECOM console benchmark while explicitly keeping it separate from Apollo 11 configuration.
- Documented NASA's formal distinction between:
  - Flight Mission Rules
  - Flight Control Operations Handbook interface procedures
  - controller-specific Flight Controller Console Handbooks
- Recorded the physical-paper adaptation for historically hard-copy products.

### New documents

- `docs/CONTROLLER_INFORMATION_WORKFLOW.md`
- `docs/PHYSICAL_DOCUMENT_WORKFLOW.md`
- `resources/research/007_mission_g_rtcc_operations.md`
- `resources/research/008_controller_console_and_document_evidence.md`

### High-priority source hunt created

1. PHO-TR170A
2. PHO-TR170B
3. Apollo-11-era PHO-TR155
4. Mission G Flight Control Operations Handbook
5. Mission G controller console handbooks
6. Data Acquisition Plan Annex B / Telemetry Data Formats Control Handbook

### Next research

- map specific controller stations to display families and telemetry parameters
- reconstruct voice-loop topology
- identify which dynamic products were hard copy versus CRT
- locate console-handbook material for the Apollo 11 CSM and LM systems positions


## 2026-09-11 — Phase 1: Voice communications, pass 1

### Completed

- Confirmed the Apollo MCC Voice Communications Subsystem as a dedicated technical subsystem in PHO-FAM001.
- Documented internal intercom, air-to-ground control, recording/playback, trainer circuits, and communications switching as part of the controller environment.
- Added a high-level voice-loop architecture document.
- Recorded the in-person communication problem explicitly: co-located players can bypass historically meaningful information channels simply by talking across the table.

### New documents

- `docs/VOICE_COMMUNICATIONS_BASELINE.md`
- `resources/research/009_voice_communications_system.md`

### Not decided

No headset/loop implementation has been selected. The first scenario's actual loop requirements will be researched before choosing how strictly to enforce voice topology.


## 2026-09-11 — Architecture clarification: later Apollo baseline

### Decisions clarified

- Paper exchange will not be formalized as a game mechanic. Hard-copy use remains a historical research topic; players may naturally use/pass paper in person as useful.
- Staff Support Rooms remain part of the historical reconstruction, but no decision has been made about representing them as player roles, automated agents, or explicit messages.
- The reusable simulation platform will use the **Apollo 13-era MCC as the default technical baseline/superset**, with mission-specific profiles overriding later features where required.
- The first playable mission/scenario remains undecided.

### Historical reason for mission profiles

Mission-specific differences are already documented. Apollo 13's Mission Operations Report has a dedicated **TELMU** appendix, whereas Apollo 11's official manning/audio uses **TELCOM**. The AS-508 MCC/MSFN Mission Configuration/System Description provides a detailed Apollo 13-era ground-system baseline.

Therefore "Apollo 13 baseline" means reusable platform architecture, not that later terminology/configuration may be shown unchanged in Apollo 11 scenarios.
