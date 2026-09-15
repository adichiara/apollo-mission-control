# Station-status addendum — H-2 mass-properties and PC+2 trim provenance

Date: 2026-09-15  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical station maturity grades are unchanged. Research notes 151–153 strengthen the Flight Dynamics/CONTROL workflow boundary rather than reconstructing a console display.

## FIDO / RETRO

**Evidence strengthened.** Apollo 13 documentation proves numbered mass-properties job identity through late-entry job 27, while PC+2's job remains unknown. The ~59-hour PC+2 GDA product was explicitly interim. Research note 153 now proves that its second-axis value did not survive unchanged to execution: LM CONTROL reports a pre-ignition **roll GDA** of approximately `-0.8°` (derived from approximately `-2°` at ignition and a `-1.2°` change).

For simulation, Flight Dynamics products may carry sourced mass-properties job identity and lifecycle/finality state. Do not invent PC+2's job number or complete final trim.

## FLIGHT

No maturity change. The evidence now demonstrates an operational chain in which an interim crew-facing trim is superseded before execution, but it does not establish what mass-properties metadata or final trim details were visible to FLIGHT.

## CONTROL

**Evidence strengthened; maturity unchanged.** CONTROL's stale-premission-mass-properties disagreement with Flight Dynamics remains the controlling ~59-hour provenance event. The mission-specific LM CONTROL postflight report independently shows that by PC+2 ignition the roll-axis state was radically different from the earlier `6.75°` second-axis interim value. It also records the ignition compliance response: roll GDA moved to approximately `-2°`, `-1.2°` from its pre-ignition value.

Represent commanded trim, actual pre-ignition actuator state, and ignition compliance response separately.

## CAPCOM / crew interface

Workflow evidence remains strong. The ~59-hour pair was communicated as usable but explicitly update-expected. Axis wording in the exchange is inconsistent; project documentation should use `pitch 5.86° / roll 6.75°` or simply 'two DPS GDA values' rather than normalize the second value to yaw. Haise's accepted readback uses pitch/roll, and LM CONTROL's mission report refers to the corresponding DPS actuator as roll GDA.

## RTCC/support boundary

Keep mass-properties job identity separate from `T+N` deck/reference epoch, generation time, input provenance, derived products, commanded trim, actuator state, compliance response, and product lifecycle. Job 27 remains late-entry only. PC+2's job number, complete final commanded trim, and explicit `T+55` linkage remain unknown.

## Remaining PC+2 gap

Recover the final ~78-hour P30/GDA artifact or H-2 Flight Dynamics/CONTROL working record that gives the complete superseding trim pair and identifies its mass-properties job/run or `T+55` basis.