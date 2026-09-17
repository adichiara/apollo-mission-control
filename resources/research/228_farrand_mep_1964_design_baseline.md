# Research note 228 — Farrand MEP 1964 design-family baseline

Date: 2026-09-17
Status: **primary technical baseline recovered; LMS effectivity remains unproven**

## Question

Can the primary Farrand/NASA technical record define what “Mission Effects Projector” meant technically before the 1967 LMS review, while keeping that technology-family description separate from the delivered LMS configuration?

## Primary-source result

NASA/NTRS record `19680013122`, J. LaRussa, *The Infinity Image System in Visual Simulation*, presented at the AIAA/NASA Manned Space Flight Meeting in Houston, 4–6 November 1964, gives a direct technical description of Farrand's MEP concept.

The paper identifies the MEP as one of as many as four image-generation inputs designed into Farrand's virtual-image display. It describes the MEP as a **non-programmed continuous color film-strip projector** capable of presenting an **Earth orbital view**, including **moving cloud cover** and **sunrise/sunset simulations**. It further states that the MEP used **two film cassettes**, allowing orbital views at different scales.

Primary NTRS copy: https://ntrs.nasa.gov/api/citations/19680013122/downloads/19680013122.pdf

## Why this matters

This closes a narrow terminology/design-family question. “Mission Effects Projector” had a specific Farrand technical meaning by 1964; it was not merely a generic label for any simulator visual scene generator.

It also sharpens the 1967 retrieval question. NASA SP-4009 later records a Grumman MEP designed and built by Farrand that failed established specifications. `LLR-400-329` therefore needs to be read for explicit configuration and requirement evidence rather than reconstructed by projecting the 1964 design forward.

## Evidence boundary

The 1964 paper does **not** establish that the LMS unit reviewed in `LLR-400-329`:

- retained the same film mechanism, cassette arrangement, imagery set, scales, or control implementation;
- used the MEP for lunar-descent imagery rather than another LMS visual subsystem;
- had the same accuracy or performance requirements;
- exposes any field appearing in LMS Volume II Section 7;
- fed any Mission Control station display;
- remained unchanged for Apollo 13 training in 1970.

The 1964 design is therefore a **technology-family baseline**, not an LMS configuration specification.

## Next action

Keep `LLR-400-329` / MSC accession `*67-15490` as the controlling configuration target. On recovery, compare its hardware/configuration language against this 1964 baseline and the August 1967 specification-failure chronology, recording only explicitly supported continuities or changes.