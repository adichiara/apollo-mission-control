# Mission Profile Model

Status: **architecture concept grounded in documented mission-to-mission differences; first profile target selected**

## Purpose

The common simulation platform should support Apollo 11, Apollo 13, and potentially other lunar missions without falsely assuming that every MCC detail was identical.

The Apollo 13-era configuration is the default technical baseline/superset. A mission profile determines which portions are historically applicable to a given scenario.

## Current first profile target

Decision D-013 selects **Apollo 13 PC+2 preparation/execution** as the first vertical slice.

Working historical context:

- mission: Apollo 13 / AS-508 / CSM-109 / LM-7;
- docked CSM/LM configuration during the contingency return;
- context window approximately 74:00–80:00 GET;
- first playable start currently expected near 77:55–78:00 GET, pending final controller-action mapping;
- LM DPS PC+2 ignition at 79:27:38.30 GET;
- endpoint after burn verification and initiation of LM power-down.

The first mission profile should contain only the configuration/state required for this interval. It is not a requirement to encode every Apollo 13 mission difference before the vertical slice can run.

See `docs/scenarios/APOLLO13_PC2_VERTICAL_SLICE.md`.

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

### Known mission-specific conditions and quirks

Mission profiles may include conditions that were already known to NASA before or during the mission, such as:

- known spacecraft anomalies at launch
- accepted ground-system/display deficiencies
- documented software limitations
- established workaround procedures
- known instrumentation quirks
- configuration-specific redlines/constraints

These are **not scenario surprises**. They belong to the historical baseline known to the appropriate controllers/crew.

Examples already documented for Apollo 13 include:

- LM Look Angle Display MSK 1475 not operating from LM low-bit-rate telemetry
- known LUMINARY/COLOSSUS operational notes and restart behaviors
- known LM-7 preflight anomalies and configuration constraints

### Scenario state

- mission elapsed time
- nominal spacecraft state
- crew state
- ground/network state
- allowable historically sourced failure/scenario injections
- separation between baseline known conditions and hidden scenario injections

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

## Research-sufficiency rule

A mission profile does not require exhaustive knowledge of every historical configuration item.

For the selected scenario, unresolved profile details can remain explicitly deferred when they do not alter:

- player-visible information needed for the scenario;
- a controller decision or procedure;
- physical/system evolution;
- communication/action authority;
- validation of the historical event.

If implementation later exposes a dependency on a deferred item, research resumes at that point.

## Implementation timing

The categories above are now stable enough to guide the first scenario profile, but do not create a universal exhaustive schema solely to encode unused Apollo details.

The PC+2 parameter/action matrix should define the minimum profile fields actually needed for the first implementation. Broader schema generalization can follow once that slice has exercised the architecture.
