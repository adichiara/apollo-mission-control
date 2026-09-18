# Player Interaction and Playability

Status: **working design document — no new project decisions accepted here**  
Date: 2026-09-18

Purpose: turn the research-complete information/authority architecture into an in-person experience people can operate under time pressure without turning Mission Control into a conventional game UI.

Historical/design boundary: see research note 314.

## Design objective

The station interface should make the controller's **job** difficult, not make the software difficult.

Preserve:

- incomplete/conflicting evidence;
- information asymmetry;
- cross-station dependence;
- continuous GET;
- procedure/rule lookup;
- uncertain diagnosis;
- consequences of late/omitted/wrong actions.

Remove or reduce:

- ambiguous navigation;
- developer vocabulary;
- accidental wrong-station actions;
- branch-revealing controls;
- test-harness operations exposed as player actions;
- unnecessary scrolling and repeated data entry;
- browser/rejoin friction.

## The interface is three layers

### 1. Simulator/session strip — modern and clearly separate

Always available:

- original call sign;
- GET;
- case/phase;
- connection/sync state;
- compact-role active original station.

This layer is modern infrastructure. It should not visually masquerade as an Apollo CRT.

### 2. Station product area — the dominant working surface

Contains only sourced/approved products required for the case.

Rules:

- stable field locations;
- preserve historical terminology when known;
- label project renderings honestly;
- no generic subsystem-health score;
- no hidden integrity;
- no automatic diagnosis;
- no merged compact-role dashboard.

### 3. Communication/action area — small and contextual

Contains only things the controller can actually do.

Preferred verbs:

- REPORT / CALLOUT;
- READINESS;
- RECOMMEND;
- GO / NO-GO for FLIGHT when applicable;
- APPROVE / QUEUE for FLIGHT;
- TRANSMIT for CAPCOM;
- documented station configuration/action only when that station truly owns it.

Avoid malfunction-named buttons that reveal the current exercise.

## Current validation client: what should not become final UI accidentally

### CONTROL

Current controls include a permanent `CALL OUT ΔP SHUTDOWN CRITERION` button and an `ASSESS SHUTDOWN EVIDENCE` button.

Keep the semantic domain events, but redesign the player interaction:

- known rules stay in the reference material;
- the player sees the evidence;
- the player makes a general callout/recommendation;
- server-side evidence evaluation remains for audit/debrief, not as an in-play answer button.

### Generic fields

Current fields display project `validity` and `source_layer` values.

Retain those in facilitator/debrief/model-proof tooling.

Final station UI should expose only data-quality/status cues that are historically or operationally justified for that product.

### Readiness

The permanent readiness form is acceptable for validation but should not dominate the eventual technical-station workspace.

The poll should feel like an operational communication event, not a game checkpoint.

## Phone layout concept

For portrait phones:

1. compact session strip;
2. station/product title;
3. one primary product viewport;
4. secondary product selector if the station needs more than one format;
5. contextual action/communication drawer;
6. no long vertical dashboard combining unrelated products.

Dense historical products may use:

- one format at a time;
- stable cropped/phone-adapted rendering;
- deliberate product switching;
- local horizontal pan only where unavoidable.

Do not make players continuously pinch-zoom a whole historical 21-inch display merely to preserve physical pixel density.

## Compact-player concept

A compact player still operates original stations.

Example:

`LM SYSTEMS`

- TELMU tab
- CONTROL tab

The bundle name may appear in the modern session strip; the dominant station identity remains the active original call sign.

Each tab may show neutral last-update GET, but not an “anomaly waiting” badge unless the original station would have an equivalent alert.

Actions always state the original station they will be attributed to.

## Information arrival

Player products should update because their modeled source/product updates, not because a game layer decides something is important.

Do not flash or highlight a new value merely because it crossed a scenario-author threshold unless the historical display/alert system would have done so.

Modern connection-loss/rejoin warnings are allowed because they describe simulator infrastructure, not spacecraft health.

## Communication

In-person conversation is initially the general controller-to-controller medium.

Software remains necessary for actions whose **state transition matters**:

- readiness/report provenance;
- FLIGHT GO/NO-GO;
- FLIGHT-approved CAPCOM queue;
- CAPCOM transmission;
- supported controller/configuration actions;
- audit/debrief timing.

Do not build a chat application merely to imitate every historical loop. Add loop restrictions only where a selected scenario's information asymmetry depends on them.

## Printed references

Paper should reduce memory burden while preserving lookup work.

Next packet prototype should favor:

- a very short common sheet;
- one original-station quick index;
- station rules/thresholds;
- phase procedure/timeline;
- detailed references behind those pages.

Measure findability before adding more paper.

## Player preparation

Before timed integrated play, require a neutral part-task checkout:

- identify station and GET;
- find one field;
- find one rule;
- make one readiness report;
- practice one role-specific action;
- compact players switch stations once.

This is not a tutorial overlay during the live case.

## What makes a case playable

A case should have:

