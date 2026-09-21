# Apollo 11 LR downlink provenance — progress

Date: 2026-09-21

## Question

What primary Apollo-11-effective evidence constrains the ground provenance of the landing-radar values displayed on MSK-1137?

## Primary evidence recovered

Flown LUMINARY 099 contains an explicit seven-word `RENDEZVOUS AND LANDING RADAR DOWNLINK STORAGE` block in `ERASABLE_ASSIGNMENTS.agc`. The four LR words are named `DNLRVELX`, `DNLRVELY`, `DNLRVELZ`, and `DNLRALT`; the source comment says the block is normally used during P20 and may also be required for the V62 spurious test.

`DOWNLINK_LISTS.agc` explicitly places `DNLRVELX,DNLRVELY,DNLRVELZ,DNLRALT` into Apollo-11 LGC downlink lists. The same source places `DNLRVELZ,DNLRALT` in the orbital-maneuvers list and all four LR words in other LM lists, including the coast/align list. This is Apollo-11-effective evidence that the LGC provided named LR velocity/altitude quantities to the telemetry/downlink path; they were not available to MCC only by an undocumented reconstruction from unrelated telemetry.

The Apollo 11 AC Electronics manual independently defines MSK-1137 controller fields `VXB/VYB/VZB` as landing-radar velocity in body-axis coordinates and `RNG` as LR slant-range altitude.

## Controlled conclusion

This closes one layer of the provenance chain: **spacecraft LGC → downlink contains explicit LR velocity/altitude words → ground processing → MSK-1137 LR products**. It materially narrows the prior open question.

It does **not** by itself prove a one-to-one routing from `DNLRVELX/Y/Z/DNLRALT` to the displayed `VXB/VYB/VZB/RNG` fields. The exact CCATS/RTCC engineering conversion, coordinate/scale handling, display-database parameter identifiers, and whether any displayed field was transformed after receipt remain unresolved. Do not label the MSK fields as raw downlink values until mission-effective ground documentation closes that mapping.

## Sources

- Flown Apollo 11 LUMINARY 099 `ERASABLE_ASSIGNMENTS.agc`, radar downlink-storage block.
- Flown Apollo 11 LUMINARY 099 `DOWNLINK_LISTS.agc`, LM downlink lists.
- AC Electronics, *Apollo 11 Manual*, MSK-1137 definition.

## Next target

Seek Apollo-11-effective telemetry/FDS/RTCC parameter documentation that maps `DNLRVELX/Y/Z/DNLRALT` (or their telemetry word positions) to the engineering-unit/display fields on MSK-1137. Preserve CCATS/RTCC/display layers separately.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** explicit LGC landing-radar downlink storage exists for X/Y/Z velocity and altitude.
- **DOCUMENTED, APOLLO-11-EFFECTIVE:** those named LR words are included in LGC downlink lists.
- **DOCUMENTED, APOLLO-11 CONTROLLER DISPLAY:** MSK-1137 exposes LR body-axis velocity and slant range.
- **UNRESOLVED:** exact ground conversion/routing from the named downlink words to individual MSK-1137 fields.
