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

## Apollo 13 LM Malfunction Procedures

- **Document:** LMA790-3-LM, *LM Malfunction Procedures*, Apollo 13 flight handbook scan.
- **Public scan:** https://www.ibiblio.org/apollo/Documents/Apollo%2013%20Malfunction%20Procedures.pdf
- **Status:** PRIMARY PROCEDURAL / REVIEWED for INVERTER caution alternate-selection sequence and re-observation ordering.
- **Use:** directly resolves the cockpit transfer chronology when inverter 2 is the operating source. The INVERTER caution flowchart's `Select alt inverter` action gives: `CB(11) EPS: INV 1 — close` → `INVERTER — 1` → `CB(16) EPS: INV 2 — open`, followed by re-observation of whether the INVERTER caution is off.
- **Timing boundary:** the procedure does not insert a crew stopwatch interval or numeric persistence dwell before the `INVERTER lt — off?` branch.
- **Boundary:** does not establish crew-member assignment, exact ground voice wording, or ground visibility of selector position.

## Apollo Operations Handbook — Lunar Module, Subsystems Data

- **Document:** LMA790-3-LM, §2.5.3.3 A-C Section
- **Public scan:** https://web.mit.edu/digitalapollo/Documents/Chapter8/lemhandbook.pdf
- **Status:** PRIMARY TECHNICAL / REVIEWED
- **Use:** identifies the LM AC section as using two identical redundant inverters and documents the generic convention that inverter 1 normally operates during DPS/APS burns while inverter 2 is commonly used during subsystem activation; also corroborates the feeder breakers and INVERTER selector used by the Apollo 13 malfunction procedure.
- **PC+2 consequence:** mission-specific evidence, not the generic convention, controls the initial PC+2 configuration. The handbook is an architecture/control cross-check.
- **Note-117 cross-check:** reviewed inverter/caution diagrams identify the caution logic and PCMTEA-related measurement paths but do not provide a separately named direct `GL4046` telemetry parameter or selector-position telemetry discrete.

## Apollo Experience Report — Lunar Module Instrumentation Subsystem

- **NASA document ID:** 19720018206
- **Report:** NASA TN D-6845 / MSC-S-294, June 1972
- **NTRS:** https://ntrs.nasa.gov/citations/19720018206
- **Public scan:** https://www.ibiblio.org/apollo/Documents/19720018206.pdf
- **Status:** PRIMARY TECHNICAL / REVIEWED for inverter warning generation, transient inhibit, underlying ground-telemetry provenance, and the direct caution/selector telemetry boundary.
- **Use:** documents the inverter caution-generation path, LM-5-and-subsequent inverter-selection transient-inhibit behavior applicable to Apollo 13 LM-7, and the telemetry path for the electrical quantities that drive the caution.
- **Figure 27 ground-observation evidence:** inverter-bus frequency **`GC0155`** and inverter-bus voltage **`GC0071`** each pass through isolation to **Telemetry PCMTEA**. The report's instrumentation architecture places PCMTEA data on the communications/MSFN path. Frequency failure-detection limits shown are **>402.0 Hz** and **<398.0 Hz**; the voltage failure-detection limit shown is **<112.0 V ac**.
- **Onboard caution separation:** the derived electrical-power-system inverter caution is identified as **`GL4046`**, with indicator **`6DS26`**. Figure 27 shows that caution path separately from the `GC0155`/`GC0071` PCM telemetry taps.
- **Selector separation:** Figure 27 shows the INV 1 / INV 2 / OFF selector (`4S14`) in the inverter-selection and caution-inhibit logic but does not show a labeled PCMTEA telemetry tap for selector position.
- **Selection-transient evidence:** LM-5-and-later circuitry delays removal of the caution inhibit during inverter selection until valid processed inverter data are established.
- **First-playable consequence:** normal selection-transient suppression belongs to spacecraft indication logic, not a separate crew persistence timer. Ground controllers may receive a project-rendered electrical product based on source-backed `GC0155`/`GC0071` telemetry without pretending that an exact Apollo 13 CRT format has been recovered.
- **Direct-telemetry boundary:** the reviewed schematic positively labels PCMTEA taps for `GC0155` and `GC0071` but does **not** label equivalent PCMTEA taps for the `GL4046` caution output or the `4S14` selector position. This is sufficient to exclude those direct paths from first-playable historical telemetry unless a later primary routing source explicitly establishes them; it is not universal proof that no other Apollo document could contain an additional path.

## Apollo Experience Report — Flight-Control Data Needs, Terminal Display Devices, and Ground System Configuration Requirements

- **NASA document ID:** 19740015284
- **Report:** NASA TN D-7685 / JSC S-396, May 1974
- **NTRS:** https://ntrs.nasa.gov/citations/19740015284
- **Public scan:** https://www.ibiblio.org/apollo/Documents/TN-7685-ApolloExperienceReport-FlightControlNeeds.pdf
- **Status:** PRIMARY APOLLO-EXPERIENCE / REVIEWED for MCC computer-driven TV routing architecture.
- **Use:** documents that an individual console could request a display format, after which the computer formatted it, assigned the next available computer-driven TV channel, and automatically connected that channel to the requesting console. It also documents channel-attach mode, in which a console could attach to an already active TV channel.
- **Consequence for note 118:** do not model `GC0155` or `GC0071` as requiring a permanently assigned TELMU/CONTROL TV channel. The remaining Apollo 13-specific gap is the display-format/configuration record that identifies exact format identity, field placement, selection action, cadence, and latency.
- **Boundary:** this 1974 experience report describes Apollo MCC architecture generally; it does not identify the Apollo 13 PC+2 inverter format or prove which station had that format selected.

