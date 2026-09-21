# Progress — Apollo 11 LR Mission-G source-recovery gate

Date: 2026-09-21
Roadmap: `docs/roadmap/2026-09-21_apollo11_lr_downlink_provenance.md`

## Question

Can the remaining parameter-level route from LUMINARY LR downlink words to MSK-1137 `VXB/VYB/VZB/RNG` be closed from presently accessible Mission-G primary records, or has the work reached a named source-recovery gate?

## Search performed

An archive-focused search was run against the already identified Mission-G document layer, using combinations of `MSK-1137`, `PHO-TR155`, `Mission G`, `VXB`, `VYB`, `VZB`, `RNG`, `landing radar`, and `Data Formats`.

The search re-recovered the Apollo-11/Mission-G RTCC Operations Support Plan (MSC Internal Note 69-FS-2), which explicitly names `PHO-TR155` and `Data Formats` as RTCC-area operational references, and the AC Electronics Apollo 11 manual, which independently identifies MSK-1137 as an LM CRT display. It did **not** recover a Mission-G PHO-TR155 parameter package, MSK-1137 data pack/computer listing, or Mission-G Data Formats table containing the LR field identifiers/conversions.

No later-mission configuration was promoted to Apollo-11 evidence.

## Controlled conclusion

The parameter-level MSK-1137 LR provenance question is now **BLOCKED on named source recovery**, not an open-ended web-research task. The discriminating evidence is one of:

1. Mission-G/Apollo-11-effective PHO-TR155 material covering MSK-1137;
2. the associated MSK-1137 display data pack/computer listing; or
3. Mission-G Data Formats material that identifies the LR dynamic-data source and engineering conversion.

Until such a record is recovered, the project cannot choose CCATS-selected telemetry versus RTCC display/control data, assign historical ground parameter mnemonics/conversion coefficients, or claim an exact ground route.

This is a source-availability result, not evidence that the records never existed. PHO-TR460 and 69-FS-2 already establish that a tested Mission-G display configuration and the relevant configuration/data-format document classes existed.

## Simulation consequence

Keep the neutral ground-processing adapter between the documented LGC LR downlink words and documented MSK-1137 LR products. Do not encode historical CCATS/RTCC ownership, conversion coefficients, latency, or refresh cadence from inference.

The broader Apollo 11 powered-descent/program-alarm research thread remains active; only this parameter-level ground-display subquestion is blocked.

## Reopen trigger

Reopen immediately if a Mission-G PHO-TR155 package, MSK-1137 data pack/listing, or Mission-G Data Formats record becomes directly accessible.

## Sources

- MSC Internal Note 69-FS-2, *Project Apollo 500 RTCC Operations Support Plan For Mission G*, April 1969: https://www.ibiblio.org/apollo/Documents/RTCC%20Operations%20Support%20Plan%20for%20Mission%20G.pdf
- AC Electronics, Apollo 11 manual: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- Philco-Ford PHO-TR460, NTRS 19690029816: https://ntrs.nasa.gov/api/citations/19690029816/downloads/19690029816.pdf

## Evidence status

- **DOCUMENTED, MISSION-G PRIMARY:** PHO-TR155 and Data Formats were operational reference classes.
- **DOCUMENTED, APOLLO-11 PRIMARY:** MSK-1137 was an LM CRT display.
- **BLOCKED ON SOURCE RECOVERY:** parameter identifiers, engineering conversion, and CCATS-versus-RTCC route for MSK-1137 LR fields.
- **NOT ESTABLISHED:** exact historical ground routing, conversion coefficients, latency, or refresh cadence.
