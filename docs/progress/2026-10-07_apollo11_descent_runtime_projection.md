# Progress — Apollo 11 bounded descent runtime projection

Date: 2026-10-07

## Completed

Composed the existing Apollo 11 powered-descent architecture domains into one read-only runtime snapshot without creating a second event model.

The projection joins:

`generic session GET + human events + nominal phase + explicit LR/controller products + guidance-computer state -> bounded descent runtime snapshot`

It reuses the generic session's actual readiness reports, FLIGHT decision audit events, and CAPCOM transmission records.

## Guardrails demonstrated

Automated tests and the Causal Model Lab demonstrate that:

- Guidance + CONTROL GO does not automatically create FLIGHT GO;
- FLIGHT GO does not automatically create a CAPCOM relay;
- manual/P66 control changes trajectory/guidance abort-rule applicability without erasing observations;
- an active onboard alarm does not automatically appear on the controller product;
- explicitly supplied controller alarm data does appear;
- projection does not mutate the authoritative session;
- phase state remains the nominal Flight Plan skeleton rather than a reconstructed flown trajectory.

## Site-facing proof

Added:

`GET /api/admin/model-proof/apollo11-descent-runtime-projection`

The reference probe is explicitly architecture-only. Its event timings and controller values are synthetic and are not claimed as Apollo 11 replay data.

## Next

Build the Apollo 11 descent scenario/runtime adapter on top of this projection and the existing `GenericScenarioSession` mechanics.

Do not make the scenario executable merely because the composition exists. Scenario readiness still has to respect model-profile gates and unresolved source-dependent products.
