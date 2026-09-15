# 202 — Apollo 11 landing-radar update boundary

## Purpose

Narrow the landing-radar causal interface required by the Apollo 11 powered-descent reference without prematurely implementing radar hardware or a guidance-state estimator.

## Source-backed operational sequence

The Apollo 11 Mission Report event table distinguishes:

- 102:37:51 — landing-radar data good;
- 102:38:45 — enable radar updates;
- 102:38:50 — velocity less than 2000 ft/s, start landing-radar velocity update.

This establishes that radar availability/quality, permission to incorporate radar, and velocity-update eligibility are distinct states.

Apollo guidance documentation describes the same structure more generally: inertial data alone are used until radar incorporation is allowed; altitude measurements then participate in state updating, while velocity measurements are additionally conditioned on an estimated-speed criterion during the braking phase.

## Model consequence

The reusable model now stops at **eligibility for estimator processing**.

It does not:

- generate radar measurements;
- decide whether a radar return is physically valid;
- directly overwrite the guidance state vector;
- reproduce Apollo weighting functions;
- encode Apollo 11's 2000-ft/s threshold as a universal constant.

This preserves the architecture:

`physical trajectory -> radar measurement/quality -> update gating -> estimator/filter -> guidance state -> controller observation`

## Apollo 11 readiness consequence

The Apollo 11 `landing_radar` domain remains **partial**.

Implemented generically:

- data-good gate;
- crew/guidance update-enable gate;
- altitude/velocity channel separation;
- optional velocity-update speed threshold.

Still unresolved historically:

- LM-5 radar measurement generation/error behavior;
- reasonability tests and flags;
- Apollo 11 weighting/filter behavior;
- exact guidance-cycle processing;
- controller-visible radar/guidance products.

## Sources

- NASA, *Apollo 11 Mission Report*, November 1969, Table 5-I.
- Apollo Guidance and Navigation / Luminary guidance-equation documentation for powered descent and state-vector updating.
- Apollo 11 landing transcript for crew reports of radar lock/data quality.
