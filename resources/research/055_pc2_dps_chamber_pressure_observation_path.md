# Apollo 13 PC+2 — DPS chamber-pressure observation path

Date: 2026-09-12  
Status: **REVIEWED — sufficient to model the ground chamber-pressure shutdown observation without inventing nominal PC+2 pressure values or exact CRT routing.**

## Purpose

Research note 054 established the first previously deferred discrete shutdown-rule observation path. The next implementation dependency is a propulsion-pressure path.

This note asks a deliberately narrow question:

> Can the PC+2 ground thrust-chamber-pressure shutdown criterion be represented as a real LM measurement delivered to CONTROL, rather than as an abstract rule input?

The answer is **yes**, with important limits preserved below.

---

## 1. Apollo 13 PC+2 rule

The Apollo 13 Flight Control Division *Mission Operations Report* records the PC+2 Mission Rules review at approximately 76:00 GET. One mandatory shutdown criterion was:

- thrust chamber pressure: approximately **85 psi on the ground**;
- corresponding onboard criterion: approximately **77 percent thrust**.

These are explicitly separate ground and onboard observations. The implementation must therefore not reduce them to one Boolean or infer the crew indication from the ground telemetry value.

Primary source:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970.
  https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf

---

## 2. Apollo 13 / LM-7 measurement identity

The already-inspected **LM-7/8/9 Elementary Functional Diagrams** identify:

- **GQ6510P — PRESS, THRUST CHAMBER**.

This is mission-era vehicle-family evidence: Apollo 13 flew LM-7. Research note 034 previously established GQ6510P as the prime source candidate for the Apollo 13 MSK 1137 `TCP` field while correctly leaving the exact CRT-routing edge provisional.

Primary source:

- *Lunar Module 7, 8 & 9 Elementary Functional Diagrams*.
  https://www.ibiblio.org/apollo/Documents/lm-7%2C8%2C9_elementary_functional_diagrams.pdf

Related repository evidence:

- `resources/research/034_apollo13_msk1137_non_lgc_telemetry.md`
- `resources/research/032_apollo13_lm_crt_field_provenance.md`

### Consequence

For the PC+2 simulation, `GQ6510P` may be treated as a real LM-7-family thrust-chamber-pressure measurement source.

This does **not** yet certify:

- the exact Apollo 13 PCM word/channel encoding;
- the exact CCATS/RTCC transformation;
- the exact MSK 1137 field routing or update cadence.

Those remain presentation/data-path gaps, not blockers to representing the measurement itself.

---

## 3. Contemporary DPS flight-instrumentation continuity

The Apollo 10 LM-4 *Descent Propulsion System Final Flight Evaluation* provides a directly inspectable flight-data table. Table 3 lists:

| Measurement | Description | Range | Sample rate in that flight-evaluation data set |
|---|---|---:|---:|
| `GQ3611P` | engine fuel interface pressure | 0–300 psia | 200 samples/s |
| `GQ4111P` | engine oxidizer interface pressure | 0–300 psia | 200 samples/s |
| `GQ6510P` | engine thrust chamber pressure | 0–200 psia | 200 samples/s |

The same report discusses measurement bias in chamber and interface-pressure instrumentation and uses the measurements in postflight propulsion analysis.

Primary source:

- TRW / NASA MSC, *Apollo 10 LM-4 Descent Propulsion System Final Flight Evaluation*, 8 August 1969, report 11176-H314-R0-00.
  https://www.nasa.gov/wp-content/uploads/static/history/afj/ap10fj/pdf/19690026326_a10-lm4-dps-final-flight-eval-trw-19690808.pdf

### Configuration caution

Apollo 10 flew LM-4, not LM-7. Therefore the **200 samples/s** figure is retained only as evidence of the engineering measurement's use in contemporary DPS flight analysis. It is **not** promoted to an Apollo 13 controller-display refresh rate or assumed PCM delivery cadence.

The LM-7-family diagrams, not the Apollo 10 table, are the authority for carrying `GQ6510P` into the Apollo 13 vehicle model.

