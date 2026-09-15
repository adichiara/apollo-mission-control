# PC+2 numerical-validation roadmap — pad-weight epoch

Date: 2026-09-14
Research notes: `resources/research/137_pc2_pad_weight_epoch_boundary.md`, `resources/research/138_pc2_rtcc_mass_property_deck_boundary.md`, `resources/research/139_pc2_dps_performance_boundary.md`, `resources/research/140_apollo13_dps_supplement_publication_boundary.md`, `resources/research/141_apollo13_dps_supplement_contractor_provenance.md`, `resources/research/142_rtcc_mass_properties_operational_semantics.md`, `resources/research/143_apollo13_tplus_mass_property_epoch_semantics.md`, `resources/research/144_rtcc_mass_properties_depletion_table_architecture.md`, `resources/research/145_apollo13_tplus_reference_epoch_boundary.md`, `resources/research/146_pc2_mass_properties_cross_console_reconciliation.md`, `resources/research/147_pc2_mission_report_mass_properties_event_boundary.md`, `resources/research/148_pc2_postflight_mass_reconstruction_semantics.md`, `resources/research/149_rtacf_weight_cg_trim_product_boundary.md`

## Current resolved boundary

The final Apollo 13 PC+2 P30 LM maneuver PAD explicitly carried `62480 lb` CSM and `33452 lb` LM at GET 077:55:24 for TIG 079:27:38.30; their sum is `95932 lb`. The Flight Control Division report establishes an in-flight, mission-relative RTCC mass-properties lineage (`T-6`, `T+6`, `T+25`, `T+55`), with `T±N` distinct from generation/load time, and shows that stale premission mass properties caused a PC+2 trim challenge later reconciled with Flight Dynamics.

Apollo 11 Mission Planning and Analysis Division operational documentation now adds a sourced processor-level architecture: **weight-c.g. tables were used by RTACF and RTCC trajectory processors to compute pitch and yaw trim angles**, while constants-update capability included mass-properties tables and thrust parameters. This is architectural evidence, not proof of an unchanged H-2 implementation, but it supports representing the Apollo 13 trim dispute as a provenance-sensitive derived-product workflow.

The September 1970 *Apollo 13 Mission Report*, Appendix A §A.5/Table A-I, gives PC+2/transearth-injection mass as **95,424.0 lb at ignition** and **87,456.0 lb at cutoff**. Research note 148 establishes the table's explicit provenance: these are conditions determined from **postflight analyses of expendable loadings and usage during flight**, using real-time/postflight usage data plus measured/calculated spacecraft properties. The post-accident maneuver mass properties are referenced to the LM coordinate system because the LM provided dynamic control.

Thus the `95,424.0 lb` value is an official **postflight reconstructed event mass**, not a demonstrated RTCC targeting input. Its **508.0-lb difference** from the final P30 module-weight sum compares two distinct historical product classes.

## Boundary retained

Do not explain the 508-lb difference without source evidence. In particular, do not assign it to consumables, venting, module bookkeeping, epoch propagation, rounding, or a specific RTCC deck. Do not retroactively inject the postflight `95424.0 lb` reconstruction into the operational targeting workflow.

Keep distinct:

1. hidden physical vehicle mass/CG;
2. official postflight reconstructed event-indexed mass properties (`95424.0 lb` PC+2/TEI ignition; `87456.0 lb` cutoff);
3. mission-control mass-properties deck/state;
4. component/module and propellant-depletion state within that computational layer;
5. mission-relative deck epoch label versus actual generation/update timestamp;
6. provenance of the mass-properties basis used by a derived calculation;
7. weight/CG table or equivalent processor input product;
8. trajectory/trim processor invocation and pitch/yaw trim output;
9. maneuver targeting/P30 module weights (`62480` / `33452`);
10. controller-visible trim/trajectory products and cross-console reconciliation.

## Propulsion boundary

Research note 139 establishes mission-specific PC+2 burn duration, staged throttle-command behavior, terminal blowdown, and the Apollo 13 nominal full-thrust baseline. Startup buildup and terminal blowdown prevent treating the historical burn as a simple constant-thrust segment. Research notes 140–141 establish that the missing October 1970 *Descent Propulsion System Final Flight Evaluation* belongs to a TRW Systems Group / MSC reporting lineage supported by adjacent NTRS records; `MSC-02680-SUPPL-2` remains an unverified search key.

## Next unresolved numerical inputs

Priority order:

1. recover H-2 RTCC/RTACF/Flight Dynamics mass-property documentation, weight/CG listings, processor descriptions, or maneuver worksheets exposing the **operational** module/depletion accounting behind the `T+55` state and identifying the mass-properties basis used for the accepted PC+2 trim and final P30 module weights (`62480` / `33452`), including the precise `T+N` reference-epoch convention;
2. recover the October 1970 Apollo 13 Mission Report Supplement 2, *Descent Propulsion System Final Flight Evaluation*;
3. recover LM-7 engine acceptance/calibration or PC+2 high-speed propulsion data if Supplement 2 remains inaccessible;
4. extract original LMS/FMES equations/integration assumptions;
5. recover sufficient state-vector/trajectory information for postburn propagation and regression.

## Integration rule

Do not force a numerical DPS model to reproduce `861.5 ft/s` by assuming either `95932 lb` or `95424.0 lb` is the exact RTCC targeting mass. Preserve both with provenance. The mission-report value is specifically a postflight reconstruction. Model trim as a derived, provenance-bearing product where appropriate, but do not assign Apollo 11 table layouts or processor constants to H-2 without mission-specific evidence. Exact agreement becomes a validation target only after operational mass/depletion accounting, delivered-thrust/mass-flow history, and integration assumptions are source-bounded.