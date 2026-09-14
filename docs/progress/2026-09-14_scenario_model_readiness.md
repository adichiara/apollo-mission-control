# Progress — scenario-specific model readiness

Date: 2026-09-14

## Completed

- Added `required_model_domains` to scenario metadata.
- Added a reusable readiness assessment over a scenario's selected model profile.
- Readiness reports:
  - required domains;
  - per-domain status;
  - missing domains;
  - unvalidated domains;
  - a single `historical_validation_ready` flag.
- PC+2 currently requires mass properties, propulsion, translational dynamics, and tracking observation.
- Scenario discovery now exposes both runtime executability and historical model readiness.
- Session status exposes the same readiness assessment.
- Prototype session creation remains allowed when historical numerical domains are incomplete.
- Added model-profile, scenario-catalog, runtime-adapter, and web API tests.

## Consequence

The project now distinguishes two independent questions:

1. **Can this scenario run in the current simulator?**
2. **Are all numerical model domains required by this scenario historically validated?**

For the current PC+2 reference case, the first answer is yes and the second is no. That distinction is explicit rather than implicit.

This also supports future scenario diversity: a communications/network scenario, lunar-descent scenario, rendezvous scenario, and entry scenario can declare different model-domain requirements rather than being judged against a PC+2-specific fidelity checklist.

## Boundary

Readiness is an evidence/validation status, not an execution lock. A future release policy may choose to require historical readiness for certain scenario labels, but the current research prototype intentionally permits partially validated scenarios while exposing their limitations.
