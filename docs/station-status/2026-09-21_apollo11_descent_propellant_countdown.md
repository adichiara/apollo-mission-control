# Station research status — Apollo 11 descent propellant countdown

Date: 2026-09-21

## CAPCOM

**Status: documented for crew-facing calls.** Primary air-to-ground transcription establishes CAPCOM calls of 60 seconds and 30 seconds during final descent, followed by contact/engine-stop traffic. CAPCOM is the crew-facing relay, not the countdown owner.

## CONTROL

**Status: research-sufficient for countdown ownership/procedure.** NASA JSC oral-history material identifies Robert L. Carlton as LM CONTROL on Gene Kranz's White Team. Carlton's first-person recollection describes watching a stopwatch and altitude during final descent and records 18 seconds remaining to the abort point at engine shutdown. NASA's Apollo 11 historical treatment, based on the JSC oral history, states that the low-level condition caused Carlton to start a stopwatch marked for the remaining-time calls.

Supported station behavior is therefore:

`low-level observation → CONTROL starts procedural stopwatch → CONTROL remaining-time call → CAPCOM relay`

This is materially different from a synthetic continuously calculated `fuel_time_remaining` telemetry field.

## FLIGHT / GUIDANCE / RTCC

**Status: no countdown-computation ownership claimed.** The recovered evidence does not require FLIGHT, GUIDANCE, or RTCC to calculate the late-descent countdown. They must not receive an invented exact-fuel timer merely to support the historical 60/30 calls.

## Simulator consequence

The Apollo 11 CONTROL projection may expose the low-level observation and a procedural stopwatch/countdown state once triggered. CONTROL can generate the sourced remaining-time calls for relay through CAPCOM. The timer must be driven from the observed low-level event/procedure, not hidden authoritative physical depletion time.

Do not invent an exact CRT field, parameter mnemonic, support-room message, or RTCC product. Those details remain unrecovered and are unnecessary to implement the sourced operational behavior.

## Next station question

Countdown station ownership is closed to implementation sufficiency. The next Apollo 11 powered-descent station research should address the next unresolved player-visible/controller decision dependency. Recovering the exact Mission-G CONTROL checklist/product for timer initiation is useful if encountered but is no longer a standing blocker.

## Evidence status

- **DOCUMENTED:** CAPCOM crew-facing 60/30 calls.
- **DOCUMENTED:** Mission Report low-level and depletion/decision timeline.
- **DOCUMENTED / RETROSPECTIVE FIRST-PERSON:** Carlton/CONTROL stopwatch use and abort-point timing.
- **RESEARCH-SUFFICIENT:** CONTROL ownership of the procedural countdown/call path.
- **NOT CLAIMED:** exact CRT field, telemetry mnemonic, RTCC involvement, support-room wording, or exact written checklist.