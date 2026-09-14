# Station-status addendum — PC+2 DPS and mass-properties provenance

Date: 2026-09-14

Historical station maturity grades are unchanged. This pass improves the source boundary for propulsion and Flight Dynamics mass-properties state, not console/display reconstruction.

## CONTROL

Maturity remains **B**.

Mission-specific sources establish the staged PC+2 throttle-command profile, terminal blowdown, and nominal Apollo 13 full-thrust baseline. Research note 141 narrows the missing dedicated LM-7 final-flight evaluation to a TRW/MSC contractor-reporting lineage supported by adjacent primary NTRS records.

Still unresolved for CONTROL-facing historical numerical fidelity:

- measured LM-7 PC+2 thrust-versus-time;
- exact startup transient;
- throttle-to-delivered-thrust calibration;
- PC+2-specific mass flow / mixture ratio / effective Isp;
- blowdown force/feed-pressure decay;
- exact Apollo 13 CONTROL display/loading for these products.

No adjacent-mission propulsion constants are promoted into the Apollo 13 station model.

## FIDO / Flight Dynamics

Maturity remains **B**, but the mass-properties interpretation is stronger.

Research note 142 establishes from Apollo 10/11 operational support documentation that mass-properties products were active computational inputs/products for trajectory, trim, DAP/control, and propellant-support work and could be updated as propellant state and vehicle configuration changed.

Research note 143 adds mission-specific Apollo 13 evidence: the Flight Dynamics narrative uses `T-6`, `T+6`, `T+25`, and `T+55` for successive mass-properties bases/products. A `T+25` run was explicitly compared against `T+6` trims, and the later LM-burn decks were updated to `T+55`. The `T+55` label should therefore be represented as a **mission-relative time-tagged mass-properties state associated with approximately +55 hours**, not as an opaque deck revision identifier.

Research note 144 adds a primary NASA RTCC requirements source from June 1971. It explicitly says the Skylab mass-properties system was to be a carryover of the present Apollo RTCC Mass Properties System and documents an architecture with module summation, total weight/CG computation, temporary or permanent propellant depletion tables, and engine-trim calculations driven by input spacecraft weight and center of mass. This supports modeling the Flight Dynamics mass-properties layer as structured operational state rather than a single scalar mission weight.

Research note 145 closes the generation-time ambiguity. The Apollo 13 report states that lift-off `T-6` mass properties were **generated and loaded in RTCC by T-2:46**. The `T±N` label is therefore distinct from the actual generation/loading timestamp and should be represented as a **mass-properties reference state/epoch label**.

Still unresolved:

- whether `T+55` denotes exactly 55:00:00 GET, a nominal/scheduled reference epoch, or a propagated-state reference epoch;
- whether `T+55` selected or contained temporary/permanent propellant depletion tables;
- H-2 LM-burn deck field layout, module breakdown, mass/CG values, and depletion-state values;
- processor mapping from deck values into the PC+2 solution;
- exact relationship between the deck and the final P30 CSM/LM weights;
- whether those P30 weights equal physical ignition mass.

The simulator should keep physical mass/CG, mission-control mass-properties state, module/depletion-table state, reference epoch label, actual generation/load timestamp, targeting weights, and controller-visible trajectory/trim products separate.

## FLIGHT

Maturity remains **B**.

No new decision authority or display behavior is inferred. The improved evidence now distinguishes the mission-relative `T+55` reference label from deck generation/loading time. The exact H-2 reference-epoch rule and deck contents remain open, as does LM-7-specific propulsion performance.

## Research priority

First priority is now mission-specific H-2 RTCC/Flight Dynamics documentation defining the **precise T+N reference-epoch convention** and LM-burn deck fields/values, especially any material showing how module summation and propellant-depletion tables were instantiated and how the reference epoch propagated into trim/targeting products. In parallel, continue recovery of the October 1970 Apollo 13 *Descent Propulsion System Final Flight Evaluation* using:

`Apollo 13 + LM-7 + exact title + October 1970 + TRW Systems Group + NAS9-8166 + MSC-02680`

`MSC-02680-SUPPL-2` remains an unverified archival search key, not a documented report identifier.