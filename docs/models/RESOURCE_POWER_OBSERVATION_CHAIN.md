# Cross-Model Resource → Power → Observation Proof

Status: **implemented synthetic causal composition test; not historical validation**

## Purpose

Demonstrate that independently reusable models compose into a causal chain without a scenario script choosing the result.

Implemented chain:

`finite resource inventory -> electrical source availability -> bus/load supply -> tracking observation availability`

## New coupling

`src/apollo_mission_control/resource_power_coupling.py`

A `ResourceElectricalSourceRule` maps one finite resource quantity to one electrical source availability state using:

- caller-supplied resource ID;
- caller-supplied electrical source ID;
- caller-supplied minimum operating quantity;
- explicit inclusive/exclusive threshold semantics;
- optional upstream hardware availability;
- provenance.

The coupling does not mutate either model and does not contain battery chemistry or mission constants.

## Synthetic consequence test

The integration test begins with a finite battery-like inventory and a constant load rate.

Before depletion:

- resource remains above the configured source threshold;
- electrical source is available;
- tracking receiver load is supplied;
- tracking observation values are available.

After depletion:

- resource reaches its minimum;
- source availability becomes false;
- receiver load loses power;
- tracking observation becomes unavailable and withholds range/range-rate values.

There is no branch such as:

`if battery depleted: tracking failed`

Instead each downstream result is derived from the preceding model state.

## Independent causes remain separable

The coupling also keeps resource sufficiency distinct from upstream hardware availability. A source can be unavailable because its energy resource is insufficient, because an upstream hardware/configuration state is false, or both.

## Historical boundary

This is a synthetic architecture proof only.

Historical scenarios must source:

- resource quantity/epoch and depletion rate;
- electrical source operating threshold;
- source/bus/load topology and capacities;
- actual equipment power dependency;
- observation-channel dependency and behavior.

No Apollo values are embedded.
