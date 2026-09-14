# Progress — PC+2 RTCC mass-property deck boundary

Date: 2026-09-14

## Completed

- Re-opened the numerical-validation queue after the deployed `dps-numerical-v2` synthetic suite passed.
- Verified in the Apollo 13 Flight Control Division Mission Operations Report that RTCC LM-burn mass-property decks were updated to **T+55 decks**.
- Verified that a PC+2 DPS trim disagreement was traced to LM Control using **premission mass properties**, which the report states were not the best data available.
- Recorded the stronger historical boundary in research note 138 and the PC+2 weight source catalog.

## Consequence

The project can now say that PC+2 Flight Dynamics calculations relied on an **in-flight updated mass-properties basis**, not merely premission values.

The project still cannot equate the final PAD weights (62480 lb CSM + 33452 lb LM) with exact physical mass at PC+2 TIG.

## Next

Continue the numerical-input queue by locating documentation for the Apollo RTCC mass-properties program / T+55 deck semantics. If that cannot close the epoch convention, proceed to LM-7 DPS thrust/throttle and propellant-performance extraction while retaining the mass uncertainty explicitly.
