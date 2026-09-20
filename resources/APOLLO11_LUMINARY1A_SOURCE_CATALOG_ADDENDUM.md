# Apollo 11 / Luminary 1A source-catalog addendum

Date: 2026-09-20

## Controlled source chain

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Mission G rendezvous report | References *Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program*, May 1969 | Primary mission-period evidence for the Luminary 1A equation document. |
| LUMINARY 099 `SERVICER.agc` / `POWERED_FLIGHT_SUBROUTINES.agc` | SETPOS, measurement-epoch capture, beam transform, propagation, qualification, update; SM/NB transform semantics | Apollo-11-effective estimator chain authority. |
| LUMINARY 099 `ASSEMBLY_AND_OPERATION_INFORMATION.agc` / `PINBALL_NOUN_TABLES.agc` / `SERVICER.agc` | LR low-scale altitude low-order bit `1.079 ft`; X/Y/Z LR velocity low-order bits `-0.6440/+1.212/+0.8668 ft/s`; `HMEAS` explicitly stored as `1.079 FT/BIT` | **Apollo-11-effective onboard converted/stored scaling.** Does not alone establish complete LM-5 raw serial encoding, raw bias, high-range hardware bit weight, rounding, or framing. |
| LUMINARY Memo #95 and LM-5 Mission G prelaunch load | Antenna→NB rotation semantics and position-specific `LRALPHA/LRBETA` | Apollo-11 mission/configuration authority. |
| AC Electronics, *Apollo 11 Guidance and Navigation System Manual* | 2-second LR component schedule; four-second `DATA GOOD` qualification; ASPO 45 MSK-1137 field definitions and mixed `D/L`/`RTCC` source categories | Apollo-11-effective onboard qualification/cadence and field-semantics authority; not MCC display cadence. |
| MIT Instrumentation Laboratory, R-700 Vol. II / NASA-CR-141898 | Apollo 11 LR reasonableness criteria: velocity `|delta q| <= 7.5 + 0.125 V_T` ft/s; range-derived altitude `|delta q| <= 200 + 0.125 h` ft; altitude test omitted above high gate | Onboard measurement admission, not sensor-error probability or MCC display behavior. |
| NASA, *Apollo 11 Mission Report*, MSC-00171 | Crew LR incorporation/convergence workflow; acquisition; expected zero-Doppler losses; Table 5-I not-good/good transitions | Apollo-11-effective operational/flight authority; event anchors, not stochastic law. |
| NASA, *Apollo 11 AS-506 Mission Operation Report*, M-932-69-11 | Distinct CCATS, RTCC, Display/Control, MOCR/SSR elements | Apollo-11-effective architecture authority; not exact per-field routing/timing. |
| NASA NTRS 19700004489, GAEC LSP-470-2D | LR 3-sigma range and altitude-banded velocity accuracy limits | Quantitative acceptance envelope; not proof of Gaussian historical noise. |
| TRW, NASA-CR-92466 / TRW-11176-H059-R0-00 | LR altimeter beam bandwidth and Doppler equations verified for mathematical-model use | Mission-period model source; not LM-5 flight-error statistics. |
| Dyer, MSC-69-EG-14 / NASA-TM-X-64374 | F-mission LR test-requirements memorandum | **Adjacent effectivity; content not yet inspected.** Do not import values without Mission-G/LM-5 applicability evidence. |
| Later R-567 Section 2 revisions | 15-bit LR raw-data descriptions, integer bias/conversion, high/low range conversion | **Later adjacent effectivity.** Useful target/cross-check only until an Apollo-11 applicability bridge is established. |
| *Apollo Operations Handbook, Lunar Module LM10 and Subsequent*, LMA790-3-LM | Selectable radar fixed-extension quantities; LR velocity/range delivered as 15-bit binary words to LGC | **Later adjacent effectivity.** Does not establish LM-5 raw serial encoding/timing/error distribution. |
| Philco `PHO-FAM001`, 30 Jun 1967 | Display-request keyboard/encoder transaction and stored-display capability | **Pre-Apollo-11 baseline.** Generic request architecture only. |
| Hoover, NASA TN D-7685 | 36 computer-driven TV channels for lunar-landing missions; request allocation/attach/release | Apollo-program shared display-resource behavior only. |
| Sullivan & Burbank, NASA TN D-8316 | Buffered D/TV updates independent of CRT refresh; reference-slide timing | Apollo-wide display-system evidence; not dynamic telemetry cadence. |
| Runnels/Philco-Ford, PHO-TR515 / NASA-CR-128843 | DTE dynamic-group source/external-name metadata | **Later primary system baseline.** Not Apollo-11-effective routing/cadence. |
| NASA, *Apollo 12 Saturn V Flight Manual*, SA-507 | DRK direct-PBI request and MSK display-request relationship | **Adjacent effectivity only.** Not Apollo 11 GUIDO assignment. |
| Costis, Ortolani & Moreland, PHO-TN401, 24 Dec 1969 | Mission-specific Apollo 11 display/control usage study | **BLOCKED:** no public digital copy located; archival holding identified. |
| Rozas & Cunningham, NASA TN D-6849 / MSC-S-311, Jun 1972 | LR processed velocity/slant range supplied to LGC in serial binary form and separately to LM displays as pulse trains/dc analog voltages; LM-5 LR generally within specification except near zero Doppler; simulator Gaussian assumption required heavier-tail correction | Apollo-program hardware/LM-5 experience authority. Establishes separate LGC-digital and local-display output paths, but not complete LM-5 serial encoding, transfer cadence, stochastic distribution, or MCC routing. |

## Current result

The Apollo 11 profile carries source-controlled LM-5 geometry, estimator behavior, and MSK-1137 field semantics. Ground/display architecture prohibits direct authoritative-state aliasing.

