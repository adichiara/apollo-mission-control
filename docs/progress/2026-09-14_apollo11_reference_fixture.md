# Progress — Apollo 11 descent reference fixture

Date: 2026-09-14

## Completed

- Added a source-bounded Apollo 11 powered-descent/program-alarm reference fixture covering 102:37:30 through P66 at 102:43:22 GET.
- Linked it to the partial Apollo 11 Mission G profile (`apollo11_g`).
- Assigned the planned runtime adapter ID `apollo11_descent_v1` without implementing or registering that adapter.
- Preserved actual-flight event chronology separately from the incompletely documented final preflight SimSup program-alarm case.
- Added tests proving the reference is:
  - discoverable in the scenario catalog;
  - associated with Apollo 11 / Mission G;
  - reported as non-default and non-executable;
  - rejected by session creation with an unsupported-runtime error.

## Consequence

The catalog now contains two historically grounded mission/scenario references with different mission profiles, while only one is executable.

This is an intentional architecture test: historical research can define and expose a future scenario without forcing unfinished scenario-specific physics or procedures into the live runtime.

## Boundary retained

The Apollo 11 reference fixture does not implement:

- lunar-descent trajectory propagation;
- landing-radar measurement physics;
- LGC restart/program-alarm mechanics;
- PGNS/AGS station products;
- Apollo 11 station presentation;
- the exact preflight program-alarm SimSup case.

## Next

Use this reference fixture to develop the minimum source-bounded guidance/radar/observation primitives needed for a future `apollo11_descent_v1` adapter.
