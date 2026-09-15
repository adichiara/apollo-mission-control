# Measurement / Output Mapping Model Proof

## Purpose

This model proof makes an explicit reusable boundary between authoritative
simulator state and exposed measurements:

```text
source/model state
    -> measurement/output definition
    -> exposed value + availability + validity
    -> later telemetry/ground/controller processing
```

The implementation is mission-neutral. It is not an Apollo 13 telemetry
configuration, an LMS channel inventory, or a reconstruction of a historical
console directory.

Implementation: `src/apollo_mission_control/measurement_output_model.py`

Unit tests: `tests/test_measurement_output_model.py`

## Historical architecture basis

Research note 217 records direct indexed text from the 13 August 1971
**LMS Console Directory** showing that the LMS maintained an explicit
measurement/output dictionary. The indexed definitions include fields for
measurement identity/description, input-data source, analog range or fixed
value, event information, telemetry/output routing metadata, and spacecraft
effectivity. The same source also documents telemetry-console malfunction
handling as behavior associated with exposed channels rather than simply
another name for hidden source state.

Research note 215 independently records Apollo Mission Simulator evidence that
telemetry faults were separable from spacecraft-system faults. Together these
sources support a reusable architecture in which an observation/output channel
can fail without mutating the physical or subsystem state that feeds it.

These sources constrain the **architecture**, not the mission-specific data
loaded into it.

## Generic contract

A `MeasurementDefinition` declares:

- an inspectable measurement identifier and description;
- representation kind: analog or event;
- source selection: named source variable or explicit fixed value;
- units for analog values;
- optional profile effectivity;
- provenance.

`evaluate_measurement_outputs()` reads an authoritative source mapping and
produces `MeasurementOutput` records. It does not modify the source mapping.

The generic proof deliberately supports only two source modes:

- **variable** — read an explicitly named source variable;
- **fixed** — expose an explicitly configured fixed value.

Additional historical source modes should be added only when their semantics
are established well enough to implement without guessing.

## Effectivity

Definitions may carry `applicable_profiles`. If a measurement is not
applicable to the active profile, the output is explicitly:

- not applicable;
- unavailable;
- invalid;
- value withheld.

The generic layer does not decide which Apollo spacecraft or mission profile a
measurement belongs to. Historical effectivity must come from the applicable
mission/vehicle configuration evidence.

An empty effectivity tuple means the caller has not restricted the generic
definition; it must not be interpreted as a historical claim that a channel
existed on every Apollo vehicle.

## Output-layer malfunction boundary

A `MeasurementFault` can explicitly change:

- measurement availability;
- measurement validity;
- the exposed replacement value.

Fault application occurs after the source value is selected. It therefore
cannot mutate the upstream source/model state.

For example:

```text
source variable = 10.0
telemetry/output fault replacement = 99.0, invalid

authoritative source remains 10.0
exposed measurement becomes 99.0 and invalid
```

If a fault makes the measurement unavailable, its exposed value is withheld
and it is marked invalid.

This is a generic causal insertion surface. `MeasurementFault` is **not** a
claim about a historical LMS malfunction code or exact instructor-console
behavior.

## Type boundary

The model currently distinguishes:

- **analog** — finite numeric value with an explicit unit;
- **event** — Boolean state with no unit.

The implementation rejects implicit event/numeric coercion. A Boolean cannot
silently become an analog 0/1 value, and numeric 0/1 cannot silently become an
event.

This is a project type-safety choice, not a claim about historical PCM encoding.

## Deliberately not implemented

The current proof does **not** implement:

- Apollo measurement IDs or channel numbers;
- Apollo 13 H-2 / LM-7 measurement membership;
- historical telemetry scaling or quantization;
- PCM encoding, word/bit placement, or sampling cadence;
- console dial/event-bit routing;
- mission-specific display routing;
- redundant or multi-redundant channel selection/combining;
- historical LMS malfunction-code semantics;
- telemetry transmission or ground processing;
- controller diagnosis or operational decisions.

Research note 217 explicitly leaves the exact redundant-channel malfunction
consequence wording unresolved because the full scanned page was not reliably
reviewable in that research pass. This model therefore does not invent a
redundancy rule.

## Apollo 13 integration gate

The reusable layer may accept a historical Apollo 13 measurement only after
mission/vehicle-specific evidence establishes the relevant mapping and
effectivity. The 1971 LMS Console Directory is later than Apollo 13 and must not
be used by itself to claim that a listed channel, identifier, or routing
existed for Mission H-2.

The expected integration path remains:

```text
Apollo 13 source/subsystem state
    -> H-2 / LM-7 sourced measurement definition
    -> telemetry/output state
    -> sourced ground/interface processing
    -> controller-visible product
```

No historical channel is added merely to demonstrate the generic engine.

## Validation

The unit suite verifies that:

1. variable and fixed mappings are explicit and inspectable;
2. profile effectivity can withhold an inapplicable measurement;
3. an output fault can alter a measurement without modifying source truth;
4. unavailable measurements suppress their values;
5. missing source variables and unknown fault targets fail explicitly;
6. ambiguous source/type definitions fail validation;
7. duplicate definitions/faults/effectivity entries fail validation;
8. analog and event values are not silently coerced.

The public model-proof API and Causal Model Lab surface are intentionally
deferred from this change while pull request #83 owns their shared files. They
can be wired to this reusable model after that branch lands, without changing
the domain contract.

## Evidence and implementation status

**Model status:** generic architecture proof; not historically validated.

Architecture evidence:

- research note 215 — AMS model partition and malfunction-insertion boundaries;
- research note 217 — LMS Console Directory output/telemetry boundary.

Historical configuration remains profile-specific and source-gated.
