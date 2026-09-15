# Research note 150 — Apollo 12 RTCC per-maneuver mass-properties workflow boundary

Date: 2026-09-14

## Question

Can primary Apollo documentation closer to H-2 narrow where operational mass-properties calculations were performed and when they were refreshed, without assuming undocumented Apollo 13 implementation details?

## Primary source

NASA Manned Spacecraft Center, Apollo 12 Flight Control Division postflight report, RETRO section, General item 1.

Archival scan: https://www.ibiblio.org/apollo/Documents/Apollo_12_Postflight_Report_RETRO.pdf

## Finding

The Apollo 12 RETRO postflight report states that **mass properties were computed in an offline computer by the RTCC controllers in lieu of the RTACF**. It further states that the resulting SPS trim values agreed to less than 0.1 degree with onboard postburn values for both CSM-alone and docked configurations, and explicitly says that **mass properties were run prior to each maneuver**.

This is a significant refinement of the architecture established in research note 149. Apollo 11 documentation showed an RTACF/RTCC processor path from weight/CG tables to pitch/yaw trim. Apollo 12 mission-specific postflight documentation shows that, by the immediately preceding mission, the operational mass-properties computation had been performed by **RTCC controllers using an offline computer in lieu of RTACF**, with a **per-maneuver run cadence**.

A sourced late-Apollo operational chain can therefore be represented as:

`current mass-properties basis -> controller-initiated pre-maneuver mass-properties run -> derived trim product -> maneuver support`

with the computational venue/provenance itself retained as metadata.

## Apollo 13 consequence

This evidence is much closer in mission sequence to Apollo 13 than the Apollo 11 RTACF architecture and is mechanically consistent with the H-2 Flight Control Division report's references to RTCC mass-property decks, updated `T+55` decks, and a PC+2 trim dispute caused by LM Control using premission mass properties.

It does **not**, however, prove that Apollo 13 used the identical Apollo 12 offline program, staffing procedure, run cadence, table layout, or constants. The H-2 source still must control mission-specific assertions.

The simulator may safely model mass-properties/trim products as **versioned calculation runs associated with maneuver support**, rather than as timeless constants. For Apollo 13 specifically, the provenance state must remain explicit so a stale premission basis can coexist with a newer Flight Dynamics basis.

## Boundary retained

Do not infer:

- that every Apollo 13 maneuver had a fresh mass-properties run solely because Apollo 12 did;
- that the accepted ~59-hour PC+2 trim was generated from the `T+55` deck;
- that `T+55` identifies the run time rather than a reference state/epoch;
- exact H-2 weight/CG fields, depletion-table contents, processor implementation, or run commands;
- that the P30 `62,480 / 33,452 lb` values were direct outputs of the Apollo 12-described mass-properties program;
- any numerical explanation for the 508-lb difference between the P30 sum and postflight reconstructed PC+2 ignition mass.

## Simulation implication

Add a distinction between **mass-properties state** and a **mass-properties calculation run**. A run should carry at minimum:

1. mission-relative reference state/epoch;
2. input/deck provenance;
3. calculation venue/version provenance;
4. maneuver association when documented or scenario-defined;
5. derived weight/CG and trim products;
6. freshness/staleness relative to competing console products.

This creates a historically grounded mechanism for the Apollo 13 PC+2 cross-console disagreement without inventing hidden H-2 fields.

## Next archival target

Continue searching for Apollo 13/H-2 RTCC controller procedures, mass-properties run sheets/listings, Flight Dynamics worksheets, or processor documentation that explicitly connects a pre-PC+2 run to the `T+55` state and to the accepted DPS trim and/or final P30 module weights.