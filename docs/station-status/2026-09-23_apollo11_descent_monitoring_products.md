# Station-status addendum — Apollo 11 descent monitoring products

Date: 2026-09-23
Parent: `docs/STATION_RESEARCH_STATUS.md`

The Apollo 13 station maturity table remains unchanged. This addendum applies only to the D-024 Apollo 11 powered-descent architecture reference.

## Source-backed boundary

NASA/MSC 70-FM-20 preserves Apollo 11 descent monitoring comparisons explicitly labeled `AGS−PGNCS` and `MSFN−PGNCS`, with in-plane/crossrange monitoring context and descent-event markers.

The mission-specific AC Electronics Apollo 11 manual defines `MSK-1137` ground-display fields directly relevant to powered descent/program alarms: `TIG`, `TGO`, significant-event timing, descent-only time-to-end-of-phase, LGC/ISS warning status, PGNCS/program caution status, first/second/most-recent alarm code, restart count, computer program, and DSKY verb/noun/flasher/rows.

NASA's Apollo 11 air-to-ground transcript establishes the crew-interface path: Eagle reports/requests alarm disposition and CAPCOM returns the ground GO disposition. NASA JSC's Jack Garman oral history further establishes that Garman and colleagues in the guidance-software back room supported Steve Bales in the front room; NASA's agency history identifies Bales as GUIDO and states that he called Garman for support on the 1202.

NASA/MSC's _Flight Mission Rules, Apollo 11_, rule 4-5, directly document the Mission-G MOCR loop vocabulary `FD LOOP`, `AFD CONF LOOP`, `MOCR SYS 1 & 2`, `MOCR DYN`, `A/G 1 LOOP`, and `A/G 2 LOOP`, while separately identifying an air-ground path used for crew communication.

## Station consequence

For the Apollo 11 reference, the historically supported alarm-assessment chain is **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**. This is sufficient to assign the front-room guidance assessment role to GUIDO and to represent back-room guidance-software support without inventing direct back-room-to-crew communication.

The Apollo 11 mission rules now make the loop terminology and internal-MOCR/A-G architectural split mission-specific rather than adjacent-mission evidence. They still do not justify assigning the GUIDO/support-room alarm conversation to `MOCR DYN`, `FD LOOP`, or any other named loop.

No broader station maturity is promoted. Exact Apollo 11 internal loop/channel assignment, per-console keyset privileges, station display request procedure, DRK mapping, routing, cadence, and per-alarm detailed call timing remain unresolved.

## Recovery target

PHO-TN401 is located in the **Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, Box 078-65/66**. Direct inspection remains required for usable Mission-G display/routing configuration evidence. Exact voice-loop mechanics require a station/keyset source unless PHO-TN401 itself supplies them.

## Next station research target

Recover PHO-TN401 or equivalent Apollo-11-effective configuration evidence and map the demonstrated comparison/MSK-1137 products to exact station requests, routing, DRK mapping, and cadence. Seek an Apollo-11-effective station/keyset document for GUIDO/support-room/FLIGHT loop assignments; rule 4-5 now supplies the mission-specific loop inventory but not station assignments.

## Evidence status

- **DOCUMENTED / SUFFICIENT:** Apollo-11-specific MSK-1137 alarm/program/descent field semantics.
- **DOCUMENTED / SUFFICIENT:** guidance-software back-room support → GUIDO assessment relationship; crew disposition is CAPCOM-mediated.
- **DOCUMENTED:** mission-specific independent-source descent comparison products.
- **DOCUMENTED / MISSION-SPECIFIC:** Apollo 11 MOCR loop vocabulary and internal-versus-A/G separation.
- **UNRESOLVED:** exact Apollo 11 live station request/routing/DRK mapping/cadence, station-to-loop assignment, keyset privileges, and detailed internal channel mechanics.
- **BLOCKED ON DOCUMENT RECOVERY:** direct PHO-TN401 inspection.
- **UNCHANGED:** Apollo 13 station maturity.