# LMS deployed compute-topology sources

Status: active source catalog for deployed Lunar Module Simulator computer-complex evidence.

Related research: `resources/research/235_lms_deployed_compute_topology_boundary.md`, `resources/research/240_lms_three_machine_guidance_allocation.md`

## NASA TN D-7112 — *Apollo Experience Report — Simulation of Manned Space Flight for Crew Training*

- Authors: C. H. Woodling et al.
- Organization: NASA Manned Spacecraft Center.
- Date: March 1973.
- Report numbers: `NASA-TN-D-7112`, `MSC-S-346`.
- NTRS document ID: `19730011149`.
- Source: https://ntrs.nasa.gov/search.jsp?R=19730011149
- Source class: primary NASA program experience report.
- Supports:
  - two LMS installations, one at MSC and one at KSC;
  - the two LMSs were designed, built, and maintained to be identical;
  - each LMS had a **three-machine digital computer complex**;
  - the computers were the same type used in the CMS;
  - **one LMS computer was assigned exclusively to simulation of the onboard guidance computer**;
  - instructor/operator console, infinity-optics display, and high-fidelity LM crew station as distinct system elements.
- Does not support:
  - program/model allocation for the other two machines;
  - an explanation for retrospective four-DDP-224 evidence from the Houston room;
  - exact Apollo 13 serial/configuration effectivity;
  - a universal simulation timestep/update rate;
  - acceptance/correlation tolerances.

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
  - resolving why the physical Houston room/complex observation differs from NASA's three-machine LMS definition;
  - exact Apollo 13 software-to-machine assignment;
  - a universal numerical cadence;
  - assuming the recalled installation state was unchanged for Apollo 13.

## Evidence boundary

The **LMS architecture count is now strongly supported as three machines** by both primary NASA TN D-7112 and the contemporaneous Brown/Waters technical description. NASA TN D-7112 additionally identifies one of those machines as dedicated to onboard-guidance-computer simulation.

Preserve the narrower unresolved physical-room discrepancy:

`NASA TN D-7112 + Brown/Waters: three-machine LMS digital computer complex`

`Jackson retrospective: four DDP-224 computers in the Houston LMS complex/room`

Do not invent an explanation. Spare/maintenance/test equipment, configuration date, support role, or terminology remain hypotheses until configuration records establish them.

## Architecture use

Use these sources to constrain **system decomposition**, not constants:

- computing complex;
- dedicated onboard-guidance-computer simulation role;
- conversion/interface electronics;
- crew-station hardware;
- visual system;
- instructor/simulator control.

Do not derive causal-domain count, the other two machines' program ownership, update cadence, integration step, or product latency from hardware machine count.

## Next targets

- `LMA-790-2-LMS` Volume I and Volume II / Section 7;
- LMS program-loading / machine-assignment records;
- RG 255 E.155B/E.155B1 configuration and acceptance files;
- direct LMS mathematical-model documents containing integration/update schedules;
- Apollo 13-period LMS configuration records.
