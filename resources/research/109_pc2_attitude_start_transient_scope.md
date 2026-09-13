# Apollo 13 PC+2 — attitude start-transient rule scope

Date: 2026-09-13  
Status: **REVIEWED — operational rule allocation resolved; transient duration remains unresolved**

## Question

Which PC+2 attitude shutdown criterion carried the documented “start transient” exception: attitude error, attitude rate, or both?

## Primary evidence

### Real-time CAPCOM instruction — 76:30:31 GET

NASA's Apollo 13 air-to-ground/mission-commentary transcript records CAPCOM Vance Brand reading the PC+2 shutdown rules to the crew. The transmitted sequence assigns the exception to the attitude-error criterion: attitude error ±10 degrees **with the exception of the start transient**, followed separately by attitude-rate limits of ±10 degrees/sec.

Source: NASA, *Apollo 13 Mission Commentary / Technical Air-to-Ground Transcription*, 76:30 GET.

### Crew readback — 76:37:13 GET

Fred Haise's readback independently repeats the same allocation: ±10-degree attitude error except for starting transients, then ±10-degree/sec rate limits without an exception. CAPCOM did not correct that readback.

This is the strongest evidence for the operational rule actually communicated to and acknowledged by the spacecraft crew immediately before PC+2.

### Flight Control Division Mission Operations Report — 28 April 1970

The later postflight summary phrases the pair differently: “attitude rate limit, except start transients, 10°/sec and attitude error limit 10°.” This conflicts with the real-time transmission/readback.

The same report's CONTROL appendix later summarizes the rule more generically as rates >10°/sec and/or attitude errors >10°, without defining a startup exception.

## Interpretation

For first-playable operational behavior, use the contemporaneous transmitted-and-read-back rule:

- **attitude error:** ±10 degrees, except during the undefined start transient;
- **attitude rate:** ±10 degrees/sec, with no sourced startup exception.

This is not a claim that every ground-controller working aid used identical punctuation. It is a provenance choice: where the postflight summary conflicts with the rule actually sent to and confirmed by the crew, the real-time operational communication controls the executable crew-facing interpretation.

## Remaining boundary

The sources reviewed do **not** define the exact start/end time of the “start transient.” Therefore:

- do not equate it automatically with the entire 12.6% + 40% low-thrust interval;
- do not assign a numeric duration such as 5, 21, or 26 seconds without a direct source;
- do not create a generic hidden `startup_transient=true` interval from inferred engine dynamics;
- until a source or explicit scenario event defines that interval, an attitude-error excursion that depends on the exception remains `NOT_EVALUABLE` with respect to the exception itself.

The attitude-rate criterion remains evaluable whenever a source-backed rate observation exists because the operationally transmitted rule gives it no startup exception.

## Project effect

This resolves the **scope** conflict recorded in research note 053 and the attitude source catalog, but not the transient-duration question. No nominal telemetry values are invented and no physical-play PASS claim changes.

## Sources

1. NASA, *Apollo 13 Mission Commentary / Technical Air-to-Ground Transcription*, GET 76:30–76:38: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
2. NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, III-25 and CONTROL appendix: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
