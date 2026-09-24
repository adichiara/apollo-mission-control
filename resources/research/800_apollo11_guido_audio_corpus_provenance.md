# Research Note 800 — Apollo 11 GUIDO audio corpus provenance

**Date:** 2026-09-23  
Research thread: `apollo11-descent-audio-provenance`
**Status:** REVIEWED-PARTIAL

## Question

Can the Mission-G GUIDO historical-recorder assignment recovered in the preceding pass be connected to an accessible primary audio corpus without treating machine-generated transcripts as primary evidence?

## Primary-recording provenance

The Apollo in Real Time Apollo 11 Mission Control Audio interface exposes the restored Mission Control corpus and identifies selectable `GUIDO [L]` and `[R]` channels. Its provenance statement says the corpus consists of approximately 11,000 hours of flight-controller conversation recorded from individual Mission Control headsets and several back rooms. The tapes were digitized in the NSF-funded UT Dallas effort; playback timing distortion was corrected, and the restored recordings retain their original IRIG-B timing signal.

This materially strengthens the recovery route established by the original `AS-506 3RD FL` recorder track sheet: the project has both a Mission-G archival mapping for GUIDO left/right (Historical Recorder #1 channels 21/22, positions 018/019) and a publicly accessible restored audio corpus exposing GUIDO left/right channels.

Source: https://apolloinrealtime.org/11/MOCRviz/MOCRviz.html

NASA independently documents Apollo 11 mission audio and the Apollo journals as repositories for mission audio/transcript material:

- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11MissionAudio.html
- https://www.nasa.gov/history/alsj-and-afj/

## Transcript boundary

Apollo in Real Time explicitly states that its Mission Control transcripts are automated Whisper `large-v3` products and remain imperfect. They are therefore **navigation aids, not historical authority**. Any claim about who spoke, what was said, or the exact call sequence around 1201/1202 must be verified against the restored audio itself (and, where applicable, contemporary NASA transcripts), not accepted solely from automated text.

The restored audio can establish voices present on a recorded station channel and their sequence. It still cannot, by itself, prove which named conference loop a received voice arrived on, or whether a person heard on the recording had transmit privilege on that circuit. Those questions remain dependent on Mission-G-effective keyset/routing evidence.

## Consequence

The next descent-alarm research pass should use the GUIDO left/right restored recordings around the alarm interval as the primary evidence object. Machine transcript search may be used only to locate candidate timestamps. Findings must preserve the distinction between:

1. **recorded station channel** — now mission-specifically mapped and publicly recoverable;
2. **speaker/call sequence** — potentially recoverable from direct audio inspection; and
3. **named loop/keyset privilege** — still unresolved without configuration evidence.

## Evidence status

- **DOCUMENTED / MISSION-SPECIFIC ARCHIVAL:** Historical Recorder #1 channels 21/22 are GUIDO left/right, positions 018/019.
- **DOCUMENTED / PRIMARY-AUDIO RECOVERY ROUTE:** restored Apollo 11 Mission Control corpus exposes GUIDO left/right recordings with IRIG-B-based timing provenance.
- **RESTRICTED TO NAVIGATION:** automated Mission Control transcripts; verify historical claims against audio.
- **NEXT:** inspect the restored GUIDO L/R audio around 1201/1202 and document only directly audible participants, wording, and sequence.
- **UNRESOLVED:** named loop carrying Bales/Garman traffic and exact Mission-G keyset privilege matrix.

## Sources

- Apollo in Real Time, Apollo 11 Mission Control Audio / MOCRviz: https://apolloinrealtime.org/11/MOCRviz/MOCRviz.html
- NASA, Apollo 11 Mission Audio: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11MissionAudio.html
- NASA, Apollo Lunar Surface Journal and Apollo Flight Journal: https://www.nasa.gov/history/alsj-and-afj/
