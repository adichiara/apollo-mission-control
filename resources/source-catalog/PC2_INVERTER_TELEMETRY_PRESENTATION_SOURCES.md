# PC+2 Inverter Telemetry Presentation Source Addendum

Status: **active supplement to `PC2_INVERTER_WARNING_SOURCES.md`**

## Purpose

Track primary sources bearing specifically on the ground sampling and presentation of the source-backed inverter electrical measurements `GC0071V` and `GC0155F`. This supplement does not replace the mission-specific inverter-warning procedural catalog.

## Lunar Module 7, 8 & 9 Elementary Functional Diagrams

- **Document family:** LED-267-37C
- **Public scan:** https://www.ibiblio.org/apollo/Documents/lm-7%2C8%2C9_elementary_functional_diagrams.pdf
- **Status:** PRIMARY / MISSION-VEHICLE-FAMILY / REVIEWED for measurement identity.
- **Use:** measurement index identifies `GC0071V` as inverter-bus voltage and `GC0155F` as inverter-bus frequency for the LM-7/8/9 family, which includes Apollo 13 LM-7.
- **Boundary:** does not establish Apollo 13 MSFN format loading, sample cadence, primary MSK routing, controller selection, or CRT field placement.

## Apollo Experience Report — Lunar Module Instrumentation Subsystem

- **Report:** NASA TN D-6845 / MSC-S-294, June 1972
- **NTRS:** https://ntrs.nasa.gov/citations/19720018206
- **Public scan:** https://www.ibiblio.org/apollo/Documents/19720018206.pdf
- **Status:** PRIMARY TECHNICAL / REVIEWED.
- **Use:** figure 27 shows `GC0155` frequency and `GC0071` voltage routed to PCM telemetry and separately into inverter failure-detection/caution logic.
- **Boundary:** establishes telemetry provenance, not Apollo 13 display-format loading or refresh timing.

## LM-10 Instrumentation Packet

- **Vehicle:** LM-10 / Apollo 15
- **Public scan:** https://www.ibiblio.org/apollo/Documents/LM-10_Instrumentation_Packet.pdf
- **Status:** PRIMARY MISSION-VEHICLE DOCUMENT / LATER-MISSION CONTINUITY EVIDENCE.
- **Use:** the Lunar Module Telemetry Data Summary gives operational ground-telemetry details for the same measurement identifiers:
  - `GC0071V` AC BUS VOLT, 0–120 VRMS: MSFN format 1 = 1 sample/s; formats 3–5 = 0.2 sample/s; strip chart LP-1; primary MSKs 1001, 1002, 1071, 1091, 1127.
  - `GC0155F` AC BUS FREQ, 380–420 Hz: MSFN format 1 = 1 sample/s; formats 3–5 = 0.2 sample/s; strip chart LP-1; primary MSKs 1001, 1002, 1091, 1127.
- **Consequence:** confirms that these IDs were operational MSFN-sampled/display-routed telemetry products and that sampling was format-dependent.
- **Boundary:** LM-10 is not LM-7. None of these exact rates or MSK lists are promoted into Apollo 13 historical configuration without Apollo 13/LM-7 corroboration.

## AS-508 MCC/MSFN Mission Configuration/System Description

- **Mission:** Apollo 13 / AS-508
- **Date:** March 1970
- **Prepared by:** Manned Spacecraft Center, Flight Support Division
- **NTRS:** https://ntrs.nasa.gov/citations/19700024253
- **Archival scan:** https://www.apollojournals.org/alsj/AS-508-MCC-MSFN-Config.pdf
- **Status:** PRIMARY / MISSION-SPECIFIC / REVIEWED for format architecture and high-speed playback boundary.
- **Use:** AS-508's utilization matrix identifies normal LM-capable 2.4-kb/s formats, including LM ONLY, CSM-LM PCM, CSM + LM BACKUP, and ASCENT/DESCENT. Section 3.2.2.3 separately defines High Speed Format 30 for **post-pass playback** of pre-defined CSM/LM high-rate subformats, with LM analog slots at 50 or 10 samples/s and real-time CEF selection at the TICC.
- **Consequence:** Apollo 13's mission-specific ground configuration confirms LM-capable normal telemetry formats while preventing a false inference that Format-30 10/50-sample/s rates were live TELMU/CONTROL CRT cadence.
- **Boundary:** does not identify `GC0071V` / `GC0155F` in a specific AS-508 normal format or Format-30 LM subformat, does not establish their live PC+2 sampling cadence, and does not identify an Apollo 13 MSK or controller selection.

## Apollo Experience Report — Flight-Control Data Needs, Terminal Display Devices, and Ground System Configuration Requirements

- **Report:** NASA TN D-7685 / JSC S-396, May 1974
- **NTRS:** https://ntrs.nasa.gov/citations/19740015284
- **Status:** PRIMARY APOLLO-EXPERIENCE / REVIEWED.
- **Use:** establishes dynamic display-request/channel-attach behavior for MCC computer-driven TV formats.
- **Boundary:** does not identify Apollo 13 inverter MSKs, fields, selected displays, or refresh cadence.

## Current source-bounded conclusion

```text
LM-7/8/9 documents: measurement identity exists for Apollo 13 vehicle family
        ↓
NASA instrumentation architecture: PCM/MSFN telemetry path exists
        ↓
AS-508 mission configuration: normal LM-capable formats exist; high-rate Format 30 is post-pass playback, not sourced live CRT cadence
        ↓
LM-10 telemetry packet: same IDs have explicit format-dependent sample rates and MSK destinations in a later flight configuration
        ↓
Apollo 13 exact live format/rate/MSK selection: still unresolved
```

For the first playable, `GC0071V` / `GC0155F` may remain source-backed ground electrical evidence, but the UI must not claim a recovered Apollo 13 MSK number, CRT field, or refresh rate. Normal telemetry sample cadence, CRT/display update latency, and post-pass high-rate playback remain distinct concepts.

## Research record

- `resources/research/116_pc2_inverter_ground_observation_path.md`
- `resources/research/117_pc2_inverter_direct_caution_selector_telemetry_boundary.md`
- `resources/research/118_pc2_inverter_mcc_display_routing_boundary.md`
- `resources/research/119_pc2_inverter_telemetry_sample_display_continuity.md`
- `resources/research/120_pc2_inverter_as508_format30_boundary.md`
