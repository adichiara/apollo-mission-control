# Progress — PC+2 GDA units and postflight actuator trace

Date: 2026-09-15
Research note: `resources/research/154_pc2_gda_actuator_units_and_postflight_trace.md`

## Completed

- Checked the mission-specific September 1970 NASA *Apollo 13 Mission Report* for the unresolved PC+2 GDA boundary.
- Found the report's maneuver-performance table explicitly labels GDA values as **inches of actuator displacement**.
- Corrected research note 153: the LM CONTROL narrative's approximately `-2` roll-GDA state and `-1.2` change are inches, not degrees; the inferred pre-ignition state is approximately `-0.8 in`.
- Recovered a separate postflight PC+2 GDA displacement trace from the Mission Report: initial pitch/roll `+0.13 / -0.28 in`, roll maximum excursion `-0.44 in`, steady-state pitch/roll `-0.21 / -0.55 in`, cutoff pitch/roll `+0.23 / -0.85 in`.
- Preserved the unresolved sampling/definition difference between that table and the LM CONTROL ignition-transient narrative rather than forcing reconciliation.
- Updated the numerical roadmap, station-status addendum, and PC+2 RTCC/mass-properties source catalog.

## Architecture consequence

The simulator must treat **commanded angular trim** and **GDA actuator displacement** as different typed quantities with explicit units and provenance. The final ~78-hour commanded angular trim pair is still missing.

## Next work

1. Recover the final ~78-hour P30/GDA angular trim artifact and its mass-properties provenance.
2. Search primary LM GDA calibration/geometry documentation for a supported angle↔actuator-displacement relationship.
3. Recover Apollo 13 Mission Report Supplement 2, *Descent Propulsion System Final Flight Evaluation*, for higher-resolution PC+2 propulsion/GDA evidence.