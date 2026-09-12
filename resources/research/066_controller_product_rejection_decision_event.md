# Apollo 13 controller rejection as an explicit decision event

Date: 2026-09-12  
Status: **IMPLEMENTED — architecture refinement based on the documented post-MCC-5 AGS/RTCC case**

## Question

Where should controller suspicion and rejection of a bad ground-derived product live in the simulation model?

## Evidence basis

Research note `065_apollo13_ground_product_integrity_failure.md` established a mission-specific Apollo 13 case in which the RTCC incorrectly processed AGS body angles after MCC-5. Mission Control did not receive an omniscient simulator diagnosis; the improper ground result was recognized through comparison with an independent FDAI reference and was then disregarded.

That sequence implies three distinct layers:

1. controller-visible product;
2. hidden simulation truth about product integrity;
3. controller interpretation/decision.

## Implementation decision

Controller suspicion/rejection is represented as an explicit **decision/audit event**, not as a mutation of the displayed product and not as an automatic consequence of `integrity=incorrect`.

The station projection layer may carry hidden integrity annotations for scenario/audit purposes. These annotations are not part of the ordinary `products` mapping and therefore are not player-facing by default.

The decision layer records events such as:

- question product;
- reject product;
- accept alternate reference.

The first implemented helper records rejection with:

- GET;
- station;
- product identifier;
- controller-stated basis;
- optional independent/alternate reference.

## Why this matters

A bad product can remain:

- present;
- current;
- formatted normally;
- declared valid;

while still being internally incorrect.

Likewise, a controller can reject a product for a stated reason without the simulator asserting that the controller's diagnosis is correct. This leaves room for future scenarios in which controllers distrust a good product or fail to detect a bad one.

## Historical boundary

The post-MCC-5 AGS/RTCC processing error remains an architecture-validation case and is not inserted into the PC+2 nominal chronology.

No exact historical erroneous angles, detection timestamp, deciding controller identity, or CRT field is invented.

## Code

- `src/apollo_mission_control/controller_products.py`
  - `ProjectionSet.integrity_annotations`
  - `ProjectionSet.annotate_integrity(...)`
- `src/apollo_mission_control/controller_decisions.py`
  - explicit controller decision/audit events
- `tests/test_integrity_projection_integration.py`

## Next boundary

The generic integrity path is now sufficient. Return to the PC+2 vertical slice and identify the next high-value nonnominal/controller-decision path supported by primary evidence. Prefer a failure that exercises an already-modeled product path rather than reopening low-value display archaeology.
