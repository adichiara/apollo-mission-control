# Station-status addendum — Apollo 11 descent monitoring products

Date: 2026-09-23
Parent: `docs/STATION_RESEARCH_STATUS.md`

The Apollo 13 station maturity table remains unchanged. This addendum applies only to the D-024 Apollo 11 powered-descent architecture reference.

## Source-backed boundary

NASA/MSC 70-FM-20 preserves Apollo 11 descent monitoring comparisons explicitly labeled `AGS−PGNCS` and `MSFN−PGNCS`. The mission-specific AC Electronics Apollo 11 manual defines `MSK-1137` ground-display fields relevant to powered descent/program alarms.

NASA's Apollo 11 air-to-ground transcript establishes the crew-interface path: Eagle reports/requests alarm disposition and CAPCOM returns the ground GO disposition. NASA JSC's Jack Garman oral history establishes that Garman and colleagues in the guidance-software back room supported Steve Bales in the front room.

NASA/MSC's _Flight Mission Rules, Apollo 11_, rule 4-5, directly documents the Mission-G MOCR loop vocabulary `FD LOOP`, `AFD CONF LOOP`, `MOCR SYS 1 & 2`, `MOCR DYN`, `A/G 1 LOOP`, and `A/G 2 LOOP`.

Garman's firsthand description now adds the keyset-level architectural distinction that was previously missing: white buttons were talk privileges, amber buttons were listen privileges, multiple loops could be monitored simultaneously, and support-room personnel could monitor A/G while A/G talk authority was restricted. He recalls the support position receiving an FD-loop talk button only "later on," but does not date that change precisely enough to establish the Apollo 11 keyset matrix.

## Station consequence

For the Apollo 11 reference, the supported alarm-assessment chain remains **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**.

The communications model should now distinguish **monitor** from **talk** permission rather than treating loop membership as binary. Do not grant back-room AGC support direct A/G transmit authority. Do not assign the Bales/Garman assessment to `FD LOOP`, `MOCR DYN`, or another named loop from the present evidence. Garman's date-imprecise recollection of the later FD talk button is a constraint, not proof of the exact 20 July 1969 configuration.

No broader station maturity is promoted. Exact Apollo 11 internal loop assignment, complete per-console keyset privileges, station display request procedure, DRK mapping, routing, cadence, and per-alarm detailed call timing remain unresolved.

## Recovery target

PHO-TN401 remains located in the **Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, Box 078-65/66**. Direct inspection remains required for usable Mission-G display/routing configuration evidence. A Mission-G-effective station/keyset record remains the discriminating voice-routing target.

## Evidence status

- **DOCUMENTED / SUFFICIENT:** Apollo-11-specific MSK-1137 alarm/program/descent field semantics.
- **DOCUMENTED / SUFFICIENT:** guidance-software back-room support → GUIDO assessment relationship; crew disposition is CAPCOM-mediated.
- **DOCUMENTED / MISSION-SPECIFIC:** Apollo 11 MOCR loop vocabulary and internal-versus-A/G separation.
- **DOCUMENTED / PARTICIPANT:** support-room talk/listen distinction, multi-loop monitoring, and restricted A/G transmit authority.
- **DATE-IMPRECISE:** Garman's recollection that FD-loop talk capability was added to the support position later.
- **UNRESOLVED:** exact Apollo 11 station-to-loop assignment, complete keyset privilege matrix, live station request/routing/DRK mapping/cadence, and detailed internal channel mechanics.
- **BLOCKED ON DOCUMENT RECOVERY:** direct PHO-TN401 inspection.
- **UNCHANGED:** Apollo 13 station maturity.