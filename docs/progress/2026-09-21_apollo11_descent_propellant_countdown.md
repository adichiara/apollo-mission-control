# Progress — Apollo 11 descent propellant countdown

Date: 2026-09-21

Continued from the program-alarm stopping point.

## Result

Primary Apollo 11 evidence now bounds the late-descent propellant state without turning the famous 60/30 calls into an invented exact fuel gauge. The Mission Report records the low-level signal at 102:44:30.4 GET and explicitly separates its sensor-location firing-time basis from the later landing decision point and postflight depletion estimate. The air-to-ground record fixes CAPCOM's 60-second and 30-second calls before contact and engine stop.

The simulator should therefore carry separate low-level indication, countdown/decision estimate, CAPCOM call, and physical depletion states. Hidden authoritative propellant truth must not leak through a controller countdown.

## Files synchronized

- `docs/roadmap/2026-09-21_apollo11_descent_propellant_countdown.md`
- `docs/progress/2026-09-21_apollo11_descent_propellant_countdown.md`
- `docs/station-status/2026-09-21_apollo11_descent_propellant_countdown.md`
- `resources/APOLLO11_DESCENT_PROPELLANT_COUNTDOWN_SOURCE_CATALOG_ADDENDUM.md`
- `docs/ROADMAP.md`

## Next

Recover the Mission-G controller/product provenance for the low-level-to-countdown path: station ownership, source parameter/product, and any documented computation or procedural timer feeding the CAPCOM 60/30 calls. Do not assign the calculation to CONTROL, GUIDANCE, FLIGHT, or RTCC without evidence.

## Evidence status

**DOCUMENTED/PARTIAL:** physical/gaging timeline and crew-facing voice calls. **OPEN:** controller-product provenance and countdown ownership. **UNRESOLVED BUT NOT INFERRED:** exact computation/display path.