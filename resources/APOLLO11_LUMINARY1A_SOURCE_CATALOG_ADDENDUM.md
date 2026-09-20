# Apollo 11 / Luminary 1A source-catalog addendum

Date: 2026-09-20

## Controlled source chain

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Mission G rendezvous report | References *Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program*, May 1969 | Primary mission-period evidence for the Luminary 1A equation document. |
| LUMINARY 099 `SERVICER.agc` / `POWERED_FLIGHT_SUBROUTINES.agc` | SETPOS, measurement-epoch capture, beam transform, propagation, qualification, update; SM/NB transform semantics | Apollo-11-effective estimator chain authority. |
| LUMINARY Memo #95 and LM-5 Mission G prelaunch load | Antenna→NB rotation semantics and position-specific `LRALPHA/LRBETA` | Apollo-11 mission/configuration authority. |
| AC Electronics, *Apollo 11 Guidance and Navigation System Manual* | 2-second LR component schedule; ASPO 45 MSK-1137 LR field definitions; MSK-1137 visibly distinguishes `D/L` and `RTCC` source categories; `ACT ΔV` identified as ground computed | Apollo-11-effective onboard cadence, field semantics, and mixed-provenance boundary; not a per-field routing table or MCC display cadence. |
| NASA, *Apollo 11 Mission Report*, MSC-00171, Nov 1969 | During powered descent, crew LR incorporation decision used reasonability/precalculated limits; convergence verified after incorporation; AGS was not LR-updated | Apollo-11-effective operational acceptance/convergence authority. Does not establish GUIDO ownership, display routing, or MCC cadence. |
| NASA, *Apollo 11 AS-506 Mission Operation Report*, M-932-69-11 | Distinct CCATS, RTCC, Display/Control, MOCR/SSR elements | Apollo-11-effective architecture authority; not exact per-field routing/timing. |
| NASA NTRS 19700004489, table reproducing GAEC specification LSP-470-2D, *Master End Item Specification for Lunar Module* | Landing-radar 3-sigma range limits plus altitude-banded velocity accuracy to LGC: 25K–2K ft Vx `1.5%/1.5 ft/s`, Vy `2.0%/2.0`, Vz `2.0%/2.0`; 2K–200 ft Vx `1.5%/1.5`, Vy `3.5%/3.5`, Vz `3.0%/3.0`; 200–5 ft Vx `1.5%/1.5`, Vy `2.0%/1.5`, Vz `2.0%/1.5`; source rule is percentage or ft/s, whichever is greater, percentage of vector velocity | Quantitative **performance/acceptance envelope**. Do not infer Gaussian historical noise merely because limits are expressed at 3 sigma. |
| Dyer, *LM landing radar test for the F mission — Project Apollo*, MSC-69-EG-14 / NASA-TM-X-64374, 11 Mar 1969 | NTRS primary-record metadata identifies an F-mission LR test-requirements memorandum | **Adjacent effectivity; content not yet inspected.** Candidate additional quantitative-error source. Do not import values into Apollo 11 without direct inspection plus Mission-G/LM-5 applicability evidence. |
| Philco `PHO-FAM001`, 30 Jun 1967 | Display-request keyboard/encoder transaction and stored-display capability | **Pre-Apollo-11 baseline.** Generic request architecture only. |
| Hoover, NASA TN D-7685 | 36 computer-driven TV channels for lunar-landing missions; request allocation, attach, usage/release | **Apollo-program experience authority.** Shared display-resource behavior only. |
| Sullivan & Burbank, NASA TN D-8316 | Buffered D/TV updates independent of CRT refresh; reference-slide timing | Apollo-wide display-system evidence; four seconds is not dynamic telemetry cadence. |
| Runnels/Philco-Ford, *Display Formats Manual*, PHO-TR515 / NASA-CR-128843, 12 Jan 1973 | DTE dynamic-group FDS records source, coordinate, configuration; external names distinguish telemetry measurements from DPB computation/MED/logic identifiers; format metadata includes downlist indicator and multi-downlist blank case; plot formats carry explicit update-rate metadata | **Later primary system baseline.** Establishes the provenance schema needed for field reconstruction, but not Apollo-11-effective MSK-1137 external names/downlists or tabular cadence. |
| NASA, *Apollo 12 Saturn V Flight Manual*, SA-507 | DRK direct-PBI request and MSK display-request relationship | **Adjacent effectivity only.** Not Apollo 11 GUIDO assignment. |
| Costis, Ortolani & Moreland, PHO-TN401, 24 Dec 1969 | Mission-specific Apollo 11 display/control usage study | **BLOCKED:** no public digital copy located; archival holding identified. |
| NASA TN D-6849 / MIT-IL E-1982 | LR error boundaries/design-history assumptions; LM-5 one-count velocity-bias defect corrected preflight; Doppler-spectrum-simulator Gaussian test assumption required heavier-tail correction; Apollo 11 flight data within specification except expected near-zero-Doppler region | Supports the distinction between specification envelope and stochastic model; does not supply a numerical flight-effective probability distribution. |

