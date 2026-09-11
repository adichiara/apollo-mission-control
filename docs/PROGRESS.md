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


## 2026-09-11 — Phase 1: Apollo 13 station baseline and simulation-case research

### Controller station reconstruction

- Added an Apollo 13 station-by-station working baseline for FLIGHT, CAPCOM, FIDO, RETRO, GUIDO, EECOM, GNC, TELMU, CONTROL, INCO, PROCEDURES, FAO, and SURGEON.
- Preserved distinction between documented responsibilities and still-missing display/console details.
- Identified EECOM as the first station that can plausibly be reconstructed from surviving console evidence:
  - actual console layout
  - two high-use display examples
  - parameter labels/example values
  - one-second display updates
  - event/limit-sense behavior
- Recorded controller-specific operational evidence from the Apollo 13 Mission Operations Report:
  - GNC diagnosing RCS/control behavior
  - TELMU managing LM lifetime/consumables
  - CONTROL handling DPS/RCS/attitude concerns
  - INCO managing link/antenna/command behavior
  - GUIDO handling onboard guidance/computer/alignment state
  - FIDO dealing with tracking validity and RTCC trajectory state

### Simulation-case research

- Confirmed that Apollo 13 premission training was broken into documented mission-phase simulations rather than one generic full-mission simulation.
- Cataloged named simulation families including LM activation/descent, descent abort, ascent, launch abort, reentry, LOI/DOI, TEI, FIDO/BSE math-model, network, and communications/data-flow validation.
- Added scenario evidence levels so a named historical simulation category is not mistaken for a fully reconstructable scenario.
- Recorded the Apollo 11 computer-failure/program-alarm simulation as a high-priority case to reconstruct from stronger source material.
- Recorded Harold Miller's account that simulations were intended to exercise procedures, ground rules, teamwork, and communications and that simulated data was routed through the control-center system.

### New documents

- `docs/APOLLO13_STATION_BASELINE.md`
- `docs/MISSION_PROFILE_MODEL.md`
- `docs/SIMULATION_SCENARIO_RESEARCH.md`
- `resources/research/010_apollo13_controller_station_evidence.md`
- `resources/research/011_apollo_simulation_cases.md`

### Next research

1. Reconstruct the Apollo 13 EECOM station in detail from figures B7-7 through B7-9 and related documentation.
2. Locate exact display-format information for GNC, TELMU, CONTROL, GUIDO, FIDO/RETRO, and INCO.
3. Search archival references for SimSup case sheets/malfunction lists.
4. Reconstruct the Apollo 11 program-alarm simulation case as far as documentation allows.
5. Continue mapping station responsibilities to telemetry parameters and control actions.


## 2026-09-11 — Phase 1: Detailed EECOM reconstruction

### Completed

- Added a detailed Apollo 13 EECOM station specification.
- Transcribed the two official Review Board display families:
  - **CSM EPS HIGH DENSITY**
  - **CSM ECS-CRYO TAB**
- Recorded their documented one-second update cadence.
- Cataloged major parameter families, measurement identifiers, units, and representative values from figures B7-8 and B7-9.
- Documented the three event-indicator groups and the manual limit-sense behavior.
- Recorded that panel 3 contained 72 lights, including 12 cryogenic pressure/temperature/quantity limit-sense lights.
- Recorded the Review Board finding that an O2 tank 2 pressure limit indication should have occurred roughly 30 seconds before failure but may not have been observed.
- Separated **HSD Format 30** historical playback from the live display named **CSM EPS HIGH DENSITY**.
- Recorded that Format 30 was new for Apollo 13 and used extensively for O2 tank 2 anomaly playback.
- Explicitly withheld any Apollo 13 EECOM direct-command controls because current evidence has not established them.
- Added a source-quality warning for the modern Andy Anderson EECOM reconstruction: parts of its DRK and limit-sense layout are acknowledged reconstructions rather than primary documentation.

### New documents

- `docs/stations/APOLLO13_EECOM.md`
- `resources/research/012_apollo13_eecom_reconstruction.md`

### Major source-provenance finding

Philco-Ford progress report **PHO-TR474** confirms that the Apollo 13 / Mission H-2 **PHO-TR155 Revision C** was issued on **1970-03-06**.

This means the missing exact Apollo 13 MCC Operational Configuration is not hypothetical; its existence and revision date are documented. Locating a surviving copy is now a high-priority archival target.

