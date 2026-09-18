# Gameplay Model

Status: **design proposal — nothing here is accepted**

Purpose: define what a *session* of this simulation actually is — what a player does minute to minute, what makes it difficult, how many players it needs, how a run ends, and how anyone can tell it went well.

Current player-interaction/playability work is tracked separately in `docs/PLAYER_INTERACTION_PLAYABILITY.md` and research note 313. That work audits the existing browser client and defines how to remove interface friction without removing operational uncertainty.

## How to read this document

Every research document in this repository describes what Apollo *was*. This one describes what the game *does*, which is a different kind of claim and must not be confused with the first. Four labels are used:

- **DOCUMENTED** — an Apollo fact, with the research note it comes from. No new history is asserted here; nothing is labelled DOCUMENTED unless it traces to an existing note.
- **IMPLEMENTED** — already built and running in `src/`, with the research note or decision that governs it.
- **PROPOSED** — a design choice this document argues for. A project decision, not a historical finding, and belongs in `DECISIONS.md` only if accepted.
- **OPEN** — a decision genuinely still the project's to make, where this document lays out options rather than choosing.

## Where this sits relative to current work

The first playable session exists. D-013 selected Apollo 13 PC+2 (77:55 GET through post-burn power-down); `docs/scenarios/` defines its parameters, state machine and player-product set; the session orchestration layer assigns seven logical stations, applies scenario events chronologically, gates the FLIGHT GO/NO-GO decision, handles the FLIGHT→CAPCOM handoff, and keeps a chronological audit log. D-014 selected the web transport, D-016 the continuous mission clock, D-017 the separate facilitator authority, and D-018 the five-player compact mode.

This document does not revisit any of that. It addresses what `DECISIONS.md` still lists as undecided and what the roadmap still marks open:

- station aggregation below five players (§4.3) — D-018 settled five; four-and-below is still open
- time acceleration / realtime pacing multiplier (§2.1)
- post-simulation evaluation format (§7)
- degree of Staff Support Room simulation (§4.3)

### What changed since the first draft of this document

The first draft was written before D-016 and proposed compressing time "between timeline events" so that "no player ever loses a decision to the clock." **D-016 rejects that, and is right to.** Under a continuous mission clock, losing an opportunity to the clock is not a failure of the design — it is the design. §2.1 is rewritten accordingly, and the proposal it contained is withdrawn rather than softened.

A later draft proposed a five-player configuration of its own. **D-018 has since accepted a different five**, on better grounds — §4.3 records why the accepted one wins by this document's own criterion, and the earlier proposal is withdrawn.

---

# 1. The central claim: Apollo supplies its own game structures

Principle 4 forbids scores, achievements, health meters, quest markers, unsolicited hints, colour-coded alerts, difficulty settings, and telling the player the correct decision. That is the right aesthetic, but it removes every conventional tool for goal communication, pacing, progress feedback and failure legibility. A design that simply deletes those functions produces an opaque, unpaced, unlearnable product.

The resolution is that Apollo operations already contained structures that do exactly this work, and the research here has already found them. The game layer does not need inventing; it needs **identifying**.

| Conventional game device | Documented Apollo mechanism that replaces it | Status |
|---|---|---|
| Turn-taking / decision beats | Flight Director **GO/NO-GO poll** | **IMPLEMENTED** — readiness reports + FLIGHT gate (note 079) |
| Win/lose criteria | **Mission rules**, published in advance, mapped to positions | IMPLEMENTED for PC+2 shutdown rules (notes 049, 053) |
| Quest log / objective list | **Flight plan and GET** | IMPLEMENTED — synchronized authoritative GET (note 084) |
| Alert system | **Limit-sense lights**, controller-set, deliberately noisy | DOCUMENTED, not in the first slice (`stations/APOLLO13_EECOM.md` §6) |
| Tutorial | **Console handbook and checklists**, per position | DOCUMENTED (note 008) |
| Difficulty setting | **Which case is run**, and its injection set | IMPLEMENTED — timed injection object (note 056) |
| Score | **Debrief** against mission rules and vehicle state | OPEN (§7) |
| Interaction verb | **Callout on a voice loop** | IMPLEMENTED for the ΔP loop (note 068) |

