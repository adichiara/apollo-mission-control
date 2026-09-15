# Progress — PC+2 GDA dual-unit reconciliation

Date: 2026-09-15
Research note: `resources/research/155_pc2_gda_dual_units_and_calibration.md`

Primary NASA/Grumman LM hardware documentation resolves the unit ambiguity introduced in note 154. GDA state is legitimately represented both as linear actuator stroke (±2 in) and engine-gimbal angular position (±6°), with a generic nominal 3°/in scale. The Apollo 13 FCD LM CONTROL narrative reports its PC+2 ignition roll-GDA event in degrees (`~ -2°`, delta `-1.2°`), while the September Mission Report maneuver table explicitly reports actuator telemetry in inches.

Documentation was reconciled so the April narrative is no longer mislabeled as inches. The inferred pre-ignition roll angular state returns to approximately `-0.8°`. The September table remains linear displacement. The nominal hardware scale provides a useful consistency check (`-0.28 in` ≈ `-0.84°`) but is not treated as exact LM-7 calibration or proof of identical sample timing.

Next priority remains recovery of the final ~78-hour commanded PC+2 angular trim and its mass-properties job/`T+55` provenance.