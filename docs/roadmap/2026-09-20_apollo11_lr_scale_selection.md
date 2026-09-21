# Apollo 11 landing-radar scale-selection roadmap update

Date: 2026-09-20
Updated: 2026-09-21
Parent: `docs/roadmap/2026-09-19_apollo11_landing_radar_beam_transform.md`

## Newly closed boundary

Flown LUMINARY 099 explicitly distinguishes landing-radar altitude high/low scale. `SERVICER.agc` tests `ALTSCBIT`; its high-scale branch bypasses the low-scale rescaling operation, while the low-scale path applies `SKALSKAL`. `ERASABLE_ASSIGNMENTS.agc` defines `SKALSKAL` as an LR altitude scale-factor ratio with `.2 NOM`; `CONTROLLED_CONSTANTS.agc` independently defines `HSCAL` as converting the documented `1.079 ft/bit` representation into the estimator's internal metric scaling.

The Apollo 11 LUMINARY 99 prelaunch pad-load document lists `SKALSKAL` at address 1356 with octal `00000`, and `RADSKAL` at addresses 1354–1355 with `00000,00000`. The flown LUMINARY 099 assembled symbol table independently confirms `SKALSKAL` at erasable address 1356. Earlier repository references to addresses 3461/3462 and the spelling `RADSCALE` were transcription errors and are withdrawn.

MIT Instrumentation Laboratory LUMINARY Memo #85 (21 May 1969), written specifically for Revision 99 / PCR 775, now resolves the apparent zero-load contradiction. It defines the landing-radar high/low scale-factor ratio `SFR = 5` and `SKALSKAL = 1/SFR = 0.2`, scaled B-0. For R12/software Doppler compensation it prescribes `RADSKAL` 1354–1355 = octal `00023,37462` and `SKALSKAL` 1356 = octal `06315`; if the landing radar performs Doppler compensation, all three registers are to be zero. The Apollo 11 prelaunch load's three zero words therefore have an explicit Revision-99 meaning: the mission load selected radar-performed rather than R12-performed slant-range Doppler compensation. The zero is not evidence that the physical altitude scale ratio was zero.

Memo #85 also supplies Apollo-11-effective scale-ratio evidence directly: `SFR = High Scale Factor / Low Scale Factor = 5`, hence low/high = 0.2. This supersedes the need to rely on Luminary 1B merely to establish the ratio. MSC-69-FS-4 remains useful adjacent-version corroboration for the explicit 1.0790 and 5.3950 ft/count values; direct LM-5 evidence for the absolute high-scale count value is still desirable.

Primary interface documentation independently bounds the physical scale transition. AC Electronics ND-1021042 identifies an LR-originated `Range low scale factor` discrete issued automatically at approximately 2,500 ft, plus digital LR data pulses under LGC readout/strobe/reset control. The LM-6 Apollo Operations Handbook preserves the same ~2,500-ft automatic scale transition and documents conversion/counting into a 15-bit serial LGC transfer.

## Next work

1. Seek Apollo-11/LM-5-effective hardware or Luminary 1A documentation directly confirming the absolute 5.3950 ft/count high-scale LR altitude conversion; the 5:1 high/low ratio itself is now directly documented for Revision 99.
2. Continue seeking LM-5 hardware-interface evidence for serial word sign/bias/framing and rounding/truncation.
3. Determine whether PCR 775 / the zero mission load has any player-visible MCC/GUIDO consequence; do not infer one from onboard implementation alone.
4. Continue the parallel Apollo-11 MSK-1137 per-field provenance and GUIDO workflow thread.
5. Keep historical stochastic LR measurement generation **BLOCKED** pending flight-effective residual/distribution evidence.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** high/low LR altitude scale selection and conditional software rescaling; low-scale stored representation 1.079 ft/count.
- **DOCUMENTED, REVISION-99 PRIMARY:** LUMINARY Memo #85 defines `SFR = 5`, `SKALSKAL = 0.2`, the nonzero R12-compensation pad values, and zero in all three registers when the radar performs Doppler compensation.
- **RESOLVED, APOLLO-11 PRELAUNCH LOAD:** `SKALSKAL` 1356 = `00000` and `RADSKAL` 1354–1355 = `00000,00000` select radar-performed Doppler compensation under the Revision-99 PCR-775 scheme; they do not define a zero scale ratio.
- **DOCUMENTED, APOLLO-11-EFFECTIVE SYMBOL TABLE:** `SKALSKAL` = erasable address 1356.
- **CORRECTED:** prior 3461/3462 address references and `RADSCALE` spelling were repository transcription errors.
- **DOCUMENTED, PRIMARY INTERFACE / STRONG CONTINUITY:** LR-originated automatic low-scale indication near 2,500 ft and digital pulse/strobe transfer architecture are documented before Apollo 11 and preserved immediately afterward; later handbook specifies 15-bit serial transfer.
- **DOCUMENTED, NEAR-MISSION LUMINARY 1B:** LR altitude = 1.0790 ft/count low scale and 5.3950 ft/count high scale; ratio = 0.2.
- **UNRESOLVED:** direct Apollo-11-effective absolute 5.3950-ft/count confirmation; complete raw serial sign/bias/framing and rounding; controller-visible consequences.
- **BLOCKED:** stochastic historical LR error generator.
