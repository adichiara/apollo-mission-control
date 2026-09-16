# Research note 177 — Apollo 13 mass-properties operation-verb boundary

Date: 2026-09-16

## Question

Does the primary Apollo 13 Flight Dynamics chronology tell us whether the T+55 LM-burn deck update itself was a trim-computation run or load event?

## Primary source

NASA/MSC Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, Flight Dynamics mission narrative, pp. B-2 through B-4.

## Finding

The same mission-specific chronology uses materially different verbs for distinct mass-properties operations:

1. for launch, T-6 mass properties (weights, c.g.'s, and aerodynamics) were **generated** and then **loaded in the RTCC** by T-2:46;
2. after launch, the T+25 RTCC mass properties were **run**, and their pitch/yaw trims were compared with T+6; no update was needed because the trims were within `0.01°`;
3. later, the **RTCC (LM burn) mass property decks were updated to T+55 decks**.

Because the report itself distinguishes generation, RTCC loading, a mass-properties run, and a deck update, the T+55 statement should not be silently expanded into any of the other operations.

The source therefore supports **T+55 deck state/update in the RTCC LM-burn domain**, but does not by itself establish when the T+55 values were generated, when/if they were separately loaded, when a downstream trim run consumed them, or which job produced `5.86 / 6.75`.

## What this improves

This tightens the provenance model and removes a subtle historical overclaim risk. `deck updated`, `mass-properties generated`, `loaded in RTCC`, and `mass-properties/trim run executed` are now separate source-evidence states rather than interchangeable descriptions.

It also sharpens the archival target: another generic statement that T+55 decks existed would add little. The needed artifact must document a **run/request/output or load/generation event** that bridges the T+55 deck to the PC+2 trim solution.

## Evidence boundary

Do not infer:

- that the T+55 deck update was itself an RTCC trim run;
- that the deck update timestamp was its generation or RTCC load timestamp;
- that the T+55 deck was necessarily consumed by the ~59 GET `5.86 / 6.75` calculation;
- that the T+25 `0.01°` comparison rule governed T+55 or PC+2;
- CONTROL's alternative trim or the numerical comparison that caused CONTROL to accept Flight Dynamics' values.

## Simulator implication

Represent at least these provenance events separately: `generated`, `loaded`, `deck_updated/reference_set_selected`, and `run_consumed`. A historical scenario may populate only events explicitly supported by source evidence. For T+55, `deck_updated/reference_set_selected` and the RTCC LM-burn domain are currently supported; generation/load/run-consumption remain unresolved.

## Next archival target

Search for Apollo 13 RTCC/Flight Dynamics working material that explicitly records a T+55 generation/load or downstream LM-burn run/request/output, ideally with weight/c.g. values and printed pitch/yaw trim. In parallel, continue seeking LM CONTROL's premission-mass-properties numerical alternative and any controller worksheet showing the comparison.