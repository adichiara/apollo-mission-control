# Progress — Apollo 11 landing-radar scale-selection boundary

Date: 2026-09-20

## Question

Can flown Apollo 11 software narrow the remaining high/low altitude-scale interface gap without importing later LM10/R-567 raw-interface details?

## Primary-source result

Yes, but only at the LUMINARY-side scale-selection boundary.

Flown LUMINARY 099 `FLAGWORD_ASSIGNMENTS.agc` defines `ALTSCALE`/`ALTSCBIT` as the landing-radar altitude-reading scale state. In `SERVICER.agc`, the position-update path explicitly tests `ALTSCBIT`; the zero branch is commented `BRANCH IF HIGH SCALE`, while the other path applies `SKALSKAL` with the comment `RESCALE IF LOW SCALE` before combining the computed Doppler correction with `HMEAS`.

`ERASABLE_ASSIGNMENTS.agc` defines `SKALSKAL` as `LR ALT SCALE FACTOR RATIO: .2 NOM`. Separately, `CONTROLLED_CONSTANTS.agc` defines `HSCAL` as the conversion that `SCALES 1.079 FT/BIT TO 2(22)M.`

This establishes that Apollo-11-effective software explicitly distinguished high- and low-scale altitude readings and carried a mission-loadable scale-ratio quantity nominally 0.2. It does **not** establish the exact LM-5 loaded `SKALSKAL` value, raw high-scale hardware LSB, raw serial integer bias, framing, or rounding/truncation. Those remain unresolved until mission-effective pad-load or hardware-interface evidence is recovered.

## Model consequence

- Preserve an explicit altitude-scale state in any faithful LR/LGC interface model.
- Do not hard-code the nominal `.2` comment as the flown LM-5 load without recovering the applicable erasable load.
- Do not derive a raw high-scale LSB by arithmetic from `.2`; the code establishes a software rescaling relationship, not the complete radar-electronics encoding.
- Existing `1.079 ft/bit` remains authoritative for the converted/stored low-scale `HMEAS` representation.

## Primary sources

- Apollo 11 LUMINARY 099, `SERVICER.agc`, MIT Instrumentation Laboratory/NASA.
- Apollo 11 LUMINARY 099, `FLAGWORD_ASSIGNMENTS.agc`, MIT Instrumentation Laboratory/NASA.
- Apollo 11 LUMINARY 099, `ERASABLE_ASSIGNMENTS.agc`, MIT Instrumentation Laboratory/NASA.
- Apollo 11 LUMINARY 099, `CONTROLLED_CONSTANTS.agc`, MIT Instrumentation Laboratory/NASA.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** software distinguishes LR altitude high/low scale and conditionally rescales the low-scale path.
- **DOCUMENTED, APOLLO-11-EFFECTIVE SOFTWARE DEFINITION:** `SKALSKAL` is an erasable LR altitude scale-factor ratio with `.2 NOM` documented in the flown listing.
- **DOCUMENTED, APOLLO-11-EFFECTIVE:** `HSCAL` converts the `1.079 ft/bit` representation to the estimator's internal metric scale.
- **UNRESOLVED:** exact LM-5 loaded `SKALSKAL`, raw high-scale hardware LSB, serial integer bias, framing, and rounding/truncation.
- **BLOCKED:** historical stochastic LR error generation beyond documented performance envelopes and flight events.
