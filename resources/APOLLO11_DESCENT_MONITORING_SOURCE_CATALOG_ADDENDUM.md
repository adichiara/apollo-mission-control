# Apollo 11 descent-monitoring source-catalog addendum

Date: 2026-09-23

## Sources

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Philco-Ford / Western Development Laboratories, _Familiarization Manual — Mission Control Center Houston_, PHO-FAM001, revised through 30 Jun 1967, §§2-1-2, 3-2-2-1 | Station keysets connected to local conference or intersite loops; keysets could provide talk/listen or monitor-only circuits; configurations varied by usage requirement; A/G transmitter control described separately | Primary contemporary technical authority for generic MCC keyset/circuit semantics. **Not** Mission-G authority for exact station-to-loop assignment or July 1969 privilege matrix. |
| NASA/MSC, _Flight Mission Rules, Apollo 11 (AS-506/107/LM-5)_, 16 Apr 1969, rule 4-5 p. 4-3 | Mission-G MOCR communications list: `FD LOOP`, `AFD CONF LOOP`, `MOCR SYS 1 & 2`, `MOCR DYN`, `A/G 1 LOOP`, `A/G 2 LOOP`; separately identifies remote-site A/G path used for crew communication | Primary mission-specific authority for loop vocabulary and internal-MOCR/A-G separation. **Not** authority for GUIDO/support-room station-to-loop assignment, keyset mapping, or alarm-call routing. |
| NASA JSC Oral History Project, John R. Garman interview, 27 Mar 2001 | Firsthand participant account of back-room support for Bales; staff-support keysets used white talk and amber listen buttons; multiple loops could be monitored; support personnel listened to A/G while A/G transmit authority was restricted; Garman recalls FD-loop talk capability being added to the support position only later | Primary-participant authority for support relationship and operational keyset semantics. The "later on" recollection is date-imprecise. |
| NASA, _Apollo Era Hero John “Jack” Garman Dies_, 29 Sep 2016 | Identifies Bales as Guidance Officer; states Bales called Garman, working in the back room supporting him, during the 1202 assessment | NASA agency cross-check for role/assessment chain. Later retrospective. |
| NASA, _Apollo 11 Air-to-Ground Voice Transcription (GOSS NET 1)_, Tape 66/7 p. 312 | First 1202 sequence: Eagle reports alarm/code, CDR asks Houston for a reading, `CC`/CAPCOM returns ground GO disposition | Primary authority for crew-interface communication path. |
| AC Electronics, _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137` | Apollo-11-specific ground-display semantics including descent timing, warning/caution, alarm codes, restart count, computer program, DSKY context | Primary mission-specific authority for field semantics; not exact station ownership/routing/cadence. |
| NASA/MSC MPAD, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 Feb 1970 | Apollo 11 descent narrative; `AGS−PGNCS` and `MSFN−PGNCS` comparison traces/event markers | Primary NASA/MSC post-mission authority for monitored comparison-product family/event context; not exact live CRT layout. |
| LOC/NPS, HAER No. TX-109-C, _Johnson Space Center, Apollo Mission Control_ | Bibliographic/archival locator for PHO-TN401, Box 078-65/66 | Secondary federal historic-documentation authority used only as archival locator/cross-check. |
| Costis, B.; Ortolani, W.; Moreland, _NASA MCC Display/Control System Usage and Effectiveness, Apollo 11_, PHO-TN401, 24 Dec 1969 | **Not yet inspected** | Primary Philco-Ford/NASA contractor recovery target. Do not infer contents from title or HAER citation. |

## Catalog consequence

The communications model now has both contemporary technical and participant evidence that **monitor and talk were distinct privileges**. PHO-FAM001 explicitly permits talk/listen and monitor-only circuits; Garman supplies the operational support-room semantics. The runtime may therefore represent multi-loop monitoring and monitor-only access without treating loop membership as transmit authority.

The defensible alarm chain remains **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**. The exact Bales/Garman loop remains unresolved. PHO-FAM001's June 1967 effectivity prevents using its generic architecture as proof of a July 1969 station assignment, and Garman's recollection that an FD-loop talk button arrived "later on" is not dated precisely enough to establish the 20 July 1969 station keyset.

PHO-TN401 remains blocked on document recovery. Retrieve **Box 078-65/66** before freezing exact Mission-G display/routing configuration; separately recover a Mission-G-effective station/keyset record for exact internal voice-loop mechanics.

## URLs

- PHO-FAM001: https://www.ibiblio.org/apollo/Documents/Familiarization%20Manual%20Mission%20Control%20Center%20Houston.pdf
- NASA/MSC Apollo 11 Mission Rules: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf
- NASA JSC Garman oral history: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf
- NASA Garman history article: https://www.nasa.gov/image-article/apollo-era-hero-john-jack-garman-dies/
- NASA Apollo 11 air-to-ground transcript: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics Apollo 11 Manual: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC 70-FM-20: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- LOC/NPS HAER TX-109-C: https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf

## Evidence status

- **DOCUMENTED / SUFFICIENT:** MSK-1137 alarm/restart/program/DSKY/descent field semantics.
- **DOCUMENTED / SUFFICIENT:** guidance-software back-room support → GUIDO assessment relationship; crew-facing disposition through CAPCOM.
- **DOCUMENTED / MISSION-SPECIFIC:** Apollo 11 MOCR loop vocabulary/internal-versus-A/G separation.
- **DOCUMENTED / PRIMARY TECHNICAL:** local conference/intersite loop classes and talk/listen versus monitor-only keyset circuits.
- **DOCUMENTED / PARTICIPANT:** support-room button semantics, multi-loop monitoring, restricted A/G transmit authority.
- **DATE-IMPRECISE:** later addition of FD-loop talk capability to support position.
- **UNRESOLVED:** exact Apollo 11 station-to-loop assignment, complete keyset privileges, station request/routing/DRK mapping/cadence, and detailed internal channel mechanics.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection and Mission-G-effective station/keyset configuration.