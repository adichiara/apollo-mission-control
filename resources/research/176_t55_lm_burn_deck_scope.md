# Research note 176 — T+55 deck scope and Apollo 13 trim workflow

Date: 2026-09-16

## Question

Can the Apollo 13 primary controller report narrow the T+55 provenance chain further without claiming the still-missing direct `T+55 -> 5.86 / 6.75` calculation record?

## Primary source

NASA/MSC Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, Flight Dynamics mission narrative, pp. B-3/B-4 (PDF pp. 98–101).

## Finding

The report provides two mission-specific statements in the same Flight Dynamics chronology:

1. after MCC-2, a **T+25 RTCC mass-properties run** was evaluated by comparing its pitch/yaw trims with the T+6 trims; they were within `0.01°`, so no update was needed;
2. later, before the ~59 GET PC+2 abort-pad event, **"RTCC (LM burn) mass property decks were updated to T+55 decks."**

This narrows the T+55 artifact class beyond a generic mass-properties update. The primary report explicitly scopes the updated decks to **RTCC LM-burn processing**. In the same mission-specific chronology, an earlier time-tagged RTCC mass-properties run is explicitly shown producing/evaluating pitch/yaw trim outputs.

Accordingly, the strongest source-backed provenance statement is now:

`time-tagged RTCC mass-properties sets/decks -> LM-burn processing context; earlier T+25 case explicitly yields P/Y trim comparison; T+55 LM-burn decks operationally available before the ~59 GET PC+2 trim dispute`.

## What this improves

The T+55 evidence is no longer merely "a newer mass-properties deck existed." It is directly identified as an **RTCC LM-burn mass-property deck family**, which is the correct computational domain for the DPS trim dispute.

This materially strengthens, but does not close, the proposed `T+55 deck -> Flight Dynamics 5.86 / 6.75` bridge.

## Evidence boundary

Do not infer:

- that the `5.86 / 6.75` PC+2/free-return pair was calculated from the T+55 deck;
- that the same RTCC job or processor produced the T+25 and T+55 products;
- that `0.01°` was a general update threshold or the PC+2 acceptance criterion;
- the contents, weight/c.g. values, generation/load timestamp, or job identifier of the T+55 deck;
- LM CONTROL's competing numerical trim.

The chronology establishes domain, availability, and an earlier workflow precedent, not direct data lineage for the ~59 GET numerical pair.

## Simulator implication

Model mass-properties provenance with separate fields for `reference_epoch`, `processing_domain` (here source-backed as RTCC LM burn), `generation/load time`, `job/run identity`, and `consumed_by_trim_solution`. Only the first two are currently source-backed for T+55; the latter three remain unresolved.

## Next archival target

Prioritize Apollo 13 Flight Dynamics/RTCC working products that can close **data lineage**, not merely architecture: T+55 weight/c.g. output, LM-burn request/job sheet, printed pitch/yaw trim output, or controller worksheet tying that run to the `5.86 / 6.75` pair. CONTROL's premission-mass-properties alternative remains a parallel high-value target.