- a clear operational purpose known at start;
- enough nominal operation to establish context;
- meaningful work for every staffed role;
- at least one cross-station dependency;
- a decision or disposition that cannot be solved by one omniscient display;
- consequences that continue after the decision;
- a natural debrief endpoint.

Avoid cases where one player diagnoses everything while others wait.

## Idle-time control

Preferred solutions, in order:

1. better case boundary;
2. assign real concurrent work;
3. shorter onboarding/part-task case;
4. historical/causal secondary tasks;
5. only then consider time acceleration.

Time acceleration is not neutral; it changes workload.

## Debrief as part of playability

The simulator deliberately withholds truth and correctness during play. It therefore needs a useful debrief early, not after all scenario expansion.

Minimum debrief should show:

- what each station could see at important times;
- communications/actions and GET;
- missed nominal opportunities;
- fresh versus stale observations where relevant;
- final vehicle/mission state;
- hidden physical/integrity state revealed only after the run;
- applicable rule/procedure;
- no numeric game score.

## First site-facing interaction lab

A non-final FLIGHT/CAPCOM prototype now lives at `/player-lab`.

It deliberately uses the existing authoritative session API rather than a mock data layer. That makes it useful for real interaction testing while preserving the current `/` validation client unchanged.

The first prototype implements the design boundary above:

- persistent original call sign + GET + phase + connection/session state;
- FLIGHT controller-report stream and explicit GO/NO-GO action;
- FLIGHT approval of a crew-facing item;
- CAPCOM approved/pending versus transmitted queue state;
- CAPCOM deliberate transmission;
- separate crew-report stream;
- no subsystem-health dashboard for FLIGHT;
- no CONTROL/ΔP solution control;
- no automated shutdown-evidence assessment;
- no generic `source_layer`, provenance, or hidden-integrity metadata in the player rendering.

The prototype is intentionally limited to FLIGHT/CAPCOM. It is an interaction experiment, not the replacement player client and not an exact Apollo console reconstruction.

The next question it should answer is whether the coordination workflow is understandable under continuous GET without project-internal explanation. After that, CONTROL/GUIDO product-scanning prototypes can be added using the same session strip/product/action hierarchy.

## Player-state semantic tightening

The first FLIGHT/CAPCOM lab exposed several additional project-internal states that should not become player concepts simply because the server has them.

### Decision gates are not player products

The session API carries `pending_gate` so the runtime can enforce action eligibility. The player lab no longer renders that value.

A controller should infer that a decision is due from the operational context, reports, timeline/procedure, and available action—not from a project label such as `flight_go`.

### Raw phase identifiers are implementation vocabulary

Internal values such as `pc2_final_readiness` are useful state-machine identifiers. The lab now converts them to a human-readable phase label before display.

Longer term, player-facing phase/timeline wording should come from scenario/profile data rather than from arbitrary internal enum/string names.

### A binary state is not necessarily a meaningful indication

The current authoritative PC+2 state stores `flight_go` as a Boolean. Before FLIGHT has recorded a decision, the value is `False`; an explicit NO-GO also leaves it `False`.

Therefore `flight.go_for_burn = false` cannot safely be shown as “NO” to the player: it would collapse **not yet decided** and **NO-GO recorded** into the same display.

The player lab now omits that field and uses the explicit FLIGHT decision interaction instead.

If a future player product needs decision status, the domain must expose unambiguous semantics such as `pending / go / no-go` or an event-derived recorded-decision state rather than asking the UI to infer meaning from a Boolean.

### Join/setup controls are not ongoing controller work

After a player establishes or restores a position, the join panel now collapses. Rejoin remains automatic through the stored identity.

This reduces accidental role-switch/setup behavior during timed play without changing assignment authority.

## First interface prototypes

Prototype in this order.

### A. FLIGHT

Why first: least blocked by exact CRT research and most dependent on interaction quality.

Prototype:

- chronological readiness/recommendation stream;
- current poll/disposition;
- timeline/GET context;
- CAPCOM approval queue;
- no subsystem dashboard.

### B. CAPCOM

Prototype:

- approved queue;
- transmitted state;
- crew receipt/readback/report;
- strong separation among the three.

### C. CONTROL

Prototype:

- stable burn-monitor product;
- rule lookup reference outside the telemetry card;
- general callout/recommendation interaction;
- remove branch-specific solution button from final-player concept.

### D. GUIDO

Prototype:

- guidance state/load verification/post-burn residual;
- product switching rather than a long combined page.

### E. Compact bundles

Evaluate whether the two-station tab model remains usable under the actual clock.

## Playtest success is not “players succeeded”

A run can be useful even if the mission outcome is poor.

The interface succeeds when:

- players knew what station they were operating;
- the information required by the modeled job was findable;
- decisions failed for operational reasons rather than UI ambiguity;
- no hidden state leaked;
- cross-station coordination remained necessary;
- players could recover from routine browser/network interruptions;
- the post-run evidence makes failures understandable.

See `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md` and the report template.
