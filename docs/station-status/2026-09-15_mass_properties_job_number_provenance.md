# Station-status addendum — H-2 mass-properties and PC+2 trim provenance

Date: 2026-09-15  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical station maturity grades are unchanged. Research notes 151–154 strengthen the Flight Dynamics/CONTROL workflow boundary rather than reconstructing a console display.

## FIDO / RETRO

**Evidence strengthened.** Apollo 13 documentation proves numbered mass-properties job identity through late-entry job 27, while PC+2's job remains unknown. The ~59-hour PC+2 angular GDA product was explicitly interim. Research note 154 corrects the later execution quantity: LM CONTROL's reported roll-GDA values are actuator displacement in **inches**, not degrees.

For simulation, Flight Dynamics products may carry sourced mass-properties job identity and lifecycle/finality state. Do not invent PC+2's job number or complete final angular trim.

## FLIGHT

No maturity change. The evidence demonstrates an operational chain in which an interim crew-facing angular trim is superseded before execution, but it does not establish what mass-properties metadata or final trim details were visible to FLIGHT.

## CONTROL

**Evidence strengthened; maturity unchanged.** CONTROL's stale-premission-mass-properties disagreement with Flight Dynamics remains the controlling ~59-hour provenance event. The later primary record separates angular trim from physical GDA displacement. The September 1970 Mission Report gives a postflight PC+2 actuator trace in inches, including initial pitch/roll `+0.13 / -0.28 in`, steady-state `-0.21 / -0.55 in`, and cutoff `+0.23 / -0.85 in`.

Represent commanded angular trim, actuator displacement, sampled/postflight actuator trace, and ignition compliance response separately. Do not derive degrees from inches without sourced GDA calibration.

## CAPCOM / crew interface

Workflow evidence remains strong. The ~59-hour pair was communicated as usable but explicitly update-expected. Axis wording in the exchange is inconsistent; project documentation should use `pitch 5.86° / roll 6.75°` or simply 'two DPS GDA angular values' rather than normalize the second value to yaw. Haise's accepted readback uses pitch/roll.

## RTCC/support boundary

Keep mass-properties job identity separate from `T+N` deck/reference epoch, generation time, input provenance, derived products, commanded angular trim, actuator displacement, postflight trace, compliance response, and product lifecycle. Job 27 remains late-entry only. PC+2's job number, complete final commanded angular trim, GDA angle/displacement calibration, and explicit `T+55` linkage remain unknown.

## Remaining PC+2 gap

Recover the final ~78-hour P30/GDA artifact or H-2 Flight Dynamics/CONTROL working record that gives the complete superseding angular trim pair and identifies its mass-properties job/run or `T+55` basis. A secondary target is LM GDA calibration/geometry documentation that can connect commanded angle to actuator inches.