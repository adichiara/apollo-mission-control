# PC+2 Attitude-Error / Attitude-Rate Source Catalog

Status: **active implementation-source supplement**

## Mission Operations Report — Apollo 13

- **Organization:** NASA Flight Control Division, Manned Spacecraft Center
- **Date:** 1970-04-28
- **URL:** https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- **Status:** PRIMARY / REVIEWED-DETAILED for PC+2
- **Use:** establishes 10 deg/s attitude-rate and 10 deg attitude-error shutdown limits; the III-25 postflight wording places the startup-transient exception on attitude rate; the CONTROL appendix later summarizes rates >10 deg/s and/or attitude errors >10 deg without defining a startup exception. The CONTROL account also reports about 7 deg maximum roll error and rates below about 1 deg/s during PC+2.
- **Limitation:** conflicts with the contemporaneous crew-facing rule transmission on which criterion carries the startup exception and does not define the duration of “start transients.”

## Apollo 13 Technical/PAO Air-to-Ground Transcription

- **Source:** NASA mission transcription
- **Relevant interval:** 76:30–76:38 GET
- **URL:** https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- **Status:** PRIMARY / REVIEWED-DETAILED
- **Use:** CAPCOM at 76:30:31 GET assigns the startup-transient exception to ±10 deg attitude error and gives ±10 deg/s attitude rate without an exception; Haise’s 76:37:13 GET readback repeats the same allocation, with no CAPCOM correction.
- **Implementation precedence:** research note 109 formalizes use of this contemporaneous transmitted-and-read-back wording for the operational first-playable rule when it conflicts with the later postflight summary.
- **Limitation:** no duration or exact start/end definition for the transient is given.

## Apollo 14 Mission Report, Supplement 5 — Descent Propulsion System Final Flight Evaluation

- **Organization:** NASA Manned Spacecraft Center / TRW Systems
- **Report:** MSC-04112 Supplement 5
- **Date:** September 1972
- **URL:** https://www.nasa.gov/wp-content/uploads/static/history/alsj/a14/a14DPSPerformance.pdf
- **Status:** PRIMARY / REVIEWED-DETAILED / CROSS-MISSION ENGINEERING EVIDENCE
- **Use:** section 9 defines DPS start-transient performance from engine-fire signal FS-1. Apollo 14 ignition delay to first chamber-pressure rise was about 0.55 s and explicitly compared favorably with the first-burn delay observed during Apollo 13. FS-1 to 90% of the minimum steady-state throttle setting required 2.14 s, with a 4.0 s specification limit for a minimum-throttle start; 90% to 100% required another 0.13 s.
- **Interpretive value:** establishes that Apollo DPS engineering used “start transient” for a short engine-start phenomenon measured in seconds, not for the entire later commanded throttle profile.
- **Limitation:** Apollo 14 engineering performance is not an Apollo 13 PC+2 operational flight-rule timing definition. It does not authorize a 2.14 s or 4.0 s historical rule gate.

## Apollo 15 DPS Final Flight Evaluation

- **Organization:** NASA
- **NTRS ID:** 19730023018
- **URL:** https://ntrs.nasa.gov/citations/19730023018
- **Status:** PRIMARY / REVIEWED-PARTIAL / CROSS-MISSION CORROBORATION
- **Use:** uses the same DPS start-transient engineering concept and reports a 2.35 s FS-1-to-90%-minimum-steady-state interval with a 4.0 s specification limit; its ignition delay is compared with earlier Apollo flights including Apollo 13.
- **Limitation:** corroborates terminology/scale only; not an Apollo 13 operational rule source.

## Apollo 16 Mission Report Supplement — Descent Propulsion System Final Flight Evaluation

- **Organization:** NASA
- **NTRS ID:** 19740024177
- **URL:** https://ntrs.nasa.gov/citations/19740024177
- **Status:** PRIMARY / REVIEWED-PARTIAL / CROSS-MISSION CORROBORATION
- **Use:** again treats the start transient as a short FS-1-to-near-steady-state engine-start interval and compares ignition delay with Apollo 13–15.
- **Limitation:** corroborates engineering terminology/scale only; not an Apollo 13 PC+2 operational rule source.

## Report of Apollo 13 Review Board — Appendices B–E

- **Organization:** NASA
- **Date:** May 1970
- **Report:** NASA-TM-X-66472
- **NTRS ID:** 19700078726
- **URL:** https://ntrs.nasa.gov/citations/19700078726
- **Status:** PRIMARY / REVIEWED-PARTIAL
- **Use:** provides corroborating postflight guidance/control material and preserves the same general ±10-degree / ±10-degree-sec shutdown-rule family.
- **Limitation:** retrospective/postflight evidence; it does not override the contemporaneous crew-facing instruction and does not define the startup-transient time boundary.

## Apollo Experience Report — Engineering and Analysis Mission Support

- **Author:** R. W. Fricke, Jr.
- **Report:** NASA-TN-D-7993 / JSC-S-438
- **NTRS ID:** 19750018953
- **Date:** 1975-07-01
- **URL:** https://ntrs.nasa.gov/citations/19750018953
- **Status:** CONTINUITY / TELEMETRY-DISPLAY SUPPORT
- **Use:** supports distinct LM attitude-error and RGA/angular-rate measurement families and their association with Apollo ground display masks.
- **Limitation:** retrospective Apollo-wide source; does not certify exact Apollo 13 LM-7 PCM word, calibration, CONTROL CRT field, or cadence.

## Current first-playable interpretation

- attitude error: ±10 degrees, except during the undefined start transient;
- attitude rate: ±10 degrees/sec, with no sourced startup exception in the contemporaneous transmitted/read-back rule;
- engineering evidence indicates “start transient” was a short engine-start phenomenon, not the complete +26 s low-throttle buildup;
- exact Apollo 13 operational transient duration/end condition remains unresolved and **must not** be inferred from Apollo 14/15/16 performance values or from the 5-second, 21-second, or burn +26-second throttle landmarks;
- an attitude-error excursion whose disposition depends on the transient exception remains `NOT_EVALUABLE` unless an Apollo 13-specific operational source or an explicitly synthetic scenario boundary defines that interval.

## Research records

- `resources/research/062_pc2_attitude_error_rate_shutdown_path.md`
- `resources/research/063_pc2_attitude_projection_and_rule_integration.md`
- `resources/research/109_pc2_attitude_start_transient_scope.md`
- `resources/research/110_pc2_attitude_start_transient_duration_boundary.md`
