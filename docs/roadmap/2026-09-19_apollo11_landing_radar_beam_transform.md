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

The Apollo 11 Mission Report adds a separate operational constraint on landing-radar use during powered descent: when LR data became available, **the crew** decided whether to incorporate it into PGNS based on reasonability and precalculated limits; after incorporation, convergence was verified. The same report's radar section further states that range and velocity were acquired at slant ranges of approximately 44,000 and 28,000 ft, and that LR tracking was lost briefly at altitudes of 240 and 75 ft. Those two losses were expected and attributed to zero-Doppler effects associated with manual maneuvering. This closes two mission-effective tracking-loss event points and their stated cause without establishing a general dropout probability, duration, or stochastic process.

A primary NASA precursor has now been identified for the remaining LR numerical-error question: D. A. Dyer, *LM landing radar test for the F mission — Project Apollo*, MSC-69-EG-14 / NASA-TM-X-64374, 11 Mar 1969 (NTRS 19700025433). NTRS identifies it specifically as an F-mission landing-radar test-requirements memorandum. The public record exposes metadata but the PDF is not presently retrievable through the available NTRS path, so its numerical contents have **not** been claimed. Even after retrieval it is adjacent-effectivity evidence and cannot by itself establish an Apollo-11/LM-5 stochastic distribution without a Mission-G applicability bridge.

## Next work

1. Pursue Apollo-11-effective FDS/RTCC/CCATS material that maps individual MSK-1137 fields to the format's `D/L`/`RTCC` provenance categories and identifies external names/downlists or computation/logic identifiers.
2. Continue seeking LM-5 qualification/acceptance or Apollo 11 flight-data reduction evidence that numerically characterizes LR residuals, quantization, correlation, dropout duration, or bias. Treat the documented 240-ft and 75-ft losses as discrete mission events, not a probability law.
3. Retrieve and inspect MSC-69-EG-14 / NASA-TM-X-64374 for any quantitative LR test/error requirements, then require an explicit Mission-G/LM-5 applicability bridge before using any F-mission numbers in Apollo 11 behavior.
4. Keep Apollo 11 GUIDO exact DRK/MSK button mapping and powered-descent selection unresolved pending mission-effective station evidence; do not convert the Mission Report's crew LR-acceptance decision into an unsupported GUIDO control action.
5. Keep PHO-TN401 direct inspection **BLOCKED** pending archival retrieval/authenticated scan.
6. Keep sample/receive/process/display timestamps distinct; do not infer tabular cadence from onboard LR timing, reference-slide timing, TV-channel allocation, or PHO-TR515 plot update-rate fields.
7. Keep historical stochastic LR measurement generation **BLOCKED** until flight-effective numerical error evidence is recovered and tied to Mission G/LM-5.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** LM-5 geometry + SETPOS + measurement-time NB→SM transform through the estimator.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR field semantics/formatting and mission-specific mixed `D/L`/`RTCC` provenance categories; `ACT ΔV` is ground computed.
- **DOCUMENTED:** Apollo 11 powered-descent LR acceptance was a crew decision based on reasonability/precalculated limits, followed by convergence verification after incorporation; this does not document a GUIDO command path.
- **DOCUMENTED, APOLLO 11 FLIGHT:** LR range/velocity acquisition at approximately 44,000/28,000-ft slant range and brief expected tracking losses at 240/75-ft altitude attributed to zero-Doppler effects during manual maneuvering.
- **DOCUMENTED:** Apollo MCC architectural separation and D/TV buffered-update behavior.
- **DOCUMENTED, APOLLO-PROGRAM EXPERIENCE:** TN D-7685 display-request/channel-allocation behavior.
- **DOCUMENTED, LATER SYSTEM BASELINE:** PHO-TR515 defines dynamic-field provenance metadata; it does not supply Apollo-11-effective MSK-1137 field routing or tabular cadence.
- **DOCUMENTED, PRE-APOLLO-11 BASELINE:** PHO-FAM001 generic display/device request transaction.
- **DOCUMENTED, ADJACENT EFFECTIVITY / CONTENT NOT YET INSPECTED:** MSC-69-EG-14 / NASA-TM-X-64374 is an F-mission LR test-requirements memorandum; no numerical result is imported into Apollo 11.
- **DOCUMENTED, ADJACENT EFFECTIVITY:** Apollo 12 DRK/MSK request semantics.
- **BLOCKED:** direct PHO-TN401 inspection; historical stochastic LR measurement generation pending quantitative evidence and Mission-G applicability.
- **UNRESOLVED:** per-field Apollo 11 MSK-1137 `D/L`/`RTCC` mapping and exact external-name/downlist/computation provenance, numeric dynamic-data cadence/latency/freshness, and GUIDO exact request workflow.
