# Progress — Apollo 11 landing-radar velocity-component cadence

Date: 2026-09-19

## Completed

Closed one timing boundary that had remained conflated with controller-product cadence.

Primary Apollo 11 technical documentation states that powered-flight Average-G/state-vector processing occurs on 2-second PIPA intervals and that the landing radar's three velocity components are used **one during each 2-second interval**. The accompanying timeline shows the component sequence repeating `Vz → Vx → Vy → Vz`.

This gives the historical onboard estimator/input schedule needed when the end-to-end landing-radar chain is composed: one LR velocity component is consumed per 2-second navigation interval. It does **not** establish a two-second MCC display cadence, telemetry freshness guarantee, controller-product refresh rate, or radar noise-generation frequency.

## Repository consequence

- Apollo 11 source catalog now records the AC Electronics manual as primary timing evidence.
- A dated roadmap addendum narrows the timing problem to the still-unresolved ground/controller interface.
- Station status explicitly keeps onboard estimator cadence separate from GUIDO/controller-visible cadence.
- No executable behavior or station maturity changes in this research-only slice.

## Next bounded work

1. Implement the already source-controlled measurement-time propagation + beam transform + qualification + weighting composition.
2. Keep landing-radar measurement/noise generation unresolved until a source constrains it.
3. For controller-facing timing, search direct Mission G downlink/telemetry/display documentation; do not project the LGC 2-second component schedule into MCC products.

## Source

AC Electronics, *Apollo 11 Guidance and Navigation System Manual*, descent-state-vector update material:
https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf

## Evidence status

- **DOCUMENTED:** one LR velocity component is used per 2-second Average-G/PIPA navigation interval, with the illustrated sequence cycling `Vz`, `Vx`, `Vy`.
- **UNRESOLVED:** controller-visible landing-radar/guidance product cadence and formatting.
- **UNRESOLVED:** landing-radar measurement/noise generation.
