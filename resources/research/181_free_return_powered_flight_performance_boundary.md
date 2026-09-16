# Research Note 181 — 61:29 free-return powered-flight performance boundary

Date: 2026-09-16

## Question

Can mission-specific primary postflight evidence constrain what happened during the 61:29 DPS firing without inventing an unrecovered gimbal-position history?

## Primary evidence

### Apollo 13 Mission Report, MSC-02680, September 1970

NASA NTRS citation: `19710003598`.

Section 8.7.4 states that the docked configuration was manually maneuvered to null primary-guidance error needles before the free-return correction, after which attitude was maintained with primary guidance in AUTO. It then reports that primary-guidance performance during the maneuver was nominal, there were **no vehicle attitude excursions**, and firing time was as predicted.

Section 6.6 reports normal descent-propulsion operation for the 34.3-second free-return correction. The maneuver began at minimum throttle, reported as 12 percent of full thrust, and after 5 seconds was manually increased to approximately 37 percent for the remainder of the firing.

These postflight values are preferable to silently treating the preburn pad's nominal `5 seconds at 10 percent / remainder at 40 percent` as measured execution.

### Apollo 13 GN&C performance-analysis supplement

NASA NTRS citation `19730017939`, *Guidance, navigation, and control systems performance analysis: Apollo 13 mission report*, MSC-02680-SUPPL-1 / TRW-11176-H586-R0-00-SUPPL-1, September 1970, is a mission-specific primary postflight analysis covering the LM digital autopilot among other GN&C systems. Its NTRS metadata makes it a high-priority archival target for the unresolved actuator-history branch. No gimbal-position value is claimed here because the available evidence inspected in this pass did not expose such a value.

## What this establishes

1. The actual 61:29 firing was a nominal primary-guidance/AUTO controlled powered-flight event with no reported vehicle attitude excursions.
2. The postflight propulsion record refines execution from the preburn nominal throttle instruction: approximately 12% initially, then approximately 37% after 5 seconds, for 34.3 seconds total.
3. Stable vehicle attitude does **not** imply static descent-engine gimbal position. Research Note 180 already establishes automatic gimbal trim as a mechanism for compensating changing center of gravity during powered flight.
4. Therefore the simulation may model the vehicle attitude response as nominal/stable for this firing while still leaving exact pitch/yaw GDA actuator history unresolved.

## Evidence boundary

Do **not** infer:

- that `5.86 / 6.75` remained the physical GDA position throughout the firing;
- an exact postburn GDA state from the absence of attitude excursions;
- any T+55 deck value, RTCC/RTACF run identity, or ground-computation acceptance criterion from this postflight performance evidence;
- exact actuator telemetry from the GN&C supplement until the relevant pages/data are actually recovered and inspected.

## Simulation implication

For a historically constrained 61:29 scenario, distinguish three layers:

`commanded/preburn reference (5.86 / 6.75)`

`powered-flight control behavior (AUTO/primary guidance; no reported attitude excursions; automatic trim physically available)`

`exact GDA actuator history (unresolved)`

Use postflight measured/reconstructed propulsion behavior (`34.3 s`, ~12% then ~37%) when modeling the executed burn rather than treating the nominal pad throttle percentages as telemetry.

## Next archival target

Continue the primary ground-computation search for the T+55 generation/load/run artifact. In parallel, recover and inspect the Apollo 13 GN&C performance-analysis supplement and other mission telemetry products specifically for descent-engine pitch/yaw gimbal position during and immediately after the 61:29 firing.