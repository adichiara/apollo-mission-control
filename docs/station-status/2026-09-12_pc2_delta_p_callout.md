# Station research-status addendum — PC+2 ΔP ground callout

Date: 2026-09-12

## CONTROL

**Maturity remains B.**

Improved:

- fuel/oxidizer ΔP >25 psi is now represented as a genuinely ground-only shutdown path rather than a generic threshold;
- CONTROL owns the modeled threshold assessment and can issue an explicit shutdown-callout decision event;
- the ground-derived product remains distinct from any crew-visible indication.

Still unresolved:

- exact ground ΔP computation/sign convention;
- exact CONTROL CRT field/update cadence;
- exact hypothetical CONTROL→FLIGHT voice-loop wording if the criterion triggered.

## CAPCOM

**Maturity remains B.**

Improved:

- CAPCOM now has an explicit crew-facing ground-callout event for the ΔP shutdown criterion;
- the callout remains separate from the CONTROL decision and from the crew's operational response.

Still unresolved:

- exact callout wording;
- whether FLIGHT would explicitly repeat/approve the call in this hypothetical branch before CAPCOM transmission.

## FLIGHT

**Maturity remains B.**

No unsupported approval step is added. FLIGHT remains the integration/decision authority in the broader architecture, but the reviewed PC+2 sources do not establish the exact internal handling of a hypothetical ΔP exceedance strongly enough to encode a mandatory intermediate event.

## Crew/CAPCOM boundary

The contemporaneous rules exchange establishes that the crew understood:

- ΔP >25 psi was a ground callout;
- the appropriate response was shutdown.

The exact LM cockpit shutdown control sequence is not established by the reviewed sources and is not invented.
