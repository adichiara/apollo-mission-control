# PC+2 Attitude-Error / Attitude-Rate Source Catalog

Status: **active implementation-source supplement**

## Mission Operations Report — Apollo 13

- **Organization:** NASA Flight Control Division, Manned Spacecraft Center
- **Date:** 1970-04-28
- **URL:** https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf
- **Status:** PRIMARY / REVIEWED-DETAILED for PC+2
- **Use:** establishes 10 deg/s attitude-rate and 10 deg attitude-error shutdown limits; postflight wording places the startup-transient exception on attitude rate; CONTROL postflight account reports about 7 deg maximum roll error and rates below about 1 deg/s during PC+2.
- **Limitation:** does not define the duration of “start transients.”

## Report of Apollo 13 Review Board — Appendices B–E

- **Organization:** NASA
- **Date:** May 1970
- **Report:** NASA-TM-X-66472
- **NTRS ID:** 19700078726
- **URL:** https://ntrs.nasa.gov/citations/19700078726
- **Status:** PRIMARY / REVIEWED-PARTIAL
- **Use:** independently repeats the guidance/control shutdown parameters as attitude rate >10 deg/s except during start transient, and attitude error >10 deg.
- **Limitation:** does not define the startup-transient time boundary. It is corroborating postflight evidence, not a reason to override the contemporaneous crew-facing instruction.

## Apollo 13 Technical/PAO Air-to-Ground Transcription

- **Source:** NASA mission transcription
- **Relevant interval:** 76:30–76:38 GET
- **URL:** https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- **Status:** PRIMARY / REVIEWED-DETAILED
- **Use:** CAPCOM at 76:30:31 GET assigns the startup-transient exception to ±10 deg attitude error and gives ±10 deg/s attitude rate without an exception; Haise’s readback at 76:37:13 GET repeats the same allocation.
- **Implementation precedence:** used for the operational executable rule because it is the instruction actually transmitted to and confirmed by the crew before PC+2.
- **Limitation:** no duration or exact start/end definition for the transient is given.

## Apollo Experience Report — Engineering and Analysis Mission Support

- **Author:** R. W. Fricke, Jr.
- **Report:** NASA-TN-D-7993 / JSC-S-438
- **NTRS ID:** 19750018953
- **Date:** 1975-07-01
- **URL:** https://ntrs.nasa.gov/citations/19750018953
- **Status:** CONTINUITY / TELEMETRY-DISPLAY SUPPORT
- **Use:** supports distinct LM attitude-error and RGA/angular-rate measurement families and their association with Apollo ground display masks.
- **Limitation:** retrospective Apollo-wide source; does not certify exact Apollo 13 LM-7 PCM word, calibration, CONTROL CRT field, or cadence.

## Research records

- `resources/research/062_pc2_attitude_error_rate_shutdown_path.md`
- `resources/research/063_pc2_attitude_projection_and_rule_integration.md`
