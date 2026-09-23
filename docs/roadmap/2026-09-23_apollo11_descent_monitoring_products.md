# Roadmap addendum — Apollo 11 descent monitoring products

Date: 2026-09-23

## Status change

The Apollo 11 powered-descent controller-product boundary is now supported by two complementary mission-specific product families. NASA/MSC 70-FM-20 preserves `AGS−PGNCS` and `MSFN−PGNCS` descent comparisons. The AC Electronics Apollo 11 manual's `MSK-1137` definition additionally establishes ground-visible descent timing, warning/caution, alarm-code, restart-count, computer-program, and DSKY-context fields.

NASA's Apollo 11 air-to-ground voice transcription now also closes the crew-interface portion of alarm call ownership: Eagle reported/requested disposition of the first 1202 over air-ground, and `CC`/CAPCOM returned the ground GO disposition. Internal controller/support-room assessment ownership remains open.

This means the program-alarm interval can be represented with sourced ground products and a sourced CAPCOM-mediated crew call rather than a modern invented alarm panel, hidden AGC state, or direct controller-to-spacecraft speech.

## Immediate next work

1. Keep the Apollo 11 reference **OPEN**, but mark the **MSK-1137 alarm/program field semantics SUFFICIENT** for current controller-product architecture.
2. Preserve `AGS−PGNCS` and `MSFN−PGNCS` as distinct comparison products.
3. Preserve MSK-1137's documented alarm codes, restart count, program number, DSKY context, `TGO`, and descent-only time-to-end-of-phase as controller-product semantics; do not assign unsupported station ownership or request timing.
4. Preserve the primary-transcript call boundary: spacecraft alarm/request → ground assessment → CAPCOM disposition to crew. Do not expose an internal controller as speaking directly to Eagle.
5. Do not expose 70-FM-20 Figure 9 as an exact live MOCR display.
6. Recover Mission-G-effective routing/configuration evidence. PHO-TN401 remains the strongest target and is located at the Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, **Box 078-65/66**.
7. Freeze exact station request/routing, DRK-button mapping, cadence, and internal alarm-assessment ownership only after direct mission-effective evidence is recovered.

## Sources

- NASA, _Apollo 11 Air-to-Ground Voice Transcription (GOSS NET 1)_, Tape 66/7 p. 312: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics, _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137`: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 February 1970: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- Library of Congress / Historic American Engineering Record, _Johnson Space Center, Apollo Mission Control_, HAER No. TX-109-C: https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf

## Evidence status

- **SUFFICIENT:** Apollo-11-specific MSK-1137 alarm/program/descent field semantics for current product architecture.
- **SUFFICIENT:** crew-interface alarm call path — spacecraft request/report and CAPCOM ground disposition.
- **OPEN:** exact station request/routing, DRK mapping, cadence/latency, and internal assessment ownership.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection.