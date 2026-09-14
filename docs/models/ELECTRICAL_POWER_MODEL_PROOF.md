# Generic Electrical Power / Equipment-Availability Model Proof

Status: **implemented coarse causal model; not historically validated**

## Purpose

Provide a reusable decision-relevant electrical layer:

`source availability + bus state + commanded loads -> powered equipment availability`

Implementation:

`src/apollo_mission_control/electrical_power_model.py`

The model is deliberately coarse. It is intended to support controller decisions where an equipment item is available/unavailable because of power configuration, without pretending to reproduce battery chemistry or wiring-level electrical behavior.

## Inputs

A bus configuration defines:

- one or more power sources with caller-supplied maximum power capacity;
- equipment loads with caller-supplied power demand;
- explicit integer priority for load shedding;
- applicability/provenance.

Runtime state supplies:

- source available/unavailable;
- bus enabled/disabled;
- load commanded on/off.

## Outputs

The model returns:

- available source set/capacity;
- commanded demand;
- supplied demand;
- overload amount;
- per-load supplied/not-supplied state;
- explicit reason for each load result.

## Load-shedding convention

Lower integer priority is served first.

Loads with equal priority are treated as an all-or-none group. If there is not enough remaining capacity for the entire group, none of that equal-priority group is marked supplied.

This is a project numerical convention, not an Apollo electrical-system claim. Historical use must source the actual switching/load-shedding behavior or configure priorities only where that abstraction is justified.

## Deliberate exclusions

- battery chemistry / voltage sag;
- amp-hour integration;
- bus-voltage dynamics;
- wiring resistance;
- breaker/fuse physics;
- relay/contact timing;
- inverter/converter transient physics;
- automatic protective logic unless explicitly modeled upstream;
- Apollo-specific bus topology or capacities.

In this first proof, an inverter/converter may be represented to a downstream bus as a caller-supplied source whose availability is determined upstream. A later reusable converter model can replace that abstraction without changing the bus/load contract.

## Scenario use

This layer is useful wherever a controller-visible product or equipment function depends on electrical availability.

For Apollo 13 PC+2, it can eventually replace boolean equipment-availability branches with a sourced LM electrical configuration.

For Apollo 11 powered descent, the same model can support guidance/radar/communications equipment availability if a selected failure scenario requires those power dependencies.

No mission constants are embedded in the generic code.
