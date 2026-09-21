# Progress — Apollo 11 LR `SKALSKAL` mission pad load

Date: 2026-09-20
Corrected: 2026-09-21

## Question

What value was actually loaded for the LUMINARY 099 erasable `SKALSKAL` on Apollo 11/LM-5, rather than merely documented as the source-listing nominal `.2`?

## Primary mission evidence

The Apollo 11 LUMINARY 99 prelaunch pad-load document, table LM5/4.5.1-1, lists:

- `RADSKAL`, addresses 1354–1355: octal `00000,00000`;
- `SKALSKAL`, address 1356: octal `00000`.

The flown LUMINARY 099 assembly symbol table independently places `SKALSKAL` at erasable address 1356. This cross-check corrects an earlier transcription in this repository that reported addresses 3461/3462 and rendered `RADSKAL` as `RADSCALE`; those values/names are not what the primary pad-load table and flown symbol table show.

This closes the pad-load lookup itself. It also creates an important interpretation boundary because the LUMINARY 099 erasable assignment source independently comments `SKALSKAL` as the LR altitude scale-factor ratio, `.2 NOM`.

## Interpretation boundary

The two records are not collapsed into an invented explanation. In particular, this finding does **not** establish that:

- the physical LR high/low ratio was zero;
- `.2` was nevertheless the flown value;
- a zero erasable value disabled the scale path;
- the raw high-scale LSB can be calculated from either record;
- `RADSKAL` and `SKALSKAL` had identical runtime semantics merely because both were loaded zero;
- any controller saw the scale state or these erasables.

The next discriminating research target is mission-effective documentation or code/load behavior that explains how the zero prelaunch load relates to the `.2 NOM` source definition.

## Documentation synchronized

- `docs/roadmap/2026-09-20_apollo11_lr_scale_selection.md`
- `docs/station-status/2026-09-20_apollo11_lr_scale_selection.md`
- `resources/APOLLO11_LUMINARY1A_SOURCE_CATALOG_ADDENDUM.md`
- this progress record

No station maturity changes. Historical stochastic LR measurement generation remains **BLOCKED**.

## Evidence status

- **DOCUMENTED, APOLLO-11 PRELAUNCH LOAD:** `SKALSKAL` 1356 = octal `00000`; `RADSKAL` 1354–1355 = octal `00000,00000`.
- **DOCUMENTED, APOLLO-11-EFFECTIVE SYMBOL TABLE:** `SKALSKAL` = erasable address 1356.
- **CORRECTED:** earlier repository references to `SKALSKAL` 3462 / `RADSCALE` 3461 were transcription errors and are withdrawn.
- **DOCUMENTED SOFTWARE DEFINITION:** LUMINARY 099 labels `SKALSKAL` `.2 NOM`.
- **UNRESOLVED:** mission-effective semantic relationship between the zero prelaunch load and `.2 NOM`.
- **BLOCKED:** deriving raw high-range encoding or stochastic sensor behavior from this evidence.

## Sources

- Apollo 11 LUMINARY 99 prelaunch pad loads: https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- LUMINARY 099 assembled listing/symbol table: https://www.ibiblio.org/apollo/listings/Luminary099/MAIN.agc.html
- LUMINARY 099 erasable assignments: https://www.ibiblio.org/apollo/listings/Luminary099/ERASABLE_ASSIGNMENTS.agc.html
- LUMINARY 099 service logic: https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
