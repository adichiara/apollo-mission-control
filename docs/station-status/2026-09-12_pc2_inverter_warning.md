# Station Status Addendum — PC+2 inverter warning after switch

Date: 2026-09-12  
Updated: 2026-09-13  
Parent: `docs/STATION_RESEARCH_STATUS.md`

## TELMU / CONTROL / CAPCOM

All three positions remain maturity **B**.

Research notes `059_pc2_inverter_warning_after_switch.md`, `060_pc2_inverter_contingency_action_report_loop.md`, `112_pc2_inverter_selection_correction.md`, and `113_pc2_inverter_alternate_identity.md` establish a more precise PC+2 rule and communication path:

- the mission-specific criterion is an inverter caution/light **after switching inverters**;
- NASA LM instrumentation documentation shows the caution is tied to processed inverter AC voltage/frequency quality, not a generic inverter-health Boolean;
- for LM-5 and subsequent vehicles—including Apollo 13 LM-7—the caution logic was modified to suppress the normal selection transient until valid inverter output had been processed;
- the Apollo 13 air-ground record at approximately 76:30–76:38 GET shows CAPCOM reading the rule to the crew and the crew reading back the ordered contingency: if the inverter light remains after trying to switch inverters, it is a shutdown condition;
- the mission-specific PC+2 read-up fixes the active burn source as **inverter 2** by closing `CB(16) INVERTER 2` and deleting `Select Inverter 1`;
- the LM AC architecture has only two redundant inverters, so from the source-bounded PC+2 starting state the other inverter identity is **inverter 1**.

Implementation may therefore represent the identity chain as:

- `lm.inverter_selected = 2` before/during nominal PC+2;
- `lm.inverter_warning` — onboard caution/telemetry observation;
- `lm.inverter_switch_attempted` — crew/procedural action event;
- contingency target identity `inverter 1`;
- CAPCOM `instruction` event requesting the switch contingency;
- crew `completion_report` event confirming the requested action was performed;
- a **distinct later inverter-warning observation** required before the shutdown rule can trigger.

The named alternate identity is now research-sufficient. The exact cockpit transfer chronology is not.

### TELMU / CONTROL

Remain **B** because the exact telemetry/display route and exact discipline call sequence for a hypothetical PC+2 inverter failure are unresolved. The simulator may expose the researched caution, selected/alternate identities, and rule semantics, but must not claim an exact Apollo 13 CRT field, ground switch-position indication, or backroom/front-room call chronology.

### CAPCOM

Remains **B**. The mission-specific rule read-up/readback strengthens the evidence for CAPCOM as the crew-facing procedure path. It does not resolve the exact wording/timing or switch/circuit-breaker sequence of a hypothetical in-burn inverter contingency that never occurred historically.

## Unresolved

- exact cockpit switch/circuit-breaker chronology for transfer from inverter 2 to inverter 1;
- exact crew member who would execute the hypothetical switch;
- exact telemetry word and TELMU/CONTROL display field;
- whether the ground independently observed the switch position or knew it from crew procedure/reporting;
- any historically specified dwell time before judging the post-switch caution;
- exact internal TELMU/CONTROL → FLIGHT call sequence for this hypothetical failure.

The inverter **identity** question is closed by note 113: PC+2 starts on inverter 2 and the only other redundant inverter is inverter 1. This is an architecture-constrained consequence of primary mission-specific and LM technical evidence, not a claim that an exact Apollo 13 malfunction checklist transfer sequence has been recovered. The remaining gaps keep the three stations at maturity B.
