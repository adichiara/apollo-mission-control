# Research note 304 — KSC LMS-2 DDP-224 post-Apollo disposition

Date: 2026-09-17  
Status: **PRIMARY KSC POST-APOLLO HARDWARE EVIDENCE RECOVERED; APOLLO-ERA FULL MACHINE ALLOCATION STILL UNRESOLVED**

## Question

Can primary NASA evidence narrow the physical-computer provenance of the KSC Lunar Module Simulator after Apollo, without using later disposition to invent the Apollo-era workload map?

## Primary source

John F. Kennedy Space Center, *Semiannual Progress Report, Research and Technology, 1 April–30 September 1973*, KSC-GP-421F, 1 October 1973, NASA NTRS `19740006581`.

Primary NTRS PDF:
https://ntrs.nasa.gov/api/citations/19740006581/downloads/19740006581.pdf

In its computer-systems discussion, KSC states:

> “Two DDP-224 systems, used as Flight Crew Training Simulators (LMS-2 system) during the Apollo Program, will be used as I/O processors.”

The report says these systems would also serve as main-memory storage devices for the KSC breadboard Space Ultrareliable Modular Computer (SUMC).

## What this establishes

This is direct KSC evidence that, in 1973, **two DDP-224 systems with Apollo-program LMS-2 provenance survived into a documented post-Apollo reuse path at KSC**.

It independently ties DDP-224 hardware to the KSC LMS-2 installation and provides a concrete disposition point after Apollo.

## What it does not establish

Do **not** infer from the phrase “two DDP-224 systems” that:

- LMS-2 had only two DDP-224 computers during Apollo;
- the mature three-machine LMS architecture documented by NASA TN D-7112 was wrong;
- the two retained systems were the original two simulation machines rather than some other subset;
- the dedicated onboard-guidance-computer simulation machine had been removed, retained elsewhere, or was one of these two;
- any particular DDP-224 ran vehicle dynamics, systems models, PGNCS/LGC simulation, visual-system control, or another named workload;
- the 1973 disposition describes the Houston LMS;
- the 1973 retained subset establishes Apollo 13 configuration/effectivity.

A post-program reuse statement is a **survivor/disposition record**, not a complete Apollo-era configuration list.

## Relationship to existing evidence

NASA TN D-7112 remains the stronger source for mature LMS architecture: each LMS is described as having a three-machine digital computer complex, with one computer assigned exclusively to onboard-guidance-computer simulation.

The 1973 KSC report adds a different evidence layer: at least two LMS-2-provenance DDP-224 systems were still present and selected for reuse after Apollo. These statements are compatible because the KSC report does not claim to enumerate every machine formerly in LMS-2.

Jackson's retrospective four-machine Houston-room observation remains unresolved and should likewise not be reconciled by guessing that a fourth machine was a spare or support computer.

## Project consequence

The compute-topology model should now distinguish three evidence questions explicitly:

1. **Apollo-era functional architecture** — three-machine LMS complex, one guidance-dedicated machine (TN D-7112);
2. **physical room/equipment observations** — four Houston DDP-224s retrospectively reported by Jackson;
3. **post-Apollo disposition** — two KSC LMS-2-provenance DDP-224 systems documented for reuse in 1973 (KSC-GP-421F).

These are not interchangeable counts.

No executable constants, causal-domain assignments, or station maturity grades change.

## Next target

Continue toward records that actually identify machine/program ownership and date effectivity: `LMA-790-2-LMS` Volume I/Section 7, program-loading or machine-assignment records, and RG 255 E.155B1 configuration/acceptance material. A particularly useful disposition follow-up would be a KSC property/configuration record identifying which LMS-2 DDP-224 serials/functions were retained versus removed, if such a record can be recovered.
