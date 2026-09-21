# Apollo 11 program-alarm chain — source catalog addendum

Date: 2026-09-21
Parent: `resources/APOLLO11_LANDING_GO_POLL_SOURCE_CATALOG_ADDENDUM.md`

| Source | Evidence used | Boundary |
| --- | --- | --- |
| NASA, *Apollo 11 Technical Air-to-Ground Voice Transcription (GOSS NET 1)* | Armstrong/Aldrin report the program alarms; CAPCOM returns GO-on-alarm calls, including `same type` for the later 1201. | Primary contemporary transcript for crew-facing leg; does not expose support-room conversation. |
| Apollo 11 descent controller-loop audio | GUIDANCE supplies GO assessment to FLIGHT; later 1201 is assessed as same type/GO and FLIGHT continues. | Primary audio. Use audible words only; do not infer hidden display fields or unheard support-room dialogue. |
| NASA, *Flight Mission Rules, Apollo 11 (AS-506/107/LM-5)*, 16 Apr 1969 | Establishes the date/content baseline of the NASA-hosted mission-rule scan. | Predates the late descent simulation/program-alarm review; cannot establish a rule created after that event. |
| Purdue University Archives, Neil A. Armstrong papers, *Final Flight Mission Rules, Apollo 11*, 16 May 1969 | Establishes existence/date of a later archived Apollo 11 rules copy. | Also predates the late simulation-driven alarm review; catalog evidence, not proof of the landing-day alarm criterion. |
| MIT Instrumentation Laboratory, George Cherry, AG#370-69, *Exegesis of the 1201 and 1202 Alarms Which Occurred During the Mission G Lunar Landing*, 4 Aug 1969 | Five executive-overflow alarms, approximate PDI timing, and overload mechanism from RR ECDU counter-increment requests. | Primary contemporary **postflight engineering** analysis; does not establish the preflight console GO/abort rule. |
| Grumman, Clint Tillman, LAV-500-940, *Program Alarms in Powered Descent - Apollo 11*, 31 Jul 1969 | Contemporary investigation of powered-descent alarm codes, meanings, and probable causes. | Primary contemporary **postflight engineering** analysis; not the missing preflight decision artifact. |
| NASA History, *Apollo Era Hero John "Jack" Garman Dies* (2016) | Identifies Garman as Bales's back-room support and states that Garman recognized the 1202 as a temporary computer-overload warning compatible with continuing the landing. | NASA institutional retrospective, not a contemporary transcript; supports role/interpretation, not verbatim wording. |

## URLs

- NASA NTRS, Apollo 11 Technical Air-to-Ground Voice Transcription: https://ntrs.nasa.gov/citations/20160014392
- NASA-hosted Apollo 11 Flight Mission Rules scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11missionrules.pdf
- Purdue Armstrong papers catalog record: https://archives.lib.purdue.edu/repositories/2/archival_objects/38088
- MIT/IL AG#370-69: https://www.ibiblio.org/apollo/Documents/CherryApollo11Exegesis.pdf
- Grumman LAV-500-940: https://www.ibiblio.org/apollo/Documents/Memo-Tillman690731_text.pdf
- NASA History, Jack Garman: https://www.nasa.gov/image-article/apollo-era-hero-john-jack-garman-dies/

## Catalog consequence

The operational alarm chain can be represented at role level: computer-specialist support informs GUIDANCE; GUIDANCE recommends; FLIGHT disposes; CAPCOM relays. Primary postflight engineering documents can support alarm mechanics, but the available April/May mission-rule copies cannot be cited as the late-preflight alarm rule because their dates precede the simulation-driven review.

The missing artifact class is now explicit: post-simulation mission-rule change material, the Bales/Garman alarm cue sheet (or authenticated contemporary copy), or revised Apollo-11-effective Guidance/training procedures. Until recovered, do not encode a numeric recurrence threshold or universal `1201/1202 = GO` rule.

## Evidence status

- **DOCUMENTED / PRIMARY:** crew-facing alarm reports and GO calls; front-room GUIDANCE→FLIGHT recommendation/disposition.
- **DOCUMENTED / PRIMARY POSTFLIGHT ENGINEERING:** alarm occurrence/mechanism and restart behavior.
- **DOCUMENTED / NASA RETROSPECTIVE:** Garman support relationship and overload interpretation.
- **SOURCE-GAP BOUNDED:** available mission-rule copies are chronologically too early to prove the late-preflight criterion.
- **UNRESOLVED:** exact late-preflight written decision criterion, exact support-room words/loop topology, exact Mission-G alarm display basis.