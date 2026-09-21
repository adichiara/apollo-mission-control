# Progress — Apollo 11 LR Mission-G display-configuration target

Date: 2026-09-21
Roadmap: `docs/roadmap/2026-09-21_apollo11_lr_downlink_provenance.md`

## Question

What primary record is most likely to resolve the remaining real-time mapping from LUMINARY landing-radar downlink quantities to MSK-1137 `VXB/VYB/VZB/RNG`?

## Primary-source result

The Apollo-11/Mission-G RTCC Operations Support Plan, MSC Internal Note 69-FS-2 (April 1969), explicitly lists `PHO-TR155` and `Data Formats` among the reference documents maintained in the RTCC computer-control area.

Philco-Ford quarterly report PHO-TR460, covering the period that includes Apollo 11, independently establishes that a final **Mission G third-floor display-system configuration** existed. It reports 1,272 cross-connect changes and 2,281 label changes for that final Mission-G display configuration, says Mission-G configuration test status was 100 percent at launch, and records release of the third-floor display system from Mission-G configuration on 28 July 1969 before installation of the Mission H-1 PHO-TR155 package.

PHO-TR515 (1973) is later than Apollo 11 and is therefore not used as mission-effective parameter evidence. It is useful only for document-process provenance: it states that display requirements were gathered through data-pack circulation and that computer listings were used to prepare PHO-TR155, the Configuration and Control Document.

## Controlled conclusion

The next discriminating evidence is not another generic MCC architecture description. Apollo-11-specific configuration records demonstrably existed, and the primary Mission-G RTCC plan identifies PHO-TR155 and Data Formats as operational references. A Mission-G PHO-TR155 package, its underlying display data pack, or corresponding Data Formats record is therefore the correct next source target for resolving MSK-1137 LR field routing.

No recovered source in this pass provides the actual `VXB/VYB/VZB/RNG` parameter identifiers or chooses CCATS-selected telemetry versus RTCC display/control data. The route remains unresolved; the available Apollo-15 PHO-TR155 must not be back-projected to Apollo 11.

## Simulation consequence

No code/model change is justified. Continue to use a neutral ground-processing adapter between the documented LGC LR downlink words and the documented MSK-1137 LR products. Do not assign that adapter to CCATS or RTCC until Mission-G parameter-level evidence is recovered.

## Next target

Archive-focused recovery of Mission-G/Apollo-11 PHO-TR155, MSK-1137 display data pack, or Data Formats documentation. Search display number plus `VXB`, `VYB`, `VZB`, `RNG`, landing radar, and telemetry/downlink identifiers.

## Sources

- MSC Internal Note 69-FS-2, *Project Apollo 500 RTCC Operations Support Plan For Mission G*, April 1969: https://www.ibiblio.org/apollo/Documents/RTCC%20Operations%20Support%20Plan%20for%20Mission%20G.pdf
- Philco-Ford PHO-TR460, quarterly progress report, 1969, NTRS 19690029816: https://ntrs.nasa.gov/api/citations/19690029816/downloads/19690029816.pdf
- Philco-Ford PHO-TR515 / NASA-CR-128843, *Display Formats Manual*, 12 January 1973: https://ntrs.nasa.gov/citations/19730010501

## Evidence status

- **DOCUMENTED, APOLLO-11/MISSION-G PRIMARY:** PHO-TR155 and Data Formats were RTCC-area operational reference-document classes.
- **DOCUMENTED, CONTEMPORANEOUS PRIMARY:** final Mission-G third-floor display configuration existed and configuration testing was complete at launch.
- **DOCUMENTED, LATER PROCESS DESCRIPTION:** display data packs/computer listings fed PHO-TR155 configuration documentation.
- **UNRESOLVED:** MSK-1137 LR parameter identifiers, engineering conversion, and CCATS-versus-RTCC source class.
