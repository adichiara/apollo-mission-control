# Research Note 189 — RTACF mass-properties processor contract

Date: 2026-09-16

## Question

What does contemporary primary documentation establish about the operational relationship between Apollo mass-properties products and downstream pitch/yaw trim computation, and does that close the Apollo 13 T+55 -> `5.86 / 6.75` provenance gap?

## Primary sources

1. NASA Manned Spacecraft Center, *Operational Support Plan for the Real-Time Auxiliary Computing Facility — Apollo 10 Flight Annex*.
2. NASA MSC Internal Note 70-FM-20, *The Apollo 11 Adventure*, 5 February 1970.
3. NASA/MSC Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970.

## Findings

The Apollo 10 RTACF operational-support plan describes the Systems program family as updating CSM and LM mass properties to reflect consumables usage and vehicle reconfiguration. It states that one program computes mass properties of the CSM/LM for a specified configuration.

The Apollo 11 mission-support description independently states that mass-properties computations produced **weight-c.g. tables**, and that those tables were used by **RTACF and RTCC trajectory processors to compute pitch and yaw trim angles**. It also lists a constants-update capability for updating RTACF constants including mass-properties tables.

Apollo 13's mission-specific Flight Dynamics chronology states that:

- T-6 mass properties were generated and loaded in the RTCC;
- T+25 RTCC mass properties were run and pitch/yaw trims compared with T+6;
- RTCC **LM-burn mass-property decks** were later updated to T+55 decks;
- the ~59 GET PC+2 DPS trim passed to the crew was challenged by LM CONTROL, which had used premission mass properties; CONTROL later agreed with Flight Dynamics' data because the premission set was not the best available.

## Interpretation

The cross-mission primary architecture now supports a tighter operational model than a generic association: Apollo RTACF mass-properties processing maintained configuration/consumables-sensitive CSM/LM mass-property data, and weight-c.g. tables were explicit inputs to RTACF/RTCC trajectory processors that computed pitch/yaw trim angles.

This makes the Apollo 13 T+55 **LM-burn** deck update exactly the right class of upstream product for a later LM DPS trim calculation. It also makes the documented CONTROL disagreement causally coherent: a premission mass-properties basis could yield a different trim from a current operational mass-properties basis.

However, this does **not** prove that the T+55 deck was the specific dataset consumed by the run that produced `5.86 / 6.75`. The Apollo 13 chronology still does not identify the downstream request/run, print the weight-c.g. table, give a job identifier, or state that the `5.86 / 6.75` solution consumed T+55. The repository must therefore preserve the distinction between **architecturally expected lineage** and **mission-specific demonstrated lineage**.

## Modeling consequence

The causal engine may represent the historically documented processor contract:

`configuration + consumables -> mass-properties product / weight-c.g. table -> RTACF/RTCC trajectory processor -> pitch/yaw trim`

For Apollo 13, `T+55 LM-burn deck updated` may populate the upstream mass-properties state, but `run_consumed = true` and a direct provenance edge to `5.86 / 6.75` remain unresolved. CONTROL's premission basis may be represented as a competing input-state class, but its numerical trim output remains unknown.

## Next target

Continue seeking an Apollo 13-specific T+55 weight/c.g. sheet, RTACF/RTCC request/output, controller working paper, or console/support-room record that explicitly ties the current mass-properties set to the ~59 GET Flight Dynamics trim. Highest-value missing fields remain the exact T+55 values, CONTROL's competing trim, run/job identity, and the ground-computation comparison/acceptance basis.