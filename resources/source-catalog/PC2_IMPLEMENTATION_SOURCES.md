# PC+2 Implementation Source Catalog Supplement

Status: **active supplement to `resources/PRIMARY_SOURCE_CATALOG.md`**  
Scope: sources used directly for the Apollo 13 PC+2 executable information-product and shutdown-rule layers.

This supplement exists so implementation-specific additions can remain small and reviewable while the master catalog continues to hold the full project source inventory. Entries should be folded into the master catalog when that file is next comprehensively edited.

## AS-508 MCC/MSFN Mission Configuration/System Description

- **Mission:** Apollo 13 / AS-508
- **Organization:** Manned Spacecraft Center, Flight Support Division
- **Date:** March 1970
- **NASA document ID:** 19700024253
- **Report:** NASA-TM-X-64290
- **URL:** https://ntrs.nasa.gov/citations/19700024253
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-PARTIAL
- **Use in current implementation:** establishes the Apollo 13-era command, communications, telemetry, tracking, and MCC interface architecture underlying the separation between authoritative spacecraft state and controller-facing products.
- **Research record:** `resources/research/052_pc2_controller_product_projection.md`.

## Mission Operations Report — Apollo 13

- **Organization:** NASA Flight Control Division, Manned Spacecraft Center
- **Date:** 1970-04-28
- **URL:** https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-DETAILED for PC+2
- **Use in current implementation:** controller responsibilities, PC+2 chronology, maneuver parameters, shutdown criteria, ground/onboard threshold distinctions, ground-only differential-pressure callout, conditional engine-restart rule, and the conjunctive ISS-warning + program-alarm criterion.
- **Research records:** `resources/research/049_pc2_controller_action_and_rule_matrix.md` through `054_pc2_iss_warning_observation_path.md`.

## Apollo 13 Technical Air-to-Ground Voice Transcription — PC+2 interval

- **Source:** NASA technical air-to-ground transcription preserved through the Apollo 13 Flight Journal document collection
- **Index:** https://apollojournals.org/afj/ap13fj/a13-documents.html
- **PC+2 rule/readback navigation:** https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-DETAILED for relevant PC+2 intervals
- **Use in current implementation:** distinguishes crew readbacks/reports from physical spacecraft event time; confirms crew-side shutdown thresholds, ground-only delta-P callout, warning combinations, and restart procedure.
- **Important conflict preserved:** crew readback attaches the startup-transient exception to attitude error, while the Mission Operations Report wording attaches it to attitude rate. The implementation does not silently choose between them.
- **Research record:** `resources/research/053_pc2_shutdown_rule_evaluation.md`.

## Apollo Operations Handbook — Lunar Module, GN&CS

- **Title family:** *Apollo Operations Handbook, Lunar Module, Volume I — Subsystems Data*
- **Organization:** Grumman
- **Document family:** LMA790-3-LM
- **Public searchable copy:** LM-10 and subsequent, Basic Date 1970-02-01
- **URL:** https://www.ibiblio.org/apollo/Documents/LMA790-3-LM10-ApolloOperationsHandbookLunarModuleLM10AndSubsequent-Volume1-SubsystemsData-SearchableText.pdf
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-PARTIAL
- **Current use:** GN&CS Figure 2.1-33 shows distinct `ISS WARNING SIGNAL` and `LGC WARNING SIGNAL` paths from the display/keyboard assembly to the Instrumentation Subsystem. This supports modeling ISS warning as a discrete onboard/telemetry observation rather than a generic guidance-health diagnosis.
- **Configuration caution:** Apollo 13 flew LM-7. The later searchable LM-10 copy is used only for signal-path architecture consistent with Apollo 13 mission-rule wording; it is not used to assert exact LM-7 telemetry-word assignment or GUIDO CRT placement.
- **Research record:** `resources/research/054_pc2_iss_warning_observation_path.md`.

## LUMINARY PGNCS functional-description material

- **Public document:** `sundance_functional_description_vol1.pdf` in the Virtual AGC document collection
- **URL:** https://www.ibiblio.org/apollo/Documents/sundance_functional_description_vol1.pdf
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-PARTIAL
- **Current use:** contemporary LM PGNCS caution/warning description supports treating ISS warning and LGC warning as distinct onboard indications and describes ISS warning as being under LGC program control.
- **Caution:** not used to assign a hypothetical PC+2 failure mechanism or program-alarm number.
- **Research record:** `resources/research/054_pc2_iss_warning_observation_path.md`.

## Apollo Experience Report — Real-Time Display System

- **Title:** Apollo Experience Report: Real-Time Display System
- **Authors:** C. J. Sullivan and L. W. Burbank
- **NASA document ID:** 19760024152
- **Report:** NASA-TN-D-8316 / JSC-S-461
- **Publication date:** 1976-09-01
- **URL:** https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19760024152.pdf
- **Status:** REVIEWED-PARTIAL / ARCHITECTURE SUPPORT
- **Use in current implementation:** supports the Apollo-wide architectural separation between data acquisition/processing and controller display subsystems.
- **Caution:** retrospective Apollo Experience Report; it does not establish exact Apollo 13 PC+2 CRT layouts or refresh cadence and is not used to invent either.
- **Research record:** `resources/research/052_pc2_controller_product_projection.md`.
