# Shareable DPS tests

Open /admin, select MODEL, then RUN SHAREABLE TEST SUITE (or open /model-tests).
Enter the facilitator token if it is not already available from the test console.
Click Run standard suite. Add observations in Notes and Download report.
Attach that JSON file in the project chat, including when tests fail.

The runner sends ten fixed synthetic profiles to the actual server model API.
It checks mass, impulse, an independent analytic rocket-equation expectation,
step refinement, cutoff ordering, lower thrust, direction, omitted burn,
combined errors, repeatability, and build identity before/after the suite.

Exports include schema/suite versions, UTC timestamps, build metadata,
complete request/response pairs, checks with expected/actual values and
tolerances, errors, and optional notes. Tokens and request headers are excluded.
Do not put secrets in notes. Reports remain in memory until downloaded/copied.
Leaving or refreshing the page loses the current report.

PASS means numerical/API checks passed. It does not validate historical Apollo
parameters, live crew interaction, trajectory propagation, or station products.
INCOMPLETE preserves partial results after an HTTP error or 30-second timeout.
No session is created, reset, advanced, or modified.

To reproduce a case, submit its request object to
POST /api/admin/model-proof/dps-burn on the recorded build with facilitator
authorization. Compare using the exported tolerances, not rounded screenshots.

Implementation verification uses repository CI; browser interaction still
requires a human run. The canonical roadmap remains unchanged because PR #28
owns it; this runner supports the current causal-engine validation priority.
