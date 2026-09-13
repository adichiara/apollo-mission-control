# Progress — PC+2 inlet-pressure rule lineage

Date: 2026-09-13

## Completed

- Reopened the bounded 150-psi ground inlet-pressure question without changing the executable rule.
- Located a surviving Apollo 10 DPS mission rule explicitly naming **fuel inlet pressure** and using a 150-psi threshold above 65% throttle.
- Confirmed Apollo 13's PC+2 rule read-up described the rules as similar to LOI Mode I abort with tight limits.
- Confirmed Apollo 13 PC+2 spent most of its burn at maximum thrust after short 12.6% and 40% segments.
- Reviewed LM-7-and-subsequent redline data showing `GQ3611P` and `GQ4111P` as separate fuel/oxidizer engine-interface pressure measurements.
- Added research note 106 and updated the focused source catalog and project status documentation.

## Result

The historical evidence now strongly favors **fuel inlet pressure (`GQ3611P`)** as the lineage behind the Apollo 13 150-psi ground criterion. However, no reviewed Apollo 13-specific source explicitly maps the PC+2 ground rule to `GQ3611P`, and Apollo 13 narrative material uses generic “engine inlet pressure” wording.

Accordingly:

- the ground 150-psi rule remains `NOT_EVALUABLE`;
- no fuel/oxidizer minimum, average, either-side trigger, or synthetic combined inlet-pressure product is introduced;
- `GQ3611P` is recorded as the leading lineage-supported candidate, not as a proven Apollo 13 mapping.

## Blocking boundary

No physical-play PASS claim is added. Seven-seat nominal live-device validation, synthetic ΔP play, and five-player compact validation remain the next unclosed validation boundaries.