The most important entry is the first, and it is no longer hypothetical. Note 079 records that GO is no longer automatic in play: the session waits for an explicitly assigned FLIGHT player to record GO or NO-GO, readiness reports carry GET, player, station, ready/not-ready and an optional note, and the FLIGHT→CAPCOM handoff is an explicit queued transmission. That is the poll as a first-class event with recorded per-position responses.

**PROPOSED**, and the only thing left to generalise here: cases are authored to *converge on polls*. The PC+2 slice gets this for free from history; a future case should be chosen partly because it has one.

---

# 2. The unit of play is a case, not a mission

**DOCUMENTED:** Apollo integrated simulations were segmented by mission phase and were rarely long end-to-end runs (`SIMULATION_SCENARIO_RESEARCH.md` §1, notes 008, 011).

**PROPOSED:** generalise the shape the first slice already has — the unit of play is a **case**: one phase, one defined start state, one end condition. This bounds session length, makes reset trivial, and is the historically correct shape rather than a concession.

## 2.1 Pacing under a continuous clock

D-016 and note 084 establish the semantics: GET advances whenever the session is running; controller decisions and missing authorizations do not stop it; only an explicit session pause stops simulated time; timed entries are nominal milestones with prerequisites, not scene transitions; and an ineligible nominal event is recorded as **missed** and is not replayed retroactively.

**This is a better mechanic than the one this document originally proposed, and the original is withdrawn.** A gated model — where the sequence waits for the team — quietly reintroduces the thing Principle 4 exists to prevent: the world arranging itself around the player. Under D-016 the world does not wait. Note 084's cascade is the sharp end: ignition requires GO, P40 and nominal ullage; if GET passes P40 before FLIGHT records GO, P40 is missed, and a later GO does not retroactively activate it.

That single rule does more for the intended experience than any amount of interface design. It makes deliberation costly, makes the poll's timing matter as much as its outcome, and produces failure that is legible without any alert telling the team they failed.

### The pacing problem that remains

It is a real constraint, not a fidelity complaint. The slice starts at 77:55 GET; Kranz signals the final poll near 78:57 and it happens around 79:17; the burn runs about four and a half minutes. At 1:1 that is roughly eighty minutes of preparation before the first decision beat, and almost all of the drama in the last five.

Under a continuous clock the only honest lever is the **rate the clock runs at**, and `DECISIONS.md` still lists "time acceleration / realtime pacing multiplier" as undecided.

**PROPOSED:** a session time scale with three constraints that keep it compatible with D-016.

1. **It is a session control, in the same category as explicit pause** — which D-016 already permits — and therefore facilitator authority under D-017, never a controller action.
2. **It is never coupled to controller state.** The rate may not change because a decision is outstanding, a station is not ready, or a poll is in progress. That is the gated model returning through the back door.
3. **It is uniform and logged.** One authoritative clock for all stations, and a rate change is an audit-log event like any other, so a debrief can show the team was running at 4× when the P40 window passed.

### The tension worth stating plainly

A rate high enough to make eighty minutes of preparation bearable is a rate at which per-second burn monitoring becomes unplayable, and it materially raises the chance of missing the GO window. Both effects are real, and both are legitimate — but they are **difficulty choices, made before the run** (§5), not knobs to rescue a struggling team mid-session. Turning the rate down because the team is behind is exactly the scene-gating D-016 removed.

**OPEN:** whether a case declares a recommended rate profile, and whether changing the rate mid-session is permitted at all or only between runs. This document leans toward permitted-but-logged, on the grounds that a facilitator running a first session for new players needs it and the audit log keeps it honest.

## 2.2 Anatomy of a case

| Stage | What happens | Why it is there |
|---|---|---|
| **Brief** | Mission, phase, vehicle configuration, known open items | Controllers knew the mission plan. The game must not withhold the premise. |
| **Console setup** | Players take their paper, select displays, set what is theirs to set | §2.3 |
| **Nominal ops** | Timeline work; establishing what normal looks like | Without a baseline an anomaly is meaningless noise. Not filler. |
| **Injection** | A physical or ground-processing condition changes. Nothing is announced. | notes 011 §3, 056 |
| **Recognition → diagnosis** | Someone notices; disciplines exchange data; indications may conflict | The core skill (§3) |
| **Decision** | Recommendation → poll → call, against a clock that does not wait | §2.1 |
| **Execution → verification** | Command or crew instruction, then a *fresh* observation confirming it took | note 070 |
| **Debrief** | Event timeline, applicable rules, what was missed. No score. | §7 |

## 2.3 The high-agency opening decision

The strongest version in the corpus is EECOM's. **DOCUMENTED:** EECOM manually set the limits driving the limit-sense lights, normally chose tight limits so small drifts were noticed early, and so several lights illuminated at once as a routine condition — panel 3 carried 72 lights, 12 of them cryogenic (`stations/APOLLO13_EECOM.md` §6). The Review Board could not establish whether the O2 tank 2 indication appeared ~30 seconds before the failure or appeared and was missed.

That is a real tradeoff chosen before anything goes wrong: tight limits give early warning at the cost of a panel you learn to ignore; loose limits give a clean panel and no warning. **PROPOSED** as a mechanic, with the corollary that the simulation never escalates an indication to ensure the player notices.

EECOM is not a first-slice station, so this lands with the accident scenario. **The PC+2-era equivalent already exists**: controller **product rejection** (notes 065, 066) — the player judges a ground-derived product wrong and discards it, as Mission Control did when RTCC mis-processed AGS body angles and controllers fell back on the FDAI reference. Same shape of decision, same refusal to say which reading to trust.

---

# 3. The player's loop and the skill ladder

The loop: **scan → compare against expected → consult paper → form a position → say it out loud → live with the call.**

1. **Locate** — find a value on your station's products.
2. **Recognise nominal** — know what the number should be.
3. **Apply a rule** — find it in your printed packet and read the threshold. Why paper is load-bearing (Principle 7).
4. **Project** — extrapolate a trend to a future event. **DOCUMENTED**: CONTROL extrapolated supercritical-helium rise to predicted PDI pressure (note 014); TELMU converted usage rates into projected exhaustion GETs against the return timeline (note 015).
5. **Diagnose against conflicting indications** — the best-documented part:
   - Quad C valve state unreadable because the valves *and their talkbacks* depended on the lost Main Bus B — unpowered indication is not a known state (`stations/APOLLO13_GNC.md` §2.4)
   - a Quad D P/T ratio reading full-scale high with nothing wrong underneath (§2.1)
   - an RCS thrust-chamber pressure switch failed closed, compromising a caution/warning indication (note 014)
   - a battery malfunction warning that proved to be an overtemperature-sensor failure (note 015)
   - RTCC mis-processing AGS body angles into a wrong-but-present product (note 065)
6. **Coordinate across a constraint collision** — where the co-operative game lives (§4.1).

**PROPOSED:** case authoring targets levels 4–6. A case exercising only 1–3 is a tutorial and should be labelled one.

Levels 4–6 are reachable in the slice today: observation age is preserved without an invented stale threshold (note 064), hidden product integrity is separated from player-visible validity (note 065), and the ΔP rule is **ground-callout only** (note 068), so CONTROL holds a criterion the crew cannot see.

---

# 4. Roles

D-018 has since accepted a five-player compact mode, so this section records how that lands against the design rules below, and addresses what remains undecided: aggregation at four players and fewer.

## 4.1 Select roles whose constraints collide

