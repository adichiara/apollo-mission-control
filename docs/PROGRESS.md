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
3. Begin mapping controller positions to actual displays/parameters and support-room inputs.
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


## 2026-09-11 — Apollo 13 GUIDO / LM data-link reconstruction

### Completed

- Located and reviewed the Apollo-13-specific **R-567 Section 2, Revision 8** for flown LUMINARY 1C / LM131 Rev. 1.
- Documented the actual ground-to-LGC update workflow, including P27 and Verbs 70–73.
- Documented the six program-dependent LM downlink families:
  - Orbital Maneuvers
  - Coast and Align
  - Rendezvous and Prethrust
  - Descent and Ascent
  - Lunar Surface Align
  - AGS Initialization and Update
- Recorded mission-specific descent/ascent activation in P12, P63, P64, P66, P68, P70 and P71.
- Recorded actual Apollo 13 downlink data families including state vectors, body rates, CDU state, DAP flags, failure registers, radar data and guidance/control channels.
- Documented downlink **snapshot/time-coherence behavior**, establishing that telemetry packaging has its own timing semantics.
- Added the first detailed Apollo 13 GUIDO station specification.
- Explicitly preserved the distinction between raw LGC downlists and MCC CRT formats.

### Source conflict identified

A passage in Apollo 13 Review Board Appendix B appears to transpose TELMU and CONTROL responsibility descriptions. The Apollo 13 Mission Operations Report, acronym list, controller appendices and actual loop behavior consistently show:

- TELMU = LM electrical/environmental/EMU/consumables
- CONTROL = LM guidance/control/propulsion

The contradictory Review Board passage is now documented rather than silently ignored.

### LM simulator catalog progress

Identified exact catalog entries for LMA-790-2-LMS, including **Volume II Section 7 — Simulator Output Tables** (*67-16127). Locating the scan is now a targeted source-retrieval task.

### New files

- `docs/stations/APOLLO13_GUIDO.md`
- `resources/research/016_apollo13_lm_data_links.md`
- `resources/research/017_telmu_control_source_conflict.md`


## 2026-09-11 — Apollo 13 INCO station reconstruction

### Completed

- Added a detailed Apollo 13 INCO station specification.
- Documented INCO as a multi-variable communications/command role rather than a single signal-strength monitor.
- Recorded contemporary INCO cues:
  - digital uplink signal strength
  - calibrated uplink/downlink meters
  - telemetry dropouts
  - voice noise
  - antenna look-angle display
  - active MSFN site / two-way lock
  - bitrate
  - command margin
- Identified the mission-specific **LM Look Angle Display — MSK 1475**.
- Documented its Apollo 13 defect: it did not operate with LM low-bit-rate telemetry, a known simulation-discovered problem accepted for the mission and recommended for correction before Apollo 14.
- Documented CLAD/LAD dependency on RTCC Computer Dynamics MED inputs and the resulting cross-discipline coordination problem with FIDO.
- Documented actual Apollo 13 command-uplink timing/margin problems during PTC antenna switching.
- Documented the CSM HGA anomaly, S-IVB/LM downlink interference, low-power communications configuration, entry geometry/attenuation anomaly, and DSE data-retrieval role.
- Recorded INCO's unusually direct simulation critique: incorrect simulation of communications dependencies produced **negative training** and reduced Flight Director confidence.

### New files

- `docs/stations/APOLLO13_INCO.md`
- `resources/research/018_apollo13_inco_station.md`

### Key architecture consequence

The communications subsystem must expose physical/link dependencies rather than scripted command success/failure. A communication command can fail because geometry, antenna selection, network lock, bitrate, carrier/subcarrier state, or ground-site procedure removes the command path.

### Next

1. Locate the actual MSK 1475 screen definition.
2. Resolve CLAD full title/display number.
3. Extract INCO DRK/MSK assignments and command-verification workflow.
4. Continue with FIDO/RETRO to reconstruct the ground trajectory side of the same cross-discipline data chain.


## 2026-09-11 — Apollo 13 FIDO / RETRO reconstruction

### Completed

- Added detailed FIDO and RETRO station specifications from the Apollo 13 Mission Operations Report.
- Preserved the internal distinction:
  - **FIDO** = ground trajectory solution and data/vector quality.
  - **RETRO** = return/reentry plan built from the accepted trajectory.
- Documented FIDO handling of:
  - invalid or unavailable tracking data
  - multiple competing vectors (IU, CMC, high-speed, Select, MSFC)
  - RTCC ephemeris/model-state errors
  - tracking glitches versus possible real ΔV
  - communications interference delaying valid LM tracking
  - final entry-vector selection
- Documented RETRO handling of:
  - P37/RTE block data
  - free-return restoration
  - direct-return and PC+2 option trades
  - landing time / landing area / ΔV / weather / recovery tradeoffs
  - entry PAD generation
  - entry flight-path angle
  - onboard/ground clock corrections
  - separation geometry and backup entry logic
- Preserved operational vector identifiers such as CCHU08, BDAX36, MILX99 and GWMX307 rather than replacing them with generic project labels.

### New files

- `docs/stations/APOLLO13_FIDO.md`
- `docs/stations/APOLLO13_RETRO.md`
- `resources/research/019_apollo13_fido_retro.md`

### Key architecture consequence

Even if future player-count scaling combines FIDO and RETRO, the simulator should retain separate trajectory-state and return-plan functions internally.


## 2026-09-11 — FLIGHT/CAPCOM, PROCEDURES/FAO, and Phase 1 station status

### New station specifications

- `docs/stations/APOLLO13_FLIGHT.md`
- `docs/stations/APOLLO13_CAPCOM.md`
- `docs/stations/APOLLO13_PROCEDURES.md`
- `docs/stations/APOLLO13_FAO.md`

