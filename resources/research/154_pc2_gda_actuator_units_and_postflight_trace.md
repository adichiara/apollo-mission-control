# Research note 154 — Apollo 13 PC+2 GDA actuator units and postflight trace

Date: 2026-09-15

## Question

Can a mission-specific primary source sharpen the final PC+2 GDA boundary and verify the physical units of the actuator values used in research note 153?

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

## Correction to note 153

Research note 153 interpreted the LM CONTROL report's approximately `-2` roll-GDA state and `-1.2` ignition change as degrees. That was unsupported. The mission report establishes the relevant GDA physical reporting convention as **actuator displacement in inches**. Note 153 has been corrected accordingly: its inferred pre-ignition value is approximately `-0.8 in`, not `-0.8°`.

This correction does **not** invalidate the supersession finding. The ~59-hour values were explicitly angular trim values (`5.86°`, `6.75°`) and explicitly update-expected; the later execution record is a distinct actuator-displacement product. They must not be numerically compared as if they were the same quantity.

## New resolved boundary

PC+2 now has three distinct trim/GDA evidence layers:

1. **~59 h crew-facing interim angular trim:** `5.86° / 6.75°`, update explicitly expected;
2. **final commanded angular trim:** still unrecovered;
3. **postflight physical GDA actuator displacement trace:** mission report values in inches, including initial `+0.13 / -0.28 in` pitch/roll and later maneuver values.

The LM CONTROL narrative's larger ignition transient and the Mission Report's tabulated values should not be forced into one number without establishing their exact sampling/definition conventions.

## Evidence boundary

Do not:

- convert actuator inches to engine-gimbal degrees without sourced geometry/calibration;
- substitute the postflight `+0.13 / -0.28 in` initial actuator values for the missing final commanded angular trim;
- assume the tabulated `initial` sample is identical in time/definition to LM CONTROL's immediately-pre-ignition narrative state;
- infer the PC+2 mass-properties job number or explicit `T+55` linkage;
- discard either primary record merely because their reported actuator values differ; their sampling/processing conventions are not yet reconciled.

## Simulation implication

The data model should distinguish at minimum:

`commanded_trim_angle -> commanded/observed actuator displacement -> sampled telemetry/postflight actuator trace`

with units and provenance mandatory. This prevents a controller product expressed in degrees from being silently mixed with a GDA hardware displacement expressed in inches.

## Next archival target

Recover the final ~78-hour PC+2 angular GDA pad/working sheet. In parallel, locate LM GDA calibration/geometry documentation or the Mission Report Supplement 2 propulsion evaluation so angular trim can be related to actuator displacement only if the primary record supports that conversion.