The instinct is to pick the most interesting individual stations. That produces parallel single-player games. The co-operative experience comes from pairs whose documented Apollo 13 interaction forced a negotiation:

| Collision | Nature of the conflict | In PC+2? |
|---|---|---|
| **TELMU ↔ FIDO/RETRO** | LM consumables versus return trajectory | Yes |
| **CONTROL ↔ TELMU** | Attitude control and heaters draw the power that sustains the crew | Yes — burn configuration versus power-down |
| **GUIDO ↔ CONTROL** | What the computer *knows* versus what the hardware *can do* | Yes — PGNS/AGS cross-check versus DPS state |
| **CONTROL ↔ CAPCOM ↔ crew** | A ground-only criterion must become a spoken instruction to act | Yes — note 068, implemented |
| **INCO ↔ TELMU** | Communications capability versus electrical load | Partly — S0 weak-link PAD transfer |
| **GNC ↔ EECOM** | Control authority depends on another position's electrical configuration | Accident scenario |
| **INCO ↔ FIDO** | A comms frequency configuration made LM tracking data unusable to RTCC | Accident scenario |

**PROPOSED** aggregation rule: *never combine two positions whose collision is the gameplay.* Combine positions that share a data domain and whose workload peaks are offset within the case.

Under D-018's accepted five-player mode every collision above survives across bundles except **CONTROL ↔ TELMU**, which becomes intra-player (§4.3).

The implemented station set already reflects this: **FIDO_RETRO is a single logical station**, which is the right merge — two positions sharing a discipline, an SSR and adjacent consoles (notes 003, 004) — while every collision above stays intact.

## 4.2 Never combine

**DOCUMENTED** from note 003: systems and flight dynamics were different disciplines; CSM and LM systems responsibilities were separate; FIDO and GUIDO were not the same job; FLIGHT was decision authority, not an omnibus technical monitor.

The last is the one a small-player-count design will be tempted to violate. A FLIGHT who owns data has a position before the poll begins. `APOLLO13_PC2_PLAYER_PRODUCTS.md` already enforces this by denying FLIGHT a consolidated dashboard, and note 079 keeps FLIGHT's job as decision integration.

## 4.3 The aggregation ladder for PC+2

The implemented set is seven logical stations: CONTROL, GUIDO, TELMU, FIDO_RETRO, INCO, FLIGHT, CAPCOM.

**D-018 settles the five-player case, and settles it better than this section's first draft did.**

| Players | Composition | Status |
|---|---|---|
| **7** | The implemented set | **IMPLEMENTED** — the documented target |
| **5** | FLIGHT · CAPCOM · **LM SYSTEMS** (TELMU + CONTROL) · **FLIGHT DYNAMICS** (GUIDO + FIDO/RETRO) · INCO | **ACCEPTED — D-018**; station-set ownership implemented, HTTP/UI pending |
| **4 or fewer** | — | **OPEN** — `DECISIONS.md` lists "four-player-or-smaller station aggregation" as undecided |

### Why D-018's five beats what this document first proposed

The earlier draft proposed FLIGHT · CAPCOM · CONTROL · GUIDO · TELMU+FIDO_RETRO. Measured against this document's own rule in §4.1 — never combine two positions whose collision *is* the gameplay — that was the worse configuration. It merged **TELMU ↔ FIDO/RETRO**, the strongest cross-discipline collision in the record, and it dropped **INCO** entirely.

D-018 does neither. By bundling along Apollo's own functional groups — Systems Operations for TELMU+CONTROL, Flight Dynamics for GUIDO+FIDO/RETRO (note 091) — it keeps TELMU and FIDO/RETRO in *different* bundles, so that negotiation survives, and it keeps INCO staffed. Note 091 also reaches §4.2's FLIGHT-and-CAPCOM-stay-separate conclusion independently, on the same authority-boundary reasoning.

