# Research note 241 — LMS deployed compute-topology boundary

Date: 2026-09-17  
Status: **REVIEWED — deployed LMS computer-complex evidence recovered; exact Apollo 13 machine allocation remains unresolved**

## Question

What does surviving evidence establish about the deployed Lunar Module Simulator computer complex, and can the project infer an exact computer count, software-domain allocation, or universal update/integration cadence from it?

## Contemporaneous technical source

Malcolm O. Brown and John G. Waters, *The Lunar Module Simulator*, **SIMULATION**, Vol. 15, No. 1, July 1970, pp. 27–29, DOI `10.1177/003754977001500110`.

The article abstract describes the operational LMS installations at **Houston and Cape Kennedy** and says that **each of the two simulators** consisted of:

- a **three-machine digital computer complex**;
- associated digital-conversion electronics;
- a crew station accurately reproducing the LM cockpit;
- an infinity-optics visual-display system; and
- an instructor-operator control console.

Source record:

- https://journals.sagepub.com/doi/10.1177/003754977001500110

This is direct, mission-era technical evidence for the deployed LMS system architecture near the Apollo 13 period.

## Retrospective first-person evidence

Albert A. Jackson, *The Lunar Module Simulator: A Personal Account of Being an Instructor*, 2022 preprint, DOI `10.13140/RG.2.2.30746.56005`.

Jackson states that he served in MSC's simulator crew-training organization from 1966 to 1970 and became the LMS Abort Guidance System instructor. His retrospective account describes the Houston LMS arriving in 1967 as a complex including the cockpit, instructor console, projectors, and **four DDP-224 computers**. A figure caption likewise identifies a room with four Honeywell DDP-224 computers driving the simulation and associated conversion/interface equipment.

Source record/full-text presentation:

- https://www.researchgate.net/publication/392195524_The_Lunar_Module_Simulator_A_Personal_Account_of_Being_an_Instructor

This is valuable first-person evidence, but it was written decades after the program and is not a configuration-controlled 1970 LMS technical record.

## The machine-count tension

The two sources therefore cannot simply be collapsed into one exact count:

`Brown & Waters, July 1970: three-machine digital computer complex`

versus

`Jackson retrospective: four DDP-224 computers in the Houston LMS complex/room`

The current evidence does **not** establish whether this difference reflects:

- different dates/configuration states;
- one machine serving a role outside what Brown and Waters called the digital-computer complex;
- site differences;
- spare/maintenance/test equipment;
- an onboard-computer simulation role treated separately from the main real-time complex; or
- retrospective imprecision.

Do not choose among those explanations without direct configuration records.

## Architecture consequence

The discrepancy strengthens, rather than weakens, the project's abstraction rule:

**hardware processor count is not a safe proxy for simulation-domain count.**

The reusable engine should continue to model causal domains and interfaces from source-described functions:

- dynamics / physical truth;
- vehicle subsystem state;
- guidance/computer behavior;
- instrumentation / telemetry / indications;
- visual/effects outputs;
- instructor/simulator control;
- external Mission Control interfaces;

rather than attempting to mirror an assumed number of DDP-224 machines.

This is consistent with research notes 215–217, which already separate program classes, integration/source hierarchy, and source-variable/output mappings.

## Cadence boundary

Neither source authorizes a universal numerical integration timestep or global model-update rate.

In particular:

- `three-machine digital computer complex` is a hardware/system description, not a numerical cadence;
- `four DDP-224 computers` is also a hardware observation, not a numerical cadence;
- the separately cataloged LMS 50-millisecond AACS integration-step study remains subsystem/context-specific evidence under research note 216.

Therefore the project must not derive a generic `1 / machine_count`, `20 Hz`, `50 ms`, or other global solver cadence from computer topology.

A historical model cadence may be frozen only when the applicable LMS model/program source states it or when D-022 closes the gate using a valid sourced range at player-product resolution.

## Apollo 13 boundary

Brown and Waters is strong evidence that a mature LMS existed at both Houston and Cape Kennedy in 1970 and that the installed system combined a digital-computer complex, conversion electronics, cockpit, visual system, and instructor console.

It does **not** establish:

- which exact DDP-224 serial/configuration was active for Apollo 13 training;
- which software/model ran on each machine;
- the exact allocation of dynamics, systems, guidance, visual, telemetry, or instructor functions among processors;
- that Houston and Cape Kennedy were configuration-identical at all dates;
- a universal simulation-loop rate;
- numerical validation/correlation tolerances.

Those remain targets for the directly identified LMS handbooks, Section 7 output tables, configuration records, and RG 255 E.155B/E.155B1 project/acceptance files.

## Project consequence

No executable causal-model constant changes from this note.

The Causal Model Lab should continue exposing each model's explicit step/update assumptions independently. If an LMS-derived historical cadence is later recovered, it should be attached to the applicable model/profile rather than treated as a property of the whole simulator merely because the LMS used multiple DDP-224 computers.

## Next retrieval targets

1. `LMA-790-2-LMS` Volume II / Section 7 for program/output ownership and identifiers;
2. LMS configuration/program-loading records that explicitly map functions to DDP-224 machines;
3. RG 255 E.155B1 technical/acceptance material, including system configuration and checkout records;
4. direct recovery of LMS mathematical-model reports with explicit integration/update schedules;
5. Apollo 13-period simulator configuration records if they survive.

## Numbering note

This material was originally research note 235. It was renumbered to 241 on 2026-09-17 because a parallel research stream independently used note 235 for the Grumman two-LMS pre-NAS9-8634 baseline. Evidence and conclusions are unchanged.
