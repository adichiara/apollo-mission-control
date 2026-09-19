# Station-status addendum — Apollo 11 P66 / PCR-700

Date: 2026-09-19
Research: 329

The Apollo 13 station maturity table remains unchanged. This addendum applies only to the D-024 Apollo 11 powered-descent reference.

## New supported vehicle/guidance fact

Apollo 11 LUMINARY 99 carried the PCR-700 P66 lag-compensation mechanism: MIT implementation records identify `LAG/TAU`, and the Mission G prelaunch erasable load supplies `LAG/TAU = 0.413333`.

## Station-facing boundary

This does **not** establish a new GUIDO, CONTROL, FLIGHT, or other MCC player product. It also does not establish a ground display cadence or prove the January SCB proposal's once-per-second HDOT display behavior in the final flight configuration.

Accordingly:

- no station maturity grade changes;
- no controller display field is added;
- no player-visible cadence is frozen;
- no executable station projection changes.

The remaining station-relevant question is whether recovered final R-567 Section 5 / associated Apollo 11 documentation maps any of these guidance internals to a sourced controller-visible product at the resolution required by the simulation.
