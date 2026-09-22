# Station research status — Apollo 11 descent propellant countdown

Date: 2026-09-21

## CAPCOM

**Status: documented for crew-facing calls.** Primary air-to-ground transcription establishes CAPCOM calls of 60 seconds and 30 seconds during final descent, followed by contact/engine-stop traffic.

## FLIGHT / CONTROL / GUIDANCE

**Status: ownership unresolved.** The Apollo 11 Mission Report establishes the low-level sensor event and the engineering depletion/decision timeline, but the evidence recovered in this pass does not establish which front-room or support-room station owned the countdown calculation or which controller product supplied it.

Do not assign a synthetic `fuel_time_remaining` field to a station merely because CAPCOM voiced the calls. CAPCOM is the transmission endpoint established by the transcript, not evidence of calculation ownership.

## Simulator consequence

Station projections may expose the historically recorded CAPCOM calls in an Apollo 11 reference replay. They must not expose exact physical depletion time or invent a CONTROL/GUIDANCE/FLIGHT display until the Mission-G product path is sourced.

## Next station question

Identify the source-to-station chain for the descent low-level/countdown workflow, ideally from Apollo-11-effective controller handbooks, Mission-G display/data-pack material, controller-loop audio, or contemporary console procedures.

## Evidence status

- **DOCUMENTED:** CAPCOM crew-facing 60/30 calls.
- **DOCUMENTED:** Mission Report low-level and depletion/decision timeline.
- **OPEN:** countdown computation/product provenance and station ownership.
- **NOT CLAIMED:** exact CRT field, timer implementation, RTCC involvement, or support-room wording.