---

## 4. Apollo 13 propulsion evidence

The Apollo 13 Mission Report states that, aside from the supercritical-helium anomaly, descent-propulsion operation including engine starts and throttle response was normal. The separate Apollo 13 LM propulsion post-mission material preserves analog recordings for the three DPS firings, including DPS 2 / PC+2.

Primary sources:

- *Apollo 13 Mission Report*, NASA-TM-X-66449 / MSC-02680, September 1970.
  https://ntrs.nasa.gov/citations/19710003598
- *MSC Apollo 13 Investigation Team, Panel 3 — Flight Operations and Network, Addendum 1*, NASA-TM-X-66935 / REPT-70-FC13-47-ADD-1, June 1970.
  https://ntrs.nasa.gov/citations/19710010487

These sources support the existence of propulsion flight data through the contingency burns. They do not, in the currently accessible indexed material, establish an exact nominal GQ6510P value at every instant of PC+2.

Therefore no nominal PC+2 chamber-pressure trace is invented.

---

## 5. Implementation decision

The first executable model may now add an **optional measured chamber-pressure observation**:

`dps.chamber_pressure_psi`

with these semantics:

```text
physical DPS condition
    ↓
GQ6510P thrust-chamber-pressure measurement
    ↓
telemetry / ground processing (details partly unresolved)
    ↓
CONTROL chamber-pressure product
    ↓
PC+2 ground criterion: <= 85 psi → shutdown-rule trigger
```

### Important null-state rule

The nominal fixture still has **no asserted numerical chamber-pressure value**.

Therefore:

- `None` in the project model means **not yet numerically modeled**;
- it must remain in `deferred_fields` and must **not** be rendered as historical telemetry `unavailable`;
- once a test/scenario explicitly supplies a chamber-pressure measurement, CONTROL receives a valid product and the rule becomes evaluable.

This preserves the existing distinction between implementation completeness and historical data validity.

---

## 6. Rule semantics

For a modeled valid ground chamber-pressure observation:

- value **> 85 psi** → criterion clear;
- value **<= 85 psi** → criterion triggered.

The current rule text is treated as an inclusive lower-limit criterion because the Flight Control report states the shutdown criterion as chamber pressure equal to 85 psi on the ground.

The audit result remains an observation/rule assessment only. It must not directly:

- stop the engine;
- mutate a generic `burn_abort` flag;
- issue a FLIGHT decision;
- generate a CAPCOM call.

Those action paths remain separate.

---

## 7. First nonnominal pressure-path validation

A source-backed rule-path test can now inject:

- `dps.chamber_pressure_psi = 80.0`

and assert:

1. CONTROL receives the chamber-pressure product;
2. the `ground_chamber_pressure` criterion is `TRIGGERED`;
3. no automatic shutdown command/state is generated.

**80 psi is a synthetic test value**, not a claim about an Apollo 13 failure case. It is chosen solely because it lies unambiguously beyond the documented 85-psi ground threshold.

No malfunction mechanism is implied by this test.

---

## 8. What remains unresolved

This pass does **not** resolve:

- an exact nominal PC+2 GQ6510P trace;
- sensor/transducer dynamics or bias for LM-7 PC+2;
- Apollo 13-specific sample/PCM delivery cadence;
- exact ground engineering conversion;
- exact MSK 1137 TCP routing/mask/update cadence;
- the separate onboard 77-percent-thrust observation path;
- engine physical failure mechanisms that would cause low chamber pressure.

These should be researched only when a scenario, display, or propulsion-model dependency requires them.

---

## 9. Consequence for next work

The project now has a second source-backed nonnominal rule path and the first analog propulsion measurement that can become evaluable only when explicitly modeled.

This is sufficient to begin a **generic failure-injection object** that perturbs underlying/observed state rather than setting a diagnosis, provided the first injection remains as simple as a documented measurement condition and is clearly labeled as a test fixture rather than a historical Apollo 13 malfunction scenario.
