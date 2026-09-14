# Generic Resource Inventory / Depletion Model Proof

Status: **implemented reusable finite-inventory model; not historically validated**

## Purpose

Represent finite mission resources whose quantities evolve with configuration and time:

`initial inventory + piecewise flow history -> remaining quantity + depletion/overflow evidence`

Implementation:

`src/apollo_mission_control/resource_inventory_model.py`

Potential uses include:

- battery energy;
- propellant inventories;
- oxygen;
- water;
- cooling consumables;
- other scenario-relevant finite resources.

The model is unit-agnostic. Each resource declares its own unit and all supplied quantities/rates for that resource must use it consistently.

## Sign convention

For each segment:

- positive rate consumes/depletes;
- negative rate replenishes/increases.

The model integrates piecewise-constant rates exactly.

## Boundaries

Each resource may define:

- minimum quantity;
- optional maximum quantity.

If consumption would cross the minimum, the quantity is clamped and the unmet consumption is recorded.

If replenishment would exceed a finite maximum, the quantity is clamped and overflow is recorded.

The result also records the exact time within a segment when a configured boundary is first reached.

## Deliberate exclusions

The generic inventory model does not simulate:

- battery voltage/current chemistry;
- pressure/temperature;
- tank geometry;
- fluid dynamics;
- transfer efficiency;
- boiloff/leakage unless represented as an explicit flow;
- automatic load shedding;
- automatic subsystem shutdown at depletion.

Those consequences belong in connected subsystem models. For example, a battery-energy inventory may feed source availability in the electrical model, but the inventory model does not silently turn a bus off.

## Historical-use gate

A scenario must source:

- initial quantity and epoch;
- resource units/convention;
- applicable consumption/replenishment rates or equations;
- configuration dependencies;
- reserve/depletion semantics;
- validation targets/tolerances.

No Apollo resource quantities or rates are embedded in the generic code.
