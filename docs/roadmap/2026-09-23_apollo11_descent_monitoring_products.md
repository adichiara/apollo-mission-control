# Roadmap addendum — Apollo 11 descent monitoring products

Date: 2026-09-23

## Status change

The Apollo 11 powered-descent controller-product boundary is supported by mission-specific product evidence: NASA/MSC 70-FM-20 preserves `AGS−PGNCS` and `MSFN−PGNCS` descent comparisons, while AC Electronics `MSK-1137` establishes ground-visible descent timing, warning/caution, alarm-code, restart-count, computer-program, and DSKY-context fields.

The alarm call path is now narrowed on both sides of the front room. The air-to-ground transcript establishes CAPCOM as the crew-facing ground voice. Jack Garman's NASA JSC oral history establishes that Garman and colleagues in the back room supported Steve Bales in the front room; NASA's agency history explicitly identifies Bales as Guidance Officer and states that he called Garman for support on the 1202.

The supported architecture is therefore **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**. Exact loop/channel mechanics remain open.

## Immediate next work

1. Keep the Apollo 11 reference **OPEN**, but mark the **MSK-1137 alarm/program field semantics SUFFICIENT** for current controller-product architecture.
2. Mark the **back-room guidance-software support → GUIDO assessment relationship SUFFICIENT** for current role architecture; do not infer exact loop names or keying.
3. Preserve `AGS−PGNCS` and `MSFN−PGNCS` as distinct comparison products.
4. Preserve the sourced crew call boundary: ground decision → CAPCOM disposition to crew; no internal controller speaks directly to Eagle.
5. Do not expose 70-FM-20 Figure 9 as an exact live MOCR display.
6. Recover Mission-G-effective routing/configuration evidence. PHO-TN401 remains the strongest target at the Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, **Box 078-65/66**.
7. Freeze exact station request/routing, DRK-button mapping, cadence, loop/channel identity, and detailed per-alarm internal call sequence only after direct mission-effective evidence is recovered.

## Sources

- NASA JSC Oral History Project, John R. Garman interview, 27 March 2001: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf
- NASA, "Apollo Era Hero John 'Jack' Garman Dies," 29 September 2016: https://www.nasa.gov/image-article/apollo-era-hero-john-jack-garman-dies/
- NASA, _Apollo 11 Air-to-Ground Voice Transcription (GOSS NET 1)_, Tape 66/7 p. 312: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics, _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137`: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 February 1970: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf

## Evidence status

- **SUFFICIENT:** Apollo-11-specific MSK-1137 alarm/program/descent field semantics for current product architecture.
- **SUFFICIENT:** guidance-software back-room support → GUIDO assessment relationship and CAPCOM-mediated crew disposition.
- **OPEN:** exact station request/routing, DRK mapping, cadence/latency, loop/channel identity, and detailed internal call sequence.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection.