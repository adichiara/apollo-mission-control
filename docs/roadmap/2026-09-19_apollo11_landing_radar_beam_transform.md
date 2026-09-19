# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-19
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective LUMINARY 099 controls `SETPOS`, Y-Z-X trigonometric preparation, and `*NBSM*`/`AX*SR*T` direction semantics. MIT `Sunburst37` preserves the predecessor `SMNB`/`NBSM`/`AXISROT` implementation: SM→NB rotates Y→Z→X; NB→SM applies the inverse X→Z→Y sequence. Its literal `AXISROT` arithmetic fixes the signs for each two-component rotation. Memo #95 fixes antenna→NB beta-then-alpha semantics.

## Completed in this step

Added a floating-point port plus a source-derived numerical-equivalence fixture. The fixture independently encodes the literal `AXISROT` branch equations and verifies the production transform for nontrivial angles, zero-angle identity, basis-vector norm preservation, inverse round trips, and orthonormal `SETPOS` velocity beams.

This closes the former modern-Euler-convention gate without claiming bit-for-bit AGC fixed-point equivalence. The implementation is an equation-level port of the historical transform, not an AGC arithmetic emulator.

## Revised next work

1. Compose LM-5 position-specific `SETPOS` beam construction and measurement-time NB→SM transformation into the historical landing-radar velocity chain, using the already recovered LM-5 alpha/beta loads and saved CDUs.
2. Preserve a separate optional yaAGC/AGC-fixed-point comparison as validation hardening if a later dependency requires machine-level rounding equivalence; it no longer blocks equation-level model composition.
3. Keep historical stochastic LR measurement generation BLOCKED until flight-effective numerical error evidence is recovered.
4. Keep spacecraft downlink, ground processing, and controller-visible cadence/formatting separate from onboard estimator behavior.

## Evidence status

- **DOCUMENTED / IMPLEMENTED:** source-derived SM→NB and NB→SM floating-point transform equations and sequence.
- **DOCUMENTED / IMPLEMENTED:** antenna→NB beta-then-alpha transform and orthonormal velocity-beam construction.
- **VERIFIED:** production transform agrees with a separately coded literal `AXISROT` oracle for nontrivial cases and inverse/basis invariants.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point rounding equivalence.
- **BLOCKED:** historical stochastic LR measurement generation.
- **UNRESOLVED:** controller-visible product timing/formatting.