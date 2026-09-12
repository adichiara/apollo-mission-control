# Apollo 13 PC+2 — ullage and throttle-profile implementation research

Date: 2026-09-11  
Status: **REVIEWED — sufficient for the first nominal command/event model; detailed engine-response dynamics remain deferred.**

## Purpose

Resolve the next implementation question for the PC+2 vertical slice:

> What exact pre-ignition ullage and commanded DPS throttle sequence should the nominal event model use, and how should that be distinguished from crew voice reports and postflight engine-response detail?

## Primary-source findings

### Final PC+2 maneuver PAD / air-to-ground record

The Apollo 13 technical air-to-ground record gives the final P30 LM maneuver PAD beginning at 77:55:24 GET. Its comments specify:

- ullage: **two jets for 10 seconds**;
- DPS throttle profile: **5 seconds at minimum, 21 seconds at 40 percent, remainder at maximum**;
- TIG: **79:27:38.30 GET**.

The earlier contingency-checklist update also instructs **Manual Ullage at minus 10 seconds** and **TTCA to 40 percent at plus 5 seconds**.

For the first nominal event model this supports the following commanded/procedural milestones:

| Event | Derived GET | Basis |
|---|---:|---|
| manual two-jet ullage begins | **79:27:28.30** | TIG − 10 s |
| DPS ignition / minimum-thrust segment begins | **79:27:38.30** | final PAD TIG |
| command 40 percent | **79:27:43.30** | TIG + 5 s |
| command maximum thrust | **79:28:04.30** | 21 s after entry to 40-percent segment |

These are procedure/command events. They are not asserted to be exact physical engine-response transition times.

### Crew voice reports are later communication events

The air-ground chronology records:

- 79:27:51 — Lovell reports, “We're burning, 40 per cent.”
- 79:28:09 — Lovell reports, “One hundred per cent.”

Those timestamps lag the corresponding commanded profile milestones and therefore reinforce the project rule that crew reports must remain a separate information channel rather than being used as exact physical transition timestamps.

### Postflight propulsion analysis

NASA TM X-66935 / REPT-70-FC13-47-ADD-1, *Analysis of Apollo 13 lunar module systems during emergency operation following command service module oxygen tank explosion*, provides a more detailed postflight DPS-2 engine profile: low-throttle operation, a ramp from low throttle to 40 percent, a 40-percent interval, and maximum-thrust operation.

The indexed report text gives rounded segment durations that do not sum exactly to the higher-precision Mission Operations Report burn duration/cutoff values used elsewhere in the project. It also presents a burn start time that differs from the final maneuver TIG used by the Flight Control Division report.

Therefore this source is valuable for later engine-response modeling but should **not** replace the final PAD/Mission Operations Report timing contract in the first event-driven nominal prototype without reconciling the differing timing conventions and rounding.

## Implementation decision

For the first executable nominal model:

1. Represent **ullage start** and the three **commanded throttle phases** explicitly.
2. Derive their event times from the final source-backed TIG and PAD/checklist timing.
3. Keep the crew 40-percent and 100-percent reports as separate communication events.
4. Continue using the Mission Operations Report actual guided cutoff (**79:32:02.12 GET**) as the physical/guidance validation target.
5. Do not yet model the detailed DPS throttle ramp or physical engine lag from the postflight propulsion report.

This preserves the difference between:

```text
crew procedure / throttle command
        ↓
engine physical response
        ↓
telemetry / onboard indications
        ↓
crew report / ground interpretation
```

## Research stop condition

Detailed DPS response dynamics become an active research target only when one of these is required:

- thrust/chamber-pressure transient simulation;
- a failure case during throttle transition;
- controller decisions dependent on exact ramp timing;
- propulsion physics sufficiently detailed that the rounded postflight profile must be reconciled with high-precision cutoff timing.

Until then, the source-backed command/event sequence is sufficient and avoids unsupported interpolation.

## Sources

Primary:

- Apollo 13 Technical Air-to-Ground Voice Transcription, PC+2 preparation and execution interval; NASA transcript preserved in the Apollo 13 Flight Journal document collection. Navigation page: https://www.apollojournals.org/afj/ap13fj/13day4-leaving-moon.html
- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970; authority for the high-precision TIG/burn-duration/cutoff validation values already recorded in research note 050.
- NASA TM X-66935 / REPT-70-FC13-47-ADD-1, *MSC Apollo 13 investigation team. Panel 3 — Flight operations and network, addendum 1 Final report: Analysis of Apollo 13 lunar module systems during emergency operation following command service module oxygen tank explosion*, June 1970. NTRS ID 19710010487: https://ntrs.nasa.gov/citations/19710010487

Secondary navigation/commentary:

- Apollo 13 Flight Journal, Day 4 Part 2, used to locate the underlying air-ground chronology and distinguish commentary from transcript material.
