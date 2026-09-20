# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-20
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective LUMINARY 099 controls `SETPOS`, measurement-time CDU capture, Y-Z-X preparation, and `*NBSM*` direction semantics. Memo #95 controls antenna→NB beta-then-alpha semantics. The LM-5 Mission G prelaunch erasable load supplies the position-specific alpha/beta values.

## Completed

The equation-level SETPOS and SM/NB transforms are composed into the landing-radar velocity estimator chain, with a provenance-bearing LM-5 profile adapter. Mission-specific MSK-1137 evidence controls LR field identities, body-axis velocity frame, units/display masks, validity fields, and the ground-computed identity of `ACT ΔV`.

Apollo 11 MCC architecture is source-controlled as distinct spacecraft/downlink, CCATS/RTCC processing, Display/Control, and controller-presentation layers. PHO-TN401 is identified as the mission-specific Apollo 11 display-usage source but remains **BLOCKED** behind archival access.

NASA TN D-8316 separates buffered dynamic-data updates from CRT refresh and reference-slide access. PHO-FAM001 constrains the pre-Apollo-11 request transaction. NASA TN D-7685 constrains Apollo-program display-request/channel-allocation behavior, including the 36-channel computer-driven TV pool for lunar-landing missions.

Philco-Ford PHO-TR515, *Display Formats Manual* (12 Jan 1973), supplies a later-system provenance model: DTE dynamic groups carry source, coordinate/configuration, external-name, and downlist metadata. It does not establish Apollo-11-effective identifiers or tabular cadence.

A renewed inspection of the primary AC Electronics Apollo 11 MSK-1137 sheet adds one mission-effective constraint: the format itself visibly distinguishes `D/L` and `RTCC` source categories, while its field notes separately identify `ACT ΔV` as ground computed. The Apollo 11 controller display therefore cannot be modeled as a simple mirror of one spacecraft downlist. This is evidence for **mixed provenance on the mission-specific format**, not enough evidence to assign an external name/downlist/computation route to each field.

The Apollo 11 Mission Report constrains landing-radar use during powered descent: range and velocity were acquired at about 44,000 and 28,000 ft slant range; the crew decided whether to incorporate LR data based on reasonability and precalculated limits; and the report attributes two later brief tracking losses to expected zero-Doppler effects during manual maneuvering. Table 5-I now closes the event-time intervals around those losses: `DATA NOT GOOD` at 102:44:11 returned `DATA GOOD` at 102:44:21, and `DATA NOT GOOD` at 102:44:59 returned `DATA GOOD` at 102:45:03. At the report's one-second event resolution these are 10-second and 4-second not-good intervals. They are mission-event timing anchors, not evidence for a generalized dropout law or sub-second transition times.

The AC Electronics Apollo 11 manual independently requires the LR `DATA GOOD` discrete to have been present for at least four seconds before range/velocity measurement tests permit state-vector updating. Therefore historical replay should distinguish **radar data-good state** from **eligibility to resume LR-aided state updates** after reacquisition; it must not equate the recorded `DATA GOOD` transition with immediate filter use.

A primary NASA precursor remains identified for the LR numerical-error question: D. A. Dyer, *LM landing radar test for the F mission — Project Apollo*, MSC-69-EG-14 / NASA-TM-X-64374, 11 Mar 1969 (NTRS 19700025433). Its numerical contents remain uninspected and cannot be imported without a Mission-G/LM-5 applicability bridge.

## Next work

1. Pursue Apollo-11-effective FDS/RTCC/CCATS material that maps individual MSK-1137 fields to the format's `D/L`/`RTCC` provenance categories and identifies external names/downlists or computation/logic identifiers.
2. Continue seeking LM-5 qualification/acceptance or Apollo 11 flight-data reduction evidence that characterizes LR residuals, quantization, correlation, bias, or transition timing below the Mission Report's one-second event resolution.
3. Preserve the two Table 5-I not-good intervals as deterministic historical replay anchors and enforce the documented four-second `DATA GOOD` qualification separately; do not infer a random dropout process from them.
4. Retrieve and inspect MSC-69-EG-14 / NASA-TM-X-64374, requiring an explicit Mission-G/LM-5 applicability bridge before using any F-mission numbers.
5. Keep Apollo 11 GUIDO exact DRK/MSK button mapping and powered-descent selection unresolved pending mission-effective station evidence.
6. Keep PHO-TN401 direct inspection **BLOCKED** pending archival retrieval/authenticated scan.
7. Keep sample/receive/process/display timestamps distinct; do not infer MCC tabular cadence from onboard LR timing.
8. Keep historical stochastic LR measurement generation **BLOCKED** until flight-effective numerical error evidence is recovered.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** LM-5 geometry + SETPOS + measurement-time NB→SM transform through the estimator.
- **DOCUMENTED:** Apollo 11 MSK-1137 semantics and mixed `D/L`/`RTCC` provenance boundary.
- **DOCUMENTED, APOLLO 11 FLIGHT:** LR acquisition at ~44,000/~28,000-ft slant range; `DATA NOT GOOD`→`DATA GOOD` intervals 102:44:11–:21 and 102:44:59–102:45:03; expected zero-Doppler/manual-maneuver cause.
- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD LOGIC:** at least four continuous seconds of `DATA GOOD` are required before LR range/velocity measurement tests permit state-vector updating.
- **DOCUMENTED:** Apollo MCC architectural separation and D/TV buffered-update behavior.
- **BLOCKED:** direct PHO-TN401 inspection; historical stochastic LR measurement generation.
- **UNRESOLVED:** per-field Apollo 11 MSK-1137 routing, exact GUIDO request workflow, MCC dynamic-data cadence/latency/freshness, and sub-second LR transition timing.
