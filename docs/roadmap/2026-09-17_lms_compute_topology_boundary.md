# Roadmap — LMS compute-topology and cadence boundary

Date: 2026-09-17

## Current state

Research notes 235 and 240 establish a stronger deployed-LMS architecture boundary:

- NASA TN D-7112 (March 1973): each MSC/KSC LMS had a **three-machine digital computer complex**, with **one computer assigned exclusively to simulation of the onboard guidance computer**; NASA says the two LMSs were designed, built, and maintained to be identical;
- Brown & Waters (July 1970): each Houston/Cape Kennedy LMS had a **three-machine digital computer complex**;
- Jackson retrospective: Houston LMS complex/room had **four DDP-224 computers**.

The LMS architecture count itself is therefore well supported as three machines. The narrower four-machine physical-room observation remains unexplained and must not be rationalized without configuration records.

## What is now closed

The project may safely treat the mature deployed LMS as:

- a three-machine digital computer complex;
- one machine explicitly dedicated to onboard-guidance-computer simulation;
- separately identifiable conversion electronics, cockpit/crew station, visual system, and instructor controls;
- two site installations intended by NASA to be maintained to the same design.

This supports the existing project decomposition into causal/model/interface layers while adding one historically explicit compute-domain separation.

## What remains open

Do not yet freeze:

- exact Apollo 13 LMS serial/configuration state;
- program/model ownership for the other two DDP-224 machines;
- whether the dedicated guidance machine covered only the LGC/PGNCS or additional guidance functions;
- the reason Jackson observed four DDP-224 machines in the Houston room;
- date-specific site configuration differences despite the intended-identical design policy;
- global LMS update rate or integration step;
- subsystem-specific cadence not explicitly recovered from a model/program source.

## Retrieval priority

1. Recover/review `LMA-790-2-LMS` Volume I and Volume II / Section 7 for subsystem, program, and output ownership.
2. Search RG 255 E.155B1 for machine configuration, program loading, checkout, and acceptance records.
3. Search E.155B / adjacent visual-system holdings for computer/interface diagrams only where they identify machine ownership or update paths.
4. Recover direct LMS mathematical-model reports that state integration/update schedules.
5. If an Apollo 13-period LMS configuration list is recovered, crosswalk it against NASA TN D-7112 and Brown/Waters before admitting mission-specific implementation details.

## Admission rule

Hardware machine count alone never authorizes a causal-engine constant.

A historical cadence/configuration enters an executable model only when its applicable model/program source is recovered or when D-022 closes the gate using a valid sourced range at actual player-product resolution.

## Note-number hygiene

The LMS three-machine/guidance-allocation result is canonical as research note **240**. Research note **236** is reserved for the distinct Apollo 9 simulator-to-flight mismatch boundary.
