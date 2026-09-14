# PC+2 Inverter-Warning Source Addendum

Status: **active supplement to `PC2_IMPLEMENTATION_SOURCES.md`**

## Mission Operations Report — Apollo 13

- **Organization:** NASA Flight Control Division, Manned Spacecraft Center
- **Date:** 28 Apr 1970
- **Use:** mission-specific PC+2 shutdown criterion involving an inverter warning/light after switching inverters.
- **Status:** PRIMARY / REVIEWED for criterion semantics.

## Apollo 13 technical/PAO air-ground transcript

- **Intervals:** approximately 72:48–73:15, 74:55–75:15, and 76:30–76:38 GET
- **Use:**
  - earlier sequence explicitly verifies/selects inverter 2 for LM AC use;
  - PC+2 read-up later restores `CB(16) INVERTER 2` and explicitly deletes the stock checklist instruction `Select Inverter 1`;
  - shutdown-rule read-up establishes inverter warning → try switching inverters → judge whether warning remains.
- **Status:** PRIMARY / REVIEWED for mission-specific inverter selection, PC+2 configuration, rule ordering, and CAPCOM/crew communication path.
- **Public transcript:** https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf

## Apollo Operations Handbook — Lunar Module, Subsystems Data

- **Document:** LMA790-3-LM, §2.5.3.3 A-C Section
- **Public scan:** https://web.mit.edu/digitalapollo/Documents/Chapter8/lemhandbook.pdf
- **Status:** PRIMARY TECHNICAL / REVIEWED
- **Use:** identifies the LM AC section as using two identical redundant inverters and documents the generic convention that inverter 1 normally operates during DPS/APS burns while inverter 2 is commonly used during subsystem activation.
- **PC+2 consequence:** this is background architecture, not the controlling Apollo 13 initial-selection evidence. The mission-specific read-up fixes PC+2 on inverter 2. Once that state is combined with the contemporaneous instruction to `switch inverters`, the only other redundant inverter identity is inverter 1. This closes the alternate **identity** without claiming recovery of an exact malfunction-transfer checklist sequence.

## Apollo Experience Report — Lunar Module Instrumentation Subsystem

- **NASA document ID:** 19720018206
- **Public PDF:** https://www.ibiblio.org/apollo/Documents/19720018206.pdf
- **Status:** PRIMARY TECHNICAL / REVIEWED-PARTIAL
- **Use:** documents the inverter caution-generation path, including inverter bus voltage/frequency monitoring and the LM-5-and-subsequent selection-transient inhibit behavior applicable to Apollo 13 LM-7.
- **Key evidence:** inverter caution responds to out-of-limit AC voltage/frequency; LM-5-and-later circuitry delays removal of the caution inhibit during inverter selection until valid processed inverter data are established.
- **Caution:** does not establish the exact Apollo 13 PC+2 controller CRT field, telemetry word, post-switch persistence interval, or ground visibility of switch position.

## Apollo 13 LM-7 Contingency Checklist — surviving artifact / transcripted read-up

- **Status:** PRIMARY PROCEDURAL EVIDENCE / REVIEWED THROUGH MISSION-SPECIFIC READ-UP; surviving artifact remains a useful future cross-check.
- **Key PC+2 modification:** at the -4 minute page-17 configuration, `CB(16) INVERTER 2` is closed and `Select Inverter 1` is scratched.
- **Consequence:** the stock checklist apparently expected the generic inverter-1 burn convention, but Apollo 13 deliberately removed that selection for PC+2.

## Current source-bounded conclusion

For the first playable:

`PC+2 selected inverter 2 → inverter light → crew switches to the other redundant inverter, inverter 1 → light remains → shutdown criterion satisfied`

The initial inverter-2 identity is mission-specific and directly supported. The alternate inverter-1 identity is an architecture-constrained consequence of (a) that mission-specific starting state, (b) the contemporaneous `switch inverters` rule, and (c) the primary LM handbook's two-inverter redundant architecture. The exact cockpit switch/circuit-breaker chronology remains unresolved and must not be invented.

## Research record

- `resources/research/059_pc2_inverter_warning_after_switch.md`
- `resources/research/060_pc2_inverter_contingency_action_report_loop.md`
- `resources/research/111_pc2_inverter_switch_identity.md` — generic-convention synthesis superseded in part
- `resources/research/112_pc2_inverter_selection_correction.md` — canonical initial inverter-2 selection correction
- `resources/research/113_pc2_inverter_alternate_identity.md` — resolves alternate inverter identity while preserving transfer-procedure uncertainty
