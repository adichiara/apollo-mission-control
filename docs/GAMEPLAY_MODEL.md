# Gameplay Model

Status: **design proposal — nothing here is accepted**

Purpose: define what a *session* of this simulation actually is — what a player does minute to minute, what makes it difficult, how many players it needs, how a run ends, and how anyone can tell it went well.

## How to read this document

Every research document in this repository describes what Apollo *was*. This one describes what the game *does*, which is a different kind of claim and must not be confused with the first. Three labels are used throughout:

- **DOCUMENTED** — an Apollo fact, with the research note it comes from. No new history is asserted in this file; if a claim is not traceable to an existing note, it is not labelled DOCUMENTED.
- **PROPOSED** — a design choice this document argues for. It is a project decision, not a historical finding, and belongs in `DECISIONS.md` only if accepted.
- **OPEN** — a decision that is genuinely the project's to make, where this document lays out the options rather than choosing.

## Where this sits relative to current work

D-013 has selected the first vertical slice: **Apollo 13 PC+2**, frozen at **77:55:00 GET** through post-burn power-down around 79:34–80:00 GET. `docs/scenarios/` defines its parameters, state machine (S0–S14), model dependencies, update semantics and minimum player-facing product set. Phase 4 has a working prototype with rule evaluation, scenario injection, ground-product integrity and controller product-rejection events.

This document does not revisit any of that. It addresses the gap the roadmap itself still marks open — Phase 2's remaining deliverable, *"full-fidelity player-position set and later low-player-count aggregation"*, plus the items D-013 lists as not yet decided: minimum player count, controller combinations by player count, time acceleration, and post-simulation evaluation format.

In several places the slice documents have already converged on positions this document argues for independently. Those are noted as **already consistent** rather than proposed, because the useful signal is the agreement, not the recommendation.

---

# 1. The central claim: Apollo supplies its own game structures

Principle 4 forbids scores, achievements, health meters, quest markers, unsolicited hints, colour-coded alerts, difficulty settings, and telling the player the correct decision. That is the right aesthetic, but it removes every conventional tool for goal communication, pacing, progress feedback and failure legibility. A design that simply deletes those functions produces an opaque, unpaced, unlearnable product.

The resolution is that Apollo operations already contained structures that do exactly this work, and the research in this repository has already found them. The game layer does not need inventing; it needs **identifying**.

| Conventional game device | Documented Apollo mechanism that replaces it | Source in this repo |
|---|---|---|
| Turn-taking / decision beats | Flight Director **GO/NO-GO poll** — every discipline states a position at a decision point | `APOLLO13_PC2_STATE_MACHINE.md` S4→S5; note 009 |
| Win/lose criteria | **Mission rules**, published in advance, mapped to positions | note 049 (PC+2 action and rule matrix); note 053 |
| Quest log / objective list | **Flight plan and mission elapsed time** | `APOLLO13_PC2_VERTICAL_SLICE.md` timeline |
| Alert system | **Limit-sense lights and event indicators**, controller-set, deliberately noisy | `stations/APOLLO13_EECOM.md` §6 |
| Tutorial | **Console handbook and checklists**, per position | note 008 |
| Difficulty setting | **Which case is run**, and its injection set | note 056 (scenario injection architecture) |
| Score | **Debrief** against mission rules and vehicle state | §7 below |
| Interaction verb | **Callout on a voice loop** | note 068 (ΔP ground-callout loop) |

The most important entry is the first. The GO/NO-GO poll is a complete co-operative game mechanic that arrives fully documented: it synchronises the group, forces commitment, creates the dramatic beat, distributes accountability, and makes one player's silence everyone's problem.

**Already consistent:** the PC+2 state machine puts the final poll at ~79:17 GET as the S4→S5 transition, and `APOLLO13_PC2_PLAYER_PRODUCTS.md` gives FLIGHT "controller readiness reports → integrate GO/NO-GO" while explicitly denying FLIGHT any "omniscient consolidated subsystem-health dashboard." The slice has independently arrived at the poll as the decision structure and at FLIGHT as an integrator rather than a monitor.

**PROPOSED:** make that explicit and general — cases are authored to *converge on polls*, and a poll is a first-class interface event with a recorded per-position response, not an informal conversation.

---

# 2. The unit of play is a case, not a mission