### FLIGHT / CAPCOM findings

- Preserved FLIGHT as a decision/integration role rather than an omniscient master console.
- Preserved the operational communication path:
  `discipline → FLIGHT → CAPCOM → crew`.
- Documented crew observations/readbacks as a separate information source from telemetry.
- Documented verbal polling as a real readiness/ownership mechanism, not a game UI feature.

### PROCEDURES / FAO findings

- PROCEDURES owns the MCC/MSFN/ground procedural interface, not the crew activity timeline.
- FAO owns/coordinated the mutable flight plan and crew timeline.
- Identified **MSK 1503 — next station contact table** from the Apollo 13 PROCEDURES report.
- Documented real-time ground-processing changes, site handover problems, playback/delog coordination, and analog-recorder calibration impacts.
- Documented FAO's continuous integration of EECOM/GNC/NETWORK/Flight Plan Support constraints and the post-accident rebuilding of the crew timeline.

### Research status matrix

Added `docs/STATION_RESEARCH_STATUS.md`.

Current maturity:

- EECOM: A — station reference
- FLIGHT, CAPCOM, FIDO, RETRO, GUIDO, GNC, TELMU, CONTROL, INCO, PROCEDURES, FAO: B — strong mission-specific workflow evidence; exact displays still incomplete
- SURGEON, NETWORK, BOOSTER and several management/support positions: C — role baseline

The largest common Phase 1 gap is now exact console/display reconstruction, not role definition.


## 2026-09-11 — Exact-display continuity and Apollo 13 simulator discrepancies

### Display reconstruction

- Added `docs/DISPLAY_RECONSTRUCTION_STATUS.md`.
- Established a known display-number backbone:
  - MSK 683 — CM
  - MSK 966 — CM
  - MSK 1123 — LM
  - MSK 1137 — LM
  - MSK 1475 — Apollo 13 LM Look Angle Display
  - MSK 1503 — Apollo 13 Next Station Contact Table
- Transcribed cross-mission field families for LM MSK 1123 and 1137 from AC/Delco guidance material.
- Confirmed that later NASA telemetry tables still assign LM guidance/radar/propulsion parameters to 1123/1137, supporting functional continuity.
- Kept Apollo 13 status unresolved until the mission-specific ASPO 45 pages are extracted.
- Updated GUIDO and CONTROL specs with this evidence without promoting it to Apollo 13 fact.

### Apollo 13 simulator evidence

- Reviewed surviving Apollo 13 **Simulation Discrepancy Reports** referencing LUM 131 Rev. 1.
- Recorded a hardware-restart test showing coupled effects on navigation updates, P32 computation state, rate-control response, and other guidance/display behavior.
- Added these as engineering/simulator-test evidence, explicitly separate from integrated SimSup scenario evidence.

### New research notes

- `resources/research/022_cross_mission_lm_crt_evidence.md`
- `resources/research/023_apollo13_simulator_discrepancies.md`

### Next high-payoff source work

1. Extract Apollo 13 ASPO 45 CRT pages.
2. Find the LM Mission Simulator Volume II Section 7 output tables.
3. Locate Apollo-era RTCC/FIDO/RETRO display definitions.
4. Reconstruct the exact INCO MSK 1475 layout and PROCEDURES MSK 1503 layout.


## 2026-09-11 — H-2 Mission Techniques and validation architecture

### Mission Techniques

- Identified the Apollo 13 / Mission H-2 Mission Techniques suite as a central primary source for real-time decision logic.
- The documents explicitly state that they contain the officially approved:
  - guidance/control sequence of events
  - data flow
  - real-time decision logic
- Reviewed H-2 Lunar Descent, Descent Abort, Lunar Orbit, Powered Ascent, and Contingency material.
- Documented the H-2 division of responsibility:
  - ground detects slow/insidious drift and makes/advises decisions
  - crew handles errors requiring immediate action
  - ground-to-LM abort decision/communication delay may be up to about 20 seconds
- Documented PDI GO/NO-GO logic and the important exception that loss of high-bit-rate data did not automatically require NO-GO if guidance/navigation status could be adequately verified by manual readout/voice.
- Documented the pre-PDI ground-processing chain using MSFN tracking, RTCC high-speed mode, PFP/Lear processing, PGNCS/AGS/MSFN residuals and strip-chart displays.
- Documented multi-cue diagnosis requirements, landing-radar logic, propellant-margin analog monitoring, and Flight Director real-time judgment points.
- Added `resources/research/028_apollo13_mission_techniques.md`.

### Validation

- Added `docs/SIMULATION_VALIDATION.md`.
- Adopted a source-derived validation hierarchy:
  1. component/source fidelity
  2. subsystem closed-loop
  3. onboard computer / RTCC integration
  4. procedure validation
  5. boundary/anomaly cases
  6. integrated controller simulation
- Added validation states for documented limitations/deviations rather than treating fidelity as binary.

### New source

- Added the March 16, 1970 Apollo 13 LM Malfunction Procedures to the source catalog.


## 2026-09-11 — Apollo 13 ASPO 45 extraction blocker resolved

- Downloaded and visually inspected the mission-specific scan; CRT section is PDF pages 179–190 (ASPO-1–12).
- Confirmed MSK 683, 966, 1123, and 1137 and located layouts and definition pages.
- Verified selected LM definitions, including ground-computed fields, repeated BIAS labels, and a two-second PIPA interval that must not be mistaken for CRT refresh rate.
- Added research note 029 with exact page map, source hash, evidence limits, and next work.
- Updated display and station references. Station maturity remains unchanged; full field transcription, telemetry mapping, and Apollo 11 comparison remain pending.


