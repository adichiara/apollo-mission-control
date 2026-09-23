# Progress — Apollo 11 descent monitoring products

Date: 2026-09-23

Continued the open Apollo 11 powered-descent controller-product reference.

## Primary-source result — comparison products

NASA/MSC **70-FM-20, _The Apollo 11 Adventure_** preserves Apollo 11 descent strip-chart comparisons labeled `AGS−PGNCS` and `MSFN−PGNCS`, with descent-event markers and in-plane/crossrange monitoring logic. This supports the repository's pairwise/consensus architecture without establishing exact live CRT presentation.

## Primary-source result — program-alarm/descent fields

The mission-specific AC Electronics _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137`, establishes ground-visible `TIG`, `TGO`, significant-event timing, descent-only time-to-end-of-phase, LGC/ISS warning status, PGNCS/program caution status, first/second/most-recent alarm code, restart count, computer program, and DSKY verb/noun/flasher/rows.

## Primary-source result — program-alarm call path

NASA's _Apollo 11 Air-to-Ground Voice Transcription (GOSS NET 1)_, Tape 66/7 p. 312, establishes that Eagle announced the first 1202 and requested Houston's disposition; `CC`/CAPCOM returned the ground GO disposition.

NASA JSC's 27 March 2001 oral-history interview with Jack Garman narrows the internal assessment path. Garman's firsthand account distinguishes the back room from the front room and describes himself and colleagues in the back room as helping Steve Bales. NASA's agency history identifies Bales as the Guidance Officer and explicitly states that Bales called Garman in the back room for support on the 1202.

The defensible chain is therefore: **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**.

## Primary-source result — Apollo 11 voice-loop vocabulary

NASA/MSC's _Flight Mission Rules, Apollo 11 (AS-506/107/LM-5)_, dated 16 April 1969, rule 4-5 COMMUNICATIONS, directly lists `FD LOOP`, `AFD CONF LOOP`, `MOCR SYS 1 & 2`, `MOCR DYN`, `A/G 1 LOOP`, and `A/G 2 LOOP`. The same rule separately identifies the MCC/remote-site air-ground path as used for communication with the crew.

## Primary-participant result — support-room keyset semantics

The same Garman oral history directly describes Apollo staff-support-room communications panels: white buttons provided talk capability, amber buttons provided listen capability, multiple loops could be monitored simultaneously, and listening volume was independently controlled. Garman says support personnel could listen to air-ground while very few positions had air-ground talk authority. He also recalls the staff-support room listening to the flight-director loop and says a flight-director talk button was added only "later on" as the computer-support role evolved.

This is enough to require **separate monitor and talk permissions** in the communications model. It is not precise enough to date the FD-talk-button change to a particular Apollo mission, so it does not prove an exact Apollo 11 keyset matrix. In particular, the repository must not invent direct AGC-support air-ground transmit authority or assume that `FD LOOP` carried the Bales/Garman alarm assessment.

## Boundary preserved

MSK-1137 field semantics do **not** establish exact station request procedure, DRK mapping, routing, cadence/latency, or detailed internal decision rules. The Garman evidence establishes support relationship and general keyset semantics but not the exact Apollo 11 loop name or complete per-position privilege matrix. Likewise, 70-FM-20 Figure 9 is not treated as an exact live MOCR display.

## Archival target

PHO-TN401 remains the leading direct display/control recovery target at Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, **Box 078-65/66**.

## Next discriminating target

Recover PHO-TN401 or another Apollo-11-effective configuration source to map documented MSK-1137/comparison products to exact station requests/routing/DRK mapping/cadence. Separately seek a Mission-G-effective station/keyset record for the exact GUIDO/support-room/FLIGHT channel and talk/listen privilege matrix.

## Sources

- NASA/MSC, _Flight Mission Rules, Apollo 11 (AS-506/107/LM-5)_, 16 April 1969, rule 4-5, p. 4-3: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf
- NASA JSC Oral History Project, John R. Garman interview, 27 March 2001: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf
- NASA, "Apollo Era Hero John 'Jack' Garman Dies," 29 September 2016: https://www.nasa.gov/image-article/apollo-era-hero-john-jack-garman-dies/
- NASA, _Apollo 11 Air-to-Ground Voice Transcription (GOSS NET 1)_, Tape 66/7 p. 312: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics, _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137`: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC MPAD, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 February 1970: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf

## Evidence status

- **DOCUMENTED / SUFFICIENT:** MSK-1137 alarm/restart/program/DSKY/descent field semantics.
- **DOCUMENTED / SUFFICIENT:** guidance-software back-room support → GUIDO assessment relationship and CAPCOM-mediated crew disposition.
- **DOCUMENTED:** Apollo 11 AGS−PGNCS and MSFN−PGNCS comparison-product family.
- **DOCUMENTED / MISSION-SPECIFIC:** Apollo 11 MOCR loop vocabulary/internal-versus-A/G separation.
- **DOCUMENTED / PARTICIPANT:** support-room talk/listen distinction, multi-loop monitoring, and restricted A/G transmit authority.
- **UNRESOLVED:** exact Apollo 11 live station request/routing/DRK mapping/cadence, station-to-loop assignment, full keyset privilege matrix, and detailed internal channel mechanics.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection.