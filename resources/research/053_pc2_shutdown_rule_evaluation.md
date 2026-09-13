# Apollo 13 PC+2 — shutdown-rule evaluation contract

Date: 2026-09-12  
Status: **REVIEWED — partial executable rule evaluation implemented; ISS-warning + program-alarm path now modeled, while several analog/conditional rules remain intentionally unevaluable**

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

The report separately states that if an early shutdown occurred for a reason other than those mandatory-shutdown conditions, the LM descent engine could be restarted using ullage, engine-start pushbutton, and descent-engine command override.

Source: NASA Flight Control Division, *Mission Operations Report — Apollo 13*, III-25.

### Technical air-to-ground / crew readback

At 76:30–76:38 GET CAPCOM read the rules to the crew and Haise read them back. This confirms the crew-side 77-percent thrust criterion, 160-psi inlet criterion, the ground-only fuel/OX delta-P callout, warning-light combinations, and restart procedure.

The contemporaneous transmission and readback both place the startup-transient exception on **attitude error**, followed separately by the ±10 deg/s attitude-rate limit. The later Mission Operations Report III-25 wording instead attaches the exception to attitude rate.

Research note 109 resolves the operational first-playable allocation by giving precedence to the actual transmitted-and-read-back rule while preserving the postflight wording conflict. The exact duration of the startup transient remains unresolved.

## Evaluation model

A rule evaluator returns:

- `clear` — available observations establish that the criterion is not active;
- `triggered` — available observations meet the documented shutdown criterion;
- `not_evaluable` — the project does not yet model the observation required to apply the rule;
- `not_applicable` — the rule is outside the relevant phase/condition.

`not_evaluable` is an implementation state, not a historical telemetry-validity state.

## Rule ownership / information paths

### CONTROL-ground criteria

- chamber pressure <= approximately 85 psi;
- inlet pressure <= approximately 150 psi;
- fuel/OX differential pressure >25 psi — ground callout only;
- engine-gimbal warning;
- attitude error ±10 deg except during the undefined start transient;
- attitude rate ±10 deg/s, with no startup exception in the contemporaneous transmitted/read-back rule;
- CES DC failure.

Exact nominal pressure, attitude-error, and rate values remain unmodeled. Those criteria remain `not_evaluable` rather than being assigned invented safe values.

### Crew/onboard criteria

- thrust monitor <=77 percent;
- inlet pressure <=160 psi;
- engine-gimbal light;
- ISS/inertial-reference warning **plus** program alarm;
- LGC warning;
- CES DC warning;
- inverter warning after attempted inverter switching.

Crew observations and ground telemetry are distinct paths even when they concern the same physical condition.

### GUIDO — ISS warning + program alarm

Research note 054 resolves the previously missing ISS-warning observation path. Contemporary LM GN&CS documentation shows ISS warning as a distinct onboard warning signal with a path to the Instrumentation Subsystem, separate from LGC warning. The evaluator can therefore apply the documented conjunctive rule directly:

- ISS warning absent or program alarm absent → criterion clear;
- ISS warning present **and** program alarm present → criterion triggered.

Exact Apollo 13 LM-7 telemetry-word assignment and GUIDO CRT placement remain unresolved and are not required for this information-path validation.

### TELMU / CONTROL interface

The inverter rule remains conditional: shutdown follows a warning that persists **after switching inverters**. A positive test must model the switch attempt; it is not equivalent to `inverter_warning == true` at all times.

## Nominal behavior

The source-backed fixture can evaluate modeled discrete criteria without fabricated numerics:

- engine-gimbal warning — clear nominally;
- ISS warning + program alarm — clear nominally;
- LGC warning — clear nominally;
- CES DC failure — clear nominally;
- persistent inverter warning — clear nominally because no inverter warning exists; positive case still requires switch-attempt state.

Pressure, delta-P, attitude/rate, and crew-side analog criteria remain explicitly unevaluable until their measurement/state paths are implemented.

For attitude specifically, note 109 resolves **which** criterion carries the startup exception but not **when** that transient ends. Do not infer a duration from the staged thrust profile without direct evidence.

## Important architecture rule

Do not collapse rule evaluation into an authoritative simulation value such as `burn_abort = true/false`.

Expose observations to responsible controllers and compute rule evaluations only as derived audit/validation objects. FLIGHT/CAPCOM/crew action remains a decision/communication path.

## Restart branch

Do not automatically restart after any engine stop. The documented restart procedure applied when an early shutdown occurred for a reason other than listed mandatory-shutdown conditions. A future failure scenario must preserve shutdown cause before offering the restart path.

## Deferred research

- exact duration/end boundary of the attitude-error startup-transient exception;
- exact normal PC+2 chamber/inlet/differential-pressure telemetry values;
- exact Apollo 13 LM-7 ISS warning telemetry word / GUIDO CRT location;
- positive-case inverter-switch attempt state;
- crew thrust-monitor and onboard inlet-pressure observation model.

See `resources/research/054_pc2_iss_warning_observation_path.md` and `resources/research/109_pc2_attitude_start_transient_scope.md`.
