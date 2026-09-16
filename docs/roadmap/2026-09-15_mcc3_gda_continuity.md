# PC+2 controller-record roadmap — GDA state continuity

Date: 2026-09-15  
Latest research note: `resources/research/179_preburn_gda_checkout_acceptance_bound.md`

## Roadmap refinement

The historical chain separates numerical/state layers that must not be collapsed:

1. **~59 GET provisional Flight Dynamics PC+2 abort-pad trim:** `5.86° / 6.75°`. Flight Dynamics says LM CONTROL challenged the passed trim using premission mass properties, then agreed with Flight Dynamics' data.
2. **61:29 free-return DPS commanded trim:** the same `5.86° / 6.75°` pair.
3. **61:11 preburn gimbal checkout:** CONTROL directs the gimbal-trim procedure, reports `Trim looks okay`, and when FLIGHT asks how close it is answers `within about 0.3` / `plenty close`. This is now classified as an operational spacecraft-checkout acceptance statement, not a ground-computation comparison criterion.
4. **Post-61:29 intended/retained PC+2 reference:** `5.85 / 6.74`, read back with "GDA should be okay as is" and qualified by "hopefully." This is not measured actuator telemetry.
5. **Immediately pre-PC+2 execution-state roll:** approximately `-0.8°`, derived from CONTROL's approximate ignition-motion report.

The strengthened continuity chain is:

`~59 provisional PC+2 5.86 / 6.75 -> same pair commanded for 61:29 free-return DPS burn -> preburn gimbal checkout within ~0.3 judged plenty close -> 40% powered-flight compliance -> exact resulting GDA state unrecovered -> CONTROL expects resulting state optimum for PC+2 -> later 5.85 / 6.74 "okay as is" reference -> no new PC+2 Noun 48 trim load`.

RTCC mass-property provenance remains source-backed only in discrete operations: T-6 generated/loaded; T+25 run with P/Y comparison; T+55 RTCC LM-burn decks updated. Direct T+55 consumption by the `5.86 / 6.75` solution remains unproven.

Note 179 adds a useful simulator distinction: **computation acceptance** and **spacecraft checkout acceptance** are separate gates. The recovered `~0.3°` statement belongs only to the latter. It must not be used to fill the unresolved Flight Dynamics-versus-CONTROL comparison rule.

## Highest-priority unresolved artifact

Search Apollo 13 archival/controller material specifically for the real-time mass-properties/trim data-lineage chain behind the ~59 GET disagreement:

1. T+55 weight/c.g. table or equivalent real-time mass-properties computation output;
2. explicit T+55 generation/load record or downstream run/request/output;
3. RTACF/RTCC LM-burn trajectory-processor trim output or associated request/job sheet;
4. LM CONTROL's alternative numerical trim from its premission-mass-properties calculation;
5. comparison delta and **ground-computation PC+2-specific acceptance/decision criterion**;
6. calculation time and job/run/request identity;
7. explicit linkage from the T+55 RTCC LM-burn deck to the Flight Dynamics `5.86 / 6.75` solution;
8. telemetry or controller working-sheet evidence for the exact post-61:29 complied two-axis GDA state;
9. the calculation/state record, if any, explaining the later `5.85 / 6.74` reference readback.

Do not infer that `deck updated` means `generated`, `loaded`, or `run`; that the exact post-compliance state was `5.86 / 6.75`; that `5.85 / 6.74` was measured telemetry; that T+25 `0.01°` or preburn-checkout `~0.3°` establishes a PC+2 computational criterion; or that T+55 directly generated either numerical pair.