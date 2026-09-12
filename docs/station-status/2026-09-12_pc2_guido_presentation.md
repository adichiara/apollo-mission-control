# Station research-status addendum — PC+2 GUIDO presentation

Date: 2026-09-12

## GUIDO

**Maturity remains B.**

Improved:

- first executable player-facing GUIDO presentation now exists;
- mission-specific Apollo 13 MSK 1123/1137 evidence constrains terminology and information families;
- LUMINARY 1C R-567 provides a direct Apollo 13-era source for program-dependent LGC downlinks and update verification;
- presentation preserves source/validity/provenance rather than flattening guidance information into one health flag;
- hidden product-integrity metadata remains outside the player view.

Still unresolved:

- exact GUIDO CRT request/selection behavior for PC+2;
- exact field coordinates and refresh cadence;
- exact display routing for ISS warning and several project assessment products;
- exact mapping of every downlist word into MSK 1123/1137 display fields;
- exact console hardware/DRK workflow needed only if later interaction requires it.

Research consequence:

The current evidence is sufficient for a useful, historically bounded GUIDO player view. Do not delay PC+2 implementation for cosmetic CRT reconstruction. Reopen exact field routing only when it changes a player decision or a primary source makes it inexpensive to resolve.

## CONTROL

**Maturity remains B.**

No new CONTROL research claim in this pass. The GUIDO implementation follows the same presentation rule already established for CONTROL: exact Apollo labels only when semantic/unit equivalence is supportable, otherwise explicit project rendering.

## TELMU

**Maturity remains B.**

No implementation change yet. TELMU is the next player-presentation target because its modeled PC+2 products already include a meaningful contingency dependency: inverter warning → switch action → distinct post-switch observation, plus burn-configuration/power-down state.
