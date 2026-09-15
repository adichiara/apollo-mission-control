# Station research status — PC+2 retained-GDA rationale

Date: 2026-09-15  
Research note: `resources/research/165_pc2_retained_gda_rationale.md`

## CONTROL

**Status: operational rationale substantially resolved; numerical provenance unresolved.**

Primary CONTROL postflight reporting states that the ground expected the GDA settings at the end of the report's `MCC-3`, with 40% thrust compliance, to provide optimum GDA alignment for PC+2. The unexpected roll-GDA motion at PC+2 ignition therefore occurred against an explicit retained-state expectation.

Do not substitute an inferred exact retained pair for the documented rationale.

## FLIGHT

**Status: final disposition resolved.**

The Flight Director narrative independently records the ground rule that no PC+2 maneuver trims were required. CONTROL now supplies an operational engineering rationale consistent with that disposition.

## Flight Dynamics / RTCC

**Status: unresolved upstream calculation.**

T+55 LM-burn mass-property decks are documented, but the calculation/job connecting those data to a PC+2 candidate/reference trim comparison has not been recovered.

## Simulator implication

A scenario may model a controller decision to retain an existing GDA state because it is judged already optimum after prior powered-flight compliance. It must not present a fabricated comparison tolerance, candidate trim, or RTCC job as historical fact.