**DOCUMENTED:** Apollo integrated simulations were segmented by mission phase and were rarely long end-to-end runs (`SIMULATION_SCENARIO_RESEARCH.md` §1, note 011, note 008).

**Already consistent:** the first slice is a bounded interval with a frozen start and a clear climax, which is this shape.

**PROPOSED:** generalise it — the unit of play is a **case**: one phase, one defined start state, one end condition. This bounds session length, makes reset trivial (a case has explicit initial conditions), and is the historically correct shape rather than a concession.

## 2.1 The wall-clock problem

PC+2 spans 77:55 → ~80:00 GET, roughly two hours of mission time. The state machine's fourteen transitions are not evenly distributed across it: S0–S4 are preparation, and S6–S13 — ignition through residual review — occupy the four and a half minutes of the burn itself.

So the case has a structural pacing problem that is not a fidelity problem: most of the clock is preparation, and almost all of the drama is in four minutes. Options:

- **Real time throughout.** Most authentic. Roughly 90 minutes of preparation before a four-minute climax.
- **Compress S0–S4, real-time from S5.** The burn and its rule monitoring run at 1:1 where per-second judgment matters; preparation is accelerated between timeline events.
- **Start later.** Begin the session at S3 or S4 and accept losing the PAD/uplink/alignment work — which is much of what GUIDO, FIDO/RETRO and CAPCOM actually do here.

**PROPOSED:** the second. Time compression is permitted only between timeline events and never within a state where a documented rule is being monitored, so no player ever loses a decision to the clock. This keeps the burn honest and makes the session fit an evening.

**OPEN:** whether compression is FLIGHT's control, SimSup's, or a case property. D-013 lists time acceleration as undecided; this is the first case that forces the question.

## 2.2 Anatomy of a case

| Stage | What happens | Why it is there |
|---|---|---|
| **Brief** | Mission, phase, vehicle configuration, known open items | Controllers knew the mission plan. The game must not withhold the premise. |
| **Console setup** | Players take their paper, select displays, set what is theirs to set | See §2.3 |
| **Nominal ops** | Timeline work; establishing what normal looks like | Without a baseline an anomaly is meaningless noise. Not filler. |
| **Injection** | A physical or ground-processing condition changes. Nothing is announced. | note 011 §3; note 056 |
| **Recognition → diagnosis** | Someone notices; disciplines exchange data; indications may conflict | The core skill (§3) |
| **Decision** | Recommendation → poll → call | The dramatic beat |
| **Execution → verification** | Command or crew instruction, then *fresh* observation confirming it took | note 070: shutdown confirmation needs a fresh post-command observation, not an assumption |
| **Debrief** | Event timeline, applicable rules, historical comparison. No score. | §7 |

## 2.3 The high-agency opening decision

The strongest version of this in the corpus is EECOM's: **DOCUMENTED**, EECOM manually set the high and low limits driving the limit-sense lights, normally chose tight limits so small drifts were noticed early, and consequently several lights illuminated at once as a routine condition — panel 3 carried 72 lights, 12 of them cryogenic (`stations/APOLLO13_EECOM.md` §6). The Review Board could not establish whether the O2 tank 2 limit indication appeared ~30 seconds before the failure or appeared and was missed. The historical system permitted a correct signal to go unobserved.

That is a real tradeoff chosen by the player before anything goes wrong: tight limits give early warning at the cost of a panel you learn to ignore; loose limits give a clean panel and no warning. **PROPOSED** as a mechanic — with the corollary that the simulation never escalates an indication to ensure the player notices.

EECOM is not a first-slice station, so this lands with the accident scenario. **The PC+2-era equivalent already exists in code**: controller **product rejection** (notes 065, 066) — the player can judge a ground-derived product wrong and discard it, as Mission Control did when RTCC mis-processed AGS body angles and controllers fell back on the FDAI reference. Same shape of decision, same refusal to tell the player which reading to trust, and it is implemented today. For the first slice this is the mechanic to build the session around.

---

# 3. The player's loop and the skill ladder

The loop is: **scan → compare against expected → consult paper → form a position → say it out loud → live with the call.**

The ladder the game should reward:

