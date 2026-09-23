# Progress — Apollo 11 descent monitoring products

Date: 2026-09-23

Continued the open Apollo 11 powered-descent controller-product reference.

## Primary-source result — comparison products

NASA/MSC **70-FM-20, _The Apollo 11 Adventure_** preserves Apollo 11 descent strip-chart comparisons labeled `AGS−PGNCS` and `MSFN−PGNCS`, with descent-event markers and in-plane/crossrange monitoring logic. This supports the repository's pairwise/consensus architecture without establishing exact live CRT presentation.

## Primary-source result — program-alarm/descent fields

The mission-specific AC Electronics _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137`, establishes ground-visible `TIG`, `TGO`, significant-event timing, descent-only time-to-end-of-phase, LGC/ISS warning status, PGNCS/program caution status, first/second/most-recent alarm code, restart count, computer program, and DSKY verb/noun/flasher/rows.

## Primary-source result — program-alarm call path

NASA's _Apollo 11 Air-to-Ground Voice Transcription (GOSS NET 1)_, Tape 66/7 p. 312, establishes that Eagle announced the first 1202 and requested Houston's disposition; `CC`/CAPCOM returned the ground GO disposition.

NASA JSC's 27 March 2001 oral-history interview with Jack Garman now narrows the previously unresolved internal assessment path. Garman's firsthand account distinguishes the back room from the front room and describes himself and colleagues in the back room as helping Steve Bales. NASA's agency history identifies Bales as the Guidance Officer and explicitly states that Bales called Garman in the back room for support on the 1202.

The defensible chain is therefore: **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**. Exact loop/channel identity and per-alarm internal call timing remain unresolved.

## Boundary preserved

MSK-1137 field semantics do **not** establish exact station request procedure, DRK mapping, routing, cadence/latency, or detailed internal decision rules. The Garman evidence establishes support relationship/assessment ownership but not exact loop names, console keying, or that Garman personally originated every later alarm recommendation. Likewise, 70-FM-20 Figure 9 is not treated as an exact live MOCR display.

## Archival target

PHO-TN401 remains the leading direct display/control recovery target at Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, **Box 078-65/66**.

## Next discriminating target

Recover PHO-TN401 or another Apollo-11-effective configuration source to map documented MSK-1137/comparison products to exact station requests/routing/DRK mapping/cadence. Separately seek mission-effective loop documentation for the exact back-room/GUIDO/FLIGHT channel mechanics; do not infer those mechanics from oral-history role descriptions.

## Sources

- NASA JSC Oral History Project, John R. Garman interview, 27 March 2001: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf
- NASA, "Apollo Era Hero John 'Jack' Garman Dies," 29 September 2016: https://www.nasa.gov/image-article/apollo-era-hero-john-jack-garman-dies/
- NASA, _Apollo 11 Air-to-Ground Voice Transcription (GOSS NET 1)_, Tape 66/7 p. 312: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics, _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137`: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC MPAD, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 February 1970: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf

## Evidence status

- **DOCUMENTED / SUFFICIENT:** MSK-1137 alarm/restart/program/DSKY/descent field semantics.
- **DOCUMENTED / SUFFICIENT:** guidance-software back-room support → GUIDO assessment relationship and CAPCOM-mediated crew disposition.
- **DOCUMENTED:** Apollo 11 AGS−PGNCS and MSFN−PGNCS comparison-product family.
- **UNRESOLVED:** exact live station request/routing/DRK mapping/cadence and exact internal loop/channel mechanics.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection.