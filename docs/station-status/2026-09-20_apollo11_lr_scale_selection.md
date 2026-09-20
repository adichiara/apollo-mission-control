# Station research status — Apollo 11 LR scale selection

Date: 2026-09-20
Parent: `docs/station-status/2026-09-19_apollo11_landing_radar_beam_transform.md`

## GUIDO / guidance-monitoring consequence

Flown LUMINARY 099 establishes that the onboard landing-radar altitude path explicitly tracked high/low scale state and conditionally rescaled the low-scale path before the altitude residual/update logic. The Apollo 11 LUMINARY 99 prelaunch pad-load table further records `SKALSKAL` (address 3462) as octal `00000`, with adjacent `RADSCALE` (3461) also `00000`.

This closes the exact mission pad-load lookup, but not its numerical interpretation: the source listing separately labels `SKALSKAL` `.2 NOM`. Until mission-effective documentation explains the zero load/source-comment relationship, the simulation must not substitute `.2`, zero, or an inferred raw scale ratio as historical numerical behavior merely from these two records.

No recovered source establishes that `ALTSCBIT`, `SKALSKAL`, the raw scale state, or the rescaling operation was exposed directly to GUIDO, CONTROL, or FLIGHT. No station display, alarm, callout, or procedure is added from this evidence.

## Player-facing boundary

A spacecraft model may preserve LR altitude scale state internally. Do not expose a raw high/low-scale indicator to controllers unless mission-effective MCC evidence establishes it. Do not derive a bit-for-bit raw high-scale quantizer from `.2 NOM` or the zero pad load.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD LOGIC:** `ALTSCBIT` selects high/low LR altitude treatment; low scale invokes `SKALSKAL` rescaling.
- **DOCUMENTED SOFTWARE DEFINITION:** `SKALSKAL` is an erasable scale-factor ratio documented as `.2 NOM`.
- **DOCUMENTED, APOLLO-11 PRELAUNCH LOAD:** `SKALSKAL` 3462 = `00000`; `RADSCALE` 3461 = `00000` (octal).
- **NO STATION MATURITY CHANGE:** controller visibility/routing remains unestablished.
- **UNRESOLVED:** semantic relationship between the zero mission load and `.2 NOM`, raw high-scale hardware LSB, serial bias/framing, rounding/truncation, and controller-visible scale-state consequences.