1. **Locate** — find a value on your station's products. Learned in minutes.
2. **Recognise nominal** — know what the number should be. Requires the nominal stage to exist.
3. **Apply a rule** — find the applicable rule in your printed packet and read the threshold. Why paper is load-bearing (Principle 7).
4. **Project** — extrapolate a trend to a future event. **DOCUMENTED** controller work: CONTROL extrapolated supercritical-helium rise to predicted PDI pressure (note 014); TELMU converted usage rates into projected exhaustion GETs against the return timeline (note 015).
5. **Diagnose against conflicting indications** — the good part, and the best-documented:
   - GNC could not read Quad C valve state because the valves *and their talkbacks* depended on the lost Main Bus B — unpowered indication is not a known state (`stations/APOLLO13_GNC.md` §2.4).
   - A Quad D P/T ratio reading sat full-scale high with nothing wrong underneath (§2.1).
   - An RCS thrust-chamber pressure switch failed closed and compromised a caution/warning indication (note 014).
   - A battery malfunction warning proved to be a probable overtemperature-sensor failure (note 015).
   - RTCC incorrectly processed AGS body angles, producing a wrong-but-present product (note 065).
6. **Coordinate across a constraint collision** — where the co-operative game lives (§4.1).

**PROPOSED:** case authoring targets levels 4–6. A case exercising only 1–3 is a tutorial and should be labelled one.

Levels 4–6 are already reachable in the slice: the prototype carries observation age without an invented stale threshold (note 064), hidden product integrity separated from player-visible validity (note 065), and a ΔP rule that is **ground-callout only** (note 068) — so CONTROL holds a criterion the crew cannot see, which is level 6 by construction.

---

# 4. Roles

This section addresses Phase 2's open deliverable directly.

## 4.1 Select roles whose constraints collide

The instinct is to pick the most interesting individual stations. That produces parallel single-player games. The co-operative experience comes from pairs of positions whose documented Apollo 13 interaction forced a negotiation:

| Collision | Nature of the conflict | In PC+2? |
|---|---|---|
| **TELMU ↔ FIDO/RETRO** | LM consumables versus return trajectory — a faster return costs propellant, a slower one costs water and amp-hours | Yes — return-plan tradeoff, post-burn power-down |
| **CONTROL ↔ TELMU** | Attitude control and heaters draw the power that sustains the crew | Yes — burn configuration versus power-down |
| **GUIDO ↔ CONTROL** | What the computer *knows* versus what the hardware *can do* | Yes — PGNS/AGS cross-check versus DPS state |
| **CONTROL ↔ CAPCOM ↔ crew** | A ground-only criterion must become a spoken instruction to act | Yes — note 068, implemented |
| **INCO ↔ TELMU/EECOM** | Communications capability versus electrical load | Partly — S0 weak-link PAD transfer |
| **GNC ↔ EECOM** | Control authority depends on the electrical configuration another position owns | Accident scenario |
| **INCO ↔ FIDO** | A comms frequency configuration made LM tracking data unusable to RTCC | Accident scenario |

**PROPOSED** aggregation rule: *never combine two positions whose collision is the gameplay.* Combine positions that share a data domain and whose workload peaks are offset within the chosen case.

This reverses a tempting simplification. Folding TELMU and FIDO into one "LM and trajectory" player is efficient and destroys the best negotiation in the record. Folding FIDO and RETRO together keeps every collision intact while merging two positions that shared a discipline, an SSR and adjacent consoles (notes 003, 004).

## 4.2 Never combine

**DOCUMENTED** from note 003: systems and flight dynamics were different disciplines; CSM and LM systems responsibilities were separate; FIDO and GUIDO were not the same job; FLIGHT was decision authority, not an omnibus technical monitor.

The last is the one a small-player-count design will be tempted to violate by giving FLIGHT a discipline to watch. That destroys the poll — a FLIGHT who owns data has a position before the poll begins. `APOLLO13_PC2_PLAYER_PRODUCTS.md` already enforces this by denying FLIGHT a dashboard.

## 4.3 The aggregation ladder for PC+2

The slice names eight positions: FLIGHT, FIDO/RETRO, GUIDO, CONTROL, TELMU, INCO, FAO/PROCEDURES, CAPCOM. **PROPOSED** reductions, in the order the collisions survive:

