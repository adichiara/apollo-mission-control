# Research Note 028 — Apollo 13 Mission Techniques

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Why this source family matters

The Mission H-2 Mission Techniques documents explicitly state that they contain the **officially approved guidance and control sequence of events, data flow, and real-time decision logic for the H-2 mission**.

That makes them one of the strongest source classes for this project.

They sit between:

- Flight Mission Rules — formal decision criteria;
- spacecraft/crew procedures — detailed execution steps;
- console/display documentation — what data is visible;
- postflight reports — what actually happened.

Mission Techniques explain **how the mission team intended to reason and coordinate in real time**.

## Located H-2 documents

The public collection includes at least:

- MSC 01296 — Abort from Lunar Powered Descent and Subsequent Rendezvous
- MSC 01297 — Lunar Orbit Activities
- MSC 01520 — Lunar Descent
- MSC 01522 — Lunar Powered Ascent
- Lunar Surface Phase
- Manual Ascent
- Translunar Midcourse Corrections and Lunar Orbit Insertion
- Contingency Procedures

The documents also identify companion volumes for:

- Launch Aborts
- Earth Parking Orbit and TLI
- Transearth Injection / MCC / Entry
- Tracking Data Selection Controllers Procedures

## Mission-specific versus reusable content

The documents distinguish between:

- H-2-specific numerical limits and trajectory values;
- procedures/data flow/decision logic applicable to H-2 and subsequent missions.

This distinction is useful for the project mission-profile system.

## Lunar Descent — decision responsibility

MSC 01520 explicitly divides responsibility:

### MCC-H

Responsible for detecting **insidious, slow-drift malfunctions** and advising the crew of the resulting decision.

### Crew

Responsible for detecting errors requiring **immediate action**.

The document states that MCC-to-LM abort decision/communication delay could be as large as **20 seconds**.

### Simulation implication

A scenario should not treat ground and crew as equivalent observers.

The simulator must preserve:

- what Mission Control can detect from telemetry/trends;
- what crew can detect locally;
- communication delay/workflow where it affects a decision.

## PDI GO/NO-GO

The H-2 lunar-descent techniques define basic requirements for PDI.

A GO means the LM retains capability to:

- land;
- ascend;
- rendezvous;
- dock;

without violating mission rules.

Ground checks include:

- agreement of PGNCS and MCC-H targets;
- acceptable PGNCS alignment;
- acceptable AGS alignment relative to PGNCS;
- communications adequacy;
- proper ignition attitude;
- functioning LGC.

Importantly, loss of high-bit-rate telemetry did **not automatically require NO-GO** if guidance/navigation operation could be adequately verified through manual readout and voice.

This is an excellent example of capability-based decision logic rather than a simplistic binary equipment requirement.

## Pre-PDI ground processing

The document describes a detailed ground sequence:

- MSFN tracking after AOS;
- updated LM state-vector / landing-site vector;
- uplink to LGC;
- LM Descent Planning Table called using the MSFN state vector;
- RTCC enters high-speed computational mode at PDI - 8 minutes;
- PGNCS / AGS / MSFN differences established;
- Powered Flight Processor (PFP/Lear processor) initiated about PDI - 4 minutes;
- PFP data differenced with PGNCS velocity;
- resulting quantities displayed on **strip-chart recorders**;
- ground evaluates telemetry adequacy and advises crew.

### Simulation implication

Powered descent needs more than one LM guidance number.

The ground has several competing/confirming estimates:

- PGNCS;
- AGS;
- MSFN;
- PFP.

Diagnosis arises from their **residuals, trends, and agreement**, not merely from the absolute value of one source.

## PFP / Lear processor

The Mission Techniques document describes the PFP as an RTCC processor using Doppler observations from multiple tracking stations and Kalman-filter equations to update a state vector.

PFP data are compared with PGNCS and other sources to help isolate a degraded guidance system.

This provides strong source support for the FIDO/GUIDO/CONTROL interaction during descent.

## Landing-radar decision logic

The document contains explicit landing-radar logic.

Examples:

- no LR altitude data-good by a PGNCS altitude threshold can require abort;
- allowable altitude disagreement changes with current trajectory/system confidence;
- PGNCS/LR altitude difference must converge;
- some decisions are evaluated by the Flight Director in real time rather than through one hard numeric limit.

### Simulation implication

Flight-control decisions often use:

- a numerical threshold;
- duration/time condition;
- trend;
- corroborating source;
- controller/Flight Director judgment.

## Propellant margin

MCC-H computes predicted DPS fuel and oxidizer remaining at touchdown using:

- telemetered remaining quantity;
- expected remaining descent requirement.

The predicted margin is plotted versus time on an **analog display**.

Before high gate it is used as a general performance indicator; later it becomes a more direct landing-margin prediction.

A zero predicted margin, corroborated by another cue such as premature DES QTY indication, is abort evidence.

This is another real ground display/product that should eventually be reconstructed.

## Descent-abort Mission Techniques

MSC 01296 defines approved real-time logic for:

- PDI NO-GO aborts;
- powered-descent aborts;
- lunar-surface aborts;
- PGNCS-controlled aborts;
- AGS-controlled aborts;
- DPS versus APS use;
- engine monitoring;
- guidance/control monitoring;
- engine cutoff;
- postinsertion rendezvous.

Ground rules include:

- use DPS in an abort whenever possible;
- do not shut down a working engine before safe orbit;
- avoid short APS burns;
- maintain communications where possible.

## Multi-cue diagnosis

The abort techniques repeatedly require corroboration.

Example:

- if only one indication suggests low thrust, a second cue is required;
- if there is no second cue and MCC-H does not confirm low thrust, no action is taken.

This reinforces a core simulation principle:

> single-channel abnormal indication ≠ automatically resolved diagnosis.

## Contingency Procedures

The H-2 contingency document covers alternate/abort options across mission phases and explicitly orders contingency modes by priority.

It describes crew + MCC-H real-time decisions rather than a generic “abort mission” action.

Examples include:

- launch aborts / contingency orbit;
- translunar aborts;
- alternate mission;
- LOI abort modes;
- return-to-Earth planning;
- LM propulsion as backup in some return cases.

## Primary sources

- Lunar Descent:
  https://www.ibiblio.org/apollo/Documents/Apollo%20Mission%20Techniques%20Mission%20H-2%20and%20Subsequent%20-%20Lunar%20Descent.pdf
- Descent Abort:
  https://www.ibiblio.org/apollo/Documents/Apollo%20Mission%20Techniques%20Mission%20H-2%20and%20Subsequent%20-%20Abort%20from%20Lunar%20Powered%20Descent%20and%20Subsequent%20Rendezvous-1.pdf
- Lunar Orbit Activities:
  https://www.ibiblio.org/apollo/Documents/Apollo%20Mission%20Techniques%20Mission%20H-2%20and%20Subsequent%20-%20Lunar%20Orbit%20Activities.pdf
- Powered Ascent:
  https://www.ibiblio.org/apollo/Documents/Apollo%20Mission%20Techniques%20Mission%20H-2%20and%20Subsequent%20-%20Lunar%20Powered%20Ascent.pdf
- Contingency Procedures:
  https://www.ibiblio.org/apollo/Documents/Apollo%20Mission%20Techniques%20Mission%20H-2%20and%20Subsequent%20-%20Contingency%20Procedures.pdf
