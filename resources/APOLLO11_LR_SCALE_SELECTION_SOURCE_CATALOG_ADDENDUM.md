# Apollo 11 LR scale-selection source-catalog addendum

Date: 2026-09-20
Parent: `resources/APOLLO11_LUMINARY1A_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| LUMINARY 099 `FLAGWORD_ASSIGNMENTS.agc` | `ALTSCALE` / `ALTSCBIT` identifies LR altitude scale state | Apollo-11-effective software state; not proof of controller visibility. |
| LUMINARY 099 `SERVICER.agc` | Tests `ALTSCBIT`; high-scale branch bypasses rescaling; low-scale path applies `SKALSKAL` | Apollo-11-effective estimator/interface logic. |
| LUMINARY 099 `ERASABLE_ASSIGNMENTS.agc` | `SKALSKAL`: `LR ALT SCALE FACTOR RATIO: .2 NOM` | Establishes erasable nominal ratio only; do not claim exact flown LM-5 load without pad-load evidence. |
| LUMINARY 099 `CONTROLLED_CONSTANTS.agc` | `HSCAL`: `SCALES 1.079 FT/BIT TO 2(22)M.` | Confirms conversion of documented low-scale stored representation into estimator internal scaling. |

## Controlled conclusion

Apollo-11-effective software explicitly distinguishes high- and low-scale LR altitude treatment. The remaining raw-interface question is narrower: recover the actual LM-5 `SKALSKAL` load and mission-effective radar-electronics encoding before claiming an exact high-scale LSB, integer bias, framing, or rounding rule.

## Sources

- https://www.ibiblio.org/apollo/listings/Luminary099/FLAGWORD_ASSIGNMENTS.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/ERASABLE_ASSIGNMENTS.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/CONTROLLED_CONSTANTS.agc.html

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** altitude scale-state branch and low-scale rescaling.
- **UNRESOLVED:** exact LM-5 erasable scale ratio and complete raw serial/high-range encoding.
