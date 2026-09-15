# Multi-Source Guidance Consensus Model Proof

Status: **implemented reusable evidence model; Apollo 11 timing/freshness still unresolved**

## Purpose

Extend the existing pairwise guidance cross-check boundary to a multi-source monitoring topology.

Generic chain:

`independent observations + caller tolerances/freshness/quorum -> agreement topology`

Implementation:

`src/apollo_mission_control/guidance_voting.py`

The model does not choose a physical truth source, declare a disagreeing source failed, or make a mission decision.

## Model behavior

For each caller-selected field, the model:

- excludes invalid or missing observations from that field's eligible set;
- evaluates pairwise value agreement and observation-time compatibility;
- finds the largest group in which every pair agrees;
- requires a caller-selected quorum;
- reports unique consensus, ambiguous equal-size groups, no consensus, or indeterminate state;
- reports sources outside a unique consensus without assigning a failure diagnosis.

The all-pairs requirement prevents a non-transitive chain from being mistaken for a true three-way consensus.

## Apollo 11 source pressure

Research note 210 records MSC Internal Note 70-FM-80 evidence that Apollo 11 powered-descent controllers compared PGNCS, AGS, and MSFN-derived velocity using two-out-of-three monitoring logic.

Research note 204 separately records source-specific pairwise fields and several historical residual limits. Those historical values remain in the profile layer, not the generic model.

## Historical-use gate

Apollo 11 implementation still requires source-backed:

- observation timing/freshness;
- exact phase/source-pair applicability;
- MSFN powered-flight-processor behavior;
- controller display/presentation;
- decision procedures for persistent discrepancies.

No Apollo 11 redline or timing constant is embedded in this generic implementation.
