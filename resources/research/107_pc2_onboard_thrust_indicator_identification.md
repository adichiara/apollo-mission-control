# Apollo 13 PC+2 — onboard thrust-indicator identification

Date: 2026-09-13  
Status: **REVIEWED / HIGH-CONFIDENCE IDENTIFICATION — the crew-side percent-thrust instrument is now constrained to the LM dual-scale CMD THRUST / ENG THRUST indicator, with the ENG scale the source-backed actual-thrust scale. The exact Apollo 13 mission-rule wording does not explicitly name the ENG pointer, so executable applicability timing remains unfrozen.**

## Purpose

Research note 061 left the Apollo 13 PC+2 crew criterion

> thrust monitor readout, 77 percent or below

`NOT_EVALUABLE` because the exact onboard percent-thrust display had not been identified.

This pass revisits that gap using primary mission and LM technical sources.

## 1. Mission-specific rule remains distinct from the ground chamber-pressure rule

Apollo 13 air-ground material at approximately 76:30 GET gives the crew a shutdown criterion of **“thrust monitor readout, 77 percent or below.”** Haise's readback repeats the threshold. The Flight Control Division Mission Operations Report separately summarizes the criterion as **thrust <77 percent (onboard)** and preserves the ground chamber-pressure criterion as a separate ground observation.

Therefore the onboard rule must remain a crew indication, not a direct alias of the ground `GQ6510P` product.

Primary sources:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970.
- Apollo 13 PAO/technical air-ground transcript, approximately 76:30–76:38 GET.

## 2. LM technical documentation identifies a percent-thrust instrument

The Apollo LM Operations Handbook describes a **dual-scale CMD THRUST / ENG THRUST indicator on panel 1**:

- CMD THRUST displays commanded manual/automatic thrust;
- ENG THRUST displays **actual engine thrust**;
- the ENG input is derived from a descent-engine combustion-chamber pressure transducer because thrust is proportional to chamber pressure;
- the ENG scale is explicitly expressed in percent thrust;
- at the fixed full-throttle position the ENG scale reads approximately **92.5 percent**, while the CMD scale may read 92.5–100 percent.

This is the first reviewed primary technical source that directly matches all of the essential properties required by the Apollo 13 rule wording: an onboard crew-visible indicator, a percent-thrust scale, and an actual-engine-thrust indication during a DPS burn.

## 3. Apollo 13 flight-data material confirms the indicator family existed in the mission configuration

The Apollo 13 LM Malfunction Procedures include the condition **“ENG THRUST and CMD THRUST ind do not agree”** in the CES/MPS malfunction material.

That mission-specific flight-data evidence is important because it confirms that CMD THRUST / ENG THRUST were not merely an earlier generic LM design feature; they were part of the Apollo 13 crew's operational malfunction vocabulary.

## 4. Interpretation of the 77-percent rule

The evidence now supports this interpretation with high confidence:

```text
Apollo 13 “thrust monitor readout”
    -> LM panel-1 CMD THRUST / ENG THRUST instrument family
    -> ENG THRUST scale for actual engine performance
```

Why ENG rather than CMD:

- the mission rule concerns whether actual DPS thrust has fallen below a shutdown limit;
- the LM handbook explicitly defines ENG as actual engine thrust and CMD as commanded thrust;
- the handbook treats disagreement between the two as evidence that the engine is not following the command;
- Apollo 13 malfunction procedures likewise treat CMD/ENG disagreement as a propulsion/control symptom.

This is a source-backed functional inference, not a verbatim Apollo 13 sentence saying “read the ENG pointer for the 77-percent rule.” The distinction should remain visible in the documentation.

## 5. P47 and thrust-to-weight indicator remain rejected mappings

The new evidence strengthens, rather than weakens, the earlier exclusions:

- **LGC P47** is a separate guidance-computer thrust-monitor program and is not established as the PC+2 burn-rule readout; PC+2 was executed in P40.
- **T/W indicator** is an acceleration/thrust-to-weight display in lunar-g units, not the identified percent-thrust scale.
- **ground `GQ6510P`** is a separate Mission Control chamber-pressure product, even though both the ground parameter and the ENG indication ultimately involve chamber-pressure sensing.

## 6. Startup applicability is still unresolved

PC+2 ignition was intentionally staged through approximately 12.6-percent and 40-percent thrust before the maximum-thrust portion. A literal 77-percent threshold cannot apply indiscriminately during those commanded low-thrust segments.

The reviewed material does not yet provide a mission-specific sentence defining the exact point at which the 77-percent shutdown rule becomes active.

Therefore this pass resolves the **instrument identity** but not the **applicability gate**.

## 7. Implementation consequence

Historical representation may now name the source as:

```text
crew ENG THRUST indication <= 77 percent
```

But the executable rule should remain `NOT_EVALUABLE` until the simulation has a source-bounded crew-observation/applicability state rather than fabricating a percent value or an activation time.

Do not:

- alias the crew indication to ground `GQ6510P` telemetry;
- synthesize an ENG THRUST percentage directly from hidden engine state without an authored observation path;
- apply the 77-percent threshold during the known 12.6/40-percent commanded startup segments;
- invent a transition time from 40 percent to “rule active” without evidence.

A later implementation can either receive an explicit scenario-authored crew ENG THRUST observation or model the actual indicator signal path if that becomes decision-relevant.

## 8. Research consequence

The prior question “what onboard display could show percent thrust?” is now closed to a high-confidence historical identification.

The remaining bounded question is narrower:

> When exactly did the 77-percent ENG THRUST shutdown limit become applicable during the PC+2 startup/max-thrust sequence?

That timing/applicability question remains deferred unless implementation or physical play requires it.

## Sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970.
- NASA Apollo 13 PAO/technical air-ground transcript, approximately 76:30–76:38 GET.
- Grumman, *Apollo Operations Handbook — Lunar Module, Subsystems Data*, DPS engine-control section describing the panel-1 dual-scale CMD THRUST / ENG THRUST indicator and ENG-scale chamber-pressure-derived actual-thrust indication.
- *Apollo 13 LM Malfunction Procedures*, Flight Data File, CES/MPS malfunction index and related DPS/CES malfunction material identifying CMD THRUST and ENG THRUST indications.
