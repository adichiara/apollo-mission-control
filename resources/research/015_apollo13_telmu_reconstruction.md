# Research Note 015 — Apollo 13 TELMU Reconstruction

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Key result

TELMU's Apollo 13 workload can be modeled as a documented **multi-resource lifetime problem** rather than an abstract spacecraft-health function.

## Central variables

Mission-specific evidence establishes continuous concern with:

- electrical current / amp-hours
- cooling water quantity and usage
- oxygen quantity and usage
- LiOH / CO2 removal
- thermal state
- mission time remaining

## Projected lifetime was operationally central

After the CSM accident, TELMU immediately compared LM consumable capability against the selected return trajectory.

Initial constraints included roughly:

- average current ≤24 A
- average water use ≤3.5 lb/hr
- oxygen not limiting
- LM-only LiOH insufficient

Subsequent power-down brought actual load to about 12 A and water usage to about 2.5–2.8 lb/hr.

## Configuration-dependent behavior

The Apollo 13 TELMU record contains several examples where simple fixed-limit logic would be wrong:

- water usage varied strongly with thermal/load history
- ascent O2 tank pressure exceeded a nominal redline that SPAN later judged invalid for the actual configuration
- a battery-malfunction warning was treated as probable sensor/overtemperature-switch trouble after voltage/current remained normal
- CO2 removal capability changed radically once a procedure allowed CSM cartridges to be used

## Simulation implication

TELMU should eventually work from real quantities/rates/configurations and calculate or receive projected margins.

Do not implement a single "LM lifetime" meter as a substitute for the underlying consumables.

## Missing display evidence

Exact Apollo 13 TELMU CRT formats and console hardware remain unresolved.

As with GNC and CONTROL, the station workflow is much better documented than its screen layout.

## Source

Apollo 13 Mission Operations Report, Appendix G; Apollo 13 Mission Report, lunar-module consumables sections.
