# Roadmap addendum — PC+2 inverter-switch identity correction

Date: 2026-09-13  
Status: **corrected archival refinement; physical-play priority unchanged**

## Correction in this pass

Research note 112 supersedes note 111's earlier first-playable identity synthesis.

The generic LM Operations Handbook says inverter 1 is normally selected for DPS/APS burns, but Apollo 13's mission-specific PC+2 read-up explicitly changed the stock procedure:

- close `CB(16) INVERTER 2` at the PC+2 -4 minute configuration step;
- **scratch out `Select Inverter 1`**.

Earlier in the mission sequence the crew had explicitly selected inverter 2 for LM AC use. The mission-specific PC+2 instruction therefore has priority over the generic handbook convention.

Current first-playable interpretation:

`PC+2 on inverter 2 → caution/light → attempt switch to redundant inverter → continuing light → shutdown criterion`

Do **not** encode a named inverter-2-to-inverter-1 post-warning transfer until a direct Apollo 13 procedure source confirms that action. Inverter 1 is the architecturally obvious redundant unit, but the recovered rule only says to try switching inverters.

## Remains deferred

- exact cockpit switch/breaker chronology after the warning;
- exact post-switch persistence/wait interval;
- explicit Apollo 13 post-warning naming of the redundant inverter;
- exact TELMU/CONTROL telemetry or CRT presentation;
- independent ground knowledge of switch position absent a crew/procedure report.

## Priority ordering

This correction does not displace the primary next work:

1. seven-seat nominal physical human/device run;
2. synthetic ΔP physical run;
3. approved five-player compact validation;
4. repair only concrete defects or historical dependencies exposed by those runs.

The correction prevents the first playable from preserving a generic handbook convention that Apollo 13's actual PC+2 procedure explicitly deleted.
