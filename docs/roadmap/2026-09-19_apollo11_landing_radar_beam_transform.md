# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-20
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective LUMINARY 099 controls `SETPOS`, measurement-time CDU capture, Y-Z-X preparation, and `*NBSM*` direction semantics. Memo #95 controls antenna→NB beta-then-alpha semantics. The LM-5 Mission G prelaunch erasable load supplies the position-specific alpha/beta values.

## Completed

The equation-level SETPOS and SM/NB transforms are composed into the landing-radar velocity estimator chain, with a provenance-bearing LM-5 profile adapter. Mission-specific MSK-1137 evidence controls LR field identities, body-axis velocity frame, units/display masks, validity fields, and the ground-computed identity of `ACT ΔV`.

Apollo 11 MCC architecture is source-controlled as distinct spacecraft/downlink, CCATS/RTCC processing, Display/Control, and controller-presentation layers. PHO-TN401 is identified as the mission-specific Apollo 11 display-usage source but remains **BLOCKED** behind archival access.

NASA TN D-8316 separates buffered dynamic-data updates from CRT refresh and reference-slide access. PHO-FAM001 constrains the pre-Apollo-11 request transaction. NASA TN D-7685 constrains Apollo-program display-request/channel-allocation behavior, including the 36-channel computer-driven TV pool for lunar-landing missions.

A fresh primary-source inspection of Philco-Ford PHO-TR515, *Display Formats Manual* (12 Jan 1973), narrows the remaining per-field routing question without back-projecting a 1973 format into Apollo 11. Its DTE format-description system records, for each dynamic group, an external source name, display coordinates/configuration, and source class. External names may be direct telemetry measurement numbers or Data Processing Branch identifiers for computations, manual-entry data, or special logic. The manual also distinguishes telemetry display types and documents a downlist indicator, including the case where a display is updated from more than one downlist. This establishes the **kind of provenance metadata** needed to reconstruct a controller field, but does not identify the Apollo-11-effective external names/downlists for MSK-1137. Its explicit update-rate field is documented for plot formats and therefore is not authority for MSK-1137 tabular cadence.

## Next work

1. Pursue Apollo-11-effective FDS/display-format material or RTCC/CCATS program documentation that identifies MSK-1137 external names, downlist provenance, and any computed/logic fields.
2. Keep Apollo 11 GUIDO exact DRK/MSK button mapping and powered-descent selection unresolved pending mission-effective station evidence.
3. Keep PHO-TN401 direct inspection **BLOCKED** pending archival retrieval/authenticated scan.
4. Keep sample/receive/process/display timestamps distinct; do not infer tabular cadence from onboard LR timing, reference-slide timing, TV-channel allocation, or PHO-TR515 plot update-rate fields.
5. Keep historical stochastic LR measurement generation **BLOCKED** until flight-effective numerical error evidence is recovered.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** LM-5 geometry + SETPOS + measurement-time NB→SM transform through the estimator.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR field semantics/formatting at field-definition level.
- **DOCUMENTED:** Apollo MCC architectural separation and D/TV buffered-update behavior.
- **DOCUMENTED, APOLLO-PROGRAM EXPERIENCE:** TN D-7685 display-request/channel-allocation behavior.
- **DOCUMENTED, LATER SYSTEM BASELINE:** PHO-TR515 defines dynamic-field provenance metadata (telemetry measurement or DPB computation/MED/logic external name), display coordinates/configuration, and downlist indicators; it does not supply Apollo-11-effective MSK-1137 field routing or tabular cadence.
- **DOCUMENTED, PRE-APOLLO-11 BASELINE:** PHO-FAM001 generic display/device request transaction.
- **DOCUMENTED, ADJACENT EFFECTIVITY:** Apollo 12 DRK/MSK request semantics.
- **BLOCKED:** direct PHO-TN401 inspection; historical stochastic LR measurement generation.
- **UNRESOLVED:** Apollo 11 MSK-1137 external-name/downlist mapping, computed/logic provenance, numeric dynamic-data cadence/latency/freshness, and GUIDO exact request workflow.
