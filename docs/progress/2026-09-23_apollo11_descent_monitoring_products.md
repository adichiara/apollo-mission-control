# Progress — Apollo 11 descent monitoring products

Date: 2026-09-23

Continued the open Apollo 11 powered-descent controller-product reference.

## Established evidence

NASA/MSC 70-FM-20 preserves Apollo 11 descent products labeled `AGS−PGNCS` and `MSFN−PGNCS`; AC Electronics `MSK-1137` establishes mission-specific ground-visible descent timing, warning/caution, alarm-code, restart-count, computer-program, and DSKY-context fields. The air-ground transcript establishes Eagle's alarm request and CAPCOM's ground GO. Jack Garman's NASA oral history establishes guidance-software back-room support to GUIDO/Steve Bales. The defensible chain remains **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**.

Apollo 11 Flight Mission Rules rule 4-5 documents Mission-G MOCR loop vocabulary. PHO-FAM001 documents local conference/intersite loops and talk/listen versus monitor-only keyset circuits. Neither establishes the exact Bales/Garman Mission-G circuit.

NASA History Division's reproduced Apollo 11 Historical Recorder #1 track sheet maps channels 21/22 to `GUIDO [L]/[R]`, positions 018/019. Research note 510 connects that map to the restored Apollo 11 Mission Control audio corpus; automated transcripts are navigation aids only.

Research notes 511–513 establish generic display request/channel attach behavior, DRK/FDK interaction semantics, and the Mission-G rule 4-9 display-resource boundary. They do not establish Apollo 11 GUIDO DRK labels, FDK loading, exact descent callups, or alarm-to-FDK behavior.

Research note 514 narrows the participant-recollected internal alarm sequence: Garman advised Bales on an unnamed back-room voice loop; Bales checked broader data before the GO; a later same-class alarm produced a rapid `Same type` relay. This supports GUIDO as an assessment node, not a blind relay, but exact wording/timing remains an audio-verification problem.

## New result — agency-cataloged Flight Director-loop descent audio

Research note 515 identifies a complementary primary recording in the NASA Apollo 11 audio collection hosted by DVIDS. The catalog explicitly identifies `792-AAI` as **Flight Director's Loop** audio and lists **Lunar Descent 1955–2025** among its covered intervals. DVIDS identifies NASA as the courtesy source and states that the collection was digitized, cataloged, and archived by the Houston Audio Control Room at Johnson Space Center under NASA identifier `Apollo11Audio`.

This gives the project a second primary-recording perspective for the alarm sequence: restored GUIDO L/R for station-local traffic and `792-AAI` for traffic that reached the Flight Director loop. Cross-comparison can test ordering and relay behavior without inferring that Garman's unnamed back-room circuit was itself `FD LOOP`.

The catalog entry is provenance/coverage evidence, not a transcript. Exact alarm-era words, speakers, timing, overlap, and the relationship between Flight-loop traffic and the back-room circuit remain unresolved until the audio is inspected.

## Boundary preserved

A voice present on a recorded GUIDO or Flight-loop channel does not establish the originating named conference loop or the speaker's complete keyset transmit privilege. NASA TN D-7685, SA-507, and rule 4-9 do not establish Apollo 11 GUIDO key mapping or which display Bales selected during P63/P64/P66. 70-FM-20 Figure 9 is not treated as an exact live MOCR display.

## Next discriminating target

Inspect restored GUIDO L/R around 1201/1202 and cross-compare with NASA `792-AAI` lunar-descent Flight Director-loop audio. Verify claims directly from recordings; use transcripts only for navigation. Separately recover a Mission-G-effective station/keyset/display record and PHO-TN401 (Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo 11 Mission Documents, **Box 078-65/66**).

## Sources

- NASA/MSC, _Flight Mission Rules, Apollo 11_, 16 April 1969: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf
- NASA/JSC, NASA TN D-7685 / JSC S-396: https://ntrs.nasa.gov/citations/19740015284
- NASA/MSFC, _Saturn V Flight Manual, SA-507_: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap12fj/pdf/a12_sa507-flightmanual.pdf
- NASA History Division, _News & Notes_ 35(3): https://www.nasa.gov/wp-content/uploads/2023/01/NewsNotes-35-3-Fall-2018.pdf
- Apollo in Real Time, Apollo 11 Mission Control Audio: https://apolloinrealtime.org/11/MOCRviz/MOCRviz.html
- DVIDS / NASA, `Apollo11Audio`, `792-AAI`: https://www.dvidshub.net/audio/32176/apollo-11
- Philco-Ford PHO-FAM001: https://www.ibiblio.org/apollo/Documents/Familiarization%20Manual%20Mission%20Control%20Center%20Houston.pdf
- NASA JSC Garman oral history: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf
- NASA Apollo 11 air-to-ground transcript: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics Apollo 11 Manual: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC 70-FM-20: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf

## Evidence status

- **DOCUMENTED / SUFFICIENT:** MSK-1137 alarm/program/descent fields; back-room support → GUIDO assessment; CAPCOM-mediated crew disposition.
- **DOCUMENTED / PRIMARY PARTICIPANT:** unnamed back-room voice-loop alarm advice; Bales checks broader data before GO; later `Same type` relay recollection.
- **DOCUMENTED / MISSION-SPECIFIC:** Apollo 11 MOCR loop vocabulary/internal-versus-A/G separation.
- **DOCUMENTED / MISSION-G-SPECIFIC DISPLAY RESOURCE:** one GUIDO D/TV channel in the prelaunch minimum; two GUIDO analog chart recorders highly desirable on D/TV.
- **DOCUMENTED / MISSION-SPECIFIC ARCHIVAL:** Historical Recorder #1 channels 21/22 = GUIDO L/R, positions 018/019.
- **DOCUMENTED / PRIMARY-AUDIO RECOVERY ROUTE:** restored GUIDO L/R recordings and NASA `792-AAI` Flight Director-loop lunar-descent recording.
- **DOCUMENTED / PRIMARY NASA / APOLLO-GENERIC:** display-request/channel-attach modes and dynamic TV-channel allocation.
- **DOCUMENTED / PRIMARY / NEAR-CONTEMPORARY GENERIC:** DRK fast-request and FDK alert-to-format-code semantics.
- **RESTRICTED TO NAVIGATION:** automated/derivative transcripts.
- **UNRESOLVED / MISSION-G-SPECIFIC:** named GUIDO/support loop, exact per-alarm wording/timing/overlap, GUIDO DRK labels/format mapping, FDK configuration, exact descent display callups/cadence, channel identity, and complete station/loop/keyset configuration.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 and Mission-G-effective station/keyset/display configuration.