## 2026-09-11 — Apollo 11/13 MSK 1137 comparison and inventory

- Visually compared Apollo 11 PDF 205–207 with Apollo 13 PDF 188–190.
- Confirmed changed CMD/SERVO versus BIAS/OCTAL rows, body versus stable-member radar velocities, and changed altitude/comparison definitions.
- Added note 030 with source hash, page references, limits and implications for mission-specific field profiles.
- Added note 031, a normalized inventory covering the named Apollo 13 1137 definition groups; grouped fields and uncertain labels are explicitly identified.
- Updated current display/station status to reflect the resolved extraction blocker.
- No live renderer, historical simplification, or scenario selection introduced.
- Next: full 1123 comparison, then CM 683/966; resolve calculations/downlist mappings before implementation.


## 2026-09-11 — Repository-wide evidence verification audit

- Inventoried all 67 pre-audit Markdown files and 54 unique external source URLs.
- Rechecked material claim families against NASA/NTRS records, contemporaneous mission reports, technical manuals, and directly rendered ASPO 45 pages.
- Corrected four obsolete NASA file URLs and clarified the exact identity/use of NTRS 19760066779 and 19710010485.
- Updated superseded ASPO 45 extraction statements while preserving genuine field-level and cross-mission limits.
- Added `resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md` with the findings and a complete file ledger.
- Added `scripts/audit_documentation.py` for repeatable link inventory, internal-link validation, duplicate-note detection, and optional HTTP diagnostics.
- Audit result: no material historical conclusion required reversal; remaining gaps are explicitly qualified.


## 2026-09-11 — LM CRT field provenance pass

### Completed

- Re-opened the Apollo 13 mission-specific **R-567 Rev. 8 LUMINARY 1C Data Links** source and visually verified the Descent/Ascent mnemonic and description pages.
- Mapped a substantial set of MSK 1123/1137 information families to actual LGC downlist sources, including radar data, DSKY state, rates, CDU angles, alarm/restart state, DAP/radar words, mass, PIPA/delta-V data, guidance thrust, and torque-command accumulators.
- Established that the Apollo 13 LM CRT pages are not raw downlist dumps.
- Identified a concrete ground-processing dependency: R-567 sends landing-radar velocity as time-tagged antenna-axis samples one component at a time, whereas MSK 1137 presents stable-member components and guidance-comparison residuals.
- Separated currently known field provenance into:
  - direct/decoded LGC downlink;
  - ground-derived/transformed;
  - non-LGC PCM/spacecraft telemetry or ground context.
- Updated GUIDO and CONTROL station specifications and the station research-status index.
- Kept both stations at maturity **B** because exact ground algorithms, non-LGC telemetry routing, refresh behavior, and console access remain incomplete.

### New research note

- `resources/research/032_apollo13_lm_crt_field_provenance.md`

### Next research

1. Locate RTCC/ground processing definitions for landing-radar coordinate conversion and PGNS/AGS comparison values.
2. Trace non-LGC telemetry feeding MSK 1137: actuator position, chamber pressure, voltages, temperatures, and related validity/status.
3. Complete MSK 1123 field-by-field provenance.
4. Continue CM MSK 683/966 transcription/comparison after the LM provenance chain is sufficiently constrained.


## 2026-09-11 — Apollo 13 PIPA-bias ground workflow

- Located a February 27, 1970 H-2 Lunar Surface Branch “Note of Interest” describing the intended Apollo 13 lunar-surface PIPA-bias calculation.
- Documented the ground inputs: MPAD lunar gravity, gimbal angles, GUIDO local-vertical attitude, and PIPA-derived measured gravity.
- Documented that launch-preparation bias measurements were intended to provide FIDO a PGNS delta-V error estimate.
- Cross-checked the operational significance against the Apollo 13 Mission Operations Report:
  - CSM GNC monitored bias before and after TLI and later updated a shifted Z-PIPA bias before entry;
  - late in the contingency, LM PGNS initialization included a check that PIPA bias “looked good” before the MCC-7 alignment/burn sequence.
- Added `resources/research/033_apollo13_pipa_bias_ground_workflow.md`.
- Updated GUIDO, FIDO, and the LM CRT provenance note.
- The source resolves one ground-computation path but does **not** yet establish the complete MSK 1137 BIAS/OCTAL display-routing or load-generation implementation.


## 2026-09-11 — MSK 1137 non-LGC telemetry provenance

### Completed

- Traced several Apollo 13 MSK 1137 hardware fields into named spacecraft telemetry measurements.
- LM-7/8/9 Elementary Functional Diagrams identify:
  - **GQ6510P** — DPS thrust-chamber pressure;
  - **GQ6806H** — variable-injector actuator position.
- Directly rendered the March 9, 1970 LM Data Book redline pages and verified:
  - **GN7563T** — LM-7 landing-radar antenna temperature;
  - **GN7723T** — rendezvous-radar antenna temperature for LM-6 and subsequent.
- The LR-temperature redline sheet explicitly warns that CRT readings may differ from heater trip values because instrumentation error is not included in the trip values.
- Cross-checked a NASA Apollo telemetry summary that maps:
  - GQ6806H;
  - GN7563T;
  - GN7723T;
  - PIPA power/telemetry-bias/IMU supply measurements;
  - PIPA temperature
  to primary MSK 1137.
- Kept the later telemetry summary classified as Apollo-wide/retrospective routing evidence rather than an Apollo-13-specific configuration source.
- Kept **GQ6510P → MSK 1137 TCP** provisional because the inspected routing row does not explicitly list 1137 even though the mission-era measurement identity and Apollo 13 field meaning match.

### New research note

- `resources/research/034_apollo13_msk1137_non_lgc_telemetry.md`

### Architecture consequence

