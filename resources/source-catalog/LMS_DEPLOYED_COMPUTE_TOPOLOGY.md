# LMS deployed compute-topology sources

Status: active source catalog for deployed Lunar Module Simulator computer-complex evidence.

Related research: `resources/research/230_lms_deployed_compute_topology_boundary.md`

## Brown & Waters — *The Lunar Module Simulator*

- Authors: Malcolm O. Brown and John G. Waters.
- Publication: *SIMULATION*, Vol. 15, No. 1, July 1970, pp. 27–29.
- DOI: `10.1177/003754977001500110`.
- Source: https://journals.sagepub.com/doi/10.1177/003754977001500110
- Source class: contemporaneous technical publication.
- Supports:
  - two deployed LMS installations, Houston and Cape Kennedy;
  - each described as having a **three-machine digital computer complex**;
  - associated digital-conversion electronics;
  - accurate LM cockpit crew station;
  - infinity-optics visual display;
  - instructor-operator console.
- Does not support:
  - exact Apollo 13 DDP-224 allocation by program/model;
  - a universal simulation timestep/update rate;
  - configuration identity between sites/dates;
  - acceptance/correlation tolerances.

## Jackson — *The Lunar Module Simulator: A Personal Account of Being an Instructor*

- Author: Albert A. Jackson.
- Date: 2022.
- DOI: `10.13140/RG.2.2.30746.56005`.
- Source: https://www.researchgate.net/publication/392195524_The_Lunar_Module_Simulator_A_Personal_Account_of_Being_an_Instructor
- Source class: retrospective first-person account by a former MSC LMS instructor; not configuration-controlled program documentation.
- Supports:
  - Jackson's 1966–1970 MSC simulator-crew-training role and LMS AGS instructor experience;
  - his recollection of the Houston LMS complex including cockpit, instructor console, projectors, and **four DDP-224 computers**;
  - associated digital/analog conversion/interface equipment.
- Does not support:
  - resolving the Brown/Waters three-machine wording;
  - exact Apollo 13 software-to-machine assignment;
  - a universal numerical cadence;
  - assuming the recalled 1967 installation state was unchanged for Apollo 13.

## Evidence boundary

Preserve the unresolved source tension:

`1970 Brown/Waters: three-machine digital computer complex`

`Jackson retrospective: four DDP-224 computers in the Houston LMS complex/room`

Do not silently pick one count or invent an explanation. Possible distinctions among active machines, support machines, functional roles, configuration dates, or terminology remain hypotheses until configuration records establish them.

## Architecture use

Use these sources to constrain **system decomposition**, not constants:

- computing complex;
- conversion/interface electronics;
- crew-station hardware;
- visual system;
- instructor/simulator control.

Do not derive causal-domain count, per-domain processor ownership, update cadence, integration step, or product latency from hardware machine count.

## Next targets

- `LMA-790-2-LMS` Volume II / Section 7;
- LMS program-loading / machine-assignment records;
- RG 255 E.155B/E.155B1 configuration and acceptance files;
- direct LMS mathematical-model documents containing integration/update schedules;
- Apollo 13-period LMS configuration records.
