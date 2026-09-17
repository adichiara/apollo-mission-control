# LMS deployed compute-topology sources

Status: active source catalog for deployed Lunar Module Simulator computer-complex evidence.

Related research: `resources/research/235_lms_deployed_compute_topology_boundary.md`, `resources/research/236_lms_three_machine_guidance_allocation.md`, `resources/research/238_lms_compute_growth_guidance_machine_chronology.md`, `resources/research/239_lms_handbook_archival_identity_retrieval_key.md`, `resources/research/240_lms_handbook_digitized_candidate_identity_gate.md`

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

## MSC-APOLLO-4 — *Apollo Engineering and Technology Index*, Vol. I

- Organization: NASA Manned Spacecraft Center.
- Date: July 1968.
- Source class: primary NASA/MSC bibliographic control publication.
- Grumman / `NAS9-1100` entries identify `LMA-790-2-LMS` archival targets:
  - `67-14186` — Volume I, Simulator Description;
  - `67-14187` — Volume II, Sections 1 and 4;
  - `67-14188` — Volume II, Sections 5 and 6;
  - `67-16127` — Volume II, Section 7, Simulator Output Tables.
- Supports precise archival retrieval and separation of the 1967 Grumman `NAS9-1100` handbook stream from later Kollsman `NAS9-8634` project files.
- Date-control caution: the main index gives `01-04-67` for `67-14186`/`67-14187`, while the supplement gives `15-05-67`; NASA KSC bibliography GP-642 independently lists the handbook as Apr. 1, 1967. Treat the discrepancy as unresolved rather than silently choosing a revision history.
- Does not expose handbook contents or support machine/program assignment claims by itself.

## Virtual AGC digitized LMS handbook candidate

- Collection: Virtual AGC Apollo document library.
- Discovery record: 13 February 2022 changelog entry.
- Listed title: *Lunar Module Mission Simulator Instructor's Handbook Volume I, Simulator Description*.
- Discovery URL: https://www.ibiblio.org/apollo/changes.html
- Source class: digitized-document discovery source; the underlying scan may be primary, but its archival identity has not yet been verified in this research pass.
- Discovery metadata says the document pertains to the LEM Mission Simulator at the Cape and contains switch/display and subsystem-simulation detail.
- Strongly matches the `67-14186` title, but the surfaced metadata does not itself expose `LMA-790-2-LMS`, `67-14186`, `NAS9-1100`, date/revision, or a title page.
- **Gate:** inspect the scan's title/revision/provenance pages before treating it as the MSC accession copy or extracting configuration claims.

## Tomayko — *Computers in Spaceflight: The NASA Experience*

- Author: James E. Tomayko.
- Publisher: NASA Scientific and Technical Information Division.
- Date: March 1988.
- Report: `NASA-CR-182505`.
- NTRS document ID: `19880069935`.
- Contract: `NASW-3714`.
- Source: https://ntrs.nasa.gov/citations/19880069935
- Source class: official NASA-published historical synthesis; authoritative secondary evidence, not configuration-controlled primary documentation.
- Supports:
  - Honeywell's 21 July 1966 DDP-224 simulator-complex contract;
  - an **initial allocation of two computers to the LMS**;
  - communication among the simulator computers through **8K words of common memory**;
  - later addition of a **third LMS computer**;
  - the added LMS computer simulated the onboard computer.
- Cross-source consequence:
  - this chronology is consistent with TN D-7112's mature three-machine LMS definition and its dedicated onboard-guidance-computer machine.
- Does not support:
  - exact workload/program assignment for the original two LMS machines;
  - date/site effectivity of the third-machine installation;
  - Apollo 13-specific loads, revisions, serials, or configuration;
  - an explanation for the four-DDP-224 Houston room recollection;
  - treating 8K common memory as a model cadence or product-resolution constant.

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

The **mature LMS architecture count is strongly supported as three machines** by primary NASA TN D-7112 and the contemporaneous Brown/Waters technical description. NASA TN D-7112 identifies one machine as dedicated to onboard-guidance-computer simulation. NASA's later official historical synthesis further supplies a developmental chronology: Singer-Link initially allocated two computers to the LMS and later added the third to simulate the onboard computer.

Preserve the evidence classes and the narrower unresolved physical-room discrepancy:

`NASA historical synthesis: initial LMS allocation = 2; later +1 onboard-computer simulation machine`

`NASA TN D-7112 + Brown/Waters: mature LMS = 3-machine digital computer complex`

`Jackson retrospective: 4 DDP-224 computers in the Houston LMS complex/room`

Do not invent an explanation. Original two-machine workloads, spare/maintenance/test equipment, configuration date, support role, or terminology remain unresolved until configuration records establish them.

## Architecture use

Use these sources to constrain **system decomposition**, not constants:

- computing complex;
- dedicated onboard-guidance-computer simulation role;
- conversion/interface electronics;
- crew-station hardware;
- visual system;
- instructor/simulator control.

Do not derive causal-domain count, the original two machines' program ownership, update cadence, integration step, or product latency from hardware machine count or common-memory size.

## Next targets

- inspect the Virtual AGC digitized Volume I candidate's title/revision pages and prove or reject identity with `LMA-790-2-LMS` / `67-14186`;
- if identity closes, search Volume I for DDP-224 roles, common memory, program allocation, digital conversion, and guidance-computer simulation;
- MSC accession `67-16127` — Volume II, Section 7, Simulator Output Tables;
- MSC accessions `67-14187` and `67-14188` — Volume II operating sections;
- LMS program-loading / machine-assignment records for the original two-machine workload;
- RG 255 E.155B/E.155B1 configuration and acceptance files;
- direct LMS mathematical-model documents containing integration/update schedules;
- Apollo 13-period LMS configuration records.
