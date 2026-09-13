# 2026-09-13 — Live-play player preparation boundary

Status: **COMPLETE — repository-side preparation defined; physical execution still pending**

## Completed

- Reviewed the remaining physical-play validation boundary after research note 095.
- Identified an ambiguity in `PLAYER_INSTRUCTION`: the project could classify an incident as training-related without having defined what preparation a player was supposed to receive.
- Researched Apollo flight-controller training and mission-rule preparation using primary NASA sources.
- Added research note 096, which establishes that integrated simulation followed broader controller preparation rather than serving as first exposure to station responsibilities, rules, and procedures.
- Added `docs/testing/PC2_PLAYER_PREPARATION.md` as the reproducible pre-run preparation package.
- Kept scenario-specific nonnominal information, hidden state, and other stations' private evidence out of the package.

## Historical boundary

The sources support prior controller preparation, procedure/rule familiarity, and integrated simulation as decisionmaking/readiness training. They do not establish this project's handout format, browser instructions, compact-role controls, or any fixed briefing duration.

## Validation consequence

A physical first-playable run should now record whether each participant received the preparation package and completed the basic client-operation checks. This makes `PLAYER_INSTRUCTION` a testable classification rather than an after-the-fact explanation.

## Next work

Execute the physical seven-seat nominal PC+2 run using the documented preparation package and evidence report, then run the synthetic ΔP branch and five-player compact repeat. No physical-play PASS claim is made here.