# Research note 403 — Apollo 11 P66 later-equation boundary

Date: 2026-09-19
Research thread: `apollo11-p66-pcr700`
Status: **Later controlled equation state recovered; Apollo 11 page ancestry still open**

## Question

Can surviving primary equation documentation close, or further constrain, the missing Apollo 11 Section 5 Revision-5 P66 page state?

## Primary evidence

MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B*, is a controlled later program-equation source. Its P66-related variable definitions explicitly include `VBIAS` as a velocity-bias factor for P66 rate-of-descent computations, `VDGVERT` as the desired vertical velocity altered by astronaut commands during manual descent control, and `WCHVERT = 0` as the P66 final-descent guidance state. This confirms that a detailed programmed-equation description of the P66 implementation survives in the immediate post-Apollo-11 LUMINARY 1B documentation.

The R-567 Section 5 cumulative history independently identifies PCR-700A, *Improve the Rate of Descent Mode (P66) Performance*, as incorporated in Revision 5. The later Revision-8 control sheet is explicitly for LUMINARY 1C and identifies later P66 changes, notably PCR-988 (*Auto P66*) and PCR-1013 (*Multiple Servicers Avoidance in P66*), with affected page ranges in Section 5.3. This proves that later surviving P66 pages are not safe wholesale substitutes for the missing Apollo 11 state: later P66-specific changes altered the controlled page set.

The Revision-8 sheet also states that complete page blocks were republished for convenience even where individual pages had no changes. Therefore mere survival of a page inside a later revision is not, by itself, evidence of when its content entered the control document.

## Consequence

`69-FS-4` is now a useful **comparison endpoint**, not an Apollo 11 substitute. It can be used after Apollo 11-effective material is recovered to identify candidate unchanged behavior, terminology, and variables, but no 1B equation or cadence is back-projected into LUMINARY 99 without a page/change ancestry.

The primary retrieval target remains Section 5 Revision 5 P63-P66 pages or `69-FS-3`. Page-level ancestry must account for later P66 changes before any surviving Revision-8/1B text is used for Apollo 11.

No executable or station-facing behavior changes.

## Sources

- MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B*: https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf
- MIT/IL `R-567`, Section 5 Revision 8, front matter/change pages: https://www.ibiblio.org/apollo/NARA-SW/R-567-sec5-rev8-5.1-5.2.pdf
- MIT/IL `R-567`, Section 5 Revision 11 cumulative historical front matter: https://www.ibiblio.org/apollo/Documents/j2-80-R-567-SEC5-REV11_text.pdf

## Evidence status

- **DOCUMENTED:** `69-FS-4` contains explicit P66 rate-of-descent variable/state definitions for LUMINARY 1B.
- **DOCUMENTED:** the Section 5 Revision-5 historical index includes PCR-700A.
- **DOCUMENTED:** Revision 8 is explicitly LUMINARY 1C and includes later P66-specific PCR-988 and PCR-1013 page changes.
- **DOCUMENTED:** Revision 8 republishes some unchanged pages for convenience, so inclusion in the later artifact does not establish change origin.
- **UNRESOLVED:** Apollo 11-effective Section 5 Revision-5 P63-P66 page text, page-level ancestry into later revisions, exact Apollo 11 P66 cadence/equations, primary PCR-700/PCR-700A crosswalk, and `69-FS-3` retrieval.