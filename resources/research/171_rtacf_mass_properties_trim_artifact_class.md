# Research note 171 — RTACF mass-properties trim artifact class

Date: 2026-09-15

## Question

Can contemporary primary documentation narrow the type of computational artifact that should be sought for the unresolved Apollo 13 ~59 GET CONTROL/Flight Dynamics trim disagreement, without pretending that an adjacent-mission procedure proves the Apollo 13 calculation?

## Primary-source finding

Yes, at the **artifact-class / architecture** level.

NASA MSC Internal Note 70-FM-20, *The Apollo 11 Adventure*, describes the real-time auxiliary computing facility (RTACF) computational capability used during Apollo 11. Its mass-properties entry states that mass-properties computations included **weight-c.g. tables**, and explicitly says those tables were used by the **RTACF and RTCC trajectory processors to compute pitch and yaw trim angles**.

Primary source:

- NASA Manned Spacecraft Center, Flight Dynamics Branch / Guidance Analysis Section, MSC Internal Note 70-FM-20, *The Apollo 11 Adventure*, 5 February 1970.
- Relevant RTACF computational-capability section: mass properties -> weight-c.g. tables -> RTACF/RTCC trajectory processors -> pitch/yaw trim angles.

This source predates Apollo 13 by about two months and documents the immediately preceding lunar mission's Flight Dynamics computational architecture.

## What this adds to the Apollo 13 search

The unresolved ~59 GET dispute is already source-bounded as a mass-properties-dependent DPS-trim disagreement. Note 170 established that Flight Dynamics passed `5.86 / 6.75`, LM CONTROL challenged it using premission mass properties, and CONTROL later accepted Flight Dynamics' data.

The Mission G source now identifies a concrete upstream artifact class used by Flight Dynamics for this kind of computation:

`mass-properties computation -> weight/c.g. table -> RTACF/RTCC trajectory processor -> pitch/yaw trim`

Therefore the highest-value archival target is no longer merely a generic "RTCC working sheet." Search should specifically prioritize:

- weight/c.g. tables or mass-properties computation output;
- RTACF/RTCC trajectory-processor trim output;
- associated job/request sheets or console hardcopy;
- any CONTROL-side equivalent based on premission mass properties.

These are the artifact classes most likely to expose the missing numerical input difference and competing trim.

## Evidence boundary

This is **adjacent-mission architecture evidence**, not Apollo 13 calculation provenance.

Do not infer from it that:

- Apollo 13 used exactly the same RTACF program, job number, request procedure, or printed format;
- the Apollo 13 `5.86 / 6.75` solution was necessarily generated in RTACF rather than RTCC;
- a particular T+55 weight/c.g. table produced `5.86 / 6.75`;
- the missing CONTROL alternative values can be reconstructed from Apollo 11 tables;
- Apollo 11 trim acceptance criteria apply to Apollo 13.

The Apollo 13 Mission Operations Report remains the mission-specific authority: it separately documents that RTCC LM-burn mass-property decks were updated to T+55 and that CONTROL's challenged ~59 GET calculation used premission mass properties. The direct bridge from the T+55 deck/input to the `5.86 / 6.75` calculation remains unrecovered.

## Simulator implication

No new Apollo 13 numerical constant should be implemented from this finding. It improves provenance modeling: a future historical trim calculation should expose mass-properties/weight-c.g. inputs separately from the trajectory-processor trim output, so competing source decks can produce competing candidate trims without hard-coded outcomes.

## Next unresolved item

Search Apollo 13 controller/Flight Dynamics archival material specifically for the **weight-c.g./mass-properties table and associated RTACF/RTCC trim output** behind the ~59 GET disagreement. Highest-value recovered fields remain CONTROL's alternative trim, input mass-properties identity, comparison/acceptance basis, job/request identity, and explicit T+55 linkage.