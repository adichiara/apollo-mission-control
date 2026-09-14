# Station research status — PC+2 maneuver-pad weights

Date: 2026-09-14
Research note: 137

## Flight Dynamics / FIDO-RETRO

**Status change:** provenance strengthened; exact internal computation remains unresolved.

The final PC+2 maneuver solution transmitted to the crew explicitly included CSM `62480 lb` and LM `33452 lb` in its comments. This supports presenting those values as part of the final historical maneuver-product context.

It does **not** establish the RTCC mass bookkeeping, calculation epoch, exact internal fields, or whether the transmitted weights equal hidden physical mass at TIG.

## GUIDO

**Status change:** none to station ownership.

The source strengthens the historical final-load/P30 context but does not establish a new GUIDO display, key sequence, or weight-computation responsibility.

## CAPCOM

**Status change:** provenance strengthened.

CAPCOM transmitted the final P30 LM maneuver PAD and its weight comments; the crew read them back and CAPCOM confirmed the readback. This is suitable historical content for the communication layer.

## CONTROL / TELMU / INCO / FLIGHT

**Status change:** none.

No reviewed evidence assigns these two PAD weight values to a new station display or computation path. Do not infer one.

## Simulation boundary

Player-visible maneuver products may carry the documented PAD weights. The authoritative vehicle model should retain a separately named physical-mass state so future source work can determine whether and how the two correspond.