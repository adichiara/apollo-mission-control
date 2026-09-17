# Progress — flight-derived simulator mismatch boundary

Date: 2026-09-17

## Work completed

Extended the flight-derived validation framework so it does not contain only favorable simulator comparisons.

The Apollo 9 Mission Report records a direct mismatch during LM rendezvous: after radar updates brought AGS range/range-rate information into agreement, that information appeared to **degrade much more rapidly in flight than in the simulator**. The same operational narrative reports pulse-mode control behavior as very similar to the mission simulator.

Added:

- `resources/research/236_apollo9_simulator_flight_mismatch_boundary.md`
- Apollo 9 negative evidence to `resources/source-catalog/LMS_FLIGHT_VALIDATION_SOURCES.md`
- Apollo Program Summary Report program-level validation synthesis to the same catalog.

## Validation-framework consequence

Flight-derived evidence is now classified at the behavior/domain level as:

1. favorable/representative comparison;
2. negative/mismatch comparison;
3. useful training transfer without a model-equivalence claim.

This prevents a strong result in one simulator domain from being generalized to unrelated models.

For AGS/rendezvous behavior, future validation must distinguish:

`agreement immediately after a radar update`

from

`correct error growth during propagation between updates`.

The Apollo 9 report specifically warns that the first does not establish the second.

## Program-level corroboration

The 1975 Apollo Program Summary Report independently summarizes that all lunar module crews regarded LMS/LLTV control responses as representative of flight hardware and credits high-fidelity landing/ascent visuals in manual-landing preparation.

The summary also records successful simulated degraded-mode landing cases within Mission Control 3-sigma altitude/targeting dispersion criteria, but the reviewed passage does not give numerical 3-sigma values. This does not create a D-022 range.

## No constant changes

No executable model constant changes from this work.

The next high-value step is quantitative source recovery for the Apollo 9 AGS discrepancy and for the underlying simulator/reference test that established expected between-update degradation.
