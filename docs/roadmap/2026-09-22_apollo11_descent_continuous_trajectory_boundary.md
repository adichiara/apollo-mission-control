# Roadmap continuation — Apollo 11 continuous powered-descent trajectory boundary

Date: 2026-09-22
Parent: `docs/roadmap/2026-09-21_apollo11_p66_decision_gate_integration.md`

## Bounded question

What source basis is sufficient to move from the already implemented phase/decision-gate model toward a continuous Apollo 11 powered-descent trajectory without inventing a high-fidelity flown trajectory?

## Primary-source findings

NASA TM X-58038 documents the ground guidance-monitoring architecture used during Apollo 11 descent: MSFN tracking was processed independently and compared with PGNS/AGS-derived information through terminal descent. This supports continuous controller observation/comparison, but it is not itself a complete spacecraft dynamics reconstruction.

NASA TN D-7143 documents the LM descent propulsion system as a throttleable, gimbaled, pressure-fed engine and describes its interfaces with guidance/navigation. It is authoritative for DPS architecture and operating characteristics, but it is a post-program experience report rather than an Apollo-11-specific time history.

NASA's lunar-descent guidance technical literature describes P63/P64/P65/P66 as interactive guidance programs controlling altitude/trajectory and DPS throttle. It supports program semantics and causal coupling, not an exact Apollo 11 as-flown state vector at arbitrary time.

A later NASA reconstruction, TM-20220007267, explicitly reports that open archival data are insufficient for direct reconstruction of the Apollo 11 final landing trajectory and therefore uses digitized graphics plus estimation methods. This is useful as a boundary finding: a continuous as-flown trajectory generated from such reconstruction must be labeled reconstructed/estimated, not DOCUMENTED historical truth.

## Architecture consequence

Keep three layers distinct:

1. **DOCUMENTED causal model:** guidance program/control mode → commanded attitude/throttle/descent behavior → vehicle dynamics → independently produced controller observations.
2. **DOCUMENTED checkpoints/ranges:** mission-report and contemporary technical values that can validate discrete events or bounded quantities.
3. **RECONSTRUCTED continuous trajectory:** interpolation/estimation between sparse historical observations, carrying explicit reconstruction provenance and uncertainty.

The current generic translational/DPS engine may be extended toward layer 1 using source-backed LM physics. It must not silently promote a modern fitted Apollo 11 trajectory to primary-source truth.

## Status

**PARTIALLY DOCUMENTED / sufficient to define the next model boundary.**

Continuous dynamics are justified as a reusable causal capability. Exact Apollo 11 continuous trajectory history remains unresolved as primary-source truth.

## Next

1. Inventory which existing generic DPS/translational parameters already have source-backed Apollo LM ranges or constants.
2. Identify the minimum additional source-backed inputs needed for a descent dynamics profile (mass properties, thrust/throttle behavior, lunar gravity/frame assumptions, guidance-command boundary).
3. Use D-022 where a fully sourced range can be shown irrelevant at controller-product resolution.
4. Keep any fitted Apollo 11 final-descent trajectory explicitly labeled `RECONSTRUCTED`, separate from the authoritative causal state.

## Evidence status

- **DOCUMENTED:** DPS is throttleable/gimbaled and coupled to guidance/navigation.
- **DOCUMENTED:** ground guidance monitoring used independent tracking and onboard-system comparisons through descent.
- **DOCUMENTED:** P63/P64/P65/P66 define distinct guidance/control behavior.
- **PARTIALLY DOCUMENTED:** enough physics/semantics exist to build the next reusable causal layer.
- **UNRESOLVED:** exact continuous Apollo 11 as-flown state history from primary sources alone.
