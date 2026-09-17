# Research note 238 — LMS compute growth and guidance-machine chronology

Date: 2026-09-17  
Status: **official NASA historical synthesis narrows three-machine chronology; exact two-machine workload remains unresolved**

## Question

Can the unresolved LMS three-machine topology be narrowed further: was the guidance-computer machine part of the original computer allocation, or was it added to an earlier two-machine LMS complex?

## Primary-source-first search

The retrieval pass first targeted `LMA-790-2-LMS`, DDP-224 machine-assignment records, and exact LMS program-loading/configuration material. No directly inspectable primary configuration record was recovered in this pass that names the two original machine workloads.

The strongest newly recovered evidence is therefore kept in its proper class: an official NASA historical synthesis, not promoted to configuration-controlled primary evidence.

## NASA source

James E. Tomayko, *Computers in Spaceflight: The NASA Experience*, NASA-CR-182505, March 1988, NTRS document `19880069935`, prepared for NASA under contract `NASW-3714` and published by NASA Scientific and Technical Information Division.

Primary NASA NTRS record:

- https://ntrs.nasa.gov/citations/19880069935
- report number: `NASA-CR-182505`
- contract: `NASW-3714`

In the Apollo mission-simulator discussion, Tomayko reports that:

- Honeywell received a $4.2 million contract on 21 July 1966 to supply DDP-224 computers for the simulator complexes;
- Singer-Link initially allocated **two computers to the Lunar Module Simulator**;
- the computers could communicate through **8K words of common memory**;
- **a third computer was later added to the LMS**;
- the added LMS computer simulated the onboard computer.

This chronology is consistent with NASA TN D-7112's later mature-system description of a three-machine LMS complex with one computer assigned exclusively to onboard-guidance-computer simulation.

## What this closes

The mature three-machine architecture need not be treated as an unexplained static count. The official NASA historical record supports a developmental sequence:

`initial LMS allocation: 2 computers`

`later LMS allocation: +1 computer for onboard-computer simulation`

`mature LMS: 3-machine complex, one machine dedicated to onboard-guidance-computer simulation`

This also provides a historically grounded explanation for why the guidance simulation can be represented as a distinct compute role without assigning the other two machines by guesswork.

## What remains unresolved

Do **not** infer:

- the exact programs/models assigned to either of the original two LMS computers;
- that the added computer simulated only PGNCS/LGC rather than every function encompassed by the source's term “on-board computer”;
- the date on which the third LMS machine became operational;
- whether the initial two-machine allocation was ever the exact fielded configuration used for crew training;
- Apollo 13-specific machine serials, loads, revisions, or configuration;
- why Albert Jackson later recalled four DDP-224 computers in the Houston LMS room;
- that the 8K common-memory architecture remained unchanged through every Apollo LMS configuration;
- any integration timestep, model execution cadence, display rate, or telemetry rate.

The four-machine room observation remains a separate physical/configuration question. This source does not justify labeling a fourth machine as spare, maintenance, test, or support equipment.

## Evidence-class boundary

`NASA-CR-182505` is an official NASA-published historical study based on cited archival/interview evidence. It is authoritative secondary evidence, not a contemporaneous configuration record. Where it supplies chronology absent from currently recovered primary records, preserve that evidence class explicitly.

The next retrieval priority remains direct contractor/NASA configuration documentation (`LMA-790-2-LMS`, program-loading records, and RG 255 E.155B1) capable of identifying the original two machine workloads and date/site effectivity.

## Architecture consequence

The causal engine may preserve the mature LMS architecture as:

- a general simulation-compute domain spanning two historically unallocated machines at the present evidence resolution; plus
- a distinct onboard-guidance-computer simulation machine/domain.

This is a documentation boundary, not a requirement to reproduce physical processor partitioning in executable code.

## Product boundary

No executable numerical constant changes from this note. The 8K common-memory figure is architecture evidence only and does not establish model cadence, state-vector resolution, station product latency, or Apollo 13-specific behavior.
