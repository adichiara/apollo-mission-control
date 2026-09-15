# Research note 149 — Apollo RTACF weight/CG-to-trim product boundary

Date: 2026-09-14

## Question

Can Apollo-era primary documentation narrow how operational mass-properties state became a controller-visible engine-trim product, without inventing Apollo 13/H-2 deck fields or values?

## Primary source

NASA Manned Spacecraft Center, Mission Planning and Analysis Division Apollo 11 mission-operations material preserved in the NARA Software collection, section **Mission Support Section**, pp. 2-79 ff.

Archival scan: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf

## Finding

The Mission Support Section describes the Real-Time Auxiliary Computing Facility (RTACF) computational capability used for Apollo 11. Under **Mass properties**, it explicitly identifies **weight-c.g. tables** and states that they were used by the **RTACF and RTCC trajectory processors to compute pitch and yaw trim angles**. The same list identifies entry-aerodynamics and DAP-load mass-properties products. A separate **constants update** capability updated RTACF constants including **mass-properties tables, aerodynamic tables, and thrust parameters**.

This is a stronger operational data-flow statement than the generic conclusion that mass properties merely "supported trim." It establishes, for Apollo operational support architecture, a documented chain:

`mass-properties weight/CG tables -> RTACF/RTCC trajectory processors -> pitch/yaw trim angles`

and separately shows that mass-properties tables and thrust parameters were updateable computational inputs.

## Apollo 13 consequence

This does **not** prove that Apollo 13 used an unchanged Apollo 11 processor implementation, nor does it identify the H-2 `T+55` deck, the accepted ~59-hour PC+2 trim basis, or the final P30 module-weight calculation. It does, however, make the Apollo 13 Flight Control Division report's stale-premission-mass-properties trim dispute mechanically coherent without speculation: a change in the provenance/version of weight/CG mass-properties inputs can legitimately change a derived pitch/yaw trim product.

The simulator may therefore model trim as a **derived product with explicit mass-properties-input provenance**, rather than storing trim and spacecraft weight as unrelated historical constants.

## Boundary retained

Do not infer:

- exact H-2 weight/CG table fields or record layout;
- that `T+55` was the specific table used for the accepted ~59-hour trim;
- that the P30 `62,480 / 33,452 lb` values were direct fields in a weight/CG table;
- that Apollo 11 RTACF software, constants, or table values were unchanged for Apollo 13;
- any numerical explanation for the 508-lb difference between the P30 module-weight sum and the postflight reconstructed PC+2 ignition mass.

## Simulation implication

Represent the operational lineage explicitly:

1. mass-properties state/deck with epoch and provenance;
2. weight/CG table/product derived from that state;
3. trajectory/trim processor invocation with versioned inputs;
4. pitch/yaw trim output presented to the relevant controller workflow;
5. challenge/reconciliation when another console's product was generated from a different or stale mass-properties basis.

This supports historically grounded failure modes in which the physical vehicle is unchanged but a stale computational basis produces a discrepant trim.

## Next archival target

Continue searching for Apollo 13/H-2 RTCC or RTACF processor descriptions, weight/CG listings, maneuver worksheets, or support-room records that connect the mission-specific `T+55` mass-properties state to the accepted PC+2 trim and/or final P30 module weights.