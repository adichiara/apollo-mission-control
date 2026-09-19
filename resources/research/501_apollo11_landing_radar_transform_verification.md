# Research 501 — Apollo 11 landing-radar transform verification

Date: 2026-09-19
Research thread: `apollo11-landing-radar`

## Question

Can the remaining `SETPOS` antenna→navigation-base and measurement-time navigation-base→stable-member transform be ported without choosing an unsupported modern Euler convention?

## Primary-source result

The flown LUMINARY 099 listing establishes the operational contract directly: `SETPOS` places `LRBETA` at Y, zero at Z, and `LRALPHA` at X before `TRG*SMNB`; `AX*SR*T` consumes sine/cosine state in Y-Z-X order and selects SM→NB with `-3` versus NB→SM with `+3`; `VELUPDAT` applies the measurement-time CDU snapshot before transforming the selected NB beam.

LUMINARY Memo #95 independently fixes the static-angle interpretation: `LRALPHA/LRBETA` are antenna→navigation-base rotations, beta then alpha, opposite in sign to the R-567 navigation-base→antenna angles.

A second primary software lineage provides an independent algorithmic cross-check. MIT `Sunburst37` `SMNB` performs three successive axis rotations Y→Z→X; `NBSM` reverses them X→Z→Y, with `AXISROT` changing arithmetic sense under `NBSMBIT`. LUMINARY 099 `FLESHPOT` supplies a further in-program cross-check by constructing the body/stable-member transformation matrix directly from `SINCDU*`/`COSCDU*` terms.

## Implementation consequence

Rotation order, direction, and source-angle semantics are independently controlled. Before replacing the explicit beam input, a modern floating-point port still needs numerical verification against original AGC arithmetic/sign behavior, preferably basis-vector cases from the original algorithm or a yaAGC/Virtual AGC oracle. This avoids silently substituting a library Euler convention for the one’s-complement/scaled AGC routine.

## Sources

- MIT/IL LUMINARY 099 `SERVICER.agc`, pp. 895–897: https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- MIT/IL LUMINARY 099 `POWERED_FLIGHT_SUBROUTINES.agc`, pp. 1259–1267: https://www.ibiblio.org/apollo/listings/Luminary099/POWERED_FLIGHT_SUBROUTINES.agc.html
- LUMINARY Memo #95, *Landing Radar Orientation*, 9 July 1969: https://www.ibiblio.org/apollo/Documents/LUM95_text.pdf
- MIT Apollo `Sunburst37/INFLIGHT_ALIGNMENT_ROUTINES.agc`, pp. 325–328: https://www.ibiblio.org/apollo/listings/Sunburst37/INFLIGHT_ALIGNMENT_ROUTINES.agc.html

## Evidence status

- **DOCUMENTED:** Apollo-11-effective `SETPOS` angle placement, antenna-basis construction, Y-Z-X input order, and SM→NB / NB→SM direction contract.
- **CORROBORATED:** predecessor primary `SMNB`/`NBSM` source gives Y→Z→X and inverse X→Z→Y sequences.
- **CORROBORATED:** LUMINARY 099 `FLESHPOT` constructs the corresponding CDU matrix from the same trig state.
- **UNRESOLVED:** numerical-equivalence fixture for a modern floating-point port.
- **BLOCKED:** historical stochastic landing-radar measurement generation remains blocked on flight-effective numerical error evidence.
- **UNRESOLVED:** controller-visible radar/guidance product cadence and formatting.