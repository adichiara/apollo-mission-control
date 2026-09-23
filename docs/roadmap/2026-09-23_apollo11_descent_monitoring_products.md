# Roadmap addendum — Apollo 11 descent monitoring products

Date: 2026-09-23

## Status change

The Apollo 11 powered-descent controller-product boundary advances from a generic search for throttle-recovery/high-gate monitoring to a narrower mission-specific mapping problem.

NASA/MSC 70-FM-20 preserves descent strip-chart comparisons for `AGS−PGNCS` and `MSFN−PGNCS` together with powered-descent event markers. This independently reinforces the already implemented guidance pairwise/consensus abstraction: source disagreement is a controller-relevant product family, not hidden simulator truth.

## Immediate next work

1. Keep the Apollo 11 reference **OPEN**.
2. Preserve `AGS−PGNCS` and `MSFN−PGNCS` as distinct source-comparison products; do not collapse them into one synthetic navigation-error value.
3. Do not expose Figure 9 as an exact live MOCR display. It establishes monitored quantities/event context, not exact console presentation.
4. Recover Mission-G-effective display/configuration evidence mapping these quantities to station-visible fields/requests/routing. Prioritize PHO-TN401 and other Apollo-11-effective display/control records.
5. Only after that mapping is sourced should the Apollo 11 runtime freeze controller-facing high-gate monitoring/call logic.

## Source

NASA/MSC, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 February 1970: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf

## Evidence status

- **OPEN / NARROWED:** controller-product family now demonstrated; exact live station mapping remains unresolved.
- **BLOCKED:** PHO-TN401 direct inspection remains archival-recovery dependent.