# Research note 155 — Apollo 13 PC+2 GDA dual units and calibration

Date: 2026-09-15

## Question

Does primary LM documentation permit the PC+2 GDA evidence to be reconciled across angular engine-gimbal position and linear actuator stroke, and does it clarify the LM CONTROL `-2` / `-1.2` quantities?

## Primary sources

1. NASA/Grumman, *Apollo News Reference — Lunar Module*, Guidance, Navigation and Control / Main Propulsion sections. NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/LM08_Guidance-Navigation-Control_ppGN1-48.pdf and https://www.nasa.gov/wp-content/uploads/static/history/alsj/LM09_Main_Propulsion_ppMP1-22.pdf
2. NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, Appendix H (LM CONTROL). NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf
3. NASA Manned Spacecraft Center, *Apollo 13 Mission Report*, MSC-02680 / NASA-TM-X-66449, September 1970. NTRS: https://ntrs.nasa.gov/citations/19710003598

## Finding

The LM hardware documentation explicitly gives both representations for the same GDA mechanism:

- actuator stroke: `+2 to -2 in` (±5%);
- engine-gimbal position: `+6° to -6°` (±5%);
- gimbal rate: `0.2°/sec` (±10%).

The Main Propulsion description likewise states that each actuator can extend/retract 2 inches from mid-position to tilt the descent engine a maximum of 6 degrees along its axis. This establishes a sourced hardware-scale relationship of nominally **3 degrees of engine-gimbal position per inch of actuator stroke**. Because the published limits carry tolerances and do not establish exact flight-unit calibration, use this as a nominal scale, not an exact LM-7 calibration curve.

Crucially, the Apollo 13 FCD LM CONTROL narrative itself prints the PC+2 ignition roll-GDA event in **degrees**: approximately `-2°`, a delta of `-1.2°` from the pre-ignition value. Therefore research note 154's blanket reinterpretation of that narrative as inches was incorrect. The implied pre-ignition angular roll-GDA state is approximately `-0.8°`.

Separately, the September Mission Report maneuver-performance table explicitly labels its GDA telemetry values in **inches**. Those values remain linear actuator displacement. The two primary reports are not contradictory merely because they use different units.

## Reconciled evidence layers

PC+2 should now distinguish:

1. ~59 h interim crew-facing commanded angular trim: pitch `5.86°`, roll `6.75°`, explicitly update-expected;
2. final commanded angular trim pair: still unrecovered;
3. LM CONTROL execution narrative: roll GDA about `-0.8°` immediately pre-ignition, moving to about `-2°` at ignition (approximate values from narrative arithmetic);
4. Mission Report postflight GDA telemetry table: actuator displacement in inches, including initial pitch/roll `+0.13 / -0.28 in`, steady-state `-0.21 / -0.55 in`, cutoff `+0.23 / -0.85 in`;
5. generic LM hardware scale: ±2 in actuator stroke corresponds to ±6° engine-gimbal position, nominally 3°/in.

The nominal hardware scale makes the Mission Report's initial roll `-0.28 in` roughly consistent in scale with the LM CONTROL pre-ignition `~ -0.8°` (nominal conversion `-0.84°`), but this is a **cross-check only**. It does not prove identical sampling time, sign convention, telemetry processing, or LM-7 calibration.

## Correction to notes 153–154

Research note 153's original degree interpretation of the LM CONTROL narrative was correct on units. Research note 154 correctly established that the Mission Report table is in inches, but incorrectly generalized that unit to the separate LM CONTROL narrative. Note 153 and derivative documentation must be corrected back to degrees for the LM CONTROL `-2 / -1.2` quantities while retaining inches for the Mission Report table.

## Evidence boundary

Do not:

- use 3°/in as an exact LM-7 flight calibration;
- substitute `-0.28 in × 3°/in` for a recovered final pad trim;
- assume LM CONTROL and Mission Report samples are temporally identical;
- infer the missing final pitch trim, mass-properties job number, or explicit `T+55` linkage.

## Simulation implication

Model GDA state with an explicit representation/unit field. A useful generic hardware transform may use the documented nominal ±2 in ↔ ±6° scale, but historical replay values should preserve their source units and provenance. Final PC+2 commanded trim remains an unresolved archival input.

## Next archival target

Return priority to the final ~78-hour PC+2 P30/GDA artifact or H-2 Flight Dynamics/CONTROL working record. For higher-fidelity hardware modeling, seek LM-7-specific GDA/engine acceptance calibration rather than treating the generic 3°/in scale as exact.