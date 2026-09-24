# Progress — Apollo 11 descent controller-product boundary

Date: 2026-09-24

## Implemented

Added a mission-specific Apollo 11 descent controller-product schema based on the
source-backed MSK-1137 field family and the documented CONTROL landing-radar position
call.

The schema covers the currently needed descent/program-alarm subset:

- LR range/velocity GOOD/BAD;
- LR body-axis VXB/VYB/VZB;
- LR slant range;
- PGNS altitude;
- TGO and descent time-to-end-of-phase;
- LGC/ISS warnings and PGNCS/program cautions;
- first/second/latest alarm code;
- restart count;
- active program;
- DSKY verb/noun/flasher;
- CONTROL LR antenna-position report.

## Evidence boundary

The projector accepts only explicitly supplied controller-visible values.

It does not read hidden spacecraft/AGC state and does not derive missing products.
Known but unsupplied products remain unavailable.

Routing status is explicit:

- LR fields with a documented Apollo-11 LGC downlink family remain
  `downlink_family_route_unresolved` until Mission-G ground conversion/display routing
  is recovered;
- fields whose current source evidence does not permit choosing D/L versus RTCC/ground
  processing remain `mixed_downlink_rtcc_unresolved`;
- field-semantics-only products retain that status rather than acquiring an invented
  processor route;
- CONTROL's LR-position call remains a controller-reported state distinct from LR
  validity/acceptance.

## Site-facing proof

Added:

- `/api/admin/model-proof/apollo11-descent-products`;
- Causal Model Lab section **Apollo 11 descent controller-product boundary**;
- normal and sparse-input proofs showing unavailable fields remain withheld;
- unit, API, and browser-contract tests.

## Preserved separations

This work does not:

- compute a ground Delta-H rule;
- infer a landing GO/NO-GO;
- assign exact station ownership from display availability;
- choose an unresolved D/L/RTCC route;
- assign DRK/FDK mappings;
- infer display cadence/latency;
- bypass the separate FLIGHT/CAPCOM decision chain.

## Next

The Apollo 11 product boundary is now sufficient for current architecture work. Exact
Mission-G routing remains source-gated. The next independent implementation pressure
point is powered-descent trajectory/propulsion plus sourced decision-rule inputs needed
before an Apollo 11 runtime is allowed.
