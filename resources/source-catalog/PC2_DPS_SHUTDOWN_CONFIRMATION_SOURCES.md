# Apollo 13 PC+2 DPS Shutdown Confirmation Sources

Status: active focused source supplement.

## Apollo 13 Mission Operations Report

- **Title:** *Mission Operations Report — Apollo 13*
- **Organization:** NASA MSC Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** Establishes thrust chamber pressure as a ground-observed PC+2 shutdown-rule quantity and documents the PC+2 maneuver chronology.
- **Boundary:** Does not define a numeric chamber-pressure value as the formal ground meaning of `engine off`.

## Apollo 13 air-ground / mission commentary record

- **Source class:** PRIMARY / contemporaneous mission record
- **Use:** Preserves Lovell's PC+2 cutoff report, “Shutdown,” and CAPCOM's acknowledgement.
- **Boundary:** Crew report is an evidence channel, not authoritative physical-state truth.

## LM elementary functional diagrams measurement index

- **Measurement:** `GQ6510P`
- **Definition:** PRESS, THRUST CHAMBER
- **Source class:** CONTEMPORARY LM technical documentation
- **Use:** Identifies the measurement semantics used by the project chamber-pressure path.

## Apollo 10 LM DPS raw-data report

- **NASA NTRS ID:** 19690026326
- **Source class:** PRIMARY, mission engineering data
- **Use:** Shows `GQ6510P` responding through ignition/thrust and falling during shutdown, supporting chamber pressure as response evidence.
- **Boundary:** Apollo 10 shutdown timing and numerical tailoff values are not imported into Apollo 13.

## Repository research record

- `resources/research/055_pc2_dps_chamber_pressure_observation_path.md`
- `resources/research/069_pc2_dps_shutdown_command_and_physical_response.md`
- `resources/research/070_pc2_dps_shutdown_confirmation_evidence.md`

## Implementation rule

Represent crew report and post-command chamber-pressure observation as separate evidence channels. Do not manufacture a dedicated engine-off discrete, an exact confirmation latency, or a chamber-pressure threshold meaning engine off.
