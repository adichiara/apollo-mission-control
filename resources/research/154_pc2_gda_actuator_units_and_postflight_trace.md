# Research note 154 — Apollo 13 PC+2 GDA actuator units and postflight trace

Date: 2026-09-15

> **Correction (research note 155):** this note correctly establishes that the September Mission Report maneuver-performance table reports GDA actuator displacement in **inches**, but it incorrectly generalized that unit to the separate April FCD LM CONTROL narrative. The LM CONTROL `-2` / `-1.2` quantities are printed in **degrees**. Primary LM hardware documentation explicitly supports both representations: ±2 in actuator stroke corresponds to ±6° engine-gimbal position (generic nominal scale, not an exact LM-7 calibration).

## Question

Can a mission-specific primary source sharpen the final PC+2 GDA boundary and verify the physical units of the actuator values in the September Mission Report table?

## Primary source

NASA Manned Spacecraft Center, *Apollo 13 Mission Report*, MSC-02680 / NASA-TM-X-66449, September 1970.

NTRS catalog: https://ntrs.nasa.gov/citations/19710003598

The mission report's maneuver-performance table explicitly labels **Gimbal drive actuator** values in **inches**. For the PC+2 / transearth-injection DPS maneuver it reports the postflight actuator trace including approximately:

- initial pitch: `+0.13 in`;
- initial roll: `-0.28 in`;
- roll maximum excursion: `-0.44 in`;
- steady-state pitch: `-0.21 in`;
- steady-state roll: `-0.55 in`;
- cutoff pitch: `+0.23 in`;
- cutoff roll: `-0.85 in`.

The table is a postflight maneuver-performance product, not the preburn P30/GDA pad.

## Unit boundary corrected by note 155

These table values are linear actuator displacement. They must remain distinct from commanded angular trim. However, the separate LM CONTROL narrative reports its ignition GDA event in degrees, not inches. Apollo LM hardware documentation confirms that GDA state can legitimately be represented both as linear actuator stroke and as resulting engine-gimbal angle.

## Resolved boundary

PC+2 has distinct trim/GDA evidence layers:

1. **~59 h crew-facing interim angular trim:** `5.86° / 6.75°`, update explicitly expected;
2. **final commanded angular trim:** still unrecovered;
3. **LM CONTROL execution angular state:** roll approximately `-0.8°` pre-ignition, moving to approximately `-2°` at ignition;
4. **postflight physical GDA actuator displacement trace:** Mission Report values in inches, including initial `+0.13 / -0.28 in` pitch/roll and later maneuver values;
5. **generic hardware relationship:** ±2 in stroke ↔ ±6° gimbal position, nominally 3°/in, with published tolerances.

## Evidence boundary

Do not:

- treat the generic 3°/in hardware scale as exact LM-7 calibration;
- substitute the postflight `+0.13 / -0.28 in` initial actuator values for the missing final commanded angular trim;
- assume the tabulated `initial` sample is identical in time/definition to LM CONTROL's immediately-pre-ignition narrative state;
- infer the PC+2 mass-properties job number or explicit `T+55` linkage.

The nominal scale makes `-0.28 in` correspond to about `-0.84°`, close to LM CONTROL's approximate pre-ignition `-0.8°`; note 155 treats this only as a consistency cross-check, not proof of sample identity.

## Simulation implication

The data model should distinguish at minimum:

`commanded_trim_angle -> observed_engine_gimbal_angle <-> actuator_displacement -> sampled_telemetry/postflight_trace`

with units and provenance mandatory. A generic nominal hardware transform may use ±2 in ↔ ±6°, while historical replay should preserve source-native quantities.

## Next archival target

Recover the final ~78-hour PC+2 angular GDA pad/working sheet. For higher-fidelity conversion, locate LM-7-specific GDA/engine acceptance calibration rather than assuming the generic nominal hardware scale is exact.