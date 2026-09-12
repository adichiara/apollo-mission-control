# Progress — Apollo 13 ground-product integrity path

Date: 2026-09-12

## Completed

- Researched the documented post-MCC-5 Apollo 13 case in which RTCC incorrectly processed AGS body angles.
- Confirmed that Mission Control rejected the improper ground readout and accepted the independent FDAI reference showing PTC was correctly established.
- Added `resources/research/065_apollo13_ground_product_integrity_failure.md`.
- Added `resources/source-catalog/APOLLO13_GROUND_PRODUCT_INTEGRITY_SOURCES.md`.
- Added `src/apollo_mission_control/product_integrity.py`.
- Added `tests/test_product_integrity.py`.
- Separated controller-facing product validity/availability semantics from hidden simulator product integrity.
- Added support for a **wrong-but-present** ground-derived product that retains its existing validity field while carrying internal `INCORRECT` integrity metadata.
- Added explicit controller-detection state so a bad product is not automatically diagnosed by the simulator.
- Preserved an independent-reference path as a separate correct product.

## Historical boundary

The post-MCC-5 RTCC/AGS problem did not occur during PC+2. It is used to validate the common Mission Control data-path architecture, not inserted into the first vertical-slice nominal history.

No historical erroneous body-angle values, exact RTCC defect, or automatic controller-visible invalid flag were invented.

## Test status

A fresh test-suite execution was attempted by cloning the repository into the container, but the runtime could not resolve `github.com`. The new tests are committed but are **not recorded as executed/passing** in this environment.

## Next work

1. Integrate internal integrity annotations with station projection/audit structures without exposing integrity as an unsolicited player hint.
2. Add an architecture validation case showing correct source state + incorrect ground product + correct independent cue + controller rejection.
3. Decide whether controller suspicion/rejection belongs in the common decision/audit event layer rather than product state itself.
4. Return to PC+2-specific failures only after this generic data-path behavior is stable.
