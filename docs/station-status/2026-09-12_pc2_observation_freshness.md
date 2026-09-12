# PC+2 station-status addendum — observation age/freshness

Date: 2026-09-12

## CONTROL

Maturity remains **B**.

The PC+2 analog product contract now preserves the actual observation/sample timestamp separately from projection/display time. This prevents a carried-forward chamber-pressure, delta-P, or attitude/rate value from being silently re-labeled as newly observed when a later controller projection is rendered.

No reviewed primary source establishes a generic PC+2 stale-data timeout, confirmation count, or maximum acceptable age for the analog shutdown criteria. The simulator therefore exposes age/validity metadata without inventing a threshold.

Remaining gaps include exact LM-7 PCM/display routing, historical display cadence for the required CONTROL fields, and any station-specific procedure for frozen/questionable data.

## TELMU / GUIDO

Maturity remains **B**.

The same architectural distinction applies to discrete warning observations and guidance products: observation time and display/evaluation time are separate. However, this pass does not assign a generic expiration interval to those products.

The inverter criterion remains governed by its source-specific ordering requirement: a warning must be observed after the inverter switch action. That rule is not generalized into a universal freshness timer.

## CAPCOM / FLIGHT

Maturity remains **B**.

No new display reconstruction was established. The relevant result is procedural: PC+2 rule read-up distinguishes onboard indications from ground-call criteria but does not specify an analog-observation age window.

## Maturity effect

No station changes grade. This pass improves the implementation contract and information fidelity rather than resolving missing console/display evidence.
