# Station status — live-play reference packet

Date: 2026-09-13

The initial physical-play reference packet now preserves original-station identity and station-scoped information for all supported PC+2 players.

- **FLIGHT** — packet states readiness integration/final modeled GO-NO-GO authority and CAPCOM handoff; no private station evidence is exposed.
- **CAPCOM** — packet distinguishes queued/approved content, deliberate transmission, and crew receipt; no authority to invent technical content is added.
- **CONTROL** — packet carries the source-backed >25 psi fuel/oxidizer differential-pressure ground criterion while preserving ground/onboard evidence distinctions. The exact onboard 77-percent thrust indication and singular 150-psi ground inlet-pressure aggregation remain unresolved rather than simplified.
- **TELMU** — packet keeps TELMU responsibility separate from CONTROL and provides no CONTROL-private evidence.
- **GUIDO** — packet keeps guidance/attitude evidence separate and does not invent a new startup-transient timing gate.
- **FIDO/RETRO** — packet preserves the project’s existing first-slice flight-dynamics surface without claiming a historical combined station.
- **INCO** — packet preserves communications/data-path monitoring as distinct from CAPCOM crew voice authority.

Compact mode continues to provide separate original-station reference sheets for TELMU and CONTROL, and for GUIDO and FIDO/RETRO. `LM SYSTEMS` and `FLIGHT DYNAMICS` remain modern player-group labels only.

Station maturity ratings are unchanged. This work changes player-reference organization, not historical station reconstruction.