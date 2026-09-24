# Apollo 11 descent voice source-catalog addendum — note 521

Date: 2026-09-24

| Source | Class | Use / restriction |
| --- | --- | --- |
| NASA, *Apollo 11 — Record of Lunar Events* | NASA mission chronology | Pairs landing GET 102:45:43 with 20:17:43 GMT on 20 July 1969. |
| NASA/NTRS, *Apollo by the Numbers*, Table 10 | NASA historical/mission chronology | Establishes range zero at 13:32:00 GMT on 16 July 1969 and GET/GMT relationship. |
| DVIDS, *Apollo 11* audio catalog | U.S. Government archival catalog metadata | Identifies `792-AAI` as Flight Director's Loop and catalogs lunar descent `1955-2025`. Catalog range is consistent with GMT/time-of-day; it does not establish digitized-file sample zero. |

## Catalog consequence

For `792-AAI`, retain separate metadata fields for:

- catalog GMT window: 19:55–20:25 GMT, 20 July 1969;
- derived approximate GET window: 102:23–102:53;
- digitized-file elapsed time: unknown until the actual file is inspected;
- IRIG-B alignment: unknown until recovered/decoded or otherwise established.

The five known descent computer-alarm anchors are inside the catalog window, making this artifact correctly scoped for direct FD-loop recovery.

## URLs

- https://www.nasa.gov/wp-content/uploads/static/history/ap11ann/ap11events.html
- https://ntrs.nasa.gov/api/citations/19710015677/downloads/19710015677.pdf
- https://www.dvidshub.net/audio/32176/apollo-11

## Evidence status

- **CLOSED:** catalog-window clock semantics.
- **DERIVED:** approximate GET coverage.
- **OPEN:** exact file offset, IRIG-B alignment, transcription, speaker attribution.