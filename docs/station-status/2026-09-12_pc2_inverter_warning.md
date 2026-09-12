# Station Status Addendum — PC+2 inverter warning after switch

Date: 2026-09-12  
Parent: `docs/STATION_RESEARCH_STATUS.md`

## TELMU / CONTROL

Both positions remain maturity **B**.

Research note `059_pc2_inverter_warning_after_switch.md` establishes a more precise PC+2 rule path:

- the mission-specific criterion is an inverter caution/light **after switching inverters**;
- NASA LM instrumentation documentation shows the caution is tied to processed inverter AC voltage/frequency quality, not a generic inverter-health Boolean;
- for LM-5 and subsequent vehicles—including Apollo 13 LM-7—the caution logic was modified to suppress the normal selection transient until valid inverter output had been processed.

Implementation now separates:

- `lm.inverter_warning` — onboard caution/telemetry observation;
- `lm.inverter_switch_attempted` — crew/procedural action event.

The positive rule becomes evaluable only when a switch action has been represented and the warning is still present afterward. No arbitrary time delay is introduced.

Unresolved:

- exact PC+2 inverter identity/selection;
- exact cockpit switch chronology;
- exact telemetry word and TELMU/CONTROL display field;
- whether the ground independently observed the switch position or knew it from crew procedure/reporting;
- any historically specified dwell time before judging the post-switch caution.

These gaps keep TELMU and CONTROL at maturity B.
