# Progress — cross-model resource/power/observation chain

Date: 2026-09-14

## Completed

- Added an explicit generic resource-to-electrical-source coupling.
- Added caller-defined operating threshold and inclusive/exclusive semantics.
- Kept resource sufficiency separate from upstream hardware availability.
- Added an integration test composing:
  - resource inventory/depletion;
  - resource-to-source coupling;
  - electrical bus/load availability;
  - tracking observation availability.
- Verified that the same chain produces available observations before depletion and unavailable observations after depletion without a scenario outcome branch.

## Consequence

The causal engine now demonstrates an actual multi-model dependency chain rather than only isolated component proofs.

This is the pattern future sourced scenario integrations should follow:

`physical/resource cause -> equipment state -> observation state -> controller-visible consequence`

## Boundary

The test is fully synthetic. No Apollo battery, electrical, or tracking constants are asserted.


## Validation-harness integration

Facilitator-only API endpoints now expose the resource and electrical models independently and the composed resource→power→tracking chain. Contract tests exercise before/after depletion and verify that direct source-availability override is rejected in the composed endpoint.
