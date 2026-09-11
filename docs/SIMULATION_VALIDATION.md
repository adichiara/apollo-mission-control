# Simulation Validation Strategy

Status: **research-derived architecture; implementation deferred**

The simulator should be validated in layers. This structure is based on the Apollo 13 Flight Software Readiness Review, FMES testing, and NASA simulator-operations practice.

## 1. Component / source fidelity

Verify that individual modeled components reproduce documented behavior for the applicable mission configuration.

Examples:

- telemetry range/accuracy;
- sensor/transducer behavior;
- fuel-cell or battery response;
- RCS valve/thrust behavior;
- AGC restart state;
- display update timing;
- RTCC processor calculations.

## 2. Subsystem closed-loop validation

Verify dependent components together.

Examples:

- jet command → valve/control state → thrust → vehicle rate → telemetry;
- DPS throttle → engine response → vehicle dynamics → guidance state;
- antenna geometry → link margin → telemetry/command availability;
- electrical load → current → heat/water/resource consequences.

The Apollo LM FMES architecture is particularly relevant here.

## 3. Onboard-computer / RTCC integration

Apollo 13 readiness testing explicitly exercised onboard guidance software against ground RTCC products.

Examples included:

### CSM

- translunar MCC;
- LOI;
- DOI;
- CMC command loads;
- REFSMMAT cases;
- alignments;
- entry.

### LM

- APS/DPS aborts;
- LGC command loads;
- CSI/CDH/TPI;
- P57 alignments.

The project should eventually validate the full chain:

```text
RTCC product
   ↓
uplink / crew load
   ↓
onboard computer
   ↓
spacecraft response
   ↓
telemetry
   ↓
ground reconstruction
```

## 4. Procedure validation

Run documented Apollo procedures against the simulated system and confirm that:

- required information is available;
- required actions are possible;
- timing is credible;
- documented decision branches remain meaningful.

## 5. Boundary / anomaly validation

Use historical readiness and engineering tests to validate cases such as:

- radar acquisition/reasonableness failures;
- slow engine starts;
- propulsion transients;
- AGC restart cases;
- abort transitions;
- sensor/indication discrepancies;
- communications degradation.

These are engineering validation cases, not automatically playable scenarios.

## 6. Integrated controller simulation

Only after lower layers are established should an integrated SimSup/controller scenario be considered historically validated.

At this level:

- several controller disciplines operate simultaneously;
- communication loops matter;
- faults propagate through real dependencies;
- players see only historically available information;
- procedures/rules/crew workload interact.

## Validation status vocabulary

Use:

- **VALIDATED**
- **VALIDATED WITH DOCUMENTED LIMITATION**
- **UNRESOLVED**
- **KNOWN MODEL DEVIATION**

A known deviation should state:

- historical behavior;
- project behavior;
- reason;
- affected scenarios.

## Regression testing

When implementation begins, objectively documented behavior should become automated regression tests wherever practical.

Examples:

- EECOM one-second display update;
- known telemetry conversion/range;
- Apollo 13 MSK 1475 low-bit-rate deficiency;
- LGC P27/update behavior;
- known program-note restart consequence;
- published RTCC processor case;
- LM-7 configuration-specific measurement/limit case.

## Primary sources

- Apollo 13 Flight Software Readiness Review:
  https://www.ibiblio.org/apollo/Documents/apollo_13_fsrr_minutes.pdf
- Apollo 13 FMES test material:
  https://www.ibiblio.org/apollo/Documents/apollo_13_fmes_tests.pdf
- NASA MSC Simulator Operations:
  https://www.ibiblio.org/apollo/Documents/msc_simulator_operations.pdf
