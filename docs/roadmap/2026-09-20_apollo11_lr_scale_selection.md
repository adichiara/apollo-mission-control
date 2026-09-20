# Apollo 11 landing-radar scale-selection roadmap update

Date: 2026-09-20
Parent: `docs/roadmap/2026-09-19_apollo11_landing_radar_beam_transform.md`

## Newly closed boundary

Flown LUMINARY 099 explicitly distinguishes landing-radar altitude high/low scale. `SERVICER.agc` tests `ALTSCBIT`; its high-scale branch bypasses the low-scale rescaling operation, while the low-scale path applies `SKALSKAL`. `ERASABLE_ASSIGNMENTS.agc` defines `SKALSKAL` as an LR altitude scale-factor ratio with `.2 NOM`; `FLAGWORD_ASSIGNMENTS.agc` identifies the corresponding altitude-scale flag. `CONTROLLED_CONSTANTS.agc` independently defines `HSCAL` as converting the documented `1.079 ft/bit` representation into the estimator's internal metric scaling.

The Apollo 11 LUMINARY 99 prelaunch pad-load document now closes the previously open mission-load question: table LM5/4.5.1-1 lists `SKALSKAL` at address 3462 with an octal load of `00000`, and `RADSCALE` at 3461 likewise `00000`. This is mission-specific pad-load evidence. It supersedes treating the `.2 NOM` source comment as the flown LM-5 value.

The zero pad-load must not be interpreted in isolation as a raw radar scale ratio, a hardware LSB, or proof that the conditional software path was inactive. The code/source-comment semantics and the mission load are retained as separate facts until their interaction is established from mission-effective software/load documentation.

## Next work

1. Resolve the mission-effective semantic relationship between the `SKALSKAL = 00000` pad load and the `.2 NOM` erasable/source comment before assigning numerical behavior to that rescaling path.
2. Continue seeking LM-5 hardware-interface evidence for raw high-scale LSB, serial word bias/framing, and rounding/truncation.
3. Do not derive raw-interface values from either `.2 NOM` or the zero pad load alone.
4. Continue the parallel Apollo-11 MSK-1137 per-field provenance and GUIDO workflow thread.
5. Keep historical stochastic LR measurement generation **BLOCKED** pending flight-effective residual/distribution evidence.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** high/low LR altitude scale selection and conditional software rescaling.
- **DOCUMENTED SOFTWARE DEFINITION:** `SKALSKAL` is erasable and documented `.2 NOM` in source.
- **DOCUMENTED, APOLLO-11 PRELAUNCH LOAD:** `SKALSKAL` address 3462 = octal `00000`; `RADSCALE` address 3461 = octal `00000`.
- **UNRESOLVED:** why the mission load is zero relative to the `.2 NOM` source comment; complete raw serial/high-range encoding.
- **BLOCKED:** stochastic historical LR error generator.
