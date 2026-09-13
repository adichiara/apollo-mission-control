# Research note 105 — PC+2 crew-action representation boundary

Date: 2026-09-13  
Status: **RESOLVED for current first playable**

## Question

For the Apollo 13 PC+2 first playable, should spacecraft-crew actions be scripted, controlled by an additional player, or represented another way?

## Primary-source findings

### Apollo 13 Mission Operations Report

The Flight Control Division's April 28, 1970 Mission Operations Report records an operational sequence in which Mission Control prepared and passed products/procedures to the spacecraft and the crew then configured and operated the LM. Examples in the PC+2 interval include:

- final PC+2 Maneuver Pads passed to the crew at about 77+59;
- LM power-up beginning at about 78+12;
- PC+2 ignition at 79:27:38.30 and a nominal burn;
- LM power-down initiated at about 79+34;
- CAPCOM reading a detailed PTC-establishment procedure to the crew at about 79+52.

Source: *Mission Operations Report, Apollo 13*, Flight Control Division, MSC, 1970. NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf

### Apollo Operations Handbook — LM operational procedures

The Apollo Operations Handbook identifies normal, backup, abort, malfunction, and emergency procedures as sequences of crew actions required for safe and efficient subsystem operation. This establishes that crew behavior was not simply an automatic spacecraft response: crew procedure execution is a distinct operational layer.

Source: *Apollo Operations Handbook, Lunar Module (LM 11 and Subsequent), Vol. 2 — Operational Procedures*, LMA790-3-LM-11, 1971. NTRS: https://ntrs.nasa.gov/citations/19710071423

### Apollo 13 mission evidence

Apollo 13 records repeatedly show Mission Control developing or modifying procedures, communicating them to the spacecraft, and the crew executing them under unusual conditions. That supports preserving a distinction among:

`ground recommendation/instruction → CAPCOM transmission → crew receipt/decision/execution → spacecraft physical response → telemetry/crew report`

It does **not** support replacing the crew with instantaneous automatic compliance.

## First-playable decision

The first PC+2 playable will **not add a separate crew player**. The players are the selected Mission Control stations; crew activity is represented by a **scenario-authored crew actor** outside the controller station set.

That actor follows these rules:

1. **CAPCOM remains the normal player-facing voice path to the crew.** Other controller stations do not directly trigger crew action merely by changing internal state.
2. **Crew actions are explicit state transitions, not automatic side effects of a controller conclusion.** A transmitted instruction/request and a resulting crew action remain separate events.
3. **Nominal crew actions may be deterministic when the historical sequence is known and no player decision depends on crew discretion.** This is simulation scaffolding, not a claim that astronauts behaved mechanically.
4. **Nonnominal crew responses must be scenario-authored.** They may differ from nominal behavior only when supported by a historical case or explicitly labeled synthetic.
5. **No unsupported reaction delay, misunderstanding probability, random noncompliance, or crew-error rate is invented.** Timing is left immediate/explicitly facilitated unless a source or scenario requirement establishes a meaningful delay.
6. **Crew reports and spacecraft telemetry remain separate evidence channels.** A crew statement does not directly overwrite hidden physical truth, and physical state does not automatically become controller-visible.
7. **Facilitator controls may advance or inject crew-response steps for validation, but those controls are modern exercise infrastructure rather than a historical Mission Control capability.**

## Why not a crew player now?

Adding a crew player would materially expand the vertical slice into LM cockpit operation, checklist execution, onboard displays/controls, workload, and crew-resource management. The current project target is Mission Control decision-making. Primary sources show the crew layer is operationally important, but they do not require a human crew role to test the selected controller interactions.

A later scenario should reopen this boundary if controller success depends on meaningful astronaut discretion, manual flying skill, competing onboard workload, ambiguous crew observations, or detailed checklist execution that cannot be represented faithfully as authored external actions.

## Architecture consequence

Canonical chain:

`controller evidence → controller decision → CAPCOM message → crew receipt → crew action → physical spacecraft response → telemetry / crew report → controller evidence`

The existing synthetic ΔP shutdown branch already follows this separation and should be treated as the reference implementation pattern.

## Open-question consequence

Open question 15 can be marked **resolved for the current PC+2 first playable**. The general architecture for future scenarios remains reopenable when crew discretion becomes a decision-relevant mechanic.
