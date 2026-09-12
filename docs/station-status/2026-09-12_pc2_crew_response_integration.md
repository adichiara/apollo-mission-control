# Station research-status addendum — PC+2 crew response integration

Date: 2026-09-12

## CONTROL

**Maturity remains B.**

- The >25 psi fuel/oxidizer ΔP branch now continues beyond CONTROL callout through explicit crew response and physical engine-off layers.
- No additional CONTROL display/routing claim was required.
- Fresh shutdown evidence remains a separate downstream concern.

## CAPCOM

**Maturity remains B.**

- A transmitted ground shutdown call no longer terminates the modeled branch.
- Transmission is now explicitly followed by a separate crew-receipt event before any crew command can occur.
- Exact wording and internal Mission Control routing remain unresolved and are not inferred.

## FLIGHT

**Maturity remains B.**

- No new FLIGHT approval stage was inserted into the hypothetical ΔP branch because reviewed sources do not establish that exact internal routing.
- Existing FLIGHT authority remains unchanged.

## Crew / spacecraft operational layer

**Integration maturity: B for this narrow branch.**

- Crew receipt is explicit.
- Crew DPS shutdown command reuses the established operational-action model.
- Command does not directly stop the physical engine.
- Physical engine-off response reuses the established DPS response model and requires an externally supplied response GET.
- No automatic confirmation telemetry is generated.

## Research constraints retained

- no response-delay model without direct evidence;
- no exact hypothetical cockpit sequence beyond the generic source-backed off-command boundary;
- no engine-off pressure tailoff synthesis;
- no chamber-pressure confirmation threshold;
- no assumption that a CAPCOM transmission is automatically received or obeyed.

## Next station-facing question

After HTTP exposure of the crew-response path, determine the minimum controller-facing evidence refresh needed after physical engine-off using the existing shutdown-confirmation model. Do not create a new station product unless the existing CONTROL evidence path proves insufficient.
