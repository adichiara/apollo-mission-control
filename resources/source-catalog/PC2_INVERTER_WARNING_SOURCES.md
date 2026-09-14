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

## Apollo Experience Report — Lunar Module Instrumentation Subsystem

- **NASA document ID:** 19720018206
- **Report:** NASA TN D-6845 / MSC-S-294, June 1972
- **NTRS:** https://ntrs.nasa.gov/citations/19720018206
- **Public scan:** https://www.ibiblio.org/apollo/Documents/19720018206.pdf
- **Status:** PRIMARY TECHNICAL / REVIEWED for inverter warning generation, transient inhibit, and underlying ground-telemetry provenance.
- **Use:** documents the inverter caution-generation path, LM-5-and-subsequent inverter-selection transient-inhibit behavior applicable to Apollo 13 LM-7, and the telemetry path for the electrical quantities that drive the caution.
- **Figure 27 ground-observation evidence:** inverter-bus frequency **`GC0155`** and inverter-bus voltage **`GC0071`** each pass through isolation to **Telemetry PCMTEA**. The report's instrumentation architecture places PCMTEA data on the communications/MSFN path. Frequency failure-detection limits shown are **>402.0 Hz** and **<398.0 Hz**; the voltage failure-detection limit shown is **<112.0 V ac**.
- **Onboard caution separation:** the derived electrical-power-system inverter caution is identified as **`GL4046`**, with indicator **`6DS26`**. Figure 27 shows that caution path separately from the `GC0155`/`GC0071` PCM telemetry taps.
- **Selection-transient evidence:** LM-5-and-later circuitry delays removal of the caution inhibit during inverter selection until valid processed inverter data are established.
- **First-playable consequence:** normal selection-transient suppression belongs to spacecraft indication logic, not a separate crew persistence timer. Ground controllers may receive a project-rendered electrical product based on source-backed `GC0155`/`GC0071` telemetry without pretending that an exact Apollo 13 CRT format has been recovered.
- **Boundary:** Figure 27 does **not** establish a direct PCM telemetry tap for the `GL4046` caution discrete or INV1/INV2 selector position. It also does not establish the exact Apollo 13 MSFN/CCATS/RTCC-to-TELMU/CONTROL routing, CRT/MSK field, display cadence/latency, or numeric selection-inhibit duration.

## Apollo 13 LM-7 Contingency Checklist — surviving artifact / transcripted read-up

- **Status:** PRIMARY PROCEDURAL EVIDENCE / REVIEWED THROUGH MISSION-SPECIFIC READ-UP; surviving artifact remains a useful future cross-check.
- **Key PC+2 modification:** at the -4 minute page-17 configuration, `CB(16) INVERTER 2` is closed and `Select Inverter 1` is scratched.
- **Consequence:** the stock checklist apparently expected the generic inverter-1 burn convention, but Apollo 13 deliberately removed that selection for PC+2.

## Current source-bounded conclusion

For the crew-side first-playable criterion:

`PC+2 selected inverter 2 → inverter light → close CB(11) EPS: INV 1 → select INVERTER 1 → open CB(16) EPS: INV 2 → selection transient handled by caution/inhibit logic → fresh valid warning re-observation → warning remains → shutdown criterion satisfied`

For the source-backed ground electrical observation path:

`selected inverter bus → GC0155 frequency + GC0071 voltage → conditioning/isolation → PCMTEA telemetry → communications/MSFN → [exact MCC station routing/display unresolved]`

The onboard derived caution remains a distinct path:

`GC0155/GC0071 failure-detection logic → GL4046 inverter caution → 6DS26 onboard indicator`

The initial inverter-2 identity is mission-specific and directly supported. The alternate inverter-1 identity is supported by the mission-specific starting state plus the two-inverter architecture. The exact transfer sequence is directly supported by the Apollo 13 LM Malfunction Procedures. The post-transfer timing rule is bounded as **valid-state re-observation rather than a fabricated crew dwell**. The underlying inverter voltage/frequency ground telemetry path is now directly supported.

A numeric inhibit duration, direct ground telemetry of the `GL4046` caution state, INV1/INV2 selector-position telemetry, exact TELMU/CONTROL routing/display field, ground display latency/cadence, crew-member assignment, and exact controller wording remain unresolved and must not be invented.

## Research record

- `resources/research/059_pc2_inverter_warning_after_switch.md`
- `resources/research/060_pc2_inverter_contingency_action_report_loop.md`
- `resources/research/111_pc2_inverter_switch_identity.md` — generic-convention synthesis superseded in part
- `resources/research/112_pc2_inverter_selection_correction.md` — canonical initial inverter-2 selection correction
- `resources/research/113_pc2_inverter_alternate_identity.md` — resolves alternate inverter identity
- `resources/research/114_pc2_inverter_transfer_procedure.md` — resolves the cockpit inverter-2-to-inverter-1 transfer sequence
- `resources/research/115_pc2_inverter_reobservation_timing_boundary.md` — resolves first-playable post-transfer timing semantics as valid-state re-observation, with no invented numeric crew dwell
- `resources/research/116_pc2_inverter_ground_observation_path.md` — resolves the source-backed ground electrical-observation provenance through `GC0155`/`GC0071` PCMTEA telemetry while preserving unresolved caution-discrete, selector-position, and exact station-routing details
