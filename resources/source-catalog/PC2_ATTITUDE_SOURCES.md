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

## Report of Apollo 13 Review Board — Appendices B–E

- **Organization:** NASA
- **Date:** May 1970
- **Report:** NASA-TM-X-66472
- **NTRS ID:** 19700078726
- **URL:** https://ntrs.nasa.gov/citations/19700078726
- **Status:** PRIMARY / REVIEWED-PARTIAL
- **Use:** provides corroborating postflight guidance/control material and preserves the same general ±10-degree / ±10-degree/sec shutdown-rule family.
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
- exact transient duration: unresolved and not inferred from the 5-second 12.6-percent segment, 21-second 40-percent segment, or burn +26-second full-throttle transition.

## Research records

- `resources/research/062_pc2_attitude_error_rate_shutdown_path.md`
- `resources/research/063_pc2_attitude_projection_and_rule_integration.md`
- `resources/research/109_pc2_attitude_start_transient_scope.md`
