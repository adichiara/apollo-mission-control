# Research note 144 — Apollo RTCC mass-properties depletion-table architecture

Date: 2026-09-14

## Question

Can primary RTCC requirements documentation narrow how Apollo-era mass-properties state was represented and updated, without inventing Apollo 13/H-2 `T+55` deck fields that have not been recovered?

## Primary source

NASA Manned Spacecraft Center Internal Note 71-FM-214, E. Ray Hischke, *Skylab RTCC Mass Properties System Requirements*, June 14, 1971, MSC-04378 / MSC-IN-71-FM-214 / NASA-TM-X-67442.

- NTRS record: https://ntrs.nasa.gov/citations/19720006192
- Archival scan: https://www.ibiblio.org/apollo/Documents/71-FM-214%20-%20Skylab%20RTCC%20mass%20properties%20system%20requirements.pdf

## Findings

The note states explicitly that the Skylab RTCC Mass Properties System was intended as a **carryover of the present Apollo RTCC Mass Properties System**, with only a few minor modifications and several deletions.

The documented system architecture then includes:

- computation and maintenance of spacecraft weight and center of gravity;
- a summation unit capable of combining module-level inputs;
- a vehicle input unit that computes total mass properties for display or for input to other computation units;
- a digital-autopilot unit in which engine trim angles are computed for an **input spacecraft weight**;
- centers of mass obtainable from either **temporary or permanent propellant depletion tables**; and
- depletion-table calculations in which fuel and oxidizer weights are derived from output weight, dry weight, and mixture ratio.

The source therefore supplies a stronger architectural interpretation for the Apollo 13 evidence already captured in notes 138, 142, and 143: Apollo-era RTCC mass-properties support was not merely a single scalar mission weight. It was a maintained computational state with module summation, weight/CG products, propellant-depletion-table support, and downstream trim use.

## Historical boundary

This is a 1971 Skylab requirements note describing a system explicitly intended to carry over the then-current Apollo RTCC Mass Properties System. It is valid evidence for the **Apollo-era system architecture**, but it is not an H-2 mission-specific deck listing.

Do **not** infer from this source alone:

- that Apollo 13 `T+55` was itself the name of a propellant-depletion table;
- whether `T+55` selected a temporary table, a permanent table, or some higher-level deck containing such tables;
- the exact H-2 LM module breakdown, dry weights, consumable quantities, CG values, mixture ratio, or record layout;
- the precise meaning of the `T+N` epoch convention;
- that the final P30 CSM/LM weights were direct copies of an RTCC depletion-table output.

## Simulation consequence

The causal model should continue to keep physical vehicle state separate from the mission-control mass-properties state. When a historical RTCC mass-properties layer is implemented, its abstraction should be capable of representing at least:

1. component/module mass contributions;
2. total vehicle weight and center of mass;
3. propellant depletion state/tables;
4. a time-tagged or otherwise versioned operational basis;
5. downstream trim/trajectory use.

This does **not** authorize populating H-2-specific values that remain unrecovered.

## Next archival target

The highest-value next source remains mission-specific Apollo 13/H-2 material that connects the generic architecture to the actual `T+55` LM-burn deck: RTCC requirements, mass-properties deck/listing definitions, processor input descriptions, or Flight Dynamics maneuver-support worksheets. A source defining whether `T+N` denotes table epoch, data basis, calculation epoch, or propagated reference state would close the most important remaining semantic gap.