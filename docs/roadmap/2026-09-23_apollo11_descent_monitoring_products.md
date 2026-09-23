# Roadmap addendum — Apollo 11 descent monitoring products

Date: 2026-09-23

## Status change

The Apollo 11 powered-descent controller-product boundary is supported by mission-specific product evidence: NASA/MSC 70-FM-20 preserves `AGS−PGNCS` and `MSFN−PGNCS` descent comparisons, while AC Electronics `MSK-1137` establishes ground-visible descent timing, warning/caution, alarm-code, restart-count, computer-program, and DSKY-context fields.

The alarm call path is now narrowed on both sides of the front room. The air-to-ground transcript establishes CAPCOM as the crew-facing ground voice. Jack Garman's NASA JSC oral history establishes that Garman and colleagues in the back room supported Steve Bales in the front room; NASA's agency history explicitly identifies Bales as Guidance Officer and states that he called Garman for support on the 1202.

The supported architecture is therefore **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**. Exact Apollo 11 loop/channel mechanics remain open.

NASA/MSC's final Apollo 10 Mission Rules (15 April 1969), rule 4-5, now supplies an immediately adjacent primary-source loop vocabulary: `FD LOOP`, `AFD CONF LOOP`, `MOCR SYS 1 & 2`, `MOCR DYN`, `A/G 1 LOOP`, and `A/G 2 LOOP`. This documents the era/configuration baseline and internal-MOCR versus air-ground separation, but does not assign the Apollo 11 GUIDO/support-room alarm path to any one of those loops.

## Immediate next work

1. Keep the Apollo 11 reference **OPEN**, but mark the **MSK-1137 alarm/program field semantics SUFFICIENT** for current controller-product architecture.
2. Mark the **back-room guidance-software support → GUIDO assessment relationship SUFFICIENT** for current role architecture; do not infer exact loop names or keying.
3. Preserve the Apollo 10 rule-4-5 loop names only as an adjacent-mission naming baseline; do not back-project station assignments into Apollo 11.
4. Preserve `AGS−PGNCS` and `MSFN−PGNCS` as distinct comparison products.
5. Preserve the sourced crew call boundary: ground decision → CAPCOM disposition to crew; no internal controller speaks directly to Eagle.
6. Do not expose 70-FM-20 Figure 9 as an exact live MOCR display.
7. Recover Mission-G-effective routing/configuration evidence. PHO-TN401 remains the strongest target at the Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, **Box 078-65/66**.
8. Freeze exact station request/routing, DRK-button mapping, cadence, Apollo 11 loop/channel identity, and detailed per-alarm internal call sequence only after direct mission-effective evidence is recovered.

## Sources

- NASA/MSC, _Apollo 10 Mission Rules_, final, 15 April 1969, rule 4-5, p. 4-3: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap10fj/pdf/a10-mission-rules-19690415.pdf
- NASA JSC Oral History Project, John R. Garman interview, 27 March 2001: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf
- NASA, "Apollo Era Hero John 'Jack' Garman Dies," 29 September 2016: https://www.nasa.gov/image-article/apollo-era-hero-john-jack-garman-dies/
- NASA, _Apollo 11 Air-to-Ground Voice Transcription (GOSS NET 1)_, Tape 66/7 p. 312: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics, _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137`: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 February 1970: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf

## Evidence status

- **SUFFICIENT:** Apollo-11-specific MSK-1137 alarm/program/descent field semantics for current product architecture.
- **SUFFICIENT:** guidance-software back-room support → GUIDO assessment relationship and CAPCOM-mediated crew disposition.
- **DOCUMENTED:** adjacent Apollo 10 primary-source MOCR loop vocabulary and internal/A-G separation.
- **OPEN:** exact Apollo 11 station request/routing, DRK mapping, cadence/latency, loop/channel identity, and detailed internal call sequence.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection.