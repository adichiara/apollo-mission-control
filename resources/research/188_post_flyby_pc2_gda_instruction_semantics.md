# Research Note 188 — Post-flyby PC+2 GDA instruction semantics

Date: 2026-09-16

## Question

Can the post-61:29 `5.85 / 6.74` PC+2 pair be classified more precisely from the primary NASA transcript?

## Primary source

NASA, *Apollo 13 Mission Commentary / Air-to-Ground Transcript*, 14 April 1970, page headed GET 63:00:00.

NASA-hosted searchable transcript result:
https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf

## Finding

Yes. The primary transcript attributes the statement to **CAPCOM**, not the crew. CAPCOM introduces a **new PC+2 P30 maneuver pad** and says:

> `Your GDA ought to be okay as it is from the last burn but pitch ought to be at 5.85, in roll it's 6.74.`

The same pad gives PC+2 TIG `079:27:40.13`, DPS propulsion, and the throttle sequence.

This improves the classification of `5.85 / 6.74`:

- it is a **ground-passed PC+2 GDA target/reference on a new P30 maneuver pad**;
- CAPCOM explicitly connects the no-action disposition (`okay as it is`) to the state left by the previous 61:29 DPS burn;
- the axes in this transcript are **pitch** and **roll**;
- it is not a crew-originated estimate and not measured actuator telemetry.

## Correction to earlier repository wording

Research note 169 relied on a searchable/OCR rendering that read approximately `which hopefully is Pitch, 5.85 Yaw 6.74`, and therefore classified the pair as a crew-qualified readback with a `Yaw` transcription caveat.

The NASA transcript text recovered in this pass is clearer and internally coherent with the operational exchange: CAPCOM is the speaker, the axis is `roll`, and the values are stated as what the GDA `ought to be` on the new PC+2 pad. Repository summaries should use this stronger source rendering and retire the `hopefully`/`Yaw` caveat for this event.

## What this does not prove

The source still does **not** establish:

- that `5.85 / 6.74` came from a newly executed mass-properties/trim computation rather than a retained/updated reference;
- the RTCC/RTACF job/run or input deck;
- the numerical GDA state measured after the 61:29 burn;
- a `0.01°` acceptance threshold merely because this pair differs from `5.86 / 6.75` by `0.01°` on each axis;
- CONTROL's competing ~59 GET numerical trim or its comparison criterion.

## Simulation implication

Represent `5.85 / 6.74` as a **ground-issued PC+2 desired/reference GDA pair with an explicit `okay as it is from the last burn` disposition**. Keep it distinct from physical actuator telemetry and from any inferred RTCC calculation product.

## Next target

The highest-value unresolved artifact remains the T+55 LM-burn mass-properties deck -> run/request/output -> Flight Dynamics trim lineage, including CONTROL's competing numerical solution and the comparison/acceptance basis.