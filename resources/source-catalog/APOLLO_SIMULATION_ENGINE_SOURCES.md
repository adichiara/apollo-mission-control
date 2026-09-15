# Apollo Simulation-Engine Sources

Status: active source catalog for the project's causal simulation-engine architecture.

This catalog separates evidence about how Apollo simulation/training worked from project architecture decisions. It does not imply that the original simulator software or complete mathematical models have been recovered.

## NASA TN D-7290 — *Apollo Experience Report: Simulation of Manned Space Flight for Crew Training*

- Authors: C. H. Woodling et al.
- NASA/JSC, 1973.
- NTRS document ID: `19730011149`.
- NTRS record: https://ntrs.nasa.gov/citations/19730011149
- Evidence use: Apollo crew-training mission simulators; functional uses, characteristics, development experience, and fidelity evolution.
- Status: identified/reviewed at report-record level; detailed simulator internals remain a target for deeper extraction.

## NASA TN D-7436 — *Apollo Experience Report: Systems and Flight Procedures Development*

- Author: P. C. Kramer.
- NASA/JSC, 1973.
- NTRS document ID: `19730023040`.
- NTRS record: https://ntrs.nasa.gov/citations/19730023040
- Evidence use: mission-simulation procedure verification; coupling of the Apollo mission simulator to simulated MSFN/MCC functions; coverage of spacecraft trajectories, telemetry, uplink/voice communications, and major spacecraft systems operations.
- Key boundary: NASA describes the Apollo mission simulator as the highest-fidelity spacecraft simulator available for mission simulation, used together with Mission Control for procedure verification and training.

## NASA TN D-7287 — *Apollo Experience Report: Guidance and Control Systems—Engineering Simulation Program*

- Author: David W. Gilbert.
- NASA/JSC, 1973.
- NTRS document ID: `19730016146`.
- NTRS record: https://ntrs.nasa.gov/citations/19730016146
- Evidence use: real-time engineering simulation; use of general-purpose analog/digital computing, subsystem hardware, special interfaces, and large hybrid mission-evaluation simulators for closed-loop verification.
- Key boundary: this is engineering-simulation evidence, not a direct software listing for the crew-training mission simulator, but it confirms that Apollo system behavior was modeled causally rather than only replayed as scripted event sequences.

## NASA Apollo training overview, 1964

- NTRS document ID: `19660019476`.
- NTRS PDF: https://ntrs.nasa.gov/api/citations/19660019476/downloads/19660019476.pdf
- Evidence use: description of planned Apollo mission simulators.
- Relevant evidence: the command-module controls, displays, and window scenes were to be active and driven closed-loop by peripheral computing equipment; the instructor console was to include duplicate displays and malfunction-insertion units.
- Key boundary: early-program description; later mission-specific implementation details may differ.

## AIAA Paper 65-266 — *Integrated Operating Mode of the Apollo Mission Simulator*

- Authors: F. O. Martikan and S. H. Nassiff.
- 1965.
- NTRS document IDs: `19650039405` / `19660033487`.
- NTRS records:
  - https://ntrs.nasa.gov/citations/19650039405
  - https://ntrs.nasa.gov/citations/19660033487
- Evidence use: integrated Apollo mission simulator/Mission Control training concept.
- Status: record identified; public full text not currently recovered through NTRS.

## NASA TN D-7822 — *Apollo Experience Report: The Role of Flight Mission Rules in Mission Preparation and Conduct*

- Author: L. W. Keyser.
- NASA/JSC, 1974.
- NTRS document ID: `19750002893`.
- NTRS record: https://ntrs.nasa.gov/citations/19750002893
- Evidence use: mission-rule development and controller training, including training for nonnominal situations for which no complete response had been preplanned.
- Architecture relevance: supports a simulator that allows controllers to reason through consequences rather than merely select the one expected historical branch.

## *Proposal for LEM Mission Simulator, Volume II, Technical Addendum: Glossary of Symbols*

- Organization: Link Group — Systems Division, General Precision, Inc.
- Public scan: https://www.ibiblio.org/apollo/Documents/proposal_for_lem_mission_simulator_vol2.pdf
- Discovery/catalog context: Virtual AGC document library, which notes that the document contains many flowcharts showing the mathematical equations underlying the LMS.
- Evidence use: direct LMS mathematical-model architecture, equation/flowchart families, variables, subsystem coupling, and abstraction choices.
- Status: **public digital copy located; high-priority extraction target**.
- Key boundary: a simulator-design source, not automatically Apollo-13-specific vehicle configuration. Every equation/constant/configuration adopted by the project still requires applicability review.