## Apollo 15 MCC Operational Configuration

- **Document:** *MCC Operational Configuration for Mission J1, AS-510 / SC-112 / LM-10, Apollo 15*, PHO-TR155, 15 Apr 1971.
- **Public scan:** https://ibiblio.org/apollo/Documents/MCC%20Operational%20Configuration%20Apollo%2015.pdf
- **Status:** PRIMARY / LATER-MISSION ARCHITECTURE CROSS-CHECK ONLY.
- **Use:** confirms separate LM TELMU Engineer and LM Control Engineer consoles in the later Apollo configuration.
- **Boundary:** not Apollo 13 format evidence and not used to infer a PC+2 display number, channel, field, or station selection state.

## Apollo 13 LM-7 Contingency Checklist — surviving artifact / transcripted read-up

- **Status:** PRIMARY PROCEDURAL EVIDENCE / REVIEWED THROUGH MISSION-SPECIFIC READ-UP; surviving artifact remains a useful future cross-check.
- **Key PC+2 modification:** at the -4 minute page-17 configuration, `CB(16) INVERTER 2` is closed and `Select Inverter 1` is scratched.
- **Consequence:** the stock checklist apparently expected the generic inverter-1 burn convention, but Apollo 13 deliberately removed that selection for PC+2.

## Current source-bounded conclusion

For the crew-side first-playable criterion:

`PC+2 selected inverter 2 → inverter light → close CB(11) EPS: INV 1 → select INVERTER 1 → open CB(16) EPS: INV 2 → selection transient handled by caution/inhibit logic → fresh valid warning re-observation → warning remains → shutdown criterion satisfied`

For the source-backed ground electrical observation path:

`selected inverter bus → GC0155 frequency + GC0071 voltage → conditioning/isolation → PCMTEA telemetry → communications/MSFN → MCC computer-driven display capability → [exact Apollo 13 format/station selection unresolved]`

The onboard derived caution remains a distinct path:

`GC0155/GC0071 failure-detection logic → GL4046 inverter caution → 6DS26 onboard indicator → crew observation/report`

Selected-inverter identity remains a procedural/action information path:

`crew breaker/selector transfer → explicit crew-action state/report → ground knowledge of selected inverter`

The initial inverter-2 identity is mission-specific and directly supported. The alternate inverter-1 identity is supported by the mission-specific starting state plus the two-inverter architecture. The exact transfer sequence is directly supported by the Apollo 13 LM Malfunction Procedures. The post-transfer timing rule is bounded as **valid-state re-observation rather than a fabricated crew dwell**. The underlying inverter voltage/frequency ground telemetry path is directly supported.

Research note 117 adds a bounded negative result: the reviewed primary schematics do not establish direct PCM telemetry of the `GL4046` caution state or INV1/INV2 selector position. The first playable therefore does not provide either as historical ground telemetry. A project-derived warning calculated from source-backed voltage/frequency may be used only if explicitly labeled as a modern/project rendering rather than a recovered caution discrete.

Research note 118 further narrows the MCC routing issue: Apollo computer-driven TV displays used dynamic display-request and channel-attach behavior, so the project must not invent a fixed historical TELMU/CONTROL TV channel for `GC0155` or `GC0071`. The exact Apollo 13 display-format identity, field placement, selection action, cadence, latency, and actual PC+2 station selection remain unresolved.

Exact Apollo 13 display-format identity/field placement, ground display cadence/latency, numeric selection-inhibit duration, crew-member assignment, exact controller wording, and any as-yet-unreviewed source establishing an additional caution/selector discrete remain unresolved and must not be invented.

## Research record

- `resources/research/059_pc2_inverter_warning_after_switch.md`
- `resources/research/060_pc2_inverter_contingency_action_report_loop.md`
- `resources/research/111_pc2_inverter_switch_identity.md` — generic-convention synthesis superseded in part
- `resources/research/112_pc2_inverter_selection_correction.md` — canonical initial inverter-2 selection correction
- `resources/research/113_pc2_inverter_alternate_identity.md` — resolves alternate inverter identity
- `resources/research/114_pc2_inverter_transfer_procedure.md` — resolves the cockpit inverter-2-to-inverter-1 transfer sequence
- `resources/research/115_pc2_inverter_reobservation_timing_boundary.md` — resolves first-playable post-transfer timing semantics as valid-state re-observation, with no invented numeric crew dwell
- `resources/research/116_pc2_inverter_ground_observation_path.md` — resolves the source-backed ground electrical-observation provenance through `GC0155`/`GC0071` PCMTEA telemetry while preserving caution/selector separation
- `resources/research/117_pc2_inverter_direct_caution_selector_telemetry_boundary.md` — bounds the remaining direct-telemetry question: reviewed primary schematics do not establish a PCM path for `GL4046` or selector position, so neither is exposed as historical ground telemetry in first playable
- `resources/research/118_pc2_inverter_mcc_display_routing_boundary.md` — resolves the fixed-channel architectural ambiguity: Apollo MCC computer-driven TV access was dynamically requested/attached; exact Apollo 13 inverter format and presentation remain unresolved