MSK 1137 is now demonstrably a composite of:

1. LGC digital-downlink data;
2. PCM hardware/instrumentation measurements;
3. ground-derived/transformed products.

The simulator must preserve those origins rather than populate the CRT directly from one idealized subsystem state.

### Next work

1. Find Apollo-13-specific instrumentation definitions for the 1137 PGNCS power/PIPA fields and radar validity discretes.
2. Certify the thrust-chamber-pressure display routing.
3. Recover engineering conversions/display precision and CRT update cadence.
4. Repeat the field-provenance process for MSK 1123.


## 2026-09-11 — MSK 1137 identifier correction and handbook verification

- Corrected a research-note transcription error: the PIPA 120-VDC pulse-torque reference is **GG1040V**, not GG0104V.
- Confirmed GG1040V in both the LM Apollo Operations Handbook and the Apollo telemetry-summary routing table; the latter routes it to MSK 1137.
- Confirmed handbook identities for GG1110V, GG1201V, GG1331V, and GG2300T.
- Preserved an evidence-boundary warning: the searchable handbook pages carrying those telemetry identities are from a June 15, 1970 changed revision.
- Confirmed that the Apollo 13 Flight Journal preserves a **1970-02-01 LM-7 and Subsequent** handbook scan, but the 639-MB file exceeds the current web renderer. Direct verification of the corresponding preflight pages remains pending.
- No Apollo-13 mission-profile mapping was promoted solely from the later changed handbook revision.


## 2026-09-11 — MSK 1123 first provenance pass

### Completed

- Began a field-provenance reconstruction for **MSK 1123 — LM GUID, CONTROL AND PROP RT**.
- Separated the page into:
  - LGC/PGNS digital downlink;
  - PCM control-hardware measurements;
  - AGS/AEA telemetry/state;
  - radar data;
  - APS/RCS propulsion telemetry;
  - ground/context and processed values.
- Confirmed Apollo telemetry routing for:
  - GH1461V / GH1462V / GH1463V — RGA yaw/pitch/roll rates → 1123;
  - GG2219V and GH1457V attitude-error families → 1123;
  - GH1644X PGNS attitude-hold mode → 1123;
  - selected APS helium/valve/fuel-low channels → 1123.
- Preserved the mission-specific boundary: those routing tables are Apollo-wide/retrospective until the corresponding LM-7 source is verified.
- Identified the Apollo 13 Flight Crew G&N Dictionary / **AGS Flight Program 7** as the next best source for the 1123 AGS/DEDA section.

### New research note

- `resources/research/035_apollo13_msk1123_field_provenance.md`

### Next work

1. Extract Apollo 13 AGS Flight Program 7 / DEDA mappings from the mission-specific G&N Dictionary.
2. Verify LM-7 definitions for the currently Apollo-wide 1123 PCM channels.
3. Resolve radar field source paths and OCR-damaged RCS identifiers.


## 2026-09-11 — AGS Flight Program 7 / DEDA pass

### Completed

- Identified the Apollo 13 G&N Dictionary as the mission-specific AGS source, but its 36.9 MB scan exceeded the available PDF web reader.
- Directly rendered the TRW **LM PGNS/AGS Training Card** and extracted Flight Program 7 operational DEDA address families.
- Documented selector/address semantics for:
  - 400 submodes/alignment;
  - 404/405/406 delta-V reset;
  - 450–452 / 470–472 / 500–502 delta-V and velocity-monitor families;
  - 337R, 360R–362R, 367R, 377 navigation/time quantities;
  - 540–542 accelerometer bias;
  - 544–546 gyro drift;
  - 614R/616 ullage logic.
- Cross-checked against actual Apollo 13 flight operations:
  - 400+5 body-axis alignment and 400+0 attitude hold were used during contingency burns;
  - MCC-7 preparation explicitly called for zeroing 404/405/406 and selecting 470;
  - Haise reported a small pre-burn bias at address 470.
- Kept the evidence boundary explicit: operational DEDA semantics are now strong, but the exact AEA telemetry-to-MSK-1123 mapping is still unresolved.

### New research note

- `resources/research/036_apollo13_ags_fp7_deda_evidence.md`

### Next work

1. Find AEA/AGS telemetry documentation linking FP7 variables to LM PCM words/channels.
2. Map MSK 1123 AGS VEL / DEL VEL / ULL / ACT VEL to exact onboard/ground quantities.
3. Recover the Apollo 13 G&N Dictionary AGS pages through an alternate page-level/transcribed source if possible.


## 2026-09-11 — AGS telemetry and RTCC processing pass

### Completed

- Confirmed that the 1 February 1970 changed **LM-7 and Subsequent Apollo Operations Handbook** contains:
  - AEA input/output signal tables;
  - **AEA Telemetry Word List, Table 2.1-7**;
  - PGNS downlink sequence;
  - separate DEDA input/output/accessibility tables.
- Preserved the current extraction boundary: the exact Flight Program 7 telemetry word list has not yet been directly recovered, so earlier Flight Program 6 word assignments are not being reused as Apollo 13 facts.
- Documented the AEA telemetry architecture:
  - 50-word softwired telemetry block;
  - repeated once per second in general AGS documentation;
  - output word built from identification code + 18-bit AEA computer word.
- Explicitly separated the DEDA crew interface from the AEA ground-telemetry stream.
- Documented the Apollo 13 post-MCC-5 anomaly in which **RTCC incorrectly processed AGS body angles** while PTC was actually correct.
- Updated the simulation architecture so ground transformations can fail independently of spacecraft state and received telemetry.
- Updated GUIDO, CONTROL, roadmap, and station-status documentation.

### New research note

- `resources/research/037_apollo13_ags_telemetry_ground_processing.md`

### Next work

