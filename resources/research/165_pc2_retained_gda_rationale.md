# Research note 165 — PC+2 retained-GDA rationale

Date: 2026-09-15

## Question

Can a primary controller source explain why PC+2 deliberately skipped a new Noun 48 trim load, even if the upstream RTCC calculation/job remains unrecovered?

## Primary-source finding

Yes, partially. The CONTROL section of the NASA Manned Spacecraft Center Flight Control Division *Mission Operations Report — Apollo 13* (MSC-02680, 28 April 1970), in its PC+2 execution narrative, records the actual GDA response at ignition and then states the controller expectation behind the retained setting.

At PC+2 ignition the report says the roll GDA moved to approximately `-2°`, a change of `-1.2°` from its pre-ignition value. It then says this was unexpected because **the ground believed the GDA settings at the end of MCC-3, with the 40-percent-thrust compliance, would provide the optimum GDA alignment**.

Primary scan/indexed copy:
- NASA/MSC Flight Control Division, *Mission Operations Report — Apollo 13*, MSC-02680, 28 April 1970, CONTROL section H-4/H-5.
- Alternate searchable scan: https://www.ccas.us/CCAS_NASA_PressKits/Apollo_Missions/Apollo13_MissionOperationsReport.pdf

## Interpretation

This materially narrows the no-trim rationale. The final PC+2 decision was not merely an unexplained omission of Noun 48. CONTROL expected the **already-established GDA state from the preceding DPS maneuver, after its 40% thrust compliance, to be the optimum alignment for PC+2**. That expectation is consistent with the later Flight Director ground rule that no PC+2 maneuver trims were required and with the explicit V34 termination before Noun 48.

The unexpected `-1.2°` roll-GDA motion at PC+2 ignition is also important: it shows that the retained-state assumption was an operational engineering judgment, not proof that the gimbal would remain fixed at ignition.

## Evidence boundary

This does **not** recover the upstream RTCC/CONTROL calculation, candidate trim pair, comparison delta, tolerance, or job identifier. It also does not justify translating the report's `MCC-3` label into a different maneuver name; repository documentation should preserve the source's nomenclature unless a separate primary-source reconciliation establishes otherwise.

Do not infer that the earlier `5.86° / 6.75°` transmitted pair was the exact retained pre-PC+2 state. The report instead supplies the controller rationale at the level actually supported: the ground considered the GDA settings left by the preceding maneuver's 40%-thrust compliance to be optimum.

## Consequence for simulator research

The historical workflow can now be represented more specifically as:

`mass-properties/reference work -> preceding DPS maneuver establishes/complies GDA state at 40% thrust -> ground judges that resulting state optimum for PC+2 -> explicit no-trim ground rule -> V34 after N47 -> no N48 trim entry -> retained state carried into PC+2 -> unexpected roll-GDA response at ignition`.

For a historically constrained simulator, the **decision to retain an existing trim state** is now supported. The numerical comparison that produced or validated that judgment remains unresolved and should not be fabricated.

## Next unresolved item

Continue searching the Flight Director Log and CONTROL/Flight Dynamics/RTCC working artifacts for the upstream calculation behind the judgment: candidate/reference trim, comparison delta or tolerance, T+55 deck linkage, calculation time, or job/run identity.