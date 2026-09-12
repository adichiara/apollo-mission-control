# Apollo 13 PC+2 — restart command and physical DPS re-ignition boundary

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED-PARTIAL — restart command-to-engine-on architecture established; exact restart transient and post-restart thrust history remain unresolved**

## Question

Once a premature PC+2 shutdown has been classified as restart-eligible and the crew performs the documented restart sequence, what physical DPS response can the simulation represent without assuming that crew actions automatically succeed or inventing an ignition transient?

## Mission-specific primary evidence

### Apollo 13 Mission Operations Report — 28 April 1970

The PC+2 Mission Rules review states that if an early shutdown occurred for reasons other than the listed shutdown criteria, the LM descent engine was to be restarted by:

1. ullaging;
2. depressing the engine START pushbutton;
3. turning on the Descent Engine Command Override switch.

This establishes that a restart attempt was an explicitly intended capability during PC+2, but it does not by itself establish a guaranteed successful physical response.

### Apollo 13 contemporaneous air-to-ground rules read-up

At approximately 76:35 GET, CAPCOM transmitted the same contingency in operational form: if the engine stopped during the burn and flashing Noun 97 appeared, the crew was to PRO, perform manual ullage, push ENGINE START, and turn the Descent Engine Command Override on. Haise read the sequence back.

The transcript therefore supports the crew-facing restart procedure independently of the postflight report.

### Apollo 13 Review Board Appendix B

The Review Board records the same final rule: an early engine shutdown not caused by the listed criteria was to be followed by a relight attempt using the engine-start pushbutton and Descent Engine Command Override switch.

## Contemporary LM subsystem evidence

### Apollo Operations Handbook — Lunar Module, LMA790-3-LM

Contemporary LM guidance/control documentation establishes the command-response architecture:

- the descent engine can receive automatic or manual on/off commands;
- manual commands use the START/STOP pushbuttons;
- descent-engine on/off commands route through the Descent Engine Control Assembly (DECA);
- these commands actuate the descent-engine pilot valves;
- the pilot-valve/actuator system opens or closes the fuel and oxidizer shutoff valves;
- the DPS is restartable.

This is enough to model a successful **engine-on physical response** as distinct from the preceding crew restart actions.

## Supported simulation boundary

The source-backed chain is:

```text
restart eligibility established
        ↓
manual ullage attempted
        ↓
ENGINE START pushed
        ↓
Descent Engine Command Override ON
        ↓
engine-on command reaches DPS control path
        ↓
pilot valves commanded/open
        ↓
fuel/oxidizer shutoff valves commanded/open
        ↓
DPS physically re-ignites / resumes thrusting
```

The final physical-response step must remain separate from the command sequence. This allows future sourced scenarios in which the crew performs the correct procedure but the engine fails to respond.

## What is not supported precisely

The reviewed sources do **not** justify inventing:

- a PC+2-specific delay from START/override action to re-ignition;
- the exact order or milliseconds between START and override electrical effects;
- a chamber-pressure rise curve;
- the first post-restart `GQ6510P` value;
- an exact post-restart throttle percentage or ramp profile;
- an exact PC+2 controller-visible restart-confirmation threshold;
- guaranteed restart success.

The physical response therefore changes only the minimum vehicle state needed to represent successful re-ignition. Analog confirmation remains a later observation layer.

## Implementation consequence

`apply_engine_on_response(...)` is added alongside the existing engine-off response helper.

When explicitly invoked by a scenario/dynamics layer, it:

- records an engine-on discrete response;
- records pilot-valve and propellant-shutoff-valve opening response;
- sets `engine_running=True`;
- does **not** manufacture chamber pressure;
- does **not** invent a post-restart throttle phase;
- does **not** infer that the restart command succeeded merely because the crew performed the procedure.

The caller must supply the physical-response GET; the helper does not invent a delay.

## Architecture consequence

The restart path is now:

`rule/cause assessment → restart eligibility → CAPCOM/crew procedure → operational actions → physical engine-on response → later controller evidence`

This completes the principal command/response boundary needed before shifting emphasis from subsystem research to playable vertical-slice integration.

## Sources

Primary / mission-specific:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, PC+2 Mission Rules review.
- NASA Apollo 13 mission commentary / air-to-ground transcript around 76:31–76:37 GET.
- *Report of Apollo 13 Review Board*, Appendix B, contingency maneuver discussion.

Contemporary subsystem:

- Grumman/NASA, *Apollo Operations Handbook — Lunar Module*, LMA790-3-LM, GN&CS/MPS interface material, especially the descent-engine START/STOP → DECA → pilot-valve path.

## Research stop condition

The restart command/physical-response boundary is sufficiently documented for the current vertical slice. Do not pursue ignition milliseconds, pressure-rise curves, or exact post-restart throttle behavior unless a future scenario/player decision specifically requires them.

## Next project priority

After this boundary, shift from subsystem expansion to **first playable PC+2 integration**: define the minimum session loop, station views, controller interactions, communications, and scenario orchestration needed to exercise the already-researched nominal and nonnominal paths end-to-end.
