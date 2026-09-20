# Apollo 11 / Luminary 1A source-catalog addendum

Date: 2026-09-20

## Controlled source chain

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Mission G rendezvous report | References *Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program*, May 1969 | Primary mission-period evidence for the Luminary 1A equation document. |
| LUMINARY 099 `SERVICER.agc` / `POWERED_FLIGHT_SUBROUTINES.agc` | SETPOS, measurement-epoch capture, beam transform, propagation, qualification, update; SM/NB transform semantics | Apollo-11-effective estimator chain authority. |
| LUMINARY Memo #95 and LM-5 Mission G prelaunch load | Antenna→NB rotation semantics and position-specific `LRALPHA/LRBETA` | Apollo-11 mission/configuration authority. |
| AC Electronics, *Apollo 11 Guidance and Navigation System Manual* | 2-second LR component schedule; ASPO 45 MSK-1137 LR field definitions; MSK-1137 visibly distinguishes `D/L` and `RTCC` source categories; `ACT ΔV` identified as ground computed | Apollo-11-effective onboard cadence, field semantics, and mixed-provenance boundary; not a per-field routing table or MCC display cadence. |
| NASA, *Apollo 11 Mission Report*, MSC-00171, Nov 1969 | Crew LR incorporation decision used reasonability/precalculated limits and convergence verification; LR range/velocity acquired at ~44,000/~28,000-ft slant range; brief tracking losses at 240/75-ft altitude were expected and attributed to zero-Doppler effects during manual maneuvering | Apollo-11-effective operational and flight-performance authority. Discrete events, not a dropout probability or stochastic law. Does not establish GUIDO ownership/display routing. |
| NASA, *Apollo 11 AS-506 Mission Operation Report*, M-932-69-11 | Distinct CCATS, RTCC, Display/Control, MOCR/SSR elements | Apollo-11-effective architecture authority; not exact per-field routing/timing. |
| NASA NTRS 19700004489, table reproducing GAEC specification LSP-470-2D, *Master End Item Specification for Lunar Module* | Landing-radar 3-sigma range limits plus altitude-banded velocity accuracy to LGC | Quantitative **performance/acceptance envelope**. Do not infer Gaussian historical noise merely because limits are expressed at 3 sigma. |
| Dyer, *LM landing radar test for the F mission — Project Apollo*, MSC-69-EG-14 / NASA-TM-X-64374, 11 Mar 1969 | NTRS primary-record metadata identifies an F-mission LR test-requirements memorandum | **Adjacent effectivity; content not yet inspected.** Do not import values into Apollo 11 without direct inspection plus Mission-G/LM-5 applicability evidence. |
| Philco `PHO-FAM001`, 30 Jun 1967 | Display-request keyboard/encoder transaction and stored-display capability | **Pre-Apollo-11 baseline.** Generic request architecture only. |
| Hoover, NASA TN D-7685 | 36 computer-driven TV channels for lunar-landing missions; request allocation, attach, usage/release | **Apollo-program experience authority.** Shared display-resource behavior only. |
| Sullivan & Burbank, NASA TN D-8316 | Buffered D/TV updates independent of CRT refresh; reference-slide timing | Apollo-wide display-system evidence; four seconds is not dynamic telemetry cadence. |
| Runnels/Philco-Ford, *Display Formats Manual*, PHO-TR515 / NASA-CR-128843, 12 Jan 1973 | DTE dynamic-group FDS records source, coordinate, configuration; external names distinguish telemetry measurements from DPB computation/MED/logic identifiers | **Later primary system baseline.** Not Apollo-11-effective routing/cadence. |
| NASA, *Apollo 12 Saturn V Flight Manual*, SA-507 | DRK direct-PBI request and MSK display-request relationship | **Adjacent effectivity only.** Not Apollo 11 GUIDO assignment. |
| Costis, Ortolani & Moreland, PHO-TN401, 24 Dec 1969 | Mission-specific Apollo 11 display/control usage study | **BLOCKED:** no public digital copy located; archival holding identified. |
| Rozas & Cunningham, NASA TN D-6849 / MSC-S-311, *Apollo Experience Report: Lunar Module Landing Radar and Rendezvous Radar*, Jun 1972 | LR design/test history; LM-5 one-count velocity-bias defect corrected preflight; Doppler-spectrum-simulator Gaussian test assumption required heavier-tail correction; Apollo 11 LR flight data generally within specification except near zero Doppler | Primary NASA Apollo-program experience authority. Does not supply a numerical flight-effective probability distribution, dropout rate, correlation model, or controller-display behavior. |

