# Progress — PC+2 attitude projection and rule integration

Date: 2026-09-12

## Completed

- Rechecked primary sources for a formal PC+2 startup-transient boundary.
- Confirmed that the Flight Control Division Mission Operations Report and Apollo 13 Review Board appendices both place the exception on attitude rate, while the contemporaneous CAPCOM read-up and Haise readback place it on attitude error.
- Found no reviewed primary source defining the transient duration or a clock-time boundary.
- Added optional three-axis attitude-error and angular-rate observations to `PC2State` without synthesizing a nominal time series.
- Integrated those observations into the common CONTROL projection with explicit units, timestamps, source layer, provenance, and project-deferred behavior when values are absent.
- Integrated `attitude_monitoring.py` into `shutdown_rules.py`.
- Kept startup-transient context explicit and separate from throttle phase/ignition timing.
- Added integration tests for missing observations, historical nominal validation envelopes, over-limit error with known/unknown startup context, and over-limit rate behavior.
- Added research note `063_pc2_attitude_projection_and_rule_integration.md`.

## Historical boundary retained

The simulator still does not know when the PC+2 “start transient” begins or ends. It must not infer that boundary from the five-second minimum-thrust command segment or from propulsion startup specifications.

## Station impact

CONTROL remains maturity B. Its attitude/rate monitoring path is now implemented at the information-contract level, but exact LM-7 PCM assignments, calibration/routing, and CONTROL CRT fields remain unresolved.

GUIDO remains B; attitude/rate products are not duplicated there without station-specific evidence.

## Validation status

A fresh repository-clone/test-suite execution was attempted after the commits. The container runtime returned a transient `ClientError` before the clone/test command executed, so the new tests are **committed but not recorded as executed/passing**. No test result is inferred from the runtime failure.

## Next documented stopping point

With the major PC+2 shutdown-rule observations now either implemented or explicitly bounded as unresolved, the next useful implementation step is to add **observation timestamp/age behavior to scenario injections and rule evaluation**, so a controller rule cannot silently evaluate from an indefinitely carried-forward analog observation. Research should first determine whether any PC+2 rule/procedure supplies an explicit freshness requirement; if not, implement age metadata without inventing a historical stale threshold.
