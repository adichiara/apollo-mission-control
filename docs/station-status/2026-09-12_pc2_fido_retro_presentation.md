# Station research-status addendum — PC+2 FIDO/RETRO presentation

Date: 2026-09-12

## FIDO

**Maturity remains B.**

Improved:

- first-pass player-facing maneuver-target / ground-solution presentation now exists;
- final PC+2 PAD values are tied to the contemporaneous 77:52 GET read-up;
- ground-solution status remains distinct from hidden product integrity;
- deferred Cartesian/post-burn trajectory products are not misrepresented as telemetry failures.

Still unresolved:

- exact Apollo 13 FIDO CRT/display IDs and layout for PC+2;
- exact RTCC state-vector representation required by a future propagator;
- executable post-burn propagated trajectory/landing assessment.

## RETRO

**Maturity remains B.**

Improved:

- final PC+2 return-plan values from the 78:00:58 monitor PAD are represented as a distinct player-facing return product;
- landing coordinates, entry-interface range/velocity, and predicted 0.05-g GET remain separate from the maneuver target itself;
- the presentation reflects RETRO's return-plan role without collapsing it into a binary safe-return flag.

Still unresolved:

- exact Apollo 13 RETRO CRT/display IDs/layout;
- detailed recovery/weather presentation beyond the bounded PC+2 target product;
- post-burn return-plan recomputation until trajectory propagation is implemented.

## Research stop condition

The first-pass FIDO/RETRO presentation is sufficient for initial play. Further RTCC/display reconstruction should be driven by an actual gameplay dependency.

## Next station presentation

INCO: weak-link quality, telemetry/voice availability, uplink state, and ranging state during final PC+2 preparation.
