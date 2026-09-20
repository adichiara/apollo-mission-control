# Apollo 11 landing-radar scale-selection roadmap update

Date: 2026-09-20
Parent: `docs/roadmap/2026-09-19_apollo11_landing_radar_beam_transform.md`

## Newly closed boundary

Flown LUMINARY 099 explicitly distinguishes landing-radar altitude high/low scale. `SERVICER.agc` tests `ALTSCBIT`; its high-scale branch bypasses the low-scale rescaling operation, while the low-scale path applies `SKALSKAL`. `ERASABLE_ASSIGNMENTS.agc` defines `SKALSKAL` as an LR altitude scale-factor ratio with `.2 NOM`; `CONTROLLED_CONSTANTS.agc` independently defines `HSCAL` as converting the documented `1.079 ft/bit` representation into the estimator's internal metric scaling.

The Apollo 11 LUMINARY 99 prelaunch pad-load document lists `SKALSKAL` at address 3462 with octal `00000`, and `RADSCALE` at 3461 likewise `00000`. This is mission-specific pad-load evidence, but its zero entry still requires interpretation before it can be treated as the run-time scale factor.

A near-mission primary MIT/MSC guidance-equations source, MSC-69-FS-4 (Luminary 1B), supplies the missing scale semantics explicitly: `DNLRALT` is 1.0790 ft/count on low scale and 5.3950 ft/count on high scale. Their ratio is exactly 0.2. This independently explains the LUMINARY 099 `.2 NOM` comment as the low/high altitude scale-factor ratio and strongly bounds the LM-5 high-scale conversion. Because MSC-69-FS-4 documents Luminary 1B rather than the flown Luminary 1A build, the 5.3950 ft/count value is retained as strong adjacent-version evidence, not yet promoted to Apollo-11-effective hardware fact.

## Next work

1. Seek Apollo-11/LM-5-effective hardware or Luminary 1A guidance documentation directly confirming the 5.3950 ft/count high-scale LR altitude conversion.
2. Resolve why the Apollo 11 prelaunch table records `SKALSKAL = 00000` despite the source definition `.2 NOM`; do not assume the table's zero is the run-time multiplier.
3. Continue seeking LM-5 hardware-interface evidence for serial word bias/framing and rounding/truncation.
4. Continue the parallel Apollo-11 MSK-1137 per-field provenance and GUIDO workflow thread.
5. Keep historical stochastic LR measurement generation **BLOCKED** pending flight-effective residual/distribution evidence.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** high/low LR altitude scale selection and conditional software rescaling; low-scale stored representation 1.079 ft/count.
- **DOCUMENTED SOFTWARE DEFINITION:** `SKALSKAL` is erasable and documented `.2 NOM` in LUMINARY 099 source.
- **DOCUMENTED, APOLLO-11 PRELAUNCH LOAD:** `SKALSKAL` address 3462 = octal `00000`; `RADSCALE` address 3461 = octal `00000`.
- **DOCUMENTED, NEAR-MISSION LUMINARY 1B:** LR altitude = 1.0790 ft/count low scale and 5.3950 ft/count high scale; ratio = 0.2.
- **UNRESOLVED:** direct Apollo-11-effective confirmation of 5.3950 ft/count; zero-padload/run-time relationship; complete raw serial encoding and rounding.
- **BLOCKED:** stochastic historical LR error generator.
