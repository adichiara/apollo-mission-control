# Station/status update — live deployed integration validation

Date: 2026-09-14  
Status: **FACILITATOR-DRIVEN LIVE INTEGRATION PASS; MULTI-HUMAN PLAY PENDING**

## Closed validation boundary

The deployed browser application has now completed both of the first-playable software/integration paths under facilitator control:

- nominal Apollo 13 PC+2 progression through the immediate post-burn assessment, LM power-down transition, and PTC-preparation boundary;
- the source-bounded synthetic DPS fuel/oxidizer ΔP contingency through CONTROL `corroborated` shutdown evidence.

The successful ΔP chain was observed end to end:

`synthetic source observation → CONTROL rule/callout → CAPCOM queue → CAPCOM transmission → crew receipt → crew shutdown command → physical DPS response → crew shutdown report → fresh ground chamber-pressure observation → CONTROL evidence assessment`

CONTROL received only controller-observable evidence. The final evidence object did not expose hidden authoritative engine state. The deliberately high synthetic post-command chamber-pressure sample remained evidence-by-freshness rather than being interpreted as a binary engine-off threshold.

## Validation-interface defects found and corrected

Live testing exposed and closed several test/facilitator-interface defects before the PASS claim:

- facilitator token continuity across admin/test screens;
- CAPCOM shutdown-item recovery after screen switching/reload;
- guided contingency setup incorrectly pausing a session even though controller/crew commands require RUNNING state;
- missing post-command chamber-pressure observation in the guided evidence check.

Repeated CONTROL/CAPCOM actions observed during troubleshooting are not by themselves treated as product defects; reproducibility is required before opening a defect.

## Station implications

No station authority, historical rule, scenario timing, or player-information boundary was changed by the final validation fixes.

The live run supports the current station architecture:

- CONTROL can detect and act on the modeled ΔP criterion without hidden state;
- CAPCOM transmission remains separate from crew receipt/compliance;
- crew command remains separate from physical vehicle response;
- physical response does not fabricate controller telemetry evidence;
- fresh ground evidence plus crew report can corroborate shutdown for CONTROL without exposing simulator truth.

## Remaining validation sequence

Multi-human station play remains unvalidated, but it is **not the next project stage**.

Before player-interface/human validation, the project will continue through the facilitator/test harness to establish:

- simulation-controlled crew responses to CAPCOM rather than a crew player role;
- causal subsystem behavior in which commands, omissions, and mistakes change authoritative state;
- numerical propulsion/attitude/trajectory consequences for arbitrary supported burn inputs;
- electrical-power and consumables consequences;
- derived instrumentation/telemetry/ground products from those states;
- deterministic tests of correct, late, omitted, and incorrect actions without pre-authored outcome branches.

After that engine boundary is mature, the separate-device station tests documented elsewhere can resume. Until then, no seven-seat or five-player compact **multi-human** PASS claim is made.

See also:

- `docs/progress/2026-09-14_live_nominal_and_delta_p_validation.md`
- `docs/ROADMAP.md`
- `docs/roadmap/2026-09-12_first_playable_integration.md`
- `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md`