## Current result

The Apollo 11 profile carries source-controlled LM-5 geometry, estimator behavior, and MSK-1137 field semantics. Ground/display architecture prohibits direct authoritative-state aliasing.

The mission-specific MSK-1137 sheet itself supplies the key provenance boundary: `D/L` and `RTCC` are explicitly distinguished on the format, and `ACT ΔV` is documented as ground computed. Thus the display is demonstrably mixed-source. PHO-TR515 independently shows the later formal metadata model for resolving that mixture field by field, but its 1973 identifiers cannot be used as Apollo 11 mappings.

The Apollo 11 Mission Report independently constrains what happened when LR data became operationally usable: the crew evaluated the data against reasonability/precalculated limits before incorporation and verified convergence afterward. That supports modeling an acceptance/convergence state, but it must not be converted into an unsupported GUIDO command or assumed MSK-1137 workflow.

The landing-radar numerical-error thread is now narrower. NTRS 19700004489 reproduces the GAEC LSP-470-2D master-end-item 3-sigma accuracy limits, including the exact altitude/component velocity cells and the `whichever is greater` rule. This closes the component-level performance envelope. It does **not** close historical stochastic generation. TN D-6849's LM-5 test history records that a Gaussian assumption used for Doppler-spectrum-simulator limits required correction because of heavier tails. A 3-sigma specification therefore must not be converted into a Gaussian random-error model without additional evidence.

MSC-69-EG-14 / NASA-TM-X-64374 remains useful as an adjacent-effectivity retrieval target for additional test detail.

PHO-TN401 remains **BLOCKED**. Historical stochastic LR generation remains **BLOCKED** separately.

## Effectivity rule

Do not back-project later mission console assignments, 1973 display identifiers, plot timing, or F-mission LR test values into Apollo 11. Do not infer a per-field route merely from the Apollo 11 format's `D/L`/`RTCC` category labels. Do not assign the crew's documented LR incorporation decision to GUIDO without separate mission-effective evidence. Do not interpret a 3-sigma master-end-item accuracy requirement as proof of a Gaussian error distribution. Apollo-11-effective FDS/RTCC/CCATS evidence is still required for exact field mapping and tabular cadence; Mission-G/LM-5 evidence is still required to characterize stochastic sensor behavior beyond the documented performance envelope.

## Sources

- https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/POWERED_FLIGHT_SUBROUTINES.agc.html
- https://www.ibiblio.org/apollo/Documents/LUM95_text.pdf
- https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11_MissionOpReport.pdf
- https://ntrs.nasa.gov/api/citations/19700004489/downloads/19700004489.pdf
- https://ntrs.nasa.gov/citations/19700025433
- `PHO-FAM001`, *Mission Control Center Houston Familiarization Manual*, Philco, 30 Jun 1967
- https://ntrs.nasa.gov/citations/19740015284
- https://ntrs.nasa.gov/citations/19760024152
- https://ntrs.nasa.gov/citations/19730010501
- https://www.nasa.gov/wp-content/uploads/static/history/afj/ap12fj/pdf/a12_sa507-flightmanual.pdf
- https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf
- https://ntrs.nasa.gov/api/citations/19720016521/downloads/19720016521.pdf
- https://www.ibiblio.org/apollo/Documents/E-1982_LEM_PGNCS_and_Landing_Radar_Operations.pdf

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** LM-5 geometry and landing-radar estimator chain.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR semantics/formatting, mixed `D/L`/`RTCC` provenance boundary, and MCC architecture separation.
- **DOCUMENTED:** Apollo 11 crew LR acceptance/convergence workflow during powered descent; no GUIDO command ownership inferred.
- **DOCUMENTED:** GAEC LSP-470-2D 3-sigma landing-radar range and altitude-banded component velocity accuracy envelope as reproduced in NASA primary material; not a stochastic distribution.
- **DOCUMENTED, ADJACENT EFFECTIVITY / CONTENT NOT YET INSPECTED:** MSC-69-EG-14 / NASA-TM-X-64374 F-mission LR test-requirements memorandum.
- **DOCUMENTED, LATER SYSTEM BASELINE:** PHO-TR515 field-source/external-name/downlist metadata model; not Apollo 11 exact routing or tabular cadence.
- **DOCUMENTED, APOLLO-PROGRAM EXPERIENCE:** TN D-7685 shared TV-resource behavior.
- **BLOCKED:** direct PHO-TN401 inspection; stochastic Apollo-11-effective LR error distribution/process beyond the documented 3-sigma performance envelope.
- **UNRESOLVED:** per-field Apollo 11 MSK-1137 `D/L`/`RTCC` mapping and exact external-name/downlist/computation provenance, GUIDO exact request workflow and role in LR acceptance, and numeric dynamic-data cadence/latency/freshness.
