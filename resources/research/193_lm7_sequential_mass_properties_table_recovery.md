# Research Note 193 — LM-7 Amendment 79 sequential mass-properties table recovery

Date: 2026-09-16

## Question

Can the late-preflight LM-7 sequential mass-properties table referenced by the Amendment 79 consumables summary be recovered directly, and what does it actually establish for the CONTROL/PC+2 provenance problem?

## Primary source

NASA/MSC, *CSM/LM Spacecraft Operational Data Book, Volume III — Mass Properties*, SNA-8-D-027(III) Rev. 2, Amendment 79, pages dated 30 March 1970. Recovered page images 3.3-10.1 through 3.3-10.3 identify **TABLE 3.3-3 (CONTINUED), LM-7 EFFECTIVE SEQUENTIAL MASS PROPERTIES**.

The same Amendment 79 document's Table 3.3-8, `LM-7 Consumables Change Summary`, says it is `to be used in conjunction with the LM sequential mass properties Table 3-3.2`.

## Finding 1 — the LM-7 sequential table is directly recoverable

The recovered Amendment 79 pages are not merely a consumables summary. They directly print LM-7 effective sequential mass-property states, with columns for weight, c.g. coordinates, inertias/products of inertia, and dispersions.

One clearly legible premission state is `LM PRE P.D.I.` on page 3.3-10.1:

- weight: **33,980.1 lb**
- c.g. X: **188.1 in**
- c.g. Y: approximately **-0.0 in** as printed
- c.g. Z: **-0.8 in**

These are source-backed premission sequential-model values. They are not Apollo 13 real-time T+55 values and are not assigned to CONTROL.

## Finding 2 — Table-number cross-reference inconsistency

Table 3.3-8 explicitly calls its companion `LM sequential mass properties Table 3-3.2`, while the recovered LM-7 sequential pages themselves are headed **Table 3.3-3**. In the same document, Table 3.3-2 pages are CSM 109 effective sequential mass properties.

Therefore the repository must no longer describe the still-missing target simply as `LM-7 Table 3-3.2`. The primary source contains an internal table-number mismatch. The directly recovered LM-7 sequential table is Table 3.3-3; Table 3.3-8's `3-3.2` wording should be preserved as a source cross-reference, not silently normalized or treated as proof that a second LM table exists.

No claim is made here about whether the Table 3.3-8 reference is a typographical error, amendment artifact, or numbering convention. That cause remains unproved.

## Finding 3 — this narrows, but does not close, CONTROL provenance

The recovery establishes a concrete official LM-7 preflight mass/c.g. model available on 30 March 1970. It therefore gives a much stronger candidate source family for the `premission mass properties` mentioned in the Flight Dynamics chronology.

It still does **not** establish:

- that CONTROL selected Table 3.3-3 or Amendment 79;
- the exact mass/c.g. state CONTROL used for the ~59 GET disagreement;
- CONTROL's competing trim values;
- the comparison/acceptance criterion;
- a T+55 real-time weight/c.g. product;
- a downstream RTCC/RTACF run consuming T+55 data; or
- a direct computational edge from any recovered preflight row to `5.86 / 6.75`.

## Modeling consequence

Add a distinct source state:

`official_available_preflight_lm7_sequential = SNA-8-D-027(III) Rev 2 / Amendment 79 / Table 3.3-3 / 1970-03-30`

Preserve its printed rows as premission reference data only. Do not substitute `LM PRE P.D.I. = 33,980.1 lb` for the Review Board's `33,941 lb at CSM/LM separation`, the 17 March analysis-specific `33,872.3 lbm`, CONTROL's unknown selected state, or T+55.

## Next target

Priority 1 remains the mission-specific `T+55 deck -> weight/c.g. -> RTCC/RTACF request/run -> 5.86 / 6.75` consumption edge.

Priority 2 is now controller working material identifying whether CONTROL used this recovered Amendment 79/Table 3.3-3 model or another premission set, plus CONTROL's competing numerical trim and comparison criterion. A useful parallel check is recovery of the opening page(s) of Table 3.3-3 and any amendment/revision annotations needed to reconstruct the full LM-7 sequential state series without extrapolation.