# Research Note 001 — MCC High-Level Structure

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Question

What historically documented high-level structure should constrain the software architecture before detailed role research?

## Findings

### Mission Control data flow

NASA Apollo-era documentation describes the Mission Control Center at the Manned Spacecraft Center as the focal point for Apollo flight-control activities.

Tracking and telemetry were received from the Manned Space Flight Network, processed through the MCC Real-Time Computer Complex, and displayed to flight controllers in the Mission Operations Control Room and adjacent staff-support rooms.

This immediately argues against a software design in which each player client reads arbitrary authoritative spacecraft variables directly.

### MOCR organizational grouping

The same documentation states that MOCR console positions fell into three basic operations groups:

1. mission command and control
2. systems operations
3. flight dynamics

This is a documented organizational grouping. It should be used as a research framework, not yet as a player-role grouping.

### Support-room structure

The historical sources explicitly distinguish the MOCR from adjacent staff-support rooms. Therefore the front-room controller role cannot be understood only from the visible console. Detailed role research must include the specialists/support rooms feeding that console.

## Architecture consequence

The current software architecture separates:

- physical mission state
- instrumentation/telemetry
- communications/ground processing
- controller-accessible information
- controller display

This is a **project software architecture decision informed by the historical information flow**, not a claim that Apollo software used these exact module boundaries.

## Sources

1. *Apollo 13 Third Lunar Landing Mission Press Kit*, NASA release 70-50K,
   April 2, 1970 (NTRS 19760066779):
   https://ntrs.nasa.gov/api/citations/19760066779/downloads/19760066779.pdf

2. MCC Display Formats Manual:
   https://ntrs.nasa.gov/citations/19730010501

## Unresolved

- Detailed CCATS/RTCC/display-system boundaries need primary technical documentation.
- Exact front-room/backroom relationships need mission/era-specific research.
