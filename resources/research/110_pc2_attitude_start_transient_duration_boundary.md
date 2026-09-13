# Apollo 13 PC+2 — attitude start-transient duration boundary

Date: 2026-09-13  
Status: **REVIEWED — engineering meaning bounded; Apollo 13 operational duration unresolved**

## Question

Can the PC+2 attitude-error shutdown-rule exception for the “start transient” be given a defensible numeric duration or end condition?

## Primary evidence

### Apollo 13 operational rule

The contemporaneous Apollo 13 CAPCOM transmission at 76:30 GET and Fred Haise’s readback at 76:37 GET establish the operational wording used for PC+2: ±10-degree attitude error carried an exception for the start transient, followed by a separate ±10-degree/sec attitude-rate limit. Neither transmission defines the transient’s duration or an end condition.

The later Flight Control Division *Mission Operations Report — Apollo 13* conflicts on which attitude criterion carries the exception, as documented in research note 109, but likewise does not provide a numeric start-transient duration.

### DPS engineering use of “start transient”

NASA’s *Apollo 14 Mission Report, Supplement 5 — Descent Propulsion System Final Flight Evaluation* treats “start transient” as a specific engine-start performance interval. For Apollo 14 it reports:

- ignition delay from engine-fire signal FS-1 to first chamber-pressure rise of about 0.55 s;
- that delay compared favorably with the first-burn delay observed on Apollo 13;
- FS-1 to 90% of the minimum steady-state throttle setting required 2.14 s;
- the specification limit for a minimum-throttle start was 4.0 s;
- 90% to 100% of the minimum throttle setting required another 0.13 s.

Source: NASA MSC-04112, Supplement 5, *Apollo 14 Mission Report — Descent Propulsion System Final Flight Evaluation*, section 9, “Start and Shutdown Transients.”

Later Apollo DPS performance supplements use the same engineering concept and report similarly short start-transient intervals. This corroborates that “start transient” was an engine-start phenomenon measured in seconds, not a synonym for an entire multi-step commanded throttle profile.

## What this does and does not establish

The engineering evidence materially narrows interpretation:

- it argues against treating the PC+2 “start transient” exception as the entire 5 s low-thrust + 21 s 40%-thrust sequence through burn +26 s;
- it shows that Apollo DPS engineering used “start transient” for a short interval beginning at the engine-fire/start signal and ending as the engine approached its commanded minimum steady-state thrust;
- it does **not** establish that the Apollo 13 PC+2 flight-rule exception was exactly 2.14 s, 4.0 s, or any other Apollo 14/15/16 value;
- it does **not** prove that the operational rule’s end condition was “90% of minimum steady-state throttle,” even though that was an engineering performance metric;
- it does **not** override the contemporaneous Apollo 13 rule allocation established in note 109.

The Apollo 14 figure is cross-mission engineering evidence. Promoting it to an Apollo 13 operational rule would violate the project’s research-first/no-invention standard.

## First-playable boundary

For the current PC+2 implementation:

1. retain the note-109 operational allocation: ±10-degree attitude error carries the startup exception;
2. do not encode a numeric exception window from the 2.14 s Apollo 14 performance result or the 4.0 s engine specification;
3. do not extend the exception automatically to burn +5 s, +21 s, or +26 s;
4. if a synthetic attitude-error excursion occurs at a time where the exception would determine the decision, classify the exception itself as `NOT_EVALUABLE` unless the scenario explicitly labels a synthetic transient boundary;
5. nominal PC+2 can proceed without inventing this timing because no source-backed nominal attitude excursion requires the exception to decide the historical outcome.

## Research disposition

The targeted review therefore **bounds but does not numerically resolve** the remaining archival gap. A future upgrade requires an Apollo 13-specific mission rule, procedure, controller working aid, simulation document, or comparable primary record that explicitly defines the operational transient window/end condition.

Until such a source is recovered, the unresolved timing is not a blocker for the nominal first playable and must not be silently converted into executable historical behavior.

## Sources

1. NASA, *Apollo 13 Mission Commentary / Technical Air-to-Ground Transcription*, GET 76:30–76:38: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
2. NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
3. NASA Manned Spacecraft Center, MSC-04112 Supplement 5, *Apollo 14 Mission Report — Descent Propulsion System Final Flight Evaluation*, September 1972, section 9: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a14/a14DPSPerformance.pdf
4. NASA, *Apollo 15 Mission Report Supplement — Descent Propulsion System Final Flight Evaluation*, NTRS record 19730023018: https://ntrs.nasa.gov/citations/19730023018
5. NASA, *Apollo 16 Mission Report Supplement — Descent Propulsion System Final Flight Evaluation*, NTRS record 19740024177: https://ntrs.nasa.gov/citations/19740024177
