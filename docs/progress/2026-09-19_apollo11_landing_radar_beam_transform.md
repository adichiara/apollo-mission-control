# Progress — Apollo 11 landing-radar beam transform

Date: 2026-09-19
Research: 405

## Completed

Recovered a primary-source chain sufficient to close the **static antenna-position** portion of the Apollo 11 landing-radar beam geometry.

LUMINARY 099 directly shows `SETPOS` transforming antenna-frame basis vectors into navigation-base beam vectors. LUMINARY Memo #95 controls the sign/order convention, and the LM-5 Mission G LUMINARY 99 prelaunch load supplies the actual position-1 and position-2 alpha/beta values. The final-program controlled constants also supply `HBEAMANT` rather than requiring a guessed range-beam vector.

The high-gate path explicitly recomputes beam vectors when the landing-radar antenna reaches position 2.

## Boundary retained

This does not yet close the full historical velocity-reference chain. `RDGIMS` captures IMU CDU attitude data near the midpoint of the five-sample velocity read, but research 405 does not yet claim the complete downstream navigation-base/reference-frame transformation or estimator/filter behavior.

No station-visible display cadence, controller-product timing, or executable scenario behavior changes in this step.

## Next

Trace `RDGIMS` → `VELUPDAT` attitude/time-tag transformation in LUMINARY 099. If fully controlled, use it to replace the historical profile's remaining externally supplied beam-vector boundary while retaining the generic lower-level proof API.

## Evidence status

- **DOCUMENTED:** static LM-5 antenna-position beam transform inputs and algorithm.
- **PARTIALLY DOCUMENTED:** dynamic attitude/reference-frame leg.
- **UNRESOLVED:** estimator/filter and station-visible timing.
