# Research note 404 — Apollo 11 P66 flight-listing cadence

Date: 2026-09-19
Research thread: `apollo11-p66-pcr700`
Status: **SUFFICIENT for current implementation; remaining equation-document ancestry deferred**

## Question

Did the January 1969 PCR-700 proposal's once-per-second P66 rate-of-descent computation survive into the Apollo 11 LUMINARY 99 implementation, and what is the relationship between PCR-700 and the Section 5 PCR-700A identifier?

## Findings

The surviving LUMINARY 099 assembly listing provides direct program evidence in `LUNAR_LANDING_GUIDANCE_EQUATIONS.agc`.

In the P66 guidance path, `P66VERT` posts `P66VERTA`. `P66VERTA` terminates phase group 3 and then loads the constant `1SEC`, calls `TWIDDLE`, and supplies `RODTASK` as the scheduled task address. `RODTASK` in turn obtains a VAC area for `RODCOMP`. `RODCOMP` updates `VDGVERT` from `RODCOUNT * RODSCAL1`, then performs the P66 computation path. The same routine updates `HDOTDISP` for Noun 63 and later uses `LAG/TAU`, `MAXFORCE`, and `MINFORCE` in the acceleration-command calculation.

This is final-program evidence for a **one-second scheduled P66 ROD computation task** in LUMINARY 099.

MIT/IL Apollo Project Memo 9-69 lists **PCR700A — Improve the Rate-of-Descent Mode (P66) Performance** and states that it is a clarifying rewrite of PCR700, with the action already assigned. This is the primary crosswalk previously missing from the project: PCR-700A is the clarified rewrite of PCR-700, not an unrelated later P66 change.

The crosswalk explains why Apollo 11-effective Section 2 Revision 4 names PCR-700 while the recovered Section 5 Revision 5 control index names PCR-700A under the same title. It does not prove that every Section 5 Revision 5 equation page is Apollo 11-effective.

A focused closure challenge then searched specifically for the missing LUMINARY 1A programmed-equation/effectivity discriminator rather than repeating broad P66 searches. The strongest accessible primary result was MSC Internal Note `69-FS-4`, whose page-change record states that it is a **complete re-issue of MSC Internal Note 69-FS-3**, titled *Programmed Guidance Equations for LUMINARY 1A Manned LM Earth Orbital and Lunar Program*, dated May 1969, updated for LUMINARY 1B. This directly confirms the identity, date, and predecessor relationship of the missing `69-FS-3`, but does not expose enough 1A→1B change control to promote the later 1B descriptive equations backward into Apollo 11.

The closure challenge therefore changes no implementation conclusion. It strengthens the provenance of the missing preferred source while preserving the effectivity boundary.

## Important boundary

The code proves the scheduling interval of the P66 `RODTASK`/`RODCOMP` path. It does **not** by itself prove a one-second DSKY refresh, telemetry/downlink cadence, MCC display refresh, or controller-facing product. `HDOTDISP` being updated within the one-second computation path establishes the variable-update path, not the separate display-service timing seen by the crew.

The PCR-700A memo establishes change-control identity/ancestry. It does not remove the separate need to establish Section 5 page effectivity before using descriptive equations as Apollo 11 equations. `69-FS-4` is explicitly a later LUMINARY 1B update of `69-FS-3`; without controlled unchanged ancestry its equations remain comparison evidence.

## Research closure

- **Status:** SUFFICIENT for the current implementation dependency.
- **Bounded question:** Apollo 11 LUMINARY 099 P66 ROD computation cadence and PCR-700/PCR-700A identity/ancestry.
- **Implementation dependency:** historical support for any model use of P66 ROD computation timing and the PCR-700 lag-compensation lineage.
- **Decision sensitivity:** a different final cadence or unrelated PCR-700A lineage would require revising the historical model boundary; neither occurred.
- **Decision-relevant findings:** LUMINARY 099 schedules `RODTASK` at `1SEC`; Apollo Project Memo 9-69 makes PCR-700A a clarifying rewrite of PCR-700.
- **Remaining gaps and disposition:** complete Section 5 Revision 5 P63–P66 page ancestry/effectivity and direct `69-FS-3` recovery are **DEFERRED** because no current player-visible, station-visible, causal-model, or validation dependency requires those descriptive pages. Crew-visible Noun 63 timing and station-visible timing are separate deferred questions until a feature names those dependencies.
- **Closure challenge:** targeted primary-source searches recovered `69-FS-4`'s explicit statement that it completely re-issued May 1969 `69-FS-3` and updated it for LUMINARY 1B. This did not contradict the final-program cadence or PCR crosswalk and did not establish safe back-projection of later equations.
- **Reopen triggers:** direct recovery of `69-FS-3` or Apollo-11-effective Section 5 pages; contradictory mission-specific primary evidence; implementation requiring exact descriptive P63–P66 equations; crew-visible Noun 63 service timing; or a station product requiring a sourced LGC→downlink→ground-display cadence.

No station maturity changes. No controller-facing cadence is promoted.

## Sources

- MIT/IL LUMINARY 099 assembly listing, `LUNAR_LANDING_GUIDANCE_EQUATIONS.agc`: https://www.ibiblio.org/apollo/listings/Luminary099/LUNAR_LANDING_GUIDANCE_EQUATIONS.agc.html
- MIT/IL Apollo Project Memo 9-69, *Results of the 29th Apollo Software Configuration Control Board Meeting*: https://www.ibiblio.org/apollo/Documents/Memo-SCB29_text.pdf
- MIT/IL LUMINARY Memo #73, *LUMINARY Revisions 80-92*, 26 Mar 1969: https://www.ibiblio.org/apollo/Documents/LUM73.pdf
- `SNA-8-D-027(II) REV 1`, LM Data Book Volume II, Mission G LUMINARY 99 prelaunch erasable load: https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- MSC Internal Note `69-FS-4`, *Programmed Guidance Equations for LUMINARY 1B Manned LM Earth Orbital and Lunar Program*: https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf

## Evidence status

- **DOCUMENTED:** LUMINARY 099 `P66VERTA` schedules `RODTASK` with `1SEC`.
- **DOCUMENTED:** `RODTASK` dispatches `RODCOMP`, which updates `VDGVERT` and performs the P66 rate-of-descent computation path.
- **DOCUMENTED:** `RODCOMP` updates `HDOTDISP` and consumes `LAG/TAU` in the P66 calculation.
- **DOCUMENTED:** MIT/IL Apollo Project Memo 9-69 identifies PCR-700A as a clarifying rewrite of PCR-700 under the same P66-performance title.
- **DOCUMENTED:** `69-FS-4` identifies May 1969 `69-FS-3` as its LUMINARY 1A predecessor and states that `69-FS-4` is a complete re-issue updated for LUMINARY 1B.
- **UNRESOLVED / DEFERRED:** complete Apollo 11 Section 5 descriptive-equation page ancestry/effectivity and direct `69-FS-3` contents.
- **UNRESOLVED / DEFERRED pending a named dependency:** crew-visible Noun 63 refresh cadence and controller-facing cadence/product implications.