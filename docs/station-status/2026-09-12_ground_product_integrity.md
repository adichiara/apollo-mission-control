# Station research-status addendum — ground-product integrity

Date: 2026-09-12

## GUIDO / CONTROL / FLIGHT data-path implication

The documented post-MCC-5 Apollo 13 AGS/RTCC attitude event adds a new common data-quality requirement across controller stations:

- source spacecraft/onboard information may be satisfactory;
- ground processing may generate an incorrect controller-facing product;
- that bad product may still be present and not automatically flagged invalid;
- controllers may need an independent cue to reject it.

### GUIDO

**Maturity remains B.**

Improved:

- ground-derived guidance/attitude products can no longer be treated as automatically correct when source telemetry is valid;
- independent onboard/reference cues must remain separable from RTCC-derived products.

Still unresolved:

- exact Apollo 13 RTCC body-angle conversion responsible for the post-MCC-5 error;
- exact controller CRT/product involved;
- exact erroneous numerical values.

### CONTROL

**Maturity remains B.**

Improved:

- CONTROL-relevant ground calculations and displayed products inherit the same integrity rule: a computed product can be wrong without implying the physical system is wrong.

Still unresolved:

- exact mapping of the post-MCC-5 bad AGS body-angle product to CONTROL versus GUIDO display usage;
- precise console presentation.

### FLIGHT

**Maturity remains B.**

Improved:

- FLIGHT must integrate discipline assessments and conflicting cues rather than receive a hidden authoritative data-quality verdict.

## Implementation consequence

The simulator now distinguishes:

- product availability/declared validity;
- internal product integrity;
- controller detection/rejection.

Internal integrity must not become an in-play diagnostic label unless historical evidence shows such a flag existed.
