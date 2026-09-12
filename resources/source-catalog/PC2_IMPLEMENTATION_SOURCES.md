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
- **Use in current implementation:** controller responsibilities, PC+2 chronology, maneuver parameters, shutdown criteria, ground/onboard threshold distinctions, ground-only differential-pressure callout, and conditional engine-restart rule.
- **Research records:** `resources/research/049_pc2_controller_action_and_rule_matrix.md`, `050_pc2_initialization_and_nominal_validation.md`, `051_pc2_ullage_and_throttle_profile.md`, `052_pc2_controller_product_projection.md`, `053_pc2_shutdown_rule_evaluation.md`.

## Apollo 13 Technical Air-to-Ground Voice Transcription — PC+2 interval

- **Source:** NASA technical air-to-ground transcription preserved through the Apollo 13 Flight Journal document collection
- **Index:** https://apollojournals.org/afj/ap13fj/a13-documents.html
- **PC+2 rule/readback navigation:** https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
- **Status:** IMPLEMENTATION-SOURCE / REVIEWED-DETAILED for relevant PC+2 intervals
- **Use in current implementation:** distinguishes crew readbacks/reports from physical spacecraft event time; confirms crew-side shutdown thresholds, ground-only delta-P callout, warning combinations, and restart procedure.
- **Important conflict preserved:** crew readback attaches the startup-transient exception to attitude error, while the Mission Operations Report wording attaches it to attitude rate. The implementation does not silently choose between them.
- **Research record:** `resources/research/053_pc2_shutdown_rule_evaluation.md`.

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
