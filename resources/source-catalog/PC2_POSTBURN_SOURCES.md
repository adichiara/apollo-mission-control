# PC+2 Immediate Post-Burn Sources

Status: active source supplement for first-playable immediate post-burn verification/power-down.

## Primary sources

### Flight Control Division Mission Operations Report — Apollo 13, 28 April 1970

NASA Manned Spacecraft Center, *Mission Operations Report: Apollo 13*.

Relevant findings:
- PC+2 ignition occurred at 79:27:38.30 GET and the burn was nominal.
- PGNS residuals were recorded as R1 +00010, R2 +00003, R3 +00000.
- At 79+34, LM power-down began except for functions required for PTC.
- At 79+52, CAPCOM read a detailed PTC-establishment procedure.

Implementation use: establishes the immediate post-burn ordering, nominal residual product, and transition from burn configuration to power conservation/PTC preparation.

### Apollo 13 mission commentary / air-ground transcript, around 79:33 GET

NASA Apollo 13 PAO/air-ground transcript.

Relevant finding: CAPCOM began reading a procedure to substantially power down the LM, with additional reduction deferred until PTC was established.

Implementation use: confirms that post-burn power-down was a crew procedure communicated from the ground rather than an instantaneous hidden state change.

### Apollo 13 change-of-shift briefing after PC+2

NASA Apollo 13 change-of-shift briefing.

Relevant findings:
- controllers described an LM power-down timing of roughly cutoff +15 minutes after confirming a good post-burn spacecraft;
- guidance/navigation and communications stayed up to support PTC initiation;
- later tracking supplied additional trajectory-performance confirmation.

Provenance caution: the `cutoff +15 minutes` statement is not silently equated with the 79:33–79:34 initial power-down chronology in the Mission Operations Report/air-ground record. The present evidence does not establish whether the briefing refers to the same reduction or to a later/deeper stage. Research note 101 preserves this as an unresolved source tension.

Implementation use: constrains the operational rationale and prevents collapsing cutoff, verification, power-down, and PTC preparation into one event; it does **not** supply an additional exact simulation timestamp.

## First-playable rule

Model the immediate post-burn interval as an ordered transition:

`cutoff → post-burn assessment → release from burn configuration → partial power-down → PTC preparation`

Use the 79:33–79:34 chronology only as evidence for the observed initial transition. Do not invent an exact reconciliation with the separate cutoff+15 briefing statement, exact controller keying, an unsupported formal post-burn poll, exact switch-by-switch timing, or full PTC dynamics.
