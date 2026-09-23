# Apollo 11 descent-monitoring source-catalog addendum

Date: 2026-09-23

## Sources

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| NASA/MSC, _Apollo 10 Mission Rules_, final, 15 Apr 1969, rule 4-5 p. 4-3 | Adjacent-mission MOCR communications list: `FD LOOP`, `AFD CONF LOOP`, `MOCR SYS 1 & 2`, `MOCR DYN`, `A/G 1 LOOP`, `A/G 2 LOOP`; separately identifies remote-site A/G path for crew communication | Primary mission-era authority for loop vocabulary and internal-MOCR/A-G separation immediately before Apollo 11. **Not** authority for Apollo 11 GUIDO/support-room loop assignment, keyset mapping, or alarm-call routing. |
| NASA JSC Oral History Project, John R. Garman interview, 27 Mar 2001 | Firsthand participant account distinguishing back room/front room; Garman describes himself and colleagues in the back room as helping Steve Bales and notes front room/back-room loop separation | Primary-participant authority for support relationship and room boundary. Does not establish exact loop/channel name, console keying, or every per-alarm call. |
| NASA, _Apollo Era Hero John “Jack” Garman Dies_, 29 Sep 2016 | Identifies Bales as Guidance Officer; states Bales called Garman, working in the back room supporting him, during the 1202 assessment | NASA agency cross-check for role/assessment chain. Later retrospective, so subordinate to participant/transcript evidence where they overlap. |
| NASA, _Apollo 11 Air-to-Ground Voice Transcription (GOSS NET 1)_, Tape 66/7 p. 312 | First 1202 sequence: Eagle reports alarm/code, CDR asks Houston for a reading, `CC`/CAPCOM returns ground GO disposition | Primary authority for **crew-interface communication path**. Does not by itself identify internal assessment ownership. |
| AC Electronics, _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137` | Apollo-11-specific ground-display semantics including `TIG`, `TGO`, significant-event timing, descent-only time-to-end-of-phase, warning/caution status, alarm codes, restart count, computer program, DSKY context | Primary mission-specific authority for field semantics. **Not** authority for exact station ownership, request timing, DRK mapping, routing, or cadence. |
| NASA/MSC MPAD, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 Feb 1970 | Apollo 11 descent narrative; powered-descent monitoring flowchart; Figure 9 with `AGS−PGNCS` and `MSFN−PGNCS` comparison traces/event markers | Primary NASA/MSC post-mission authority for monitored comparison-product family/event context. **Not** authority for exact live CRT/MSK layout/routing/request workflow/cadence. |
| LOC/NPS, HAER No. TX-109-C, _Johnson Space Center, Apollo Mission Control_ | Footnote 37 cites PHO-TN401 p. 5-5; bibliography gives JSC History Collection, UHCL, Apollo Program, Mission Documents: Apollo 11, Box 078-65/66 | Secondary federal historic-documentation authority used only as archival locator/bibliographic cross-check. |
| Costis, B.; Ortolani, W.; Moreland, W., _NASA MCC Display/Control System Usage and Effectiveness, Apollo 11_, PHO-TN401, 24 Dec 1969 | **Not yet inspected** | Primary Philco-Ford/NASA contractor recovery target. Do not infer contents from title or HAER citation. |

## Catalog consequence

The Apollo 11 controller-product boundary now has direct mission-specific evidence for independent-source descent comparisons, ground-visible program-alarm/descent status, and the alarm decision chain at useful role resolution. The defensible chain is **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**.

Apollo 10 rule 4-5 adds a primary, immediately adjacent configuration baseline for authentic MOCR loop names and confirms the architectural distinction between internal Mission Control loops and crew-facing A/G communications. It does **not** close the Apollo 11 GUIDO/support-room loop assignment.

The runtime may model the support/ownership boundary and use sourced era loop vocabulary, but must not invent exact Apollo 11 loop assignments, keying, DRK behavior, request timing, routing, cadence, or a detailed per-alarm internal sequence.

PHO-TN401 remains blocked on document recovery. Retrieve **Box 078-65/66** before freezing exact Mission-G routing/configuration; recover an Apollo-11-effective communications/keyset source for exact internal voice-loop mechanics if PHO-TN401 does not provide them.

## URLs

- NASA/MSC Apollo 10 Mission Rules: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap10fj/pdf/a10-mission-rules-19690415.pdf
- NASA JSC Garman oral history: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf
- NASA Garman history article: https://www.nasa.gov/image-article/apollo-era-hero-john-jack-garman-dies/
- NASA Apollo 11 air-to-ground transcript: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- AC Electronics Apollo 11 Manual: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC 70-FM-20: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- LOC/NPS HAER TX-109-C: https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf

## Evidence status

- **DOCUMENTED / SUFFICIENT:** MSK-1137 alarm/restart/program/DSKY/descent field semantics.
- **DOCUMENTED / SUFFICIENT:** guidance-software back-room support → GUIDO assessment relationship; crew-facing disposition through CAPCOM.
- **DOCUMENTED:** mission-specific AGS−PGNCS and MSFN−PGNCS comparison products/event context.
- **DOCUMENTED:** adjacent Apollo 10 MOCR loop vocabulary/internal-versus-A/G separation.
- **UNRESOLVED:** exact Apollo 11 live station request/routing/DRK mapping/cadence and internal loop/channel mechanics.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection.