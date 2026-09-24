# Roadmap addendum — Apollo 11 descent monitoring products

Date: 2026-09-23

## Status change

Apollo 11 powered-descent controller-product architecture is now supported by mission-specific evidence for `AGS−PGNCS` / `MSFN−PGNCS` comparisons, MSK-1137 alarm/program/descent fields, the crew-facing CAPCOM disposition path, and the guidance-software back-room → GUIDO/Bales assessment relationship.

Mission-G Flight Mission Rules document `FD LOOP`, `AFD CONF LOOP`, `MOCR SYS 1 & 2`, `MOCR DYN`, `A/G 1 LOOP`, and `A/G 2 LOOP`. PHO-FAM001 independently establishes talk/listen versus monitor-only keyset circuits, while Jack Garman supplies participant evidence for support-room talk/listen semantics and restricted A/G transmit authority. Neither source establishes the exact Apollo 11 Bales/Garman loop.

The reproduced Apollo 11 `AS-506 3RD FL` Historical Recorder #1 track sheet maps channels 21/22 to `GUIDO [L]/[R]`, positions 018/019. Research note 510 connects that archival map to the restored Apollo 11 Mission Control audio corpus, which exposes GUIDO left/right recordings and retains IRIG-B timing provenance. Apollo in Real Time's automated Whisper transcripts are explicitly imperfect and are navigation aids only; historical claims must be checked against the audio.

Research note 511 adds primary NASA Apollo-wide display-control semantics from NASA TN D-7685. Controllers could request a display format; the computer assigned the next available computer-driven TV channel and automatically connected it to the requesting console. A separate channel-attach mode let a console view an already active TV channel. The report also treats display-system configuration and intercommunication-panel configuration as distinct configuration categories. Generic request/routing semantics are therefore documented, while Mission-G GUIDO DRK mapping, exact powered-descent callups, and operational cadence remain open.

## Immediate next work

1. Keep the Apollo 11 reference **OPEN**, while retaining MSK-1137 field semantics and the back-room-support → GUIDO → ground decision → CAPCOM chain as **SUFFICIENT** for current architecture.
2. Treat Historical Recorder #1 channels 21/22 as **DOCUMENTED Apollo 11 GUIDO recording assignments**, not named loop assignments.
3. Inspect the restored GUIDO L/R audio around the 1201/1202 interval. Use automated transcript search only to locate candidate timestamps; verify participants, wording, and sequence directly against audio.
4. Do not infer named loop identity or transmit privilege merely because a voice is audible on a station recording.
5. Use NASA TN D-7685's **display request** and **channel attach** modes as the supported generic console-display interaction. Do not invent fixed per-console TV-channel ownership.
6. Do not infer Apollo 11 GUIDO DRK keys, exact descent display callups, or request cadence/latency from the Apollo-wide TN D-7685 architecture.
7. Preserve `AGS−PGNCS` and `MSFN−PGNCS` as distinct comparison products and CAPCOM as the crew-facing disposition path. Do not expose 70-FM-20 Figure 9 as an exact live MOCR display.
8. Recover Mission-G-effective routing/configuration evidence. PHO-TN401 remains the strongest display/control target at the Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, **Box 078-65/66**.
9. Seek a Mission-G-effective station/keyset record before freezing exact station-to-loop assignment, complete talk/listen privilege matrix, GUIDO DRK mapping, exact descent callups, or cadence.

## Sources

- NASA/JSC, Richard A. Hoover, _Apollo Experience Report: Flight-Control Data Needs, Terminal Display Devices, and Ground System Configuration Requirements_, NASA TN D-7685 / JSC S-396, May 1974: https://ntrs.nasa.gov/citations/19740015284
- NASA History Division, _News & Notes_, Vol. 35 No. 3, 3rd Quarter 2018, pp. 3–5: https://www.nasa.gov/wp-content/uploads/2023/01/NewsNotes-35-3-Fall-2018.pdf
- Apollo in Real Time, Apollo 11 Mission Control Audio: https://apolloinrealtime.org/11/MOCRviz/MOCRviz.html
- NASA, _Apollo 11 Mission Audio_: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11MissionAudio.html
- Philco-Ford, _Familiarization Manual — Mission Control Center Houston_, PHO-FAM001: https://www.ibiblio.org/apollo/Documents/Familiarization%20Manual%20Mission%20Control%20Center%20Houston.pdf
- NASA/MSC, _Flight Mission Rules, Apollo 11_, 16 April 1969, rule 4-5: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf
- NASA JSC Oral History Project, John R. Garman interview, 27 March 2001: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf
- NASA, _Apollo 11 Air-to-Ground Voice Transcription_: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics, _Apollo 11 Manual_, `MSK-1137`: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC, _The Apollo 11 Adventure_, 70-FM-20: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf

## Evidence status

- **SUFFICIENT:** Apollo-11-specific MSK-1137 alarm/program/descent field semantics; guidance-software back-room support → GUIDO assessment relationship; CAPCOM-mediated crew disposition.
- **DOCUMENTED / MISSION-SPECIFIC:** Apollo 11 MOCR loop vocabulary and internal/A-G separation.
- **DOCUMENTED / MISSION-SPECIFIC ARCHIVAL:** Historical Recorder #1 channels 21/22 are GUIDO left/right, positions 018/019.
- **DOCUMENTED / PRIMARY-AUDIO RECOVERY ROUTE:** restored Mission Control corpus exposes GUIDO L/R with IRIG-B timing provenance.
- **DOCUMENTED / PRIMARY TECHNICAL:** talk/listen versus monitor-only circuit architecture.
- **DOCUMENTED / PRIMARY NASA / APOLLO-GENERIC:** display-request and channel-attach modes, including automatic channel allocation/console connection.
- **RESTRICTED TO NAVIGATION:** automated Mission Control transcripts; direct audio verification required.
- **OPEN / MISSION-G-SPECIFIC:** GUIDO DRK mapping, exact powered-descent display callups, request cadence/latency, station-to-loop assignment, complete keyset privilege matrix, and detailed per-alarm internal call sequence.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection and Mission-G-effective station/keyset/display configuration.
