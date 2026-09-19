# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-19
Parent: `docs/ROADMAP.md`
Research: 405

## Completed in this step

The Apollo 11 landing-radar velocity-reference gate is narrower than the parent roadmap currently states.

Primary Apollo-11-effective evidence now controls the static antenna-position transform:

- LUMINARY 099 `SETPOS1`/`SETPOS2` select the position-specific alpha/beta pair;
- `SETPOS` constructs antenna-to-navigation-base velocity/range beam vectors;
- LUMINARY Memo #95 fixes the otherwise ambiguous sign/order convention;
- the LM-5 Mission G prelaunch erasable load supplies all four position-angle values;
- LUMINARY 099 supplies the fixed `HBEAMANT` antenna-frame range-beam constant;
- the high-gate path recomputes the beam vectors after the antenna reaches position 2.

The project therefore must not continue treating the entire LM-5 antenna-position transform as unknown or substitute arbitrary normalized beam geometry.

## Revised next work

1. Trace the **dynamic** LUMINARY 099 velocity-measurement attitude path from `RDGIMS` (`LRXCDU`, `LRYCDU`, `LRZCDU`) through the reference-frame transform used by `VELUPDAT`, preserving the midpoint/time-tag semantics.
2. If that chain closes, update the historical landing-radar profile so its navigation-base/reference beam is derived from controlled LM-5 inputs rather than supplied externally.
3. Then recover/implement the downstream estimator/filter and its historical cadence.
4. Keep controller-visible radar/guidance product cadence and formatting separate; no internal computation cadence is automatically a station display cadence.
5. Keep direct `69-FS-3` recovery preferred but dependency-triggered where the final LUMINARY 099 listing and LM-5 pad-load chain already establish the required behavior.

## Model boundary

This step changes historical readiness, not executable behavior. The existing generic beam-projection proof remains valid infrastructure. A historical Apollo 11 adapter should not be promoted until the dynamic attitude/reference-frame leg is closed and tested.

## Evidence status

- **DOCUMENTED:** static antenna-position transform structure, polarity/order, LM-5 position angles, and fixed altitude/range antenna vector.
- **PARTIALLY DOCUMENTED:** complete time-tagged velocity-beam reference-frame transform.
- **UNRESOLVED:** downstream estimator/filter cadence and controller-visible product timing/formatting.
