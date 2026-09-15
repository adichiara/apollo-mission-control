# Progress — D-022 initial gate survey and audit hardening

Date: 2026-09-15

## Issue #68 follow-up

The three withdrawn claims that motivated D-023 were already corrected and registry-seeded by PR #67. Their registry patterns are now broadened to catch reformatted regressions.

The stale multi-source guidance PR identified by #68 was superseded by PR #69, which transplanted the model onto current main.

## D-022 survey

Research note 214 surveys every currently unresolved PC+2 numerical integration gate in the active model profile.

Result: **no gate currently has a valid fully sourced same-input range suitable for D-022 sensitivity closure**.

The tempting mass pair (95,932 lb P30 sum vs 95,424 lb postflight event mass) remains invalid as a range because the values belong to different product classes. The 9,870-lbf Apollo 13 nominal full-thrust value and 10,500-lbf general maximum-rated value likewise remain different definitions rather than bounds on one delivered-thrust input.

D-022 therefore remains policy but has no current executable PC+2 target. Archival recovery remains the next step until a genuine same-input sourced interval appears.

## Audit hardening

- Restored the explanatory comment documenting why broad network/TLS exceptions remain distinguishable from HTTP failures.
- Added tests for malformed withdrawn-claims JSON.
- Added tests that a withdrawn claim referencing a missing correction-note path is rejected.
