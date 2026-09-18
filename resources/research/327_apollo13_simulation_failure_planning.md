# Research note 327 — Apollo 13 simulation failure-planning evidence

Date: 2026-09-18

## Question

Can an Apollo 13-period primary source constrain how simulated failures should be selected and handled without inventing LMS instructor controls or scripting mechanics?

## Result

Yes. NASA Flight Control Division's **Mission Operations Report — Apollo 13**, dated **28 April 1970**, contains a simulation lessons-learned discussion that directly constrains failure-scenario design at the operational level.

The report states that a simulation mistake should be corrected promptly so the exercise can continue without providing **negative training**. It further explains that malfunction procedures depend on the failure that exists: restoring data can require a different procedure than restoring both voice and data. The report therefore says simulated failures should be planned carefully so the appropriate procedures can be exercised.

Primary source:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970.
- NASA-hosted PDF: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- NTRS record/download: https://ntrs.nasa.gov/api/citations/19710010485/downloads/19710010485.pdf

## Evidence boundary

This is direct Apollo 13-period evidence about **simulation exercise design and operational training consequences**. It does **not** identify LMS instructor-console controls, scripting syntax, internal failure representation, automatic recovery behavior, or which spacecraft malfunctions the LMS could inject.

The report's example concerns flight-control/data-system training rather than a recovered LM simulator malfunction-definition page. It therefore supports a general scenario-design rule, not a claim that a particular LM failure was available in the LMS.

## Project consequence

The project can now treat the following as historically grounded scenario-authoring constraints:

1. A simulated failure should be selected to exercise the intended operational procedure or decision path.
2. Failure scope matters: superficially similar failures can require different procedures when different capabilities are lost.
3. A simulation artifact or instructor mistake should not be allowed to persist merely for dramatic continuity when doing so teaches the wrong operational response; recovery/correction is preferable to negative training.
4. Scenario validation should therefore test **failure -> observable consequence -> applicable procedure/decision path**, while keeping the injection mechanism evidence-gated separately.

These constraints fit the existing causal-engine/product-validation architecture and player-interaction work; they do not require a new runtime abstraction.

## What remains open

- Section 2 **Malfunction Data** technical content and LMS failure-insertion mechanisms;
- Section 6 **Scripting Data Sheets** and any historical scenario-authoring syntax/abstractions;
- Apollo 13 `SKB32100076-386` page-level symptom/procedure inventory;
- exact 16 March FINAL -> 1 April FINAL CHANGE A technical delta;
- which LMS failures were actually available/effective for Apollo 13 training.

No station maturity, processor allocation, causal constant, or executable behavior changes from this note.
