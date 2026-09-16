# Progress — 61:29 free-return GDA actuator history

Date: 2026-09-16

## Completed

Recovered mission-specific GDA actuator values for the Apollo 13 61:29 free-return DPS maneuver from the primary *Apollo 13 Mission Report*, Table 6.4-I.

The table reports GDA position in inches:

- initial: pitch `-0.02`, roll `-0.34`;
- maximum excursion: pitch `+0.31`, roll `-0.27`;
- steady-state: pitch `+0.04`, roll `-0.51`;
- cutoff: pitch `+0.10`, roll `-0.31`.

Research Note 184 additionally recovers the generic NASA LM GDA mechanical range: ±2 inches actuator stroke corresponds to ±6° engine tilt, giving a nominal endpoint ratio of 3°/in. This is a mechanism-scale bound, not an Apollo 13/LM-7 calibration or a definition of the crew-facing `5.86 / 6.75` trim representation.

This closes the exact-value actuator-history target at the resolution of the postflight summary and the generic mechanism-scale question. It does not provide a continuous telemetry trace, LM-7-specific calibration, or a sourced mapping from actuator inches to the preburn angular trim-number representation.

## Documentation impact

- added Research Notes 183 and 184;
- updated the PC+2 GDA roadmap;
- updated GDA trim source catalog;
- updated station-research status for CONTROL/GDA monitoring.

## Next unresolved item

Continue the main provenance target: recover a T+55 generation/load or downstream RTCC/RTACF run/request/output artifact tying the LM-burn mass-properties deck to `5.86 / 6.75`, ideally including weight/c.g., CONTROL's competing trim, and the comparison criterion. In parallel, seek the primary GDA trim representation definition/LM-7 calibration needed to explain the crew-facing numbers without assuming their zero or sign convention.
