# Roadmap — LMS compute growth chronology

Date: 2026-09-17

## Current state

Research notes 235, 236, and 238 now constrain LMS compute topology at three levels:

- primary NASA TN D-7112: mature MSC/KSC LMS = **three-machine digital computer complex**, with one machine assigned exclusively to onboard-guidance-computer simulation;
- contemporaneous Brown & Waters: deployed Houston/Cape LMS = **three-machine digital computer complex**;
- official NASA historical synthesis (Tomayko): Singer-Link initially allocated **two computers** to the LMS and **later added a third to simulate the onboard computer**; simulator computers communicated through 8K words of common memory.

The remaining machine-allocation problem is therefore no longer “what was the LMS computer count?” It is “what workloads occupied the original two machines, when was the third machine introduced at each site, and what explains the separate four-DDP-224 Houston room recollection?”

## Priority order

1. Recover `LMA-790-2-LMS` Volume I and Volume II/Section 7 material naming program/model/output ownership.
2. Recover LMS program-loading, DDP-224 assignment, or configuration-control records that identify the original two machine workloads.
3. Recover RG 255 E.155B1 acceptance/configuration records for site/date effectivity.
4. Crosswalk the resulting configuration against Apollo 13 training dates.
5. Only then decide whether any physical processor partitioning matters to the causal-engine implementation.

## Hard boundary

Do not infer:

- original two-machine workload from generic LM subsystem groupings;
- that the added machine was PGNCS/LGC-only unless a source narrows “onboard computer” accordingly;
- a role for Jackson's fourth Houston DDP-224;
- Apollo 13 effectivity from mature-system descriptions;
- numerical timestep/update behavior from processor count or 8K common-memory capacity.

## Implementation consequence

Keep the site-facing causal-engine test/model pages processor-agnostic unless a historically meaningful player-visible behavior depends on processor partitioning. The documented topology currently constrains provenance and architecture, not an executable timing constant.
