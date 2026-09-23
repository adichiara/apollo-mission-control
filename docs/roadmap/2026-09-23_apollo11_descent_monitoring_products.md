# Roadmap addendum — Apollo 11 descent monitoring products

Date: 2026-09-23

## Status change

The Apollo 11 powered-descent controller-product boundary advances from a generic search for throttle-recovery/high-gate monitoring to a narrower mission-specific mapping problem.

NASA/MSC 70-FM-20 preserves descent strip-chart comparisons for `AGS−PGNCS` and `MSFN−PGNCS` together with powered-descent event markers. This independently reinforces the already implemented guidance pairwise/consensus abstraction: source disagreement is a controller-relevant product family, not hidden simulator truth.

## Immediate next work

1. Keep the Apollo 11 reference **OPEN**.
2. Preserve `AGS−PGNCS` and `MSFN−PGNCS` as distinct source-comparison products; do not collapse them into one synthetic navigation-error value.
3. Do not expose Figure 9 as an exact live MOCR display. It establishes monitored quantities/event context, not exact console presentation.
4. Recover Mission-G-effective display/configuration evidence mapping these quantities to station-visible fields/requests/routing. PHO-TN401 is now a **precisely located archival target**: B. Costis, W. Ortolani, and W. Moreland, _NASA MCC Display/Control System Usage and Effectiveness, Apollo 11_, 24 Dec 1969, Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, **Box 078-65/66**.
5. Request/inspect that holding before broadening the search again. The locator comes from the Library of Congress/NPS HAER documentation of the Apollo Mission Control Center, whose authors directly cited PHO-TN401 (including p. 5-5).
6. Only after live mapping is sourced should the Apollo 11 runtime freeze controller-facing high-gate monitoring/call logic.

## Sources

- NASA/MSC, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 February 1970: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- Library of Congress / Historic American Engineering Record, _Johnson Space Center, Apollo Mission Control_, HAER No. TX-109-C. Footnote 37 and bibliography identify PHO-TN401 and its UHCL archival holding: https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf

## Evidence status

- **OPEN / NARROWED:** controller-product family demonstrated; exact live station mapping remains unresolved.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 itself remains uninspected, but its archival holding is now identified to collection and box.