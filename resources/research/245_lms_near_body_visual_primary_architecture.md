# 245 — LMS near-body visual system primary architecture

Date: 2026-09-17
Status: primary NASA system-level architecture recovered; exact subsystem naming/vendor configuration remains bounded

## Question

Can the deployed Lunar Module Simulator near-body visual architecture be constrained directly from NASA technical evidence without assuming that the 1964 Farrand MEP configuration carried unchanged into the operational LMS?

## Primary source

NASA TN D-7112, *Apollo Experience Report — Simulation of Manned Space Flight for Crew Training*, NASA Manned Spacecraft Center, March 1973, `NASA-TN-D-7112`, `MSC-S-346`, NTRS `19730011149`.

Direct NASA scan: https://ntrs.nasa.gov/api/citations/19730011149/downloads/19730011149.pdf

This is a NASA program experience report describing the Apollo crew-training simulators and their visual-simulation implementation.

## Explicit LMS findings

TN D-7112 states that, in the LMS near-body visual system:

- a **common filmstrip** was projected through **zoom optics onto four screens**;
- the altitude range from near zero to orbit was simulated by a combination of **optical zoom and film changes**;
- optical probes were mounted at a fixed distance above the screens and could articulate to scan to any point on a screen;
- at higher altitudes, additional optical elements introduced spherical distortion;
- the horizon at higher altitudes was produced by illuminating less than the full screen, while below **100,000 ft** a servomechanism-operated mirror system surrounding the screen produced the horizon;
- lunar-scene film evolved from artistic renditions, through Lunar Orbiter-updated material, to Lunar Orbiter photomosaics and then mosaics incorporating Apollo photography; and
- the final configuration described used Lunar Orbiter strips for high-altitude full-orbit scenes and Lunar Orbiter strips mosaicked with Apollo photographs for low-altitude scenes near the landing site.

The report also documents fidelity limitations. Splitting the image to four screens left each vidicon at roughly one-third to one-half of desired minimum illumination. Dynamic optical-axis wander restricted usable zoom ratio to **3**, versus a design ratio of **10**, and made registration during film changes difficult. NASA also states that continuous filmstrips with all desired information were impractical, Lunar Orbiter coverage was limited, framelet lines reproduced visibly, and sun-elevation effects could not be represented adequately in the Lunar Orbiter film material.

## Important identity boundary

TN D-7112 directly establishes this architecture for the **LMS near-body visual simulation**. In the immediately following discussion it explicitly names the analogous CMS near-body system as the Mission Effects Projector (MEP), but the recovered LMS passage itself does not require us to equate every LMS near-body element with the exact Farrand MEP hardware/configuration discussed in 1964 or with `LLR-400-329` in July 1967.

Therefore this note does **not** claim:

- that the complete LMS near-body chain described by TN D-7112 was formally named the MEP at every date;
- that its four-screen/zoom/probe implementation was unchanged from the 1964 Farrand two-cassette design;
- which vendor supplied each final optical/mechanical element;
- a Farrand→Itek→Kollsman succession;
- the exact relationship between MEP and EVDE terminology;
- DDP-224 ownership or control path;
- update cadence or computer program allocation;
- MSC/KSC identity at a specific mission date; or
- Apollo 13 effectivity.

## Consequence

This closes a major generic LMS visual-architecture uncertainty at NASA system level. We no longer need to infer the mature LMS near-body technique from the 1964 Farrand paper: NASA directly documents a common-filmstrip → zoom-optics → four-screen → articulated-probe chain, with altitude-dependent distortion/horizon mechanisms and a documented evolution of lunar imagery.

It does **not** close the July 1967 MEP configuration or vendor history. `67-15490` / `LLR-400-329` and the 30 Aug. 1967 Bethpage weekly report remain the correct primary targets for that narrower question.

No executable model constant, station product contract, or maturity grade changes from this finding. The numerical values above are descriptive historical characteristics and limitations; they are not promoted to causal-engine constants absent a player-visible requirement and applicable configuration evidence.
