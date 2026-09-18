# Research note 326 — Apollo 13 flown LM malfunction-procedure document state

Date: 2026-09-18

## Question

Can the March 16 / April 1, 1970 state ambiguity left by research 325 be narrowed without treating later catalog descriptions as primary document control?

## Result

Yes. The publicly indexed text of the digitized **Apollo 13 LM Malfunction Procedures** scan itself exposes the cover fields for the Lovell copy: title **APOLLO 13 LM MALFUNCTION PROCEDURES**, part number `SKB32100076-386`, status **FINAL**, and handwritten/printed date **3/16/70**. Virtual AGC states that this digitization was made from Jim Lovell's original copy.

A separate primary NASA launch stowage list for AS-508 / LM-7 identifies `SKB32100076-386` as **LM MALFUNCTION PROCEDURES** within the LM Flight Data File carried for the mission. This independently establishes the part-number/mission relationship.

Primary/public records:

- digitized Lovell copy: https://www.ibiblio.org/apollo/Documents/Apollo%2013%20Malfunction%20Procedures.pdf
- Virtual AGC provenance record: https://www.ibiblio.org/apollo/changes.html
- NASA Apollo 13 final stowage list: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/as13b-stowage-list-final-197007.pdf

## Effectivity conclusion

For the **digitized Lovell copy**, the controlled state is therefore **FINAL, 16 March 1970**. The April 1, 1970 `FINAL CHANGE A` quarters/training copy documented in surviving-copy records is a different later document state and must not be silently substituted for the scanned flown-copy state.

This resolves the retrieval ambiguity for the public Lovell scan. It does **not** establish what technical changes were introduced by Change A, nor does it prove that every page in the flown copy carries the same printed date. Page-level technical extraction must retain page dates/revision markings when present.

## Additional corroboration

Surviving pages from the flown copy have repeatedly been described with the heading `LMA790-3-LM, Apollo Operations Handbook` and date 16 March 1970. That secondary provenance is compatible with the scan state but is not needed to establish the cover-level result above.

## What this closes

- Public Lovell scan identity: `SKB32100076-386`.
- Scan cover status: **FINAL**.
- Scan cover date: **16 March 1970**.
- Mission carriage: NASA final stowage documentation lists the same part number as LM Malfunction Procedures in the Apollo 13 LM Flight Data File.

## What remains open

- exact technical delta between 16 March FINAL and 1 April FINAL CHANGE A;
- page-by-page dates/change markings inside the scan;
- complete symptom/procedure inventory;
- relationship between crew procedures and LMS Section 2 malfunction definitions;
- LMS instructor controls, scripting syntax, internal failure representation, and injectability.

## Project consequence

The public Lovell scan may now be treated as a page-extraction source with a controlled **16 March 1970 FINAL** document state. It is a strong Apollo 13 operational cross-check for player-visible LM symptoms and crew troubleshooting, but remains outside the evidence class for simulator-side malfunction insertion.

No station maturity, causal constant, processor assignment, or executable behavior changes from this note.
