# 138 — Apollo 13 PC+2 RTCC mass-property deck boundary

## Question

Can the Apollo 13 record narrow the RTCC/Flight Dynamics mass-property basis used for the PC+2 maneuver beyond the final PAD weights established in research note 137?

## Primary-source finding

NASA's *Mission Operations Report — Apollo 13* (Flight Control Division, 28 April 1970) gives two mission-specific facts that materially narrow the numerical-model boundary.

During the MCC-2-to-PC+2 narrative, the report states that the **RTCC (LM burn) mass property decks were updated to T+55 decks**.

Later, while describing a PC+2 abort PAD uplinked at approximately 59:00 GET, the report says the DPS trim passed to the crew was challenged by LM Control, but the disagreement was resolved because LM Control had used **premission mass properties**, which the report explicitly says were not the best data available.

The same report later states that the final PC+2 PAD sent near 78 hours was based on the GYM 289 vector and records the planned/actual PC+2 burn timing.

Primary source:

- NASA, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, MSC-02680.
- NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf
- Relevant material: Flight Dynamics narrative, pages B-4 through B-9.

## DOCUMENTED

- The RTCC LM-burn mass-property decks were updated to a **T+55** set before the accident/abort maneuver work.
- Premission mass properties were explicitly inferior to the then-current Flight Dynamics data for a PC+2 DPS trim calculation.
- The operational PC+2 computation therefore used an **in-flight updated mass-properties basis**, not simply a frozen premission mass set.
- The final PC+2 PAD was generated later, after the free-return burn, and the mission report identifies it as based on the GYM 289 vector.

## NOT ESTABLISHED

This source still does not establish:

- the internal field definitions of the T+55 mass-property deck;
- whether "T+55" means an exact 55:00 GET physical-state epoch, a planning/depletion-table epoch, or another RTCC naming convention;
- whether the final PAD weights of CSM 62480 lb and LM 33452 lb were copied directly from that T+55 deck or propagated from it;
- whether the PAD-weight sum 95932 lb equals exact physical vehicle mass at PC+2 ignition;
- how ullage, RCS use, consumables, venting, or the earlier free-return burn were reflected in the final targeting weights;
- the exact RTCC maneuver-integrator mass convention.

## Model consequence

Research note 137's semantic separation remains required:

`pad_weight / targeting_weight_reference != proven physical ignition mass`

But the historical input provenance is now stronger. The causal numerical model may record the Apollo 13 PC+2 regression case as using an **in-flight updated RTCC mass-properties basis**, with a documented T+55 deck lineage and documented rejection of premission mass properties for DPS trim work.

The model must not convert that lineage into an exact ignition-mass value without another source.

## Status of research-note-130 mass target

The target is narrowed again:

- final PAD weight values: resolved;
- final operational communication epoch: resolved;
- proof that PC+2 Flight Dynamics used updated in-flight rather than premission mass properties: resolved;
- named RTCC LM-burn deck lineage: resolved to T+55;
- exact deck semantics / propagation convention / physical ignition-mass epoch: unresolved.

## Next archival target

Seek the Apollo RTCC mass-properties program documentation, Apollo 13 Flight Dynamics support material, or mission-specific weight/depletion tables that define what the T+55 LM-burn deck contained and how it fed a docked DPS maneuver solution.

Adjacent evidence such as later Skylab RTCC mass-properties requirements may be used to understand architecture only; it must not be treated as Apollo 13 mission-specific proof without an applicability bridge.
