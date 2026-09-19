# Research note 404 — Apollo 11 P66 flight-listing cadence

Date: 2026-09-19
Research thread: `apollo11-p66-pcr700`
Status: **Apollo 11 P66 ROD computation cadence directly recovered; PCR-700/700A crosswalk recovered**

## Question

Did the January 1969 PCR-700 proposal's once-per-second P66 rate-of-descent computation survive into the Apollo 11 LUMINARY 99 implementation, and what is the relationship between PCR-700 and the Section 5 PCR-700A identifier?

## Primary evidence

The surviving LUMINARY 099 assembly listing provides direct program evidence in `LUNAR_LANDING_GUIDANCE_EQUATIONS.agc`.

In the P66 guidance path, `P66VERT` posts `P66VERTA`. `P66VERTA` terminates phase group 3 and then loads the constant `1SEC`, calls `TWIDDLE`, and supplies `RODTASK` as the scheduled task address. `RODTASK` in turn obtains a VAC area for `RODCOMP`. `RODCOMP` updates `VDGVERT` from `RODCOUNT * RODSCAL1`, then performs the P66 computation path. The same routine updates `HDOTDISP` for Noun 63 and later uses `LAG/TAU`, `MAXFORCE`, and `MINFORCE` in the acceleration-command calculation.

This is final-program evidence for a **one-second scheduled P66 ROD computation task** in LUMINARY 099. It closes the earlier boundary that treated the January SCB one-second computation detail as proposal/change-intent only.

A second primary MIT/IL configuration-control record now closes the PCR-number crosswalk. Apollo Project Memo 9-69, reporting the 29th Apollo Software Configuration Control Board meeting, lists **PCR700A — Improve the Rate-of-Descent Mode (P66) Performance** and states: **“This is just a clarifying re-write of PCR700. The action has already been assigned.”** The same memo discusses the lag-compensation idea being implemented by Craig Schulenberg. This is the primary crosswalk previously missing from the project: PCR-700A is the clarified rewrite of PCR-700, not an unrelated later P66 change.

That crosswalk also explains why Apollo 11-effective Section 2 Revision 4 names PCR-700 while the recovered Section 5 Revision 5 control index names PCR-700A under the same title. It does not, by itself, prove that every Section 5 Revision 5 equation page is Apollo 11-effective; section-specific revision/effectivity controls still apply.

## Important boundary

The code proves the scheduling interval of the P66 `RODTASK`/`RODCOMP` path. It does **not** by itself prove:

- a one-second DSKY refresh or visible Noun 63 display cadence;
- a one-second telemetry/downlink cadence;
- a one-second MCC display refresh;
- a new GUIDO, CONTROL, FLIGHT, or other controller-facing product;
- that every descriptive equation in a later LUMINARY 1B/1C GSOP page is unchanged from Apollo 11.

`HDOTDISP` being updated within the one-second computation path establishes the variable-update path, not the separate display-service timing seen by the crew.

The PCR-700A memo establishes change-control identity/ancestry. It does not remove the separate need to establish Section 5 page effectivity before using descriptive equations as Apollo 11 equations.

## Consequence

The exact Apollo 11 P66 ROD **computation cadence** is no longer unresolved: it is one second. The primary PCR-700/PCR-700A crosswalk is also no longer unresolved. The remaining equation-document research is narrowed to Section 5 Revision 5 descriptive equation/page ancestry/effectivity and `69-FS-3` recovery. Crew-visible Noun 63 timing and station-visible timing remain separate dependency-triggered questions.

No station maturity changes. No controller-facing cadence is promoted.

## Sources

- MIT/IL LUMINARY 099 assembly listing, `LUNAR_LANDING_GUIDANCE_EQUATIONS.agc`: https://www.ibiblio.org/apollo/listings/Luminary099/LUNAR_LANDING_GUIDANCE_EQUATIONS.agc.html
- MIT/IL Apollo Project Memo 9-69, *Results of the 29th Apollo Software Configuration Control Board Meeting*: https://www.ibiblio.org/apollo/Documents/Memo-SCB29_text.pdf
- MIT/IL LUMINARY Memo #73, *LUMINARY Revisions 80-92*, 26 Mar 1969: https://www.ibiblio.org/apollo/Documents/LUM73.pdf
- `SNA-8-D-027(II) REV 1`, LM Data Book Volume II, Mission G LUMINARY 99 prelaunch erasable load: https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf

## Evidence status

- **DOCUMENTED:** LUMINARY 099 `P66VERTA` schedules `RODTASK` with `1SEC`.
- **DOCUMENTED:** `RODTASK` dispatches `RODCOMP`, which updates `VDGVERT` and performs the P66 rate-of-descent computation path.
- **DOCUMENTED:** `RODCOMP` updates `HDOTDISP` and consumes `LAG/TAU` in the P66 calculation.
- **DOCUMENTED:** MIT/IL Apollo Project Memo 9-69 identifies PCR-700A as a clarifying rewrite of PCR-700 under the same P66-performance title.
- **UNRESOLVED:** crew-visible Noun 63 refresh cadence, controller-facing cadence/product implications, complete Apollo 11 Section 5 descriptive-equation page ancestry/effectivity, and `69-FS-3` retrieval.