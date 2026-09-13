# 101 — PC+2 immediate post-burn verification and power-down boundary

Date: 2026-09-13  
Status: **RESOLVED FOR FIRST PLAYABLE — source-backed immediate post-burn sequence established**

## Question

What immediate post-burn verification and power-down activities are sufficiently documented to belong in the PC+2 first playable without inventing unsupported historical details?

## Primary evidence reviewed

### Apollo 13 Mission Operations Report

The Flight Control Division Mission Operations Report records:

- PC+2 ignition at **79:27:38.30 GET**;
- the burn as **nominal**;
- PGNS residuals of **R1 +00010, R2 +00003, R3 +00000**;
- LM power-down beginning at **79+34**, except functions needed for Passive Thermal Control (PTC);
- a detailed PTC-establishment procedure being read to the crew at **79+52**.

The same report states that the LM had been powered up for the maneuver and that post-burn operations then transitioned into transearth-coast power conservation.

### Apollo 13 PAO / air-ground chronology

At approximately **79:33 GET**, CAPCOM began reading a procedure that would "power [the LM] down a good bit," with further reductions deferred until PTC was established. The procedure explicitly retained selected communications/guidance functions needed for the next operational step.

A contemporary change-of-shift briefing adds the operational reason: controllers intended to begin the initial LM power-down roughly cutoff +15 minutes only after confirming a good, stable post-burn spacecraft. Guidance/navigation and communications remained powered long enough to establish PTC; tracking later provided an additional assessment of maneuver performance.

## First-playable interpretation

The immediate post-burn phase should be represented as a **sequence**, not as an instantaneous successful-burn flag followed by generic shutdown:

1. **burn cutoff / maneuver result available**;
2. **initial onboard/ground post-burn assessment**, including sourced PGNS residuals for the nominal branch;
3. **FLIGHT/controller confirmation that the spacecraft is suitable to leave burn configuration**;
4. **initial LM power-down begins**, while functions required for communications, guidance/navigation, and PTC setup remain available;
5. **PTC setup becomes the next operational objective**;
6. **later tracking refines trajectory performance**, but this is outside the minimum immediate post-burn first-playable closure unless physical play shows it is needed.

## Evidence limits

Do **not** infer or invent:

- exact MOCR console keying used to assess the residuals;
- an exact controller-by-controller verbal poll after cutoff unless directly sourced;
- exact current draw at each individual switch transition beyond values explicitly documented in sources;
- exact timing of every power-down switch operation;
- a full PTC dynamics model for the first playable;
- an invented automatic rule that a nominal residual vector itself authorizes power-down.

The historical record supports the operational ordering and timing envelope, not every internal controller action.

## Implementation / play boundary

For the current first playable, the important player-facing requirement is that a nominal PC+2 does **not** end at engine cutoff. Players must recognize a short post-burn verification state and transition into a source-bounded power-conservation/PTC-preparation state.

The existing first-playable model need not add a full PTC simulator before physical play. Physical validation should first determine whether the post-burn transition needs additional station-specific products, actions, or handoffs.

## Open-question effect

Open question 35 is resolved **for the current first playable**. Additional post-burn detail is demand-driven by physical play or later transearth-coast scenarios.