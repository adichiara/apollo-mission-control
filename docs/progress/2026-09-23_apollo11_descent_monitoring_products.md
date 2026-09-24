# Progress — Apollo 11 descent monitoring products

Date: 2026-09-23

Continued the open Apollo 11 powered-descent controller-product reference.

## Established evidence

NASA/MSC 70-FM-20 preserves Apollo 11 descent products labeled `AGS−PGNCS` and `MSFN−PGNCS`; AC Electronics `MSK-1137` establishes mission-specific ground-visible descent timing, warning/caution, alarm-code, restart-count, computer-program, and DSKY-context fields. The Apollo 11 air-ground transcript establishes that Eagle requested alarm disposition and CAPCOM returned the ground GO. Jack Garman's firsthand NASA oral history establishes guidance-software back-room support to GUIDO/Steve Bales. The defensible chain remains **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**.

Apollo 11 Flight Mission Rules rule 4-5 documents the Mission-G MOCR loop vocabulary. PHO-FAM001 documents local conference/intersite loops and talk/listen versus monitor-only keyset circuits. Garman independently describes support-room talk/listen buttons, multi-loop monitoring, and restricted A/G transmit authority. None establishes the exact Bales/Garman Mission-G circuit.

NASA History Division's reproduction of the original `AS-506 3RD FL` Historical Recorder #1 track sheet dated `06-09-69` maps channels 21/22 to `GUIDO [L]/[R]`, positions 018/019. This is recorder/station mapping, not keyset or loop mapping.

## Restored GUIDO audio recovery route

Research note 510 connected that Mission-G recorder map to the publicly accessible restored Apollo 11 Mission Control Audio corpus. The corpus exposes selectable GUIDO left/right channels and documents approximately 11,000 hours of headset/back-room recordings digitized from the historical tapes. Its provenance statement records correction of playback wow/flutter and retention of the original IRIG-B timing signal.

This gives the project a direct primary-recording route for the participants and sequence around the descent program alarms. The corpus's automated Whisper `large-v3` transcripts are explicitly imperfect. They may be used to find candidate timestamps but **not as historical authority**; claims must be verified against the restored audio itself.

## Apollo display request/routing semantics

Research note 511 uses NASA/JSC's 1974 Apollo Experience Report, NASA TN D-7685, to close the generic console-display interaction question. In **display request mode**, an individual console requested a display format; the computer generated/formatted it, assigned the next available computer-driven TV channel, and automatically connected that channel to the requesting console. In **channel attach mode**, a console requested an existing TV channel and received the data already on that channel.

The report also records a channel-usage display and treats display-system configuration and intercommunication-panel configuration as distinct categories. This supports keeping display selection and voice-loop assignment as separate evidence problems.

## New result — fast request and forced-display interaction

Research note 512 adds primary near-contemporary MCC evidence from the Apollo 12 SA-507 Flight Manual. It defines the **DRK** as a faster equivalent of the MSK's display-request mode: a controller presses an appropriately labeled pushbutton rather than selecting a format through thumbwheels. It separately defines the **FDK**: a preprogrammed analog out-of-tolerance condition illuminates an indicator; acknowledging it produces the four-digit code identifying the display format containing that parameter.

This supplies a useful controller-interaction distinction without filling in Apollo 11 configuration gaps. The generic simulator can distinguish numeric MSK request, fast pre-labeled DRK request, and FDK alert/format lookup. It must not invent GUIDO's Mission-G DRK labels, format numbers, FDK loading, or an automatic program-alarm-to-FDK mapping.

## Boundary preserved

A voice present on a recorded GUIDO station channel does not establish the named conference loop that delivered it or that speaker's keyset transmit privilege. NASA TN D-7685 and SA-507 do not establish Apollo 11 GUIDO key mapping or which display Bales actually selected during P63/P64/P66. 70-FM-20 Figure 9 is not treated as an exact live MOCR display.

## Next discriminating target

Inspect restored GUIDO L/R audio around 1201/1202 and document only directly audible participants, wording, and sequence. Separately recover a Mission-G-effective station/keyset/display record and PHO-TN401 (Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo 11 Mission Documents, **Box 078-65/66**).

## Sources

- NASA/JSC, Richard A. Hoover, _Apollo Experience Report: Flight-Control Data Needs, Terminal Display Devices, and Ground System Configuration Requirements_, NASA TN D-7685 / JSC S-396, May 1974: https://ntrs.nasa.gov/citations/19740015284
- NASA/MSFC, _Saturn V Flight Manual, SA-507_, mission-control console-keyboard discussion, 1969: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap12fj/pdf/a12_sa507-flightmanual.pdf
- NASA History Division, _News & Notes_ 35(3), reproduced Apollo 11 recorder track sheet: https://www.nasa.gov/wp-content/uploads/2023/01/NewsNotes-35-3-Fall-2018.pdf
- Apollo in Real Time, Apollo 11 Mission Control Audio: https://apolloinrealtime.org/11/MOCRviz/MOCRviz.html
- NASA, _Apollo 11 Mission Audio_: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11MissionAudio.html
- Philco-Ford PHO-FAM001: https://www.ibiblio.org/apollo/Documents/Familiarization%20Manual%20Mission%20Control%20Center%20Houston.pdf
- NASA/MSC Apollo 11 Mission Rules: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf
- NASA JSC Garman oral history: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf
- NASA Apollo 11 air-to-ground transcript: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics Apollo 11 Manual: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC 70-FM-20: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf

## Evidence status

- **DOCUMENTED / SUFFICIENT:** MSK-1137 alarm/program/descent fields; back-room support → GUIDO assessment; CAPCOM-mediated crew disposition.
- **DOCUMENTED:** Apollo 11 `AGS−PGNCS` and `MSFN−PGNCS` comparison-product family.
- **DOCUMENTED / MISSION-SPECIFIC:** Apollo 11 MOCR loop vocabulary/internal-versus-A/G separation.
- **DOCUMENTED / MISSION-SPECIFIC ARCHIVAL:** Historical Recorder #1 channels 21/22 = GUIDO L/R, positions 018/019.
- **DOCUMENTED / PRIMARY-AUDIO RECOVERY ROUTE:** restored GUIDO L/R recordings with IRIG-B timing provenance.
- **DOCUMENTED / PRIMARY NASA / APOLLO-GENERIC:** display-request and channel-attach modes and dynamic TV-channel allocation.
- **DOCUMENTED / PRIMARY / NEAR-CONTEMPORARY GENERIC:** DRK fast-request and FDK alert-to-format-code semantics.
- **RESTRICTED TO NAVIGATION:** automated Mission Control transcripts.
- **UNRESOLVED / MISSION-G-SPECIFIC:** GUIDO DRK labels/format mapping, FDK configuration, exact descent display callups/cadence, station/loop/keyset configuration, and directly verified per-alarm internal call sequence.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 and Mission-G-effective station/keyset/display configuration.
