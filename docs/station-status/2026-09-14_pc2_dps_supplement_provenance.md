# Station-status addendum — PC+2 DPS and mass-properties provenance

Date: 2026-09-14

Historical station maturity grades are unchanged. This pass improves the source boundary for propulsion and Flight Dynamics mass-properties state, not console/display reconstruction.

## CONTROL

Maturity remains **B**.

Mission-specific sources establish the staged PC+2 throttle-command profile, terminal blowdown, and nominal Apollo 13 full-thrust baseline. Research note 141 narrows the missing dedicated LM-7 final-flight evaluation to a TRW/MSC contractor-reporting lineage supported by adjacent primary NTRS records.

Research note 146 adds an operational provenance constraint: at about 59 hours GET, LM Control challenged the PC+2 DPS trim and later agreed with the Flight Dynamics data after the report identified LM Control's premission mass properties as not the best data available. This supports a simulator behavior in which CONTROL/LM Control can challenge a derived trim when its mass-properties basis is stale.

Still unresolved for CONTROL-facing historical numerical fidelity:

- measured LM-7 PC+2 thrust-versus-time;
- exact startup transient;
- throttle-to-delivered-thrust calibration;
- PC+2-specific mass flow / mixture ratio / effective Isp;
- blowdown force/feed-pressure decay;
- exact Apollo 13 CONTROL display/loading for these products;
- the exact numerical trim discrepancy in the ~59-hour challenge;
- whether the accepted trim explicitly used the `T+55` deck.

No adjacent-mission propulsion constants are promoted into the Apollo 13 station model.

## FIDO / Flight Dynamics

Maturity remains **B**, but the mass-properties interpretation is stronger.

Research note 142 establishes from Apollo 10/11 operational support documentation that mass-properties products were active computational inputs/products for trajectory, trim, DAP/control, and propellant-support work and could be updated as propellant state and vehicle configuration changed.

Research note 143 adds mission-specific Apollo 13 evidence: the Flight Dynamics narrative uses `T-6`, `T+6`, `T+25`, and `T+55` for successive mass-properties bases/products. A `T+25` run was explicitly compared against `T+6` trims, and the later LM-burn decks were updated to `T+55`. The `T+55` label should therefore be represented as a **mission-relative time-tagged mass-properties state associated with approximately +55 hours**, not as an opaque deck revision identifier.

Research note 144 adds a primary NASA RTCC requirements source from June 1971. It explicitly says the Skylab mass-properties system was to be a carryover of the present Apollo RTCC Mass Properties System and documents an architecture with module summation, total weight/CG computation, temporary or permanent propellant depletion tables, and engine-trim calculations driven by input spacecraft weight and center of mass. This supports modeling the Flight Dynamics mass-properties layer as structured operational state rather than a single scalar mission weight.

Research note 145 closes the generation-time ambiguity. The Apollo 13 report states that lift-off `T-6` mass properties were **generated and loaded in RTCC by T-2:46**. The `T±N` label is therefore distinct from the actual generation/loading timestamp and should be represented as a **mass-properties reference state/epoch label**.

Research note 146 closes a separate operational question: mass-property provenance could matter enough to create and resolve a cross-console disagreement in a maneuver-support product. At ~59 hours GET, LM Control challenged the PC+2 DPS trim but later accepted the Flight Dynamics data; the report says LM Control had used premission mass properties, which were not the best data available. The source does not explicitly identify the accepted Flight Dynamics basis as the `T+55` deck.

Still unresolved:

- whether `T+55` denotes exactly 55:00:00 GET, a nominal/scheduled reference epoch, or a propagated-state reference epoch;
- whether `T+55` selected or contained temporary/permanent propellant depletion tables;
- H-2 LM-burn deck field layout, module breakdown, mass/CG values, and depletion-state values;
- processor mapping from deck values into the PC+2 solution;
- exact relationship between the deck and the final P30 CSM/LM weights;
- whether those P30 weights equal physical ignition mass;
- explicit proof that the accepted ~59-hour trim used the `T+55` deck rather than another updated mass-properties basis.

The simulator should keep physical mass/CG, mission-control mass-properties state, module/depletion-table state, reference epoch label, actual generation/load timestamp, calculation provenance, targeting weights, and controller-visible trajectory/trim products separate.

## FLIGHT

Maturity remains **B**.

No new decision authority or display behavior is inferred. The improved evidence now distinguishes the mission-relative `T+55` reference label from deck generation/loading time and establishes that a stale premission mass-properties basis could trigger a cross-console trim challenge that was later reconciled. The exact H-2 reference-epoch rule, accepted ~59-hour deck identity, and deck contents remain open, as does LM-7-specific propulsion performance.

## Research priority

First priority is now mission-specific H-2 RTCC/Flight Dynamics documentation defining the **precise T+N reference-epoch convention** and LM-burn deck fields/values, especially any material explicitly linking the accepted ~59-hour PC+2 DPS trim to the `T+55` deck and showing how module summation and propellant-depletion tables propagated into trim/targeting products. In parallel, continue recovery of the October 1970 Apollo 13 *Descent Propulsion System Final Flight Evaluation* using:

`Apollo 13 + LM-7 + exact title + October 1970 + TRW Systems Group + NAS9-8166 + MSC-02680`

`MSC-02680-SUPPL-2` remains an unverified archival search key, not a documented report identifier.