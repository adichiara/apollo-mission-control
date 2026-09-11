# Decisions Log

Only decisions explicitly established for the project are recorded as accepted. Historical facts belong in research notes and should carry sources.

## D-001 — Research-first authenticity

**Status:** Accepted  
**Date:** 2026-09-11

Apollo-specific behavior will be researched from actual documentation before implementation. Missing historical details will not be invented silently.

## D-002 — Simplification is deferred

**Status:** Accepted  
**Date:** 2026-09-11

The real workflow/complexity is established first. Simplification decisions are made only afterward.

## D-003 — Simulator presentation, not game presentation

**Status:** Accepted  
**Date:** 2026-09-11

The experience may be played for enjoyment, but operational screens and workflow should feel like a simulator rather than a conventional game. Player enjoyment comes from role performance, teamwork, interpretation, decision-making, and communication.

## D-004 — Mission outcome priority

**Status:** Accepted  
**Date:** 2026-09-11

Primary goal: accomplish mission objectives.

If that becomes infeasible, controllers pursue the best valid alternate/contingency outcome, with safe return of the astronauts the ultimate priority.

Abort is phase- and condition-dependent, not a generic success mechanic.

## D-005 — In-person cooperative play

**Status:** Accepted  
**Date:** 2026-09-11

Players are intended to be physically together and communicate as a team.

## D-006 — One controller station per player

**Status:** Accepted in principle  
**Date:** 2026-09-11

Each player assumes responsibility for a Mission Control role/station. Role aggregation for low player counts is expected to be necessary but is **not yet designed**.

## D-007 — Phone-based station interface

**Status:** Accepted  
**Date:** 2026-09-11

Each player uses a phone as the station display/interface, connected to the live central simulation.

## D-008 — Physical controller documentation

**Status:** Accepted  
**Date:** 2026-09-11

Players use printed station documentation such as flight rules. Exact contents and amount of material remain to be determined from historical research and usability requirements.

## D-009 — Central authoritative simulation

**Status:** Accepted  
**Date:** 2026-09-11

A central server owns the live mission state. Player devices are station clients, not independent simulators.

## D-010 — Deployment target

**Status:** Accepted  
**Date:** 2026-09-11

Production deployment target is Render.

## Not yet decided

The following are deliberately not decisions:

- first Apollo mission/mission phase
- minimum player count
- exact controller combinations by player count
- exact technical stack
- degree of RTCC/CCATS/MSFN emulation
- degree of Staff Support Room simulation
- voice-loop implementation
- time acceleration
- scenario-selection UI
- post-simulation evaluation format


## D-011 — Represent documented hard-copy flow physically where practical

**Status:** Accepted in principle  
**Date:** 2026-09-11

Where Apollo information was historically delivered or verified as hard copy, the in-person simulation may represent that product with a physical paper sheet passed to the appropriate player.

This is an adaptation of the information-delivery mechanism, not a claim that controllers literally passed the same document hand-to-hand in the MOCR.

Exact document classes and delivery method remain scenario-specific and must be researched before implementation.
