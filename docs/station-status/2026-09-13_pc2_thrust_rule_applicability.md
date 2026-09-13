# Station status — PC+2 77-percent thrust-rule applicability

Date: 2026-09-13

## CONTROL

Maturity remains **B**.

No new ground measurement is added. CONTROL's chamber-pressure criterion remains separate from the crew ENG THRUST indication. The new result only constrains when the crew-side percent-thrust criterion can meaningfully become active in the nominal PC+2 throttle profile.

## CAPCOM

Maturity remains **B**.

CAPCOM's historical rule read-up remains the source of the crew criterion. For first-playable sequencing, the rule is inactive during the commanded low-thrust startup segments and becomes applicable on entry to commanded maximum/full throttle.

## Crew boundary

The Apollo 13 Technical Crew Debriefing fixes the full-throttle transition at burn +26 seconds. This allows a source-bounded applicability state without inventing an arbitrary timer:

`12.6% startup -> 40% startup -> full/max thrust -> 77% ENG THRUST criterion applicable`

The final arrow is a documented lineage-based inference, not a verbatim recovered Apollo 13 mission-rule qualifier.

A crew-visible ENG THRUST observation is still required to evaluate the rule. No station receives hidden engine truth or a synthetic mirrored crew gauge.

## Status consequence

No station maturity grade changes. The archival applicability gap is sufficiently bounded for the first playable; physical human/device validation remains the blocking next step.
