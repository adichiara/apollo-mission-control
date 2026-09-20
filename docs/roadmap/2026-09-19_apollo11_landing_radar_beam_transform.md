# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-20
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective LUMINARY 099 controls `SETPOS`, measurement-time CDU capture, Y-Z-X preparation, and `*NBSM*` direction semantics. Memo #95 controls antenna→NB beta-then-alpha semantics. The LM-5 Mission G prelaunch erasable load supplies the position-specific alpha/beta values.

## Completed

The equation-level SETPOS and SM/NB transforms are composed into the landing-radar velocity estimator chain, with a provenance-bearing LM-5 profile adapter. Mission-specific MSK-1137 evidence controls LR field identities, body-axis velocity frame, units/display masks, validity fields, and the ground-computed identity of `ACT ΔV`.

Apollo 11 MCC architecture is source-controlled as distinct spacecraft/downlink, CCATS/RTCC processing, Display/Control, and controller-presentation layers. PHO-TN401 is identified as the mission-specific Apollo 11 display-usage source but remains **BLOCKED** behind archival access.

NASA TN D-8316 narrows the timing boundary: D/TV generators buffered display instructions/data, so computer dynamic-data updates were independent of CRT refresh requirements and could replace either a complete instruction list or a single data word. Its four-second access requirement applies to reference slides, not dynamic telemetry cadence.

A primary NASA Apollo 12 Saturn V Flight Manual constrains the adjacent display-request mechanism without being back-projected as an Apollo 11 station configuration. It states that the Display Request Keyboard (DRK) requested a specific RTCC display format by labeled PBI and provided the same capability as the MSK in display-request mode, but faster because thumbwheel selection was unnecessary.

Research 400 now tightens the effectivity boundary further. The Apollo 11 AC Electronics manual explicitly places MSK-1137 in the `ASPO 45 CRT DISPLAYS` family; Apollo 12 and NASA-hosted Apollo 15 Delco manuals preserve the same four-format family. This establishes format-family continuity, not GUIDO ownership. A targeted Apollo-11-effective search did not recover primary evidence assigning DRK/MSK hardware or MSK-1137 request workflow to GUIDO.

## Next work

1. Keep Apollo 11 GUIDO request hardware/workflow **UNRESOLVED** until mission-effective console configuration, controller procedure, or shift material is recovered.
2. Continue RTCC/CCATS research for per-field MSK-1137 routing and numeric dynamic-data latency/freshness.
3. Keep PHO-TN401 direct inspection **BLOCKED** pending archival retrieval/authenticated scan; it remains the next discriminating mission-specific display-usage source.
4. Keep sample/receive/process/display timestamps distinct; do not use the two-second onboard LR cadence or four-second reference-slide access as controller-display cadence.
5. Keep historical stochastic LR measurement generation **BLOCKED** until flight-effective numerical error evidence is recovered.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** LM-5 geometry + SETPOS + measurement-time NB→SM transform through the estimator.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR field semantics/formatting and ASPO 45 format identity.
- **DOCUMENTED:** ASPO 45 MSK-1137 display-family continuity across recovered Apollo 11/12/15 manuals; not station-assignment authority.
- **DOCUMENTED:** Apollo MCC architectural separation and D/TV buffered-update behavior; reference-slide access is distinct from dynamic-data update.
- **DOCUMENTED, ADJACENT EFFECTIVITY:** Apollo 12 flight manual defines DRK request behavior and its equivalence to MSK display-request mode; not authority for Apollo 11 GUIDO console configuration.
- **DOCUMENTED:** PHO-TN401 identity and archival location; HAER aggregate Apollo 11 display-usage reporting is secondary/indirect evidence only.
- **BLOCKED:** direct PHO-TN401 inspection; historical stochastic LR measurement generation.
- **UNRESOLVED:** Apollo 11 GUIDO DRK/MSK configuration and exact request sequence, per-field CCATS/RTCC routing, numeric dynamic-data cadence/latency/freshness, and powered-descent display selection.
