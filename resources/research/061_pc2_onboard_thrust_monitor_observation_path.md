# Apollo 13 PC+2 — onboard 77-percent thrust-monitor observation path

Date: 2026-09-12  
Status: **REVIEWED-PARTIAL / DEFERRED — mission-specific criterion is established, but the exact onboard percent-thrust display/source has not been identified strongly enough to implement.**

## Purpose

Research note 060 closed the first bounded inverter action/report loop. The next unresolved PC+2 rule is the crew-side thrust criterion:

> What onboard indication did the crew use for the “77 percent or below” thrust shutdown rule?

The project already has a separate ground chamber-pressure path (`GQ6510P`) for the 85-psi ground criterion. The onboard 77-percent rule must not be silently aliased to that ground product.

## 1. Mission-specific criterion

The Apollo 13 PC+2 Mission Rules review establishes two distinct thrust-performance criteria:

- ground: thrust chamber pressure approximately 85 psi;
- onboard: thrust approximately 77 percent.

The air-ground read-up at approximately 76:30 GET tells the crew to shut down for a **“thrust monitor readout, 77 percent or below.”** The crew readback repeats the **thrust monitor at 77 percent or below** criterion.

The Apollo 13 CONTROL/postflight material likewise summarizes the onboard criterion as **thrust <77 percent (onboard)** while preserving the ground propulsion-monitoring criteria separately.

Primary sources:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970.
- Apollo 13 technical/PAO air-ground transcript, approximately 76:30–76:38 GET.

## 2. Do not equate the wording with LGC Program 47

Apollo LM guidance documentation includes **Program 47 — Thrust Monitor**.

However, the PC+2 burn was explicitly set up and executed in **P40**, the LM DPS powered-flight program. The mere existence of a program named “Thrust Monitor” therefore does not establish that the crew's “thrust monitor readout” in the PC+2 rule was a P47 display.

No reviewed source in this pass states that PC+2 switched to P47 or used P47 to generate the 77-percent indication.

Implementation consequence:

> Do not map the 77-percent criterion to P47 without a direct mission/crew-procedure source.

## 3. Do not equate it with the thrust-to-weight indicator

The LM also carried a **thrust-to-weight indicator**. NASA technical material describes it as an accelerometer-based display calibrated in lunar-gravity / thrust-to-weight terms.

That establishes an onboard thrust-related instrument, but it does not establish a percent-thrust scale or a 77-percent threshold presentation.

Therefore the project must not convert the PC+2 77-percent criterion into a thrust-to-weight-indicator threshold without a sourced conversion/procedure showing that this was the intended readout.

## 4. Do not alias it to ground chamber pressure

The Mission Operations Report explicitly distinguishes:

- ground thrust-chamber-pressure criterion: approximately 85 psi;
- onboard thrust criterion: approximately 77 percent.

Research note 055 established the LM-7-family `GQ6510P` chamber-pressure measurement for the ground path. That evidence does not make `GQ6510P` the crew readout.

The simulator should preserve the two criteria as independent observations unless a primary source later establishes a direct instrument relationship.

## 5. What the PC+2 engine chronology confirms

The CONTROL report provides the nominal engine profile:

- ignition at approximately 12.6 percent thrust;
- 40-percent segment;
- maximum-thrust segment;
- crew manually backed up the maximum-thrust portion.

This shows that crew awareness of thrust state was operationally important, but it still does not identify the exact 77-percent onboard display or its signal path.

The 77-percent rule also clearly cannot be applied indiscriminately during the commanded low-thrust startup segments. The reviewed rule wording does not yet provide enough detail to freeze the applicability transition during the 12.6/40-percent phases.

## 6. Current implementation decision

Keep:

```text
crew_thrust_monitor <= 77 percent
```

as `NOT_EVALUABLE`.

Do not introduce:

- a fabricated percent-thrust crew gauge;
- a P47-derived readout;
- a thrust-to-weight conversion presented as percent thrust;
- a direct alias of ground chamber pressure;
- an invented time gate defining when the 77-percent criterion becomes active after startup.

## 7. Research stop condition

Further searching for the exact onboard percent-thrust readout is deferred unless one of the following becomes readily available:

- Apollo 13 LM-7 contingency/activation checklist page naming the readout;
- LM-7 crew-station/panel documentation explicitly identifying a percent-thrust display;
- a mission-era DPS/controls handbook mapping a crew percent-thrust indication to a sensor/signal;
- training/mission procedure explicitly applying the 77-percent rule to a named display.

The source gap is now specific enough that broader searching is lower value than moving to the next PC+2 rule family.

## 8. Next research item

Proceed to the **attitude-error / attitude-rate shutdown criteria**, focusing first on the source conflict:

- Mission Operations Report: start-transient exception is attached to the rate criterion;
- crew-facing air-ground read-up/readback: start-transient exception is attached to attitude error.

The next pass should determine whether additional primary flight-rule/procedure material resolves that difference before either criterion is made executable.

## Sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970.
- Apollo 13 technical/PAO air-ground transcript, approximately 76:30–76:38 GET.
- Apollo LM guidance documentation identifying P40 (DPS) and P47 (Thrust Monitor) as distinct programs.
- NASA technical documentation for the LM thrust-to-weight indicator, describing an acceleration/thrust-to-weight display rather than a percent-thrust readout.
