# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-19
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective evidence controls `SETPOS`, LM-5 alpha/beta loads, measurement-time CDU capture, Y-Z-X trigonometric preparation, and `*NBSM*`/`AX*SR*T` direction semantics. Research 501 adds an independent primary-software cross-check: the earlier MIT `Sunburst37` `SMNB`/`NBSM` routines perform SM→NB as Y→Z→X axis rotations and NB→SM in reverse X→Z→Y order. LUMINARY 099 `FLESHPOT` separately constructs the CDU transformation matrix from the same sine/cosine state.

This closes the former **convention** ambiguity. It does not yet justify substituting an arbitrary modern Euler implementation for AGC arithmetic.

## Revised next work

1. Build a reproducible numerical-equivalence fixture for the transform using original AGC behavior (source-derived `AXISROT` cases or yaAGC/Virtual AGC execution).
2. Verify basis vectors, both transform directions, inverse round trips, and the zero-angle identity case.
3. Only after equivalence is demonstrated, implement `SETPOS` antenna→NB plus measurement-time NB→SM beam synthesis and replace the composed proof's explicit beam input.
4. Keep historical stochastic LR measurement generation BLOCKED until flight-effective numerical error evidence is recovered.
5. Keep spacecraft downlink, ground processing, and controller-visible cadence/formatting separate from onboard estimator behavior.

## Evidence status

- **DOCUMENTED:** Apollo-11-effective static geometry, angle placement, Y-Z-X order, and transform-direction contract.
- **CORROBORATED:** transform axis sequence from independent primary Apollo software lineage and LUMINARY 099 matrix construction.
- **UNRESOLVED:** numerical equivalence of a modern floating-point port to original AGC behavior.
- **BLOCKED:** historical stochastic LR measurement generation.
- **UNRESOLVED:** controller-visible product timing/formatting.