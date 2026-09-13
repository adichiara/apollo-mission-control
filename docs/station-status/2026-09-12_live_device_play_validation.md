# Station research status — live-device / human-play validation

Date: 2026-09-12

## Status

**PROTOCOL DEFINED — physical multi-device execution pending**

## Cross-station validation target

Primary Apollo/NASA simulation-training evidence supports validating the controller environment as an integrated mission rehearsal rather than as isolated station screens.

Minimum live configuration:

- FLIGHT;
- CONTROL;
- CAPCOM;
- GUIDO;
- facilitator/SimSup on the separate admin surface.

TELMU, FIDO/RETRO, and INCO should be added when enough players/devices are available.

## Station-specific observations required

### FLIGHT

- can understand aggregated readiness state;
- can make the modeled GO/NO-GO decision while GET continues;
- does not receive hidden facilitator/source truth.

### CONTROL

- can interpret its propulsion/control products and rule state;
- can initiate the modeled ΔP callout explicitly during the nonnominal run;
- receives fresh shutdown evidence without hidden `engine_running` truth.

### CAPCOM

- can distinguish queued/approved communication from already transmitted material;
- must deliberately transmit rather than having communication occur automatically;
- handoff from FLIGHT is understandable in actual play.

### GUIDO

- remains limited to its guidance/alignment/maneuver presentation;
- does not receive FLIGHT/CAPCOM operational collections.

### Facilitator

- remains outside every controller station;
- pause/resume and validation operations affect the shared session coherently;
- facilitator credentials/functions are not exposed through normal station clients.

## Human-play guardrails

- no out-of-band facilitator coaching may provide information the station should not possess;
- controller thinking time does not automatically pause GET;
- player confusion is classified before it becomes a research request;
- historical/procedural gaps, simulation defects, UI defects, network defects, and player-instruction gaps are logged separately.

## Remaining station-validation work

Execute `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md` on actual phones/browsers. Nominal PC+2 comes first; the synthetic ΔP branch follows only after normal station coordination is coherent.

No real-device PASS claim is recorded yet.

See research note 090 and `resources/source-catalog/LIVE_HUMAN_PLAY_VALIDATION_SOURCES.md`.
