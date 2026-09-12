# Station Status Addendum — PC+2 onboard 77-percent thrust monitor

Date: 2026-09-12  
Parent: `docs/STATION_RESEARCH_STATUS.md`

## CONTROL / CAPCOM

Both positions remain maturity **B**.

Research note `061_pc2_onboard_thrust_monitor_observation_path.md` confirms the mission-specific crew criterion but does not identify the exact onboard percent-thrust display/signal strongly enough to implement.

Documented:

- ground thrust-chamber-pressure rule and onboard 77-percent thrust rule are distinct;
- CAPCOM read the onboard criterion to the crew as a “thrust monitor readout, 77 percent or below”;
- crew readback repeated the threshold;
- PC+2 was executed in P40.

Explicitly not assumed:

- that the readout came from LGC P47 merely because P47 is named “Thrust Monitor”;
- that the LM thrust-to-weight indicator was the 77-percent display;
- that ground `GQ6510P` chamber pressure was mirrored directly to the crew;
- when, during the commanded 12.6-percent/40-percent startup segments, the 77-percent shutdown threshold became applicable.

### CONTROL

Remains **B**. Ground chamber-pressure monitoring is already source-bounded, but the corresponding crew percent-thrust indication and exact crew/ground cross-check workflow remain unresolved.

### CAPCOM

Remains **B**. The mission-specific rule transmission/readback is strong workflow evidence, but the exact crew display/instrument and procedure applicability timing remain unresolved.

## Current disposition

`crew_thrust_monitor` remains `NOT_EVALUABLE`. This is an implementation gap, not a claim that the crew lacked the indication historically.

Next station-focused research moves to the attitude-error/rate criteria and the start-transient wording conflict unless a direct LM-7 thrust-display source becomes readily available.
