# Progress — post-free-return PC+2 GDA instruction

Date: 2026-09-16
Research note: `resources/research/188_post_flyby_pc2_gda_instruction_semantics.md`

## Completed

- Rechecked the post-61:29 `5.85 / 6.74` event against the primary NASA Apollo 13 mission commentary / air-to-ground transcript.
- Recovered the clearer speaker-attributed wording: CAPCOM issues a new PC+2 P30 maneuver pad, says the GDA `ought to be okay as it is from the last burn`, and specifies pitch `5.85`, roll `6.74`.
- Corrected the earlier repository interpretation that treated this as a crew-qualified `hopefully` readback with a `Yaw` transcription caveat.
- Reclassified `5.85 / 6.74` as a **ground-issued PC+2 desired/reference pair with an explicit no-action disposition**, not telemetry and not a demonstrated new RTCC computation.
- Updated research note 169, the GDA source catalog, current roadmap, and CONTROL station status to keep the repository internally consistent.

## Evidence boundary

The primary transcript does not identify the calculation that generated `5.85 / 6.74`, a job/run identity, mass-properties inputs, or a comparison threshold. The `0.01°` per-axis difference from the earlier `5.86 / 6.75` pair remains numerically interesting but cannot be promoted into a decision rule.

## Next unresolved item

Continue targeting the T+55 LM-burn mass-properties deck -> RTCC/RTACF run/request/output -> Flight Dynamics trim lineage, especially CONTROL's competing numerical trim and the actual comparison/acceptance basis.