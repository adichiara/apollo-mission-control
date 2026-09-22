# Roadmap continuation — Apollo 11 descent dynamics input audit

Date: 2026-09-22
Parent: `docs/roadmap/2026-09-22_apollo11_descent_continuous_trajectory_boundary.md`

## Bounded question

Which inputs already accepted by the generic DPS/translational proofs can be tied to primary Apollo sources without pretending that design values are Apollo 11 delivered-flight values?

## Primary-source findings

NASA TN D-7143 establishes the program/design envelope: pressure-fed hypergolic engine, 10:1 throttling ratio, 10,500 lbf maximum-rated thrust, ±6 degree gimbal capability, and a 305 lbf-sec/lbm end-of-duty-cycle specific-impulse design requirement. These are architecture/design evidence, not an LM-5 as-flown thrust/Isp time history.

The contemporary **Apollo 11 Press Kit** supplies a mission-specific preflight DPS specification: **9,870 lbf maximum rated thrust**, throttleable between **1,050 and 6,300 lbf**, with ±6° gimbal capability. This remains preflight specification evidence rather than delivered-flight thrust.

The Apollo 11 Mission Report says LM-5 advanced from minimum thrust to the **fixed throttle point (FTP)** about 26 seconds after PDI. A provenance audit of the searchable **LMA790-3-LM** Subsystems Data handbook found that its detailed 92.5-percent FTP description and explicit **9,870-lbf nominal fixed-full-throttle** statement belong to a later handbook/configuration family: surviving primary catalog records identify 1 February 1970 material as **LM-7 and subsequent**, and NTRS identifies the later operational handbook as **LM-11 and subsequent**.

Therefore the later handbook is retained as primary **design-family/control-semantics** evidence, not LM-5 calibration evidence. It corroborates that mature LM documentation treated fixed full throttle as a distinct operational point and nominally associated it with 9,870 lbf, but it cannot by itself prove the LM-5 force calibration. The apparent 9,870/10,500 issue remains a rating/configuration question rather than an arithmetic conversion.

The Apollo 11 final Flight Plan provides configuration bookkeeping but not PDI mass. SNA-8-D-027(III) Rev. 2 / NASA-TM-X-68968 is the correct mass-properties source family, but its surviving public binder contains later replacement pages and cannot be treated as a pristine Mission-G snapshot.

The **Apollo 11 Mission Report, Appendix A.6 / table A-I** provides primary postflight LM masses: **33,683.5 lb at separation, 33,669.6 lb at DOI ignition, 33,401.6 lb at DOI cutoff, and 16,153.2 lb at landing**. It contains no PDI row.

## Event-provenance hazard

NASA SP-4029 shifts Mission Report DOI masses into different event labels and is rejected for PDI closure. NASA technical paper **20080013635** uses **33,683.5 lb at PDI** in an approximate simulation, exactly matching the primary Mission Report's LM-separation mass. It is therefore a model input, not historical PDI evidence.

The gate remains: **a candidate PDI number is not closable merely because it appears in NASA material or numerically matches an authentic Apollo 11 mass. The source must explicitly establish Mission-G/LM-5 event identity and provenance.** The same rule now applies to propulsion calibration: a later LM handbook cannot silently become LM-5 configuration evidence.

## Supplement 7 recovery status

Primary NASA mission-report supplement tables document Apollo 11 Supplement 7, *Descent Propulsion System Final Flight Evaluation*, as published in **September 1970**. Current public/searchable holdings recover other Apollo 11 supplements but not this report. Treat this as a named archival recovery problem, not permission to infer its contents or identifiers from Apollo 10/12/14/15 reports.

## Existing model audit

| Model input | Apollo source status | Promotion decision |
| --- | --- | --- |
| `thrust_n` / `end_thrust_n` | Press Kit: 9,870-lbf LM-5 mission specification; Mission Report: LM-5 FTP timing; later LMA790-3-LM: 9,870-lbf nominal fixed-full-throttle / 92.5% mature-design semantics; D-7143: 10,500-lbf maximum-rated design requirement | Keep caller supplied; do not promote later-LM calibration to LM-5 or infer delivered thrust |
| `specific_impulse_s` | D-7143 design requirement; no LM-5 flight-effective history recovered | Keep caller supplied; do not freeze 305 s as Apollo 11 truth |
| `mass_kg` | Primary Mission Report documents named event masses through DOI cutoff and landing; no PDI row | Keep PDI mass unresolved; reject later event-relabeling/simulation assignments |
| `dry_mass_kg` | Published stage/resource bookkeeping does not equal model depletion-floor convention | Do not equate without a scenario mass convention |
| thrust `direction` | ±6° capability documented; attitude validation products documented | Exact command history unresolved |
| burn duration | 756.3 s documented | Historical checkpoint |
| continuous position/velocity history | Reconstruction method documented; Volume-II NAT listing unrecovered | Keep RECONSTRUCTED; do not fabricate exact samples |

## D-022 result

No D-022 closure is claimed for PDI mass, delivered thrust, or flight-effective Isp. The recovered sources support a bounded Apollo 11 preflight thrust specification and later-LM FTP semantics, but do not provide a sourced LM-5 delivered-force calibration range whose endpoints can be tested for demonstrated irrelevance.

## Architecture consequence

Historical validation may use **DOCUMENTED primary named-event masses + DOCUMENTED Apollo 11 preflight DPS specification + DOCUMENTED Apollo 11 FTP timing + DOCUMENTED later-LM FTP semantics (configuration-qualified) + DOCUMENTED as-flown throttle/pressure telemetry + RECONSTRUCTED trajectory methodology + MODELLED unresolved PDI mass/thrust/Isp inputs**. Any scenario fixture using a convenient PDI mass or exact throttle-to-force conversion must remain MODELLED unless mission-specific evidence closes it.

## Next

Continue Mission-G PDI-mass recovery from superseded ODB pages, contractor/postflight mass ledgers, or equivalent provenance-controlled primary records. For propulsion, prioritize a **LM-5-specific AOH/vehicle manual revision, acceptance/performance record, or Apollo 11 DPS Supplement 7**. Do not use the later LMA790-3-LM handbook as a substitute for LM-5 configuration evidence.

## Evidence status

**PARTIALLY DOCUMENTED.** Primary postflight LM mass checkpoints, Apollo 11 preflight DPS limits, and Apollo 11 FTP use are documented. Later primary operations documentation clarifies mature-design FTP semantics but is configuration-qualified. Exact LM-5 PDI mass, FTP force calibration, delivered thrust, and flight-effective Isp remain unresolved. Apollo 11 DPS Supplement 7 and TRW Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.