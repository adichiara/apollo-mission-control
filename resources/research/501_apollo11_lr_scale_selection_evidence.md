# Research 501 — Apollo 11 landing-radar altitude scale selection

Date: 2026-09-20
Research thread: `apollo11-landing-radar`

## Findings

The Apollo 11 LUMINARY 099 listing provides a mission-effective software boundary for landing-radar altitude scale handling:

- `FLAGWORD_ASSIGNMENTS.agc`: `ALTSCALE` / `ALTSCBIT` identifies whether the LR altitude reading is on the high/low scale.
- `SERVICER.agc`: the position-update path tests `ALTSCBIT`; the zero branch is explicitly commented `BRANCH IF HIGH SCALE`, while the alternate path executes `CA SKALSKAL` / `TC SHORTMP` with `RESCALE IF LOW SCALE`.
- `ERASABLE_ASSIGNMENTS.agc`: `SKALSKAL` is defined as `LR ALT SCALE FACTOR RATIO: .2 NOM`.
- `CONTROLLED_CONSTANTS.agc`: `HSCAL` is defined with the comment `SCALES 1.079 FT/BIT TO 2(22)M.`

## Interpretation boundary

This evidence establishes high/low scale awareness and conditional rescaling in Apollo-11-effective flight software. Because `SKALSKAL` is erasable and the listing labels `.2` as nominal, the comment is not sufficient evidence that the flown LM-5 erasable load was exactly 0.2. It also does not independently establish the radar electronics' raw high-scale LSB, integer bias, serial framing, or rounding behavior.

Later R-567/LM10 raw-interface descriptions remain adjacent-effectivity cross-checks only.

## Sources

- https://www.ibiblio.org/apollo/listings/Luminary099/FLAGWORD_ASSIGNMENTS.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/ERASABLE_ASSIGNMENTS.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/CONTROLLED_CONSTANTS.agc.html

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** high/low altitude-scale state and conditional rescaling path.
- **DOCUMENTED SOFTWARE DEFINITION:** nominal scale-factor ratio `.2`, stored in erasable `SKALSKAL`.
- **UNRESOLVED:** actual LM-5 loaded `SKALSKAL`; raw high-scale hardware encoding, bias, framing, and rounding.
- **BLOCKED:** stochastic historical LR error distribution/process.
