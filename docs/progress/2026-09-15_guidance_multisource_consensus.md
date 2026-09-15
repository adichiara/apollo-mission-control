# Progress — multi-source guidance consensus

Date: 2026-09-15

## Completed

- Recovered the useful model work from superseded PR #56 onto current `main`.
- Added mission-neutral multi-source guidance consensus analysis.
- Added caller-defined fields, tolerances, freshness, and quorum.
- Added all-pairs consensus groups so non-transitive pairwise agreement is not misclassified as full consensus.
- Added explicit consensus, ambiguous, no-consensus, and indeterminate states.
- Sources outside a unique consensus are reported without being classified as failed.
- Added synthetic tests.
- Added research note 210 for the Apollo 11 three-source/two-out-of-three monitoring topology.
- Added an explicit Apollo 11 `guidance_monitoring` readiness domain and scenario requirement.

## Historical boundary

The existing Apollo 11 pairwise monitoring profile remains non-executable because observation freshness/update cadence is unresolved. The new consensus model does not invent that timing and does not promote the documented 35-ft/s PDI example to a universal redline.

## Consequence

The architecture can now represent both:

`pairwise residual checks`

and

`multi-source agreement topology`

without assigning hidden truth or a failure diagnosis.