| Players | Composition | What is lost |
|---|---|---|
| **8** | Full slice set as specified | Nothing — this is the documented target |
| **6** | FLIGHT · CAPCOM · CONTROL · GUIDO · TELMU · FIDO+RETRO | FAO/PROCEDURES folded into FLIGHT; INCO folded into GUIDO for the PAD-transfer phase |
| **5** | FLIGHT · CAPCOM · CONTROL · GUIDO · DYNAMICS+TELMU | Consumables negotiation weakens — the same player holds trajectory and consumables |
| **4** | FLIGHT · CAPCOM · CONTROL · GUIDO | Trajectory becomes a SimSup-supplied PAD; the burn monitoring and guidance cross-check remain intact |
| **3** | FLIGHT · CONTROL · GUIDO | CAPCOM folded into FLIGHT. Still viable: the burn, the shutdown rules and the PGNS/AGS cross-check survive |
| **2** | Not recommended | FLIGHT + one discipline collapses into a conversation |

**Recommended design target: 5–6.** Every collision marked "Yes" above is available and no player is idle. Note that PC+2 degrades gracefully in a way the accident scenario would not, because its climax is one propulsion event monitored by two or three disciplines — another argument for D-013's choice.

At **10+**, add **backroom (SSR) players** behind front-room positions. **DOCUMENTED:** each MOCR group had a supporting SSR; the Vehicle Systems SSR worked malfunction detection and isolation; Apollo 13's EECOM report specifically praised its SSR's electrical-power specialists (notes 004, 010, 012). A backroom player sees more detail than their controller and can act only through them — pure co-operative information asymmetry, so extra players deepen existing roles rather than diluting them.

**OPEN:** the target count to design the first session against. This recommends 5–6 with a documented 3-player floor; the project should decide from the group it expects to play with.

---

# 5. Difficulty without difficulty settings

Principle 4 bans easy/normal/hard. Six levers replace it, each a historical fact rather than a tuning constant:

1. **Which case, and its injection set.** The documented approach — simulations intensified as launch approached (note 011). note 056's timed injection object is the mechanism.
2. **Instrumentation and product honesty.** The strongest lever. The distance between truthful data and one lying source is the whole difference between reading a dashboard and doing the job. Already implemented: wrong-but-present ground products with hidden integrity (note 065), observation age (note 064).
3. **Player-set limits** where the station has them (§2.3).
4. **Backroom availability.** With SSR support you get analysis; without it you derive it yourself.
5. **Crew dependence.** How much the crew does correctly unprompted versus how precisely you must instruct them (§6).
6. **Time compression.** Off is harder and more authentic (§2.1).

**PROPOSED:** these are exposed to whoever configures the case, never to players as a difficulty menu, and never labelled with difficulty words. A case is described by its configuration, not by a tier.

---

# 6. The crew

D-013 leaves this open, and it gates the execution stage: CAPCOM says "Aquarius, Houston — fuel/oxidizer ΔP is over the limit, shut down," and then *what*?

**Already partly built.** note 068 implements the ground-callout loop as CONTROL decision → CAPCOM callout → crew shutdown command; note 059/060 implement a CAPCOM instruction → crew completion report → distinct post-switch re-observation cycle; note 069 recovers the actual LM STOP pushbutton as the crew's shutdown control; note 070 requires a fresh post-command observation before shutdown is treated as confirmed. The crew is already an actor that receives instructions, acts, reports, and whose action must be independently verified.

What is missing is the general rule for instructions the case did not anticipate.

| Option | Strength | Weakness |
|---|---|---|
| Fully scripted crew | Deterministic | Breaks the moment players do something unanticipated |
| Operator/SimSup plays the crew | Maximum flexibility; authentic voice | Needs a dedicated non-playing person |
| A player plays the crew | Dramatic | Not Mission Control; splits the group |
| **Checklist executor** | Crew performs well-formed instructions after a delay, with readback; malformed or ambiguous ones produce a request for clarification | Requires modelling instruction grammar |

**PROPOSED:** the checklist executor, generalising the event exchanges already implemented, with SimSup able to override or voice the crew. It makes CAPCOM's phrasing a real skill, makes **readback a gameplay verification loop** as well as a documented ritual, and degrades gracefully — an unparseable instruction becomes "Houston, say again," which is what a real crew would say.

**OPEN:** the instruction grammar — what counts as well-formed. note 070's refusal to invent an engine-off pressure threshold is the right precedent: bound it by documented crew-facing procedure wording rather than inventing a parser.

