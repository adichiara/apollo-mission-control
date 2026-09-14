# PC+2 numerical-validation roadmap — pad-weight epoch

Date: 2026-09-14
Research notes: `resources/research/137_pc2_pad_weight_epoch_boundary.md`, `resources/research/138_pc2_rtcc_mass_property_deck_boundary.md`, `resources/research/139_pc2_dps_performance_boundary.md`, `resources/research/140_apollo13_dps_supplement_publication_boundary.md`, `resources/research/141_apollo13_dps_supplement_contractor_provenance.md`, `resources/research/142_rtcc_mass_properties_operational_semantics.md`, `resources/research/143_apollo13_tplus_mass_property_epoch_semantics.md`, `resources/research/144_rtcc_mass_properties_depletion_table_architecture.md`, `resources/research/145_apollo13_tplus_reference_epoch_boundary.md`, `resources/research/146_pc2_mass_properties_cross_console_reconciliation.md`

## Resolved this pass

Research-note-130 target 5 is narrowed substantially. The final Apollo 13 PC+2 P30 LM maneuver PAD explicitly carried `62480 lb` CSM and `33452 lb` LM at GET 077:55:24 for TIG 079:27:38.30, and the pair survived crew readback/ground confirmation.

The Flight Control Division Mission Operations Report further establishes that:

- RTCC **LM-burn mass-property decks were updated to T+55 decks** before the abort maneuver work; and
- a PC+2 DPS trim disagreement was resolved because LM Control had used **premission mass properties**, which were not the best data then available.

Research note 142 adds Apollo-era operational semantics from primary Apollo 10/11 support documentation: mass-properties products fed trajectory, trim, DAP/control, and propellant-support computations, with in-flight updates as propellant state and vehicle configuration changed. This supports treating the Apollo 13 T+55 deck as an in-flight operational mass-properties state product rather than a fixed preflight constant.

Research note 143 narrows the `T+55` label using the Apollo 13 report itself. The same Flight Dynamics narrative records lift-off (`T-6`) mass properties, compares a `T+25` mass-properties run against `T+6` trims, and later updates LM-burn decks to `T+55`. This establishes the labels as successive **mission-relative, time-tagged mass-properties bases/products**. `T+55` can therefore be represented as a mass-properties state associated with approximately mission time +55 hours, rather than an opaque revision identifier.

Research note 144 adds a primary NASA RTCC requirements source from June 1971 that explicitly describes the Skylab mass-properties system as a **carryover of the present Apollo RTCC Mass Properties System**. Its architecture maintains weight/CG, sums module-level inputs, supports temporary or permanent propellant depletion tables, and feeds engine-trim calculations from input spacecraft weight and center of mass. This confirms that the Apollo-era mass-properties state was structurally richer than a single scalar weight and provides a safe architectural target for the simulator without supplying unrecovered H-2 values.

Research note 145 resolves one remaining ambiguity using a stronger timing separation in the same Apollo 13 report: the lift-off `T-6` mass properties were **generated and loaded into RTCC by T-2:46**. Therefore the `T±N` label is distinct from the actual generation/loading timestamp. `T+55` should be modeled as a mission-relative mass-properties **reference state/epoch label**, while exact-versus-nominal/propagated epoch semantics remain unresolved.

Research note 146 formalizes the operational consequence of stale-versus-current mass-property provenance. At about 59 hours GET, LM Control challenged a PC+2 DPS trim and later agreed with the Flight Dynamics data after the report identified LM Control's **premission mass properties** as not the best data available. This establishes cross-console reconciliation of a derived maneuver product when stations used different mass-property bases. The report does **not** explicitly state that the accepted data in this dispute were the `T+55` deck, so that linkage remains unproven.

These values are therefore safe to use as **historical final-PAD / targeting regression inputs with an in-flight updated, mission-time-tagged RTCC mass-properties lineage**.

## Boundary retained

