# Apollo 11 LR Mission-G configuration source-catalog addendum

Date: 2026-09-21
Parent: `resources/APOLLO11_LR_DOWNLINK_PROVENANCE_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| MSC Internal Note 69-FS-2, *Project Apollo 500 RTCC Operations Support Plan For Mission G*, April 1969 | Lists `PHO-TR155`, mission-specific Flight Controller Operations Handbook, mission-specific trajectory documentation, Mission Rules, Station Characteristics, and `Data Formats` among RTCC mission-support references | Apollo-11/Mission-G primary evidence identifying the relevant configuration/data-format document classes. Does not itself map MSK-1137 LR fields. |
| AC Electronics Apollo 11 manual | Identifies MSK-1137 among the LM CRT displays | Apollo-11 primary corroboration of the display identity. Does not supply the Mission-G ground parameter routing/conversion table. |
| Philco-Ford PHO-TR460, 1969 quarterly progress report, NTRS 19690029816 | Records final Mission-G third-floor display configuration; 1,272 cross-connect and 2,281 label changes; Mission-G configuration test status 100 percent at launch; release from Mission-G configuration on 28 July 1969 | Contemporaneous primary proof that a concrete tested Apollo-11 display configuration existed. Does not expose the LR parameter table in the recovered report. |
| Philco-Ford PHO-TR515 / NASA-CR-128843, *Display Formats Manual*, 12 Jan 1973 | Describes dynamic display data and says requirements/data-pack circulation plus computer listings feed PHO-TR155 Configuration and Control documentation | Later process evidence only. Useful for identifying the likely record chain; not Apollo-11-effective parameter evidence. |
| PHO-FAM001, Appendix A | Identifies MCC subsystem manual families, including telemetry and Display/Control interface documentation | Primary architecture/document-family lead. Does not provide Mission-G LR parameter mapping. |

## Controlled conclusion

Mission-specific display configuration is not hypothetical: primary 1969 documentation shows that a final Mission-G display configuration existed and was tested for launch, while the Mission-G RTCC plan explicitly points operators to PHO-TR155 and Data Formats. The remaining MSK-1137 LR provenance question therefore belongs in those mission-specific records rather than later configurations or generic architecture.

A targeted archive-focused search on 2026-09-21 re-recovered the Mission-G RTCC plan and Apollo 11 AC Electronics manual but did not surface a Mission-G PHO-TR155 MSK-1137 parameter package, associated data pack/computer listing, or Mission-G Data Formats LR table. This negative search result does not establish nonexistence; it establishes a current **source-recovery gate** because primary records already prove the configuration/document classes existed.

## Recovery target / reopen trigger

1. Mission-G/Apollo-11 PHO-TR155 material covering MSK-1137.
2. MSK-1137 display data pack/computer listing feeding that package.
3. Mission-G Data Formats record containing the LR dynamic-data identifiers/conversions.

Until one is recovered, the parameter-level source class is **BLOCKED ON SOURCE RECOVERY**. Do not continue broad searching merely to fill the bibliography, and do not back-project Apollo-15 configuration data.

## Sources

- https://www.ibiblio.org/apollo/Documents/RTCC%20Operations%20Support%20Plan%20for%20Mission%20G.pdf
- https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- https://ntrs.nasa.gov/api/citations/19690029816/downloads/19690029816.pdf
- https://ntrs.nasa.gov/citations/19730010501
- https://www.ibiblio.org/apollo/Documents/Familiarization%20Manual%20Mission%20Control%20Center%20Houston.pdf

## Evidence status

- **DOCUMENTED, MISSION-G PRIMARY:** relevant configuration/data-format reference classes.
- **DOCUMENTED, APOLLO-11 PRIMARY:** MSK-1137 LM CRT display identity.
- **DOCUMENTED, CONTEMPORANEOUS PRIMARY:** final tested Mission-G display configuration.
- **BLOCKED ON SOURCE RECOVERY:** parameter-level LR routing and conversion.
