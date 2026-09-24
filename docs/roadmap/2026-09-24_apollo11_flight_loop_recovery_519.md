# Roadmap update — Apollo 11 Flight Director-loop recovery

Date: 2026-09-24
Research note: 519
Parent: `docs/roadmap/2026-09-24_apollo11_alarm_radio_timing_518.md`

## Change

The next descent-alarm task is now explicitly an **audio verification** task, not a transcript-mining task. The Apollo Flight Journal complete-descent compilation provides a usable Flight Director-loop listening route, but its modern synchronization, subtitles, and speaker labels are discovery aids only. NASA/JSC `792-AAI` remains the controlling primary artifact.

## Next

Align `792-AAI` against the note-518 GOSS NET 1 radio windows, then compare the same windows against GUIDO L/R. Promote exact wording, speaker attribution, and latency only when directly supported by the recordings. Do not infer the Garman/Bales circuit name from propagated Flight-loop traffic.

PHO-TN401 remains the blocked Mission-G configuration recovery target for station/keyset/display details.
