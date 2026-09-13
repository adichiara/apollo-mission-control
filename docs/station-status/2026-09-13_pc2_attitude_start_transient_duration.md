# Station research status — PC+2 attitude start-transient duration

Date: 2026-09-13

## Affected stations

### CONTROL

**Status:** operational rule allocation source-backed; exception timing unresolved.

The contemporaneous crew-facing PC+2 rule remains ±10-degree attitude error except during the start transient. Targeted propulsion research now shows that Apollo DPS engineering used “start transient” for a short engine-start phenomenon measured in seconds, but no reviewed Apollo 13 operational source defines the exact exception duration/end condition.

CONTROL therefore must not receive an invented numeric transient gate. If an attitude-error excursion depends on that exception, its historical rule disposition remains `NOT_EVALUABLE` unless a future Apollo 13-specific source resolves the timing.

### CAPCOM

**Status:** wording source-backed; no timing added.

CAPCOM’s 76:30 GET transmission and Haise’s readback remain the controlling first-playable evidence for which criterion carries the exception. The simulator/reference material must not silently add a duration that CAPCOM did not transmit in the recovered record.

### FLIGHT

**Status:** no new authority or decision rule.

FLIGHT may act on sourced CONTROL/GUIDO evidence, but the research does not create a new automatic shutdown condition or authorize a guessed startup-exception timer.

### GUIDO

**Status:** no change to attitude/rate observation boundary.

The research concerns rule applicability, not the provenance or cadence of GUIDO/CONTROL attitude products. Existing information-boundary rules remain unchanged.

## Simulation consequence

- Do not treat the exception as lasting through burn +26 s.
- Do not substitute Apollo 14’s 2.14 s measured transient or 4.0 s specification as an Apollo 13 rule duration.
- Preserve `NOT_EVALUABLE` when an exception-dependent synthetic attitude excursion is introduced without an explicit synthetic timing boundary.
- Nominal PC+2 remains unaffected because no sourced nominal excursion requires resolving the exception duration.

See research note 110 and `resources/source-catalog/PC2_ATTITUDE_SOURCES.md`.
