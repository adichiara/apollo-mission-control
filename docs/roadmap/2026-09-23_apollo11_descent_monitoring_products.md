# Roadmap addendum — Apollo 11 descent monitoring products

Date: 2026-09-23

## Status change

The Apollo 11 powered-descent controller-product boundary is now supported by two complementary mission-specific product families. NASA/MSC 70-FM-20 preserves `AGS−PGNCS` and `MSFN−PGNCS` descent comparisons. The AC Electronics Apollo 11 manual's `MSK-1137` definition additionally establishes ground-visible descent timing, warning/caution, alarm-code, restart-count, computer-program, and DSKY-context fields.

This means the program-alarm interval can be represented with sourced ground products rather than a modern invented alarm panel or hidden AGC state.

## Immediate next work

1. Keep the Apollo 11 reference **OPEN**, but mark the **MSK-1137 alarm/program field semantics SUFFICIENT** for current controller-product architecture.
2. Preserve `AGS−PGNCS` and `MSFN−PGNCS` as distinct comparison products.
3. Preserve MSK-1137's documented alarm codes, restart count, program number, DSKY context, `TGO`, and descent-only time-to-end-of-phase as controller-product semantics; do not assign unsupported station ownership or request timing.
4. Do not expose 70-FM-20 Figure 9 as an exact live MOCR display.
5. Recover Mission-G-effective routing/configuration evidence. PHO-TN401 remains the strongest target and is located at the Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, **Box 078-65/66**.
6. Freeze exact station request/routing, DRK-button mapping, and cadence only after direct mission-effective evidence is recovered.

## Sources

- AC Electronics, _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137`: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 February 1970: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- Library of Congress / Historic American Engineering Record, _Johnson Space Center, Apollo Mission Control_, HAER No. TX-109-C: https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf

## Evidence status

- **SUFFICIENT:** Apollo-11-specific MSK-1137 alarm/program/descent field semantics for current product architecture.
- **OPEN:** exact station request/routing, DRK mapping, cadence/latency, and call ownership.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection.