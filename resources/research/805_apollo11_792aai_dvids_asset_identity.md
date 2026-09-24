# Research note 805 — Apollo 11 `792-AAI` DVIDS asset-identity gate

Date: 2026-09-24
Research thread: `apollo11-descent-audio-provenance`

## Question

Can a public DVIDS Apollo 11 audio page be treated as the digitized `792-AAI` lunar-descent file solely because its description lists `792-AAI`?

## Primary / government evidence

DVIDS Apollo 11 audio pages are U.S. Government/NASA catalog records. The inspected page for Audio ID `32176` identifies a page-specific file (`1302/DOD_100738674.mp3`) and page-specific duration (`00:57:28`), but its description is a collection-level inventory that lists many distinct Apollo audio artifacts, including `792-AAI`, `3172`, `3212`, `938-AAG`, `939-AAG`, and mission-commentary reels. The same collection inventory is repeated on other DVIDS Apollo 11 audio pages whose page-specific filenames and durations differ.

The page therefore does **not** state that Audio ID `32176` / `DOD_100738674.mp3` is `792-AAI`, nor does the repeated description provide a page-to-reel mapping.

DVIDS also states that the Apollo 11 audio collection was digitized, cataloged, and archived by the Houston Audio Control Room at NASA Johnson Space Center.

## Consequence

Do not infer a DVIDS Audio ID, `DOD_*.mp3` filename, or player offset for `792-AAI` from the repeated collection description. Direct transcription remains gated on an asset whose identity is explicitly tied to `792-AAI` (or on another provenance chain that establishes that mapping).

This prevents a false-positive source attribution: a page can mention `792-AAI` while serving a different item from the Apollo 11 audio collection.

## Retrieval result

The public page exposes a `Download Audio` control, but direct automated retrieval returned HTTP 403 in this research environment. That access result is operational, not historical evidence, and does not establish that the underlying audio is unavailable through other authorized/manual routes.

## Sources

- DVIDS, *Apollo 11*, Audio ID 32176: https://www.dvidshub.net/audio/32176/apollo-11
- Comparison catalog pages inspected during discovery include DVIDS Audio IDs 32145, 32208, 32214, and 32222; each repeats the same collection inventory while reporting a different page-specific filename/duration.

## Evidence status

- **UNRESOLVED:** open retrieval/alignment questions listed below remain unresolved.

- **CLOSED:** a DVIDS page's repeated Apollo-collection description is insufficient to map that page to `792-AAI`.
- **OPEN:** explicit public asset/reel mapping for `792-AAI`; actual descent-file retrieval; file elapsed-time alignment; direct FD-loop transcription.
- **BLOCKED IN CURRENT AUTOMATED ROUTE:** DVIDS direct audio download returned HTTP 403.
