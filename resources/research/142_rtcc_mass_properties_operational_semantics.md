# 142 — RTCC/RTACF mass-properties operational-semantics boundary

## Question

What can primary Apollo-era operations documentation establish about the function of mission mass-properties products, and how far does that let us interpret the Apollo 13 Flight Dynamics statement that LM-burn mass-property decks were updated to `T+55` decks?

## Primary-source findings

### Apollo 10 Real-Time Auxiliary Computing Facility operational support plan

The Apollo 10 RTACF support plan describes a Mass Properties / RCS-SPS computational path in which spacecraft weight and mass properties are operational inputs to propulsion/control support. For the SM RCS predicted-propellant-profile function, the Mass Properties, RCS/SPS (MRS) program used spacecraft weight, total RCS propellant, spacecraft mass properties, and a mission-event timeline. As propellant was expended and vehicle configuration changed during flight, the RCS computation accepted updated inputs from the mass-properties portion of the program.

The plan also identifies mass-properties-derived products used for maneuver/control work, including pitch/yaw trim and DAP-related support.

Archival scan: https://www.ibiblio.org/apollo/Documents/Operational%20Support%20Plan%20for%20the%20Real-Time%20Auxiliary%20Computing%20Facility%20Apollo%2010%20Flight%20Annex.pdf

### Apollo 11 Mission Operations Report

The Apollo 11 Mission Operations Report describes the RTACF mass-properties capability as producing, among other outputs, **weight-c.g. tables** used by RTACF and RTCC trajectory processors to compute pitch and yaw trim angles, together with entry-aerodynamics and DAP-load support products.

Mission-document index: https://www.apollojournals.org/afj/ap11fj/a11-documents.html

### Apollo 13 Flight Control Division report

The mission-specific Apollo 13 Flight Control Division report states that LM-burn mass-property decks were updated to `T+55` decks, and later records that LM Control initially challenged the PC+2 DPS trim because it had used premission mass properties rather than the better data then available.

Primary scan: https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf

## What this establishes

Across Apollo operations documentation, `mass properties` were not merely bookkeeping weights. They were operational computational inputs/products connected to trajectory, trim, DAP/control, and propellant-support calculations, and they could be updated as propellant state and vehicle configuration changed.

That context makes the Apollo 13 `T+55` update operationally meaningful: Flight Dynamics was replacing an earlier mass-properties basis with a later in-flight basis before the abort-maneuver work, and the resulting difference was material enough to affect the DPS trim passed for PC+2.

## Evidence boundary

The reviewed sources do **not** establish:

- the exact definition of `T+55` in the Apollo 13 deck name;
- whether `T+55` denotes a single epoch, a deck-generation time, a propagated state, or another configuration-control convention;
- the H-2 deck record layout or individual mass-property entries;
- the exact equations by which the deck generated the final PC+2 CSM/LM P30 weights;
- whether the final PAD weights are identical to physical ignition mass;
- which Apollo 13 RTCC processor consumed each specific LM-burn deck field.

Do not infer those details from Apollo 10/11 support documents.

## Model consequence

The project can now treat the PC+2 mass-property input as an **in-flight updated operational state product** rather than a fixed launch/preflight constant. The simulator architecture should preserve separate concepts for:

1. physical vehicle mass and center of gravity;
2. mission-control mass-properties state/deck;
3. targeting/P30 weight values derived or selected for a maneuver;
4. controller-visible trim and trajectory products.

The historical regression fixture may use the documented final P30 weights as targeting references, but must not label them exact ignition mass until the H-2 deck semantics or equivalent mission-specific calculation records are recovered.

## Next archival target

Highest-value documents are now mission-specific H-2 RTCC/Flight Dynamics mass-properties requirements, deck definitions/listings, or auxiliary-computing documentation that explicitly defines `T+55` and the LM-burn deck fields. Search terms should include `Apollo 13`, `H-2`, `mass properties`, `LM burn`, `T+55`, `RTCC`, `RTACF/ACF`, `trim`, and `P30`.
