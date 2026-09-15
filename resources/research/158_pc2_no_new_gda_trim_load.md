# Research note 158 — PC+2 deliberately omitted a new GDA trim load

Date: 2026-09-15

## Question

Was there actually a later PC+2 commanded angular trim product to recover after the 61:29 free-return burn?

## Primary evidence

### Apollo 13 air-to-ground transcript — PC+2 activation procedure, GET 075:07–075:09

During modification of the LM contingency two-hour activation checklist, CAPCOM Charlie Duke instructed the crew to change the DAP Noun 46 and then, **after Noun 47, insert `VERB 34 ENTER`**. Fred Haise read this back and explicitly interpreted the consequence as the gimbals already looking all right. Duke answered, **“That's affirmative on the gimbals, Fred. Nothing else on page 14.”**

The procedural significance is strong because the normal sequence on that page continued from the vehicle-weight entry into Noun 48, the engine-gimbal trim entry. `VERB 34 ENTER` terminated the operation before that trim entry.

Transcript navigation:
- https://apollo13.spacelog.org/03%3A03%3A07%3A13/
- corrected transcript/context: https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html

### Apollo 13 air-to-ground / PAO transcript — burn rules, GET 076:35–076:39

CAPCOM Vance Brand told the crew, “After PC plus 2, there are no trim requirements.” In Haise's readback, the statement became **“there's no trim requirements on this burn.”** CAPCOM did not correct that item while correcting Haise's mistaken “178 hours” to “78 hours.”

NASA primary transcript PDF:
https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf

Corrected transcript navigation:
https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html

## Finding

The prior search target — a missing post-free-return **final PC+2 commanded GDA trim pair** — was framed too strongly. The PC+2 activation procedure positively directed the crew to terminate the DAP-loading sequence after Noun 47, before Noun 48 trim entry, and Mission Control affirmed that the gimbals were already satisfactory. The subsequent burn-rules exchange also records no trim requirement for the burn.

Therefore, the best-supported operational model is:

`load/update DAP configuration -> load vehicle weights -> terminate before Noun 48 -> retain acceptable existing gimbal state -> perform PC+2 with no new crew-entered trim pair`

This is stronger than merely observing that the final P30 PAD omitted trim.

## Important boundary

This evidence does **not** prove:

- the exact angular gimbal state retained at the moment the Noun 48 step was skipped;
- that the retained state was numerically identical to the earlier `5.86° / 6.75°` free-return trim;
- whether ground personnel had computed a candidate PC+2 trim and decided no update was needed;
- a numbered mass-properties job for the decision;
- that “no trim requirements” means the engine remained fixed during powered flight. The documented low-throttle startup allowed the guidance/control system to sense and respond to thrust-vector/CG mismatch, and postflight evidence shows GDA motion during the burn.

The existing execution evidence — including the approximately `-0.8°` pre-ignition roll-GDA state and subsequent motion — must remain separate from any earlier crew-entered Noun 48 values.

## Simulation implication

Model PC+2 as a **no-new-trim-load decision**, not as a maneuver with an unrecovered final Noun 48 pair. The crew-facing activation workflow should support an explicit branch that terminates after vehicle-weight entry and preserves the existing gimbal state when CONTROL judges it acceptable.

The provenance model should distinguish:

1. computed/recommended trim;
2. crew-entered Noun 48 trim;
3. retained pre-existing gimbal state;
4. CONTROL acceptance/no-update decision;
5. observed GDA response during ignition and powered flight.

## Next archival target

The highest-value remaining trim question is no longer “what was the final PC+2 pair?” It is whether H-2 CONTROL/Flight Dynamics working material documents **why no new Noun 48 load was required** — ideally a mass-properties calculation/job, comparison tolerance, or gimbal-state check between the free-return burn and PC+2. Separately, continue the numerical queue for the operational module/depletion accounting behind the final Noun 47 weights and the missing Apollo 13 DPS final-flight evaluation.