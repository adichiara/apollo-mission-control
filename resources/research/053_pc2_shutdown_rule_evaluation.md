# Apollo 13 PC+2 — shutdown-rule evaluation contract

Date: 2026-09-12  
Status: **REVIEWED — sufficient to implement partial rule evaluation; several rules remain intentionally unevaluable until their measurement paths are modeled**

## Purpose

Convert the documented PC+2 Mission Rules into an executable evaluation contract without creating a generic authoritative `burn_abort` flag and without inventing nominal telemetry values.

## Primary sources

### Mission Operations Report — Apollo 13, 28 April 1970

At approximately 76:00 GET Mission Control reviewed the PC+2 shutdown criteria. The Flight Director report lists:

1. thrust chamber pressure: ground criterion 85 psi, or onboard thrust 77 percent;
2. engine inlet pressure: ground criterion 150 psi, or onboard 160 psi;
3. fuel/oxidizer differential pressure greater than 25 psi, explicitly a ground callout;
4. attitude-rate limit 10 deg/s and attitude-error limit 10 deg, with startup-transient wording in the report;
5. engine-gimbal warning;
6. inertial-reference warning plus computer program alarm;
7. LGC warning or CES DC power-failure warning;
8. inverter warning after switching inverters.

The report separately states that if an early shutdown occurred for a reason **other than those mandatory-shutdown conditions**, the LM descent engine could be restarted using ullage, engine-start pushbutton, and descent-engine command override.

Source: NASA Flight Control Division, *Mission Operations Report — Apollo 13*, III-25.

### Technical air-to-ground / crew readback

At 76:30–76:38 GET CAPCOM read the rules to the crew and Haise read them back. This confirms the crew-side 77-percent thrust criterion, 160-psi inlet criterion, the ground-only fuel/OX delta-P callout, the warning-light combinations, and the restart procedure.

It also exposes a wording difference that should not be silently normalized:

- the Mission Operations Report wording places the “except start transients” phrase with the **attitude-rate** limit;
- the crew readback places the exception with **attitude error**, then states the rate limit separately.

Both sources agree on approximately ±10 deg attitude error and ±10 deg/s attitude rate as the limits. The exact scope of the startup-transient exception should remain unresolved until stronger rule/procedure evidence is located or the distinction becomes implementation-critical.

Source: Apollo 13 technical air-to-ground record around 76:30 GET, preserved in the Flight Journal/PAO transcript.

## Evaluation model

A rule evaluator should return one of:

- `clear` — available observations establish that the criterion is not active;
- `triggered` — available observations meet the documented shutdown criterion;
- `not_evaluable` — the project does not yet model the observation required to apply the rule;
- `not_applicable` — the rule is outside the relevant phase/condition.

`not_evaluable` is an **implementation state**, not a historical telemetry-validity state.

## Rule ownership / information paths

### CONTROL-ground criteria

- chamber pressure <= approximately 85 psi;
- inlet pressure <= approximately 150 psi;
- fuel/OX differential pressure >25 psi — ground callout only;
- engine-gimbal warning;
- attitude/rate criteria;
- CES DC failure.

The exact nominal pressure, attitude-error and rate values remain unmodeled. These rules therefore remain `not_evaluable` in the current nominal executable model rather than being assigned invented safe values.

### Crew/onboard criteria

- thrust monitor <=77 percent;
- inlet pressure <=160 psi;
- engine-gimbal light;
- ISS/inertial-reference warning **plus** program alarm;
- LGC warning;
- CES DC warning;
- inverter warning after attempted inverter switching.

Crew observations and ground telemetry are distinct paths even when they concern the same physical condition.

### GUIDO

The inertial-reference + program-alarm criterion is conjunctive. A program alarm alone is not the documented rule. The current model has program-alarm state but does not yet model a distinct ISS/inertial-reference warning, so a future nonnominal positive case requires that additional state.

### TELMU / CONTROL interface

The inverter rule is conditional: shutdown follows a warning that persists **after switching inverters**. A future positive test must model the switch attempt; it is not equivalent to `inverter_warning == true` at all times.

## Nominal first-pass behavior

The current source-backed fixture can confidently evaluate only criteria whose observations are modeled without fabricated numerics:

- engine-gimbal warning — clear nominally;
- LGC warning — clear nominally;
- CES DC failure — clear nominally;
- ISS + program alarm — clear when no program alarm exists; a positive case remains incomplete without ISS warning state;
- persistent inverter warning — clear nominally because no inverter warning exists; a positive case requires switch-attempt state.

Pressure, delta-P, attitude/rate, and crew-side analog criteria remain explicitly unevaluable until their actual measurement/state paths are implemented.

## Important architecture rule

Do not collapse rule evaluation into an authoritative simulation value such as:

`burn_abort = true/false`

Instead expose the observations to the responsible controller and, where useful for validation/testing, compute rule evaluations as **derived audit objects**. FLIGHT/CAPCOM/crew action remains a decision/communication path.

## Restart branch

Do not automatically restart after any engine stop. The documented restart procedure applied when an early shutdown occurred for a reason other than the listed mandatory-shutdown criteria. A future failure scenario must therefore preserve the shutdown cause before offering the restart path.

## Deferred research

- exact scope of the startup-transient exception across attitude error vs attitude rate;
- exact normal PC+2 chamber/inlet/differential-pressure telemetry values;
- positive-case ISS warning state path;
- positive-case inverter-switch attempt state;
- crew thrust-monitor and onboard inlet-pressure observation model.

These are not blockers for implementing the partial evaluator and proving that unsupported criteria remain visibly unevaluable.
