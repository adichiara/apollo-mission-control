# Roadmap addendum — Apollo 11 descent monitoring products

Date: 2026-09-23

## Status change

Apollo 11 powered-descent controller-product architecture is supported by mission-specific evidence for `AGS−PGNCS` / `MSFN−PGNCS` comparisons, MSK-1137 alarm/program/descent fields, the crew-facing CAPCOM disposition path, and the guidance-software back-room → GUIDO/Bales assessment relationship.

Mission-G Flight Mission Rules document `FD LOOP`, `AFD CONF LOOP`, `MOCR SYS 1 & 2`, `MOCR DYN`, `A/G 1 LOOP`, and `A/G 2 LOOP`. PHO-FAM001 establishes talk/listen versus monitor-only keyset circuits, while Jack Garman supplies participant evidence for support-room talk/listen semantics and restricted A/G transmit authority. Neither establishes the exact Apollo 11 Bales/Garman loop.

The reproduced Apollo 11 Historical Recorder #1 track sheet maps channels 21/22 to `GUIDO [L]/[R]`, positions 018/019. Research note 800 connects that archival map to the restored Apollo 11 Mission Control audio corpus. Automated transcripts remain navigation aids only; historical claims must be checked against audio.

Research notes 704–513 establish generic display request/channel attach behavior, DRK/FDK interaction semantics, and the Mission-G rule 4-9 resource boundary: one GUIDO D/TV channel in the mandatory prelaunch minimum and two GUIDO analog chart recorders listed as highly desirable on D/TV. These do not establish GUIDO's Apollo 11 DRK/FDK mapping or actual descent display callups.

Research note 603 narrows the internal alarm sequence using Garman's NASA oral history: an unnamed back-room voice loop carried his first-alarm advice to Bales; Bales checked broader data before the GO; a later different-but-same-class alarm produced a participant-recollected `Same type` relay from Garman through Bales toward CAPCOM. This supports role/sequence behavior but not a named loop or exact 1969 wording/timing.

Research note 801 adds an independent agency-cataloged primary-audio route. DVIDS's NASA `Apollo11Audio` catalog identifies `792-AAI` as **Flight Director's Loop** audio including **Lunar Descent 1955–2025**, digitized/cataloged/archived by the Houston Audio Control Room at JSC. This can be cross-compared with GUIDO L/R to verify what reached the Flight loop during the alarm sequence.

Research note 604 adds the primary Mission-G event clock needed to perform that comparison. NASA/MSC _Apollo 11 Mission Report_ table 5-I records five alarm anchors: `102:38:22` 1202, `102:39:02` 1202, `102:42:18` 1201, `102:42:43` 1202, and `102:42:58` 1202; it also records P64 entry at `102:41:32` and P66 at `102:43:22`. These are postflight computer/event times, not assumed timestamps for spoken reports or controller calls.

## Immediate next work

1. Keep the Apollo 11 reference **OPEN**, while retaining MSK-1137 field semantics and the back-room-support → GUIDO → ground decision → CAPCOM chain as **SUFFICIENT** for current architecture.
2. Treat Garman's participant recollection as support for GUIDO being an active assessment node rather than a blind relay.
3. Treat Historical Recorder #1 channels 21/22 as **DOCUMENTED Apollo 11 GUIDO recording assignments**, not named loop assignments.
4. Use the five Mission Report alarm-event times as search anchors for restored GUIDO L/R and NASA `792-AAI`; include lead/lag around each anchor to capture the spacecraft report and controller relay chain.
5. Reconcile recording clocks before asserting exact voice timing or overlap. Do not equate a computer-determined event time with a spoken-call timestamp.
6. Do not infer named loop identity or transmit privilege merely because a voice is audible on a station or Flight-loop recording. In particular, `792-AAI` does not identify Garman's unnamed back-room circuit.
7. Use NASA TN D-7685 display-request/channel-attach modes as supported generic interaction; distinguish MSK numeric request, DRK fast pre-labeled request, and FDK out-of-tolerance format-code lookup without inventing Apollo 11 mappings.
8. Treat rule 4-9's `GUIDO 1` D/TV requirement as minimum resource availability, not permanently bound channel ownership; preserve the two GUIDO analog chart recorders without assigning unsupported powered-descent use.
9. Preserve `AGS−PGNCS` and `MSFN−PGNCS` as distinct comparison products and CAPCOM as the crew-facing disposition path. Do not expose 70-FM-20 Figure 9 as an exact live MOCR display.
10. Recover Mission-G-effective routing/configuration evidence. PHO-TN401 remains the strongest display/control target at the Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, **Box 078-65/66**.
11. Seek a Mission-G-effective station/keyset record before freezing exact station-to-loop assignment, complete talk/listen privilege matrix, GUIDO DRK mapping, FDK configuration, exact descent callups, or cadence.

