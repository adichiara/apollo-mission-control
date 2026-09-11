# Mission Profile Model

Status: **architecture concept grounded in documented mission-to-mission differences**

## Purpose

The common simulation platform should support Apollo 11, Apollo 13, and potentially other lunar missions without falsely assuming that every MCC detail was identical.

The Apollo 13-era configuration is the default technical baseline/superset. A mission profile determines which portions are historically applicable to a given scenario.

## Profile categories

A mission profile will eventually need to specify, from historical evidence:

### Mission identity

- mission
- launch vehicle / spacecraft numbers
- mission dates
- relevant configuration revision
- selected mission phase

### Controller organization

- active positions
- period-appropriate call signs
- responsibility differences
- staffing/shift organization where it matters

### Ground system

- RTCC software/configuration
- CCATS/MSFN configuration
- available display/control capabilities
- network stations and mission-specific support differences

### Station configuration

For every controller position:

- console nomenclature
- available display formats
- display request mechanism
- event/limit indications
- command capabilities
- voice-loop access
- applicable backroom/support relationship

### Spacecraft configuration

- CSM/LM configuration
- instrumentation
- telemetry parameter availability
- onboard software/configuration
- subsystem differences

### Documentation

- flight rules
- console procedures
- Flight Control Operations Handbook procedures
- flight plan/timeline
- mission-specific reference tables

### Scenario state

- mission elapsed time
- nominal spacecraft state
- crew state
- ground/network state
- allowable historically sourced failure/scenario injections

## Inheritance rule

The technical implementation may inherit from the Apollo 13-era common baseline for convenience, but **historical presentation does not inherit blindly**.

A feature is enabled for another mission only when:

1. it is documented for that mission, or
2. there is sufficient evidence that the configuration was unchanged and applicable.

If neither condition is met, mark the feature unresolved rather than assume backward compatibility.

## Known example

- Apollo 11: **TELCOM**
- Apollo 13: **TELMU**

This difference is small in software terms but important as a test of the profile system: visible historical terminology should be scenario-specific even when the underlying station engine is shared.

## Implementation timing

This document defines the data categories only.

Do not create a complete JSON/schema yet. The fields should stabilize after at least several stations have been reconstructed from documentation; otherwise the schema itself would encode assumptions made too early.
