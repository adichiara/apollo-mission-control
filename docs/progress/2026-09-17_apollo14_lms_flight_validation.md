# Progress — Apollo 14 LMS flight-derived validation boundary

Date: 2026-09-17

## Work completed

Added a new validation evidence class from a primary postflight source rather than an acceptance-test artifact.

The Apollo 14 Mission Report directly compares flown LM behavior with LMS training and states that the simulator's **steering equations** and **torque-to-inertia ratio** were nearly identical to those of the actual vehicle. The same report separately attributes successful landing-site recognition in part to the **high fidelity of the simulator visual display**.

Added:

- `resources/research/234_apollo14_lms_flight_validation_boundary.md`
- `resources/source-catalog/LMS_FLIGHT_VALIDATION_SOURCES.md`

## Architecture consequence

The project now distinguishes two validation evidence classes:

1. **engineering acceptance/correlation evidence** — the preferred source for numerical tolerances, reference inputs/outputs, and pass/fail criteria;
2. **flight-derived operational validation** — useful for identifying model domains that NASA regarded as representative of flight, but not a numerical tolerance source unless the report actually supplies comparison numbers.

The Apollo 14 evidence reinforces explicit reusable boundaries for:

- guidance/steering computation;
- rotational dynamics and mass/inertia coupling;
- visual/observation generation.

## D-022 consequence

No new D-022 range is authorized. “Nearly identical” is qualitative and cannot be converted into a numerical interval.

## Next research action

Continue attempting to recover formal LMS acceptance/correlation material from RG 255 E.155B1 and the surviving `1L5-102-(H)` lineage. When mathematical-model documents are recovered, cross-check their steering and mass/inertia interfaces against the behavior families that Apollo 14 later reported as matching flight.
