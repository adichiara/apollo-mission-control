# Progress — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## Completed

Audited the generic DPS and translational model inputs against primary Apollo documentation. NASA TN D-7143 maps cleanly onto existing thrust, effective-Isp, direction/gimbal, and depletion semantics, but its design values remain design-envelope evidence rather than an LM-5 delivered-flight profile. The Apollo 11 press kit provides launch mass/resource bookkeeping but not PDI mass, and the Mission Report supplies the 756.3-second powered-descent checkpoint without a continuous throttle history.

TRW Note 70-FMT-819 / NASA CR-108349 Volume I documents a postflight continuous LM trajectory reconstruction from DOI through touchdown, based on combined MSFN/onboard/relative-tracking evidence. It remains **RECONSTRUCTED**, not raw truth. Volume I explicitly assigns the actual 45-day NAT-format BET listing to Volume II.

### Volume-II recovery challenge

Ran a targeted recovery pass using `70-FMT-819`, the full title, Volume II, 45-day BET, NASA Apollo Trajectory/NAT, contractor identifiers, NASA accession terms, NTRS, and archive-oriented searches. No public primary Volume-II copy or traceable derivative preserving NAT metadata surfaced. Volume I itself says the listing was not generally distributed and directed requests to the MSC Central Metric Data File.

Result: the state listing remains **BLOCKED ON NAMED SOURCE RECOVERY**, but broad online discovery is now exhausted. Reopen this thread on a concrete archive/digitization lead rather than repeatedly searching the same web corpus.

### Primary validation envelope

Recovered and audited NASA TN D-6846 / MSC-S-295, Floyd V. Bennett, *Apollo Experience Report: Mission Planning for Lunar Module Descent and Ascent* (June 1972; NTRS 19720018205). It is a primary NASA synthesis of Apollo 11 premission planning, real-time events, and postflight analysis and includes source-backed descent validation products: planned event/thrust/attitude behavior, guidance thrust command versus horizontal velocity, landing-radar updates, approach/landing trajectory and attitude products, altitude-rate behavior, and landing-phase events.

This does not provide an exact delivered LM-5 thrust/Isp history or the missing NAT states. It does provide a legitimate validation envelope for model behavior, allowing historical checks to proceed without fabricating exact inputs.

## Boundary preserved

No launch mass was substituted for PDI mass. No design thrust or Isp was promoted to an Apollo 11 as-flown value. No reconstructed state was relabeled raw telemetry. No state series was digitized from plots and presented as Volume-II BET. No planned or commanded thrust curve was relabeled as exact delivered engine performance.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

Move the active search to LM-5 PDI mass/state bookkeeping, prioritizing mission-specific mass-property/operational-data and postflight propulsion/performance records. Keep delivered DPS thrust/Isp as a parallel unresolved input. Volume-II BET recovery is archive-triggered rather than a standing broad-search task.

## Evidence status

**PARTIALLY DOCUMENTED.** Reconstruction methodology and a primary descent validation envelope are bounded. The tabulated 45-day BET state history remains **BLOCKED ON NAMED SOURCE RECOVERY**. PDI mass and delivered DPS thrust/Isp history remain unresolved.