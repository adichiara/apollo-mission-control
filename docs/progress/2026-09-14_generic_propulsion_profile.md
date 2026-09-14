# Progress — generic propulsion profile contract

Date: 2026-09-14

## Completed

- Generalized the mission-neutral Level-1 propulsion model without adding any Apollo-specific constants.
- A propulsion segment can now supply:
  - start thrust;
  - optional end thrust for a linear delivered-thrust profile;
  - fixed direction;
  - optional segment-specific effective specific impulse;
  - a descriptive regime label such as `startup`, `regulated`, or `blowdown`.
- Regime labels are metadata only. They do not select hidden engine, valve, pressurization, or blowdown physics.
- Preserved backward compatibility: an ordinary `BurnSegment(duration, thrust, direction)` remains a constant-thrust segment using the run-wide Isp.
- Extended the facilitator model-proof API to accept the new optional fields.
- Added unit/API/browser-suite coverage for:
  - linear-ramp impulse and propellant accounting;
  - split-profile invariance;
  - segment-specific Isp behavior;
  - invalid end-thrust / Isp inputs.

## Architectural consequence

The numerical engine no longer requires PC+2-specific branches to represent a sourced startup or terminal thrust decay. Any later Apollo scenario can provide a source-backed delivered-thrust profile through the same contract.

This is still a Level-1 numerical input mechanism, not a historical engine model. It does not infer a transient curve, throttle calibration, effective Isp, or blowdown law.

## Next

1. Validate this change through CI and the deployed numerical test runner.
2. Continue archival recovery of Apollo 13 Supplement 2 / LM-7 propulsion data.
3. In parallel, start separating reusable mission/scenario configuration from the current PC+2 session scaffold so additional scenarios can use the same causal model.
