# Progress — RTACF weight/CG-to-trim product boundary

Date: 2026-09-14
Research note: `resources/research/149_rtacf_weight_cg_trim_product_boundary.md`

## Work completed

- Continued from research note 148's unresolved operational mass-accounting lineage.
- Reviewed primary Apollo mission-operations material from the NASA MSC Mission Planning and Analysis Division's Apollo 11 Mission Support Section.
- Established that Apollo operational mass-properties computations produced **weight-c.g. tables used by RTACF and RTCC trajectory processors to compute pitch and yaw trim angles**.
- Established separately that RTACF constants updates included mass-properties tables and thrust parameters.
- Added research note 149 and reconciled the PC+2 numerical roadmap, FIDO/CONTROL/FLIGHT station-status addendum, and RTCC mass-properties source catalog.

## Result

The historical model can now represent a sourced computational lineage from mass-properties weight/CG products to trajectory-processor trim outputs. This strengthens the interpretation of the Apollo 13 ~59-hour stale-premission-mass-properties trim dispute while preserving the mission-specific uncertainty: no source yet identifies the accepted trim's exact H-2 deck or maps `T+55` to the final P30 module weights.

## Next

Recover H-2 RTCC/RTACF weight/CG tables, processor documentation, maneuver worksheets, or support records tying `T+55` to the accepted PC+2 trim and/or `62,480 / 33,452 lb` P30 weights.