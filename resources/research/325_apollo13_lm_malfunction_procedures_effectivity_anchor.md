# Research note 325 — Apollo 13 LM malfunction-procedure effectivity anchor

Date: 2026-09-18

## Question

While the 1967 LMS Volume II Section 2 **Malfunction Data** remains inaccessible at page level, is there a mission-specific Apollo 13 source that can independently constrain which LM malfunction symptoms/procedures are historically appropriate without pretending that crew procedures document LMS instructor injection mechanics?

## Result

Yes, with a strict scope boundary.

The Virtual AGC document collection records a digitization of **Apollo 13 LM Malfunction Procedures** made from James Lovell's original copy. Its collection change log records the scan's addition on 6 March 2023. The same library independently controls Apollo 13 LM guidance configuration with the Apollo-era `2021112-121` assembly listing for **LM131 rev 1**, identifying it as the Apollo 13 LM AGC flight software.

Collection records:

- https://www.ibiblio.org/apollo/changes.html
- https://www.ibiblio.org/apollo/links2.html

Surviving physical-copy descriptions provide a useful retrieval key for the primary artifact: **Apollo 13 LM Malfunction Procedures**, Flight Data File part number `SKB32100076-386`. Multiple surviving-copy records identify March 16 / April 1, 1970 states; those dates must be resolved from the scanned artifact's own control/change pages before choosing an effectivity state.

NASA's contemporaneous H-2 mission-technique series provides an independent period boundary around the same mission class, including final issues for lunar-orbit activities, lunar surface, powered ascent, lunar descent, manual ascent, contingency procedures, and translunar/lunar-orbit operations from January-April 1970. These are useful cross-checks for phase applicability, not substitutes for the malfunction checklist or LMS handbook.

## What this closes

The project now has a **mission-specific Apollo 13 malfunction-procedure corroboration target** that is much closer in effectivity than the 1967 LMS handbook. It can be used, once page-extracted, to test whether candidate player-visible LM symptoms, caution/warning indications, crew troubleshooting branches, and phase restrictions are appropriate to Apollo 13.

This is especially useful for D-022-style demonstrated irrelevance and causal-engine validation: a simulated failure should not expose a player-visible symptom merely because a 1967 simulator handbook or proposal contains it if Apollo 13-period operational material contradicts or omits that behavior at the product resolution being modeled.

## What this does not close

Crew Flight Data File procedures do **not** establish LMS instructor-side mechanisms. Do not infer from them:

- LMS malfunction insertion controls or scripting syntax;
- instructor console actions;
- simulator processor allocation or numerical cadence;
- how a malfunction was represented internally in LMS software;
- whether every crew-procedure malfunction was injectable in the LMS;
- whether every LMS-injectable malfunction appeared in the crew checklist.

Likewise, collection metadata is not a substitute for the scanned checklist's own title/change pages. The March 16 / April 1 state distinction remains page-gated.

## Retrieval consequence

1. Keep 1967 Volume II Section 2 **Malfunction Data** as the primary source for LMS instructor-side failure definitions/insertion mechanics.
2. Add the Apollo 13 `SKB32100076-386` scan as the first mission-specific operational cross-check for player-visible LM malfunction symptoms and crew response.
3. On extraction, read cover/title/change-control pages first; then inventory section tabs and symptom/procedure headings before encoding any behavior.
4. Cross-check any candidate behavior against Apollo 13-period AOH/mission-technique material and LM-7 configuration evidence where applicable.

No station maturity, causal constants, or executable behavior changes from this research note.
