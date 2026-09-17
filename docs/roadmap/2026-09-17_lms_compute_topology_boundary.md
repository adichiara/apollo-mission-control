# Roadmap — LMS compute-topology and cadence boundary

Date: 2026-09-17

## Current state

Research note 235 adds a deployed-LMS architecture boundary:

- Brown & Waters (July 1970): each Houston/Cape Kennedy LMS had a **three-machine digital computer complex**;
- Jackson retrospective: Houston LMS complex/room had **four DDP-224 computers**.

The discrepancy is intentionally unresolved.

## What is now closed

The project may safely treat the deployed LMS as a multi-computer system with separately identifiable conversion electronics, cockpit/crew station, visual system, and instructor controls.

This is enough to support the existing project decomposition into causal/model/interface layers.

## What remains open

Do not yet freeze:

- exact Apollo 13 LMS processor count/configuration;
- DDP-224 machine-to-program/model ownership;
- site-specific configuration differences;
- which machine, if any, was outside the 'three-machine' complex terminology;
- global LMS update rate or integration step;
- subsystem-specific cadence not explicitly recovered from a model/program source.

## Retrieval priority

1. Recover `LMA-790-2-LMS` Volume II / Section 7 and extract program/output identifiers.
2. Search RG 255 E.155B1 for machine configuration, program loading, checkout, and acceptance records.
3. Search E.155B / adjacent visual-system holdings for computer/interface diagrams only where they identify machine ownership or update paths.
4. Recover direct LMS mathematical-model reports that state integration/update schedules.
5. If an Apollo 13-period LMS configuration list is recovered, crosswalk it against the mature 1970 Brown/Waters architecture description.

## Admission rule

Hardware machine count alone never authorizes a causal-engine constant.

A historical cadence/configuration enters an executable model only when its applicable model/program source is recovered or when D-022 closes the gate using a valid sourced range at actual player-product resolution.
