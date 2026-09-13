# PC+2 Inlet-Pressure Source Addendum

Status: **active supplement to `PC2_IMPLEMENTATION_SOURCES.md`**  
Scope: sources reviewed in research notes 057 and 106 for the Apollo 13 PC+2 inlet-pressure observation path and rule lineage.

## Lunar Module 7, 8 & 9 Elementary Functional Diagrams

- **Document:** LED-267-37C
- **Vehicle family:** LM-7 / LM-8 / LM-9; Apollo 13 flew LM-7
- **URL:** https://www.ibiblio.org/apollo/Documents/lm-7%2C8%2C9_elementary_functional_diagrams.pdf
- **Status:** PRIMARY / REVIEWED for measurement identity
- **Relevant measurements:**
  - `GQ3611P` — PRESS ENGINE INTERFACE FUEL
  - `GQ4111P` — PRESS, ENGINE INTERFACE OXID
- **Use:** establishes that the Apollo 13 LM vehicle family had distinct fuel and oxidizer engine-interface pressure measurements.
- **Caution:** does not by itself define the Apollo 13 PC+2 150-psi ground-rule selection semantics.

## LM-7 OCP Outline

- **Document:** OCP-GF-26043-LM7
- **NASA document ID:** 19700001339
- **URL:** https://ntrs.nasa.gov/citations/19700001339
- **Status:** PRIMARY / REVIEWED-PARTIAL
- **Relevant content:** independently lists `GQ3611P` as Pressure, Engine Interface Fuel and `GQ4111P` as Pressure, Engine Interface Oxidizer; describes controlled pressurization and expected transducer indications during LM-7 checkout.
- **Use:** mission-specific LM-7 confirmation of both pressure-transducer identities.

## LM Data Book Volume 2 Part 2 — LM-6 and subsequent launch mission-rule redlines

- **Document family:** SNA-8-D-027(II)PT2 / LED-540-57
- **Revision:** Rev. 5, 9 Mar 1970
- **Status:** PRIMARY / REVIEWED-PARTIAL
- **Relevant content:** lists `GQ3611P` and `GQ4111P` separately as Press Engine Interface Fuel / Press Engine Interface Ox; nominal operation table shows Fuel: 150 and Ox: 150 at 70°F.
- **Use:** confirms separate LM-7-family fuel and oxidizer interface-pressure measurements immediately before Apollo 13.
- **Caution:** this is redline/data-book evidence, not an Apollo 13 PC+2 maneuver-rule page; it does not prove that both values participate in the PC+2 ground shutdown criterion.

## Apollo 10 Mission Rules — Section 3, item 3-77

- **Organization:** NASA Manned Spacecraft Center
- **Revision date on reviewed page:** 23 Apr 1969
- **Status:** PRIMARY / REVIEWED for DPS maneuver-rule lineage
- **Relevant rule:** DPS maneuver inhibit if **fuel inlet pressure <120 psi for <65% throttle and <150 psi for >65% throttle**.
- **Use:** strongest recovered evidence that the 150-psi DPS ground criterion in the LOI/DPS rule lineage referred specifically to **fuel inlet pressure**, not a minimum/average of fuel and oxidizer.
- **Caution:** Apollo 10 is antecedent evidence, not an Apollo 13-specific rule page. It narrows the historical interpretation but does not authorize an exact Apollo 13 `GQ3611P` implementation by itself.

## Apollo 11 Mission Rules — Section 3, item 3-72

- **Organization:** NASA Manned Spacecraft Center
- **Date on reviewed summary:** 16 Apr 1969
- **Status:** PRIMARY / CONTINUITY EVIDENCE
- **Relevant rule:** DPS maneuver inhibit criterion names **fuel inlet pressure**, with a 120-psi value in the reviewed summary.
- **Use:** supports continuity of the controlled quantity as fuel inlet pressure.
- **Caution:** numeric limits differ from the Apollo 10 rule and from Apollo 13 PC+2; do not import the Apollo 11 threshold.

## Apollo 13 Mission Operations Report

- **Organization:** NASA Flight Control Division
- **Date:** 28 Apr 1970
- **URL:** https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- **Status:** PRIMARY / REVIEWED-DETAILED for PC+2
- **Relevant rule:** engine inlet pressure = 150 psi on the ground or 160 psi onboard.
- **Relevant burn profile:** approximately 5 sec at 12.6%, 21 sec at 40%, then approximately 235 sec at maximum thrust.
- **Use:** defines the Apollo 13 PC+2 threshold and shows that most of the burn was in the >65% regime corresponding to the 150-psi branch in the Apollo 10 DPS rule lineage.
- **Caution:** the Apollo 13 narrative uses generic “engine inlet pressure” wording and does not explicitly name `GQ3611P`.

## Apollo 13 CONTROL post-mission appendix

- **Container:** Flight Control Division *Mission Operations Report — Apollo 13*
- **Status:** PRIMARY / REVIEWED-PARTIAL
- **Relevant content:** states that several mission rules were passed to the crew for PC+2; describes “engine inlets” at the onboard 160-psia threshold and the fuel/oxidizer inlet delta-P >25 psia as a separate ground-only callout.
- **Use:** confirms CONTROL ownership/context and preserves the distinction between inlet-pressure and differential-pressure rules.
- **Caution:** does not expose the exact ground display field or explicitly map the 150-psi criterion to `GQ3611P`.

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
- **Relevant content:** CAPCOM says the rules should be similar to **LOI Mode I abort with tight limits**; crew-side quantity is described as DPS propellant-tank/inlet pressure with a 160-psi shutdown threshold.
- **Use:** supplies the explicit historical bridge from Apollo 13 PC+2 back to the LOI/DPS rule family in which Apollo 10 item 3-77 names fuel inlet pressure.
- **Caution:** does not establish which exact ground telemetry product CONTROL watched at 150 psi.

## Apollo 10 LM-4 DPS Final Flight Evaluation

- **Report:** 11176-H314-R0-00
- **NASA document ID:** 19690026326
- **Date:** 8 Aug 1969
- **Status:** PRIMARY / CONTINUITY EVIDENCE
- **Relevant measurements:** `GQ3611P` and `GQ4111P` appear as engine fuel/oxidizer interface-pressure flight measurements.
- **Caution:** LM-4 sampling/performance details are not imported as Apollo 13 display cadence or rule semantics.

## Current interpretation

The source set now supports a narrower conclusion than research note 057 alone:

- `GQ3611P` / fuel inlet pressure is the **leading lineage-supported candidate** for the Apollo 13 PC+2 150-psi ground criterion;
- there is no evidence supporting minimum(fuel, oxidizer), average(fuel, oxidizer), an either-side trigger, or a synthetic combined inlet-pressure product;
- an Apollo 13-specific rule/display/routing source explicitly tying PC+2 to `GQ3611P` has not yet been recovered.

Therefore the executable 150-psi rule remains **`NOT_EVALUABLE`**. If a later design deliberately adopts `GQ3611P`, it must be labeled as a lineage-based historical approximation unless stronger Apollo 13 evidence is found.

See `resources/research/057_pc2_dps_inlet_pressure_observation_path.md` and `resources/research/106_pc2_inlet_pressure_rule_lineage.md`.
