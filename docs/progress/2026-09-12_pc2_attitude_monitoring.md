# Progress — PC+2 attitude-error and attitude-rate monitoring

Date: 2026-09-12

## Research completed

Researched the next unresolved PC+2 shutdown-rule item using primary mission sources first.

Key result:

- the Apollo 13 Mission Operations Report places the phrase “except start transients” on the 10 deg/s attitude-rate criterion;
- CAPCOM's contemporaneous 76:30 GET rule read-up instead places the exception on the ±10 deg attitude-error criterion and then states ±10 deg/s rate with no exception;
- Fred Haise's 76:37 GET readback independently repeats the CAPCOM allocation.

The implementation therefore follows the rule actually transmitted to and confirmed by the crew while preserving the postflight-report wording as an explicit primary-source discrepancy. This is an evidence-precedence decision, not a silent correction of the historical record.

The reviewed sources do **not** define the exact duration of the startup transient. The project therefore does not equate it automatically with the five-second minimum-thrust segment or any other guessed interval.

## Additional primary evidence

The Apollo 13 CONTROL postflight account reports:

- maximum PC+2 attitude error of approximately 7 deg in roll;
- angular rates never exceeding 1 deg/s.

These values are now retained as nominal validation envelopes, not as fabricated time-series samples.

Apollo-wide LM instrumentation documentation also supports separate three-axis attitude-error and angular-rate measurement families. Exact Apollo 13 LM-7 PCM assignments, conversions, and CONTROL CRT routing remain unresolved.

## Repository changes

Added:

- `resources/research/062_pc2_attitude_error_rate_shutdown_path.md`
- `src/apollo_mission_control/attitude_monitoring.py`
- `tests/test_attitude_monitoring.py`
- `docs/station-status/2026-09-12_pc2_attitude_monitoring.md`

Updated:

- `docs/ROADMAP.md`
- `docs/scenarios/APOLLO13_PC2_PARAMETERS.md`
- `resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md`

The new helper supports:

- optional three-axis attitude-error observations;
- optional three-axis rate observations;
- 10 deg / 10 deg/s threshold evaluation;
- an explicitly supplied startup-transient context for attitude error only;
- `NOT_EVALUABLE` when observations or required transient context are missing;
- `NOT_APPLICABLE` for an explicitly over-limit attitude error while a sourced startup-transient exception is active;
- no direct cutoff/abort side effect.

Tests use the historical ~7 deg and <1 deg/s envelopes as nominal bounds and clearly labeled 10.1 synthetic values for rule-boundary behavior.

## Validation status

A test execution was attempted, but the container runtime returned a transient client error before the suite could run. The tests are committed but are **not recorded as passing**.

## New stopping point

Wire the new attitude-monitoring helper into the common CONTROL projection and `shutdown_rules.py` audit path without inventing a startup-transient time boundary.

Research the exact startup-transient definition only if a directly relevant primary flight-rule/procedure/control source becomes reasonably accessible. Otherwise keep that temporal boundary explicit and unresolved.