### Current EECOM implementation status

Enough evidence exists for a research prototype of the two principal EECOM displays and basic console behavior.

Not enough evidence yet exists to claim a complete Apollo 13 EECOM console recreation.


## 2026-09-11 — Phase 1: Detailed CSM GNC reconstruction

### Completed

- Added a detailed Apollo 13 CSM GNC station specification.
- Reconstructed mission-specific GNC reasoning around:
  - SM RCS quad/manifold pressures
  - helium isolation state
  - electrical-bus dependencies
  - DAP quad selection
  - commanded jets versus actual control authority
  - unavailable valve/talkback indications
  - CM RCS injector-temperature/preheat requirements
- Recorded the critical information-quality rule that **loss of indication power does not reveal the physical valve state**.
- Clarified the GNC/GUIDO boundary:
  - GNC = physical propulsion/control hardware and achieved vehicle control
  - GUIDO = onboard computer/guidance/navigation state and updates
- Identified **CSM GNC PRIMARY TAB 0683** in Apollo 11/12 AC/Delco material as a strong continuity candidate.
- Confirmed that an Apollo 13-specific AC Electronics Guidance and Navigation Summary exists in the Smithsonian archive and contains an **ASPO 45 CRT Displays** section.
- Did **not** assume that display 0683 carried into Apollo 13 unchanged.

### New documents

- `docs/stations/APOLLO13_GNC.md`
- `resources/research/013_apollo13_gnc_reconstruction.md`

### Highest-value missing evidence

1. Digitally inspect the Smithsonian Apollo 13 AC Electronics manual.
2. Locate H-2 PHO-TR155 Revision C.
3. Confirm Apollo 13 GNC display numbers/layouts.
4. Locate exact GNC console panel configuration.


## 2026-09-11 — Phase 1: Detailed LM CONTROL and TELMU reconstruction

### LM CONTROL

- Added a detailed Apollo 13 CONTROL station specification.
- Reconstructed the pre-accident DPS supercritical-helium monitoring decision tree:
  - 660–770 psia: acceptable
  - 770–800 psia: recheck
  - >800 psia: periodic telemetry/trend extrapolation
  - predicted ≥1800 psia at PDI: proposed DPS burn/vent procedure
- Documented CONTROL's role in LM activation, DPS/RCS configuration, GDA trim, DAP/deadband changes, RCS conservation, PTC establishment, and contingency maneuver planning.
- Recorded the PC+2 shutdown rules, including a fuel/oxidizer inlet differential criterion explicitly described as a **ground callout only**.
- Preserved the distinction between CONTROL's physical propulsion/control role and GUIDO's guidance/computer role.

### TELMU

- Added a detailed Apollo 13 TELMU station specification.
- Reconstructed the LM lifetime problem around:
  - electrical current / amp-hours
  - cooling water
  - oxygen
  - LiOH / CO2 removal
  - thermal state
- Documented progressive power-down from roughly 45–50 A to about 12 A and water-use reduction to about 2.5–2.8 lb/hr.
- Recorded the early consumable targets used to support the selected return trajectory.
- Recorded configuration-dependent cases where simple fixed-limit logic would be wrong:
  - invalid nominal O2 redline in the actual configuration
  - probable battery-warning sensor failure despite nominal voltage/current
  - changing CO2 capability after adaptation of CSM LiOH cartridges
- Documented TELMU's continuous use of projected consumable lifetime relative to mission milestones.

### New documents

- `docs/stations/APOLLO13_CONTROL.md`
- `docs/stations/APOLLO13_TELMU.md`
- `resources/research/014_apollo13_control_reconstruction.md`
- `resources/research/015_apollo13_telmu_reconstruction.md`

### Pattern now established across four stations

EECOM, GNC, CONTROL, and TELMU all show the same important simulator principle: the controller should reason from **imperfect measurements, configuration, trends, dependencies, and rules**, not receive a software diagnosis of the underlying failure.


## 2026-09-11 — Apollo 13 EECOM reference-station deep dive

### Completed

- Promoted CSM EECOM to the first detailed reference-station specification.
- Transcribed the documented logical contents of the two Apollo 13 EECOM formats identified by the Review Board as most frequently used:
  - **CSM EPS HIGH DENSITY**
  - **CSM ECS-CRYO TAB**