## *Lunar Module Mission Simulator Instructor's Handbook, Volume I — Simulator Description*

- Organization: Grumman / LMS program documentation lineage; exact scan metadata to be captured during extraction.
- Public scan: https://www.ibiblio.org/apollo/Documents/lms_instructors_handbook_vol1.pdf
- Archive index: https://ibiblio.org/apollo/Documents/
- Evidence use: simulator subsystem representation, controls/displays, and how individual spacecraft subsystems were simulated.
- Status: **public digital copy located; direct extraction pending**.
- Architecture relevance: likely complements the technical-addendum equations with subsystem-level functional descriptions.
- Identity boundary: this is a separate LMS source; do not conflate it with the 1965 AMS Volume II scan.

## *Lunar Module Mission Simulator Instructors Handbook, Volume II*, LMA790-2-LMS

- Date: 1 April 1967.
- Independent NASA citation: NTRS `19700026546`, *LM Descent/Phasing Summary Document*, references Volume II, Sections II and III.
- NTRS PDF: https://ntrs.nasa.gov/api/citations/19700026546/downloads/19700026546.pdf
- Evidence use: LMS operating/instructor procedures and simulator behavior lineage.
- Status: handbook lineage independently confirmed by NASA source; exact public scan/sections remain an extraction target.

## North American Aviation — *Preliminary Apollo Mission Simulator Instructor Handbook, Volume II: Operation & Utilization*

- Document: `SM6T-2-02` / `SID 65-974-2`.
- Date: 1 July 1965.
- Contract: NAS 9-150.
- Public primary-source scan: https://ibiblio.org/apollo/Documents/19730060784_1973060784.pdf
- Evidence use:
  - five operational-program classes: vehicle dynamics, vehicle systems, simulation effects, simulator control, and Mission Simulation Control Center interface;
  - equations-of-motion outputs feed subsequent inputs and drive onboard, instrument, and visual simulations;
  - manual, preprogrammed, and time-dependent malfunction insertion;
  - physical/system-derived telemetry plus the ability to inject a telemetry malfunction directly;
  - Volume III described as containing complete simulated-malfunction and simulation-output tables, including program/math-model designators.
- Architecture relevance: direct primary evidence for causal feedback, simulator model partitioning, output variables, external interfaces, and separate physical/observation failure paths.
- Key boundaries: this is the **AMS**, not LMS, handbook; it is preliminary initial-configuration material and explicitly not design-requirements data. Later accepted, Block II, and Apollo-13 behavior must be checked before importing details.
- Detailed extraction: `resources/research/135_public_ams_instructor_handbook_extraction.md` and `resources/research/215_ams_model_partition_malfunction_boundaries.md`.
- Architecture extraction now additionally records the five-program partition, subsystem-normal/malfunctioned real-time behavior, manual/preprogrammed/time-dependent malfunction insertion, multi-code realization of one training malfunction, and telemetry-channel fault insertion as a distinct layer.

## Virtual AGC document-library continuity

Virtual AGC has continued adding simulator material. Its 2025 additions include improved scans of AMS instructor-handbook volumes and note that one volume includes a complete simulator-output listing, giving insight into the level at which each subsystem was simulated.

- Library/change log: https://www.ibiblio.org/apollo/changes.html
- Evidence use: discovery index and scan provenance, not a substitute for the underlying primary documents.

## Grumman LED-440-3 — *LEM Mission Simulator (LMS) Math Model: True Motion Equations*

- Date: August 1965.
- Organization: Grumman Aircraft Engineering Corporation.
- Report identity: cited as part 1 of 3 by Brian Woycechowsky's 2021 *Lunar Module Moon-Referenced Equations of Motion*.
- Former public-file reference: `1965-08-LEM-Mission-Simulator-Math-Model-1-130-1-65.pdf` at TechWorks.
- Evidence use: source-attributed true-motion model partition and interfaces among propulsion thrust, Stabilization and Control thrust direction, Weight and Balance mass/inertia/center-of-gravity state, RCS thrust, slosh, stage separation, ephemeris/gravity, and translational/rotational integration.
- Status: original report identity and a modern technical reconstruction are located; the primary three-part report still requires direct page extraction.
- Key boundary: Woycechowsky's reconstruction is an extraction/provenance aid, not a replacement for the original Grumman report.
- Relationship to LED 500-5: unresolved; do not treat the two report identities as equivalent without documentary evidence.
- Reconstruction/extraction aid: https://static1.squarespace.com/static/567433669cadb6ac8da3ff92/t/6071a7ea04f3ed70ebd956f0/1618061309500/lunar%2Bv6.0%2B%2Bincl%2Bcover%2Bsupplement%2B%2B%2Bfront%2Bmatter.pdf

