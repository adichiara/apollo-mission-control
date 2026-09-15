# Station research-status addendum — PC+2 TELMU presentation

Date: 2026-09-12

## TELMU

**Maturity remains B.**

Improved:

- first-pass player-facing TELMU presentation now exists;
- burn power configuration, documented 38–40 A reference load, inverter contingency, and post-burn power-down are represented without inventing an exact CRT;
- reference/planning values are explicitly distinguished from live measured telemetry;
- crew switch action remains separate from the onboard INVERTER caution;
- **2026-09-15 correction:** the derived caution is no longer rendered as direct TELMU telemetry; reviewed schematics establish underlying inverter-bus voltage/frequency telemetry but not a direct caution channel;
- hidden integrity metadata remains outside the player view.

Still unresolved:

- exact Apollo 13 TELMU CRT/display used for PC+2;
- exact field coordinates/abbreviations;
- exact measured-current telemetry identifier/routing/update cadence for the burn configuration;
- exact H-2 loading/display path for `GC0071V` / `GC0155F`;
- whether stronger primary evidence ever establishes a direct derived-caution telemetry path; current reviewed evidence does not;
- broader consumable-lifetime presentation, which is intentionally out of scope for the first PC+2 screen.

## FLIGHT / CAPCOM interaction

No new historical voice-loop routing is asserted. TELMU provides its own station information; FLIGHT/CAPCOM integration remains through explicit controller reports/communications rather than a hidden synthesized health state.

## Research stop condition

The PC+2 TELMU presentation is sufficient for the first playable slice. Further TELMU archival reconstruction should be demand-driven by an actual player decision, not pursued for visual completeness alone.

## Next station presentation

FIDO/RETRO: maneuver target, RTCC/trajectory-solution status, return consequences, and post-burn trajectory assessment.
