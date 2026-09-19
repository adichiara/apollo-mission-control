# Research Sufficiency and Closure

## Purpose

Historical research in this project is not expected to exhaust every surviving Apollo source. It is expected to establish the facts needed to make a historically defensible implementation decision, identify the facts that remain unknown, and stop when further research no longer has a current decision payoff.

Research sufficiency is therefore judged against a **bounded research question and an implementation dependency**, not against a whole subject area. "LMS research" cannot be complete. A question such as "which LMS output-table evidence is needed to constrain a controller-visible product for this scenario and configuration?" can be sufficient for a defined implementation stage.

This document operationalizes Project Principle 4 and decision D-024.

## 1. Define the exit condition before extending a thread

An active research thread should identify:

- **Bounded question** — the specific historical question being answered.
- **Effectivity boundary** — mission, date/revision, vehicle/configuration, station, or simulation context when relevant.
- **Implementation dependency** — the controller product, authority, procedure, causal-model behavior, scenario condition, validation target, or player interaction that could change depending on the answer.
- **Decision sensitivity** — what materially different implementation would follow from a different answer.

If no current implementation dependency or decision sensitivity can be named, the thread is normally **DEFERRED**, not an invitation to continue general discovery indefinitely.

## 2. Research-thread states

Use these states for bounded research questions:

- **OPEN** — active research is still expected to change or constrain a current implementation decision.
- **SUFFICIENT** — the sufficiency gate below passes. Implementation may proceed without inventing historical behavior.
- **DEFERRED** — further evidence could be interesting or useful later, but no current implementation dependency justifies continued active research.
- **BLOCKED** — a material implementation dependency remains unresolved and the next discriminating evidence is not presently accessible or recoverable. The implementation remains blocked on that point unless an explicit project decision creates a clearly identified design adaptation.
- **REOPENED** — a previously sufficient, deferred, or blocked question has met a reopen trigger.

These states describe research activity and implementation readiness. They do **not** replace the claim-level evidence labels `DOCUMENTED`, `PARTIALLY DOCUMENTED`, and `UNRESOLVED`.

## 3. Sufficiency gate

A bounded question may be marked **SUFFICIENT** only when all of the following are true.

### A. Scope is bounded

The question is narrow enough that its mission/configuration/effectivity and intended implementation use are explicit. A broad domain label is not a closure target.

### B. Decision-relevant claims are accounted for

Every claim that can materially change the current implementation has:

- an appropriate source citation;
- a claim-level evidence status under Project Principle 2; and
- enough provenance to reopen the source later.

A claim repeated from another research note is not evidence for this gate.

### C. Current implementation behavior is covered

The evidence is sufficient to determine the behavior currently required at the player's or validation target's actual resolution, including whichever of these apply:

- what a controller can observe;
- what a controller or crew member can do;
- which rule/procedure/authority governs the action;
- how the causal state must evolve;
- what a ground or spacecraft product must display;
- what result must be validated.

The gate is about the behavior the simulator must reproduce, not every internal historical implementation detail.

### D. Every remaining gap has an explicit disposition

Each unresolved item is classified as one of:

1. **resolved enough for current use** by direct evidence;
2. **demonstrated irrelevant** at the player-visible/product resolution under D-022;
3. **non-decision-relevant at current scope** and therefore deferred;
4. **belongs to a later scenario/feature/effectivity boundary** and therefore deferred; or
5. **material and blocked**, in which case the question is not sufficient.

An unresolved gap may remain in a **SUFFICIENT** thread only when it falls into categories 2–4. Sufficiency never converts an unresolved historical claim into a documented one.

### E. Material source conflicts are settled or exposed

If two sources disagree in a way that could alter current behavior, the conflict must be resolved by stronger/effectivity-appropriate evidence or the question remains OPEN/BLOCKED.

Conflicts that do not change current behavior may remain recorded as deferred gaps.

### F. A closure challenge has converged

After the last material change to the tentative conclusion, perform one focused challenge pass intended to overturn it. The pass should, as applicable:

- look for a more mission-specific or revision-appropriate primary source;
- check the source catalog and research index for contrary evidence;
- inspect the strongest accessible source class likely to contradict the conclusion; and
- search specifically for the remaining material unknown rather than repeating broad discovery searches.

If that pass produces new evidence that changes the implementation conclusion, the thread stays OPEN and the challenge is repeated only after the new evidence has been integrated.

If the challenge produces no material change, the convergence criterion is met. This is the project's stopping rule; it is not necessary to prove that no additional source exists anywhere.

### G. A closure record exists

The latest thread note, status document, or other canonical research artifact records:

- bounded question;
- implementation dependency;
- status;
- decision-relevant findings;
- remaining gaps and their dispositions;
- closure-challenge result; and
- explicit reopen triggers.

Without that handoff, the thread is not closed because a later agent cannot tell why research stopped.

## 4. Stopping without sufficiency

Some research should stop even though it is not sufficient.

### DEFERRED

Use **DEFERRED** when:

- the topic has no current implementation dependency;
- the gap cannot change a player-visible product, controller decision, causal behavior, or current validation target;
- a later scenario/configuration is the natural place to resolve it; or
- higher-value research should proceed first.

A deferred question is not a research failure. It is a deliberate priority decision.

### BLOCKED

Use **BLOCKED** when:

- a material dependency remains;
- further broad searching is no longer producing discriminating evidence; and
- the next meaningful step requires an inaccessible archive, unavailable scan, missing revision, physical collection, or other concrete retrieval condition.

Record the best known evidence, the exact missing discriminator, where it is believed to exist, and what implementation remains blocked.

Do not respond to BLOCKED by cycling through semantically equivalent searches indefinitely.

## 5. Signals that more broad searching has low value

These signals support DEFERRED or BLOCKED status but do not by themselves make a question SUFFICIENT:

- targeted searches repeatedly return the same already-reviewed sources;
- new results are lower-authority derivatives of sources already opened;
- remaining candidate material is bibliographic metadata rather than technical content;
- the next source is known but presently inaccessible;
- unresolved details are below the resolution of the actual controller product;
- additional detail would enrich historical description but not change the current simulation.

The existence of another possible search query is not evidence that the thread should remain active.

## 6. Reopen triggers

A SUFFICIENT, DEFERRED, or BLOCKED question is reopened only when something material changes, such as:

- implementation exposes a new dependency or requires finer resolution;
- a new mission/scenario/configuration makes a deferred gap decision-relevant;
- a stronger, more mission-specific, or conflicting source is recovered;
- a playtest shows that the unresolved point changes player interpretation, workload, authority, or action;
- a correction or withdrawn claim under D-023 changes the evidence basis;
- a D-022 demonstrated-irrelevance result no longer holds at the implemented product resolution; or
- the concrete access condition that caused BLOCKED status changes.

The following are **not** sufficient reopen triggers by themselves:

- curiosity;
- the possibility that a deeper archive may contain more detail;
- a secondary source that repeats the existing evidence;
- a desire for a more exhaustive bibliography;
- elapsed time since the last search.

## 7. Standard closure record

Use this structure when closing, deferring, blocking, or reopening a bounded research question:

```markdown
## Research closure

- **Status:** OPEN | SUFFICIENT | DEFERRED | BLOCKED | REOPENED
- **Bounded question:** ...
- **Implementation dependency:** ...
- **Decision sensitivity:** ...
- **Decision-relevant findings:** ...
- **Remaining gaps and disposition:** ...
- **Closure challenge:** ...
- **Reopen triggers:** ...
```

The closure record supplements the note's `## Sources` and `## Evidence status` sections. It does not replace them.

## 8. Examples

### Exact numerical value remains unknown

If a sourced plausible range has been tested against the actual controller-visible product and D-022 shows that no value in the range changes what the player can read or decide, the bounded question may be **SUFFICIENT** even though the exact historical value remains `UNRESOLVED`.

### Exact malfunction mechanism is needed

If a scenario or explicitly targeted capability requires a particular malfunction insertion/effect mechanism and the surviving accessible sources establish only the malfunction name, not the causal effect needed by the model, the bounded question is not sufficient. If the next discriminating evidence is an inaccessible archival handbook section, mark that capability/question **BLOCKED** and stop broad searching until the access condition changes. This does not imply that unrelated simulator work is blocked; scope the BLOCKED state to the implementation dependency it actually gates.

### Historically interesting detail has no current effect

If a surviving document may establish a backroom staffing detail but no current station product, authority boundary, communication path, or player workload depends on it, mark that question **DEFERRED**. Reopen it if Staff Support Room simulation becomes an implementation target.

## 9. Relationship to implementation

`SUFFICIENT` means **sufficient for the stated scope**, not "historically complete."

Implementation should cite the evidence and closure record that justify proceeding. If implementation later needs more than that record established, the research question reopens rather than silently extrapolating beyond the closed scope.