1. Recover the LM-7 Table 2.1-7 exact Flight Program 7 telemetry word list.
2. Compare it with the earlier FP6 list to identify software-version changes.
3. Map AEA telemetry words to MSK 1123 fields and ground coordinate transformations.
4. Use the Apollo 13 RTCC body-angle error as a future ground-processing validation case.


## 2026-09-11 — Apollo 13 G&N Dictionary indexed verification

- NASA's indexed text for the mission-specific Apollo 13 G&N Dictionary exposed key AGS Flight Program 7 entries directly.
- Corrected the Apollo 13 profile wording for **400 +30000** to **IMU Align**; the earlier “AGS/PGNS alignment” label came from later training-card continuity evidence.
- Directly verified from indexed mission-specific source text:
  - 400 selector modes;
  - 404/405/406 reset values and 470/471/472 measured-delta-V readouts;
  - 450–452 local-vertical delta-V;
  - 500–502 ΔVg;
  - 377 AGS computer time;
  - 540–542 accelerometer bias coefficients;
  - 544–546 gyro bias coefficients;
  - 547 lunar-align azimuth correction;
  - 614/616 ullage counters.
- Preserved the source-quality boundary: the large PDF still could not be rendered, so this is indexed-text verification rather than page-image verification.
- The AGS research target is now narrower: recover the **Flight Program 7 AEA telemetry word list** and connect it to MSK 1123.

## 2026-09-11 — FP7 telemetry continuity matrix

### Completed

- Compared the full 50-word telemetry regions in the surviving FP6 and FP8 AGS assembly listings.
- Confirmed both place the telemetry block at **0325–0406 octal**.
- Found symbol continuity at **49 of 50** positions; address **0371** differs between FP6 (`VT`) and FP8 (`VF`).
- Used the Apollo 13 G&N Dictionary to resolve mission-specific meaning for address 0371 and to verify or partially verify **25 of 50** candidate telemetry addresses overall.
- Added an evidence-status matrix rather than inferring the unresolved half of FP7.
- Kept telemetry ID ordering and all unresolved addresses unfrozen until the LM-7 Table 2.1-7 is directly recovered.

### New research notes

- `resources/research/038_apollo13_fp7_telemetry_continuity_bounds.md`
- `resources/research/039_apollo13_fp7_telemetry_candidate_matrix.md`

### Next work

1. Search Apollo 13 indexed material for unresolved addresses in the 0325–0406 block.
2. Recover the LM-7 Table 2.1-7.
3. Map verified AGS telemetry words into the AGS fields on MSK 1123, keeping RTCC transformations separate.


## 2026-09-11 — AGS attitude direction-cosine path

### Completed

- Traced the AGS attitude telemetry representation in surviving FP6/FP8 source listings.
- Confirmed that the telemetry block carries **six direction cosines**:
  - A11T/A12T/A13T — X-body row;
  - A31T/A32T/A33T — Z-body row.
- Confirmed the telemetry-initialize routine copies the current internal A11–A13 and A31–A33 values into those telemetry words.
- Cross-checked general AGS telemetry documentation stating that six direction cosines are snapshotted at the one-second telemetry-block boundary.
- Connected that architecture to Apollo 13's documented post-MCC-5 event in which RTCC incorrectly processed AGS body angles.
- Kept the exact RTCC conversion equation and FP7 word-ID certification unresolved rather than inferring them.

### New research note

- `resources/research/040_apollo13_ags_attitude_direction_cosine_path.md`

### Next work

1. Locate the RTCC/ground equation converting AGS direction cosines to body angles.
2. Recover LM-7 Table 2.1-7 to certify the FP7 telemetry IDs.
3. Map the final ground-derived angles into exact Apollo 13 MSK 1123 AGS ATT fields.


## 2026-09-11 — AGS delta-V interface separation

### Completed

- Distinguished the AEA telemetry delta-V variables from DEDA crew readouts:
  - VD1X/Y/Z (0404–0406): 40-ms body-axis sensed-velocity accumulation in telemetry;
  - VDX/Y/Z (0470–0472): 2-second navigation-update values exposed through DEDA 470–472.
- Verified the adjacent-program source-code relationship in which navigation logic copies VD1 into VDX.
- Retained Apollo 13 mission-specific validation for the DEDA side through the 404/405/406 → 470 contingency-burn procedure.
- Established that Mission Control's ground delta-V information need not depend on the crew's current DEDA selection.
- Kept the exact MSK 1123 AGS DEL VEL source unresolved pending MCC/RTCC display-routing evidence.

### New research note

- `resources/research/041_apollo13_ags_delta_v_interfaces.md`

### Next work

1. Trace MSK 1123 AGS DEL VEL into RTCC/display documentation.
2. Perform the same provenance analysis for AGS ULL.
3. Recover the exact FP7 telemetry table where possible.


## 2026-09-11 — AGS ullage provenance

### Completed

- Separated the AGS ullage chain into:
  - sensed X-axis delta-V / thrust acceleration;
  - per-cycle threshold qualification;
  - MU8 consecutive-cycle counter;
  - 1K9 completion limit;
  - ullage-acquired state;
  - controller-facing AGS ULL measurement.
- Confirmed adjacent-program code uses AT as the thrust-acceleration quantity compared with the ullage threshold.
- Confirmed MU8 is incremented only when the threshold is met and reset otherwise.
- Confirmed MU8/S12 is separately packaged for telemetry and DEDA 614/616 exposes the counter logic.
- Established that MSK 1123 AGS ULL, because it is a velocity-unit field, cannot simply be the counter/status value.
- Left the exact FP7 / MCC calculation source unresolved pending direct display-routing evidence.

### New research note

- `resources/research/042_apollo13_ags_ullage_provenance.md`

