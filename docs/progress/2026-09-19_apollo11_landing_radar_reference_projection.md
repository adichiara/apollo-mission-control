# Progress — Apollo 11 landing-radar velocity-reference projection

Date: 2026-09-19

## Scope

Advance the Apollo 11 landing-radar path without guessing the unresolved LM-5 antenna/attitude transform.

## Source-backed boundary

The flown Luminary 099 `SERVICER.agc` velocity-update path:

1. advances the estimated LM velocity to the radar measurement time;
2. subtracts the lunar-rotation correction `DELVS`;
3. selects the current landing-radar velocity-beam vector;
4. computes the estimated velocity component with a dot product;
5. forms the measured-minus-estimated residual and applies the existing affine reasonableness limit.

Later R-567 guidance documentation independently describes the selected velocity-component unit vector and the vehicle/platform transformation used to express the antenna axis at measurement time. The later revision is used only as a descriptive cross-check; the Apollo 11 implementation boundary is anchored by the flown Luminary 099 source.

## Implemented

- added `landing_radar_reference.py`;
- explicit inputs:
  - estimated vehicle velocity;
  - lunar-surface velocity;
  - selected radar-beam unit vector;
- explicit output:
  - velocity relative to the lunar surface;
  - signed selected-beam reference velocity;
- rejects non-unit beam vectors rather than silently normalizing them;
- keeps the antenna/vehicle/platform transform upstream;
- added facilitator API:
  - `/api/admin/model-proof/landing-radar-velocity-reference`;
- integrated the reference stage into the Causal Model Lab before the existing quality/update chain;
- added unit, API, model-lab contract, and cross-module reference→reasonableness tests;
- narrowed the Apollo 11 landing-radar profile and roadmap wording accordingly.

## Deliberate boundary

This does **not** yet implement:

- LM-5 antenna Position 1/2 geometry;
- conversion of antenna axes through Navigation Base / Stable Member / platform attitude;
- terrain/slant-range intersection;
- radar noise/bias generation;
- recursive estimator/filter weighting;
- state-vector correction;
- historical controller-product cadence.

The next radar question is therefore no longer "what scalar reference does the residual use?" It is the exact LM-5 transform that supplies the selected beam unit vector at measurement time.

## Primary/source references

- Virtual AGC, flown Apollo 11 `Luminary099/SERVICER.agc`, velocity update and `DELVS`/selected-beam projection path.
- MIT/IL R-567 Section 5 powered-flight navigation/guidance, State-Vector Update and LR Data Read descriptions, used as a later descriptive cross-check.
- Existing research note 205 and Apollo 11 landing-radar partial profile for the residual-rule boundary.
