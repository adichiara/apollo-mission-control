# Progress — nominal FLIGHT/CAPCOM crew handoff

Date: 2026-09-18

## Problem found

The non-final `/player-lab` allowed FLIGHT to queue and CAPCOM to transmit `continue_pc2_burn_sequence`, but the deterministic simulated-crew actor did not recognize that nominal item. The player-facing workflow therefore ended at transmission even though D-020 requires crew receipt/acknowledgement to remain a distinct modeled stage.

CAPCOM presentation also exposed only pending versus transmitted, so a player could not distinguish transmitted from crew received.

## Implemented

- added a scenario-bounded simulated-crew rule for the nominal `continue_pc2_burn_sequence` item;
- the rule supports receipt/acknowledgement only and does not assert exact historical wording or response latency;
- CAPCOM queue projection now exposes separate receipt state, receipt GET, and acknowledgement;
- `/player-lab` renders:
  - **APPROVED / PENDING**;
  - **TRANSMITTED / AWAITING RECEIPT**;
  - **CREW RECEIVED**;
- transmission still does not itself perform a crew operational action or spacecraft response;
- web integration tests protect the nominal pending → transmitted → received sequence;
- player-lab contract tests protect the visible state distinction;
- added `docs/testing/PLAYER_LAB_PART_TASK_CHECKOUT.md` for the next human usability checkpoint.

## Boundary

This change does not automate crew operational actions and does not add response timing. Receipt remains an explicit simulation event. The generic nominal continuation item remains a project integration handoff, not a claim about exact Apollo 13 call wording.

## Next

Run the neutral FLIGHT/CAPCOM part-task checkout under continuous GET. If the approval/transmission/receipt boundary is understood without facilitator UI coaching, proceed to CONTROL/GUIDO phone product-scanning prototypes.