The one collision it trades is **CONTROL ↔ TELMU**, which becomes intra-player. That is the right one to give up: it is the collision most internal to a single vehicle, while the cross-discipline ones — harder to reconstruct, more interesting to play — all survive.

### Station-set ownership changes what aggregation costs

D-018 and note 092 do not merge the stations; one player **owns multiple original station identities**. TELMU and CONTROL keep separate products, alerts, readiness judgments, actions and audit identities; information available to one is not silently reclassified as available to the other; rules and authorization still resolve against the original call sign.

That changes the cost of aggregation. A bundled player is doing two jobs with two information sets, not one blended job — so the collision does not disappear, it relocates, from a negotiation between two people to a reconciliation inside one head. Weaker as co-operative drama, intact as an information boundary.

### Below five

Still **OPEN**, and the useful shape is to extend D-018's bundles downward rather than invent a separate ladder. FLIGHT and CAPCOM are the last things to merge, for note 091's reasons; the honest four-player question is whether INCO folds into FLIGHT DYNAMICS for the PAD-transfer phase, or whether keeping a fourth bundle costs less.

A wrinkle under D-016: at low player counts a single player holds more decisions, and the clock does not wait for any of them. A compact configuration is not merely thinner — it is **harder**, because the same GO window arrives with fewer people to reach it. That argues for compact mode being presented as a difficulty axis (§5) rather than purely as an accessibility feature.

At **8+**, add **backroom (SSR) players** behind front-room positions. **DOCUMENTED:** each MOCR group had a supporting SSR; the Vehicle Systems SSR worked malfunction detection and isolation; Apollo 13's EECOM report praised its SSR's electrical-power specialists (notes 004, 010, 012). A backroom player sees more detail than their controller and can act only through them — pure co-operative information asymmetry, so extra players deepen roles rather than diluting them. This is also the natural home for the "degree of Staff Support Room simulation" question.

---

# 5. Difficulty without difficulty settings

Principle 4 bans easy/normal/hard. Six levers replace it, each a historical fact or an accepted architectural property rather than a tuning constant:

1. **Which case, and its injection set.** Simulations intensified as launch approached (note 011). The timed injection object (note 056) is the mechanism.
2. **Instrumentation and product honesty.** The strongest lever, and already built: wrong-but-present ground products with hidden integrity (note 065), observation age (note 064).
3. **Clock rate.** Under D-016 this is a difficulty choice, because a faster clock genuinely costs opportunities (§2.1). Chosen before the run.
4. **Player count.** Per §4.3, D-018's compact mode against an unwaiting clock is harder, not just thinner.
5. **Backroom availability.** With SSR support you get analysis; without it you derive it yourself.
6. **Crew dependence.** How much the crew does correctly unprompted versus how precisely you must instruct them (§6).

**PROPOSED:** these are exposed to the facilitator (D-017), never to players as a difficulty menu, and never labelled with difficulty words. A case is described by its configuration, not by a tier.

---

# 6. The crew

**Already partly built.** The ΔP ground-callout loop runs CONTROL decision → CAPCOM callout → crew shutdown command (note 068); notes 059/060 implement CAPCOM instruction → crew completion report → distinct post-switch re-observation; note 069 recovers the LM STOP pushbutton as the crew's control; note 070 requires a fresh post-command observation before shutdown counts as confirmed; notes 083 and 085 integrate crew response after a ground shutdown call. The crew already receives instructions, acts, reports, and has its action independently verified.

What is missing is the general rule for instructions the case did not anticipate.

| Option | Strength | Weakness |
|---|---|---|
| Fully scripted crew | Deterministic | Breaks the moment players do something unanticipated |
| Facilitator plays the crew | Maximum flexibility; authentic voice | Needs a dedicated non-playing person |
| A player plays the crew | Dramatic | Not Mission Control; splits the group |
| **Checklist executor** | Crew performs well-formed instructions after a delay, with readback; malformed ones produce a request for clarification | Requires modelling instruction grammar |

