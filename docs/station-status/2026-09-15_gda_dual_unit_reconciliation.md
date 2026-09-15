# Station research status — PC+2 GDA dual-unit reconciliation

Date: 2026-09-15

## CONTROL

**Evidence strengthened/corrected.** Primary LM hardware documentation shows that GDA state has both linear actuator-stroke and angular engine-gimbal representations. Apollo 13 LM CONTROL's PC+2 ignition narrative is angular: roll GDA approximately `-2°`, delta `-1.2°`, implying approximately `-0.8°` pre-ignition. The September Mission Report table is separately linear, in inches.

Do not treat the generic ±2 in ↔ ±6° relationship as exact LM-7 calibration or infer the missing final commanded pitch/roll trim.

## FIDO / Flight Dynamics

No new PC+2 mass-properties job identity was recovered. Existing boundary remains: the ~59-hour interim trim was challenged because CONTROL used premission mass properties, later reconciled with Flight Dynamics; the final pad used GYM 289. `T+55` linkage to the final trim remains unproven.

## FLIGHT

Product-finality model remains important: interim trim, final targeting/pad product, observed angular engine/GDA state, and telemetry displacement are distinct products. Units and provenance must be explicit before values are compared.

## Simulation status

Safe generic hardware relationship: ±2 in GDA stroke ↔ ±6° engine-gimbal position (nominal 3°/in). Historical replay should preserve source-native units. Exact LM-7 calibration and final PC+2 commanded trim remain unresolved.