## Grumman LED 500-5 — *LMS Math Model — Equations of Motion, Subsystem Interfaces and Visual Display Drive Equations*

- Date: 22 April 1965.
- MSC accession: *66-10469.
- Contract: NAS 9-1100.
- Archive evidence: NASA/NARA corporate index preserved by Virtual AGC.
- Evidence use: direct LMS mathematical-model lineage covering equations of motion, subsystem interfaces, and visual-display drive equations.
- Status: title/date/accession verified in archive index; full report extraction remains pending.
- Architecture relevance: strongest current direct evidence that the LMS separated dynamic equations, subsystem coupling, and display-drive mathematics.

## Grumman LED 500-16 — *LEM Guidance Computer (LGC) Math Model for the Full Mission Engineering Simulator (FMES) and LEM Mission Simulator (LMS)*

- Date: 8 June 1966.
- MSC accession: *66-13246.
- Contract: NAS 9-1100.
- Archive evidence: NASA/NARA corporate index preserved by Virtual AGC.
- Evidence use: dedicated LGC model boundary shared by FMES and LMS.
- Status: title/date/accession verified; full report not yet recovered.

## Grumman 1965 — *Effect of LMS Fifty-Millisecond Integration Steps on Simulated Response of Abort Attitude Control System*

- Archive listing: TechWorks archival-document catalog.
- Evidence use: numerical-integration fidelity and timestep sensitivity in the LMS.
- Status: exact report contents not yet extracted.
- Key boundary: the title supports only that a 50 ms LMS integration step was studied for its effect on simulated AACS response. It does **not** establish a global LMS timestep or require this project to use 50 ms.

## Modern implementation references — Orbiter and Project Apollo–NASSP

These projects are **not historical Apollo evidence**. They are implementation-review, source-discovery, and potential comparison resources.

### Orbiter

- Repository: https://github.com/orbitersim/orbiter
- Technical reference: https://github.com/orbitersim/orbiter/blob/main/Doc/Orbiter%20Technical%20Reference/dynamics.tex
- License: MIT for the core repository.
- Use: integration methods, timestep/convergence questions, translational/rotational state contracts, and independent trajectory comparisons.
- Boundary: no dependency or code adoption is currently approved.

### Project Apollo–NASSP

- Project: https://nassp.space/index.php/Main_Page
- Repository: https://github.com/orbiternassp/NASSP
- License: GPL-2.0 lineage.
- Use: implementation reconnaissance, missing-mechanism review, and discovery of primary-document citations.
- Boundary: do not copy NASSP code or inherit its constants. Reviewed LM DPS code contains explicit approximations and TBD behavior; every candidate equation/value must be traced to a primary source.

Detailed assessment: `resources/research/136_orbiter_nassp_reference_assessment.md`.

## Apollo Operations Handbooks and subsystem engineering reports

The mission-simulator documents establish the need for causal/closed-loop behavior but do not by themselves provide every subsystem equation or failure consequence. The project should continue using mission-specific or vehicle-specific sources for physical mechanisms, including:

- Apollo Operations Handbook LM/CSM systems descriptions and operational procedures;
- subsystem specifications and malfunction procedures;
- Apollo Experience Reports for propulsion, electrical, guidance/control, communications, instrumentation, etc.;
- telemetry/instrumentation documentation where observation behavior matters;
- mission rules and controller console documentation for controller interpretation/action boundaries.

## Current evidence conclusion

The surviving Apollo documentation now does more than merely support a generic closed-loop architecture. A direct **LEM Mission Simulator mathematical-model source has been located**, alongside simulator-description and instructor-handbook lineages that can expose subsystem abstraction and malfunction behavior.

The project still should not claim recovery of the complete Apollo simulator software/model. The LED-440-3 reconstruction now constrains a separable propulsion/control/mass-properties/true-motion interface, but the original report and Apollo 13 profile inputs remain unextracted. The next research step is direct LMS/AMS model-document extraction and cross-checking against Apollo 13 LM-7/CSM spacecraft documentation before freezing equations, constants, coordinate frames, or historical acceptance tolerances.
