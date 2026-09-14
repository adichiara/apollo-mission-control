# Station-status addendum — PC+2 DPS Supplement 2 provenance

Date: 2026-09-14

Historical station maturity grades are unchanged. This pass improves propulsion-source provenance, not console/display reconstruction.

## CONTROL

Maturity remains **B**.

The documented Apollo 13 PC+2 propulsion boundary is stronger: mission-specific sources already establish the staged throttle-command profile, terminal blowdown, and nominal Apollo 13 full-thrust baseline. Research note 141 further narrows the missing dedicated LM-7 final-flight evaluation to a TRW/MSC contractor-reporting lineage supported by adjacent primary NTRS records.

Still unresolved for CONTROL-facing historical numerical fidelity:

- measured LM-7 PC+2 thrust-versus-time;
- exact startup transient;
- throttle-to-delivered-thrust calibration;
- PC+2-specific mass flow / mixture ratio / effective Isp;
- blowdown force/feed-pressure decay;
- exact Apollo 13 CONTROL display/loading for these products.

No adjacent-mission propulsion constants are promoted into the Apollo 13 station model.

## FIDO / Flight Dynamics

Maturity remains **B**.

The independent mass-properties uncertainty is unchanged: Apollo 13 Flight Dynamics used an in-flight updated T+55 LM-burn mass-property deck lineage, but the deck semantics and exact propagation to the final PC+2 P30 weights remain unresolved.

## FLIGHT

Maturity remains **B**.

No new decision authority or display behavior is inferred. The improved source provenance only makes the propulsion-validation dependency more explicit: a historically calibrated PC+2 causal model still requires LM-7-specific performance evidence or an explicit lower-fidelity project decision.

## Research priority

For station-facing PC+2 fidelity, prioritize recovery of the October 1970 Apollo 13 *Descent Propulsion System Final Flight Evaluation* using the evidence-based tuple:

`Apollo 13 + LM-7 + exact title + October 1970 + TRW Systems Group + NAS9-8166 + MSC-02680`

`MSC-02680-SUPPL-2` remains an unverified archival search key, not a documented report identifier.