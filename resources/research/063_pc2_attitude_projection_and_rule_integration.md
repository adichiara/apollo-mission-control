# Apollo 13 PC+2 — attitude projection and rule integration

Date: 2026-09-12  
Status: **IMPLEMENTED — startup-transient duration remains unresolved by primary sources.**

## Purpose

Complete the integration boundary left by research note 062: carry optional three-axis attitude-error and angular-rate observations through the common CONTROL product projection and into the PC+2 shutdown-rule audit without inventing a startup-transient clock interval.

## Primary-source recheck

A targeted primary-source search was made for an operational definition or time boundary for the PC+2 phrase “start transient.”

### Apollo 13 Mission Operations Report

The Flight Control Division postflight report gives:

- attitude rate limit 10 deg/s, except start transients;
- attitude error limit 10 deg.

It does not define when the transient begins or ends.

### Apollo 13 Review Board appendices

NASA-TM-X-66472, *Report of Apollo 13 Review Board* appendices, independently repeats the guidance/control shutdown parameters as:

- attitude rate >10 deg/s, except during start transient;
- attitude error >10 deg.

This is useful because it shows the postflight formulation is not confined to one summary document. It still does not define a duration or clock boundary.

### Contemporaneous air-ground rule transmission

At 76:30:31 GET CAPCOM instead instructed the crew to shut down for:

- attitude error ±10 deg, with the exception of the start transient;
- attitude rate ±10 deg/s.

Haise’s readback at 76:37:13 GET repeats that allocation.

No reviewed source in this pass defines the duration of “start transient.”

## Implementation consequence

The project continues to use the contemporaneous crew-facing rule for operational evaluation, while explicitly retaining the contradictory postflight wording.

The integration now works as follows:

1. `PC2State` can optionally carry `attitude_error_xyz_deg` and `body_rate_xyz_deg_s`.
2. When values are absent, CONTROL retains them as project-deferred fields; this is not represented as lost telemetry.
3. When values are present, CONTROL receives explicit three-axis products with units, timestamps, source layer, and provenance.
4. `shutdown_rules.py` delegates threshold evaluation to `attitude_monitoring.py`.
5. The attitude-error startup exception must be supplied explicitly to the audit as `True`, `False`, or unknown (`None`).
6. The audit never derives startup context from throttle phase, ignition time, or the five-second minimum-thrust command segment.
7. A triggered rule remains an audit result; it does not command engine cutoff or set an omniscient abort state.

## Why the transient is not tied to DPS engine-response timing

Primary propulsion documentation can describe engine chamber-pressure startup response, but the PC+2 rule phrase concerns an allowed guidance/control attitude-error transient. No reviewed source establishes that its operational boundary is identical to a propulsion pressure-settling interval.

Therefore propulsion startup specifications are not used as a substitute definition.

## Validation strategy

Integration tests cover:

- absent observations → deferred CONTROL fields and `NOT_EVALUABLE` audit results;
- historical postflight validation envelope (~7 deg maximum roll error, rates at or below about 1 deg/s) → clear rules;
- synthetic 10.1-deg error with unknown startup context → `NOT_EVALUABLE`;
- the same synthetic error with explicit non-startup context → `TRIGGERED`;
- the same synthetic error with explicit startup exception active → `NOT_APPLICABLE`;
- synthetic 10.1-deg/s rate → `TRIGGERED` even when the attitude-error startup context is active.

Synthetic values are boundary tests, not reconstructed Apollo 13 failures.

## Station implication

CONTROL’s PC+2 monitoring path is now represented end to end at the information-contract level: optional source observation → CONTROL product → rule audit. Exact LM-7 PCM assignment, calibration path, and CRT field remain unresolved, so CONTROL remains maturity B.

GUIDO is not automatically given duplicate rate/error products because current evidence does not establish the exact independent PC+2 display use at that station.

## Sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970. https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf
- NASA, *Report of Apollo 13 Review Board*, Appendices B–E, NASA-TM-X-66472, May 1970, NTRS 19700078726. https://ntrs.nasa.gov/citations/19700078726
- Apollo 13 Technical/PAO Air-to-Ground Transcription, 76:30–76:38 GET. https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- Research note `062_pc2_attitude_error_rate_shutdown_path.md`.
