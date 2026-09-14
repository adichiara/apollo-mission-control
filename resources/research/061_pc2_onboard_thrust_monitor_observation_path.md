# Apollo 13 PC+2 — onboard 77-percent thrust-monitor observation path

Date: 2026-09-12  
Status: **SUPERSEDED IN PART BY NOTE 107 — this note correctly bounded the original gap; research note 107 later identifies the LM panel-1 CMD THRUST / ENG THRUST instrument family, with ENG THRUST as the source-backed actual-thrust percent scale. The exact PC+2 startup applicability gate remains unresolved.**

## Purpose

Research note 060 closed the first bounded inverter action/report loop. The next unresolved PC+2 rule was the crew-side thrust criterion:

> What onboard indication did the crew use for the “77 percent or below” thrust shutdown rule?

The project already had a separate ground chamber-pressure path (`GQ6510P`) for the 85-psi ground criterion. The onboard 77-percent rule could not be silently aliased to that ground product.

## 1. Mission-specific criterion

The Apollo 13 PC+2 Mission Rules review establishes two distinct thrust-performance criteria:

- ground: thrust chamber pressure approximately 85 psi;
- onboard: thrust approximately 77 percent.

The air-ground read-up at approximately 76:30 GET tells the crew to shut down for a **“thrust monitor readout, 77 percent or below.”** The crew readback repeats the **thrust monitor at 77 percent or below** criterion.

The Apollo 13 CONTROL/postflight material likewise summarizes the onboard criterion as **thrust <77 percent (onboard)** while preserving the ground propulsion-monitoring criteria separately.

Primary sources:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970.
- Apollo 13 technical/PAO air-ground transcript, approximately 76:30–76:38 GET.

## 2. P47 remains an unsupported mapping

Apollo LM guidance documentation includes **Program 47 — Thrust Monitor**.

However, the PC+2 burn was explicitly set up and executed in **P40**, the LM DPS powered-flight program. The mere existence of a program named “Thrust Monitor” therefore does not establish that the crew's “thrust monitor readout” in the PC+2 rule was a P47 display.

No reviewed source states that PC+2 switched to P47 or used P47 to generate the 77-percent indication.

Implementation consequence:

> Do not map the 77-percent criterion to P47.

## 3. Thrust-to-weight indicator remains a rejected mapping

The LM also carried a **thrust-to-weight indicator**. NASA technical material describes it as an accelerometer-based display calibrated in lunar-gravity / thrust-to-weight terms.

That establishes an onboard thrust-related instrument, but it is not the percent-thrust scale later identified in note 107.

## 4. Do not alias it to ground chamber pressure

The Mission Operations Report explicitly distinguishes:

- ground thrust-chamber-pressure criterion: approximately 85 psi;
- onboard thrust criterion: approximately 77 percent.

Research note 055 established the LM-7-family `GQ6510P` chamber-pressure measurement for the ground path. That evidence does not make `GQ6510P` the crew readout.

The simulator must preserve the two criteria as independent observations.

## 5. What the PC+2 engine chronology confirms

The CONTROL report provides the nominal engine profile:

- ignition at approximately 12.6 percent thrust;
- 40-percent segment;
- maximum-thrust segment;
- crew manually backed up the maximum-thrust portion.

This shows that crew awareness of thrust state was operationally important.

The 77-percent rule clearly cannot be applied indiscriminately during the commanded low-thrust startup segments. The reviewed rule wording does not yet provide enough detail to freeze the applicability transition during the 12.6/40-percent phases.

## 6. Superseding finding from research note 107

Later primary LM technical evidence identifies a **dual-scale CMD THRUST / ENG THRUST indicator on panel 1**. CMD displays commanded thrust; ENG displays actual engine thrust, with the ENG input derived from a combustion-chamber pressure transducer and expressed as percent thrust. Apollo 13 mission-specific malfunction procedures also use CMD THRUST / ENG THRUST indicator terminology.

Accordingly, the original question “what onboard instrument could provide the percent-thrust indication?” is now closed with high confidence to that instrument family, with **ENG THRUST** the source-backed actual-thrust scale.

The exact Apollo 13 mission-rule text still does not explicitly say “use the ENG pointer,” so note 107 labels that last step as a strong functional inference rather than a verbatim mission-rule mapping.

## 7. Current implementation decision

Historical representation may now name:

```text
crew ENG THRUST indication <= 77 percent
```

but the executable rule remains `NOT_EVALUABLE` until the model has a source-bounded crew observation/applicability state.

Do not introduce:

- a fabricated percent-thrust value from hidden engine state;
- a P47-derived readout;
- a thrust-to-weight conversion presented as percent thrust;
- a direct alias of ground chamber pressure;
- an invented time gate defining when the 77-percent criterion becomes active after startup.

## 8. Current research stop condition

The remaining bounded question is no longer instrument identity. It is:

> At what point in the PC+2 12.6-percent → 40-percent → maximum-thrust sequence did the 77-percent ENG THRUST shutdown criterion become applicable?

Defer that timing question unless a procedure source or implementation need makes it consequential.

## Sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970.
- Apollo 13 technical/PAO air-ground transcript, approximately 76:30–76:38 GET.
- Apollo LM guidance documentation identifying P40 (DPS) and P47 (Thrust Monitor) as distinct programs.
- NASA/Grumman LM operations documentation for the panel-1 CMD THRUST / ENG THRUST and T/W indicators.
- Apollo 13 LM Malfunction Procedures.
