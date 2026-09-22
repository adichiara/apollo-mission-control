# Progress — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## Completed

Audited the generic DPS and translational model inputs against primary Apollo documentation.

Key result: the reusable model interfaces do not need new hidden physics constants. NASA TN D-7143 maps cleanly onto existing thrust, effective-Isp, direction/gimbal, and depletion semantics, but its 10,500-lbf maximum-rated thrust, 10:1 throttling ratio, ±6-degree gimbal capability, and 305-second end-of-duty-cycle Isp are design-envelope evidence rather than an LM-5 delivered-flight profile.

The Apollo 11 press kit provides LM-5 launch mass/resource bookkeeping, including 18,100 lb DPS propellant and 33,205 lb total launch weight, but this is not the powered-descent-initiation mass. The Mission Report's 756.3-second powered-descent duration is a useful checkpoint but cannot define a continuous throttle history.

A targeted follow-on recovered TRW Note 70-FMT-819 / NASA CR-108349, *Apollo Mission 11, Trajectory Reconstruction and Postflight Analysis, Volume 1*. Its descent section documents a postflight best-estimate trajectory derived first from low-speed MSFN data and landing-site constraint, then a subsequent reconstruction combining onboard and high-speed MSFN data with pre-PDI relative tracking. The report states that this combination produced a consistent continuous LM trajectory from DOI to touchdown.

This materially improves the validation path: a mission-specific continuous reference trajectory exists. It remains **RECONSTRUCTED**, because the source explicitly describes fitting, data combination, and constraint rather than a raw continuous truth record.

## Boundary preserved

No launch mass was substituted for PDI mass. No design thrust or Isp was promoted to an Apollo 11 as-flown value. No postflight reconstructed state was relabeled as raw telemetry or exact physical truth. No D-022 irrelevance closure was claimed without sourced endpoints and a player-product comparison.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

Extract the 70-FMT-819 DOI→touchdown reconstruction products and their coordinate/frame/epoch definitions for model validation. Continue the narrower LM-5 PDI mass and DPS delivered-performance search. If those remain unrecovered, formalize scenario inputs as DOCUMENTED checkpoints + RECONSTRUCTED trajectory reference + MODELLED propulsion/mass inputs.

## Evidence status

**PARTIALLY DOCUMENTED.** Generic model parameterization is compatible with primary-source DPS physics and a mission-specific continuous postflight trajectory reconstruction is now identified. PDI mass and delivered DPS thrust/Isp history remain unresolved.