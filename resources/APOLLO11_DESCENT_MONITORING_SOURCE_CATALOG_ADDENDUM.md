# Apollo 11 descent-monitoring source-catalog addendum

Date: 2026-09-23

## Sources

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| NASA/JSC, Richard A. Hoover, _Apollo Experience Report: Flight-Control Data Needs, Terminal Display Devices, and Ground System Configuration Requirements_, NASA TN D-7685 / JSC S-396, May 1974 | Apollo display-request mode: console requests format, computer assigns next available TV channel and automatically connects it; channel-attach mode; channel-usage management; display and intercom configuration treated separately | Primary NASA Apollo-wide operational architecture. Not Mission-G authority for GUIDO DRK mapping, exact descent callups, or cadence. |
| NASA/MSFC, _Saturn V Flight Manual, SA-507_, 1969, mission-control console-keyboard discussion | DRK = fast pre-labeled equivalent of MSK display-request mode; FDK out-of-tolerance acknowledgement returns four-digit identifying display-format code | Primary near-contemporary generic MCC interaction evidence. Apollo 12 vehicle manual; not Mission-G GUIDO key/format/FDK configuration. |
| NASA History Division, _News & Notes_, 35(3), 2018; reproduced Apollo 11 `AS-506 3RD FL` Historical Recorder #1 track sheet dated `06-09-69` | Ch. 21 `GUIDO [L]` → pos. 018; ch. 22 `GUIDO [R]` → pos. 019 | Mission-G-specific archival recorder map. Not a keyset/loop assignment. |
| Apollo in Real Time, Apollo 11 Mission Control Audio | Restored corpus of ~11,000 hours of headset/back-room recordings; selectable GUIDO L/R channels; timing restoration retains original IRIG-B signal | Primary-recording recovery route. Automated Whisper transcripts are imperfect navigation aids, not historical authority. |
| NASA, _Apollo 11 Mission Audio_ / Apollo Journals | NASA-hosted Apollo 11 mission-audio provenance and journal access | Agency corroboration for mission-audio corpus context. |
| Philco-Ford, PHO-FAM001, revised through 30 Jun 1967 | Station keysets connected to local conference/intersite loops; talk/listen or monitor-only circuits; configurations varied by use | Primary contemporary technical architecture; not exact Mission-G station assignment. |
| NASA/MSC, _Flight Mission Rules, Apollo 11_, 16 Apr 1969, rule 4-5 | `FD LOOP`, `AFD CONF LOOP`, `MOCR SYS 1 & 2`, `MOCR DYN`, `A/G 1 LOOP`, `A/G 2 LOOP` | Mission-specific loop vocabulary/internal-A/G separation; not GUIDO/support assignment. |
| NASA JSC Oral History Project, John R. Garman, 27 Mar 2001 | Back-room support for Bales; talk/listen button semantics; multi-loop monitoring; restricted A/G transmit authority | Primary-participant evidence; "later on" FD-loop talk recollection is date-imprecise. |
| NASA, _Apollo 11 Air-to-Ground Voice Transcription_, Tape 66/7 p. 312 | Eagle reports first 1202/requests reading; CAPCOM returns ground GO | Primary crew-interface path. |
| AC Electronics, _Apollo 11 Manual_, `MSK-1137` | Mission-specific descent timing, warning/caution, alarm codes, restart count, computer program, DSKY context | Primary field semantics; not exact station routing/cadence. |
| NASA/MSC, _The Apollo 11 Adventure_, 70-FM-20 | `AGS−PGNCS` and `MSFN−PGNCS` descent comparisons/event context | Primary post-mission comparison-product evidence; not exact live CRT layout. |
| LOC/NPS, HAER TX-109-C | Locator for PHO-TN401, Box 078-65/66 | Secondary federal archival locator only. |
| Costis, Ortolani, Moreland, _NASA MCC Display/Control System Usage and Effectiveness, Apollo 11_, PHO-TN401, 24 Dec 1969 | **Not yet inspected** | Primary recovery target; do not infer contents from title/citation. |

## Catalog consequence

NASA TN D-7685 closes the generic central display-selection mechanism. SA-507 further distinguishes controller-side interactions: MSK numeric display request, DRK fast pre-labeled request, and FDK out-of-tolerance acknowledgement yielding a four-digit display-format identifier. Together these permit historically grounded request-driven CRT behavior without inventing a fixed modern dashboard or automatic alert navigation.

The remaining display question is Mission-G-specific: GUIDO DRK labels/format mapping, FDK configuration, exact powered-descent display callups, and request cadence/latency. PHO-TN401 remains the strongest recovery target for those details. No program alarm is mapped to FDK behavior from the present evidence.

The project also has a Mission-G archival recorder map and an accessible restored primary-audio corpus exposing GUIDO left/right. Searchable automated transcripts may locate candidate timestamps, but any historical claim about participants, wording, or sequence must be verified against the restored audio.

The audio does **not** collapse the voice-configuration boundary. Hearing a voice on a GUIDO recording cannot by itself identify the named loop carrying it or establish talk privilege. The exact Bales/Garman loop remains unresolved.

The defensible alarm chain remains **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**.

## URLs

- NASA NTRS, NASA TN D-7685: https://ntrs.nasa.gov/citations/19740015284
- NASA/MSFC SA-507 Flight Manual: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap12fj/pdf/a12_sa507-flightmanual.pdf
- NASA History Division track-sheet reproduction: https://www.nasa.gov/wp-content/uploads/2023/01/NewsNotes-35-3-Fall-2018.pdf
- Apollo in Real Time Mission Control Audio: https://apolloinrealtime.org/11/MOCRviz/MOCRviz.html
- NASA Apollo 11 Mission Audio: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11MissionAudio.html
- PHO-FAM001: https://www.ibiblio.org/apollo/Documents/Familiarization%20Manual%20Mission%20Control%20Center%20Houston.pdf
- Apollo 11 Mission Rules: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf
- Garman oral history: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf
- Apollo 11 air-ground transcript: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics Apollo 11 Manual: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC 70-FM-20: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- LOC/NPS HAER TX-109-C: https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf

## Evidence status

- **DOCUMENTED / PRIMARY NASA / APOLLO-GENERIC:** display-request and channel-attach modes; dynamic TV-channel allocation; channel-usage management.
- **DOCUMENTED / PRIMARY / NEAR-CONTEMPORARY GENERIC:** DRK fast-request and FDK alert-to-format-code semantics.
- **DOCUMENTED / MISSION-SPECIFIC ARCHIVAL:** Historical Recorder #1 ch. 21/22 = GUIDO L/R, positions 018/019.
- **DOCUMENTED / PRIMARY-AUDIO RECOVERY ROUTE:** restored GUIDO L/R corpus with IRIG-B timing provenance.
- **RESTRICTED TO NAVIGATION:** automated Mission Control transcripts; verify against audio.
- **DOCUMENTED / SUFFICIENT:** MSK-1137 fields; back-room support → GUIDO relationship; CAPCOM crew disposition.
- **DOCUMENTED / PRIMARY TECHNICAL:** local conference/intersite loop classes and talk/listen versus monitor-only circuits.
- **UNRESOLVED / MISSION-G-SPECIFIC:** GUIDO DRK labels/format mapping, FDK configuration, exact descent display callups/cadence, station-to-loop assignment, complete keyset privileges, and directly verified internal alarm sequence.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 and Mission-G-effective station/keyset/display configuration.