**PROPOSED:** the checklist executor, generalising the exchanges already implemented, with the facilitator able to override or voice the crew. It makes CAPCOM's phrasing a real skill, makes **readback a verification loop** as well as a documented ritual, and degrades gracefully — an unparseable instruction becomes "Houston, say again."

Under D-016 this acquires a second edge: crew action takes mission time, and the clock does not wait for a badly-phrased instruction to be corrected. Ambiguity has a cost measured in GET.

**OPEN:** the instruction grammar. Note 070's refusal to invent an engine-off pressure threshold is the right precedent — bound it by documented crew-facing procedure wording rather than inventing a parser.

---

# 7. How a run ends, and the debrief

`DECISIONS.md` still lists post-simulation evaluation format as undecided.

**PROPOSED:** a case outcome is a **state, not a grade**. The debrief reports, without scoring:

- final vehicle and consumables state against the case's end condition
- the decision timeline — what was seen, when, by whom, what was called
- **which nominal opportunities were missed, and what each one required** — the D-016 cascade makes this the single most informative thing a debrief can show
- which mission rules applied at each decision point, and what the rule said
- where indications or ground products diverged from physical truth, revealed *after* the run
- comparison with the historical outcome

The fifth item is the payoff for the whole information-boundary architecture, and it is only possible because physical state, telemetry and ground products are separate layers with provenance metadata. Showing players afterwards that the product they rejected really was mis-processed — or that the one they trusted was not — is the honest substitute for an in-play hint system.

Most of the data already exists: the session keeps a chronological audit log, and note 084's engine records missed nominal events explicitly. What is missing is the view.

## 7.1 Roadmap consequence

`ROADMAP.md` places post-simulation review at Phase 10, after expansion. That is the one sequencing change this document argues for. Players are denied hints during play by design; denying them explanation afterwards by scheduling makes the product unlearnable.

For PC+2 the natural anchor is **residual review**, where planned-versus-executed guidance quantities are documented.

---

# 8. Case sequencing after PC+2

D-013 settles the first slice and note 048's reasoning is stronger than a purely gameplay-driven argument would have produced. This document defers to it entirely.

Two forward-looking observations:

**An onboarding case is worth authoring before the accident.** PC+2 asks a new group to hold seven positions through a burn with per-second rule monitoring, against a clock that does not wait. The **DPS supercritical-helium monitoring case** during translunar coast (note 014, `stations/APOLLO13_CONTROL.md` §2) is the smallest complete loop the research supports: 2–3 players, one subsystem, a documented threshold ladder, and a projection step. It teaches ladder levels 3–4 on a case whose drama is not compressed into four minutes — which matters more under a continuous clock, not less.

**The accident brings the limit-setting mechanic.** §2.3's strongest mechanic needs EECOM, which needs the accident scenario. That argues for the accident as the next major case after PC+2 — not for doing it first.

---

# 9. Product risks not yet examined

## 9.1 Phone density versus authentic formats — the largest risk

A reconstructed Apollo format is dense numeric tabular data designed for a 21-inch monitor at arm's length. This has sharpened now that MSK 1123 and 1137 layouts have been inspected and per-station presentation boundaries exist for all seven stations (notes 073–078): the rendering question is concrete, and it is the next thing between the prototype and a session people can actually play.

On a phone, dense formats need pan and zoom, which destroys the at-a-glance scan that *was* the controller's competency. Under D-016 this is worse than an ergonomic problem — time spent hunting for a value is mission time, and the window may pass while you scroll.

Options: tablet-class devices for data-dense positions; authentic-density single-format-at-a-time with explicit switching; per-case product subsetting, which the player-product set already does and which is historically defensible since controllers selected among formats; or accept pan/zoom and treat knowing where to look as part of the skill. **OPEN**, and worth deciding before first-pass station screens are built.

## 9.2 Idle time is a real failure mode

