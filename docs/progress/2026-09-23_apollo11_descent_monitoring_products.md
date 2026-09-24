# Progress — Apollo 11 descent monitoring products

Date: 2026-09-23

Continued the open Apollo 11 powered-descent controller-product reference.

## Established evidence

NASA/MSC 70-FM-20 preserves Apollo 11 descent products labeled `AGS−PGNCS` and `MSFN−PGNCS`; AC Electronics `MSK-1137` establishes mission-specific ground-visible descent timing, warning/caution, alarm-code, restart-count, computer-program, and DSKY-context fields. The Apollo 11 air-ground transcript establishes that Eagle requested alarm disposition and CAPCOM returned the ground GO. Jack Garman's firsthand NASA oral history establishes guidance-software back-room support to GUIDO/Steve Bales. The defensible chain remains **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**.

Apollo 11 Flight Mission Rules rule 4-5 documents the Mission-G MOCR loop vocabulary. PHO-FAM001 documents local conference/intersite loops and talk/listen versus monitor-only keyset circuits. Garman independently describes support-room talk/listen buttons, multi-loop monitoring, and restricted A/G transmit authority. None establishes the exact Bales/Garman Mission-G circuit.

NASA History Division's reproduction of the original `AS-506 3RD FL` Historical Recorder #1 track sheet dated `06-09-69` maps channels 21/22 to `GUIDO [L]/[R]`, positions 018/019. This is recorder/station mapping, not keyset or loop mapping.

## New result — restored GUIDO audio recovery route

Research note 510 connected that Mission-G recorder map to the publicly accessible restored Apollo 11 Mission Control Audio corpus. The corpus exposes selectable GUIDO left/right channels and documents approximately 11,000 hours of headset/back-room recordings digitized from the historical tapes. Its provenance statement records correction of playback wow/flutter and retention of the original IRIG-B timing signal.

This gives the project a direct primary-recording route for the next unresolved question: the participants and sequence around the descent program alarms. The corpus's automated Whisper `large-v3` transcripts are explicitly described as imperfect. They may be used to find candidate timestamps but **not as historical authority**; claims must be verified against the restored audio itself.

A voice present on a recorded GUIDO station channel does not establish the named conference loop that delivered it or that speaker's keyset transmit privilege. Those configuration questions remain open.

## Boundary preserved

No exact station request procedure, DRK mapping, routing, cadence/latency, station-to-loop assignment, or complete keyset privilege matrix is inferred. 70-FM-20 Figure 9 is not treated as an exact live MOCR display.

## Next discriminating target

Inspect restored GUIDO L/R audio around 1201/1202 and document only directly audible participants, wording, and sequence. Separately recover a Mission-G-effective station/keyset record and PHO-TN401 (Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo 11 Mission Documents, **Box 078-65/66**).

## Sources

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
- **RESTRICTED TO NAVIGATION:** automated Mission Control transcripts.
- **UNRESOLVED:** exact station/loop/keyset configuration and directly verified per-alarm internal call sequence.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 and Mission-G-effective station/keyset configuration.
