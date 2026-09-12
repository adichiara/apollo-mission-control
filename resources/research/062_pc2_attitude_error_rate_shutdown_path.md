# Apollo 13 PC+2 — attitude-error and attitude-rate shutdown path

Date: 2026-09-12  
Status: **REVIEWED — sufficient for bounded implementation of the two rule observations; startup-transient documentation discrepancy preserved.**

## Question

What attitude-error and attitude-rate observations should the PC+2 simulator expose, and which criterion carries the documented startup-transient exception?

## Primary-source findings

### 1. Mission-specific thresholds are unambiguous

The Apollo 13 Flight Control Division *Mission Operations Report* records the PC+2 shutdown limits as:

- attitude rate: 10 deg/s;
- attitude error: 10 deg.

It places the phrase **“except start transients”** on the attitude-rate clause.

Source: NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970, PC+2 Mission Rules Review.

### 2. The contemporaneous crew-facing rule says the opposite

At 76:30:31 GET, CAPCOM Vance Brand read the PC+2 shutdown rules to the crew. His operational instruction was:

- attitude error: plus/minus 10 deg, with the startup-transient exception;
- attitude rate: plus/minus 10 deg/s, with no stated exception.

At 76:37:13 GET, Fred Haise read the rules back and independently repeated the same allocation: startup exception on attitude error, rate limit simply plus/minus 10 deg/s.

This is not a later editorial paraphrase: it is the contemporaneous air-ground operational exchange by which the rule was communicated and confirmed.

Sources:

- Apollo 13 Technical/PAO Air-to-Ground Transcription, 76:30–76:38 GET.
- Apollo 13 Flight Journal Day 4 transcript, used as a navigation/corrected-text aid.

### 3. Postflight CONTROL evidence shows both quantities were actually monitored

The CONTROL postflight account states that during PC+2:

- the maximum attitude error observed was about **7 deg in roll**;
- rates **never exceeded 1 deg/s**.

This directly supports treating attitude error and angular rate as separate controller-observable quantities rather than one generic guidance-stability flag.

The same account notes an unexpected roll GDA response at ignition, demonstrating why startup behavior was operationally relevant.

### 4. Measurement-family continuity evidence

Apollo LM instrumentation documentation identifies distinct attitude-error and RGA-rate telemetry families and routes them to LM guidance/control displays. Later searchable instrumentation tables list, for example, roll/pitch/yaw attitude-error channels and separate roll/pitch/yaw rate channels, with MSK 1123/1137 among the receiving display masks.

This supports the architecture of three-axis error and rate products but is **not** used to assert an exact Apollo 13 LM-7 PCM word/display field unless mission-specific evidence is recovered.

## Resolving the wording conflict for implementation

The repository must preserve both historical statements.

For the **operational simulator rule**, however, the stronger execution evidence is the rule that was actually transmitted to and read back by the crew immediately before PC+2. Therefore the first implementation uses:

- `abs(attitude_error_axis) > 10 deg` → shutdown criterion, **except during an identified startup transient**;
- `abs(body_rate_axis) > 10 deg/s` → shutdown criterion, with **no startup exception**.

This is an implementation evidence-precedence decision, not a claim that the postflight Mission Operations Report is definitively erroneous. The documentation discrepancy remains explicit.

## Startup-transient boundary remains unresolved

No reviewed source in this pass defines the exact start/end timing of “the start transient.”

Therefore the simulator must **not** equate it automatically with:

- the full 5-second minimum-thrust segment;
- the 21-second 40-percent segment;
- a guessed number of seconds after ignition.

Implementation should evaluate an over-limit attitude error as follows:

- outside a separately established startup-transient context: rule can be `TRIGGERED`;
- while a startup-transient exception is explicitly active: rule can be `NOT_APPLICABLE` for that observation;
- if whether the exception is active cannot be established: do not silently clear an over-limit error.

The first nominal fixture does not need to invent a transient flag because it does not supply a full attitude-error time series.

## Nominal validation envelope

The CONTROL postflight report supplies useful historical bounds without requiring reconstruction of a complete trace:

- maximum observed PC+2 attitude error: approximately 7 deg, roll axis;
- maximum observed rate: less than 1 deg/s.

These are validation envelopes, not initialization values and not permission to synthesize an arbitrary time history.

## Implementation contract

Add optional source observations:

- `vehicle.attitude_error_xyz_deg`
- `vehicle.body_rate_xyz_deg_s`

When absent, the corresponding rules remain `NOT_EVALUABLE`.

When present:

- evaluate the maximum absolute axis magnitude against the documented threshold;
- retain the full vector in the rule observation for controller/audit visibility;
- never turn a triggered audit rule directly into engine cutoff or an omniscient `burn_abort` state.

For attitude error only, allow a separately supplied `startup_transient_exception_active` context. Do not derive that context from guessed elapsed time.

## Station implications

### CONTROL

Source support improves for a PC+2-critical monitoring function: CONTROL explicitly monitored both error and rate during the burn and reported their postflight maxima. Exact Apollo 13 CRT field placement/PCM mapping remains incomplete, so CONTROL remains maturity B.

### GUIDO

Attitude error is also guidance-relevant, but this pass does not establish which PC+2 error/rate fields GUIDO independently relied upon versus CONTROL. Do not duplicate CONTROL products onto GUIDO solely for convenience.

## Sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970. https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf
- Apollo 13 Technical/PAO Air-to-Ground Transcription, 76:30–76:38 GET. https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- Apollo 13 Flight Journal, Day 4 Part 1. https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
- NASA, *Apollo Experience Report: Engineering and Analysis Mission Support*, NASA-TN-D-7993, 1975, used only for Apollo-wide telemetry/display-family continuity. https://ntrs.nasa.gov/citations/19750018953
