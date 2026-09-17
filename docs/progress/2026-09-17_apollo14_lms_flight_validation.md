# Progress — LMS flight-derived validation boundary

Date: 2026-09-17

## Work completed

Added a new validation evidence class from primary postflight sources rather than acceptance-test artifacts.

The Apollo 14 Mission Report directly compares flown LM behavior with LMS training and states that the simulator's **steering equations** and **torque-to-inertia ratio** were nearly identical to those of the actual vehicle. The same report separately attributes successful landing-site recognition in part to the **high fidelity of the simulator visual display**.

Follow-on checks found two compatible later-mission boundaries:

- **Apollo 15:** preflight experience with visual simulator displays made actual descent rates appear nominal/comfortable, and visual simulations plus LLTV flying were judged excellent training for the manual landing phase.
- **Apollo 17:** the landing narrative attributes the comfortable/safe manual approach partly to LMS training and states that the Commander's out-the-window / in-cockpit attention technique used in flight was practiced in the LMS and LLTV.

Added/updated:

- `resources/research/234_apollo14_lms_flight_validation_boundary.md`
- `resources/source-catalog/LMS_FLIGHT_VALIDATION_SOURCES.md`
- `docs/roadmap/2026-09-17_lms_flight_validation_boundary.md`

## Architecture consequence

The project now distinguishes two validation evidence classes:

1. **engineering acceptance/correlation evidence** — the preferred source for numerical tolerances, reference inputs/outputs, and pass/fail criteria;
2. **flight-derived operational validation** — useful for identifying model domains and operator-facing effects that NASA postflight reporting linked to actual flight, but not a numerical tolerance source unless the report supplies comparison numbers.

The combined Apollo 14 / Apollo 15 / Apollo 17 evidence reinforces explicit reusable boundaries for:

- guidance/steering computation;
- rotational dynamics and mass/inertia coupling;
- visual/observation generation;
- operator-facing display/attention information sufficient to support trained control technique.

## D-022 consequence

No new D-022 range is authorized. “Nearly identical,” “high fidelity,” and training-transfer attribution are qualitative and cannot be converted into a numerical interval.

## Next research action

Continue attempting to recover formal LMS acceptance/correlation material from RG 255 E.155B1 and the surviving `1L5-102-(H)` lineage. When mathematical-model documents are recovered, cross-check their steering, mass/inertia, visual/display, and operator-facing interfaces against the behavior families that later mission reports linked to flight performance.
