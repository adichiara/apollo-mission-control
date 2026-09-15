# Research note 159 — Luminary 131 confirms the V34-after-N47 termination path

Date: 2026-09-15

## Question

Does Apollo 13's actual LM guidance software support the interpretation in research note 158 that `VERB 34 ENTER` at the Noun 47 step terminates the DAP-load routine before Noun 48 trim display/entry?

## Primary evidence

### Apollo 13 Luminary 1C / Luminary 131 source listing — `EXTENDED_VERBS.agc`

The Apollo 13 LM AGC source listing preserves the `DAPDISP` / R03 DAP-data-load routine directly.

Source listing:
https://www.ibiblio.org/apollo/listings/Luminary131/EXTENDED_VERBS.agc.html

Relevant listing sequence (printed pages 297–298; labels `DAPDATA2`, `ENDR03`, `DAPDAT2`, `DAPDATA3`):

- the routine explicitly reaches Noun 47 as `V0647`, described in the source comment as **“PROCEED TO NOUN 47, MASS LOAD”**;
- the response dispatch immediately after the Noun 47 display maps **`V34E` to `ENDR03`**, with the source comment **“V34E TERMINATE”**;
- `ENDR03` restores the deadbank state and branches to `ENDEXT`, ending the extended-verb routine;
- only the separate `V33E PROCEED` branch goes through `DAPDAT2`, validates/loads LM and CSM mass, computes total mass/moments of inertia, and then reaches `DAPDATA3`;
- `DAPDATA3` displays `V06N48`, explicitly commented **“DISPLAY TRIM ANGLES AND REQUEST RESPONSE”**;
- a subsequent `V33E` from Noun 48 invokes the trim operation (`TRIMGIMB`).

The source therefore encodes a real branch boundary:

`N47 display -> V34E -> ENDR03 -> ENDEXT`

versus

`N47 display -> V33E -> mass/moment processing -> N48 display -> optional trim action`.

## Finding

Research note 158's procedural interpretation is now independently confirmed by the **Apollo 13 flight-software source**, not merely inferred from checklist ordering or transcript wording. When Mission Control told Haise to insert `VERB 34 ENTER` after Noun 47, that response selected the software's explicit termination branch. The Noun 48 display/trim branch was not executed as part of that Verb 48 DAP-load operation.

This materially strengthens the historical model:

`V48 DAP load -> N46 configuration -> N47 display -> V34 terminate -> no N48 display -> no TRIMGIMB action from this sequence`

## Important boundary

The software evidence proves **what the crew/computer branch did**, not **why CONTROL judged termination acceptable**. It does not establish:

- the exact retained pitch/roll GDA state;
- the computed candidate PC+2 trim, if one existed;
- a comparison tolerance used by CONTROL;
- the mass-properties job identity supporting the decision;
- direct linkage of the earlier `5.86° / 6.75°` pair to `T+55`;
- that no other mechanism could alter gimbal state outside this particular R03/V48 sequence.

The controller-side rationale therefore remains the unresolved archival target.

## Simulation implication

The simulator should implement this as a genuine procedural/computer branch rather than a hidden omission. At Noun 47, a terminate response ends the DAP-load routine before Noun 48. A proceed response continues through mass processing to Noun 48 and can ultimately command `TRIMGIMB`.

For the Apollo 13 PC+2 scenario, the historical branch is the terminate path. The reason Mission Control selected it remains a controller-side evidence gap.

## Next archival target

Continue searching H-2 CONTROL/Flight Dynamics working material for the **basis of the no-update decision**: calculated trim, retained-state comparison, tolerance, mass-properties run/job, or controller worksheet. Separately retain the numerical queue for Noun 47 module/depletion accounting and DPS final-flight evaluation.