---

# 7. How a run ends, and the debrief

**PROPOSED:** a case outcome is a **state, not a grade**. The debrief reports, without scoring:

- final vehicle and consumables state against the case's end condition
- the decision timeline — what was seen, when, by whom, what was called
- which mission rules applied at each decision point, and what the rule said
- where indications or ground products diverged from physical truth, revealed *after* the run
- comparison with the historical outcome

The fourth item is the payoff for the entire information-boundary architecture, and it is only possible because physical state, telemetry and ground products are already separate layers with provenance metadata. Showing players afterwards that the product they rejected really was mis-processed — or that the one they trusted was not — is the honest substitute for an in-play hint system.

For PC+2 the natural anchor is **S13 residual review**: the historical burn's planned-versus-executed guidance quantities are documented, so the debrief can compare the players' burn against the real one without inventing a metric.

## 7.1 Roadmap consequence

`ROADMAP.md` places post-simulation review at Phase 10, after expansion. That is the one sequencing change this document argues for.

A research-first simulator with no debrief is unlearnable: players are denied hints during play by design, and would then be denied explanation afterwards by scheduling. `SIMULATION_ARCHITECTURE.md` §11 already specifies the event/audit record a minimal debrief needs, and the PC+2 prototype already emits decision events (note 066).

**PROPOSED:** a minimal event log plus debrief view moves into the first slice. Most of the data already exists; what is missing is the view.

---

# 8. Case sequencing after PC+2

D-013 settles the first slice, and the reasoning in note 048 — bounded model scope, explicit shutdown rules, graceful degradation, no compound failure propagation — is stronger than a purely gameplay-driven argument would have produced. This document defers to it entirely.

Two observations about what comes next, from a gameplay rather than a research standpoint:

**An onboarding case is worth authoring before the accident.** PC+2 asks a new group to hold eight positions through a burn with per-second rule monitoring. The **DPS supercritical-helium monitoring case** during translunar coast (note 014, `stations/APOLLO13_CONTROL.md` §2) is the smallest complete loop the research supports: 2–3 players, one subsystem, a documented threshold ladder (660–770 acceptable / 770–800 recheck in 2–3 hours / >800 extrapolate to PDI / predicted ≥1800 psia → propose a burn and vent), and a projection step. It teaches ladder levels 3–4 and the poll on a case where nothing happens in four minutes. It is also a *scheduled recurring check*, so its nominal stage has real work in it.

The project's own evidence audit reports these CONTROL thresholds as verified present in the Mission Operations Report, so the provenance concern is closed — though the LM-7 redline distinction added to the CONTROL spec (a ~959 psia launch redline versus the in-flight branches) shows why phase-specific criteria must not be merged.

**The accident brings the limit-setting mechanic.** §2.3's strongest mechanic needs EECOM, which needs the accident scenario. That is an argument for the accident as the next major case after PC+2 — not for doing it first.

---

# 9. Product risks not yet examined

## 9.1 Phone density versus authentic formats — the largest risk

A reconstructed Apollo format is dense numeric tabular data designed for a 21-inch monitor at arm's length. This has sharpened since MSK 1123 and 1137 were inspected and their layouts identified: the project now knows what the real GUIDO and CONTROL pages look like, which makes the rendering question concrete rather than hypothetical. `stations/APOLLO13_EECOM.md` §4 documents a page carrying dozens of parameters at one-second updates.

On a phone this needs pan and zoom, which destroys the at-a-glance scan that *was* the controller's competency. Open questions 20–21 identify the problem; nothing yet weighs it.

Options: tablet-class devices for the data-dense positions; authentic-density single-format-at-a-time with explicit format switching; per-case product subsetting, which `APOLLO13_PC2_PLAYER_PRODUCTS.md` already does and is historically defensible since controllers selected among formats; or accept pan/zoom and treat knowing where to look as part of the skill. **OPEN**, and worth deciding before the Phase 3 item "map required products into first-pass station screens" is built.

## 9.2 Idle time is a real failure mode

Real shifts were mostly quiet. §2.1's compression proposal is the mitigation; the risk is worth stating because PC+2's preparation-heavy shape makes it acute in the very first session.

## 9.3 FLIGHT is the most important role and the least reconstructed

