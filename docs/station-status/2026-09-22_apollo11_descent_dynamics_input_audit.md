# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents a mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown using MSFN, onboard, and relative-tracking evidence. It supplies historical reconstruction/validation evidence, not a newly recovered Mission-G live display or raw controller truth stream.

NASA TN D-6846 adds a primary NASA validation envelope: planned and postflight descent event/trajectory products, guidance thrust-command relationship, landing-radar updates, approach/landing trajectory and attitude, altitude-rate behavior, and landing-phase events. These can validate modeled behavior but are not to be converted into an invented exact controller display or exact continuous state history.

The actual 45-day BET state listing remains assigned to unrecovered Volume II in NASA Apollo Trajectory format. A targeted exact-identifier recovery pass found no public primary copy or traceable NAT-preserving derivative. That thread is now archive-triggered rather than an active broad-web search.

## CONTROL

**Status: PARTIALLY DOCUMENTED for underlying DPS/resource physics and validation behavior; player product unchanged.** Primary documentation supports DPS throttling/gimbal/resource architecture. TN D-6846 provides planned/commanded thrust behavior useful for validation. LM-5 launch propellant loading is documented, but PDI mass and exact delivered thrust/Isp history remain unresolved. Do not substitute the planned/commanded profile for delivered engine performance.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from the trajectory/propulsion validation audit.

## Implementation boundary

Design-envelope values may constrain tests and scenario-input sanity checks. Volume I defines RECONSTRUCTED trajectory provenance/methodology; TN D-6846 supplies source-backed validation/checkpoint relationships. Neither is a license to expose postflight reconstruction as live controller truth or to manufacture exact historical states/engine values.

## Evidence status

- underlying DPS parameter semantics: **DOCUMENTED**;
- LM-5 launch resource bookkeeping: **DOCUMENTED**;
- Apollo 11 DOI→touchdown reconstruction methodology: **DOCUMENTED AS RECONSTRUCTED**;
- source-backed descent validation/checkpoint envelope: **DOCUMENTED**;
- CSM-centered UVW comparison-frame semantics: **DOCUMENTED FOR THE SPECIFIC COMPARISON FIGURES**;
- 45-day BET NAT state listing / exact state-series metadata: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II; BROAD ONLINE DISCOVERY EXHAUSTED**;
- Apollo 11 PDI mass and delivered DPS time history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.