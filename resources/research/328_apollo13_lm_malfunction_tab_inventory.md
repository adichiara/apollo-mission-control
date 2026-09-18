# Research note 328 — Apollo 13 LM malfunction-procedure tab inventory

Date: 2026-09-18

## Question

Can the first page-extraction target from research 326 be narrowed to a concrete section/tab inventory while the 70 MB public scan remains inaccessible to direct page extraction in the current tool path?

## Result

Partially.

The indexed OCR returned from the **16 March 1970 FINAL** Lovell-copy scan itself exposes multiple cover/tab labels, including **AGS**, **CES**, **DPS**, and **RCS**. This is primary-document evidence, but the current indexed response is incomplete and does not expose every tab cleanly enough to claim a complete inventory from the scan alone.

A separately described March 16, 1970 training copy of the same part number (`SKB32100076-386`) provides a fuller artifact-level tab inventory: **G&C Displays, PGNS, AGS, CES, DPS, APS, RCS, EPS, COMM, ECS, ED, HTRS, Camera, and EMU**. Because that description is a secondary artifact catalog rather than direct page inspection of S/N 1001, this full list remains **PROVISIONAL** for the flown/public Lovell scan until direct page or tab-image verification.

Sources:

### Primary/public scan

- *Apollo 13 LM Malfunction Procedures*, `SKB32100076-386`, FINAL, 16 March 1970:
  https://www.ibiblio.org/apollo/Documents/Apollo%2013%20Malfunction%20Procedures.pdf

### Secondary artifact cross-check

- RR Auction description of James Lovell's March 16, 1970 training-used copy of `SKB32100076-386`:
  https://www.rrauction.com/auctions/lot-detail/347221406649375-james-lovells-apollo-13-training-used-lm-malfunction-procedures-book/

## Evidence boundary

The four labels visible in indexed primary OCR can be treated as directly observed in the scan retrieval path. The complete fourteen-label inventory cannot yet be promoted to direct flown-copy evidence.

Do not infer from a tab name:

- exact symptom list;
- page count or page range;
- LMS malfunction availability;
- simulator injection controls;
- internal failure representation;
- Change A equivalence.

## Retrieval consequence

When direct scan page access becomes available, page extraction should proceed by tab rather than as an undifferentiated 80-page document. First verify the provisional inventory against S/N 1001, then capture for each tab:

1. tab/section label;
2. page range;
3. page date/change marking;
4. symptom/entry headings;
5. crew decision/action branches;
6. caution/warning indications;
7. cross-references to other malfunction procedures.

This creates a controlled operational crosswalk that can later be compared to LMS Section 2 **Malfunction Data** without assuming the two documents share structure or failure identifiers.

## What remains open

- complete direct tab inventory for S/N 1001;
- page-level symptom/procedure inventory;
- 16 March FINAL -> 1 April FINAL CHANGE A delta;
- mapping, if any, between crew-procedure entries and LMS Section 2 malfunction definitions.

No station maturity, causal constant, or executable behavior changes from this note.
