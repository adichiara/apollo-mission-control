# PC+2 player reference packet

Date: 2026-09-13  
Status: **READY FOR INITIAL PHYSICAL PLAY — structure is a project adaptation, not an Apollo handout reconstruction**

Use this document together with `PC2_PLAYER_PREPARATION.md`. Players may consult it during timed play.

## 1. Common operational brief

Scenario phase: Apollo 13 PC+2 preparation/execution beginning near 77:55 GET and continuing through immediate post-burn verification/power-down.

Operating rules:

- GET normally continues while controllers evaluate and coordinate.
- Use only information available to your assigned original station(s), plus communications actually received during play.
- FLIGHT owns the modeled final GO/NO-GO decision.
- CAPCOM is the modeled crew-facing transmission path.
- Facilitator/admin controls are not player controls.
- A controller conclusion, crew report, telemetry observation, and hidden physical state are different evidence types.
- Uncertainty is allowed. Do not infer hidden simulator state merely because a decision is difficult.

This packet intentionally does not state whether a nonnominal branch will occur.

---

## 2. Original-station sheets

### FLIGHT

Responsibility in this implementation:

- integrate readiness and reported station judgments;
- make the modeled final GO/NO-GO decision;
- preserve station authority boundaries rather than infer private evidence;
- route approved crew-facing information through CAPCOM.

Use during play:

- review station readiness/status as presented;
- resolve operational disposition from available reports/evidence;
- do not treat facilitator state as controller evidence.

### CAPCOM

Responsibility in this implementation:

- serve as the modeled crew voice path;
- transmit approved queued items deliberately;
- preserve controller/FLIGHT authority rather than invent technical content.

Use during play:

- queued content is not transmitted automatically;
- distinguish message approval from actual transmission and crew receipt.

### CONTROL

Responsibility in this implementation:

- monitor the modeled descent-stage propulsion/system evidence assigned to CONTROL;
- evaluate source-backed ground criteria represented by the simulator;
- explicitly initiate modeled controller callouts/actions when warranted.

Important evidence distinction:

- ground telemetry, crew/onboard indication, crew report, controller conclusion, and hidden engine state must not be treated as interchangeable.

### TELMU

Responsibility in this implementation:

- monitor the modeled LM electrical/environmental/system products assigned to TELMU;
- report readiness/issues from TELMU evidence;
- remain distinct from CONTROL even when both stations belong to the same compact player.

### GUIDO

Responsibility in this implementation:

- monitor modeled guidance/navigation/attitude information;
- evaluate attitude-related criteria only from presented evidence;
- remain distinct from FIDO/RETRO even in compact play.

### FIDO/RETRO

Responsibility in this implementation:

- monitor the modeled trajectory/burn information used by the first PC+2 slice;
- use the displayed/received flight-dynamics information and modeled coordination path;
- treat `FLIGHT DYNAMICS` as a modern compact-player label only, not a historical combined station.

### INCO

Responsibility in this implementation:

- monitor the modeled communications/data-path evidence assigned to INCO;
- distinguish communications/data-path status from CAPCOM's crew voice role;
- report communications issues through the modeled controller coordination path.

---

## 3. Rule / criterion sheet

Only criteria already supported strongly enough for first-playable use are executable. Preserve the distinction between ground and onboard criteria.

### CONTROL — fuel/oxidizer differential pressure

- Source-backed ground callout criterion: fuel/oxidizer inlet differential pressure **greater than 25 psi**.
- This is represented as a ground/controller criterion.
- The packet does **not** state whether this condition will occur in the run.

### CONTROL — thrust / chamber pressure

Historical PC+2 material distinguishes:

- ground thrust-chamber-pressure criterion: approximately **85 psi**;
- onboard thrust criterion: approximately **77 percent**.

Project boundary:

- the ground chamber-pressure observation path is represented;
- the exact onboard 77-percent indication remains unresolved and must not be fabricated or aliased to ground chamber pressure.

### CONTROL — inlet pressure

Historical PC+2 material distinguishes:

- ground engine-inlet-pressure criterion: approximately **150 psi**;
- onboard criterion: approximately **160 psi**.

Project boundary:

- the exact singular historical ground selection/aggregation behind the 150-psi criterion remains unresolved;
- do not infer or fabricate a single combined value beyond what the client actually presents.

### GUIDO / guidance-attitude criteria

Use only the attitude/error/rate evidence and rule status actually presented by the client. Startup-transient wording has been source-reviewed in the project; do not invent an additional timing gate from memory or assumption.

### Warning / alarm criteria

Use warning/alarm evidence as presented by the assigned station. Do not interpret absence of a displayed field as proof that the corresponding spacecraft condition is normal.

---

## 4. Nominal PC+2 phase reference

At a high level, the run represents:

1. final PC+2 preparation and readiness;
2. maneuver execution under continuous GET;
3. controller monitoring during the burn;
4. immediate post-burn verification;
5. power-down / disposition work represented by the current vertical slice.

This is orientation, not a branch script. The facilitator may introduce no nonnominal condition at all, or may exercise a source-bounded branch. Players are not told which before the run.

---

## 5. Modern client-operation sheet

The following are simulator mechanics, not Apollo procedures.

Before timed play, each player must be able to:

- join the assigned station or approved station set;
- identify current GET;
- identify the active original station;
- locate readiness/actions relevant to that station;
- reload/rejoin without changing ownership.

For five-player compact mode:

- `LM SYSTEMS` owns TELMU + CONTROL;
- `FLIGHT DYNAMICS` owns GUIDO + FIDO/RETRO;
- switch deliberately between original substations;
- confirm the active original call sign before taking a station-qualified action;
- readiness/action/audit attribution remains tied to the original station.

## Historical-source boundary

This packet's organization is a modern validation aid. Its historical content is constrained by the project's primary-source research, especially research notes 049, 053–064, 090, 095–097. The five-part packet layout, page order, compact presentation, and browser instructions are not claimed to reproduce an Apollo-era controller handout.