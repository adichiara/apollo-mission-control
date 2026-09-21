# Progress — Apollo 11 LR convergence monitoring

Date: 2026-09-21

Continued the open Apollo 11 powered-descent research thread from the trajectory-rule stopping point.

## Result

Primary NASA postflight evidence now closes the **observable flown LR convergence sequence** sufficiently for a reference-model state chain. NASA TM X-58040 records LR lock near 37,000 ft, initial Δh of -2,200 ft, altitude-data incorporation near 31,600 ft, convergence to about 100 ft within 30 seconds, and nominal velocity updates beginning near 29,000 ft. It also explicitly says flight controllers and crew monitored altitude and altitude rate, with ground controllers limited by communications delay to advising on projected trends.

The Apollo 11 Mission Report provides compatible event timestamps for LR data good, radar-update enable, the velocity-update condition, and P64 entry.

## Guardrail

This does **not** recover the Mission-G CRT field/routing or prove a station-specific call chain. No GUIDO ownership, exact display request, back-room role, or landing-GO voice sequence is inferred from generic responsibilities.

## Repository updates

- added `docs/roadmap/2026-09-21_apollo11_lr_convergence_monitoring.md`;
- added `docs/station-status/2026-09-21_apollo11_lr_convergence_monitoring.md`;
- added `resources/APOLLO11_LR_CONVERGENCE_MONITORING_SOURCE_CATALOG_ADDENDUM.md`;
- retained the existing Mission-G parameter-routing BLOCKED boundary.

## Next

Bound the station-specific voice/call workflow around LR acceptance/convergence and the GO for landing using Apollo-11-effective controller documentation, controller-loop/transcript material, or postflight controller reports. Do not infer station ownership where speaker/source identity is absent.

## Evidence status

- **DOCUMENTED:** flown LR convergence sequence and ground trend-monitoring role.
- **PARTIAL:** event-level controller evidence chain.
- **UNRESOLVED:** exact display and station-specific call workflow.