# Apollo 11 LR downlink-provenance source-catalog addendum

Date: 2026-09-21
Parent: `resources/APOLLO11_LR_SCALE_SELECTION_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Flown LUMINARY 099 `ERASABLE_ASSIGNMENTS.agc` | Seven-word `RENDEZVOUS AND LANDING RADAR DOWNLINK STORAGE`; names `DNLRVELX`, `DNLRVELY`, `DNLRVELZ`, `DNLRALT` | Apollo-11-effective proof that explicit LR quantities were reserved for downlink. Does not establish MCC display routing. |
| Flown LUMINARY 099 `DOWNLINK_LISTS.agc` | Explicitly emits `DNLRVELX/Y/Z/DNLRALT` in LM downlink lists; also places `DNLRVELZ/DNLRALT` in the orbital-maneuvers list | Apollo-11-effective downlink availability. Do not equate a downlink-list position with a ground display field without ground documentation. |
| AC Electronics, *Apollo 11 Manual*, MSK-1137 | `VXB/VYB/VZB` = LR body-axis velocity; `RNG` = LR slant-range altitude; LR validity fields | Mission-specific controller product semantics. Does not state the exact telemetry/RTCC routing for each field. |
| TRW Systems Group, *Apollo Mission 11, Trajectory Reconstruction and Postflight Analysis, Volume 1*, NASA-CR-108349 / TRW-11176-H508-R0-00, §7.4 | LR data were obtained by processing downlink telemetry with a special-purpose program into onboard observations; HOPE then used those observations with trajectory/REFSMAT/gimbal/radar-mode data. §7.4.1 separately identifies an RTCC trajectory obtained in real time. | Apollo-11-specific proof of a telemetry-derived LR-observation path and separation from an RTCC trajectory product. This is a postflight-analysis description: do **not** treat its special-purpose program as the real-time MSK-1137 path or infer per-field display routing from it. |

## Controlled conclusion

The spacecraft-to-ground provenance gap is narrowed substantially: Apollo 11 LUMINARY itself supplied named landing-radar velocity and altitude quantities in its downlink, and Apollo-11-specific postflight documentation confirms that LR observables could be recovered by processing downlink telemetry. The same report describes an RTCC real-time descent trajectory separately, so the evidence does not justify silently inserting an RTCC transformation into the LR measurement/display path.

The remaining question is the **real-time** engineering conversion and routing from the LGC words to MSK-1137. Matching names/semantics are insufficient to assert one-to-one routing. Preserve an explicit unresolved telemetry/FDS/CCATS/display layer until Apollo-11-effective real-time documentation is recovered.

## Sources

- https://www.ibiblio.org/apollo/listings/Luminary099/ERASABLE_ASSIGNMENTS.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/DOWNLINK_LISTS.agc.html
- https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19700014995.pdf

## Evidence status

- **DOCUMENTED:** Apollo-11-effective LR downlink source family.
- **DOCUMENTED:** Apollo-11 controller-visible LR products.
- **DOCUMENTED, APOLLO-11-SPECIFIC:** postflight LR observations derived from downlink telemetry; RTCC real-time trajectory described separately.
- **UNRESOLVED:** exact real-time ground engineering conversion and per-field MSK-1137 routing.
