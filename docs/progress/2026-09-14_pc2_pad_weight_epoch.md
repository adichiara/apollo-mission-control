# Progress — PC+2 pad-weight epoch boundary

Date: 2026-09-14

## Completed

- Located the Apollo 13 Technical Air-to-Ground Voice Transcription in NASA NTRS (`20160014370`).
- Verified the indexed NASA transcript passage for the final PC+2 P30 LM maneuver PAD.
- Confirmed operational transmission of CSM `62480 lb` and LM `33452 lb` at GET 077:55:24 for TIG 079:27:38.30.
- Confirmed the crew repeated those weights and CAPCOM accepted the readback at 077:59:50.
- Separated the documented **PAD/targeting weight reference** from the still-unresolved **exact physical/RTCC mass epoch**.
- Added research note 137 and a numerical-validation roadmap addendum.

## Consequence

The existing scenario fixture values have stronger provenance, but the numerical model must not call their sum (`95932 lb`) exact ignition mass until an RTCC/Flight Dynamics or mission-specific weight-accounting source establishes that convention.

## Next

Search mission-specific RTCC/Flight Dynamics maneuver-computation and weight-accounting material, then continue the research-note-130 numerical-input queue.