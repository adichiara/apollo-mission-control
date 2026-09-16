# Roadmap — PC+2 GDA trim next targets

Date: 2026-09-16

Research Notes 180–193 separate commanded trim, powered-flight behavior, actuator state/telemetry, post-free-return reference handling, RTCC/RTACF mass-property processing, and preflight-versus-real-time source authority.

Note 190 identified Volume III as the current-official mass-properties authority. Note 191 recovered the late-preflight source state **SNA-8-D-027(III) Rev. 2, Amendment 79, dated 30 March 1970**. Note 193 now directly recovers the LM-7 effective sequential mass-properties pages: they are headed **Table 3.3-3**, with weight, c.g., inertia, product-of-inertia, and dispersion fields. A legible `LM PRE P.D.I.` row gives **33,980.1 lb**, X c.g. **188.1 in**, Y approximately **-0.0 in**, Z **-0.8 in**.

Important source-control correction: Amendment 79 Table 3.3-8 says it is to be used with `LM sequential mass properties Table 3-3.2`, but the recovered LM-7 sequential pages are Table **3.3-3**; Table 3.3-2 in the same document is CSM 109. Preserve this as an unresolved internal cross-reference inconsistency rather than silently calling the LM table 3-3.2 or asserting why the mismatch exists.

Note 192's independent constraint remains separate: the Apollo 13 Review Board reports **33,941 lb at CSM/LM separation**, versus **33,872.3 lbm** in the 17 March analysis-specific source. Neither may be substituted for the recovered pre-PDI row, CONTROL's unknown input, or T+55.

## Priority 1 — mission-specific ground-computation lineage

Recover an Apollo 13 artifact bridging:

`T+55 LM-burn mass-properties deck -> weight/c.g. product -> specific RTCC/RTACF request/run -> trim output -> 5.86 / 6.75`

Best targets remain weight/c.g. sheets, RTCC/RTACF request/output, job/run records, controller working papers, or support-room products.

## Priority 2 — CONTROL premission source and disagreement

Determine whether CONTROL actually selected the now-recovered **LM-7 Amendment 79 / Table 3.3-3** model or another premission set. Recover CONTROL's competing numerical trim, exact state/input row, and comparison/acceptance basis.

Do not equate `official available preflight` with `selected by CONTROL`. Do not substitute the 17 March analysis value, Review Board's 33,941-lb mission-summary value, or Table 3.3-3 pre-PDI value for CONTROL absent provenance evidence.

## Priority 3 — complete LM-7 sequential-table capture

Recover the opening page(s) and remaining relevant rows of Table 3.3-3 plus amendment/revision markings needed to reconstruct the full official LM-7 sequential state series. Preserve the Table 3.3-8 `3-3.2` cross-reference verbatim until its cause can be established from source evidence.

## Priority 4 — LM-7 telemetry calibration / trim representation

Continue seeking LM-7 instrumentation/PCM calibration mapping GH1313V/GH1314V to engineering degrees and polarity, plus the primary definition of the crew-facing GDA trim-number zero/reference.

## Modeling rule

Represent `analysis_specific`, `official_available_preflight_lm7_sequential`, `mission_summary`, `controller_selected_source`, and `realtime_updated` separately. Record the recovered official sequential source as `SNA-8-D-027(III) Rev 2 / Amendment 79 / Table 3.3-3 / 1970-03-30`, with `controller_selected = unknown`.

Use `5.86 / 6.75` only as the sourced commanded/preburn reference in the ~59/61:29 chain; `5.85 / 6.74` remains the later ground-issued PC+2 reference with no-action disposition. Do not infer the missing T+55 consumption edge or CONTROL alternative.