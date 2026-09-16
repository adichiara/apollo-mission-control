# Research note 178 — NTRS 19710010485 metadata/payload mismatch

Date: 2026-09-16

## Question

Can NTRS citation `19710010485` safely be described as the bibliographic record for the Flight Control Division *Mission Operations Report — Apollo 13*?

## Primary-source/archive check

NASA Technical Reports Server citation page `https://ntrs.nasa.gov/citations/19710010485` currently identifies the record as:

- *MSC Apollo 13 investigation team. Panel 3 - Flight operations and network Final report*;
- publication date 1 May 1970;
- report number `NASA-TM-X-66933`.

However, the download currently served at `https://ntrs.nasa.gov/api/citations/19710010485/downloads/19710010485.pdf` opens with the cover:

- **MISSION OPERATIONS REPORT — APOLLO 13**;
- **APRIL 28, 1970**;
- **PREPARED BY FLIGHT CONTROL DIVISION**;
- **MANNED SPACECRAFT CENTER, HOUSTON, TEXAS**.

NASA's separate History/ALSJ scan presents the same Mission Operations Report title/cover and is consistent with the document used in notes 170–177.

## Finding

There is an archive-level **metadata/payload mismatch** at NTRS citation `19710010485`: the NTRS landing-page metadata names a different Apollo 13 investigation document, while the downloadable PDF payload is the Flight Control Division Mission Operations Report used in this research chain.

Accordingly, the repository must not describe `19710010485` as an unambiguous NTRS bibliographic record for the Mission Operations Report. It may be retained as a NASA-hosted download endpoint only with the mismatch explicitly documented. For bibliographic identity, use the report's own cover/title page and the independent NASA History/ALSJ copy.

## What this improves

This corrects source-provenance hygiene without changing any historical finding derived from the report text. The mass-properties chronology remains supported by the Flight Control Division report itself; what changes is how the NTRS endpoint is cataloged.

## Evidence boundary

Do not infer that:

- `NASA-TM-X-66933` is the report number of the Flight Control Division Mission Operations Report merely because NTRS currently associates that number with citation `19710010485`;
- the NTRS landing-page title and the downloaded PDF are the same document;
- archive metadata can override the identity printed on the primary document's own cover.

## Next archival target

Continue the substantive search for a T+55 generation/load record or downstream RTCC/RTACF LM-burn run/request/output tying the T+55 deck to `5.86 / 6.75`. When new archival identifiers are added, verify both landing-page metadata and the actual payload before treating the identifier as bibliographic provenance.