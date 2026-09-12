# Apollo 13 PC+2 — premature DPS shutdown / restart branch

Date: 2026-09-12  
Status: **REVIEWED — sufficient for a bounded restart-decision and crew-action model**

## Question

What should happen in the simulation if the DPS stops prematurely during PC+2, and how should that differ from a deliberate shutdown caused by one of the documented mission-rule criteria?

## Primary-source finding

The Apollo 13 Mission Operations Report explicitly records two linked rules from the PC+2 Mission Rules Review:

1. the burn was to be shut down for the listed propulsion, attitude, guidance/control, and electrical criteria;
2. **if an early shutdown occurred for reasons other than those criteria, the descent engine was to be restarted** by ullaging, pressing the engine-start pushbutton, and turning on the descent-engine command-override switch.

The contemporaneous NASA mission transcript gives the crew-facing procedure more directly. CAPCOM told the crew that if the engine stopped during the burn and a flashing Noun 97 appeared, they should PRO, perform ullage, push Engine Start, and turn Descent Engine Override on. Haise subsequently read the rule/procedure back.

This creates a real decision branch:

```text
premature DPS stop
        |
        +-- caused by listed shutdown criterion --> do not treat as restart contingency
        |
        +-- affirmatively known non-rule cause ---> restart procedure eligible
        |
        +-- cause unresolved ----------------------> insufficient context; do not assume eligibility
```

## Important distinction from ignition-failure backup

Earlier checklist revisions around 75:15 GET also gave manual backup actions for **failure to ignite at TIG**: Start pushbutton, then Descent Engine Command Override if needed.

That is not the same event as an engine that has already ignited and then stops prematurely during the burn. The implementation must not collapse these two contingencies into one generic `engine_start_failure` state.

## Noun 97 boundary

The contemporaneous read-up associates a flashing Noun 97 with the in-burn stop/restart procedure.

For the current implementation:

- Noun 97 is retained as a crew-facing procedural cue;
- no unsupported detailed LGC/DSKY state machine is created around it;
- Noun 97 does not override the mission-rule restriction against restarting a rule-caused shutdown.

Exact Luminary internal sequencing can be researched later only if needed for a player-facing computer simulation.

## Implementation consequence

The restart evaluator distinguishes:

- `RESTART_ELIGIBLE`: premature engine stop whose cause is affirmatively classified as outside the listed shutdown criteria;
- `DO_NOT_RESTART_RULE_SHUTDOWN`: one or more listed criteria are triggered;
- `INSUFFICIENT_CONTEXT`: a premature stop occurred but the cause has not been established as non-rule;
- `NOT_APPLICABLE`: no premature stop.

This conservative distinction is necessary because several historical criteria remain intentionally `NOT_EVALUABLE` in the current model. The absence of a modeled trigger is **not** proof that the shutdown was unrelated to the rule set.

This is a procedural/audit classification, not an automatic engine command.

The crew actions are represented separately:

1. PRO on flashing Noun 97;
2. manual ullage;
3. Engine Start pushbutton;
4. Descent Engine Command Override on.

The current action layer records the latter three physical/control actions. It **does not** set `engine_running=True`. A later physical-response model or explicit source-bounded response event must determine whether restart actually occurs.

## Controller ownership

Do not invent a post-stop FLIGHT approval requirement.

The procedure and criteria were transmitted to and read back by the crew before the maneuver. Ground controllers still have important roles in determining whether a listed shutdown criterion exists, especially for ground-only observations such as fuel/oxidizer ΔP, but the restart sequence itself was already a crew-facing contingency.

## Sources

### Primary — Apollo 13 Mission Operations Report

NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, PC+2 Mission Rules Review.

Documents the listed shutdown criteria and states that an early shutdown for reasons other than those criteria was to be restarted by ullaging, pressing Engine Start, and using Descent Engine Command Override.

### Primary — Apollo 13 Mission Commentary / air-ground transcript

NASA Apollo 13 mission commentary/transcript around 76:31–76:37 GET.

CAPCOM gives the in-burn stop procedure: flashing Noun 97, PRO, ullage, Engine Start push, Descent Engine Override on; the crew reads the burn rules/procedure back.

### Supporting transcript reconstruction

Apollo 13 Flight Journal, Day 4 Part 1, reproduces the air-ground exchange and separately records the earlier no-ignition backup procedure. Used only to clarify chronology; the NASA transcript and Mission Operations Report are the governing sources.

## Stop condition

This is sufficient to implement the restart branch without reconstructing Noun 97 internals, exact DPS restart transients, or a detailed engine failure model.

Do not research those deeper topics until a playable decision requires them.

## Next implementation boundary

Once this branch is tested, the next high-value PC+2 work should connect a **ground-only shutdown criterion** to controller callout / crew action, because that creates a player-essential information asymmetry not already covered by the crew-visible alarm paths.
