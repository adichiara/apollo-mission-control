# PC+2 Implementation Source Catalog Supplement

Status: **active supplement to `resources/PRIMARY_SOURCE_CATALOG.md`**  
Scope: sources used directly for the Apollo 13 PC+2 executable information-product, shutdown-rule, and scenario-injection layers.

This supplement exists so implementation-specific additions can remain small and reviewable while the master catalog continues to hold the full project source inventory. Entries should be folded into the master catalog when that file is next comprehensively edited.

## AS-508 MCC/MSFN Mission Configuration/System Description

- **Mission:** Apollo 13 / AS-508
- **Organization:** Manned Spacecraft Center, Flight Support Division
- **Date:** March 1970
- **NASA document ID:** 19700024253
- **Report:** NASA-TM-X-64290
- **URL:** https://ntrs.nasa.gov/citations/19700024253
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-PARTIAL
- **Use:** Apollo 13-era command, communications, telemetry, tracking, and MCC interface architecture underlying the separation between authoritative state and controller products.
- **Research record:** `resources/research/052_pc2_controller_product_projection.md`.

## Mission Operations Report — Apollo 13

- **Organization:** NASA Flight Control Division, Manned Spacecraft Center
- **Date:** 1970-04-28
- **URL:** https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-DETAILED for PC+2
- **Use:** controller responsibilities, PC+2 chronology, maneuver parameters, shutdown criteria, ground/onboard threshold distinctions, simulation-support categories, ground-only differential-pressure callout, conditional engine-restart rule, conjunctive ISS-warning + program-alarm criterion, approximately 85-psi ground chamber-pressure criterion, singular 150-psi ground inlet-pressure criterion, and >25-psi fuel/oxidizer differential-pressure criterion.
- **Research records:** `resources/research/049_pc2_controller_action_and_rule_matrix.md` through `058_pc2_fuel_oxidizer_delta_p_observation_path.md`.

## Apollo 13 Technical/PAO Air-to-Ground Transcription — PC+2 interval

- **Source:** NASA Apollo 13 air-ground/PAO transcription
- **NASA PDF:** https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- **Navigation copy:** https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-DETAILED for relevant intervals
- **Use:** separates crew reports from physical event time; confirms crew-side thresholds, the >25-psi fuel/oxidizer ΔP criterion as a ground-only callout, warning combinations, and restart procedure.
- **Conflict preserved:** crew readback attaches the startup-transient exception to attitude error, while the Mission Operations Report wording attaches it to attitude rate.
- **Research records:** `resources/research/053_pc2_shutdown_rule_evaluation.md`, `058_pc2_fuel_oxidizer_delta_p_observation_path.md`.

## Apollo 11 Final Flight Mission Rules

- **Organization:** NASA Manned Spacecraft Center
- **Mission:** Apollo 11
- **Relevant revision:** 3 Jul 1969 LOI rule summary
- **URL:** https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf
- **Status:** CONTINUITY / RULE-FAMILY EVIDENCE
- **Use:** contemporary LOI Mode I rule-family evidence. The revised LOI rule treats fuel-oxidizer ΔP as a distinct propulsion criterion and requires confirmation by chamber-pressure drop.
- **Caution:** Apollo 11's 20-psi threshold and confirmation logic are **not** imported into Apollo 13 PC+2. Apollo 13 mission-specific sources establish the applicable >25-psi ground-callout criterion.
- **Research record:** `resources/research/058_pc2_fuel_oxidizer_delta_p_observation_path.md`.

## Apollo 13 Simulator Discrepancy Reports — LUM 131 Rev. 8

- **Document type:** contemporaneous Grumman/NASA simulator engineering discrepancy reports
- **Relevant report:** `LM-LUM-31`, test `H20T-7.2 #1`, dated 27 Jan 1970
- **Program/configuration:** LUM 131 Rev. 8
- **Public scan:** https://www.ibiblio.org/apollo/Documents/apollo_13_simulator_discrepencies.pdf
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-PARTIAL
- **Current use:** primary architecture evidence that a simulated initiating condition could produce multiple dependent onboard/control/navigation/display effects. The reviewed case tests a hardware restart and records changed P20 navigation-update frequency, changed P32 inputs/computations, and a temporary rate-command control reversal.
- **Caution:** this is simulator engineering/discrepancy evidence, not a reconstructed integrated SimSup mission scenario. The project does not infer undocumented malfunction codes, operator UI, or exact injection syntax from it.
- **Research record:** `resources/research/056_pc2_scenario_injection_architecture.md`.

## Lunar Module 7, 8 & 9 Elementary Functional Diagrams

