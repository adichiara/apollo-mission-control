# Research note 210 — Apollo 11 three-source guidance-monitoring boundary

Date: 2026-09-15

## Question

Does Apollo 11 powered-descent guidance monitoring require a reusable multi-source consensus model beyond the already implemented pairwise comparison layer?

## Primary evidence

NASA MSC Internal Note 70-FM-80 / MSC-02419, Floyd V. Bennett, *Project Apollo: Lunar Descent and Ascent Trajectories*, 21 April 1970, describes real-time Apollo 11 powered-descent monitoring using three independently produced LM velocity sources:

1. PGNCS;
2. AGS;
3. MSFN powered-flight ground computation.

The note describes a **two-out-of-three voting comparison** used to determine whether PGNCS or AGS performance was degrading. It also states that velocity-residual redlines were established premission.

The same source records an Apollo 11 radial PGNCS/MSFN difference of 18 ft/s at PDI against a 35 ft/s limit. The discrepancy persisted into powered descent but was interpreted as an initialization/downrange-position effect rather than evidence of guidance-system degradation.

## Relationship to research note 204

Research note 204 and the existing historical guidance-monitoring profile source several specific pairwise Apollo 11 comparison limits from MSC Internal Note 70-FM-20 and the mission rules.

This note adds a different architectural fact: **the operational monitoring topology was multi-source and two-out-of-three**, not merely a collection of unrelated pairwise checks.

The two findings are complementary:

`pairwise source-specific residual limits + three-source voting topology`

## Architecture consequence

The reusable engine needs a mission-neutral layer that can:

- accept multiple independently produced observations;
- apply caller-supplied fields, tolerances, freshness limits, and quorum;
- identify mutually agreeing source groups;
- distinguish a unique consensus from ambiguous or no-consensus states;
- report a source outside consensus without labeling that source failed;
- avoid selecting hidden truth or issuing a GO/NO-GO / abort decision.

A generic multi-source consensus model can implement this relationship without embedding Apollo 11 thresholds.

## Historical boundary

Do not promote the documented 35 ft/s PDI example to a universal redline.

Apollo 11 runtime use still requires source-backed timing/freshness, exact phase/source-pair applicability, controller presentation, MSFN powered-flight processing, and the operational decision rules that acted on persistent disagreement.

The existing pairwise historical profile remains non-executable because its observation freshness/cadence is unresolved. Adding the voting topology does not close that gate.

## Source

NASA Manned Spacecraft Center, MSC Internal Note 70-FM-80 / MSC-02419, Floyd V. Bennett, *Project Apollo: Lunar Descent and Ascent Trajectories*, 21 April 1970.
