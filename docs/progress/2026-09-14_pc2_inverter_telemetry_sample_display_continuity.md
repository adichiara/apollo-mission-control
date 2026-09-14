# Progress — PC+2 inverter telemetry sample/display continuity

Date: 2026-09-14

## Completed

- Continued from research note 118's unresolved inverter display/cadence boundary.
- Reviewed primary LM telemetry material for `GC0071V` (AC bus voltage) and `GC0155F` (AC bus frequency).
- Added research note 119.
- Added a focused inverter telemetry-presentation source catalog.
- Preserved the distinction between Apollo 13/LM-7 evidence and later LM-10/Apollo 15 continuity evidence.

## Finding

The LM-10 telemetry summary explicitly lists both measurements as operational MSFN telemetry products. It gives format-dependent sample rates:

- format 1: 1 sample/s;
- formats 3, 4, 5: 0.2 sample/s.

It also lists multiple primary MSK destinations for both values. This is strong evidence that the inverter voltage/frequency values were operational display products and that telemetry sampling was not governed by one universal cadence.

The LM-7/8/9 elementary diagrams independently preserve the same measurement identities for Apollo 13's vehicle family.

## Historical boundary retained

LM-10 is not LM-7. The project therefore does **not** assign those later sample rates, MSK numbers, strip-chart configuration, or display selection to Apollo 13 PC+2.

Exact Apollo 13:

- MSFN format loading;
- sample cadence;
- primary MSK list;
- selected controller display;
- field placement/precision;
- CRT update latency

remain unresolved.

## First-playable consequence

No implementation change is required. The existing project-rendered ground electrical evidence remains source-bounded. It must not present an Apollo 13 historical MSK number or refresh rate as recovered fact.

## Validation status

No maturity grade changes and no new physical-play PASS claims.

Principal outstanding validation boundaries remain:

1. physical seven-seat nominal play;
2. synthetic ΔP case;
3. five-player compact play.

## Research next

Seek an LM-7/Apollo 13 instrumentation packet, telemetry-format loading record, or Apollo 13 MCC display-load artifact that can certify `GC0071V` / `GC0155F` format and MSK routing for PC+2.
