# Progress — LMS three-machine guidance allocation

Date: 2026-09-17

## Completed

Research note 244 reviewed primary NASA simulator architecture evidence in *Apollo Experience Report — Simulation of Manned Space Flight for Crew Training* (`NASA-TN-D-7112`, `MSC-S-346`, NTRS `19730011149`).

NASA defines each MSC/KSC Lunar Module Simulator as using a **three-machine digital computer complex** and states that **one computer was assigned exclusively to simulation of the onboard guidance computer**. The report also says the two LMS installations were designed, built, and maintained to be identical.

This independently confirms the three-machine description in Brown & Waters and narrows the earlier compute-topology uncertainty.

## Boundary retained

The repository does not infer:

- allocation of the other two machines;
- the exact scope of the dedicated guidance-computer simulation;
- why Jackson retrospectively describes four DDP-224 machines in the Houston LMS room;
- Apollo 13-specific configuration/effectivity;
- any global or subsystem numerical cadence.

## Documentation synchronized

Updated:

- `resources/research/244_lms_three_machine_guidance_allocation.md`
- `resources/source-catalog/LMS_DEPLOYED_COMPUTE_TOPOLOGY.md`
- `docs/roadmap/2026-09-17_lms_compute_topology_boundary.md`
- `docs/station-status/2026-09-17_lms_three_machine_guidance_allocation.md`

## Next

Prioritize `LMA-790-2-LMS` Volume I / Volume II Section 7 and configuration/program-loading records to identify program/model ownership for the remaining machines and outputs. Crosswalk any recovered machine map against Apollo 13-period effectivity before implementation.