## Current result

The Apollo 11 profile carries source-controlled LM-5 geometry, estimator behavior, and MSK-1137 field semantics. Ground/display architecture prohibits direct authoritative-state aliasing.

The mission-specific MSK-1137 sheet supplies the key provenance boundary: `D/L` and `RTCC` are explicitly distinguished on the format, and `ACT ΔV` is documented as ground computed. Thus the display is demonstrably mixed-source. PHO-TR515 independently shows the later formal metadata model for resolving that mixture field by field, but its 1973 identifiers cannot be used as Apollo 11 mappings.

The Apollo 11 Mission Report now supplies two complementary mission-effective LR constraints. Operationally, the crew evaluated LR data against reasonability/precalculated limits before incorporation and verified convergence afterward. At the sensor-performance level, range and velocity were acquired at approximately 44,000 and 28,000 ft slant range, and tracking was lost briefly at 240 and 75 ft altitude; the report explicitly calls those losses expected and attributes them to zero-Doppler effects associated with manual maneuvering. These exact events may anchor historical validation, but they may not be generalized into an invented dropout probability, duration, or stochastic mechanism.

The landing-radar numerical-error thread remains narrower than the performance envelope. NTRS 19700004489 reproduces the GAEC LSP-470-2D master-end-item 3-sigma accuracy limits. TN D-6849 supplies generally in-spec LM-5 behavior and a near-zero-Doppler exception, while also warning that a Gaussian simulator assumption required correction for heavier tails. Neither a 3-sigma requirement nor the observed discrete losses may be converted into a Gaussian random-error model.

MSC-69-EG-14 / NASA-TM-X-64374 remains useful as an adjacent-effectivity retrieval target for additional test detail. PHO-TN401 remains **BLOCKED**. Historical stochastic LR generation remains **BLOCKED** separately.

## Effectivity rule

Do not back-project later mission console assignments, 1973 display identifiers, plot timing, or F-mission LR test values into Apollo 11. Do not infer a per-field route merely from the Apollo 11 format's `D/L`/`RTCC` category labels. Do not assign the crew's documented LR incorporation decision to GUIDO without separate mission-effective evidence. Do not interpret a 3-sigma master-end-item accuracy requirement as proof of a Gaussian error distribution. Treat the Mission Report's 240-ft and 75-ft losses as discrete source-described events only; do not invent their duration, probability, or controller-visible symptoms. Apollo-11-effective FDS/RTCC/CCATS evidence is still required for exact field mapping and tabular cadence; Mission-G/LM-5 evidence is still required to characterize stochastic sensor behavior beyond the documented performance envelope and flight events.

## Sources

- https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/POWERED_FLIGHT_SUBROUTINES.agc.html
- https://www.ibiblio.org/apollo/Documents/LUM95_text.pdf
- https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- https://www.nasa.gov/wp-content/uploads/static/history/afj/a11/A11_MissionOpReport.pdf
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
- **DOCUMENTED, APOLLO 11 FLIGHT:** range/velocity acquisition at ~44,000/~28,000-ft slant range; brief expected LR tracking losses at 240/75-ft altitude attributed to zero-Doppler effects during manual maneuvering.
- **DOCUMENTED:** GAEC LSP-470-2D 3-sigma landing-radar performance envelope; not a stochastic distribution.
- **DOCUMENTED, APOLLO 11 FLIGHT EXPERIENCE:** TN D-6849 establishes generally in-spec LR behavior plus localized near-zero-Doppler behavior; not a probability model.
- **DOCUMENTED, ADJACENT EFFECTIVITY / CONTENT NOT YET INSPECTED:** MSC-69-EG-14 / NASA-TM-X-64374 F-mission LR test-requirements memorandum.
- **DOCUMENTED, LATER SYSTEM BASELINE:** PHO-TR515 field-source/external-name/downlist metadata model; not Apollo 11 exact routing or tabular cadence.
- **DOCUMENTED, APOLLO-PROGRAM EXPERIENCE:** TN D-7685 shared TV-resource behavior.
- **BLOCKED:** direct PHO-TN401 inspection; stochastic Apollo-11-effective LR error distribution/process beyond the documented 3-sigma performance envelope and discrete flight events.
- **UNRESOLVED:** per-field Apollo 11 MSK-1137 `D/L`/`RTCC` mapping and exact external-name/downlist/computation provenance, GUIDO exact request workflow and role in LR acceptance, and numeric dynamic-data cadence/latency/freshness.
