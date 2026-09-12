# Apollo 13 PC+2 — fuel/oxidizer differential-pressure observation path

Date: 2026-09-12  
Status: **REVIEWED-PARTIAL — sufficient to model the documented ground differential-pressure observation as an independent ground-derived product; exact computation/routing from LM source measurements remains unresolved and must not be inferred.**

## Purpose

Research note 057 established the separate LM-7 fuel and oxidizer engine-interface pressure measurements but could not resolve how the singular 150-psi ground inlet-pressure criterion selected or combined them.

The documented stop condition was therefore applied: do not infer the inlet-pressure mapping; examine the next PC+2 propulsion rule instead.

Question:

> Can the PC+2 fuel/oxidizer differential-pressure shutdown criterion be represented without inventing an unsupported calculation from the two interface-pressure transducers?

Answer: **yes, if the ground ΔP is represented as its own optional ground-derived observation and its internal transformation remains explicitly unresolved.**

## 1. Apollo 13 PC+2 rule evidence

The Flight Control Division *Mission Operations Report — Apollo 13* states the PC+2 shutdown criterion as:

- fuel/oxidizer ΔP greater than **25 psi**;
- based on a **ground call-out**.

The contemporaneous Apollo 13 air-ground rule read-up at approximately 76:30 GET likewise tells the crew that fuel-to-oxidizer ΔP greater than 25 psi is a ground callout.

This directly establishes three implementation facts:

1. a scalar fuel/oxidizer differential-pressure criterion existed;
2. the trigger relation was **greater than 25 psi**;
3. the crew depended on the ground for this criterion rather than independently reading the same value onboard.

Primary sources:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970, p. III-25.
- Apollo 13 technical/PAO air-ground transcript near 76:30 GET.

## 2. Relationship to LOI Mode I rules

CAPCOM explicitly introduced the PC+2 criteria by saying their philosophy should be similar to **LOI Mode I abort with the tight limits**.

Apollo 11 Final Flight Mission Rules provide useful contemporary continuity evidence for that rule family. The revised LOI rule includes:

- fuel-oxidizer ΔP greater than 20 psi, confirmed by a drop in chamber pressure.

This does **not** justify importing Apollo 11's 20-psi threshold or its exact confirmation logic into Apollo 13 PC+2. Apollo 13's mission-specific sources supersede those details with the 25-psi ground-callout criterion.

What it does support is treating fuel/oxidizer ΔP as a distinct propulsion-monitoring rule quantity rather than collapsing it into the inlet-pressure or chamber-pressure rules.

Primary source:

- NASA MSC, *Apollo 11 Final Flight Mission Rules*, revised 3 Jul 1969, LOI rule summary.

## 3. Source measurements remain separate

Research note 057 established LM-7-family source measurements:

- `GQ3611P` — engine-interface fuel pressure;
- `GQ4111P` — engine-interface oxidizer pressure.

It is tempting to define the PC+2 rule product simply as one measurement subtracted from the other. The reviewed evidence does **not** yet establish:

- sign convention;
- absolute-value versus signed difference;
- whether the displayed/monitored quantity was computed directly from those two telemetry words;
- ground filtering, scaling, validation, or limit logic;
- exact CONTROL display field or update cadence.

Therefore the executable model must not derive the historical ΔP from those measurements yet.

## 4. Implementation decision

Add an optional runtime observation:

- `dps_fuel_oxidizer_delta_p_psi`

Semantics:

- it represents the **ground-derived fuel/oxidizer differential-pressure product** used by CONTROL for the PC+2 rule;
- `None` means the project has not supplied/modelled that ground product, not that Apollo telemetry was unavailable;
- when a value exists, CONTROL may project it as `dps.fuel_oxidizer_delta_p_psi`;
- rule evaluation is:
  - `> 25 psi` → `TRIGGERED`;
  - `<= 25 psi` → `CLEAR`;
  - no modeled product → `NOT_EVALUABLE`.

The exact transformation from underlying LM pressure measurements remains a future ground-processing research item.

## 5. Safe test fixture

A source-bounded implementation test may inject a synthetic **26 psi** ground ΔP observation during the burn and confirm that the rule evaluator triggers.

That test value is not an Apollo 13 historical malfunction or reconstructed telemetry sample. It exists only to test the documented >25-psi boundary.

Likewise, an exact 25-psi test should remain clear because the source wording is **greater than 25 psi**, not greater-than-or-equal.

Neither result may automatically stop the engine or set a generic abort flag.

## 6. Inlet-pressure research stop remains in force

This work does not resolve the singular 150-psi inlet-pressure mapping from note 057.

The project should continue to carry:

- fuel and oxidizer interface measurement identities as known source measurements;
- singular ground inlet-pressure selection/aggregation as unresolved;
- fuel/oxidizer ΔP as an independently documented ground-derived rule product.

These are separate questions.

## 7. Next research target

After implementing this bounded ΔP path, the next useful unresolved PC+2 observation should be chosen by evidence strength. Candidates include:

- persistent inverter warning after an inverter-switch attempt;
- attitude-error/rate observations and the startup-transient wording conflict;
- crew/onboard thrust-monitor or propellant-pressure indication paths.

Do not resume the inlet-pressure aggregation question unless a direct CONTROL/procedure/display source becomes available cheaply.

## Sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970, p. III-25.
  - https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf
- NASA Apollo 13 PAO / air-ground transcript, approximately 76:30 GET.
  - https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- NASA MSC, *Apollo 11 Final Flight Mission Rules*, revised 3 Jul 1969, LOI rule summary.
  - https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf
- *Lunar Module 7, 8 & 9 Elementary Functional Diagrams*, LED-267-37C, for the separate GQ3611P/GQ4111P source measurements established in note 057.
