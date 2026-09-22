# Progress — Apollo 11 descent propellant countdown

Date: 2026-09-21

Continued from the program-alarm stopping point.

## Result

Primary Apollo 11 evidence bounds the late-descent propellant state without turning the famous 60/30 calls into an invented exact fuel gauge. The Mission Report records the low-level signal at 102:44:30.4 GET and explicitly separates its sensor-location firing-time basis from the later landing decision point and postflight depletion estimate. The air-to-ground record fixes CAPCOM's 60-second and 30-second calls before contact and engine stop.

The previously unresolved ownership/procedure path is now research-sufficient. NASA JSC oral-history material identifies Robert L. Carlton as the LM CONTROL controller on Kranz's White Team. Carlton's first-person recollection describes using a stopwatch while monitoring altitude during the landing, and NASA's Apollo 11 historical treatment based on that oral history records that he started the marked stopwatch when the low-level condition occurred. This supports a **CONTROL procedural timer → CONTROL call → CAPCOM relay** chain, not an inferred RTCC/GUIDANCE computation.

The simulator should therefore carry separate low-level indication, CONTROL timer, CONTROL remaining-time call, CAPCOM transmission, and physical depletion states. Hidden authoritative propellant truth must not leak through the controller countdown.

## Files synchronized

- `docs/roadmap/2026-09-21_apollo11_descent_propellant_countdown.md`
- `docs/progress/2026-09-21_apollo11_descent_propellant_countdown.md`
- `docs/station-status/2026-09-21_apollo11_descent_propellant_countdown.md`
- `resources/APOLLO11_DESCENT_PROPELLANT_COUNTDOWN_SOURCE_CATALOG_ADDENDUM.md`

## Next

Treat the countdown provenance question as research-sufficient for implementation. Preserve the missing exact Mission-G written CONTROL procedure/display parameter as a bounded optional archival target, but do not continue broad searching for it. Move the Apollo 11 powered-descent thread to the next unresolved player-visible/controller decision dependency.

## Evidence status

**DOCUMENTED/PRIMARY:** physical/gaging timeline and crew-facing voice calls. **DOCUMENTED/RETROSPECTIVE FIRST-PERSON:** Bob Carlton/CONTROL stopwatch procedure. **RESEARCH-SUFFICIENT:** station ownership and human procedural-timer model. **UNRESOLVED BUT NOT REQUIRED:** exact Apollo-11-effective written timer procedure, CRT field, parameter mnemonic, and internal display route.