# Research note 521 — Apollo 11 `792-AAI` clock-window reconciliation

Date: 2026-09-24

## Question

What clock does the catalog range `1955–2025` attached to NASA/JSC artifact `792-AAI` represent, and can it be related to Apollo 11 GET without inventing an offset from a web player's elapsed time?

## Primary / institutional evidence

NASA's Apollo 11 event chronology gives range zero as 13:32:00 GMT on 16 July 1969. The same chronology independently pairs lunar landing GET 102:45:43 with 20:17:43 GMT on 20 July 1969.

The U.S. Government DVIDS catalog record for Apollo 11 identifies artifact `792-AAI` as `Flight Director's Loop` and describes three clock ranges: `Lift off 1327-1347, Lunar Descent 1955-2025, Lunar Ascent 1748-1808`. Read against the mission chronology, the descent range brackets the 20:17:43 GMT landing and therefore functions as a time-of-day/GMT catalog range, not as GET and not as an arbitrary media-player elapsed-time range.

Using the mission's range-zero relation, the cataloged descent interval maps arithmetically to approximately GET 102:23:00–102:53:00 on 20 July. The five Mission Report computer/event alarm anchors at GET 102:38:22, 102:39:02, 102:42:18, 102:42:43, and 102:42:58 therefore all fall inside the cataloged `792-AAI` descent segment.

## What this closes

The earlier ambiguity around the meaning of `1955–2025` is closed at the catalog-window level: it is a GMT/time-of-day range consistent with NASA's independent GET↔GMT chronology.

This gives a defensible first-order conversion for locating the alarm windows in the historical artifact:

`GET = GMT - 16 Jul 1969 13:32:00`, with date rollover accounted for.

## What this does not close

- It does not establish the sample-accurate start time of a digitized `792-AAI` file.
- It does not prove that a particular web player begins exactly at 19:55:00 GMT.
- It does not replace the Historical Recorder IRIG-B timing channel for precise alignment.
- It does not identify individual speakers or prove which station microphone contributed a given utterance.
- It does not yet transcribe Garman→Bales→Flight traffic.

Direct audio inspection must retain a separate distinction between catalog GMT, digitized-file elapsed time, IRIG-B time (where recoverable), and derived GET.

## Sources

- NASA, *Apollo 11 — Record of Lunar Events*: https://www.nasa.gov/wp-content/uploads/static/history/ap11ann/ap11events.html
- NASA/NTRS, *Apollo by the Numbers*, Table 10: range zero 13:32:00 GMT, 16 July 1969: https://ntrs.nasa.gov/api/citations/19710015677/downloads/19710015677.pdf
- DVIDS, *Apollo 11* audio catalog entry, including `792-AAI`: https://www.dvidshub.net/audio/32176/apollo-11

## Evidence status

- **CLOSED:** semantic meaning of the `792-AAI` catalog descent range `1955–2025` as GMT/time-of-day.
- **DERIVED:** approximate GET coverage 102:23:00–102:53:00 from NASA range zero.
- **OPEN:** sample/file offset, IRIG-B-level alignment, direct FD-loop transcription, and GUIDO L/R comparison.