# PC+2 Inverter-Warning Source Addendum

Status: **active supplement to `PC2_IMPLEMENTATION_SOURCES.md`**

## Mission Operations Report — Apollo 13

- **Organization:** NASA Flight Control Division, Manned Spacecraft Center
- **Date:** 28 Apr 1970
- **Use:** mission-specific PC+2 shutdown criterion involving an inverter warning/light after switching inverters.
- **Status:** PRIMARY / REVIEWED for criterion semantics.

## Apollo 13 technical/PAO air-ground transcript

- **Intervals:** approximately 74:55–75:15 GET and 76:30–76:38 GET
- **Use:** the first interval records PC+2 electrical configuration work: check inverter 2 then inverter 1, leave the inverter-2 EPS feed open after the check, then close `CB(16) INVERTER 2` before the burn procedure continues. The later interval establishes the crew-facing shutdown-rule order: inverter warning → try switching inverters → judge whether the warning is still on.
- **Key mission-specific wording:** the crew readback says the inverter light is a shutdown condition if still on after trying the switch.
- **Status:** PRIMARY / REVIEWED for mission-specific preparation, rule ordering, and CAPCOM/crew communication path.
- **Public transcript:** https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf

## Apollo Operations Handbook — Lunar Module, Subsystems Data

- **Document:** LMA790-3-LM, §2.5.3.3 A-C Section
- **Public scan:** https://web.mit.edu/digitalapollo/Documents/Chapter8/lemhandbook.pdf
- **Status:** PRIMARY TECHNICAL / REVIEWED
- **Use:** identifies the two inverters as redundant, describes the selector/feed architecture, and explicitly states that inverter 1 is the operating inverter during DPS and APS engine burns while inverter 2 is normally used for initial subsystem activation.
- **PC+2 consequence:** combined with the Apollo 13 mission-specific preparation of inverter 2 and the contemporaneous “switch inverters” shutdown rule, this supports a source-bounded first-playable interpretation of normal PC+2 operation on **inverter 1** with **inverter 2** as the contingency alternate.
- **Caution:** the handbook does not supply the Apollo 13-specific post-warning switch chronology or any persistence timer.

## Apollo Experience Report — Lunar Module Instrumentation Subsystem

- **NASA document ID:** 19720018206
- **Public PDF:** https://www.ibiblio.org/apollo/Documents/19720018206.pdf
- **Status:** PRIMARY TECHNICAL / REVIEWED-PARTIAL
- **Use:** documents the inverter caution-generation path, including inverter bus voltage/frequency monitoring and the LM-5-and-subsequent selection-transient inhibit behavior applicable to Apollo 13 LM-7.
- **Key evidence:** inverter caution responds to out-of-limit AC voltage/frequency; LM-5-and-later circuitry delays removal of the caution inhibit during inverter selection until valid processed inverter data are established.
- **Caution:** does not establish the exact Apollo 13 PC+2 controller CRT field, telemetry word, post-switch persistence interval, or ground visibility of switch position.

## Apollo 13 LM-7 Contingency Checklist — Museum of Flight collection record

- **Repository:** The Museum of Flight Archives, Apollo 11 and 13 Checklists collection.
- **Status:** PRIMARY ARTIFACT LOCATION / NOT REVIEWED FOR THE SPECIFIC POST-WARNING SWITCH SEQUENCE.
- **Use:** confirms survival of the flown Apollo 13 LM-7 Contingency Checklist and provides a future source target.
- **Caution:** the accessible catalog record reviewed does not expose a page resolving the exact post-warning switch-toggle/breaker chronology or timing. Do not infer those details from the artifact's existence.

## Current source-bounded conclusion

For the first playable:

`DPS burn on inverter 1 → inverter light → crew attempts transfer to inverter 2 → light remains → shutdown criterion satisfied`

The inverter-number mapping is a synthesis of direct LM subsystem documentation plus mission-specific Apollo 13 configuration/rule evidence. It is not claimed as a verbatim Apollo 13 rule sentence.

## Research record

- `resources/research/059_pc2_inverter_warning_after_switch.md`
- `resources/research/060_pc2_inverter_contingency_action_report_loop.md`
- `resources/research/111_pc2_inverter_switch_identity.md`
