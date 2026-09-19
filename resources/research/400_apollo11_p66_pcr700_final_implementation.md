# Research note 400 — Apollo 11 P66 / PCR-700 final implementation boundary

Date: 2026-09-19
Research thread: `apollo11-p66-pcr700`
Status: **final implementation materially constrained; exact Section 5 equation text still unrecovered**

## Question

Did the P66 improvement described prospectively under PCR-700 survive into the Apollo 11 LUMINARY 1A / Rev. 099 configuration, and what can be admitted without inventing an exact controller-facing cadence or equation?

## Primary evidence

### LUMINARY Memo #73 — 26 March 1969

MIT Instrumentation Laboratory LUMINARY Memo #73, *LUMINARY Revisions 80-92*, records under the major changes incorporated into Revision 80 that **P66 was modified to allow for total lag in its control loop**. The memo says the compensation accounts for computation lag plus engine-response lag, introduces the pad-loaded parameter `LAG/TAU`, defines it as total lag divided by the existing `TAUROD`, and explicitly tags the change **PCR 700**.

This is implementation evidence, not merely SCB intent.

### Apollo 11 LM-5 Mission G erasable-load document

`SNA-8-D-027(II) REV 1`, LM Data Book Volume II, dated 11 June 1969, contains the Mission G prelaunch erasable load for **LUMINARY 99**. The table includes `LAG/TAU` at addresses 2542/2543 with decimal value **0.413333** and the associated octal representation.

This is mission/configuration evidence that the PCR-700 parameter existed in the Apollo 11 LUMINARY 99 load. It is stronger than projecting the January SCB proposal forward.

### LUMINARY Memo #85 — 21 May 1969

MIT/IL LUMINARY Memo #85, *LUMINARY Revision 99*, records Revision 99 as correcting anomaly LNY70 and implementing PCR 775. PCR 775 concerns landing-radar slant-range Doppler compensation. Memo #85 does not redefine PCR-700; it is useful as the controlled Rev. 99 change record, but absence of a PCR-700 mention is not independently proof of no intervening modification.

### LUMINARY 99 listing

The surviving/transcribed LUMINARY 99 listing exposes `LAG/TAU` in erasable assignments and uses it in the lunar-landing guidance code. This is implementation corroboration. Repository policy should continue to distinguish the digitized/transcribed listing from contemporaneous MIT/NASA paper records when describing provenance.

## What is now supported

The project may treat these as Apollo 11-effective facts:

1. PCR-700 was implemented by LUMINARY Revision 80 as a P66 control-loop lag-compensation change.
2. The implementation introduced `LAG/TAU` as a pad-loaded quantity tied to `TAUROD`.
3. The Apollo 11 LM-5 Mission G LUMINARY 99 erasable load contains `LAG/TAU = 0.413333`.
4. LUMINARY 99 code uses the `LAG/TAU` quantity in lunar-landing guidance.

## What is still not supported

Do **not** infer from this evidence alone:

- the exact final Section 5 P66 equation presentation;
- a one-second Apollo 11 DSKY HDOT update cadence;
- a one-second controller-facing product cadence;
- an MCC display or station product derived from P66 internals;
- a precise physical lag in seconds without the associated Apollo 11 `TAUROD` interpretation/value chain;
- that every detail in the January 1969 PCR-700 proposal survived unchanged.

The January SCB memo's proposed once-per-second ROD/command/display behavior therefore remains proposal/change-intent evidence until final implementation evidence is recovered for those details.

## Consequence for the active D-024 item

The P66/PCR-700 branch is no longer blocked on proving that the lag-compensation concept reached Apollo 11. It did. The remaining high-value gap is narrower: recover the LUMINARY 1A-effective R-567 Section 5 control/technical pages (or an equivalent controlled final equation source) before promoting exact P66 equations or cadence into the historical model.

No executable model change is justified by this note alone.

## Sources

- MIT/IL LUMINARY Memo #73, *LUMINARY Revisions 80-92*, 26 Mar 1969: https://www.ibiblio.org/apollo/Documents/LUM73.pdf
- MIT/IL LUMINARY Memo #85, *LUMINARY Revision 99*, 21 May 1969: https://www.ibiblio.org/apollo/Documents/LUM85_text.pdf
- `SNA-8-D-027(II) REV 1`, LM Data Book Volume II, Mission G prelaunch erasable load (LUMINARY 99), 11 Jun 1969: https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- LUMINARY 99 listing / erasable assignments and lunar-landing guidance, Virtual AGC transcription of the surviving program listing: https://www.ibiblio.org/apollo/listings/Luminary099/

## Evidence status

- **DOCUMENTED:** MIT/IL LUMINARY Memo #73 records that Revision 80 modified P66 for total control-loop lag, added the pad-loaded `LAG/TAU` parameter, and defines it as total lag divided by the existing `TAUROD` parameter under PCR-700.
- **DOCUMENTED:** the Apollo 11 LM-5 Mission G prelaunch erasable-load table is explicitly for LUMINARY 99 and lists `LAG/TAU` at addresses 2542/2543 with value 0.413333.
- **DOCUMENTED:** the LUMINARY 099 listing identifies `LAG/TAU` as the P66 lag-time / `TAUROD` quantity and consumes it in the lunar-landing guidance computation.
- **PARTIALLY DOCUMENTED:** these sources establish Apollo 11-effective presence and use of the lag-compensation parameter, but do not by themselves establish the exact flight-effective Section 5 descriptive equation set or any controller-facing cadence.
- **UNRESOLVED:** exact Apollo 11-effective Section 5 P66 equation text, crew-visible refresh cadence, controller-facing product cadence, and any station-product consequence not separately sourced.
