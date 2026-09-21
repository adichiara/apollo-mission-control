# Station research status — Apollo 11 LR scale selection

Date: 2026-09-20
Updated: 2026-09-21
Parent: `docs/station-status/2026-09-19_apollo11_landing_radar_beam_transform.md`

## GUIDO / guidance-monitoring consequence

Flown LUMINARY 099 establishes that the onboard landing-radar altitude path explicitly tracked high/low scale state and conditionally rescaled the low-scale path before the altitude residual/update logic. The Apollo 11 LUMINARY 99 prelaunch pad-load table records `SKALSKAL` at erasable address 1356 as octal `00000`; `RADSKAL` occupies 1354–1355 and is also zero. Earlier repository references to 3461/3462 and `RADSCALE` were transcription errors and have been corrected.

MIT Instrumentation Laboratory LUMINARY Memo #85 (21 May 1969) resolves the zero-load semantics directly for Revision 99 / PCR 775. It defines the landing-radar scale-factor ratio `SFR = High Scale Factor / Low Scale Factor = 5` and `SKALSKAL = 1/SFR = 0.2`. To have R12 perform slant-range Doppler compensation, the memo prescribes `RADSKAL = 00023,37462` and `SKALSKAL = 06315`; if the landing radar performs the compensation, all three registers are set to zero. Thus Apollo 11's zero prelaunch values select radar-performed Doppler compensation in this scheme; they are not a zero physical scale ratio.

The absolute high-scale conversion is bounded without importing a later mission configuration. Flown LUMINARY 099 documents 1.079 ft/count for the low-scale representation, and Revision-99 Memo #85 documents a high/low scale-factor ratio of 5. Their direct arithmetic consequence is 5.395 ft/count high scale. MSC-69-FS-4 independently prints 5.3950 ft/count and therefore corroborates rather than supplies the Apollo-11-effective derivation.

The MIT/IL *LEM PGNCS Guidance System Operations Plan*, Section 3, identifies two LR-to-LGC binary data-flow inputs, `LR in "1"` and `LR in "0"`, separately from LR validity, antenna-position, and range-low-scale discretes. AC Electronics ND-1021042 identifies the complementary LGC outputs: `Readout command`, a continuous 3,200-cps `Gate reset`, and distinct range/Vx/Vy/Vz strobe pulses enabling LR transfer gates. Together these primary sources establish a useful framing boundary: binary value transfer is separate from LGC-controlled quantity selection/timing.

Flown LUMINARY 099 now closes the software-side quantity-select mapping as well. In `P20-P25.agc`, the radar lead-ins invoke `INITREAD` with octal `14` for `LRVELX`, `15` for `LRVELY`, `16` for `LRVELZ`, and `17` for `LRALT`. These are Apollo-11-effective read-selection commands, not evidence for the numeric encoding of the returned serial data. Bit order, sign convention, integer bias, raw word length, and rounding/truncation therefore remain unresolved.

The LM-6 Apollo Operations Handbook preserves that architecture immediately after Apollo 11 and specifies a 15-bit serial transfer path. Its 15-bit detail remains adjacent-effectivity corroboration, not a silently back-projected LM-5 fact.

No recovered source establishes that `ALTSCBIT`, the raw scale discrete, PCR-775 compensation selection, `SKALSKAL`, transfer strobes, or the rescaling operation was exposed directly to GUIDO, CONTROL, or FLIGHT. No station display, alarm, callout, or procedure is added from this evidence.

## Player-facing boundary

A spacecraft model may preserve LR altitude scale state internally, use 1.079 ft/count low scale and the directly derived 5.395 ft/count high scale, encode the Apollo 11 mission load as selecting radar-performed slant-range Doppler compensation, and preserve the flown LGC quantity-selection mapping (`Vx/Vy/Vz/range` = octal `14/15/16/17`). These are onboard/interface facts; they do not establish a controller-visible control or the unresolved raw numerical coding. Do not present 2,500 ft as an exact invariant Apollo-11 switching altitude.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD LOGIC:** `ALTSCBIT` selects high/low LR altitude treatment; low scale invokes `SKALSKAL` rescaling.
- **DOCUMENTED, APOLLO-11-EFFECTIVE LOW SCALE:** 1.079 ft/count stored representation.
- **DOCUMENTED, REVISION-99 PRIMARY:** Memo #85 gives high/low scale-factor ratio 5, `SKALSKAL = 0.2`, and the PCR-775 compensation-selection pad values.
- **DERIVED, APOLLO-11-EFFECTIVE HIGH SCALE:** 5.395 ft/count = 1.079 ft/count × 5; independently corroborated by the 5.3950-ft/count Luminary 1B value.
- **RESOLVED, APOLLO-11 PRELAUNCH LOAD:** zero `RADSKAL`/`SKALSKAL` means radar-performed Doppler compensation under the documented Revision-99 scheme.
- **DOCUMENTED INTERFACE:** LR uses separate `LR in "1"`/`LR in "0"` binary data flow and LGC-controlled readout/reset/range/Vx/Vy/Vz strobes.
- **DOCUMENTED, APOLLO-11-EFFECTIVE QUANTITY SELECTION:** `LRVELX=14`, `LRVELY=15`, `LRVELZ=16`, `LRALT=17` (octal) at the flown LUMINARY 099 `INITREAD` boundary.
- **ADJACENT EFFECTIVITY:** LM-6 explicitly documents 15-bit serial transfer; do not promote that word length to LM-5 without an applicability bridge.
- **NO STATION MATURITY CHANGE:** controller visibility/routing remains unestablished.
- **UNRESOLVED:** LM-5 raw word length, bit order, sign/bias, rounding/truncation, and controller-visible compensation/scale-state consequences.
