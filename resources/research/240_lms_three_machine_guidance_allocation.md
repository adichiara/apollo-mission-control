# Research note 240 — LMS three-machine complex and guidance-computer allocation

Date: 2026-09-17  
Status: **primary NASA architecture evidence recovered; remaining machine allocation unresolved**

## Question

Can the deployed LMS computer-count boundary be strengthened with primary NASA evidence, and does surviving evidence identify any processor role without inventing the rest of the machine allocation?

## Primary source

C. H. Woodling et al., *Apollo Experience Report — Simulation of Manned Space Flight for Crew Training*, NASA TN D-7112 / MSC-S-346, March 1973, NTRS document `19730011149`.

Primary NTRS record:

- https://ntrs.nasa.gov/search.jsp?R=19730011149
- report number: `NASA-TN-D-7112`
- report number: `MSC-S-346`

The report's Apollo-program LMS description states that:

- two LMS installations existed, one at MSC and one at KSC;
- the two simulators were **designed, built, and maintained to be identical**;
- each included an instructor/operator console, infinity-optics display system, high-fidelity LM crew station, and a **three-machine digital computer complex**;
- the LMS digital computers were the same type used in the CMS;
- **one LMS computer was assigned exclusively to simulation of the onboard guidance computer**.

This independently confirms the three-machine architecture reported contemporaneously by Brown & Waters and adds one explicit machine-role assignment.

## What this closes

For the mature Apollo LMS architecture, the project may now treat the following as primary-source-supported:

1. a three-machine LMS digital computer complex;
2. one machine in that complex dedicated to onboard-guidance-computer simulation;
3. MSC and KSC LMS designs intended to be kept identical at the system level.

The earlier Brown & Waters three-machine description is therefore no longer a lone technical-publication claim.

## What remains unresolved

Do **not** infer:

- what exact programs/models occupied the other two machines;
- whether the dedicated guidance machine simulated only the PGNCS/LGC or also any other guidance functions;
- whether Jackson's retrospective observation of four DDP-224 machines in the Houston LMS room represents a spare, support/test machine, a later/earlier configuration, or a different counting convention;
- exact Apollo 13 serial/configuration state;
- that MSC and KSC were literally configuration-identical on every date merely because NASA says they were designed, built, and maintained to be identical;
- any numerical integration or update cadence from the machine count.

Jackson's four-machine observation remains useful evidence about the physical room/complex, but it must not override the primary NASA definition of the LMS itself as a three-machine digital computer complex without a configuration record explaining the difference.

## Architecture consequence

The causal engine may represent an explicit **onboard-guidance-computer simulation domain** as historically distinct from the remainder of the LMS digital-computer workload. That does not authorize mapping the other causal domains one-to-one onto the remaining two machines.

The existing abstraction rule remains:

`hardware processor count != causal/model-domain count`

## Retrieval consequence

The next high-value target is no longer simply “find the LMS processor count.” It is:

1. recover `LMA-790-2-LMS` Volume I and Volume II/Section 7 material for program/model/output ownership;
2. recover program-loading or machine-assignment records that identify the other two machines' workloads;
3. use RG 255 E.155B1 configuration/acceptance records to establish date/site effectivity;
4. crosswalk any recovered configuration against Apollo 13 training dates before freezing mission-specific implementation details.

## Product boundary

No executable numerical constant changes from this note. The finding improves simulator architecture provenance and narrows the machine-allocation retrieval problem; it does not establish a timestep, telemetry cadence, station display rate, or Apollo 13-specific processor map.

## Numbering note

This material was originally committed as research note 236. It was renumbered to 240 on 2026-09-17 after a parallel research stream created a distinct Apollo 9 simulator-mismatch note with the same ID. The content/evidence boundary is unchanged; only the canonical note identifier changed.
