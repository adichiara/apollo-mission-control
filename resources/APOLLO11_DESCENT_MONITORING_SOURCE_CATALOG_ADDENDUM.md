# Apollo 11 descent-monitoring source-catalog addendum

Date: 2026-09-23

## Sources

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| NASA/JSC, NASA TN D-7685 / JSC S-396, May 1974 | Display-request mode; dynamic TV-channel allocation; channel-attach mode; display/intercom configuration treated separately | Primary Apollo-wide architecture; not Mission-G GUIDO mapping. |
| NASA/MSFC, _Saturn V Flight Manual, SA-507_, 1969 | DRK fast pre-labeled request; FDK out-of-tolerance acknowledgement returns identifying display-format code | Primary near-contemporary generic MCC interaction evidence; not Mission-G configuration. |
| NASA/MSC, _Flight Mission Rules, Apollo 11_, rule 4-9 | 10 of 36 MOCR D/TV channels mandatory prelaunch; one for GUIDO; two GUIDO analog chart recorders highly desirable on D/TV | Primary Mission-G resource evidence; not permanent channel ownership or descent display selection. |
| NASA History Division, _News & Notes_ 35(3), reproduced Apollo 11 Historical Recorder #1 track sheet | Ch. 21 `GUIDO [L]` → pos. 018; ch. 22 `GUIDO [R]` → pos. 019 | Mission-G archival recorder map; not keyset/loop assignment. |
| Apollo in Real Time, Apollo 11 Mission Control Audio | Restored headset/back-room corpus; selectable GUIDO L/R; IRIG-B timing provenance | Primary-recording recovery route. Automated transcripts are navigation aids only. |
| DVIDS / NASA, `Apollo11Audio`, `792-AAI` | Catalog identifies Flight Director's Loop audio including `Lunar Descent 1955-2025`; collection digitized/cataloged/archived by Houston Audio Control Room at JSC | Primary-audio archival route for descent Flight-loop traffic. Catalog metadata is not authority for exact words/speakers/timing and does not identify Garman's back-room circuit. |
| Philco-Ford, PHO-FAM001 | Local conference/intersite loops; talk/listen or monitor-only circuits | Primary contemporary technical architecture; not exact Mission-G assignment. |
| NASA/MSC, _Flight Mission Rules, Apollo 11_, rule 4-5 | `FD LOOP`, `AFD CONF LOOP`, `MOCR SYS 1 & 2`, `MOCR DYN`, `A/G 1 LOOP`, `A/G 2 LOOP` | Mission-specific loop vocabulary/internal-A/G separation; not GUIDO/support assignment. |
| NASA JSC Oral History Project, John R. Garman, 27 Mar 2001 | Back-room support for Bales; keyset semantics; restricted A/G transmit authority; first-alarm advice on unnamed back-room voice loop; later `Same type` relay | Primary-participant evidence; not authority for exact 1969 timing/wording or named loop. |
| NASA, _Apollo 11 Air-to-Ground Voice Transcription_ | Eagle requests alarm reading; CAPCOM returns ground GO | Primary crew-interface path. |
| AC Electronics, _Apollo 11 Manual_, `MSK-1137` | Mission-specific descent timing, warning/caution, alarm codes, restart count, computer program, DSKY context | Primary field semantics; not exact routing/cadence. |
| NASA/MSC, _The Apollo 11 Adventure_, 70-FM-20 | `AGS−PGNCS` and `MSFN−PGNCS` descent comparisons | Primary post-mission comparison-product evidence; not exact live CRT layout. |
| LOC/NPS, HAER TX-109-C | Locator for PHO-TN401, Box 078-65/66 | Secondary federal archival locator only. |
| Costis, Ortolani, Moreland, PHO-TN401, 24 Dec 1969 | **Not yet inspected** | Primary recovery target; do not infer contents from title/citation. |

## Catalog consequence

The display architecture is bounded by NASA TN D-7685, SA-507, and Apollo 11 Mission Rules rule 4-9 without inventing Mission-G GUIDO key mappings or powered-descent display callups.

Garman's oral history narrows the internal alarm workflow to an unnamed back-room voice-loop advice path into Bales, with Bales checking broader data before the GO and a later participant-recollected `Same type` relay. It does not name the circuit.

The audio evidence now has two complementary primary-recording routes. Historical Recorder #1 channels 21/22 and the restored corpus expose GUIDO L/R station recordings. Separately, NASA `792-AAI` is cataloged as Flight Director's Loop audio covering lunar descent 1955–2025. Cross-comparing these recordings can verify relay order and what reached the Flight loop more strongly than either alone.

Neither recording route collapses the configuration boundary. Hearing a voice on GUIDO or Flight-loop audio cannot by itself identify the originating back-room circuit or complete talk privilege. Exact wording, timing, overlap, and speaker attribution require direct audio inspection; automated/derivative transcripts remain navigation aids only.

The defensible alarm chain remains **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**.

## URLs

- NASA NTRS, NASA TN D-7685: https://ntrs.nasa.gov/citations/19740015284
- NASA/MSFC SA-507 Flight Manual: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap12fj/pdf/a12_sa507-flightmanual.pdf
- Apollo 11 Mission Rules: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf
- NASA History Division track-sheet reproduction: https://www.nasa.gov/wp-content/uploads/2023/01/NewsNotes-35-3-Fall-2018.pdf
- Apollo in Real Time Mission Control Audio: https://apolloinrealtime.org/11/MOCRviz/MOCRviz.html
- DVIDS / NASA `Apollo11Audio`, `792-AAI`: https://www.dvidshub.net/audio/32176/apollo-11
- PHO-FAM001: https://www.ibiblio.org/apollo/Documents/Familiarization%20Manual%20Mission%20Control%20Center%20Houston.pdf
- Garman oral history: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf
- Apollo 11 air-ground transcript: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics Apollo 11 Manual: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC 70-FM-20: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- LOC/NPS HAER TX-109-C: https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf

## Evidence status

- **DOCUMENTED / PRIMARY NASA / APOLLO-GENERIC:** display-request/channel-attach modes and dynamic TV-channel allocation.
- **DOCUMENTED / PRIMARY / NEAR-CONTEMPORARY GENERIC:** DRK fast-request and FDK alert-to-format-code semantics.
- **DOCUMENTED / PRIMARY / MISSION-G-SPECIFIC:** rule 4-9 GUIDO display-resource minimum.
- **DOCUMENTED / PRIMARY PARTICIPANT:** unnamed back-room voice-loop advice and later `Same type` relay recollection.
- **DOCUMENTED / MISSION-SPECIFIC ARCHIVAL:** Historical Recorder #1 ch. 21/22 = GUIDO L/R, positions 018/019.
- **DOCUMENTED / PRIMARY-AUDIO RECOVERY ROUTE:** restored GUIDO L/R plus NASA `792-AAI` Flight Director-loop lunar-descent audio.
- **RESTRICTED TO NAVIGATION:** automated/derivative transcripts; verify against audio.
- **DOCUMENTED / SUFFICIENT:** MSK-1137 fields; back-room support → GUIDO relationship; CAPCOM crew disposition.
- **DOCUMENTED / PRIMARY TECHNICAL:** local conference/intersite loop classes and talk/listen versus monitor-only circuits.
- **UNRESOLVED / MISSION-G-SPECIFIC:** exact named GUIDO/support loop, exact per-alarm wording/timing/overlap, GUIDO DRK labels/format mapping, FDK configuration, exact powered-descent display callups/cadence, channel identity, station-to-loop assignment, and complete keyset privileges.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 and Mission-G-effective station/keyset/display configuration.