- Preserved original telemetry/channel identifiers where visible in the source rather than replacing them with project-generated names.
- Recorded the documented **one-second update cadence** for these two formats.
- Documented Apollo 13 EECOM event/limit-sense behavior:
  - manually selected high/low thresholds
  - intentionally tight monitoring limits
  - 72 indicators on panel 3
  - 12 cryogenic pressure/temperature/quantity limit-sense indications
  - master caution/warning event indication
  - historically non-latching transient behavior
- Recorded the Review Board finding that an O2 tank 2 pressure limit indication should have occurred roughly 30 seconds before tank failure but may not have been noticed.
- Separated normal one-second CRT telemetry from **High Speed Data Format 30** playback.
- Recorded HSD Format 30 structure from AS-508 configuration documentation: 2.4 kbps post-pass playback, selectable CSM/LM high-rate subformats.
- Explicitly left unresolved the Apollo 13 EECOM DRK, MSK, SMEK, event-panel legends, analog-meter use, full display inventory, and exact ground-command authority.
- Recorded that modern EECOM reconstruction drawings contain acknowledged inference from later missions and therefore cannot resolve those gaps.

### New/updated documents

- `docs/stations/APOLLO13_EECOM.md`
- `resources/research/012_apollo13_eecom_reference_station.md`

### Key simulation implication

EECOM monitoring is not merely a numeric-data screen. The historical station has at least three distinct information mechanisms that must remain separable:

1. real-time selectable CRT formats,
2. transient event/limit-sense indications,
3. higher-rate recorded telemetry/playback products.

The simulator should preserve the possibility that the correct information exists but is overlooked, transient, contradictory, or initially interpreted as instrumentation failure.


## 2026-09-11 — GNC display-source and simulator-document research

### Apollo 13 GNC display source

- Confirmed that the full **AC Electronics Apollo 13 Guidance & Navigation Summary** is publicly linked in the Apollo 13 Flight Journal high-resolution collection.
- Independently confirmed the same title in the Smithsonian NASM Hamilton collection.
- Confirmed the Apollo 13 volume contains an **ASPO 45 CRT Displays** section.
- Did **not** assume that Apollo 11/12 **CSM GNC PRIMARY TAB 0683** or LM displays 1123/1137 carried over unchanged.
- Updated the GNC station specification to mark mission-specific CRT extraction as the remaining primary-source task.

### Simulator technical sources

- Identified surviving Lunar Module Mission Simulator instructor documentation describing simulator switches, displays, and subsystem simulation.
- Identified the LEM Mission Simulator technical addendum containing mathematical-model flowcharts.
- Identified a Lunar Module Simulator user's manual and Console Directory reportedly listing available simulator telemetry.
- Added a new research distinction:
  - spacecraft documentation tells us what the real vehicle did;
  - Mission Control documentation tells us what controllers saw/did;
  - simulator documentation tells us how NASA/Singer itself modeled the vehicle for training.

### New notes

- `resources/research/013_apollo13_gnc_crt_source.md`
- `resources/research/014_mission_simulator_technical_sources.md`

### Next

1. Extract the Apollo 13 ASPO 45 CRT section.
2. Locate/download the LM Mission Simulator Instructor Handbook and Console Directory.
3. Use simulator documentation to validate the LM subsystem model before inventing any equations.
4. Continue station-display reconstruction for CONTROL/TELMU/INCO.


## 2026-09-11 — NASA simulator configuration/fidelity research

### Completed

- Reviewed NASA MSC's 1968 **Flight Crew Operations Branch — Simulator Operations** report.
- Documented that Apollo simulator fidelity was maintained through formal configuration/change control rather than informal approximation.
- Recorded that simulator system changes were checked against controlled spacecraft sources such as Apollo Operations Handbooks, schematics, and approved modification data.
- Recorded the simulator distinction between:
  - spacecraft-representation behavior,
  - instructor-only aids/readouts,
  - known simulator discrepancies.
- Confirmed that integrated training was preceded by explicit MCC-Houston ground-interface checkout.
- Added the principle that known historical simulator artifacts/limitations must not be mistaken for actual spacecraft physics.

### New research note

- `resources/research/015_simulator_configuration_fidelity.md`

### Architecture implication

The eventual SimSup/instructor interface may expose authoritative simulation state and special instructor aids, but those data must remain isolated from controller players unless a historical controller product carries them into Mission Control.
