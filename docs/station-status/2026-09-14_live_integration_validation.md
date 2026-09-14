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

## Remaining station/player validation

The next unclosed boundary is simultaneous human use of the actual player clients on separate devices. Required observations include:

- whether each station can find and interpret its information without facilitator explanation;
- FLIGHT/CAPCOM coordination in timed play;
- station information isolation;
- phone readability and action discoverability;
- reference-packet findability;
- five-player compact switching between TELMU↔CONTROL and GUIDO↔FIDO/RETRO;
- station-qualified readiness/action attribution under real use.

Until that is completed, no seven-seat or five-player compact **multi-human** PASS claim is made.

See also:

- `docs/progress/2026-09-14_live_nominal_and_delta_p_validation.md`
- `docs/ROADMAP.md`
- `docs/roadmap/2026-09-12_first_playable_integration.md`
- `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md`
