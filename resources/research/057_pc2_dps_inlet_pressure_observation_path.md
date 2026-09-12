# Apollo 13 PC+2 — DPS inlet-pressure observation path

Date: 2026-09-12  
Status: **REVIEWED-PARTIAL — LM-7 fuel/oxidizer engine-interface measurements are established, but the exact ground rule aggregation/selection behind singular “engine inlet pressure” remains unresolved. Do not implement the 150-psi rule as either-side/minimum/average without stronger evidence.**

## Purpose

After implementing the generic timed scenario-injection layer, the next candidate PC+2 observation is the DPS inlet-pressure shutdown criterion.

Question:

> Can the documented 150-psi ground engine-inlet-pressure criterion be mapped unambiguously to an Apollo 13 LM-7 measurement/product?

Answer: **the source measurements are clear; the exact rule-to-product mapping is not yet clear enough to freeze.**

## 1. PC+2 rule evidence

The Apollo 13 Flight Control Division Mission Operations Report records:

- **Engine inlet pressure = 150 psi on the ground or 160 psi onboard.**

The Apollo 13 Review Board Appendix B independently gives the early-termination criterion as:

- inlet pressure ≤150 psi (TM);
- inlet pressure ≤160 psi (on board).

The crew rule read-up at approximately 76:30 GET describes the onboard quantity as DPS propellant-tank pressure / inlet pressure and gives the 160-psi threshold.

Primary sources:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970.
- *Report of Apollo 13 Review Board*, Appendix B, PC+2 ground rules.
- Apollo 13 Technical Air-to-Ground Voice Transcription, rule read-up/readback near 76:30 GET.

## 2. LM-7 source measurements

The **Lunar Module 7, 8 & 9 Elementary Functional Diagrams** measurement index explicitly identifies two engine-interface pressure measurements:

- `GQ3611P` — **PRESS ENGINE INTERFACE FUEL**;
- `GQ4111P` — **PRESS, ENGINE INTERFACE OXID**.

Apollo 13 flew LM-7, so this is direct mission-era vehicle-family evidence that both fuel and oxidizer engine-interface pressure measurements existed.

Primary source:

- *Lunar Module 7, 8 & 9 Elementary Functional Diagrams*, LED-267-37C.
  https://www.ibiblio.org/apollo/Documents/lm-7%2C8%2C9_elementary_functional_diagrams.pdf

A separate LM-7 checkout document independently lists:

- Pressure, Engine Interface Fuel — `GQ3611P`;
- Pressure, Engine Interface Oxidizer — `GQ4111P`;

and describes transducer-output checks at controlled feed-section pressures.

Primary source:

- LM-7 OCP outline, `OCP-GF-26043-LM7`, NASA document ID 19700001339.
  https://ntrs.nasa.gov/citations/19700001339

## 3. Contemporary flight-data continuity

The Apollo 10 LM-4 DPS Final Flight Evaluation lists both `GQ3611P` and `GQ4111P` as engine fuel/oxidizer interface-pressure flight measurements, each with a 0–300 psia engineering range in that evaluation data set.

Later LM flight-performance reports retain the same measurement identities.

This continuity strengthens the interpretation of the LM-7 signals as actual propulsion feed/interface measurements, but later/earlier vehicle sampling rates are **not** imported as Apollo 13 controller display cadence.

## 4. The unresolved mapping

The historical PC+2 rule uses singular wording:

> engine inlet pressure

But the vehicle has distinct fuel and oxidizer interface-pressure measurements.

The currently reviewed primary material does **not** establish which of the following ground-rule semantics was used:

- either fuel or oxidizer interface pressure ≤150 psi;
- the lower/minimum of the two;
- a selected/processed single value;
- a different derived inlet-pressure product;
- another display convention not yet recovered.

Likewise, the crew's single 160-psi onboard indication should not be assumed to be a direct mirror of either telemetry transducer without reconstructing the onboard selector/display path.

## 5. Implementation decision

Do **not** yet make `ground_inlet_pressure` evaluable.

It should remain `NOT_EVALUABLE` in `shutdown_rules.py` until the selection/aggregation rule is sourced.

However, future authoritative runtime state may safely carry two distinct source observations:

- `dps_fuel_interface_pressure_psi` ← `GQ3611P`;
- `dps_oxidizer_interface_pressure_psi` ← `GQ4111P`.

Those measurements may be injected/projected individually once the implementation is extended, provided no single combined “inlet pressure” diagnosis is manufactured from them.

## 6. Scenario-injection consequence

The generic injection layer should **not** add a single `dps_inlet_pressure_psi` target at this stage.

A safe future extension is to add the two physical/measurement targets separately. The rule evaluator should still remain unresolved until ground-rule aggregation is documented.

This keeps the architecture useful without baking an unsupported interpretation into scenario files.

## 7. Next research target

The most valuable next evidence is one of:

1. Apollo 13 CONTROL/MSK documentation showing the inlet-pressure field(s) used during PC+2;
2. a PC+2/LOI mode-I rule/procedure defining whether the 150-psi ground criterion applied to either feed leg or to a processed value;
3. MCC/telemetry routing material tying `GQ3611P`/`GQ4111P` to the relevant CONTROL display and limit logic.

If none is readily accessible, stop rather than infer. The alternative next rule path is fuel/oxidizer differential pressure, where the existence of both interface measurements may help but the exact ground delta-P computation still requires source support.

## Sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970.
- *Report of Apollo 13 Review Board*, Appendix B.
- Apollo 13 Technical Air-to-Ground Voice Transcription, ~76:30 GET.
- *Lunar Module 7, 8 & 9 Elementary Functional Diagrams*, LED-267-37C.
- LM-7 OCP Outline, `OCP-GF-26043-LM7`, NASA ID 19700001339.
- TRW/NASA MSC, *Apollo 10 LM-4 Descent Propulsion System Final Flight Evaluation*, 8 Aug 1969, 11176-H314-R0-00.
