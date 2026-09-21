# Station research status — Apollo 11 LR scale selection

Date: 2026-09-20
Updated: 2026-09-21
Parent: `docs/station-status/2026-09-19_apollo11_landing_radar_beam_transform.md`

## GUIDO / guidance-monitoring consequence

Flown LUMINARY 099 establishes that the onboard landing-radar altitude path explicitly tracked high/low scale state and conditionally rescaled the low-scale path before the altitude residual/update logic. The Apollo 11 LUMINARY 99 prelaunch pad-load table records `SKALSKAL` at erasable address 1356 as octal `00000`; `RADSKAL` occupies 1354–1355 and is also zero. Earlier repository references to 3461/3462 and `RADSCALE` were transcription errors and have been corrected.

MIT Instrumentation Laboratory LUMINARY Memo #85 (21 May 1969) resolves the zero-load semantics directly for Revision 99 / PCR 775. It defines the landing-radar scale-factor ratio `SFR = High Scale Factor / Low Scale Factor = 5` and `SKALSKAL = 1/SFR = 0.2`. To have R12 perform slant-range Doppler compensation, the memo prescribes `RADSKAL = 00023,37462` and `SKALSKAL = 06315`; if the landing radar performs the compensation, all three registers are set to zero. Thus Apollo 11's zero prelaunch values select radar-performed Doppler compensation in this scheme; they are not a zero physical scale ratio.

MSC-69-FS-4, the primary MIT/MSC programmed-guidance-equations document for Luminary 1B, gives LR altitude count values of 1.0790 ft low scale and 5.3950 ft high scale. Memo #85 now directly establishes the 5:1 high/low ratio for Revision 99, while the later document corroborates the corresponding absolute high-scale value. Direct LM-5 evidence for 5.3950 ft/count remains desirable before labeling that absolute value Apollo-11-effective.

AC Electronics ND-1021042 independently documents a radar-originated `Range low scale factor` discrete, automatically issued near 2,500 ft, and digital LR data pulses controlled by LGC readout/strobe/reset signals. The LM-6 Apollo Operations Handbook preserves that architecture immediately after Apollo 11 and specifies a 15-bit serial transfer path.

No recovered source establishes that `ALTSCBIT`, the raw scale discrete, PCR-775 compensation selection, `SKALSKAL`, or the rescaling operation was exposed directly to GUIDO, CONTROL, or FLIGHT. No station display, alarm, callout, or procedure is added from this evidence.

## Player-facing boundary

A spacecraft model may preserve LR altitude scale state internally and may encode the Apollo 11 mission load as selecting radar-performed slant-range Doppler compensation rather than R12 compensation. This is an onboard implementation state, not a controller-visible control unless MCC evidence establishes visibility or operational consequence. Do not present 2,500 ft as an exact invariant Apollo-11 switching altitude. The 5:1 high/low scale ratio is Revision-99 primary evidence; retain 5.3950 ft/count as a sourced candidate absolute high-scale conversion pending direct LM-5 confirmation.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD LOGIC:** `ALTSCBIT` selects high/low LR altitude treatment; low scale invokes `SKALSKAL` rescaling.
- **DOCUMENTED, APOLLO-11-EFFECTIVE LOW SCALE:** 1.079 ft/count stored representation.
- **DOCUMENTED, REVISION-99 PRIMARY:** Memo #85 gives high/low scale-factor ratio 5, `SKALSKAL = 0.2`, and the PCR-775 compensation-selection pad values.
- **RESOLVED, APOLLO-11 PRELAUNCH LOAD:** zero `RADSKAL`/`SKALSKAL` means radar-performed Doppler compensation under the documented Revision-99 scheme.
- **DOCUMENTED INTERFACE / STRONG CONTINUITY:** LR-originated automatic low-scale indication near 2,500 ft plus digital pulse/strobe transfer; 15-bit serial transfer explicitly documented immediately after Apollo 11.
- **DOCUMENTED, NEAR-MISSION LUMINARY 1B:** 1.0790 ft/count low scale; 5.3950 ft/count high scale; ratio 0.2.
- **NO STATION MATURITY CHANGE:** controller visibility/routing remains unestablished.
- **UNRESOLVED:** direct Apollo-11-effective absolute high-scale count value, raw serial sign/bias/framing, rounding/truncation, and controller-visible compensation/scale-state consequences.