FLIGHT runs the poll, owns the pacing and is the role that makes a session work. `APOLLO13_PC2_PLAYER_PRODUCTS.md` gives it four products, three of them class C — which is correct for a position whose job is integration, but it means FLIGHT's experience is almost entirely interface and ritual rather than data. If FLIGHT is a poor experience the product fails regardless of how faithful CONTROL's page is.

**PROPOSED:** FLIGHT's session interface — the poll, the timeline, per-discipline readiness state — is prototyped early. It is not blocked on display-format research.

## 9.4 In-person voice leaks information by design

Note 009 identifies this: co-located players can talk across the table, bypassing loop structure. **PROPOSED:** do not fight it with audio engineering. Enforce asymmetry through *artifacts* — each player has only their own phone and their own printed packet. This matters most for exactly the cases the slice has implemented: a ground-only ΔP criterion and a hidden-integrity product mean nothing if another player can read your screen.

---

# 10. Proposed decisions

Offered for acceptance, amendment or rejection in `DECISIONS.md`. None is accepted by this document.

| # | Proposal |
|---|---|
| P-1 | The unit of play is a **case**: one phase, defined start state, defined end condition |
| P-2 | The **GO/NO-GO poll** is a first-class interface event with recorded per-position responses |
| P-3 | Time compression is permitted **between** timeline events only, never within a state where a documented rule is being monitored |
| P-4 | Roles are selected for **constraint collisions**; positions whose collision is the gameplay are never combined |
| P-5 | Design target **5–6 players** for the PC+2 session, with the documented 3-player floor in §4.3 |
| P-6 | Difficulty is expressed only through the six levers in §5, never as a tier |
| P-7 | The crew is a **checklist executor** with readback, generalising the implemented instruction/report/re-observation loops, overridable by SimSup |
| P-8 | A case outcome is a **state, not a grade**; the debrief carries the learning |
| P-9 | A minimal event log and debrief view move into the **first slice** (roadmap change) |
| P-10 | Where a station has controller-set limits, they are a **real player action**, and the simulation never escalates an indication to guarantee it is noticed |
| P-11 | **FLIGHT's session interface is prototyped early**, ahead of data-dense station screens |
| P-12 | An **onboarding case** (DPS supercritical-helium monitoring) is authored before the accident scenario |

## Questions this raises for `OPEN_QUESTIONS.md`

- Target player count for the first session, and who arbitrates position assignment (§4.3)
- Whether time compression is FLIGHT's control, SimSup's, or a case property (§2.1)
- Phone versus tablet, and product density policy, before first-pass station screens (§9.1)
- Instruction grammar for crew execution — what counts as well-formed (§6)
- Whether SimSup is a required role, an optional role, or a case-definition file (§5, §6)
- How a case defines its end condition, and what happens if players never reach it

---

## Provenance

DOCUMENTED claims trace to existing research notes and station specifications: notes 003, 004, 008, 009, 010, 011, 012, 014, 015, 048, 049, 053, 056, 059, 060, 064, 065, 066, 068, 069, 070; the Apollo 13 station specifications; and `docs/scenarios/*`.

Three defects noted during source verification on 2026-09-12 are still present on `main` and are relevant to material this document cites:

1. `stations/APOLLO13_GUIDO.md` §5 and note 016 give "**P21 — LGC Update**". P27 is LGC UPDATE; P21 is Ground Track Determination, and R-567 Section 2 associates the AGS Initialization/Update downlist with P27. This document cites GUIDO's downlist material in §3 and §4.
2. `stations/APOLLO13_INCO.md` and note 018 cite "R. W. Winkelman et al., *Telemetry and Communications to Apollo*". The paper is "Telemetry and communications to Apollo **flight controllers**" by A. Glines and J. A. Lazzaro, ITC 1970.
3. `SIMULATION_SCENARIO_RESEARCH.md` §4 and note 011 treat Miller's recollection of Jay Honeycutt running a lunar-landing case involving the computer failure light as the same event as the well-documented pre-Apollo-11 program-alarm simulation, which was run by SimSup Dick Koos on 5 July 1969. A program alarm and the computer failure light are also different indications. This document therefore does **not** propose that case as an early scenario despite its appeal.

No claim in this document should be promoted to DOCUMENTED status on the strength of appearing here.
