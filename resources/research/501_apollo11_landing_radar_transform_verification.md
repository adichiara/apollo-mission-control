# Research 501 — Apollo 11 landing-radar transform verification

Date: 2026-09-19
Thread: `apollo11-landing-radar` (500–599)

## Question

Can the remaining `SETPOS` antenna→navigation-base and measurement-time navigation-base→stable-member transform be ported without choosing an unsupported modern Euler convention?

## Primary-source result

The answer is now narrower than the previous documentation implied, but a numerical port is not yet justified solely by prose conventions.

The flown LUMINARY 099 listing establishes the operational contract directly:

- `SETPOS` places `LRBETA` at the Y-angle slot, zero at Z, and `LRALPHA` at X, then calls `TRG*SMNB` on antenna `UNITY` and `*SMNB*` on `UNITX`; `VZBEAMNB` is formed by cross product.
- `POWERED_FLIGHT_SUBROUTINES.agc` states that `AX*SR*T` expects sine/cosine inputs in **Y-Z-X** order, enters with `-3` for SM→NB and `+3` for NB→SM, and that `*NBSM*` reuses the already-computed trigonometric values.
- `VELUPDAT` uses the measurement-time CDU snapshot before the selected NB beam is transformed into stable-member coordinates.

LUMINARY Memo #95 independently fixes the landing-radar static-angle interpretation: `LRALPHA/LRBETA` are antenna→navigation-base rotations, applied beta then alpha, and have the opposite sign from the R-567 navigation-base→antenna angles.

A second primary software lineage provides an independent algorithmic cross-check rather than a modern convention. The earlier MIT Apollo `Sunburst37` `SMNB`/`NBSM` implementation explicitly performs the same gimbal transform as three successive axis rotations: SM→NB rotates about Y, then Z, then X; NB→SM reverses that sequence (X, Z, Y). Its `AXISROT` routine changes the arithmetic sense under `NBSMBIT`. This agrees with the LUMINARY 099 Y-Z-X angle ordering and inverse-direction contract.

The LUMINARY 099 `FLESHPOT` routine supplies a further in-program cross-check by constructing the body/stable-member transformation matrix directly from `SINCDU*`/`COSCDU*` terms.

## Implementation consequence

The rotation **order, direction, and source angle semantics are now independently controlled**. What remains before replacing the explicit beam input is numerical verification of a modern floating-point implementation against the AGC arithmetic/sign behavior (preferably known basis-vector cases from the original algorithm or a yaAGC/Virtual AGC oracle). That check matters because `AX*SR*T` is not merely a named modern Euler transform: it is a one’s-complement, scaled AGC routine with direction selected by the sign of its entry value.

Therefore this research step does **not** silently introduce a Python Euler library convention. It narrows the implementation gate to a reproducible numerical-equivalence test.

## Sources

- MIT/IL, LUMINARY 099 final-program listing, `SERVICER.agc`, pp. 895–897: https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- MIT/IL, LUMINARY 099 final-program listing, `POWERED_FLIGHT_SUBROUTINES.agc`, pp. 1259–1267: https://www.ibiblio.org/apollo/listings/Luminary099/POWERED_FLIGHT_SUBROUTINES.agc.html
- MIT/IL, LUMINARY Memo #95, *Landing Radar Orientation*, 9 July 1969: https://www.ibiblio.org/apollo/Documents/LUM95_text.pdf
- MIT Apollo software listing, `Sunburst37/INFLIGHT_ALIGNMENT_ROUTINES.agc`, pp. 325–328: https://www.ibiblio.org/apollo/listings/Sunburst37/INFLIGHT_ALIGNMENT_ROUTINES.agc.html

## Evidence status

- **DOCUMENTED:** Apollo-11-effective `SETPOS` angle placement, antenna-basis construction, and transform direction.
- **DOCUMENTED:** Apollo-11-effective `AX*SR*T` Y-Z-X input order and SM→NB / NB→SM entry-direction contract.
- **CORROBORATED:** independent predecessor `SMNB`/`NBSM` source expresses the same transform as Y→Z→X and inverse X→Z→Y axis-rotation sequences.
- **CORROBORATED:** LUMINARY 099 `FLESHPOT` independently constructs the corresponding CDU transformation matrix from the same sine/cosine state.
- **UNRESOLVED:** numerical-equivalence fixture proving a modern floating-point port against original AGC transform behavior.
- **BLOCKED:** historical stochastic landing-radar measurement generation remains blocked on flight-effective numerical error evidence.
- **UNRESOLVED:** controller-visible radar/guidance product cadence and formatting.