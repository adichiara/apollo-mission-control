# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents a mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown using MSFN, onboard, and relative-tracking evidence. It also documents the reconstruction techniques and six descent solutions considered in landing-radar analysis. This supplies historical reconstruction/validation evidence, not a newly recovered Mission-G live display or raw controller truth stream.

The report's CSM-centered UVW-type relative-comparison frame (RZ = -U/radial, RX = V/downrange, RY = -W/crossrange, plus corresponding velocities) applies to the comparison figures described in Section 7.3. It is not promoted to a generic FIDO/GUIDANCE display convention or assumed to be the NAT frame.

The actual 45-day BET state listing is assigned by Volume I to **Volume II** in NASA Apollo Trajectory format. Because that volume is not presently recovered, no tabulated BET state series is available for the model lab without deriving one from secondary/graphical material.

## CONTROL

**Status: PARTIALLY DOCUMENTED for underlying DPS/resource physics; player product unchanged.** Primary documentation supports DPS throttling/gimbal/resource architecture. LM-5 launch propellant loading is documented, but PDI mass and an exact delivered thrust/Isp history remain unresolved. The postflight trajectory reconstruction does not close those propulsion inputs.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from the postflight reconstruction-method audit.

## Implementation boundary

Design-envelope values may constrain validation tests and scenario-input sanity checks. Volume I may define RECONSTRUCTED trajectory provenance and validation methodology. It must not be exposed directly as a controller product, and its plots must not be converted into apparently exact historical states. A state-series fixture awaits Volume II or an independently traceable archival derivative with preserved NAT metadata.

## Evidence status

- underlying DPS parameter semantics: **DOCUMENTED**;
- LM-5 launch resource bookkeeping: **DOCUMENTED**;
- Apollo 11 DOI→touchdown reconstruction methodology: **DOCUMENTED AS RECONSTRUCTED**;
- CSM-centered UVW comparison-frame semantics: **DOCUMENTED FOR THE SPECIFIC COMPARISON FIGURES**;
- 45-day BET NAT state listing / its exact state-series metadata: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 PDI mass and delivered DPS time history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.