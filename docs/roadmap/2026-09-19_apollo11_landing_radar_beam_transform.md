# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-20
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective LUMINARY 099 controls `SETPOS`, measurement-time CDU capture, Y-Z-X preparation, and `*NBSM*` direction semantics. Memo #95 controls antenna→NB beta-then-alpha semantics. The LM-5 Mission G prelaunch erasable load supplies the position-specific alpha/beta values.

## Completed

The equation-level SETPOS and SM/NB transforms are composed into the landing-radar velocity estimator chain, with a provenance-bearing LM-5 profile adapter. Mission-specific MSK-1137 evidence controls LR field identities, body-axis velocity frame, units/display masks, validity fields, and the ground-computed identity of `ACT ΔV`.

Apollo 11 MCC architecture is source-controlled as distinct spacecraft/downlink, CCATS/RTCC processing, Display/Control, and controller-presentation layers. PHO-TN401 is identified as the mission-specific Apollo 11 display-usage source but remains **BLOCKED** behind archival access.

NASA TN D-8316 narrows the timing boundary: D/TV generators buffered display instructions/data, so computer dynamic-data updates were independent of CRT refresh requirements and could replace either a complete instruction list or a single data word. Its four-second access requirement applies to reference slides, not dynamic telemetry cadence.

The 30 June 1967 Philco `PHO-FAM001`, *Mission Control Center Houston Familiarization Manual*, now constrains the pre-Apollo-11 Display/Control interface baseline. Its Computer Display/Control Interface description says display-request keyboards and encoders let an operator select up to 384 stored displays by pressing the desired-display switch and then the desired-display-device switch. This is direct pre-mission architecture evidence for the request transaction, but it does **not** identify Apollo 11 GUIDO's installed keyboard, button legends, or powered-descent selection. The Apollo 12 Saturn V Flight Manual remains adjacent-effectivity evidence that DRK labeled PBIs and MSK thumbwheel display-request mode were alternate mechanisms.

## Next work

1. Pursue Apollo-11-effective console configuration/controller procedure evidence for GUIDO's actual DRK/MSK installation, button/format mapping, and powered-descent selection. The generic request transaction itself is no longer wholly unknown.
2. Continue RTCC/CCATS research for per-field MSK-1137 routing and numeric dynamic-data latency/freshness.
3. Keep PHO-TN401 direct inspection **BLOCKED** pending archival retrieval/authenticated scan.
4. Keep sample/receive/process/display timestamps distinct; do not use the two-second onboard LR cadence or four-second reference-slide access as controller-display cadence.
5. Keep historical stochastic LR measurement generation **BLOCKED** until flight-effective numerical error evidence is recovered.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** LM-5 geometry + SETPOS + measurement-time NB→SM transform through the estimator.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR field semantics/formatting at field-definition level.
- **DOCUMENTED:** Apollo MCC architectural separation and D/TV buffered-update behavior; reference-slide access is distinct from dynamic-data update.
- **DOCUMENTED, PRE-APOLLO-11 BASELINE:** PHO-FAM001 defines the Display/Control request transaction and 384-display DRK/encoder capability; not station-assignment authority.
- **DOCUMENTED, ADJACENT EFFECTIVITY:** Apollo 12 flight manual defines DRK request behavior and its equivalence to MSK display-request mode; not authority for Apollo 11 GUIDO console configuration.
- **DOCUMENTED:** PHO-TN401 identity and archival location; HAER aggregate Apollo 11 display-usage reporting is secondary/indirect evidence only.
- **BLOCKED:** direct PHO-TN401 inspection; historical stochastic LR measurement generation.
- **UNRESOLVED:** Apollo 11 GUIDO DRK/MSK configuration, exact button/format mapping and powered-descent selection, per-field CCATS/RTCC routing, and numeric dynamic-data cadence/latency/freshness.
