# Research note 148 — Apollo 13 PC+2 postflight mass-reconstruction semantics

Date: 2026-09-14

## Question

What exactly does the `95,424.0 lb` PC+2/transearth-injection ignition weight in the September 1970 *Apollo 13 Mission Report* represent, and how should it be related to the final P30 module-weight sum (`95,932 lb`)?

## Primary source

NASA Manned Spacecraft Center, *Apollo 13 Mission Report*, September 1970, `MSC-02680`, Appendix A §A.5, **Mass Properties**, Table A-I.

NTRS citation: https://ntrs.nasa.gov/citations/19710003598

NTRS scan: https://ntrs.nasa.gov/api/citations/19710003598/downloads/19710003598.pdf

## Finding

The prose immediately preceding Table A-I defines the table's provenance. It states that the spacecraft mass properties represent conditions **determined from postflight analyses of expendable loadings and usage during the flight**. It further says that expendables usage is based on reported real-time and postflight data; individual CSM and LM stage weights/CG were measured before flight, inertia values were calculated, and changes after weighing were monitored so spacecraft mass properties could be updated.

Therefore the Table A-I PC+2/transearth-injection value of **`95,424.0 lb` at ignition** is an official **postflight reconstructed event mass-property product**. It is not evidence that `95,424.0 lb` was the mass value loaded into RTCC or used by Flight Dynamics before the maneuver.

Table A-I also explicitly marks the post-accident maneuver mass properties with footnote `b`: they are referenced to the **lunar-module coordinate system**, because the LM provided spacecraft dynamic control during these phases. This reinforces that the table is a full event-indexed mass-properties reconstruction (weight, CG, moments/products of inertia), not merely a transcription of a P30 pad weight field.

## Consequence for the 508-lb difference

The final transmitted P30 pad carried `62,480 lb` CSM and `33,452 lb` LM, totaling `95,932 lb`. The mission report's reconstructed PC+2 ignition weight is `95,424.0 lb`, a difference of `508.0 lb`.

Research note 147 established the numerical difference. This note establishes a stronger provenance boundary: the two values come from **different historical product classes**:

1. the P30 values are preburn operational maneuver-pad module weights transmitted to the crew;
2. `95,424.0 lb` is a postflight reconstructed total event mass embedded in a weight/CG/inertia table.

The difference therefore must not be treated as a contradiction requiring normalization. Nor may it be assigned to consumables, venting, epoch propagation, bookkeeping, rounding, or a particular RTCC deck without direct evidence.

## Simulation implication

Represent at least two distinct mass-product layers:

- `operational_targeting_mass_basis`: provenance-bearing module weights available to the maneuver-targeting/pad workflow;
- `postflight_reconstructed_mass_properties`: event-indexed reconstructed weight/CG/inertia used as a historical validation reference.

The second may validate the simulated physical/event state after reconstruction, but must not silently overwrite the first or be injected retroactively into the historical controller workflow.

## What remains unresolved

- exact `T+55` reference-epoch semantics;
- whether the accepted ~59-hour Flight Dynamics trim explicitly used the `T+55` deck;
- exact H-2 RTCC mass-property deck fields and depletion accounting;
- how the operational `62,480 / 33,452 lb` P30 values were generated;
- the specific accounting causes of the 508-lb difference;
- which mass value(s) were used internally by the final PC+2 targeting solution.

## Next archival target

Prioritize H-2 RTCC/Flight Dynamics maneuver worksheets, mass-property deck listings, processor descriptions, or controller support records that expose the operational module/depletion accounting behind the P30 weights. The postflight `95,424.0 lb` value is now sufficiently classified; the unresolved problem is the lineage and accounting of the **operational** mass basis.