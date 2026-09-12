# PC+2 Inverter-Warning Source Addendum

Status: **active supplement to `PC2_IMPLEMENTATION_SOURCES.md`**

## Mission Operations Report — Apollo 13

- **Organization:** NASA Flight Control Division, Manned Spacecraft Center
- **Date:** 28 Apr 1970
- **Use:** mission-specific PC+2 shutdown criterion involving an inverter warning/light after switching inverters.
- **Status:** PRIMARY / REVIEWED for criterion semantics.

## Apollo 13 technical/PAO air-ground transcript

- **Interval:** approximately 76:30 GET
- **Use:** crew-facing rule read-up confirms that the inverter-light condition is judged after switching inverters.
- **Status:** PRIMARY / REVIEWED for rule wording.

## Apollo Experience Report — Lunar Module Instrumentation Subsystem

- **NASA document ID:** 19720018206
- **Public PDF:** https://www.ibiblio.org/apollo/Documents/19720018206.pdf
- **Status:** PRIMARY TECHNICAL / REVIEWED-PARTIAL
- **Use:** documents the inverter caution-generation path, including inverter bus voltage/frequency monitoring and the LM-5-and-subsequent selection-transient inhibit behavior applicable to Apollo 13 LM-7.
- **Key evidence:** inverter caution responds to out-of-limit AC voltage/frequency; LM-5-and-later circuitry delays removal of the caution inhibit during inverter selection until valid processed inverter data are established.
- **Caution:** does not establish the exact Apollo 13 PC+2 inverter-switch chronology, controller CRT field, telemetry word, or a required persistence interval.

## Research record

- `resources/research/059_pc2_inverter_warning_after_switch.md`
