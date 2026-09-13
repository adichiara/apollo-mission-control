# Progress — PC+2 spacecraft physical-model scope

Date: 2026-09-13  
Status: **RESOLVED FOR FIRST PLAYABLE**

## Completed

- Reviewed the next unresolved scenario-scope item: open question 12, how much spacecraft physics the PC+2 slice requires.
- Used primary Apollo/NASA subsystem sources for LM instrumentation, DPS, guidance/control, electrical power, and communications, together with the already reviewed Apollo 13 PC+2 mission chronology.
- Added research note 102 and `PC2_SPACECRAFT_MODEL_SCOPE_SOURCES.md`.
- Defined a decision-relevant causal-fidelity rule: model only physical state required to generate sourced player information, enforce sourced rules/procedures, or support a selected branch.
- Required causal domains are DPS/maneuver state, guidance/attitude/control state, coarse electrical/equipment availability, communications/uplink/ranging availability, and instrumentation observation integrity.
- Explicitly deferred full ECS/CSM physics, six-DOF propagation, pulse-level RCS, detailed battery/wiring physics, RF physics, complete LM instrumentation, and internal RTCC/CCATS computation until a sourced scenario dependency requires them.
- No historical station maturity grade is changed by this pass.

## Result

Open question 12 is resolved for the current PC+2 first playable. This prevents full-spacecraft-simulator scope creep without authorizing unsupported simplification: any omitted subsystem must be added when a sourced player decision or failure mechanism depends on it.

## Remaining validation

Physical seven-seat nominal validation, synthetic ΔP validation, and five-player compact validation remain unclosed.