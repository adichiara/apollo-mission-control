# Progress — Apollo 11 landing-radar beam transform

Date: 2026-09-19

## Completed

Recovered a primary-source chain sufficient to control both the static antenna-position and dynamic attitude/reference-frame portions of the Apollo 11 landing-radar velocity-beam geometry.

LUMINARY 099 `SETPOS` transforms antenna-frame basis vectors into navigation-base beam vectors. LUMINARY Memo #95 controls the sign/order convention, and the LM-5 Mission G LUMINARY 99 prelaunch load supplies the actual position-1 and position-2 alpha/beta values. The final-program constants also supply `HBEAMANT`.

The dynamic leg is explicit in the flown listing. `RDGIMS` stores measurement time, IMU CDU angles, and PIPAs; `VELUPDAT` restores the saved CDU values in Y-Z-X order, calls `QUICTRIG`, and applies `*NBSM*` to the selected `V?BEAMNB`.

Research 501 now independently constrains the transform convention. LUMINARY 099 says `AX*SR*T` consumes Y-Z-X sine/cosine state and selects SM→NB versus NB→SM by its signed entry value. The earlier primary MIT `Sunburst37` implementation independently expresses SM→NB as successive Y, Z, X axis rotations and NB→SM as the reverse X, Z, Y sequence; LUMINARY 099 `FLESHPOT` separately constructs the CDU transformation matrix from the same trigonometric state. This removes the need to infer rotation order from a modern Euler convention.

## Current implementation boundary

The repository already composes measurement-time propagation → explicit selected-beam projection → residual qualification → historical weighting/correction. The remaining beam-synthesis gate is now only a **numerical-equivalence fixture**: verify a floating-point port against original AGC transform behavior before replacing the explicit beam input. No Python/graphics-library Euler convention should be adopted merely because it appears equivalent by name.

Historical stochastic landing-radar measurement generation remains BLOCKED on flight-effective numerical error evidence. Controller-facing products remain a separate evidence problem.

## Next

Build a small source-derived transform oracle/fixture from the original `AXISROT`/`AX*SR*T` behavior (or yaAGC/Virtual AGC execution), test basis vectors and inverse round trips, then implement `SETPOS` + measurement-time `NBSM` only if those cases agree. Preserve AGC-vs-floating-point approximation provenance.

## Evidence status

- **DOCUMENTED:** static LM-5 antenna-position inputs and algorithm.
- **DOCUMENTED:** measurement-midpoint CDU/time capture and NB→SM velocity-beam transform contract.
- **CORROBORATED:** Y-Z-X / inverse X-Z-Y axis sequence from independent primary Apollo software lineage and LUMINARY 099 matrix construction.
- **UNRESOLVED:** numerical-equivalence fixture for the modern executable transform port.
- **BLOCKED:** historical stochastic LR measurement generation.
- **UNRESOLVED:** controller-visible product timing and formatting.