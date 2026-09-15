# 162 — PC+2 no-trim ground-rule timing

## Question

Can a primary controller record narrow when Mission Control had formally decided that PC+2 required no new maneuver trim, beyond the later crew procedure that terminated Verb 48 before Noun 48?

## Primary source

NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, Flight Director mission narrative.

NASA scan/cataloged project copy: see `resources/PRIMARY_SOURCE_CATALOG.md` and `resources/source-catalog/PC2_GDA_TRIM_SOURCES.md`.

## Evidence

The Flight Director narrative states that the shift handover to the White Team was completed at approximately **74:00 GET** and that the major activity on that shift was completion of the PC+2 maneuver. It then lists the ground rules established for PC+2. Ground rule 2 is explicit: **“No PC+2 maneuver trims were required.”**

The same narrative subsequently records that at **75:35 GET** the PC+2 maneuver pad was updated and the state vector and target load were uplinked.

This is independent of the later air-to-ground activation sequence at approximately 75:08 GET in which CAPCOM inserted `VERB 34 ENTER` after Noun 47. The Flight Director record therefore establishes that the no-trim disposition was an explicit ground rule during final PC+2 preparation, not merely an inference from the crew procedure or a casual crew interpretation.

## What this establishes

The controller-side decision timeline can now be bounded more tightly:

1. at approximately 59:00 GET, a PC+2 abort-pad DPS trim was challenged because LM CONTROL had used inferior premission mass properties; Flight Dynamics reports that CONTROL later agreed with its data;
2. the 61:29 free-return burn used the accepted `5.86° / 6.75°` trim pair;
3. by the White Team PC+2 preparation period beginning around 74:00 GET, **no PC+2 maneuver trims required** was an explicit Flight Director ground rule;
4. at approximately 75:08 GET, the crew-facing DAP procedure implemented that disposition by terminating Verb 48 after Noun 47 and before Noun 48;
5. the maneuver pad was updated at 75:35 GET, and the final P30 read-up likewise contained no trim pair.

This strengthens the product lifecycle from a merely observed no-entry procedure to a documented controller ground rule followed by a matching crew/computer implementation.

## Evidence boundary

The report still does **not** state:

- the calculation time or RTCC job that produced the PC+2 candidate trim;
- the candidate pitch/roll values compared by controllers;
- the current/reference trim values used in that comparison;
- the numerical tolerance or criterion for deciding that no PC+2 trim update was required;
- whether the no-trim ground rule was first established exactly at 74:00 GET or earlier;
- a direct calculation-level link between the T+55 LM-burn deck and this ground rule.

Do not transfer the separately documented T+25 `0.01°` comparison criterion to PC+2.

## Model consequence

Represent `trim_update_required = false` for the final PC+2 preparation as a **controller-approved ground-rule disposition** by the White Team preparation period, not merely as an inference from the absence of Noun 48 entry. Preserve the unknown upstream calculation/comparison fields.

## Next archival target

The highest-value unresolved artifact is now one **before or underlying the ground-rule disposition**: a Flight Dynamics/CONTROL working sheet, Flight Director log detail, RTCC mass-properties output, or GDA calculation record between the T+55 deck update / ~59-hour reconciliation and the ~74-hour final-preparation period that gives the candidate trim, reference trim, delta/tolerance, calculation time, or job identity.