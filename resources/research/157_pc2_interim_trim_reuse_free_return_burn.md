# Research note 157 — PC+2 interim trim reused for the free-return DPS burn

Date: 2026-09-15

## Question

Can the ~59-hour `pitch 5.86° / roll 6.75°` pair be tied to an actual maneuver, rather than only to the update-expected contingency PC+2 pad?

## Primary evidence

### Apollo 13 Flight Control Division Mission Operations Report

The Flight Dynamics/RETRO narrative states that RTCC LM-burn mass-property decks were updated to **T+55 decks** before the crew's early LM ingress. It then records that the ~59-hour PC+2 block-data DPS trim was challenged by LM Control because CONTROL had used **premission mass properties**, after which CONTROL agreed with the Flight Dynamics data.

Source: NASA MSC-02680, *Flight Control Division Mission Operations Report — Apollo 13*, 28 April 1970.

Scan: https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf

### NASA Apollo 13 technical air-to-ground transcription — GET 060:53

For the actual free-return DPS maneuver at TIG `061:29:42.84`, CAPCOM transmitted:

- GDA pitch `5.86°`;
- GDA roll `6.75°`;
- 5 seconds at 10-percent throttle, then 40 percent;
- two-jet, 10-second ullage.

This is the **same angular GDA pair** transmitted at ~59:03 with the contingency PC+2 pad, where CAPCOM had said the PC+2 angles would be updated.

NASA transcript navigation: https://www.apollojournals.org/afj/ap13fj/09day3-lifeboat.html

## Finding

The `5.86° / 6.75°` pair was not merely an abandoned contingency-pad artifact. Mission Control reused the same pair approximately two hours later for the **actual free-return DPS burn**. Combined with the Flight Dynamics report's reconciliation narrative, this makes the pair an operationally accepted near-term DPS trim product after the mass-properties disagreement.

However, this does **not** make it the final PC+2 trim. CAPCOM explicitly said at ~59 hours that the PC+2 angles would be updated, and the final PC+2 P30 read-up later omitted GDA trim entirely.

## Important provenance boundary

The evidence supports the sequence:

`T+55 LM-burn mass-property decks available -> ~59 h cross-console trim disagreement -> Flight Dynamics/CONTROL reconciliation -> 5.86°/6.75° used for actual 61:29 free-return DPS burn`

It does **not** directly prove:

- that `5.86° / 6.75°` was calculated from a specific numbered mass-properties job;
- that the pair was mathematically generated from the `T+55` deck rather than merely accepted after comparison;
- the final PC+2 commanded trim;
- that the same pair remained valid through PC+2 at 79:27;
- the exact reason a later PC+2 update was expected.

## Simulation implication

Represent trim products with maneuver applicability and lifecycle state. A trim can be:

- proposed for one future maneuver;
- challenged/reconciled across consoles;
- accepted and used for a nearer maneuver;
- still marked update-required for a later maneuver.

Do not model `5.86° / 6.75°` as simply "wrong" or "discarded." It was operationally used for the free-return burn even though its PC+2 use was provisional.

## Next archival target

Continue searching H-2 CONTROL/Flight Dynamics working records between the 61:29 free-return burn and 79:27 PC+2 for an explicit later trim computation/setpoint, mass-properties job identity, or crew/console GDA setup record. A particularly useful artifact would distinguish the **free-return accepted trim** from the **later PC+2 update** and identify the mass-properties state/job behind each.