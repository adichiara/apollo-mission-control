# Station research status — Apollo 11 LR scale selection

Date: 2026-09-20
Parent: `docs/station-status/2026-09-19_apollo11_landing_radar_beam_transform.md`

## GUIDO / guidance-monitoring consequence

Flown LUMINARY 099 establishes that the onboard landing-radar altitude path explicitly tracked high/low scale state and conditionally rescaled the low-scale path before the altitude residual/update logic. The Apollo 11 LUMINARY 99 prelaunch pad-load table records `SKALSKAL` as octal `00000`, while the source listing labels it `.2 NOM`.

MSC-69-FS-4, the primary MIT/MSC programmed-guidance-equations document for Luminary 1B, explicitly gives LR altitude count values of 1.0790 ft low scale and 5.3950 ft high scale. The exact 0.2 low/high ratio explains the meaning of the `.2 NOM` scale-factor comment. It does not, by itself, establish that 5.3950 ft/count was unchanged in LM-5/Luminary 1A, so that value remains adjacent-version corroboration pending Apollo-11-effective confirmation.

No recovered source establishes that `ALTSCBIT`, `SKALSKAL`, the raw scale state, or the rescaling operation was exposed directly to GUIDO, CONTROL, or FLIGHT. No station display, alarm, callout, or procedure is added from this evidence.

## Player-facing boundary

A spacecraft model may preserve LR altitude scale state internally. Do not expose a raw high/low-scale indicator to controllers unless mission-effective MCC evidence establishes it. The model may retain 5.3950 ft/count as a sourced candidate for high-scale conversion, but should not label it Apollo-11-effective until direct LM-5/Luminary 1A evidence is recovered.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD LOGIC:** `ALTSCBIT` selects high/low LR altitude treatment; low scale invokes `SKALSKAL` rescaling.
- **DOCUMENTED, APOLLO-11-EFFECTIVE LOW SCALE:** 1.079 ft/count stored representation.
- **DOCUMENTED SOFTWARE DEFINITION:** `SKALSKAL` is an erasable scale-factor ratio documented as `.2 NOM`.
- **DOCUMENTED, NEAR-MISSION LUMINARY 1B:** 1.0790 ft/count low scale; 5.3950 ft/count high scale; ratio 0.2.
- **NO STATION MATURITY CHANGE:** controller visibility/routing remains unestablished.
- **UNRESOLVED:** direct Apollo-11-effective high-scale confirmation, zero-padload/run-time relationship, raw serial bias/framing, rounding/truncation, and controller-visible scale-state consequences.
