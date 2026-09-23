# Progress — Apollo 11 descent monitoring products

Date: 2026-09-23

Continued the open Apollo 11 powered-descent controller-product reference.

## Primary-source result — comparison products

NASA/MSC **70-FM-20, _The Apollo 11 Adventure_** preserves Apollo 11 descent strip-chart comparisons labeled `AGS−PGNCS` and `MSFN−PGNCS`, with descent-event markers and in-plane/crossrange monitoring logic. This supports the repository's pairwise/consensus architecture without establishing exact live CRT presentation.

## Primary-source result — program-alarm/descent fields

The mission-specific AC Electronics _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137`, establishes ground-visible `TIG`, `TGO`, significant-event timing, descent-only time-to-end-of-phase, LGC/ISS warning status, PGNCS/program caution status, first/second/most-recent alarm code, restart count, computer program, and DSKY verb/noun/flasher/rows.

## Primary-source result — crew-interface alarm call path

NASA's _Apollo 11 Air-to-Ground Voice Transcription (GOSS NET 1)_, Tape 66/7 p. 312, records the first 1202 sequence at `04 06 38 26–53`: Eagle announces the program alarm and code, the CDR asks Houston for a reading, and `CC`/CAPCOM returns the ground GO disposition. The transcript then records Houston telling Eagle that it will monitor `DELTA-H`.

This closes one previously broad part of “call ownership”: **the crew-facing alarm disposition is CAPCOM-mediated**. It does not identify the internal controller/support-room assessment path that produced the GO recommendation.

## Boundary preserved

MSK-1137 field semantics do **not** establish which station requested the display at a given moment, the exact DRK legend/button mapping, update cadence/latency, or internal controller decision rules. The air-ground transcript does **not** establish which internal controller/support-room position generated the alarm recommendation. Likewise, 70-FM-20 Figure 9 is not treated as an exact live MOCR display.

## Archival target

PHO-TN401 remains the leading direct display/control recovery target at Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, **Box 078-65/66**.

## Next discriminating target

Recover PHO-TN401 or another Apollo-11-effective configuration/loop source to map the documented MSK-1137/comparison products to exact station requests/routing/DRK mapping/cadence and determine the internal alarm-assessment path. Do not infer those details from the field inventory or air-ground transcript.

## Sources

- NASA, _Apollo 11 Air-to-Ground Voice Transcription (GOSS NET 1)_, Tape 66/7 p. 312: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics, _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137`: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC MPAD, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 February 1970: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- LOC/NPS, HAER No. TX-109-C, _Johnson Space Center, Apollo Mission Control_: https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf

## Evidence status

- **DOCUMENTED / SUFFICIENT:** MSK-1137 alarm/restart/program/DSKY/descent field semantics.
- **DOCUMENTED / SUFFICIENT:** spacecraft-to-ground request/report and CAPCOM-to-spacecraft alarm disposition path.
- **DOCUMENTED:** Apollo 11 AGS−PGNCS and MSFN−PGNCS comparison-product family.
- **UNRESOLVED:** exact live station request/routing/DRK mapping/cadence and internal alarm-assessment ownership.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection.