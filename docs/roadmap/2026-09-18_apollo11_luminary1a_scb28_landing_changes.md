# Apollo 11 LUMINARY 1A landing-guidance retrieval roadmap

Date: 2026-09-18

## New primary-source result

MIT Instrumentation Laboratory Apollo Project Memo 7-69, dated 23 January 1969, records the results of the 28th Apollo Software Configuration Control Board meeting and explicitly describes the then-approved contents of LUMINARY 1A, the Mission G program.

For the landing domain it records:

- PCR 700, *Improve the ROD Mode (P66) Performance*, with planned changes including an erasable click scale factor, once-per-second rate-of-descent equations/commands, once-per-second DSKY HDOT updating, and protection against losing clicks at P66 entry;
- PCR 670, *Simplify Landing Programs*, with Section 5 GSOP action assigned to Allan Klumpp and Section 4 action to Walker Kupfer;
- landing-radar PCRs 704, 705, 706 and 723 as disapproved at that board state;
- a separate unresolved P64 attitude-oscillation correction for which the memo says a PCR/PCN was still to be submitted.

The June 1969 R-567 Section 2 Rev. 4 control sheet independently lists PCR 700 and PCR 670 in the LUMINARY 1A Rev. 099 document state. This provides a controlled crosswalk from January approved intent to June LUMINARY 1A documentation, but not the missing Section 5 equations themselves.

## Retrieval consequence

The next direct-content target is narrower:

1. recover the LUMINARY 1A-effective R-567 Section 5 revision/control pages;
2. prioritize the Section 5 pages implementing PCR 670 and any landing-equation pages governing P63-P66;
3. recover the final implementation evidence for PCR 700 from the program listing and/or controlled GSOP change pages before encoding P66 cadence/click behavior;
4. identify the later PCR/PCN, if any, that closed the P64 attitude-oscillation item before treating the January proposed extrapolation as flight behavior;
5. continue searching for MSC 69-FS-3 as the preferred complete LUMINARY 1A programmed-guidance-equation source.

## Guardrail

Memo 7-69 is configuration-control intent as of 23 January 1969. It is not proof that every described change was present unchanged in the flown Rev. 099 program. No equation, constant, cadence, display behavior, or runtime interaction is promoted solely from this memo.