### Next work

1. Locate MCC/RTCC definitions for MSK 1123 AGS DEL VEL and AGS ULL.
2. Recover the exact LM-7 FP7 telemetry table where possible.
3. Continue converting the AGS portion of MSK 1123 into a field-by-field provenance specification.


## 2026-09-11 — MSK 1123 DEDA telemetry provenance

### Completed

- Traced the MSK 1123 AGS/DEDA block into explicit AEA telemetry variables:
  - RMF — readout-mode flag;
  - DD — most recent DEDA data;
  - CMF — clear-mode flag;
  - ADST — DEDA address.
- Verified those meanings in the AGS operating manual and corresponding FP6/FP8 source variables.
- Preserved the distinction between:
  - the astronaut's physical DEDA display;
  - AEA DEDA-processing state;
  - the AEA telemetry stream;
  - the Mission Control CRT representation.
- Confirmed that Apollo 13 MSK 1123 includes AGS DEDA information, while leaving exact mission-specific labels/masks and FP7 telemetry IDs unresolved.

### New research note

- `resources/research/043_apollo13_msk1123_deda_telemetry.md`

### Next work

1. Transcribe the exact Apollo 13 MSK 1123 DEDA block.
2. Recover FP7 Table 2.1-7 telemetry IDs.
3. Search Apollo 13 controller loops for actual use of the ground DEDA-status block.
4. Continue field-by-field AGS mapping for MSK 1123.


## 2026-09-11 — consolidated MSK 1123 AGS provenance

### Completed

- Consolidated the AGS portion of MSK 1123 into one field-oriented provenance matrix.
- Established strong source paths for:
  - AGS time;
  - RGA rates;
  - AGS body attitude;
  - AGS attitude error;
  - DEDA status.
- Refined strong candidates for:
  - ASA body rates;
  - AGS indicated velocity;
  - AGS measured delta velocity;
  - AGS ullage measurement.
- Corrected an overly narrow earlier delta-V assumption by restoring **DVX/DVY/DVZ (0350–0352)** as an important direct telemetry candidate alongside VD1 and DEDA VDX.
- Distinguished AEA analog attitude-error outputs from the separate AEA digital telemetry path.
- Preserved unresolved field mappings instead of forcing a one-source AGS display model.

### New research note

- `resources/research/044_apollo13_msk1123_ags_field_matrix.md`

### Next work

1. Locate MCC/RTCC definitions for AGS VEL / DEL VEL / ULL.
2. Recover exact FP7 Table 2.1-7.
3. Re-transcribe Apollo 13 MSK 1123 field masks/precision.
4. Verify LM-7 instrumentation calibration for attitude/rate channels.


## 2026-09-11 — MSK 1123 velocity semantics and mixed-source ground format

### Completed

- Added research note 045 to separate the adjacent velocity-related rows on MSK 1123 using AC/Delco Apollo 11/12 definitions:
  - **AGS VEL** — Abort Guidance System indicated velocity (`XXXX` ft/sec in the earlier definition family);
  - **LGC DEL VEL** — PIPA output for a 2-second interval (`XX.X` ft/sec);
  - **AGS DEL VEL** — Abort Guidance System measured velocity (`XX.X` ft/sec);
  - **AGS ULL** — Abort Guidance ullage measurement (`XX.X` ft/sec);
  - **ACT VEL** — accumulated velocity along thrust (`XX.X` ft/sec).
- Used the Apollo 12 source to resolve the OCR ambiguity around the **AGS ULL** label.
- Located and inspected J. L. Nevins' January 1970 MIT Instrumentation Laboratory report, which reproduces the 1123-style page as Figure 16(a), **Typical Data Format for Ground Consoles**, including the AEA/LGC/PCM header and the same AGS/LGC velocity rows.
- Documented the surrounding operational context: the ground compared onboard primary/backup guidance state with ground-tracking-derived information during powered descent and used a powered-flight processor for independent state estimation.
- Preserved the evidence boundary: these sources clarify field meaning and composite ground-console architecture, but they do **not** select the Apollo 13 FP7 telemetry word, establish the exact RTCC conversion, or prove that the AEA/LGC/PCM header boxes were dynamic validity/status indicators.
- Updated the display-status, station-status, roadmap, and source-catalog documentation accordingly.

### New research note

- `resources/research/045_msk1123_velocity_semantics_and_ground_format.md`

### Next work

1. Directly transcribe the Apollo 13 MSK 1123 velocity rows/masks from the mission-specific ASPO page.
2. Recover the LM-7 Table 2.1-7 Flight Program 7 telemetry list.
3. Locate MCC/RTCC definitions selecting or transforming AGS VEL / DEL VEL / ULL / ACT VEL.
4. Determine the runtime meaning, if any, of the AEA/LGC/PCM header boxes.


## 2026-09-11 — AEA telemetry-word-list recovery

### Completed

- Added research note 046 documenting recovery of the engineering structure of **Table 2.1-7 — Abort Electronics Assembly - Telemetry Word List**.
- Corrected the handbook chronology: the Apollo 13 **LM 7 and Subsequent** volume is **Basic Date 15 December 1968 / Change Date 1 February 1970**; the searchable **LM 10 and Subsequent** continuity copy is **Basic Date 1 February 1970 / Change Date 15 June 1970**.
- Used the searchable LM-10 table as explicit later-configuration continuity evidence rather than silently treating it as Apollo 13 flight authority.
- Recovered distinct AEA telemetry products including:
  - present LM inertial velocity, telemetry IDs 34–36 octal;
  - compensated 20-ms body-axis incremental velocity, IDs 24–26;
  - a dimensionless ullage counter, ID 37;
  - a separate three-word sensed body-axis velocity-increment family, IDs 60–62;
  - DEDA state, six attitude direction cosines, timing, and other AGS quantities.
