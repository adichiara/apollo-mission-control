# PC+2 Inverter-Warning Source Addendum

Status: **active supplement to `PC2_IMPLEMENTATION_SOURCES.md`**

## Mission Operations Report — Apollo 13

- **Organization:** NASA Flight Control Division, Manned Spacecraft Center
- **Date:** 28 Apr 1970
- **Use:** mission-specific PC+2 shutdown criterion involving an inverter warning/light after switching inverters.
- **Status:** PRIMARY / REVIEWED for criterion semantics.

## Apollo 13 technical/PAO air-ground transcript

- **Interval:** approximately 76:30–76:38 GET
- **Use:** crew-facing rule read-up and crew readback establish the procedural order: inverter warning → try switching inverters → judge whether the warning is still on.
- **Key mission-specific wording:** CAPCOM states the inverter-light criterion is after switching inverters; the crew readback says the light is a shutdown condition if still on after trying the switch.
- **Status:** PRIMARY / REVIEWED for rule ordering and CAPCOM/crew communication path.

## Apollo Experience Report — Lunar Module Instrumentation Subsystem

- **NASA document ID:** 19720018206
- **Public PDF:** https://www.ibiblio.org/apollo/Documents/19720018206.pdf
- **Status:** PRIMARY TECHNICAL / REVIEWED-PARTIAL
- **Use:** documents the inverter caution-generation path, including inverter bus voltage/frequency monitoring and the LM-5-and-subsequent selection-transient inhibit behavior applicable to Apollo 13 LM-7.
- **Key evidence:** inverter caution responds to out-of-limit AC voltage/frequency; LM-5-and-later circuitry delays removal of the caution inhibit during inverter selection until valid processed inverter data are established.
- **Caution:** does not establish the exact Apollo 13 PC+2 inverter-switch chronology, controller CRT field, telemetry word, or a required persistence interval.

## Apollo 13 LM-7 Contingency Checklist — Museum of Flight collection record

- **Repository:** The Museum of Flight Archives, Apollo 11 and 13 Checklists collection.
- **Status:** PRIMARY ARTIFACT LOCATION / NOT REVIEWED FOR THIS SPECIFIC PROCEDURE.
- **Use:** confirms survival of the flown Apollo 13 LM-7 Contingency Checklist and provides a future source target.
- **Caution:** the accessible catalog record reviewed in this pass does not expose a page resolving the PC+2 inverter-switch identity, exact switch positions, or timing. Do not infer those details from the artifact's existence.

## Research record

- `resources/research/059_pc2_inverter_warning_after_switch.md`
- `resources/research/060_pc2_inverter_contingency_action_report_loop.md`
