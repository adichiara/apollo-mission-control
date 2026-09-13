# Station status — PC+2 immediate post-burn verification / power-down

Date: 2026-09-13

Historical station maturity grades remain unchanged. Research note 101 refines the end-of-slice operational sequence rather than adding new console reconstruction.

## FLIGHT

First-playable responsibility now explicitly extends beyond burn GO/cutoff into the transition out of burn configuration. The sources support confirming a good/stable post-burn spacecraft before substantial power-down, but do not establish an exact formal controller poll for this moment. Do not invent one.

## GUIDO / FIDO-RETRO

The nominal branch may expose the documented PGNS residuals as post-burn maneuver evidence. Later tracking provided additional trajectory confirmation, but a detailed tracking workflow is not required for immediate first-playable closure unless physical play exposes that dependency.

## TELMU / CONTROL

Post-burn spacecraft/system monitoring remains relevant while the LM leaves burn configuration. Research note 101 does not assign either station an unsupported automatic power-down authorization or new telemetry fields.

## INCO

Communications remained required during the initial post-burn period and PTC preparation. No new INCO action is added without a more specific source-backed need.

## CAPCOM

CAPCOM is the supported path for reading the post-burn power-down/PTC procedure to the crew. Exact wording and full switch-by-switch procedure are not reconstructed by note 101.

## First-playable status

The end state is now source-bounded as:

`cutoff/result → post-burn assessment → partial power-down → PTC preparation`

Physical play must determine whether this transition needs more station-specific interaction before implementation expands.