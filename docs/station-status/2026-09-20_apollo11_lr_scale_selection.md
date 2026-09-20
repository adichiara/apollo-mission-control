# Station research status — Apollo 11 LR scale selection

Date: 2026-09-20
Parent: `docs/station-status/2026-09-19_apollo11_landing_radar_beam_transform.md`

## GUIDO / guidance-monitoring consequence

Flown LUMINARY 099 now establishes that the onboard landing-radar altitude path explicitly tracked high/low scale state and conditionally rescaled the low-scale path before the altitude residual/update logic. This strengthens the spacecraft-side estimator model only.

No recovered source establishes that `ALTSCBIT`, `SKALSKAL`, the raw scale state, or the rescaling operation was exposed directly to GUIDO, CONTROL, or FLIGHT. No station display, alarm, callout, or procedure is added from this evidence.

## Player-facing boundary

A spacecraft model may preserve LR altitude scale state internally. Do not expose a raw high/low-scale indicator to controllers unless mission-effective MCC evidence establishes it. Do not treat `.2 NOM` as the exact flown LM-5 load or derive a bit-for-bit raw high-scale quantizer from it.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD LOGIC:** `ALTSCBIT` selects high/low LR altitude treatment; low scale invokes `SKALSKAL` rescaling.
- **DOCUMENTED SOFTWARE DEFINITION:** `SKALSKAL` is an erasable scale-factor ratio documented as `.2 NOM`.
- **NO STATION MATURITY CHANGE:** controller visibility/routing remains unestablished.
- **UNRESOLVED:** exact LM-5 loaded `SKALSKAL`, raw high-scale hardware LSB, serial bias/framing, rounding/truncation, and controller-visible scale-state consequences.