The Apollo 13 report still does not define whether `T+55` means exactly 55:00:00 GET, a nominal scheduled reference epoch, or a propagated state referenced to approximately +55 hours. The 1971 RTCC requirements note does not close that gap: it does not identify `T+55` as a depletion table or define H-2 deck fields. Nor do the sources provide the H-2 deck record layout, processor fields, or mapping from the deck to the final `62480 + 33452 = 95932 lb` P30 pair. The pair must not be labeled exact physical ignition mass.

Keep distinct:

1. hidden physical vehicle mass/CG;
2. mission-control mass-properties deck/state;
3. component/module and propellant-depletion state within that computational layer;
4. mission-relative deck epoch label versus actual generation/update timestamp;
5. provenance of the mass-properties basis used by a derived calculation (`premission` versus current operational state);
6. maneuver targeting/P30 weights;
7. controller-visible trim/trajectory products and any cross-console reconciliation of them.

## Propulsion boundary now partially resolved

Research note 139 establishes mission-specific PC+2 burn duration, staged throttle-command behavior, terminal blowdown, and the Apollo 13 configuration's nominal full-thrust value. It also shows why an instantaneous piecewise-constant-thrust history is not yet a historical reconstruction: startup buildup was operationally material, and the final portion of PC+2 was a distinct blowdown condition.

General DPS design values remain separate from LM-7 PC+2 calibration. In particular, the Apollo 13 `9870 lbf` nominal full-thrust baseline must not be silently equated with the general design report's `10,500 lbf` maximum rated thrust, and the design `305 s` specific impulse is not yet frozen as the PC+2 effective Isp.

## Apollo 13 DPS Supplement 2 retrieval status

Research note 140 establishes that Apollo 13 Mission Report Supplement 2, *Descent Propulsion System Final Flight Evaluation*, was recorded by later official NASA mission reports as published in **October 1970**, although a public copy and verified report identifier remain unrecovered.

Research note 141 narrows the archival search using primary NTRS metadata from adjacent dedicated DPS evaluations. Apollo 10, Apollo 12, and Apollo 14 evaluations all sit in a TRW Systems Group / MSC propulsion-analysis lineage, with contract `NAS9-8166` documented on the adjacent records. This supports using `TRW Systems Group` and `NAS9-8166` as retrieval terms for Apollo 13.

This does **not** verify an Apollo 13 TRW number, author list, or `MSC-02680-SUPPL-2` identifier. That MSC form remains only a search key until a primary record confirms it.

## Next unresolved numerical inputs

Priority order is now:

1. recover mission-specific H-2 RTCC/Flight Dynamics documentation defining the **precise T+N reference-epoch convention** and LM-burn deck fields/values, with special attention to an explicit link between the accepted ~59-hour PC+2 DPS trim and the `T+55` deck, plus how module summation and temporary/permanent propellant depletion tables entered the mission-specific deck/state;
2. recover the published October 1970 Apollo 13 Mission Report Supplement 2, *Descent Propulsion System Final Flight Evaluation*, using the evidence-based provenance tuple `Apollo 13 + LM-7 + exact title + October 1970 + TRW Systems Group + NAS9-8166 + MSC-02680`;
3. recover LM-7 engine acceptance/calibration or PC+2 high-speed propulsion data if Supplement 2 remains inaccessible;
4. extract original LMS/FMES equations/integration assumptions beyond the current public handbook boundary;
5. recover sufficient state-vector/trajectory information for postburn propagation and regression.

## Integration rule

Do not force a numerical DPS model to reproduce `861.5 ft/s` by assuming `95932 lb` is exact ignition mass. Treat exact agreement as a validation target only after the precise mass epoch convention, mission-specific mass/depletion state, delivered-thrust / mass-flow history (including transient and blowdown treatment), propellant consumption, and integration assumptions are source-bounded.

For controller logic, retain the provenance of the mass-properties basis used to derive each trim/targeting product. A stale premission basis may produce an operational disagreement, but do not label the accepted Apollo 13 ~59-hour trim as explicitly `T+55` unless a source directly makes that connection.