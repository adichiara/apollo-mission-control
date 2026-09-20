# Apollo 11 landing-radar scale-selection roadmap update

Date: 2026-09-20
Parent: `docs/roadmap/2026-09-19_apollo11_landing_radar_beam_transform.md`

## Newly closed boundary

Flown LUMINARY 099 explicitly distinguishes landing-radar altitude high/low scale. `SERVICER.agc` tests `ALTSCBIT`; its high-scale branch bypasses the low-scale rescaling operation, while the low-scale path applies `SKALSKAL`. `ERASABLE_ASSIGNMENTS.agc` defines `SKALSKAL` as an LR altitude scale-factor ratio with `.2 NOM`; `FLAGWORD_ASSIGNMENTS.agc` identifies the corresponding altitude-scale flag. `CONTROLLED_CONSTANTS.agc` independently defines `HSCAL` as converting the documented `1.079 ft/bit` representation into the estimator's internal metric scaling.

This closes the question of whether Apollo-11-effective software recognized distinct LR altitude scales and where the scale distinction enters the estimator. It does not close the raw radar-electronics encoding.

## Next work

1. Search the LM-5/Luminary 099 mission pad-load material for the actual loaded `SKALSKAL` value and effectivity.
2. Continue seeking LM-5 hardware-interface evidence for raw high-scale LSB, serial word bias/framing, and rounding/truncation.
3. Do not derive those raw-interface values from the `.2 NOM` software comment alone.
4. Continue the parallel Apollo-11 MSK-1137 per-field provenance and GUIDO workflow thread.
5. Keep historical stochastic LR measurement generation **BLOCKED** pending flight-effective residual/distribution evidence.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** high/low LR altitude scale selection and conditional software rescaling.
- **DOCUMENTED SOFTWARE DEFINITION:** `SKALSKAL` is erasable and documented `.2 NOM`.
- **UNRESOLVED:** exact LM-5 loaded scale ratio and complete raw serial/high-range encoding.
- **BLOCKED:** stochastic historical LR error generator.
