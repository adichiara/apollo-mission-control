# Progress — Apollo 11 landing-radar beam transform

Date: 2026-09-19

## Completed

The source-controlled landing-radar geometry now has an executable equation-level transform. LUMINARY 099 controls `SETPOS`, measurement-time CDU use, Y-Z-X trigonometric order, and `*NBSM*`/`AX*SR*T` direction. The predecessor MIT `Sunburst37` listing retains the explicit `SMNB`, `NBSM`, and `AXISROT` implementation and therefore supplies a direct sign/sequence oracle rather than requiring a named modern Euler convention.

Added `landing_radar_transform.py` with:

- SM→NB Y→Z→X transformation;
- NB→SM inverse X→Z→Y transformation;
- Memo-95 beta-then-alpha antenna→NB transformation;
- `SETPOS`-style velocity-beam construction from antenna X/Y basis vectors and cross product.

Added a separately coded literal `AXISROT` oracle in unit tests. Nontrivial-angle cases agree with the production port; zero-angle identity, inverse round trips, basis-vector norm preservation, and beam orthonormality are also checked.

## Boundary retained

This is numerical equivalence to the source equations in ordinary floating point. It does **not** claim bit-for-bit equivalence to AGC one's-complement/fixed-point rounding. No unsupported radar noise, terrain, gravity, PIPA, telemetry, or controller-display behavior is introduced.

Historical stochastic landing-radar measurement generation remains BLOCKED. Controller-facing products remain separate.

## Next

Compose the now-executable position-specific antenna→NB beam construction and measurement-time NB→SM transform into `landing_radar_velocity_chain.py`, using historical LM-5 loads/CDUs as explicit controlled inputs. Preserve optional AGC-machine-level comparison as validation hardening rather than silently claiming it.

## Evidence status

- **DOCUMENTED / IMPLEMENTED:** static antenna→NB and dynamic SM/NB equation-level transforms.
- **VERIFIED:** independent literal-`AXISROT` floating-point fixture plus identity/inverse/basis invariants.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point equivalence.
- **BLOCKED:** historical stochastic LR measurement generation.
- **UNRESOLVED:** controller-visible product timing and formatting.