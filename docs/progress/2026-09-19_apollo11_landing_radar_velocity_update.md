# Progress — Apollo 11 landing-radar velocity estimator/update

Date: 2026-09-19

## Completed

The Apollo-11-effective landing-radar velocity proof is executable from source-controlled geometry inputs through measurement-time propagation, beam projection, residual qualification, and weighted correction.

A fresh primary-source check of the LM-5 Mission G prelaunch erasable load confirms the exact geometry constants and source units: `LRALPHA1=0.0163371759 rev`, `LRBETA1=0.0665287037 rev` (stow), `LRALPHA2=0.0161680555 rev`, and `LRBETA2=0.0001361111 rev` (hover), addresses 2522–2525. The same table identifies itself as the G PRELAUNCH ERASABLE LOAD (LUMINARY 99) and NASA data source.

The next unresolved controller-product item was then rechecked against the mission-specific AC Electronics Apollo 11 guidance/navigation summary, MSK-1137 definitions. The source directly fixes a useful subset of the controller-visible LR contract:

- `LR RNG`: landing-radar range-data status, GOOD/BAD;
- `VEL`: landing-radar velocity-data status, GOOD/BAD;
- `VXB, VYB, VZB`: landing-radar velocity in **body-axis coordinates**, displayed as `±XXXX FT/SEC`;
- `RNG`: landing-radar slant range altitude, displayed as `XXXXX FT`;
- `ALT`: PGNS-computed altitude, displayed as `XXXXX FT`;
- `ACT ΔV`: explicitly identified separately as actual delta-V gained, **ground computed**.

This is consistent with the direct Apollo 11/Apollo 13 MSK-1137 comparison already recorded in research note 030: the same display number does not imply the same field semantics across missions. Apollo 13 changes the LR velocity family to stable-member coordinates and changes several altitude/comparison products. No Apollo 13 transform or residual semantics should therefore be back-projected into Apollo 11.

## Implementation

- `landing_radar_transform.py` supplies the verified equation-level SETPOS and SM/NB transforms.
- `landing_radar_velocity_chain.py` accepts explicit geometry or an explicit synthetic/unit-test beam.
- `apollo11_lm5_landing_radar_partial.json` stores both LM-5 angle pairs in source units with mission/configuration provenance.
- `landing_radar_profiles.py` exposes a position-selecting adapter that converts revolutions to radians and combines the selected historical angles with caller-supplied measurement-time CDUs.
- Tests verify all four pad-load values, conversion, CDU preservation, invalid-position rejection, and updated unresolved boundaries.

No controller renderer was changed in this pass: the source establishes field meaning/format, but exact Apollo 11 downlink-to-ground routing and CRT refresh behavior remain unresolved.

## Boundaries

No continuous antenna motion is inferred. Measurement-time CDUs remain dynamic inputs; no attitude history is invented. Radar measurements and historical noise remain caller supplied, with historical stochastic generation **BLOCKED** on flight-effective numerical error evidence. Apollo 11 controller-visible LR formatting is now partially source-controlled at the MSK-1137 field-definition level; display cadence, latency, freshness, request workflow, and unresolved routing remain separate. Bit-for-bit AGC fixed-point equivalence is not claimed.
