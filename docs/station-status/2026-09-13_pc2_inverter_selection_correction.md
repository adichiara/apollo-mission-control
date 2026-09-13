# Station research status — PC+2 inverter selection correction

Date: 2026-09-13

## CONTROL / TELMU

**Status:** mission-specific pre-burn inverter identity corrected; exact ground presentation remains unresolved.

For PC+2, use inverter 2 as the selected pre-burn AC source. Apollo 13's mission-specific read-up explicitly closed the inverter-2 breaker and deleted `Select Inverter 1` from the stock procedure.

CONTROL/TELMU may reason from a represented inverter warning and crew-reported/procedural switch attempt, but the project still does not claim an exact Apollo 13 CRT field, telemetry word, independent switch-position indication, or post-switch persistence timer.

## CAPCOM

**Status:** rule wording remains source-backed.

CAPCOM's rule is still: shut down for an inverter light if it remains after the crew has tried switching inverters. The reviewed source does not name the alternate inverter in that contingency sentence. Do not embellish the call with a named inverter unless later primary evidence supports it.

## FLIGHT

**Status:** decision semantics unchanged.

A warning alone is insufficient. The positive criterion requires the switch attempt plus a continuing warning. Initial source identity is corrected from inverter 1 to inverter 2.

## Crew / scenario actor

**Status:** explicit action boundary retained.

Crew action remains a separately represented scenario event. Do not infer that the switch occurred from the warning itself, and do not invent a delay or a named inverter-1 selection step absent direct procedural evidence.

## Other stations

GUIDO, FIDO/RETRO, and INCO are unaffected by this correction.
