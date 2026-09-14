# Progress — multi-source guidance consensus

Date: 2026-09-14

## Completed

- Added mission-neutral multi-source guidance consensus analysis.
- Added caller-defined fields, redlines/tolerances, freshness, and quorum.
- Added all-pairs consensus groups so non-transitive pairwise agreement is not misclassified as full consensus.
- Added explicit consensus, ambiguous, no-consensus, and indeterminate states.
- Sources outside a unique consensus are reported without being classified as failed.
- Added synthetic tests.
- Added research note 146 from MSC Internal Note 70-FM-80.
- Added an explicit Apollo 11 `guidance_monitoring` readiness domain and scenario requirement.

## Apollo 11 evidence

Powered-descent flight controllers compared PGNCS, AGS, and MSFN-derived velocity with two-out-of-three logic. Premission redlines were defined for residuals. A documented 18 ft/s PGNCS/MSFN radial residual at PDI remained below a 35 ft/s limit and was attributed to initialization/downrange-position error rather than guidance degradation.

## Boundary

The 35 ft/s value is not treated as a universal redline. Historical runtime use still requires exact phase/source-pair redlines, component definitions, cadence/freshness, MSFN powered-flight processing, and controller presentation.