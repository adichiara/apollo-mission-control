# Progress — Apollo 11 P66 / PCR-700 implementation

Date: 2026-09-19
Research: 329–332

## Completed

- Direct MIT implementation evidence establishes PCR-700 ancestry in LUMINARY: Memo #67 records PCR-700 and PCR-670 implemented in Revision 72; Memo #73 records the later P66 total-lag compensation in Revision 80 and introduction of `LAG/TAU`.
- Apollo 11 mission/configuration evidence from `SNA-8-D-027(II) REV 1` shows the LM-5 Mission G LUMINARY 99 prelaunch load containing `LAG/TAU = 0.413333`.
- Section 5 Revision 4 remains a historical anchor; its recovered inventory does not list PCR-670/PCR-700.
- The surviving cumulative R-567 Section 5 artifact preserves a **Guidance Equations (Revision 5)** index listing PCR-670 and PCR-700A without later-revision dagger marks.
- Section 5 Revision 5 is therefore the earliest directly recovered Section 5 control state in the inspected chain containing both landing-change identifiers. This is a retrieval/effectivity lead, not proof that Rev. 5 was the first historical documentation state or the Apollo 11 flight-effective page set.
- Research 332 inspected the next controlled equation endpoint. MSC `69-FS-4` explicitly documents LUMINARY 1B P66 rate-of-descent variables/states, while R-567 Revision 8 explicitly records later P66 changes PCR-988 and PCR-1013 and notes that some unchanged pages were republished for convenience.

## Boundary retained

The January SCB once-per-second P66 ROD computations/commands and HDOT display behavior are still not promoted as final flight behavior. The secondary document-library description of PCR-700A as a rewritten clarification of PCR-700 remains a retrieval aid pending a primary 700/700A crosswalk. LUMINARY 1B/1C equation text is now explicitly classified as comparison evidence only until page-level unchanged ancestry to the Apollo 11 state is demonstrated.

## Model effect

No executable equation, cadence, DSKY behavior, controller product, or station maturity changed.

## Next

Recover the Section 5 Revision 5 P63-P66 affected pages and establish their LUMINARY 1A Rev. 099/Apollo 11 effectivity or unchanged-page ancestry. Use later controlled equation documents to test ancestry rather than back-project behavior. Retain `69-FS-3` as the parallel preferred complete-equation target.