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

## Next work

1. Pursue Apollo-11-effective FDS/RTCC/CCATS material that maps individual MSK-1137 fields to the format's `D/L`/`RTCC` provenance categories and identifies external names/downlists or computation/logic identifiers.
2. Keep Apollo 11 GUIDO exact DRK/MSK button mapping and powered-descent selection unresolved pending mission-effective station evidence.
3. Keep PHO-TN401 direct inspection **BLOCKED** pending archival retrieval/authenticated scan.
4. Keep sample/receive/process/display timestamps distinct; do not infer tabular cadence from onboard LR timing, reference-slide timing, TV-channel allocation, or PHO-TR515 plot update-rate fields.
5. Keep historical stochastic LR measurement generation **BLOCKED** until flight-effective numerical error evidence is recovered.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** LM-5 geometry + SETPOS + measurement-time NB→SM transform through the estimator.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR field semantics/formatting and mission-specific mixed `D/L`/`RTCC` provenance categories; `ACT ΔV` is ground computed.
- **DOCUMENTED:** Apollo MCC architectural separation and D/TV buffered-update behavior.
- **DOCUMENTED, APOLLO-PROGRAM EXPERIENCE:** TN D-7685 display-request/channel-allocation behavior.
- **DOCUMENTED, LATER SYSTEM BASELINE:** PHO-TR515 defines dynamic-field provenance metadata; it does not supply Apollo-11-effective MSK-1137 field routing or tabular cadence.
- **DOCUMENTED, PRE-APOLLO-11 BASELINE:** PHO-FAM001 generic display/device request transaction.
- **DOCUMENTED, ADJACENT EFFECTIVITY:** Apollo 12 DRK/MSK request semantics.
- **BLOCKED:** direct PHO-TN401 inspection; historical stochastic LR measurement generation.
- **UNRESOLVED:** per-field Apollo 11 MSK-1137 `D/L`/`RTCC` mapping and exact external-name/downlist/computation provenance, numeric dynamic-data cadence/latency/freshness, and GUIDO exact request workflow.
