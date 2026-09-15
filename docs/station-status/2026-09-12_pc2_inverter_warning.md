# Station Status Addendum — PC+2 inverter warning after switch

Date: 2026-09-12  
Parent: `docs/STATION_RESEARCH_STATUS.md`

## TELMU / CONTROL / CAPCOM

All three positions remain maturity **B**.

Research notes `059_pc2_inverter_warning_after_switch.md` and `060_pc2_inverter_contingency_action_report_loop.md` establish a more precise PC+2 rule and communication path:

- the mission-specific criterion is an inverter caution/light **after switching inverters**;
- NASA LM instrumentation documentation shows the caution is tied to processed inverter AC voltage/frequency quality, not a generic inverter-health Boolean;
- for LM-5 and subsequent vehicles—including Apollo 13 LM-7—the caution logic was modified to suppress the normal selection transient until valid inverter output had been processed;
- the Apollo 13 air-ground record at approximately 76:30–76:38 GET shows CAPCOM reading the rule to the crew and the crew reading back the ordered contingency: if the inverter light remains after trying to switch inverters, it is a shutdown condition.

Implementation now separates:

- `lm.inverter_warning` — onboard caution/telemetry observation;
- `lm.inverter_switch_attempted` — crew/procedural action event;
- CAPCOM `instruction` event requesting the switch contingency;
- crew `completion_report` event confirming the requested action was performed;
- a **distinct later inverter-warning observation** required before the shutdown rule can trigger.

This closes the first bounded controller/crew action-report loop. Later notes 112–114 resolve initial inverter 2, alternate inverter 1, and the three-control transfer sequence; the implementation still does not invent a timer.

### TELMU / CONTROL

Remain **B** because the exact telemetry/display route and exact discipline call sequence for a hypothetical PC+2 inverter failure are unresolved. The simulator may expose the researched caution and rule semantics, but must not claim an exact Apollo 13 CRT field or backroom/front-room call chronology.

### CAPCOM

Remains **B**. The mission-specific rule read-up/readback strengthens the evidence for CAPCOM as the crew-facing procedure path. It does not resolve CAPCOM console/display configuration or the exact wording/timing of a hypothetical in-burn inverter contingency that never occurred historically.

## Unresolved

- exact crew member who would execute the hypothetical switch;
- exact telemetry word and TELMU/CONTROL display field;
- whether the ground independently observed the switch position or knew it from crew procedure/reporting;
- any historically specified dwell time before judging the post-switch caution;
- exact internal TELMU/CONTROL → FLIGHT call sequence for this hypothetical failure.

The Apollo 13 LM Malfunction Procedures subsequently resolved the transfer controls (research note 114). The remaining timing, display/routing, crew-assignment, and hypothetical front-room coordination gaps remain explicit and keep the three stations at maturity B.