Real shifts were mostly quiet. §2.1's clock-rate proposal is the mitigation; the risk is worth stating because PC+2's preparation-heavy shape makes it acute in the very first session.

## 9.3 FLIGHT is the most important role and the least data-bearing

FLIGHT runs the poll and owns the pacing. The player-product set gives it four products, three of them class C — correct for an integrator, but it means FLIGHT's experience is almost entirely interface and ritual. If FLIGHT is a poor experience the product fails regardless of how faithful CONTROL's page is.

**PROPOSED:** FLIGHT's session interface — the poll, the timeline, per-discipline readiness state, and now the visible cost of an unwaiting clock — is prototyped early. It is not blocked on display-format research.

## 9.4 In-person voice leaks information by design

Note 009 identifies this: co-located players can talk across the table, bypassing loop structure. **PROPOSED:** do not fight it with audio engineering. Enforce asymmetry through *artifacts* — each player has only their own device and their own printed packet. This matters most for exactly what the slice has implemented: a ground-only ΔP criterion and a hidden-integrity product mean nothing if another player can read your screen.

---

# 10. Proposed decisions

Offered for acceptance, amendment or rejection in `DECISIONS.md`. None is accepted by this document.

| # | Proposal |
|---|---|
| P-1 | The unit of play is a **case**: one phase, defined start state, defined end condition |
| P-2 | Cases are authored to **converge on polls** |
| P-3 | A **session time scale** exists as a facilitator control in the same category as explicit pause: never coupled to controller state, uniform across stations, and logged as an audit event |
| P-4 | Roles are selected for **constraint collisions**; positions whose collision is the gameplay are never combined |
| P-5 | ~~Design target 5–6 players~~ — **superseded by D-018**, which accepts a five-player compact mode built on better grounds (§4.3) |
| P-6 | Difficulty is expressed only through the six levers in §5, never as a tier; **player count and clock rate are difficulty axes**, chosen before a run |
| P-7 | The crew is a **checklist executor** with readback, generalising the implemented exchanges, overridable by the facilitator |
| P-8 | A case outcome is a **state, not a grade**; the debrief reports missed nominal opportunities as first-class content |
| P-9 | A minimal debrief view moves into the **first playable milestone** (roadmap change) |
| P-10 | Where a station has controller-set limits, they are a **real player action**, and the simulation never escalates an indication to guarantee it is noticed |
| P-11 | **FLIGHT's session interface is prototyped early**, ahead of data-dense station screens |
| P-12 | An **onboarding case** (DPS supercritical-helium monitoring) is authored before the accident scenario |

**Withdrawn from the first draft:** the proposal to compress time between timeline events so that no decision is lost to the clock. D-016 supersedes it, and the continuous-clock model is the better mechanic.

## Questions this raises for `OPEN_QUESTIONS.md`

- Target player count for the first session, and who arbitrates station assignment (§4.3)
- Whether a case declares a recommended clock rate, and whether mid-session rate changes are permitted (§2.1)
- Device class and product density policy, before first-pass station screens (§9.1)
- Instruction grammar for crew execution — what counts as well-formed (§6)
- How a case defines its end condition, and what happens if players never reach it — sharper under D-016, where a case can end with the burn simply never having occurred

---

## Provenance

DOCUMENTED claims trace to existing research notes and station specifications: notes 003, 004, 008, 009, 010, 011, 012, 014, 015, 048, 049, 053, 056, 059, 060, 064, 065, 066, 068, 069, 070, 073–079, 084, 091, 092; the Apollo 13 station specifications; and `docs/scenarios/*`.

Three source defects this document's citations touch are tracked in **issue #3** and are unresolved on `main`: the P21/P27 program-number error in the GUIDO spec and note 016; the ITC 1970 paper attribution in the INCO material; and the Honeycutt/Koos simulation conflation in the scenario research. The third is why §8 does **not** propose the program-alarm case as an early scenario despite its appeal.

No claim in this document should be promoted to DOCUMENTED status on the strength of appearing here.
