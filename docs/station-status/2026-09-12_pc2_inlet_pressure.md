# Station Status Addendum — PC+2 DPS inlet pressure

Date: 2026-09-12

## CONTROL

Maturity remains **B**.

Research note `057_pc2_dps_inlet_pressure_observation_path.md` establishes two Apollo 13/LM-7-family source measurements:

- `GQ3611P` — engine interface fuel pressure;
- `GQ4111P` — engine interface oxidizer pressure.

This is a meaningful provenance advance for the documented PC+2 inlet-pressure shutdown criterion.

However, the rule itself is stated in the primary sources as singular **engine inlet pressure ≤150 psi on the ground**, while the vehicle exposes two interface-pressure measurements. The reviewed evidence does not yet establish whether the ground criterion used either leg, the minimum of the pair, a selected value, or another processed quantity.

Therefore:

- CONTROL remains maturity B;
- the 150-psi rule remains `NOT_EVALUABLE` in the executable model;
- a combined `dps_inlet_pressure_psi` product must not be invented;
- future runtime state may carry fuel and oxidizer interface pressures separately once needed.

Main unresolved evidence target: exact CONTROL display/limit logic or procedure defining the ground inlet-pressure selection/aggregation semantics.
