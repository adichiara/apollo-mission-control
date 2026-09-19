# Progress — Apollo 11 landing-radar velocity estimator/update

Date: 2026-09-19

## Completed

The Apollo-11-effective landing-radar velocity proof is executable from source-controlled geometry inputs through measurement-time propagation, beam projection, residual qualification, and weighted correction.

A fresh primary-source check of the LM-5 Mission G prelaunch erasable load confirms the exact geometry constants and source units: `LRALPHA1=0.0163371759 rev`, `LRBETA1=0.0665287037 rev` (stow), `LRALPHA2=0.0161680555 rev`, and `LRBETA2=0.0001361111 rev` (hover), addresses 2522–2525. The same table identifies itself as the G PRELAUNCH ERASABLE LOAD (LUMINARY 99) and NASA data source.

## Implementation

- `landing_radar_transform.py` supplies the verified equation-level SETPOS and SM/NB transforms.
- `landing_radar_velocity_chain.py` accepts explicit geometry or an explicit synthetic/unit-test beam.
- `apollo11_lm5_landing_radar_partial.json` now stores both LM-5 angle pairs in source units with mission/configuration provenance.
- `landing_radar_profiles.py` exposes a position-selecting adapter that converts revolutions to radians and combines the selected historical angles with caller-supplied measurement-time CDUs.
- Tests verify all four pad-load values, conversion, CDU preservation, invalid-position rejection, and updated unresolved boundaries.

The profile's stale unresolved entries for the already implemented antenna/CDU transform and PIPA/gravity propagation were removed.

## Boundaries

No continuous antenna motion is inferred. Measurement-time CDUs remain dynamic inputs; no attitude history is invented. Radar measurements and historical noise remain caller supplied, with historical stochastic generation **BLOCKED** on flight-effective numerical error evidence. Controller-visible product cadence/formatting remains separately unresolved. Bit-for-bit AGC fixed-point equivalence is not claimed.
