# Station-status addendum — Apollo 11 descent monitoring products

Date: 2026-09-23
Parent: `docs/STATION_RESEARCH_STATUS.md`

The Apollo 13 station maturity table remains unchanged. This addendum applies only to the D-024 Apollo 11 powered-descent architecture reference.

## Source-backed boundary

NASA/MSC 70-FM-20 preserves Apollo 11 descent monitoring comparisons explicitly labeled `AGS−PGNCS` and `MSFN−PGNCS`, with in-plane/crossrange monitoring context and descent-event markers.

The mission-specific AC Electronics Apollo 11 manual defines `MSK-1137` ground-display fields directly relevant to powered descent/program alarms: `TIG`, `TGO`, significant-event timing, descent-only time-to-end-of-phase, LGC/ISS warning status, PGNCS/program caution status, first/second/most-recent alarm code, restart count, computer program, and DSKY verb/noun/flasher/rows.

NASA's Apollo 11 air-to-ground transcript establishes the crew-interface path: Eagle reports/requests alarm disposition and CAPCOM returns the ground GO disposition. NASA JSC's Jack Garman oral history further establishes that Garman and colleagues in the guidance-software back room supported Steve Bales in the front room; NASA's agency history identifies Bales as GUIDO and states that he called Garman for support on the 1202.

## Station consequence

For the Apollo 11 reference, the historically supported alarm-assessment chain is **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**. This is sufficient to assign the front-room guidance assessment role to GUIDO and to represent back-room guidance-software support without inventing direct back-room-to-crew communication.

No broader station maturity is promoted. Exact internal loop/channel identity, console keying, station display request procedure, DRK mapping, routing, cadence, and per-alarm detailed call timing remain unresolved.

## Recovery target

PHO-TN401 is located in the **Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, Box 078-65/66**. Direct inspection remains required for usable Mission-G routing/configuration evidence. Exact voice-loop mechanics may require an additional mission-effective loop/configuration source.

## Next station research target

Recover PHO-TN401 or equivalent Apollo-11-effective configuration evidence and map the demonstrated comparison/MSK-1137 products to exact station requests, routing, DRK mapping, and cadence. Seek separate loop documentation if PHO-TN401 does not identify the back-room/GUIDO/FLIGHT channel mechanics.

## Evidence status

- **DOCUMENTED / SUFFICIENT:** Apollo-11-specific MSK-1137 alarm/program/descent field semantics.
- **DOCUMENTED / SUFFICIENT:** guidance-software back-room support → GUIDO assessment relationship; crew disposition is CAPCOM-mediated.
- **DOCUMENTED:** mission-specific independent-source descent comparison products.
- **UNRESOLVED:** exact live station request/routing/DRK mapping/cadence and internal loop/channel mechanics.
- **BLOCKED ON DOCUMENT RECOVERY:** direct PHO-TN401 inspection.
- **UNCHANGED:** Apollo 13 station maturity.