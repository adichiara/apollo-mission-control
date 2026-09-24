# Research note 520 — Apollo 11 descent audio provenance boundary

Date: 2026-09-24

## Question

Before transcribing the descent alarm exchanges, what can be established directly about the surviving Mission Control recordings and their channel identity?

## Primary / archival evidence

NASA History's published image of the Apollo 11 Historical Recorder #1 track sheet identifies separate recorded channels for FLIGHT DIRECTOR L/R (channels 7/8), CAPCOM L/R (14/15), and GUIDO L/R (21/22). The sheet also assigns channel 1 to GMT time in IRIG-B format. This is configuration evidence for the historical recording itself, not a later speaker reconstruction.

NASA's Apollo 11 Mission Audio page states that the mission audio, except LM onboard audio, came from a recent NASA Johnson digitization supplied by an Audio Control Room senior technician. That establishes a NASA/JSC digitization provenance for the mission-audio corpus, but does not by itself prove that every web presentation preserves original channel separation or clock alignment.

The cataloged `792-AAI` artifact remains the primary Flight Director-loop descent recording. Its catalog description gives a lunar-descent segment of 1955–2025, but those catalog clock values must not be converted into GET without an independently verified clock relationship.

## Result

The next audio comparison must preserve three independent identities:

1. recorder channel identity (for example GUIDO L versus GUIDO R),
2. recording/catalog clock or IRIG-B time,
3. mission GET/event time.

A web player's elapsed time, a catalog time, and GET are not interchangeable. Speaker attribution also cannot be inferred merely because speech appears on a GUIDO or Flight Director recording: the recorded station feed can contain received loop traffic as well as the controller's own transmissions.

## Simulation consequence

Do not encode a 1201/1202 internal relay timestamp, named circuit, or speaker attribution until the historical audio is directly inspected and clock-reconciled. Existing radio-side anchors from notes 516–518 remain valid search windows, not substitutes for that reconciliation.

## Sources

- NASA History, *News & Notes*, Vol. 35 No. 3 (2018), Apollo 11 Historical Recorder #1 track-sheet image.
- NASA, Apollo Lunar Surface Journal, *Apollo 11 Mission Audio*.
- NASA/JSC audio catalog entry `792-AAI`, Flight Director's Loop: lunar descent 1955–2025.

## Evidence status

- **PRIMARY/ARCHIVAL CONFIGURATION:** Historical Recorder #1 track sheet: channel 1 IRIG-B GMT; FLIGHT L/R 7/8; CAPCOM L/R 14/15; GUIDO L/R 21/22.
- **NASA PROVENANCE:** ALSJ mission-audio corpus description documents JSC digitization provenance.
- **PRIMARY AUDIO TARGET:** `792-AAI` within its cataloged scope.
- **OPEN:** direct descent-audio inspection; mapping of audio/sample time to GET; exact speaker attribution; named support-room circuit.
