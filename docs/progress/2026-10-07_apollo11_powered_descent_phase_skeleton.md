# Progress — Apollo 11 powered-descent phase skeleton

Date: 2026-10-07

## Completed

Converted the existing Apollo 11 powered-descent phase research into an executable, mission-profile-driven phase skeleton.

The implementation deliberately separates:

- **nominal planned phase anchors**, which drive the deterministic architecture state;
- **flown/postflight propulsion observations**, which are carried as evidence metadata but do not drive phase selection.

The nominal phase path is:

`PDI -> braking -> high gate/approach -> low gate/landing -> post-planned-touchdown`

The Apollo 11 profile uses the already controlled Flight Plan anchors at TFI 0, 504, 608, and 718 s.

The Mission Report's 756.3-s powered-descent duration, approximately 6,775 ft/s delta-V, 13-percent initial throttle, approximately +26-s full-throttle transition, and approximately 45-s early data loss remain separate flown observations.

## Guardrail demonstrated

At TFI 730 s the phase evaluator reports `post_planned_touchdown` because the nominal Flight Plan touchdown anchor is 718 s, while still returning the independent 756.3-s flown firing-duration observation.

This apparent mismatch is preserved intentionally. The model does not rewrite the nominal plan to match the flown duration and does not infer an exact flown touchdown time.

## Site-facing proof

The Causal Model Lab now exposes the phase skeleton and lets the facilitator jump to:

- high gate;
- low gate;
- after nominal planned touchdown.

The surface explicitly labels planned versus flown evidence.

## Next

Compose this nominal phase state with the already implemented Apollo 11 descent decision gate, controller-product schema, landing-radar chain, and program-alarm state into a bounded runtime projection.

That composition must continue to preserve human controller decisions and must not turn phase membership into an automatic landing/abort rule.
