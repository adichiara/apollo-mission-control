# 139 — Apollo 13 PC+2 DPS performance boundary

## Question

What propulsion behavior is sufficiently documented to constrain a historical Apollo 13 PC+2 numerical validation case, and what remains unresolved before the Level-1 model can claim historical propulsion fidelity?

## Mission-specific primary evidence

### Apollo 13 Mission Operations Report — Flight Control Division

The Flight Control Division report gives the PC+2 commanded profile in operational terms:

- TIG: `079:27:38.30` GET;
- approximately 5 seconds at 12.6-percent thrust;
- approximately 21 seconds at 40-percent thrust;
- approximately 235 seconds at maximum thrust;
- actual total burn time reported by Flight Dynamics: `4:23.82` (263.82 s).

The spacecraft-systems narrative also records that the revised burn checklist called for closing DPS No. 1 REG SOV about 10 seconds before termination and that the engine entered blowdown for the final few seconds.

A later DPS maneuver narrative is important to model architecture even though it is not PC+2: high-speed analog data showed engine buildup from zero to 12.6 percent was slower than CONTROL had assumed. Flight Control compensated by planning an early shutdown. This establishes that startup transient behavior was operationally material and must not be silently equated with an instantaneous step to minimum thrust.

Source: NASA, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, MSC-02680.

### Apollo 13 Mission Report

The Mission Evaluation Team reports normal DPS engine starts and throttle response. For the transearth injection / PC+2 firing it states:

- duration approximately 264 seconds;
- approximately 15 seconds before engine shutdown, the pressurization isolation solenoid was closed;
- the maneuver was completed in **blowdown mode**, with residual helium as the sole pressure source.

This is stronger subsystem-performance evidence than a simple three-command throttle schedule because it establishes a distinct feed/pressurization condition during the terminal portion of the firing.

Source: NASA, *Apollo 13 Mission Report*, September 1970, MSC-02680.

### Apollo 13 Review Board baseline

The Apollo 13 vehicle baseline describes the descent engine as:

- throttleable from 1050 lbf to 6300 lbf;
- automatically at full thrust for throttle positions above that range;
- nominal full thrust: **9870 lbf**;
- gimbaled and restartable.

Source: *Report of Apollo 13 Review Board*, June 1970.

## General DPS design evidence — not mission calibration

NASA TN D-7143, *Apollo Experience Report — Descent Propulsion System*, gives fleet/design-level values and terminology including:

- maximum rated thrust: **10,500 lbf**;
- fixed throttle point nominally 92.5 percent of maximum rated thrust;
- minimum throttle point 10 percent of rated thrust;
- 65-to-92.5-percent thrust treated as a nonoperating region;
- design specific impulse at end of duty cycle: **305 lbf-sec/lbm**.

These values are useful engineering context. They are **not** yet established as the exact LM-7 PC+2 thrust or specific-impulse calibration.

## Important terminology/configuration boundary

The mission/configuration baseline value `9870 lbf nominal full thrust` is not numerically identical to the general design report's `10,500 lbf maximum rated thrust`, nor should the design fixed-throttle-point percentage be silently substituted for the Apollo 13 mission value.

Possible reasons include differing definitions, calibration, vehicle configuration, acceptance-test performance, or document conventions. No choice among those explanations is made here.

Likewise, the operational labels `12.6 percent`, `40 percent`, and `maximum thrust` are documented commands/conditions, but the exact LM-7 force-versus-time history and throttle-to-thrust calibration for PC+2 remain unresolved.

## DOCUMENTED for the PC+2 regression case

The historical validation fixture may safely carry:

- TIG `079:27:38.30` GET;
- actual burn duration `263.82 s` from Flight Dynamics;
- the staged operational throttle sequence;
- terminal blowdown as a real propulsion state, not a narrative label;
- Apollo 13 vehicle-baseline nominal full thrust of `9870 lbf`, explicitly labeled as nominal baseline rather than measured PC+2 thrust;
- the fact that startup buildup is non-instantaneous and can matter operationally.

## NOT YET DOCUMENTED WELL ENOUGH TO FREEZE AS NUMERICAL INPUTS

- measured LM-7 PC+2 thrust-versus-time history;
- exact time-dependent startup transient;
- exact transition behavior at 12.6, 40 percent, and maximum thrust;
- PC+2-specific effective specific impulse;
- throttle-dependent specific impulse / mixture ratio;
- exact propellant mass-flow history;
- exact chamber/feed-pressure decay during PC+2 blowdown;
- exact mapping between percent-thrust command terminology and delivered thrust on LM-7;
- whether `9870 lbf` should be used as a constant regulated full-thrust force in a historical propagator;
- PC+2-specific propellant consumption separated from the mission-wide DPS consumption totals.

## Consequence for the current numerical model

The existing Level-1 model remains valid as a **synthetic causal mechanics proof**. Its piecewise-constant thrust segments and run-wide constant specific impulse are not yet adequate to claim a historically validated PC+2 propulsion reproduction.

Historical integration should not be achieved by tuning one constant thrust and one constant Isp until the model happens to reproduce the documented ΔV.

Before historical validation, the propulsion input boundary should be able to represent, at minimum:

1. ignition/startup transient;
2. regulated commanded portions of the burn;
3. transition to terminal blowdown;
4. source-calibrated thrust/mass-flow behavior for those states, or an equivalent source-backed thrust history.

This does **not** require implementing detailed tank/helium thermodynamics now. It means the architecture must not preclude a distinct blowdown state or time-varying thrust history.

## Numerical consistency note

The operational profile rounded as 5 s + 21 s + 235 s totals 261 s, while Flight Dynamics reports an actual burn duration of 263.82 s. Those values come from different levels of reporting precision and must not be forced to sum by inventing an extra segment.

The Mission Report's 264 s is consistent with the Flight Dynamics value as a rounded duration.

## Named missing-source lead

Appendix E of the September 1970 *Apollo 13 Mission Report* lists **Apollo 13 Supplement 2 — Descent Propulsion System Final Flight Evaluation** with status **Preparation**.

Research note 140 closes the publication-status question: later official Apollo mission-report tables consistently record Apollo 13 Supplement 2 as **October 1970**. The source should therefore be treated as **published but currently unrecovered**, not merely planned.

Current public Apollo 13 document indexes reviewed in this pass expose Supplement 1 but not Supplement 2, and title-based NTRS searches did not recover a direct record.

## Next archival targets

Highest-value sources are now:

1. the published October 1970 Apollo 13 Mission Report Supplement 2, *Descent Propulsion System Final Flight Evaluation*, including its report identifier or archival copy;
2. LM-7 engine acceptance/calibration data relevant to thrust, mixture ratio, and Isp;
3. PC+2 high-speed propulsion telemetry or engineering plots;
4. detailed DPS pressurization/blowdown equations or simulator-model documentation that can be bridged to LM-7;
5. continued search for RTCC T+55 mass-property semantics, which remains an independent uncertainty.

Until those are recovered, keep the historical PC+2 validation target explicit but unfrozen.
