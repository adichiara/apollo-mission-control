# 090 — Live-device / human-play validation boundary

Date: 2026-09-12  
Status: **RESEARCHED — validation protocol defined; physical multi-device execution still pending**

## Question

How should the first real-device/human play validation be structured so it exercises the project as an integrated Mission Control environment without inventing Apollo-era procedures or mistaking modern web/mobile mechanics for historical behavior?

## Primary-source findings

### Apollo mission simulator integrated mode

The 1965 Apollo mission-simulator paper by F. O. Martikan and S. H. Nassiff describes an integrated operating mode linking the Apollo mission simulator with the Mission Control Center for combined training of flight and ground crews.

Source: AIAA Paper 65-266, NTRS records 19650039405 / 19660033487.

Project implication: the validation target should be the *integrated operational system* — several station roles, crew interface, and simulation control acting against one scenario — rather than isolated screen inspection.

### Flight-control decisionmaking simulation

Harold G. Miller's NASA SP-209 paper, *Simulation Training for Flight Control Decisionmaking* (1970), describes simulation in a mission environment as the final readiness training for Mercury/Gemini/Apollo flight controllers and emphasizes decisionmaking, controller interfaces, procedure use, and readiness under adverse conditions.

Source: NASA SP-209, NTRS 19700013438.

Project implication: the first human validation should explicitly observe whether players can acquire information, coordinate, make station-appropriate decisions, and pass decisions/communications through the modeled authority chain under continuous mission time.

### Apollo training integration

NASA's Apollo training history records the tie-in between mission simulators and the Mission Control Center as a major step in realistically training crews and ground controllers together.

Source: NTRS 19720005243.

Project implication: testing one browser at a time is insufficient evidence for the current first-playable success criterion.

## What the sources do **not** establish

They do not establish:

- mobile-phone layout requirements;
- browser reload/rejoin behavior;
- HTTP latency thresholds;
- facilitator tokens or browser storage;
- a historical Apollo usability questionnaire;
- exact modern pass/fail timing limits for UI interaction;
- an Apollo-era equivalent of the project's `/admin` page.

Those are modern prototype-validation concerns and must remain labeled as such.

## Derived validation boundary

The first live validation should be a structured mission rehearsal, not an open-ended usability session.

Minimum configuration:

- one facilitator using the separate admin surface;
- separate human players for FLIGHT, CONTROL, CAPCOM, and GUIDO;
- additional implemented stations when enough players/devices are available;
- one authoritative server/session;
- real phones/browsers on the actual intended network path.

The run should preserve the normal project rules:

1. mission GET runs continuously except for an explicit facilitator pause;
2. station players use only their own operational surfaces;
3. facilitator functions remain outside all player stations;
4. no verbal out-of-band coaching supplies information a station should not possess;
5. FLIGHT decisions and CAPCOM transmissions remain explicit human actions;
6. missed prerequisites remain missed rather than being silently replayed;
7. historical/procedural defects and modern UI/network defects are logged separately.

## Validation observations

The session should capture four distinct classes of evidence.

### A. Technical/session integrity

- all clients show one coherent GET;
- pause/resume affects every client coherently;
- reload/rejoin restores the same station identity;
- occupied-station protection still works;
- no player acquires facilitator authority;
- no station receives another station's private operational collections.

### B. Player presentation/usability

- information is readable on a phone without desktop assumptions;
- players can locate the next relevant action while GET continues;
- important state changes are noticed without requiring page reloads or facilitator narration;
- controls are not so dense or ambiguous that normal mission decisions become UI puzzles.

These are prototype usability criteria, not historical Apollo console claims.

### C. Mission-control workflow

- subsystem stations can form readiness judgments from their own products;
- FLIGHT can obtain/understand readiness status and make the modeled GO/NO-GO decision;
- CAPCOM can distinguish queued/approved material and deliberately transmit it;
- station-to-station dependency becomes visible through modeled information flow rather than hidden state leakage.

### D. Historical/research gaps exposed by play

Record a research gap only when play reveals that a station lacks information, procedure, authority, or terminology actually required to make the modeled decision.

Do not convert mere player uncertainty into a historical fact request automatically. First classify whether the issue is:

- missing historical information;
- missing project instruction/training;
- poor UI presentation;
- missing simulation behavior;
- normal decision uncertainty.

## Nominal first run

Use the nominal PC+2 scenario first. The purpose is to verify that the core coordination path is playable before adding a nonnominal injection.

Recommended run sequence:

1. join stations and verify identity/isolation;
2. begin/rejoin the running PC+2 session;
3. observe continuous GET through normal preparation;
4. collect station readiness without facilitator coaching;
5. execute the FLIGHT decision and FLIGHT→CAPCOM handoff;
6. complete the nominal burn/post-burn path;
7. capture defects and research gaps immediately after the run.

The already-implemented synthetic ΔP branch should be a second run after nominal play is coherent.

## Pass criterion for this boundary

The live-device boundary is closed only when an actual multi-device human session demonstrates that:

- station identity/rejoin and authority separation survive real browser use;
- continuous mission time remains coherent enough for play;
- players can complete the nominal PC+2 coordination path without hidden facilitator guidance;
- station information boundaries remain intact;
- any blocking usability defects are either repaired or explicitly documented;
- any newly claimed historical behavior is separately sourced before implementation.

## Next implementation step

Create and use a concrete playtest checklist/report template based on this boundary. Physical execution remains necessary; automated tests cannot substitute for the device/readability/human-coordination portion.
