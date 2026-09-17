# Progress — flight-derived simulator mismatch and AGS validation architecture

Date: 2026-09-17

## Work completed

Extended the validation framework so it does not contain only favorable simulator comparisons, then recovered a primary Apollo-era verification architecture for the LM Abort Guidance System.

The Apollo 9 Mission Report records a direct mismatch during LM rendezvous: after radar updates brought AGS range/range-rate information into agreement, that information appeared to **degrade much more rapidly in flight than in the simulator**. The same operational narrative reports pulse-mode control behavior as very similar to the mission simulator. The report also supplies a flight-side observable magnitude: AGS solution variation reached approximately **±3 ft/s about the mean** during rendezvous. The simulator-side same-input magnitude remains unrecovered, so this is not a D-022 interval.

Added/updated:

- `resources/research/236_apollo9_simulator_flight_mismatch_boundary.md`
- Apollo 9 negative evidence to `resources/source-catalog/LMS_FLIGHT_VALIDATION_SOURCES.md`
- Apollo Program Summary Report program-level validation synthesis to the same catalog
- `resources/research/237_ags_verification_validation_architecture.md`
- `resources/source-catalog/AGS_VERIFICATION_SOURCES.md`
- `docs/VALIDATION_EVIDENCE_MODEL.md`

## NASA TN D-7990 recovery

Official source identity is now confirmed:

- Pat M. Kurten, *Apollo Experience Report — Guidance and Control Systems: Lunar Module Abort Guidance System*
- NASA TN D-7990 / JSC S-424
- NTRS `19750018954`
- July 1975

The report documents a layered verification process:

1. closed-loop engineering/equation simulations under nominal and 3σ vehicle/sensor/trajectory dispersions;
2. bit-by-bit interpretive computer simulation to verify coded implementation against equations;
3. closed-loop AEA-program + vehicle flight simulation;
4. 600-cycle Monte Carlo performance analysis against mission requirements;
5. independent MSC hybrid-computer tests with actual ASA/DEDA hardware;
6. mission-specific six-degree-of-freedom simulations incorporating AGS and LM flight-control hardware;
7. operational simulated-flight procedures whose criteria were represented as **value bounds or bounded curves** for AEA/display parameters.

The simulated-flight procedures explicitly included the **radar filter**, which gives a strong archival/test-case retrieval target for the Apollo 9 mismatch.

## Validation-framework consequence

Flight-derived evidence is classified at the behavior/domain level as:

1. favorable/representative comparison;
2. negative/mismatch comparison;
3. useful training transfer without a model-equivalence claim.

Engineering verification is separately layered into equation/model, implementation-equivalence, closed-loop causal integration, ensemble/statistical, independent/hardware-reference, and operational bounded-observable evidence.

This prevents a strong result in one simulator domain from being generalized to unrelated models and prevents synthetic architecture proofs from being mislabeled as historical validation.

For AGS/rendezvous behavior, future validation must distinguish:

`agreement immediately after a radar update`

from

`correct error growth during propagation between updates`.

The Apollo 9 report specifically warns that the first does not establish the second.

## Numerical-cadence boundary

TN D-7990 also documents a simulated-flight roundoff discrepancy involving a **20-ms AEA computing cycle**. This value is retained only as AGS/AEA computing-context evidence.

It is not a global LMS integration step and must remain separate from the previously cataloged LMS 50-ms AACS integration-step study.

## Program-level corroboration

The 1975 Apollo Program Summary Report independently summarizes that all lunar module crews regarded LMS/LLTV control responses as representative of flight hardware and credits high-fidelity landing/ascent visuals in manual-landing preparation.

The summary also records successful simulated degraded-mode landing cases within Mission Control 3-sigma altitude/targeting dispersion criteria, but the reviewed passage does not give numerical 3-sigma values. This does not create a D-022 range.

## No constant changes

No executable model constant changes from this work.

The next high-value step is recovering the actual AGS radar-filter simulated-flight bounds/bounded curves and crosswalking them with Apollo 9 Supplement 3 and the applicable simulator/software configuration. Formal LMS acceptance/correlation retrieval from RG 255 E.155B1 remains a separate priority.
