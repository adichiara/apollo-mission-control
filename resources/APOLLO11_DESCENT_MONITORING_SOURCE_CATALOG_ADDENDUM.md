# Apollo 11 descent-monitoring source-catalog addendum

Date: 2026-09-23

## Sources

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| AC Electronics, _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137` | Apollo-11-specific ground-display semantics including `TIG`, `TGO`, last/next significant event, descent-only time-to-end-of-phase, LGC/ISS warning status, PGNCS/program caution status, first/second/most-recent alarm code, restart count, computer program, DSKY verb/noun/flasher/rows, plus previously cataloged LR/guidance fields | Primary mission-specific authority for field semantics. **Not** authority for exact station ownership, historical request timing, DRK button mapping, routing, or update cadence. |
| NASA/MSC MPAD, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 Feb 1970 | Apollo 11 descent narrative; powered-descent monitoring flowchart; Figure 9 with `AGS−PGNCS` and `MSFN−PGNCS` comparison traces/event markers | Primary NASA/MSC post-mission authority for monitored comparison-product family/event context. **Not** authority for exact live CRT/MSK layout/routing/request workflow/cadence. |
| LOC/NPS, HAER No. TX-109-C, _Johnson Space Center, Apollo Mission Control_ | Footnote 37 cites PHO-TN401 p. 5-5; bibliography gives JSC History Collection, UHCL, Apollo Program, Mission Documents: Apollo 11, Box 078-65/66 | Secondary federal historic-documentation authority used only as archival locator/bibliographic cross-check. |
| Costis, B.; Ortolani, W.; Moreland, W., _NASA MCC Display/Control System Usage and Effectiveness, Apollo 11_, PHO-TN401, 24 Dec 1969 | **Not yet inspected** | Primary Philco-Ford/NASA contractor recovery target. Do not infer contents from title or HAER citation. |

## Catalog consequence

The Apollo 11 controller-product boundary now has direct mission-specific evidence for both independent-source descent comparisons and a rich ground-visible program-alarm/descent status product. The runtime may model alarm codes, restart count, computer program, DSKY context, and descent-phase timing as sourced ground products; it must not invent station routing or DRK behavior.

PHO-TN401 remains blocked on document recovery. Retrieve **Box 078-65/66** from the identified UHCL collection before freezing exact Mission-G routing/configuration.

## URLs

- AC Electronics Apollo 11 Manual: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC 70-FM-20: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- LOC/NPS HAER TX-109-C: https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf

## Evidence status

- **DOCUMENTED / SUFFICIENT:** MSK-1137 alarm/restart/program/DSKY/descent field semantics for current product architecture.
- **DOCUMENTED:** mission-specific AGS−PGNCS and MSFN−PGNCS comparison products/event context.
- **UNRESOLVED:** exact live station request/routing/DRK mapping/cadence and call ownership.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection.