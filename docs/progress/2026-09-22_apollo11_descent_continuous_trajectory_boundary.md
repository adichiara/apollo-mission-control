# Progress — Apollo 11 continuous powered-descent trajectory boundary

Date: 2026-09-22

## Completed

Resumed from the P66 decision-authority implementation and moved to the next unresolved powered-descent model dependency: continuous trajectory/propulsion reconstruction.

Primary-source-first review established a conservative boundary rather than inventing a flown trajectory:

- NASA TM X-58038 supports independent ground tracking/guidance comparison through lunar descent.
- NASA TN D-7143 supports the LM DPS causal architecture: throttleable, gimbaled, pressure-fed propulsion coupled to guidance/navigation.
- NASA lunar-descent guidance documentation supports distinct P63/P64/P65/P66 control semantics and computer control of descent/throttle behavior.
- NASA TM-20220007267 is retained only as a later reconstruction/boundary source; its explicit need for digitization and estimation demonstrates why a fitted final-descent path must not be represented as direct historical truth.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_continuous_trajectory_boundary.md`
- `docs/progress/2026-09-22_apollo11_descent_continuous_trajectory_boundary.md`
- `docs/station-status/2026-09-22_apollo11_descent_continuous_trajectory_boundary.md`
- `resources/APOLLO11_DESCENT_CONTINUOUS_TRAJECTORY_SOURCE_CATALOG_ADDENDUM.md`

## Boundary preserved

No continuous Apollo 11 state vector, throttle schedule, attitude history, or landing-path interpolation has been invented. Modern reconstruction is not promoted to primary-source evidence.

## Next

Audit the existing generic DPS/translational model inputs against Apollo source-backed values/ranges. Promote only parameters whose semantics and applicability are established; use D-022 only where both range endpoints are sourced and controller-visible irrelevance can be demonstrated.

## Evidence status

**PARTIALLY DOCUMENTED.** The causal architecture is sufficiently sourced for continued model work; the exact continuous Apollo 11 as-flown trajectory remains unresolved.
