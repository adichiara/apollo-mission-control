# Multi-Source Guidance Consensus Model Proof

Status: **implemented reusable evidence model; mission-specific redlines unresolved**

## Purpose

Extend pairwise guidance comparison to the multi-source monitoring pattern used in Apollo Mission Control.

Generic chain:

`independent observations + caller redlines/freshness/quorum -> agreement topology`

The implementation does not choose a physical truth source and does not declare a disagreeing source failed.

## Model behavior

For each caller-selected field, the model:

- excludes invalid or missing observations from that field's eligible set;
- evaluates pairwise value agreement and observation-time compatibility;
- finds the largest group in which every pair agrees;
- requires a caller-selected quorum;
- reports a unique consensus, ambiguous equal-size groups, no consensus, or indeterminate state;
- reports sources outside a unique consensus without assigning a failure diagnosis.

The all-pairs requirement prevents a non-transitive chain from being mistaken for a true three-way consensus.

## Apollo 11 source pressure

MSC Internal Note 70-FM-80, *Lunar Descent and Ascent Trajectories*, describes Apollo 11 powered-descent monitoring as continuous comparison of LM velocity components from:

- PGNCS;
- AGS;
- MSFN ground tracking.

It explicitly describes two-out-of-three voting logic and premission velocity-residual redlines.

The same source records an 18 ft/s PGNCS/MSFN radial difference at PDI against a 35 ft/s limit and explains that the difference reflected an initialization/downrange-position effect rather than a guidance-system performance problem.

That evidence is why this model returns **outside consensus** rather than **failed**.

## Historical-use gate

Apollo 11 implementation still requires source-backed:

- exact compared velocity-component definitions;
- redlines by phase/source pair;
- update cadence/freshness;
- MSFN powered-flight-processor behavior;
- controller display/presentation;
- decision procedures for acting on a persistent discrepancy.

No Apollo 11 redline is embedded in the generic implementation.
