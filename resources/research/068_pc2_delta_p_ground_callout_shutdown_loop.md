# Apollo 13 PC+2 — fuel/oxidizer ΔP ground-callout shutdown loop

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED — source-backed communication/action boundary; exact internal voice-loop routing and cockpit shutdown control remain unresolved**

## Question

How should the PC+2 rule `fuel/oxidizer ΔP > 25 psi` propagate from the ground-derived CONTROL product to the crew without inventing an onboard indication or an unsupported Mission Control approval sequence?

## Primary-source evidence

### Apollo 13 Mission Operations Report — 28 April 1970

The PC+2 Mission Rules review lists:

- `ΔP fuel/oxidizer greater than 25 psi (based on a ground call-out)`

as one of the maneuver shutdown criteria.

The same section separately states that an early shutdown for reasons **other than** the listed criteria was restart-eligible. Therefore a ΔP-triggered shutdown belongs to the rule-caused branch and must not flow into the generic restart branch.

### Apollo 13 Technical Air-to-Ground Voice Transcription — April 1970

NASA NTRS document 20160014370 preserves the mission technical air-to-ground transcript. The corrected transcript access copy at the Apollo Flight Journal records Vance Brand's PC+2 rules read-up at about 76:30 GET:

- fuel-to-oxidizer ΔP greater than 25 psi;
- this would have to be a **ground call** to the crew;
- the crew should shut down when one of the listed conditions occurred.

Fred Haise's readback explicitly confirms the same structure: ΔP >25 psi, ground callout, shutdown criterion.

## What is documented

The source supports this minimum causal/operational chain:

```text
ground-derived fuel/oxidizer ΔP product
        ↓
CONTROL threshold assessment (>25 psi)
        ↓
ground shutdown callout reaches crew
        ↓
crew commands DPS shutdown
```

It also supports:

- the crew did not have to derive this criterion from an onboard ΔP indication;
- exactly 25 psi is not over the limit; `>25` is the documented trigger;
- this is a listed shutdown criterion, so a resulting shutdown is not automatically restart-eligible.

## What is not documented sufficiently for this implementation

The reviewed sources do **not** establish:

- the exact ground computation/sign convention that produced the ΔP product;
- the exact CONTROL CRT field or update cadence;
- the exact controller-to-FLIGHT voice-loop wording/sequence used if the threshold were exceeded;
- whether FLIGHT would repeat/approve the call before CAPCOM transmitted it in this hypothetical branch;
- exact callout wording;
- the exact LM cockpit switch/button sequence the crew would use to shut down the DPS for this criterion;
- a historical occurrence of this ΔP exceedance during the nominal PC+2 burn.

Those details are not invented.

## Implementation boundary

Three separate event layers are used:

1. **Controller decision/audit** — CONTROL decides to call out the shutdown criterion after the modeled rule evaluator returns `TRIGGERED`.
2. **Procedural communication** — CAPCOM transmits a ground shutdown callout to the crew. CAPCOM is the modeled air-ground sender; this does not assert a detailed internal CONTROL→FLIGHT→CAPCOM chronology.
3. **Operational action** — the crew commands DPS shutdown. This records the crew action but does **not** directly set `engine_running=False` because physical engine response belongs to the vehicle model.

This preserves the project's rule that decisions, communications, commands, and physical response are separate.

## Synthetic validation case

A synthetic ΔP value of **26 psi** may be used to exercise the path because it is just beyond the documented >25 psi boundary. It is explicitly a test value, not a historical Apollo 13 measurement.

The expected software flow is:

```text
26 psi ground-derived product
→ shutdown rule TRIGGERED
→ CONTROL callout decision event
→ CAPCOM ground callout event
→ crew shutdown-command action
→ no automatic physical engine state change
```

At exactly 25 psi, the rule remains clear and no callout/action should be generated.

## Sources

Primary:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, PC+2 Mission Rules review, p. III-25 in the searchable NASA copy.
- NASA, *Apollo 13 Technical Air-To-Ground Voice Transcription*, April 1970, NTRS 20160014370.

Access/cross-check:

- Apollo Flight Journal, Day 4 Part 1, corrected transcript around 076:30 GET. This is used to locate/read the NASA transcript sequence; the historical claim is grounded in the NASA technical transcript and Mission Operations Report.

Repository context:

- `resources/research/058_pc2_fuel_oxidizer_delta_p_observation_path.md`
- `resources/research/053_pc2_shutdown_rule_evaluation.md`
- `resources/research/067_pc2_premature_shutdown_restart_branch.md`

## Research stop condition

The minimum decision/communication/action loop is now documented well enough to implement. Do not pursue exact CONTROL CRT routing, exact call wording, or cockpit shutdown-control archaeology unless a later interface or physical-response implementation requires it.

## Next target

After integrating and testing this loop, select the next PC+2 decision path that adds new information asymmetry or physical-response behavior rather than duplicating another threshold callout. A strong candidate is the separation between a crew shutdown **command** and verified engine shutdown/physical response, if primary DPS control sources can establish the response chain economically.
