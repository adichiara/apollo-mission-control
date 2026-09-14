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

## SA-204/LM-1 Data Evaluation Guide — Rev. 2 changes

- **Mission/vehicle:** SA-204 / LM-1
- **Date:** 16 January 1968
- **Public scan:** https://www.ibiblio.org/apollo/Documents/SA-204_LM-1_Data_Evaluation_Guide_Rev2_changes_only.pdf
- **Status:** PRIMARY EARLY-LM / CONTINUITY EVIDENCE.
- **Use:** Appendix Y lists `GC0071V` (VOLT, INVERTER BUS) with display request 5746 and telemetry channel/loading `1022069 15`, and `GC0155F` (FREQ, INVERTER BUS) with display request 5771 and telemetry channel/loading `1041069 15`.
- **Consequence:** proves both inverter measurements were explicit ground display/telemetry products well before Apollo 13; the base loading numbers also match those carried in the later LM-10 telemetry packet.
- **Boundary:** LM-1 display-request numbers and channel notation are not promoted into Apollo 13/LM-7 historical configuration without mission-specific corroboration.

## LM-10 Instrumentation Packet

- **Vehicle:** LM-10 / Apollo 15
- **Public scan:** https://www.ibiblio.org/apollo/Documents/LM-10_Instrumentation_Packet.pdf
- **Status:** PRIMARY MISSION-VEHICLE DOCUMENT / LATER-MISSION CONTINUITY EVIDENCE.
- **Use:** the Lunar Module Telemetry Data Summary gives operational ground-telemetry details for the same measurement identifiers:
  - `GC0071V` AC BUS VOLT, 0–120 VRMS: loading 1022069; MSFN format 1 = 1 sample/s; formats 3–5 = 0.2 sample/s; strip chart LP-1; primary MSKs 1001, 1002, 1071, 1091, 1127.
  - `GC0155F` AC BUS FREQ, 380–420 Hz: loading 1041069; MSFN format 1 = 1 sample/s; formats 3–5 = 0.2 sample/s; strip chart LP-1; primary MSKs 1001, 1002, 1091, 1127.
- **Consequence:** confirms that these IDs were operational MSFN-sampled/display-routed telemetry products and that sampling was format-dependent.
- **Boundary:** LM-10 is not LM-7. None of these exact rates or MSK lists are promoted into Apollo 13 historical configuration without Apollo 13/LM-7 corroboration.

## Apollo 15 MCC Operational Configuration — PHO-TR155

- **Mission:** Apollo 15 / Mission J1 / AS-510
- **Date:** 26 March 1971
- **Public scan:** https://www.ibiblio.org/apollo/Documents/MCC%20Operational%20Configuration%20Apollo%2015.pdf
- **Status:** PRIMARY MCC CONFIGURATION / LATER-MISSION CONTINUITY EVIDENCE.
- **Use:** identifies console 09 as **LM TELMU** and, on console 09 module 05, lists `GC0071V * AC BUS V` at indicator 07 and `GC0155F * AC BUS F` at indicator 16, both sourced from MOC.
- **Consequence:** directly ties both inverter-bus measurements to a named front-room station and physical TELMU operational indicators in a later Apollo configuration.
- **Boundary:** Apollo 15 console/module/indicator positions do not establish Apollo 13/AS-508 panel loading; no reviewed Apollo 13 operational-configuration sheet has yet been recovered for these measurements.

## AS-508 MCC/MSFN Mission Configuration/System Description

- **Mission:** Apollo 13 / AS-508
- **Date:** March 1970
- **Prepared by:** Manned Spacecraft Center, Flight Support Division
- **NTRS:** https://ntrs.nasa.gov/citations/19700024253
- **Archival scan:** https://www.apollojournals.org/alsj/AS-508-MCC-MSFN-Config.pdf
- **Status:** PRIMARY / MISSION-SPECIFIC / REVIEWED for format architecture and high-speed playback boundary.
- **Use:** AS-508's utilization matrix identifies normal LM-capable 2.4-kb/s formats, including LM ONLY, CSM-LM PCM, CSM + LM BACKUP, and ASCENT/DESCENT. Section 3.2.2.3 separately defines High Speed Format 30 for **post-pass playback** of pre-defined CSM/LM high-rate subformats, with LM analog slots at 50 or 10 samples/s and real-time CEF selection at the TICC.
- **Consequence:** Apollo 13's mission-specific ground configuration confirms LM-capable normal telemetry formats while preventing a false inference that Format-30 10/50-sample/s rates were live TELMU/CONTROL CRT cadence.
- **Boundary:** does not identify `GC0071V` / `GC0155F` in a specific AS-508 normal format or Format-30 LM subformat, does not establish their live PC+2 sampling cadence, and does not identify an Apollo 13 MSK or exact indicator loading.

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
LM-1: both IDs are explicit ground display/telemetry products
        ↓
AS-508 mission configuration: normal LM-capable formats exist; high-rate Format 30 is post-pass playback, not sourced live CRT cadence
        ↓
Apollo 15: both IDs appear on TELMU console 09 operational indicators
        ↓
LM-10 telemetry packet: same IDs/loadings have explicit format-dependent sample rates and primary MSKs
        ↓
Apollo 13 exact live format/rate/indicator/MSK loading: still unresolved
```

For the first playable, `GC0071V` / `GC0155F` may remain source-backed TELMU electrical evidence. The station-family assignment is now stronger than the exact presentation assignment: later primary MCC configuration explicitly places both measurements on TELMU, but the UI must not claim Apollo 15 module/indicator coordinates, LM-1 display-request numbers, a recovered Apollo 13 MSK number, or a recovered Apollo 13 refresh rate. Normal telemetry sample cadence, physical operational indicators, CRT/display routing, and post-pass high-rate playback remain distinct concepts.

## Research record

- `resources/research/116_pc2_inverter_ground_observation_path.md`
- `resources/research/117_pc2_inverter_direct_caution_selector_telemetry_boundary.md`
- `resources/research/118_pc2_inverter_mcc_display_routing_boundary.md`
- `resources/research/119_pc2_inverter_telemetry_sample_display_continuity.md`
- `resources/research/120_pc2_inverter_as508_format30_boundary.md`
- `resources/research/121_pc2_inverter_telmu_indicator_continuity_boundary.md`