- **Vehicle family:** LM-7 / LM-8 / LM-9; Apollo 13 flew LM-7
- **Public scan:** https://www.ibiblio.org/apollo/Documents/lm-7%2C8%2C9_elementary_functional_diagrams.pdf
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-PARTIAL
- **Use:** mission-era vehicle-family measurement identities for `GQ6510P — PRESS, THRUST CHAMBER`, `GQ3611P — PRESS ENGINE INTERFACE FUEL`, and `GQ4111P — PRESS, ENGINE INTERFACE OXID`.
- **Caution:** does not by itself prove exact Apollo 13 PCM words, ground engineering conversions, CONTROL display routing, or the transformation used to form the PC+2 fuel/oxidizer ΔP product.
- **Research records:** `resources/research/034_apollo13_msk1137_non_lgc_telemetry.md`, `055_pc2_dps_chamber_pressure_observation_path.md`, `057_pc2_dps_inlet_pressure_observation_path.md`, `058_pc2_fuel_oxidizer_delta_p_observation_path.md`.

## Apollo 10 LM-4 Descent Propulsion System Final Flight Evaluation

- **Organization:** TRW Systems / NASA Manned Spacecraft Center
- **Date:** 1969-08-08
- **Report:** 11176-H314-R0-00
- **NASA document ID:** 19690026326
- **PDF:** https://www.nasa.gov/wp-content/uploads/static/history/afj/ap10fj/pdf/19690026326_a10-lm4-dps-final-flight-eval-trw-19690808.pdf
- **Status:** IMPLEMENTATION-SOURCE / CONTINUITY EVIDENCE
- **Use:** independently documents `GQ6510P` as engine thrust-chamber pressure and documents fuel/oxidizer interface-pressure measurements.
- **Configuration caution:** Apollo 10 flew LM-4; its flight-evaluation sampling rate is not imported as Apollo 13 PCM or CRT cadence.
- **Research record:** `resources/research/055_pc2_dps_chamber_pressure_observation_path.md`.

## Apollo 13 Mission Report

- **Organization:** NASA Manned Spacecraft Center
- **Date:** September 1970
- **NASA document ID:** 19710003598
- **Report:** NASA-TM-X-66449 / MSC-02680
- **URL:** https://ntrs.nasa.gov/citations/19710003598
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-PARTIAL
- **Use:** supports normal descent-propulsion operation apart from the supercritical-helium anomaly; does not supply an exact nominal PC+2 chamber-pressure trace.
- **Research record:** `resources/research/055_pc2_dps_chamber_pressure_observation_path.md`.

## Apollo 13 Investigation Team, Panel 3 — Addendum 1

- **Title:** *Analysis of Apollo 13 lunar module systems during emergency operation following command service module oxygen tank explosion*
- **Organization:** NASA Manned Spacecraft Center
- **Date:** June 1970
- **NASA document ID:** 19710010487
- **Reports:** NASA-TM-X-66935 / REPT-70-FC13-47-ADD-1
- **URL:** https://ntrs.nasa.gov/citations/19710010487
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-PARTIAL
- **Use:** Apollo 13-specific LM systems/propulsion post-mission evidence, including indexed analog-recording material for DPS firings; does not justify inventing a nominal GQ6510P value throughout PC+2.
- **Research records:** `resources/research/051_pc2_ullage_and_throttle_profile.md`, `055_pc2_dps_chamber_pressure_observation_path.md`.

## Apollo Operations Handbook — Lunar Module, GN&CS

- **Organization:** Grumman
- **Document family:** LMA790-3-LM
- **Searchable continuity copy:** LM-10 and subsequent, Basic Date 1970-02-01
- **URL:** https://www.ibiblio.org/apollo/Documents/LMA790-3-LM10-ApolloOperationsHandbookLunarModuleLM10AndSubsequent-Volume1-SubsystemsData-SearchableText.pdf
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-PARTIAL
- **Use:** GN&CS Figure 2.1-33 shows distinct `ISS WARNING SIGNAL` and `LGC WARNING SIGNAL` paths to the Instrumentation Subsystem.
- **Configuration caution:** Apollo 13 flew LM-7; not used to assert exact LM-7 telemetry-word assignment or GUIDO CRT placement.
- **Research record:** `resources/research/054_pc2_iss_warning_observation_path.md`.

## LUMINARY PGNCS functional-description material

- **Public document:** `sundance_functional_description_vol1.pdf`
- **URL:** https://www.ibiblio.org/apollo/Documents/sundance_functional_description_vol1.pdf
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-PARTIAL
- **Use:** supports treating ISS and LGC warnings as distinct onboard indications and describes ISS warning as under LGC program control.
- **Caution:** not used to invent a PC+2 failure mechanism or program-alarm number.
- **Research record:** `resources/research/054_pc2_iss_warning_observation_path.md`.

## Apollo Experience Report — Real-Time Display System

- **Authors:** C. J. Sullivan and L. W. Burbank
- **NASA document ID:** 19760024152
- **Report:** NASA-TN-D-8316 / JSC-S-461
- **Publication date:** 1976-09-01
- **URL:** https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19760024152.pdf
- **Status:** REVIEWED-PARTIAL / ARCHITECTURE SUPPORT
- **Use:** Apollo-wide architectural separation between acquisition/processing and controller display subsystems.
- **Caution:** retrospective; does not establish exact Apollo 13 PC+2 CRT layouts or refresh cadence.
- **Research record:** `resources/research/052_pc2_controller_product_projection.md`.
