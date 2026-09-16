# Roadmap — PC+2 GDA trim next targets

Date: 2026-09-16

Research Notes 180–191 separate commanded trim, powered-flight behavior, actuator state/telemetry, post-free-return reference handling, RTCC/RTACF mass-property processing, and preflight-versus-real-time source authority.

Note 190 identified Volume III as the current-official mass-properties authority. Note 191 now recovers the applicable late-preflight source state: **SNA-8-D-027(III) Rev. 2, LM-7 Amendment 79, dated 30 March 1970**. Its Table 3.3-8 is an LM-7 consumables change summary explicitly used with `LM sequential mass properties Table 3-3.2`; the amendment stream also contains LM-7 propellant-loading uncertainties. This proves an Apollo-13-specific sequential mass-properties/consumables set existed twelve days before launch. It does not prove CONTROL selected it.

## Priority 1 — mission-specific ground-computation lineage

Recover an Apollo 13 artifact bridging:

`T+55 LM-burn mass-properties deck -> weight/c.g. product -> specific RTCC/RTACF request/run -> trim output -> 5.86 / 6.75`

Best targets remain weight/c.g. sheets, RTCC/RTACF request/output, job/run records, controller working papers, or support-room products.

## Priority 2 — CONTROL premission source and disagreement

Recover **LM-7 Table 3-3.2 at Amendment 79/current state**, including separation/docked weight and c.g. values and amendment markings. Then seek evidence identifying which premission set CONTROL actually used, CONTROL's competing numerical trim, and the actual comparison/acceptance basis.

Do not equate `official available preflight` with `selected by CONTROL`. Do not substitute Volume II analysis values or Volume III values for CONTROL absent selection evidence.

## Priority 3 — LM-7 telemetry calibration / trim representation

Continue seeking LM-7 instrumentation/PCM calibration mapping GH1313V/GH1314V to engineering degrees and polarity, plus the primary definition of the crew-facing GDA trim-number zero/reference.

## Modeling rule

Represent `official_available_preflight`, `controller_selected_source`, and `realtime_updated` separately. Record the recovered official source as `SNA-8-D-027(III) Rev 2 / Amendment 79 / 1970-03-30 / LM-7`, with `controller_selected = unknown`.

Use `5.86 / 6.75` only as the sourced commanded/preburn reference in the ~59/61:29 chain; `5.85 / 6.74` remains the later ground-issued PC+2 reference with no-action disposition. Do not infer the missing T+55 consumption edge or CONTROL alternative.