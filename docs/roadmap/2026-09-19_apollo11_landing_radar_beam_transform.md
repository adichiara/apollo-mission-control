# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-20
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective LUMINARY 099 controls `SETPOS`, measurement-time CDU capture, Y-Z-X preparation, and `*NBSM*` direction semantics. Memo #95 controls antenna→NB beta-then-alpha semantics. The LM-5 Mission G prelaunch erasable load supplies the position-specific alpha/beta values.

## Completed

The equation-level SETPOS and SM/NB transforms are composed into the landing-radar velocity estimator chain, with a provenance-bearing LM-5 profile adapter. Mission-specific MSK-1137 evidence controls LR field identities, body-axis velocity frame, units/display masks, validity fields, and the ground-computed identity of `ACT ΔV`.

Apollo 11 MCC architecture is source-controlled as distinct spacecraft/downlink, CCATS/RTCC processing, Display/Control, and controller-presentation layers. PHO-TN401 is identified as the mission-specific Apollo 11 display-usage source but remains **BLOCKED** behind archival access.

NASA TN D-8316 now narrows the remaining timing boundary: D/TV generators buffered display instructions/data, so computer dynamic-data updates were independent of CRT refresh requirements and could replace either a complete instruction list or a single data word. The report's four-second access requirement applies to reference slides, not dynamic telemetry cadence. Therefore CRT refresh, dynamic-word update, operator request latency, and reference-slide access must not be collapsed into one timing constant.

## Next work

1. Continue accessible mission-era RTCC/CCATS/Display-Control/controller-procedure research only where it can establish Apollo 11 GUIDO/MSK-1137 routing, request semantics, or numeric dynamic-data latency/freshness.
2. Keep PHO-TN401 direct inspection **BLOCKED** pending archival retrieval/authenticated scan.
3. Keep sample/receive/process/display timestamps distinct; do not use the two-second onboard LR cadence or four-second reference-slide access as controller-display cadence.
4. Keep historical stochastic LR measurement generation **BLOCKED** until flight-effective numerical error evidence is recovered.
5. Preserve optional yaAGC/fixed-point comparison as validation hardening if later required.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** LM-5 geometry + SETPOS + measurement-time NB→SM transform through the estimator.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR field semantics/formatting at field-definition level.
- **DOCUMENTED:** Apollo MCC architectural separation and D/TV buffered-update behavior; reference-slide access is distinct from dynamic-data update.
- **DOCUMENTED:** PHO-TN401 identity and archival location; HAER aggregate Apollo 11 display-usage reporting is secondary/indirect evidence only.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point equivalence.
- **BLOCKED:** direct PHO-TN401 inspection; historical stochastic LR measurement generation.
- **UNRESOLVED:** exact per-field Apollo 11 CCATS/RTCC transformation/routing, numeric dynamic-data cadence/latency/freshness, powered-descent display selection, and GUIDO request/key workflow.