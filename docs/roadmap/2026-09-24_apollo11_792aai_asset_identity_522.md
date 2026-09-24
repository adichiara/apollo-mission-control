# Roadmap update — `792-AAI` DVIDS asset identity

Date: 2026-09-24
Research note: 522
Parent: `docs/roadmap/2026-09-24_apollo11_792aai_clock_521.md`

## Change

The next retrieval gate is now explicit. DVIDS Apollo 11 pages repeat a collection-level inventory containing `792-AAI`, while each page separately reports its own Audio ID, `DOD_*.mp3` filename, and duration. A mention of `792-AAI` in that repeated inventory is therefore not evidence that the page's served file is the `792-AAI` reel/segment.

## Next discriminating work

1. Recover an explicit page/file/reel mapping for `792-AAI` from NASA/JSC, DVIDS metadata, or another provenance-bearing government record.
2. Once mapped, retrieve/inspect the lunar-descent audio and establish file elapsed time ↔ catalog GMT.
3. Inspect the five Mission Report alarm windows on the FD loop.
4. Compare with Historical Recorder #1 GUIDO L/R 21/22.
5. Keep speaker attribution conservative and PHO-TN401 as the blocked Mission-G configuration target.

## Gate

Do not identify any DVIDS `DOD_*.mp3` as `792-AAI` merely because its page repeats the collection inventory.

## Evidence status

- **CLOSED:** catalog-clock semantics; invalid shortcut from collection description to asset identity.
- **OPEN:** explicit `792-AAI` asset mapping, retrieval, alignment, transcription.
