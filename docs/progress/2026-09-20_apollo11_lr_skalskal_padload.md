# Progress — Apollo 11 LR `SKALSKAL` mission pad load

Date: 2026-09-20

## Question

What value was actually loaded for the LUMINARY 099 erasable `SKALSKAL` on Apollo 11/LM-5, rather than merely documented as the source-listing nominal `.2`?

## Primary mission evidence

The Apollo 11 LUMINARY 99 prelaunch pad-load document, table LM5/4.5.1-1, lists:

- `RADSCALE`, address 3461: octal `00000`;
- `SKALSKAL`, address 3462: octal `00000`.

This closes the pad-load lookup itself. It also creates an important interpretation boundary because the LUMINARY 099 erasable assignment source independently comments `SKALSKAL` as the LR altitude scale-factor ratio, `.2 NOM`.

## Interpretation boundary

The two records are not collapsed into an invented explanation. In particular, this finding does **not** establish that:

- the physical LR high/low ratio was zero;
- `.2` was nevertheless the flown value;
- a zero erasable value disabled the scale path;
- the raw high-scale LSB can be calculated from either record;
- `RADSCALE` and `SKALSKAL` had identical runtime semantics merely because both were loaded zero;
- any controller saw the scale state or these erasables.

The next discriminating research target is mission-effective documentation or code/load behavior that explains how the zero prelaunch load relates to the `.2 NOM` source definition.

## Documentation synchronized

- `docs/roadmap/2026-09-20_apollo11_lr_scale_selection.md`
- `docs/station-status/2026-09-20_apollo11_lr_scale_selection.md`
- `resources/APOLLO11_LUMINARY1A_SOURCE_CATALOG_ADDENDUM.md`
- this progress record

No station maturity changes. Historical stochastic LR measurement generation remains **BLOCKED**.

## Evidence status

- **DOCUMENTED, APOLLO-11 PRELAUNCH LOAD:** `SKALSKAL` 3462 = octal `00000`; `RADSCALE` 3461 = octal `00000`.
- **DOCUMENTED SOFTWARE DEFINITION:** LUMINARY 099 labels `SKALSKAL` `.2 NOM`.
- **UNRESOLVED:** mission-effective semantic relationship between those two facts.
- **BLOCKED:** deriving raw high-range encoding or stochastic sensor behavior from this evidence.

## Sources

- Apollo 11 LUMINARY 99 prelaunch pad loads: https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- LUMINARY 099 erasable assignments: https://www.ibiblio.org/apollo/listings/Luminary099/ERASABLE_ASSIGNMENTS.agc.html
- LUMINARY 099 service logic: https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
