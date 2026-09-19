# Research note 333 — Apollo 11 P66 flight-listing cadence

Date: 2026-09-19
Status: **Apollo 11 P66 ROD computation cadence directly recovered from LUMINARY 099 listing**

## Question

Did the January 1969 PCR-700 proposal's once-per-second P66 rate-of-descent computation survive into the Apollo 11 LUMINARY 99 implementation?

## Primary evidence

The surviving LUMINARY 099 assembly listing provides direct program evidence in `LUNAR_LANDING_GUIDANCE_EQUATIONS.agc`.

In the P66 guidance path, `P66VERT` posts `P66VERTA`. `P66VERTA` terminates phase group 3 and then loads the constant `1SEC`, calls `TWIDDLE`, and supplies `RODTASK` as the scheduled task address. `RODTASK` in turn obtains a VAC area for `RODCOMP`. `RODCOMP` updates `VDGVERT` from `RODCOUNT * RODSCAL1`, then performs the P66 computation path. The same routine updates `HDOTDISP` for Noun 63 and later uses `LAG/TAU`, `MAXFORCE`, and `MINFORCE` in the acceleration-command calculation.

This is final-program evidence for a **one-second scheduled P66 ROD computation task** in LUMINARY 099. It closes the earlier boundary that treated the January SCB one-second computation detail as proposal/change-intent only.

The listing also directly confirms that the implemented P66 path contains the PCR-700 lineage already established independently by LUMINARY Memo #73 and the LM-5 Mission G erasable-load document: `LAG/TAU` is consumed in the P66 calculation, and `HDOTDISP` is updated inside `RODCOMP`.

## Important boundary

The code proves the scheduling interval of the P66 `RODTASK`/`RODCOMP` path. It does **not** by itself prove:

- a one-second DSKY refresh or visible Noun 63 display cadence;
- a one-second telemetry/downlink cadence;
- a one-second MCC display refresh;
- a new GUIDO, CONTROL, FLIGHT, or other controller-facing product;
- that every descriptive equation in a later LUMINARY 1B/1C GSOP page is unchanged from Apollo 11.

`HDOTDISP` being updated within the one-second computation path establishes the variable-update path, not the separate display-service timing seen by the crew.

## Consequence

The exact Apollo 11 P66 ROD **computation cadence** is no longer unresolved: it is one second. The remaining equation-document research can narrow to descriptive equation ancestry/effectivity, PCR-700/PCR-700A change-control wording, and any station-visible dependency. `69-FS-3` and Section 5 Revision 5 remain valuable archival targets, but they are no longer required to establish the P66 ROD computation interval.

No station maturity changes. No controller-facing cadence is promoted.

## Sources

- MIT/IL LUMINARY 099 assembly listing, `LUNAR_LANDING_GUIDANCE_EQUATIONS.agc`: https://www.ibiblio.org/apollo/listings/Luminary099/LUNAR_LANDING_GUIDANCE_EQUATIONS.agc.html
- MIT/IL LUMINARY Memo #73, *LUMINARY Revisions 80-92*, 26 Mar 1969: https://www.ibiblio.org/apollo/Documents/LUM73.pdf
- `SNA-8-D-027(II) REV 1`, LM Data Book Volume II, Mission G LUMINARY 99 prelaunch erasable load: https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf

## Evidence status

- **DOCUMENTED:** LUMINARY 099 `P66VERTA` schedules `RODTASK` with `1SEC`.
- **DOCUMENTED:** `RODTASK` dispatches `RODCOMP`, which updates `VDGVERT` and performs the P66 rate-of-descent computation path.
- **DOCUMENTED:** `RODCOMP` updates `HDOTDISP` and consumes `LAG/TAU` in the P66 calculation.
- **UNRESOLVED:** crew-visible Noun 63 refresh cadence, controller-facing cadence/product implications, complete Apollo 11 Section 5 descriptive-equation page ancestry, primary PCR-700/PCR-700A crosswalk, and `69-FS-3` retrieval.