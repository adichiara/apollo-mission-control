# Independent Guidance Cross-Check Model Proof

Status: **implemented reusable comparison model; mission-specific tolerances unresolved**

## Purpose

Compare two independently produced guidance observations without treating either one as authoritative hidden truth.

The generic chain is:

`source A observation + source B observation + caller tolerances/freshness -> agreement / disagreement / indeterminate`

Implementation:

`src/apollo_mission_control/guidance_crosscheck.py`

## Inputs

Each observation supplies:

- source identity;
- observation time;
- validity;
- named numerical fields;
- provenance.

The comparison configuration supplies:

- fields to compare;
- per-field absolute tolerances;
- maximum time separation;
- applicability/provenance.

## Outputs

- whether the observations are comparable;
- agreement true/false when comparable;
- per-field signed/absolute difference;
- tolerance result;
- reasons for indeterminate comparison.

## Critical boundary

The model does not decide which source is correct.

It does not turn agreement into GO, disagreement into abort, or substitute for a controller judgment/rule.

## Apollo applicability

This abstraction is useful for:

- Apollo 11 PGNS/AGS cross-check during powered descent;
- Apollo 13 PGNS/AGS guidance cross-checks;
- later scenarios with independent navigation/guidance sources.

Mission-specific fields, tolerances, freshness windows, and presentation paths remain caller/profile data and require historical sourcing.

## Validation

Synthetic tests cover agreement, disagreement, invalid/stale inputs, missing fields, and configuration validation.