R-700 Vol. II closes the onboard reasonableness-test parameter boundary for Apollo 11. The Mission Report supplies event-table timing for the two LR tracking interruptions, while the AC Electronics manual supplies the separate four-second `DATA GOOD` qualification before measurement tests permit updating.

The numerical-error thread remains narrower than the performance envelope. LSP-470-2D gives 3-sigma acceptance limits; TN D-6849 supplies generally in-spec LM-5 behavior and cautions against a simple Gaussian simulator assumption. NASA-CR-92466 is a mission-period source for beam/Doppler model equations, but not flight-error evidence.

The flown LUMINARY 099 listing materially narrows the prior quantization gap without using later LM hardware documentation: Apollo-11-effective onboard converted/stored scales are now documented as `1.079 ft/bit` for low-scale altitude and `-0.6440/+1.212/+0.8668 ft/s` per low-order bit for X/Y/Z velocity. This controls the LUMINARY-side numerical representation, not the complete radar-electronics serial encoding. In particular, raw serial word length/bias, high-range hardware conversion, rounding/truncation, and framing remain unresolved.

TN D-6849 independently establishes that the processed LR path to the LGC was serial binary while local LM displays used separate pulse-train/dc-analog outputs. Later LM10/R-567 15-bit/raw-conversion descriptions remain adjacent-effectivity cross-checks rather than Apollo-11 authority for the still-open serial details.

Historical stochastic LR generation remains **BLOCKED**. PHO-TN401 remains **BLOCKED** separately.

## Effectivity rule

Do not back-project later console assignments, 1973 display identifiers, plot timing, later 15-bit raw encoding, or F-mission LR values into Apollo 11. Do not infer per-field routing from `D/L`/`RTCC` labels alone. Do not assign the crew's LR incorporation decision to GUIDO without mission-effective evidence. Do not convert 3-sigma requirements, reasonableness gates, flown bit weights, or timed flight interruptions into a random-error/dropout distribution. Do not equate a recorded `DATA GOOD` transition with immediate LGC state updating. Do not expose the onboard reasonableness criterion as a GUIDO control/display unless MCC-effective evidence establishes it. Treat the flown LUMINARY bit weights as onboard converted/stored scaling, not proof of the complete LM-5 serial protocol.

## Sources

- https://www.ibiblio.org/apollo/listings/Luminary099/ASSEMBLY_AND_OPERATION_INFORMATION.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/PINBALL_NOUN_TABLES.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/POWERED_FLIGHT_SUBROUTINES.agc.html
- https://www.ibiblio.org/apollo/Documents/LUM95_text.pdf
- https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- https://ntrs.nasa.gov/citations/19750020038
- https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- https://www.nasa.gov/wp-content/uploads/static/history/afj/a11/A11_MissionOpReport.pdf
- https://ntrs.nasa.gov/api/citations/19700004489/downloads/19700004489.pdf
- https://ntrs.nasa.gov/citations/19690007699
- https://ntrs.nasa.gov/citations/19700025433
- https://www.ibiblio.org/apollo/NARA-SW/R-567-sec2-rev8.pdf
- https://www.ibiblio.org/apollo/Documents/LMA790-3-LM10-ApolloOperationsHandbookLunarModuleLM10AndSubsequent-Volume1-SubsystemsData-SearchableText.pdf
- `PHO-FAM001`, *Mission Control Center Houston Familiarization Manual*, Philco, 30 Jun 1967
- https://ntrs.nasa.gov/citations/19740015284
- https://ntrs.nasa.gov/citations/19760024152
- https://ntrs.nasa.gov/citations/19730010501
- https://www.nasa.gov/wp-content/uploads/static/history/afj/ap12fj/pdf/a12_sa507-flightmanual.pdf
- https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf
- https://ntrs.nasa.gov/api/citations/19720016521/downloads/19720016521.pdf

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** LM-5 geometry and landing-radar estimator chain.
- **DOCUMENTED:** Apollo-11-specific onboard LR reasonableness equations and high-gate altitude-test omission.
- **DOCUMENTED:** Apollo 11 MSK-1137 semantics/formatting and mixed `D/L`/`RTCC` provenance boundary.
- **DOCUMENTED, APOLLO 11 FLIGHT:** LR acquisition plus one-second-resolution not-good intervals and expected zero-Doppler/manual-maneuver cause.
- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD LOGIC:** four-second continuous `DATA GOOD` qualification before LR measurement tests permit updating.
- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD SCALING:** low-scale altitude `1.079 ft/bit`; X/Y/Z velocity low-order bit weights `-0.6440/+1.212/+0.8668 ft/s`.
- **DOCUMENTED:** GAEC LSP-470-2D 3-sigma performance envelope; not a stochastic distribution.
- **DOCUMENTED, APOLLO-PROGRAM HARDWARE / LM-5 EXPERIENCE SOURCE:** LR processed velocity/range to LGC as serial binary data; separate pulse-train/dc-analog output to LM displays.
- **DOCUMENTED, MISSION-PERIOD MODEL SOURCE:** NASA-CR-92466 for LR beam-bandwidth/Doppler model verification.
- **ADJACENT EFFECTIVITY:** later LM10/R-567 material confirms 15-bit raw LR/LGC architecture/conversions; complete Apollo 11 serial encoding is not inferred.
- **BLOCKED:** direct PHO-TN401 inspection; stochastic Apollo-11-effective LR error distribution/process beyond documented envelope/events.
- **UNRESOLVED:** per-field MSK-1137 routing, GUIDO exact request workflow, controller-visible consequence of onboard reasonableness rejection, MCC dynamic-data cadence/latency/freshness, complete LM-5 raw serial encoding/high-range conversion/rounding/framing, and sub-second LR transition timing.
