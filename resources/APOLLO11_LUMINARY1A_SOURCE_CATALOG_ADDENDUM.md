# Apollo 11 / Luminary 1A source-catalog addendum

Date: 2026-09-20

## Controlled source chain

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Mission G rendezvous report | References *Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program*, May 1969 | Primary mission-period evidence for the Luminary 1A equation document. |
| LUMINARY 099 `SERVICER.agc` / `POWERED_FLIGHT_SUBROUTINES.agc` | SETPOS, measurement-epoch capture, beam transform, propagation, qualification, update; SM/NB transform semantics | Apollo-11-effective estimator chain authority. |
| LUMINARY Memo #95 and LM-5 Mission G prelaunch load | Antenna→NB rotation semantics and position-specific `LRALPHA/LRBETA` | Apollo-11 mission/configuration authority. |
| AC Electronics, *Apollo 11 Guidance and Navigation System Manual* | 2-second LR component schedule; LR `DATA GOOD` must persist at least 4 seconds before range/velocity measurement tests permit updating; ASPO 45 MSK-1137 field definitions and mixed `D/L`/`RTCC` source categories | Apollo-11-effective onboard qualification/cadence and field-semantics authority. The four-second rule is onboard measurement qualification, not MCC display cadence. |
| MIT Instrumentation Laboratory, *MIT's Role in Project Apollo, Volume II: Optical, Radar, and Candidate Subsystems*, R-700 Vol. II / NASA-CR-141898, Mar 1972 | Section 5.5.2 gives Apollo 11 LR reasonableness criteria: velocity `|delta q| <= 7.5 + 0.125 V_T` ft/s; range-derived altitude `|delta q| <= 200 + 0.125 h` ft; altitude test omitted above high gate; cross-lobe-lock motivation | Primary NASA contractor retrospective with explicit Apollo-11-specific equations. Use for onboard measurement admission, not sensor-error probability, cross-lobe occurrence rate, or MCC display behavior. |
| NASA, *Apollo 11 Mission Report*, MSC-00171, Nov 1969 | Crew LR incorporation/convergence workflow; LR acquisition at ~44,000/~28,000-ft slant range; expected zero-Doppler tracking losses; Table 5-I records not-good/good transitions at 102:44:11/:21 and 102:44:59/102:45:03 | Apollo-11-effective operational and flight-performance authority. At one-second table resolution the not-good intervals are 10 s and 4 s. These are discrete event anchors, not a dropout probability or stochastic law. |
| NASA, *Apollo 11 AS-506 Mission Operation Report*, M-932-69-11 | Distinct CCATS, RTCC, Display/Control, MOCR/SSR elements | Apollo-11-effective architecture authority; not exact per-field routing/timing. |
| NASA NTRS 19700004489, GAEC LSP-470-2D | Landing-radar 3-sigma range and altitude-banded velocity accuracy limits | Quantitative performance/acceptance envelope; not proof of Gaussian historical noise. |
| TRW, NASA-CR-92466 / TRW-11176-H059-R0-00, 25 Oct 1968 | LR altimeter beam bandwidth and Doppler equations verified for mathematical-model use | Mission-period primary contractor model source. Use for physical/model-equation verification after direct inspection; not LM-5 flight-error statistics. |
| Dyer, MSC-69-EG-14 / NASA-TM-X-64374, 11 Mar 1969 | NTRS metadata identifies an F-mission LR test-requirements memorandum | **Adjacent effectivity; content not yet inspected.** Do not import values without Mission-G/LM-5 applicability evidence. |
| *Apollo Operations Handbook, Lunar Module LM10 and Subsequent*, LMA790-3-LM | Selectable radar fixed-extension quantities; LR velocity/range delivered as 15-bit binary words to LGC | **Later adjacent effectivity.** Architecture cross-check only; does not establish LM-5/Apollo-11 bit weighting, quantization, timing, or error distribution. |
| Philco `PHO-FAM001`, 30 Jun 1967 | Display-request keyboard/encoder transaction and stored-display capability | **Pre-Apollo-11 baseline.** Generic request architecture only. |
| Hoover, NASA TN D-7685 | 36 computer-driven TV channels for lunar-landing missions; request allocation, attach, usage/release | **Apollo-program experience authority.** Shared display-resource behavior only. |
| Sullivan & Burbank, NASA TN D-8316 | Buffered D/TV updates independent of CRT refresh; reference-slide timing | Apollo-wide display-system evidence; reference-slide timing is not dynamic telemetry cadence. |
| Runnels/Philco-Ford, PHO-TR515 / NASA-CR-128843, 12 Jan 1973 | DTE dynamic-group source/external-name metadata | **Later primary system baseline.** Not Apollo-11-effective routing/cadence. |
| NASA, *Apollo 12 Saturn V Flight Manual*, SA-507 | DRK direct-PBI request and MSK display-request relationship | **Adjacent effectivity only.** Not Apollo 11 GUIDO assignment. |
| Costis, Ortolani & Moreland, PHO-TN401, 24 Dec 1969 | Mission-specific Apollo 11 display/control usage study | **BLOCKED:** no public digital copy located; archival holding identified. |
| Rozas & Cunningham, NASA TN D-6849 / MSC-S-311, Jun 1972 | LM-5 LR generally within specification except near zero Doppler; simulator Gaussian assumption required heavier-tail correction | Apollo-program experience authority. Does not supply a numerical flight-effective probability distribution or controller-display behavior. |

