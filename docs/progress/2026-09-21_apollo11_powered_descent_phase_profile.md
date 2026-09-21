# Progress — Apollo 11 powered-descent phase profile

Date: 2026-09-21

Continued the open Apollo 11 powered-descent architecture reference after the MSK-1137 parameter-routing question was correctly marked BLOCKED on named archival source recovery.

## Completed

Primary-source review established a bounded propulsion/trajectory phase skeleton without inventing a continuous flown trajectory. The final Flight Plan supplies nominal throttle-recovery/high-gate/low-gate/touchdown anchors. The Mission Report supplies flown DPS duration, delta-V, minimum-throttle start, approximately +26 s throttle-up, and the important approximately 45 s early data-loss limitation. The Mission Operation Report independently defines braking/approach/landing phase boundaries.

## Repository updates

- `docs/roadmap/2026-09-21_apollo11_powered_descent_phase_profile.md`
- `docs/station-status/2026-09-21_apollo11_powered_descent_phase_profile.md`
- `resources/APOLLO11_LUMINARY1A_SOURCE_CATALOG_ADDENDUM.md`

## Boundary preserved

Planned nominal phase states are not represented as exact flown states. The smoothed postflight propulsion figure is not treated as measured data through its documented dropout. Mission-level values are not exposed to controller stations absent separate display/provenance evidence.

## Next target

Apollo-11-effective controller-visible propulsion/trajectory monitoring and decision rules at throttle recovery/high gate.