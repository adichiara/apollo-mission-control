# Progress — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## Completed

Audited the generic DPS and translational model inputs against primary Apollo documentation.

Key result: the reusable model interfaces do not need new hidden physics constants. NASA TN D-7143 maps cleanly onto existing thrust, effective-Isp, direction/gimbal, and depletion semantics, but its 10,500-lbf maximum-rated thrust, 10:1 throttling ratio, ±6-degree gimbal capability, and 305-second end-of-duty-cycle Isp are design-envelope evidence rather than an LM-5 delivered-flight profile.

The Apollo 11 press kit provides LM-5 launch mass/resource bookkeeping, including 18,100 lb DPS propellant and 33,205 lb total launch weight, but this is not the powered-descent-initiation mass. The Mission Report's 756.3-second powered-descent duration is a useful checkpoint but cannot define a continuous throttle history.

## Boundary preserved

No launch mass was substituted for PDI mass. No design thrust or Isp was promoted to an Apollo 11 as-flown value. No D-022 irrelevance closure was claimed without sourced endpoints and a player-product comparison.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- companion station-status and source-catalog addenda

## Next

Search specifically for LM-5/Apollo-11 PDI mass/state bookkeeping and DPS final-flight/performance evaluation. If those do not close the profile, formalize the scenario input provenance boundary between DOCUMENTED checkpoints and RECONSTRUCTED continuous inputs.

## Evidence status

**PARTIALLY DOCUMENTED.** Generic model parameterization is compatible with primary-source DPS physics; mission-specific continuous inputs remain incomplete.