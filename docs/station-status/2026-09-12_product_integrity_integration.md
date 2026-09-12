# Station research-status addendum — controller product rejection

Date: 2026-09-12

## GUIDO

**Maturity remains B.**

Improved:

- ground-derived product integrity is now separable from visible product validity;
- GUIDO can explicitly question/reject a ground product based on an independent cue rather than receiving hidden simulator truth.

Still unresolved:

- exact post-MCC-5 RTCC body-angle CRT field;
- deciding controller identity and exact call sequence;
- erroneous numeric angles.

## CONTROL

**Maturity remains B.**

Improved:

- common station projection supports the same hidden-integrity semantics for CONTROL ground-derived products;
- future CONTROL decisions can reject suspect derived products without mutating spacecraft state.

## FLIGHT

**Maturity remains B.**

Improved:

- controller interpretations can now be represented as explicit events suitable for later FLIGHT integration;
- FLIGHT need not receive an omniscient product-quality verdict.

## Research consequence

No further research into the post-MCC-5 display details is required for the current architecture. The remaining uncertainty is low-value for the PC+2 vertical slice and should remain bounded unless a later scenario requires it.
