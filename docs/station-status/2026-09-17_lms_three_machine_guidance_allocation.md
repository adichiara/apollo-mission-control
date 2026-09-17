# Station-status addendum — LMS three-machine guidance allocation

Date: 2026-09-17  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical Mission Control station maturity grades remain unchanged.

Research note 240 strengthens the simulator-side architecture used to generate training inputs/products: primary NASA TN D-7112 defines the mature LMS as a three-machine digital computer complex and explicitly assigns one machine to onboard-guidance-computer simulation.

## Station consequence

This does **not** establish any new Apollo 13 console display, telemetry parameter, controller procedure, or station-specific update cadence. It therefore does not justify changing any station reconstruction grade.

It does strengthen the provenance boundary behind integrated simulation: simulator guidance behavior could be represented by a distinct dedicated compute role before information reached external Mission Control interfaces.

## Open boundary

Do not map CONTROL, GUIDO, TELMU, GNC, or any other station product directly to a specific LMS DDP-224 machine. Mission Control routing/product generation remains a separate evidence problem.

The next useful station-facing evidence would be a configuration/output/interface source that connects LMS program/model outputs to MCC/RTCC inputs or named controller products.
