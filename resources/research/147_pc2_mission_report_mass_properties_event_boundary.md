# Research note 147 — Apollo 13 PC+2 mission-report event mass-properties boundary

Date: 2026-09-14

## Question

Can a second mission-specific primary source independently bound the physical/event mass associated with PC+2, and does it support equating the final P30 PAD weights with exact ignition mass?

## Primary source

NASA Manned Spacecraft Center, *Apollo 13 Mission Report*, September 1970, MSC-02680 / NTRS 19710003598.

NTRS scan: https://ntrs.nasa.gov/api/citations/19710003598/downloads/19710003598.pdf

Appendix A, Table A-I, **Mass Properties**, gives event-indexed spacecraft mass properties. Relevant rows include:

- cryogenic oxygen-tank incident: `96,646.9 lb` before / `96,038.7 lb` after;
- second midcourse correction: `95,959.9 lb` ignition / `95,647.1 lb` cutoff;
- **transearth injection**: `95,424.0 lb` ignition / `87,456.0 lb` cutoff;
- third midcourse correction: `87,325.3 lb` ignition / `87,263.3 lb` cutoff;
- fourth midcourse correction: `87,132.1 lb` ignition / `87,101.8 lb` cutoff.

The same mission report identifies the major maneuver sequence in which the 61:29 DPS maneuver restored free return and the later PC+2 DPS maneuver at 79:27 accelerated the transearth return. In this post-accident sequence, the table's `transearth injection` event corresponds to the PC+2 return-acceleration maneuver.

## Finding

The mission report supplies an independent, mission-specific event mass for PC+2: **95,424.0 lb at transearth-injection ignition**.

This is **508.0 lb lower** than the final P30 PAD module-weight sum documented in research note 137:

`62,480 + 33,452 = 95,932 lb`

`95,932 - 95,424 = 508 lb`

The two primary products therefore must not be silently treated as numerically identical representations of spacecraft mass at PC+2 ignition.

This is a useful positive result rather than a discrepancy to be forced away. It confirms that the project needs separate fields for:

1. controller/targeting module weights carried on the final P30 PAD;
2. mission-report event mass properties at ignition/cutoff;
3. RTCC mass-properties deck/state and its reference epoch;
4. hidden physical/simulation mass state.

## Critical boundary

The table does not, by itself, explain the 508-lb difference. Do **not** attribute it to consumables, venting, LM/CSM bookkeeping, epoch propagation, rounding, a particular RTCC deck, or a transcription convention without a source that makes that accounting explicit.

Likewise, this finding does not prove that the mission-report `95,424.0 lb` value is the exact value used by RTCC for the final PC+2 targeting solution. It is an official postflight event-indexed mass-property value and is therefore a stronger physical/event-mass validation anchor than the PAD module-weight sum, but the computational lineage remains unresolved.

## Simulation implication

Use `95,424.0 lb` as the mission-report PC+2/TEI ignition event-mass regression datum and `87,456.0 lb` as the corresponding cutoff datum, with provenance identifying Appendix A Table A-I. Preserve `95,932 lb` separately as the final transmitted P30 PAD module-weight sum.

A numerical model should not be tuned by redefining either datum to equal the other. Reconciliation requires recovery of the H-2 RTCC mass-property/depletion bookkeeping or another primary source that explains the relationship.

## Next unresolved item

The highest-value target is now more specific: recover H-2 RTCC/Flight Dynamics mass-property documentation or maneuver worksheets that explain the accounting relationship between the `T+55` operational mass-properties state, the final P30 module weights (`62,480` / `33,452`), and the postflight PC+2/TEI ignition event mass (`95,424.0 lb`).