- Confirmed from the table architecture that the controller-facing **AGS ULL** velocity field cannot simply be the telemetered ullage counter.
- Updated the roadmap, display reconstruction status, station research status, and primary source catalog.
- Kept GUIDO and CONTROL at maturity **B**.

### Evidence boundary

The table now answers much of **what AEA velocity information existed in telemetry**, but not **which transmitted quantity and ground transformation populated each MSK 1123 row**. The later LM-10 table still requires row-by-row comparison against the exact LM-7 flight-edition page before its complete word list can be promoted to Apollo 13 mission-specific status.

### Next work

1. Directly recover/inspect the LM-7 Table 2.1-7 page and compare it against the searchable LM-10 copy.
2. Search MCC/RTCC/display-format material for AGS VEL, AGS DEL VEL, AGS ULL, and ACT VEL selection/transformation rules.
3. Resolve which of the distinct incremental-velocity telemetry families feeds AGS DEL VEL.
4. Resolve the engineering calculation behind AGS ULL and ACT VEL.
5. Continue to keep telemetry membership, ground processing, and CRT formatting as separate evidence layers.


## 2026-09-12 — AGS ullage criterion and source chronology correction

### Completed

- Added `resources/research/047_ags_ullage_threshold_and_handbook_chronology.md`.
- Corrected the LM handbook chronology wherever the note-046 work had described the later LM-10 copy as sharing the LM-7 basic date.
- Added primary Grumman AGS specification evidence that ullage qualification requires accumulated **+X-axis velocity increment greater than 0.2 ft/s in each 2-second computer cycle for three consecutive cycles**.
- Cross-checked the later LM-10 handbook wording, which states the equivalent condition as average +X acceleration greater than **0.1 ft/s²** over the same 2-second cycle.
- Narrowed the strongest physical candidate behind MSK 1123 **AGS ULL** to a velocity-valued quantity in the two-second +X ullage-test chain.
- Preserved the evidence boundary: no source yet identifies the exact telemetry word or RTCC/display transformation used for AGS ULL.
- Preserved **AGS ULL** and **ACT VEL** as separate display parameters; their similar accumulated-velocity language is not sufficient evidence to merge them.
- Updated the roadmap, display reconstruction status, station research status, and source catalog.
- GUIDO and CONTROL remain maturity **B**.

### Next work

1. Recover/directly inspect the Apollo 13 LM-7 Table 2.1-7 page image and compare it row-by-row with the later LM-10 table.
2. Locate PHO/RTCC/display-format documentation mapping AEA telemetry into MSK 1123.
3. Resolve the exact AGS DEL VEL source selection.
4. Resolve the ground calculations for AGS ULL and ACT VEL.


## 2026-09-12 — Research sufficiency and first vertical-slice selection

### Completed

- Formalized a research-sufficiency rule so inaccessible, repeatedly searched, or low-impact historical gaps can be logged and deferred rather than blocking the project indefinitely.
- Determined that Phase 1 is **research-sufficient to proceed**, not historically exhaustive.
- Compared three first-slice candidates:
  - Apollo 13 oxygen-tank accident/immediate stabilization;
  - Apollo 13 PC+2 preparation/execution;
  - Apollo 11 powered descent.
- Selected **Apollo 13 PC+2 preparation/execution** as the first vertical slice because it provides the strongest current combination of primary-source coverage, meaningful controller interaction, bounded model scope, explicit decision criteria, and compatibility with the Apollo 13-era technical baseline.
- Recorded the choice as D-013.
- Added a controller action/rule matrix focused on PC+2 rather than continuing generic display archaeology.
- Deferred exact non-critical MSK 1123/1137 routing unless a PC+2 implementation dependency requires it.

### New/updated documents

- `resources/research/048_first_vertical_slice_candidate_assessment.md`
- `resources/research/049_pc2_controller_action_and_rule_matrix.md`
- `docs/scenarios/APOLLO13_PC2_VERTICAL_SLICE.md`
- `docs/PROJECT_PRINCIPLES.md`
- `docs/DECISIONS.md`
- `docs/ROADMAP.md`
- `docs/OPEN_QUESTIONS.md`
- `docs/SIMULATION_SCENARIO_RESEARCH.md`

### Architecture consequence

The active research question is no longer “can every Apollo 13 controller station be reconstructed completely?” It is now “what state, information products, rules and interactions are required to make the selected PC+2 slice historically operable?”


## 2026-09-12 — PC+2 initialization and nominal parameter contract

### Completed

- Used the Apollo 13 Mission Operations Report and technical air-ground chronology to freeze the nominal first-slice start at **77:55:00 GET**.
- Chose that boundary because the final P30 LM maneuver PAD begins at **77:55:24** while the air-ground link is still weak, preserving a real communications/readback task rather than beginning after all maneuver data are already established.
- Documented the final PC+2 maneuver PAD:
  - TIG 79:27:38.30 GET;
  - LVLH ΔV +833.0 / -50.9 / -213.9 ft/s;
  - resultant ΔV 861.5 ft/s;
  - expected perigee 20.5 nmi;
  - burn attitude 272° roll / 81° pitch;
  - two-jet, 10-second ullage;
  - documented throttle sequence.
