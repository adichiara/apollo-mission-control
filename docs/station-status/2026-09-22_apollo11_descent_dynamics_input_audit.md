# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, strengthened.** TRW Note 70-FMT-819 documents a mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown using MSFN, onboard, and relative-tracking evidence. This supplies a historical validation/reference trajectory, not a newly recovered Mission-G live display or raw controller truth stream. Do not expose the postflight BET directly as a controller product unless a separate source establishes that product.

## CONTROL

**Status: PARTIALLY DOCUMENTED for underlying DPS/resource physics; player product unchanged.** Primary documentation supports DPS throttling/gimbal/resource architecture. LM-5 launch propellant loading is documented, but PDI mass and an exact delivered thrust/Isp history remain unresolved. The postflight trajectory reconstruction does not close those propulsion inputs.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from the recovered postflight trajectory reconstruction.

## Implementation boundary

Design-envelope values may constrain validation tests and scenario-input sanity checks. The 70-FMT-819 DOI→touchdown reconstruction may serve as a RECONSTRUCTED historical reference for model outputs after its frame/epoch definitions are extracted. Neither class may silently become station telemetry, exact Apollo 11 physical truth, or decision thresholds.

## Evidence status

- underlying DPS parameter semantics: **DOCUMENTED**;
- LM-5 launch resource bookkeeping: **DOCUMENTED**;
- Apollo 11 postflight DOI→touchdown continuous trajectory reconstruction: **DOCUMENTED AS RECONSTRUCTED**;
- Apollo 11 PDI mass and delivered DPS time history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.