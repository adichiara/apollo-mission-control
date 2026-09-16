# Roadmap — PC+2 GDA trim next targets

Date: 2026-09-16

Research Notes 180–184 separate commanded trim, powered-flight control behavior, maneuver outcome, measured actuator state, and generic GDA mechanical calibration. Apollo 13 primary material establishes that DPS gimbal trim can change automatically during powered flight to compensate for changing center of gravity. Mission Report Table 6.4-I supplies mission-specific 61:29 GDA actuator positions in inches at initial, maximum-excursion, steady-state, and cutoff phases. NASA LM reference material now bounds the generic mechanism at ±2 inches stroke for ±6° engine tilt (nominal endpoint ratio 3°/in), but this does not establish the Apollo 13 crew-facing trim representation or LM-7-specific calibration.

## Priority 1 — ground-computation lineage

Recover a mission-specific artifact that bridges:

`T+55 LM-burn mass-properties deck -> generation/load/run identity -> RTCC/RTACF trim output -> 5.86 / 6.75`

Best targets: weight/c.g. sheet, RTCC/RTACF request/output, job/run record, controller working paper, or support-room product.

## Priority 2 — disagreement details

Recover CONTROL's competing numerical trim and the actual comparison/acceptance basis used when CONTROL challenged Flight Dynamics' solution. Do not apply the T+25 `0.01°` no-update comparison, the later `~0.3°` spacecraft-checkout statement, or the Mission Report's `+0.3 ft/s` post-trim velocity residual to this decision without direct evidence.

## Priority 3 — trim representation / LM-7 calibration

The 61:29 postflight actuator state is documented in Table 6.4-I:

- initial: pitch `-0.02 in`, roll `-0.34 in`;
- maximum excursion: pitch `+0.31 in`, roll `-0.27 in`;
- steady-state: pitch `+0.04 in`, roll `-0.51 in`;
- cutoff: pitch `+0.10 in`, roll `-0.31 in`.

Generic NASA LM documentation establishes ±2 in actuator stroke corresponding to ±6° engine tilt, i.e. a nominal endpoint ratio of 3°/in. Do not use that generic ratio as an exact Apollo 13 telemetry conversion. Recover the primary definition of the crew-facing GDA trim-number reference/zero, axis/sign conventions, and preferably LM-7-specific calibration. Preserve the Mission Report's `Roll` axis label rather than silently translating conventions.

A continuous telemetry trace is only needed if a player-visible product requires finer temporal resolution than the four sourced phase values.

## Priority 4 — executed propulsion profile

Use the postflight Apollo 13 Mission Report as the execution baseline: 34.23-second firing; propulsion narrative reports minimum throttle about 12% for the first 5 seconds, then approximately 37%. Preserve the nominal preburn `10% / 40%` pad values separately as planned/commanded procedure rather than telemetry.

## Modeling rule meanwhile

Use `5.86 / 6.75` only as a sourced commanded/preburn trim reference. For the actual 61:29 actuator state, use the four Table 6.4-I GDA inch values at their source resolution. A generic mechanism visualization may use nominal 3°/in only if explicitly identified as an approximation, never as recovered Apollo 13 angle telemetry. Do not infer the crew-facing trim-number zero/reference. The post-trim translational residual remains `[+0.2, 0.0, +0.3] ft/s` and is not an actuator quantity.