## Sources

- NASA/MSC, _Apollo 11 Mission Report_, MSC-00171, November 1969: https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- NASA/MSC, _Flight Mission Rules, Apollo 11_, 16 April 1969, rules 4-5 and 4-9: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf
- NASA/JSC, NASA TN D-7685 / JSC S-396, May 1974: https://ntrs.nasa.gov/citations/19740015284
- NASA/MSFC, _Saturn V Flight Manual, SA-507_, 1969: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap12fj/pdf/a12_sa507-flightmanual.pdf
- NASA History Division, _News & Notes_, Vol. 35 No. 3: https://www.nasa.gov/wp-content/uploads/2023/01/NewsNotes-35-3-Fall-2018.pdf
- Apollo in Real Time, Apollo 11 Mission Control Audio: https://apolloinrealtime.org/11/MOCRviz/MOCRviz.html
- DVIDS / NASA, `Apollo11Audio`, `792-AAI` Flight Director's Loop lunar-descent catalog: https://www.dvidshub.net/audio/32176/apollo-11
- NASA Apollo Lunar Surface Journal, Apollo 11 landing chronology: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.landing.html
- Philco-Ford, PHO-FAM001: https://www.ibiblio.org/apollo/Documents/Familiarization%20Manual%20Mission%20Control%20Center%20Houston.pdf
- NASA JSC Oral History Project, John R. Garman, 27 March 2001: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf
- NASA, _Apollo 11 Air-to-Ground Voice Transcription_: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics, _Apollo 11 Manual_: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC, _The Apollo 11 Adventure_, 70-FM-20: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf

## Evidence status

- **SUFFICIENT:** Apollo-11-specific MSK-1137 field semantics; guidance-software back-room support → GUIDO assessment relationship; CAPCOM-mediated crew disposition.
- **DOCUMENTED / PRIMARY / MISSION-G-SPECIFIC TIMING:** five Mission Report alarm-event anchors and P64/P66 boundaries; not exact spoken-call timing.
- **DOCUMENTED / PRIMARY PARTICIPANT:** unnamed back-room voice-loop advice to Bales; Bales checks broader data before GO; later `Same type` relay recollection.
- **DOCUMENTED / MISSION-SPECIFIC:** Apollo 11 MOCR loop vocabulary and internal/A-G separation.
- **DOCUMENTED / PRIMARY / MISSION-G-SPECIFIC DISPLAY RESOURCE:** one GUIDO D/TV channel in the mandatory prelaunch minimum; GUIDO analog chart recorders one and two highly desirable on D/TV.
- **DOCUMENTED / MISSION-SPECIFIC ARCHIVAL:** Historical Recorder #1 channels 21/22 are GUIDO left/right, positions 018/019.
- **DOCUMENTED / PRIMARY-AUDIO RECOVERY ROUTE:** restored GUIDO L/R corpus plus NASA `792-AAI` Flight Director-loop lunar-descent recording.
- **DOCUMENTED / PRIMARY TECHNICAL:** talk/listen versus monitor-only circuit architecture.
- **DOCUMENTED / PRIMARY NASA / APOLLO-GENERIC:** display-request and channel-attach modes.
- **DOCUMENTED / PRIMARY / NEAR-CONTEMPORARY GENERIC:** DRK fast-request and FDK alert-to-format-code lookup.
- **RESTRICTED TO NAVIGATION:** automated/derivative transcripts; direct audio verification required.
- **OPEN / MISSION-G-SPECIFIC:** exact named GUIDO/support loop, exact per-alarm spoken wording/timing/overlap, recording-clock reconciliation, GUIDO DRK labels/format mapping, FDK configuration, exact powered-descent display callups, request cadence/latency, channel identity, and complete keyset privilege matrix.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection and Mission-G-effective station/keyset/display configuration.
