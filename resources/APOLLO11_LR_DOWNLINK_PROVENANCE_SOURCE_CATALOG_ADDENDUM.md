# Apollo 11 LR downlink-provenance source-catalog addendum

Date: 2026-09-21
Parent: `resources/APOLLO11_LR_SCALE_SELECTION_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Flown LUMINARY 099 `ERASABLE_ASSIGNMENTS.agc` | Seven-word `RENDEZVOUS AND LANDING RADAR DOWNLINK STORAGE`; names `DNLRVELX`, `DNLRVELY`, `DNLRVELZ`, `DNLRALT` | Apollo-11-effective proof that explicit LR quantities were reserved for downlink. Does not establish MCC display routing. |
| Flown LUMINARY 099 `DOWNLINK_LISTS.agc` | Explicitly emits `DNLRVELX/Y/Z/DNLRALT` in LM downlink lists; also places `DNLRVELZ/DNLRALT` in the orbital-maneuvers list | Apollo-11-effective downlink availability. Do not equate a downlink-list position with a ground display field without ground documentation. |
| AC Electronics, *Apollo 11 Manual*, MSK-1137 | `VXB/VYB/VZB` = LR body-axis velocity; `RNG` = LR slant-range altitude; LR validity fields | Mission-specific controller product semantics. Does not state the exact telemetry/RTCC routing for each field. |

## Controlled conclusion

The spacecraft-to-ground provenance gap is narrowed substantially: Apollo 11 LUMINARY itself supplied named landing-radar velocity and altitude quantities in its downlink. The remaining question is no longer whether LR measurements existed in the downlink, but exactly how MCC telemetry processing converted/routed those words to MSK-1137.

Matching names/semantics are insufficient to assert one-to-one routing. Preserve an explicit unresolved ground-processing layer until Apollo-11-effective CCATS/RTCC/FDS parameter documentation is recovered.

## Sources

- https://www.ibiblio.org/apollo/listings/Luminary099/ERASABLE_ASSIGNMENTS.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/DOWNLINK_LISTS.agc.html
- https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf

## Evidence status

- **DOCUMENTED:** Apollo-11-effective LR downlink source family.
- **DOCUMENTED:** Apollo-11 controller-visible LR products.
- **UNRESOLVED:** exact ground engineering conversion and per-field MSK-1137 routing.
