# Roadmap addendum — Apollo 11 descent monitoring products

Date: 2026-09-23

## Status change

The Apollo 11 powered-descent controller-product boundary is supported by mission-specific product evidence: NASA/MSC 70-FM-20 preserves `AGS−PGNCS` and `MSFN−PGNCS` descent comparisons, while AC Electronics `MSK-1137` establishes ground-visible descent timing, warning/caution, alarm-code, restart-count, computer-program, and DSKY-context fields.

The supported alarm architecture remains **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**. NASA/MSC Apollo 11 Mission Rules rule 4-5 supplies mission-specific loop vocabulary: `FD LOOP`, `AFD CONF LOOP`, `MOCR SYS 1 & 2`, `MOCR DYN`, `A/G 1 LOOP`, and `A/G 2 LOOP`.

Jack Garman's NASA JSC oral history now adds primary-participant keyset semantics: Apollo support-room communications distinguished white **talk** buttons from amber **listen** buttons, supported simultaneous monitoring of multiple loops, and allowed support personnel to monitor air-ground without general air-ground transmit authority. Garman recalls that the support position gained an FD-loop talk button only "later on"; the date is too imprecise to freeze an Apollo 11 FD-loop privilege, but it makes a presumed direct support-room → FD talk path unsafe.

## Immediate next work

1. Keep the Apollo 11 reference **OPEN**, but mark the **MSK-1137 alarm/program field semantics SUFFICIENT** for current controller-product architecture.
2. Keep the **back-room guidance-software support → GUIDO assessment relationship SUFFICIENT** for current role architecture.
3. Treat rule-4-5 loop names and internal-MOCR/A-G separation as **Apollo-11-specific documented architecture**.
4. Model loop **monitor** and **talk** permissions separately; do not give AGC support direct A/G transmit authority from the available evidence.
5. Do not assign the Bales/Garman assessment to `FD LOOP`, `MOCR DYN`, or another named loop without Mission-G-effective configuration evidence.
6. Preserve `AGS−PGNCS` and `MSFN−PGNCS` as distinct comparison products and CAPCOM as the crew-facing disposition path.
7. Do not expose 70-FM-20 Figure 9 as an exact live MOCR display.
8. Recover Mission-G-effective routing/configuration evidence. PHO-TN401 remains the strongest display/control target at the Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, **Box 078-65/66**.
9. Seek a Mission-G-effective station/keyset record before freezing exact station-to-loop assignment, complete talk/listen privilege matrix, DRK mapping, request routing, or cadence.

## Sources

- NASA/MSC, _Flight Mission Rules, Apollo 11 (AS-506/107/LM-5)_, 16 April 1969, rule 4-5, p. 4-3: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf
- NASA JSC Oral History Project, John R. Garman interview, 27 March 2001: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf
- NASA, _Apollo 11 Air-to-Ground Voice Transcription (GOSS NET 1)_, Tape 66/7 p. 312: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics, _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137`: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 February 1970: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf

## Evidence status

- **SUFFICIENT:** Apollo-11-specific MSK-1137 alarm/program/descent field semantics.
- **SUFFICIENT:** guidance-software back-room support → GUIDO assessment relationship and CAPCOM-mediated crew disposition.
- **DOCUMENTED / MISSION-SPECIFIC:** Apollo 11 MOCR loop vocabulary and internal/A-G separation.
- **DOCUMENTED / PARTICIPANT:** support-room talk/listen distinction, multi-loop monitoring, and restricted A/G transmit authority.
- **OPEN:** exact Apollo 11 station request/routing, DRK mapping, cadence/latency, station-to-loop assignment, complete keyset privilege matrix, and detailed per-alarm internal call sequence.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection.