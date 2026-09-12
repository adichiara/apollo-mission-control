# PC+2 Inlet-Pressure Source Addendum

Status: **active supplement to `PC2_IMPLEMENTATION_SOURCES.md`**  
Scope: sources added by research note 057 for the Apollo 13 PC+2 inlet-pressure observation path.

## Lunar Module 7, 8 & 9 Elementary Functional Diagrams

- **Document:** LED-267-37C
- **Vehicle family:** LM-7 / LM-8 / LM-9; Apollo 13 flew LM-7
- **URL:** https://www.ibiblio.org/apollo/Documents/lm-7%2C8%2C9_elementary_functional_diagrams.pdf
- **Status:** PRIMARY / REVIEWED for measurement identity
- **Relevant measurements:**
  - `GQ3611P` — PRESS ENGINE INTERFACE FUEL
  - `GQ4111P` — PRESS, ENGINE INTERFACE OXID
- **Use:** establishes that the Apollo 13 LM vehicle family had distinct fuel and oxidizer engine-interface pressure measurements.
- **Caution:** does not define the singular 150-psi PC+2 ground-rule aggregation/selection semantics.

## LM-7 OCP Outline

- **Document:** OCP-GF-26043-LM7
- **NASA document ID:** 19700001339
- **URL:** https://ntrs.nasa.gov/citations/19700001339
- **Status:** PRIMARY / REVIEWED-PARTIAL
- **Relevant content:** independently lists `GQ3611P` as Pressure, Engine Interface Fuel and `GQ4111P` as Pressure, Engine Interface Oxidizer; describes controlled pressurization and expected transducer indications during LM-7 checkout.
- **Use:** mission-specific LM-7 confirmation of both pressure-transducer identities.

## Apollo 13 Mission Operations Report

- **Organization:** NASA Flight Control Division
- **Date:** 28 Apr 1970
- **URL:** https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- **Status:** PRIMARY / REVIEWED-DETAILED for PC+2
- **Relevant rule:** engine inlet pressure = 150 psi on the ground or 160 psi onboard.
- **Use:** defines the PC+2 threshold but not how the singular ground value is selected/derived from the two LM interface-pressure measurements.

## Report of Apollo 13 Review Board — Appendix B

- **Organization:** NASA
- **Date:** 1970
- **Status:** PRIMARY / REVIEWED-PARTIAL for PC+2 rules
- **Relevant rule:** inlet pressure ≤150 psi (TM), ≤160 psi onboard.
- **Use:** independent confirmation of the threshold and ground/onboard distinction.

## Apollo 13 Technical Air-to-Ground Voice Transcription

- **Relevant interval:** ~76:30 GET PC+2 rule read-up/readback
- **Navigation:** https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
- **Status:** PRIMARY / REVIEWED-DETAILED for readback wording
- **Relevant content:** crew-side quantity described as DPS propellant-tank/inlet pressure with 160-psi shutdown threshold.
- **Caution:** does not establish which ground telemetry combination produced the singular 150-psi criterion.

## Apollo 10 LM-4 DPS Final Flight Evaluation

- **Report:** 11176-H314-R0-00
- **NASA document ID:** 19690026326
- **Date:** 8 Aug 1969
- **Status:** PRIMARY / CONTINUITY EVIDENCE
- **Relevant measurements:** `GQ3611P` and `GQ4111P` appear as engine fuel/oxidizer interface-pressure flight measurements.
- **Caution:** LM-4 sampling/performance details are not imported as Apollo 13 display cadence or rule semantics.

## Implementation consequence

These sources are sufficient to model two distinct LM-7 interface-pressure source observations, but **not** sufficient to implement the singular PC+2 150-psi ground rule as either-side, minimum, average, or selected value.

See `resources/research/057_pc2_dps_inlet_pressure_observation_path.md`.