- Preserved a critical frame distinction: the crew maneuver PAD's LVLH components are not the same quantities as GUIDO's PGNS/IMU velocity-to-be-gained values.
- Added planned/executed PGNS Vg and post-burn residuals as historical validation targets.
- Documented initial communications behavior: weak link after AOS, S-band power-amplifier increase, ranging/uplink availability, and crew reports as a separate information source from telemetry.
- Built the first implementation-oriented parameter dictionary, including mission, ground-trajectory, PGNS/LGC, AGS, DPS, RCS/attitude, electrical and communications state.
- Added source-layer, validity, sample/receive-time and data-age requirements so the nominal model does not structurally collapse physical state into perfect controller data.
- Explicitly declined to invent:
  - an exact RTCC Cartesian state vector at 77:55 before the trajectory propagator requires it;
  - exact nominal propulsion pressures where current sources provide only shutdown thresholds;
  - full consumables or noncritical MSK fields not needed for PC+2.

### New/updated documents

- `resources/research/050_pc2_initialization_and_nominal_validation.md`
- `docs/scenarios/APOLLO13_PC2_PARAMETERS.md`
- `docs/scenarios/APOLLO13_PC2_VERTICAL_SLICE.md`
- `docs/ROADMAP.md`
- `docs/STATION_RESEARCH_STATUS.md`
- `resources/PRIMARY_SOURCE_CATALOG.md`

### Nominal validation targets

The first deterministic run should reproduce at least:

- ignition: 79:27:38.30 GET;
- actual burn duration: 263.82 s;
- actual guided cutoff: 79:32:02.12 GET;
- target resultant ΔV: 861.5 ft/s;
- executed PGNS Vg approximately +742.21 / -425.88 / +91.04 ft/s;
- post-burn residuals approximately +1.0 / +0.3 / 0.0 ft/s;
- no shutdown-rule trigger in the nominal case;
- transition into LM power-down after burn verification.

### Next work

1. Define the nominal event/state transition model from 77:55 through 79:34.
2. Identify the smallest historical player-facing display/product set required by GUIDO, CONTROL, FIDO/RETRO, TELMU, INCO, FLIGHT and CAPCOM.
3. Map only those products onto the new parameter/source layers.
4. Determine the minimum numerical trajectory-state representation needed when the first propagator is implemented.


## 2026-09-12 — PC+2 executable nominal prototype

### Completed

- Added `docs/scenarios/APOLLO13_PC2_UPDATE_SEMANTICS.md` defining source/sample/receive/process/display timestamps, validity, and provenance without inventing unsupported CRT refresh rates.
- Added `src/apollo_mission_control/pc2_nominal.py`, a standard-library-only nominal domain prototype.
- Added `tests/test_pc2_nominal.py` with validation for event ordering, historical TIG/cutoff timing, nominal progression through residual review/power-down, and zero nominal shutdown-rule triggers.
- Kept the prototype explicitly bounded: it validates scenario/event architecture and the research fixture, not full spacecraft physics or RTCC dynamics.
- Preserved unsupported nominal engineering values as null/TBD rather than fabricating them.
- Confirmed that exact PC+2 GUIDO/CONTROL CRT refresh cadence remains unresolved and non-blocking.

### Next work

1. Add explicit throttle-phase events (minimum, 40 percent, maximum) and pre-ignition ullage transition to the nominal event fixture/state machine.
2. Add controller-product projection objects from authoritative state, carrying validity and provenance.
3. Add shutdown-rule evaluation as independent controller-observable conditions rather than a precomputed burn-abort flag.
4. Add the first nonnominal test only after the nominal path is deterministic and internally consistent.


## 2026-09-12 — PC+2 ullage and commanded throttle chronology

### Completed

- Added `resources/research/051_pc2_ullage_and_throttle_profile.md`.
- Verified from the final PC+2 maneuver instructions and air-ground record that the first-slice commanded procedure is:
  - manual two-jet ullage beginning at **TIG−10 s**;
  - minimum throttle at ignition;
  - 40-percent command at **TIG+5 s**;
  - 21 seconds at 40 percent;
  - maximum throttle for the remainder of the burn.
- Converted that into explicit nominal event times:
  - 79:27:28.30 — manual two-jet ullage begins;
  - 79:27:38.30 — ignition / minimum-throttle segment;
  - 79:27:43.30 — 40-percent command;
  - 79:28:04.30 — maximum-thrust command.
- Preserved the crew's later **79:27:51** 40-percent and **79:28:09** 100-percent reports as separate communication events rather than using them as physical transition timestamps.
- Reviewed NASA TM X-66935 / REPT-70-FC13-47-ADD-1 as a more detailed postflight propulsion source. Its rounded segment timing/timing convention is useful for future engine-response modeling but is not substituted into the high-precision Flight Control Division TIG/cutoff validation contract without reconciliation.
- Updated `data/scenarios/apollo13_pc2_nominal.json` to schema 0.2 with explicit ullage/throttle/voice events.
- Updated `src/apollo_mission_control/pc2_nominal.py` to represent ullage, throttle commands and crew-report events separately.
- Expanded `tests/test_pc2_nominal.py` to validate commanded-profile timing and the separation between command and voice-report chronology.
- Updated the PC+2 state-machine document, roadmap, CONTROL station-status note, and primary source catalog.

### Evidence boundary

The executable prototype currently models **commanded/procedural throttle phases**, not a fully sourced physical DPS transient. Command, engine response, telemetry indication and crew voice report remain separate layers. Detailed ramp/lag dynamics are deferred until a controller decision, transient model, or failure case requires them.

### Validation note

The test suite was expanded in this pass, but local test execution could not be completed because the container-backed repository checkout failed in the tool environment. No claim is made here that the updated tests were executed successfully.

### Next work

1. Add controller-product projection objects from authoritative state with sample/receive time, validity, age and provenance.
2. Implement independent shutdown-rule evaluation over controller-observable conditions rather than a precomputed `burn_abort` flag.
3. Add the first nonnominal validation case only after the nominal information/rule path is complete.
4. Defer the minimum numerical trajectory-state implementation until the first propagator actually requires it.
