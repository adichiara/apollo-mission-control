# Progress — Apollo 11 landing-radar velocity estimator/update

Date: 2026-09-19

## Completed

The Apollo-11-effective landing-radar velocity proof is now executable from explicit source-controlled geometry inputs through measurement-time propagation, beam projection, residual qualification, and weighted correction.

A fresh primary-source check of flown LUMINARY 099 confirms the position transition semantics: `SETPOS1` selects the first `LRALPHA/LRBETA` pair; `SETPOS2` selects the second; after the antenna physically reaches position 2, `HIGATJOB` calls `SETPOS2` and only then clears the no-read flag. `SETPOS` transforms antenna UNITY/UNITX into NB and forms the third velocity beam by cross product. `RDGIMS` separately saves measurement-time CDUs used by the downstream NB→SM transformation. This supports composition without inventing a continuous antenna slew model.

## Implementation

- `landing_radar_transform.py` supplies the verified equation-level SETPOS and SM/NB transforms.
- `landing_radar_velocity_chain.py` now accepts either an explicit beam or `LandingRadarBeamGeometryInput` containing alpha, beta, and measurement-time CDU angles.
- Historical-geometry mode constructs the selected X/Y/Z velocity beam in NB, transforms it NB→SM at the measurement attitude, and passes that beam through the existing propagation/projection/qualification/update chain.
- Tests preserve the explicit-beam path, exercise geometry composition, and enforce exactly one beam source.

The implementation deliberately keeps the LM-5 pad-load values external rather than copying numbers by hand into code. The next small implementation step is a provenance-bearing profile adapter for the already recovered position-1/position-2 load values.

## Boundaries

No continuous antenna motion is inferred: the flown code supports discrete position-1/position-2 beam recomputation. Radar measurements and historical noise remain caller supplied; historical stochastic generation remains **BLOCKED** on flight-effective numerical error evidence. Controller-visible product cadence/formatting remains separately unresolved. Bit-for-bit AGC fixed-point equivalence is not claimed.