## Current result

The Apollo 11 profile carries source-controlled LM-5 geometry, estimator behavior, and MSK-1137 field semantics. Ground/display architecture prohibits direct authoritative-state aliasing.

R-700 Vol. II closes the previously generic reasonableness-test parameter boundary for Apollo 11: velocity and range-derived-altitude admission equations are explicit, and the altitude test is omitted above high gate. The source says the test was designed to guard against cross-lobe lockup but rejects any measurement outside the criterion regardless of cause. This is an onboard estimator-admission rule, not evidence for a cross-lobe probability or random sensor-error generator.

The Mission Report supplies event-table timing for the two previously duration-unbounded LR tracking interruptions: 102:44:11–102:44:21 and 102:44:59–102:45:03. The table is recorded to one-second resolution, so these support 10-second and 4-second historical replay intervals at that resolution, not sub-second physical transition timing. The report's narrative identifies the losses as expected zero-Doppler effects associated with manual maneuvering.

The AC Electronics Apollo 11 manual provides the complementary onboard rule: `DATA GOOD` must remain present for at least four seconds before LR range/velocity measurement tests permit state-vector updating. Historical replay must therefore model the radar-good discrete separately from filter-update eligibility after reacquisition.

The numerical-error thread remains narrower than the performance envelope. LSP-470-2D gives 3-sigma acceptance limits; TN D-6849 supplies generally in-spec LM-5 behavior and cautions against a simple Gaussian simulator assumption. NASA-CR-92466 is now a concrete mission-period source for beam/Doppler model equations, but its stated scope does not make it flight-error evidence. The later LM10 handbook confirms a 15-bit digital LR/LGC architecture, but its effectivity is too late to set an Apollo 11 quantization constant. Historical stochastic LR generation remains **BLOCKED**.

PHO-TN401 remains **BLOCKED** separately.

## Effectivity rule

Do not back-project later console assignments, 1973 display identifiers, plot timing, LM10 interface bit weighting, or F-mission LR values into Apollo 11. Do not infer per-field routing from `D/L`/`RTCC` labels alone. Do not assign the crew's LR incorporation decision to GUIDO without mission-effective evidence. Do not convert 3-sigma requirements, reasonableness gates, or the two timed flight interruptions into a random-error/dropout distribution. Do not equate a recorded `DATA GOOD` transition with immediate LGC state updating; apply the documented four-second qualification rule separately. Do not expose the onboard reasonableness criterion as a GUIDO control or display unless MCC-effective evidence establishes that behavior.

## Sources

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
- **DOCUMENTED:** Apollo-11-specific onboard LR velocity/altitude reasonableness equations and high-gate altitude-test omission.
- **DOCUMENTED:** Apollo 11 MSK-1137 semantics/formatting and mixed `D/L`/`RTCC` provenance boundary.
- **DOCUMENTED, APOLLO 11 FLIGHT:** LR acquisition plus one-second-resolution not-good intervals 102:44:11–:21 and 102:44:59–102:45:03, with expected zero-Doppler/manual-maneuver cause.
- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD LOGIC:** four-second continuous `DATA GOOD` qualification before LR measurement tests permit updating.
- **DOCUMENTED:** GAEC LSP-470-2D 3-sigma performance envelope; not a stochastic distribution.
- **DOCUMENTED, MISSION-PERIOD MODEL SOURCE:** NASA-CR-92466 for LR beam-bandwidth/Doppler mathematical-model verification.
- **ADJACENT EFFECTIVITY:** LM10 handbook confirms selectable 15-bit LR/LGC digital quantities; no Apollo 11 quantization is inferred.
- **BLOCKED:** direct PHO-TN401 inspection; stochastic Apollo-11-effective LR error distribution/process beyond documented envelope/events.
- **UNRESOLVED:** per-field MSK-1137 routing, GUIDO exact request workflow, controller-visible consequence of onboard reasonableness rejection, MCC dynamic-data cadence/latency/freshness, Apollo-11-effective LR bit weighting/quantization, and sub-second LR transition timing.
