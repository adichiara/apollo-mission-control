# 902 — Apollo 11 LUMINARY 1A equation reissue boundary

Research thread: `apollo11-descent-runtime`

## Bounded question

Can the recoverable LUMINARY 1B programmed-guidance-equation document constrain Apollo 11 / LUMINARY 1A descent equations without silently treating later software as Apollo 11 configuration?

## Findings

MSC Internal Note 69-FS-4, *Programmed Guidance Equations for LUMINARY 1B Manned LM Earth Orbital and Lunar Program*, states in its own Page Change Record that it is a **complete re-issue** of MSC Internal Note 69-FS-3, *Programmed Guidance Equations for LUMINARY 1A Manned LM Earth Orbital and Lunar Program*, dated May 1969, updated for LUMINARY 1B.

The same change record explicitly distinguishes coding changes between LUMINARY 1A and 1B from editorial changes and identifies affected pages. Its changed-page inventory includes multiple descent and radar pages, including DESC and RADR sections. Therefore 69-FS-4 is a primary configuration-delta source, not permission to treat all 1B equations as Apollo-11-effective.

This improves the earlier recovery boundary: the missing 69-FS-3 body is still the preferred direct Apollo 11 equation authority, but 69-FS-4 can be used to identify where 1A→1B changes occurred and to avoid importing changed 1B material into the Apollo 11 runtime.

## Runtime consequence

For the Apollo 11 runtime:

- do not globally alias LUMINARY 1B equations to LUMINARY 1A;
- use 69-FS-4 as a change-control map when evaluating a specific equation;
- any equation on a page identified as changed requires Apollo-11-effective corroboration before admission;
- unchanged/reissued material may narrow the search, but the project should not claim exact 1A text solely from an OCR/rendering assumption without page-level inspection.

This leaves the event/checkpoint runtime from research 900 admissible while keeping exact programmed-equation implementation source-gated.

## Closure challenge

A focused exact-document search recovered the complete-reissue/change-record statement but did not recover a separately authenticated public copy of 69-FS-3. The new evidence changes the recovery strategy, not the Apollo 11 equation set itself.

## Sources

1. NASA MSC, *Programmed Guidance Equations for LUMINARY 1B Manned LM Earth Orbital and Lunar Program*, MSC Internal Note 69-FS-4, public scan mirrored by the Virtual AGC archive; Page Change Record states that it is a complete re-issue of 69-FS-3 and describes the 1A→1B change markings.
2. MSC Internal Note 69-FS-3, *Programmed Guidance Equations for LUMINARY 1A Manned LM Earth Orbital and Lunar Program*, May 1969 — identified by 69-FS-4; separate body not recovered in this pass.

## Evidence status

- **DOCUMENTED:** 69-FS-4 identifies itself as a complete re-issue of May 1969 69-FS-3 updated for LUMINARY 1B.
- **DOCUMENTED:** 69-FS-4 explicitly identifies 1A→1B coding changes and editorial changes and lists affected DESC/RADR pages.
- **PARTIALLY DOCUMENTED:** 69-FS-4 can constrain the 1A→1B delta at page/change-record level.
- **UNRESOLVED:** exact 69-FS-3 page text wherever Apollo-11-effective equation details are required and cannot be independently corroborated.
