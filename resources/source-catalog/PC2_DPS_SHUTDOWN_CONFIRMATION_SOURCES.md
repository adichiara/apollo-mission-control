# Apollo 13 PC+2 DPS Shutdown Confirmation Sources

Status: active focused source supplement.

## Apollo 13 Mission Operations Report

- **Title:** *Mission Operations Report — Apollo 13*
- **Organization:** NASA MSC Flight Control Division
- **Date:** 28 April 1970
- **NTRS record:** 19710010485
- **URL:** https://ntrs.nasa.gov/citations/19710010485
- **Source class:** PRIMARY, mission-specific
- **Use:** Establishes thrust chamber pressure as a ground-observed PC+2 shutdown-rule quantity and documents the PC+2 maneuver chronology.
- **Boundary:** Does not define a numeric chamber-pressure value as the formal ground meaning of `engine off`.

## Apollo 13 air-ground / mission commentary record

- **Source class:** PRIMARY / contemporaneous mission record
- **Use:** Preserves a PC+2 crew cutoff/shutdown report and CAPCOM acknowledgement.
- **Boundary:** Crew report is an evidence channel, not authoritative physical-state truth. The nominal mission wording is not assumed to be the exact response wording for a hypothetical ΔP exceedance.

## LM elementary functional diagrams measurement index

- **Measurement:** `GQ6510P`
- **Definition:** PRESS, THRUST CHAMBER
- **Source class:** CONTEMPORARY LM technical documentation
- **Use:** Identifies the measurement semantics used by the project chamber-pressure path.

## Apollo 10 LM DPS raw-data report

- **Title:** *Apollo 10 LM-4, Descent Propulsion System Final Flight Evaluation*
- **NASA NTRS ID:** 19690026326
- **URL:** https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19690026326.pdf
- **Source class:** PRIMARY, mission engineering data
- **Use:** Shows `GQ6510P` responding through ignition/thrust and falling during shutdown, supporting chamber pressure as response evidence.
- **Boundary:** Apollo 10 shutdown timing, numerical tailoff values, and pressure magnitudes are not imported into Apollo 13.

## Repository research record

- `resources/research/055_pc2_dps_chamber_pressure_observation_path.md`
- `resources/research/069_pc2_dps_shutdown_command_and_physical_response.md`
- `resources/research/070_pc2_dps_shutdown_confirmation_evidence.md`
- `resources/research/086_pc2_shutdown_evidence_http_integration.md`

## Implementation rule

Represent crew report and post-command chamber-pressure observation as separate evidence channels. A chamber-pressure observation counts only if its source/sample time is after the shutdown command. Do not manufacture a dedicated engine-off discrete, an exact confirmation latency, a chamber-pressure threshold meaning engine off, or an automatic `engine_off_confirmed` verdict.

The HTTP/session integration deliberately does not consult authoritative `engine_running` when assessing controller evidence.
