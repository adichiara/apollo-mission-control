# Apollo 13 PC+2 — observation age and freshness

Date: 2026-09-12  
Status: **IMPLEMENTED CONTRACT — no source-backed stale threshold found**

## Question

Do the Apollo 13 PC+2 shutdown rules or associated crew/ground procedures define a maximum age, repeat-confirmation interval, or other explicit freshness requirement for analog shutdown observations?

## Primary-source result

A targeted review of the strongest mission-specific sources did **not** identify an explicit time-based freshness threshold for the PC+2 analog criteria.

### Mission Operations Report — Apollo 13

The Flight Control Division postflight report records the PC+2 shutdown criteria at the 76+00 GET Mission Rules Review, including:

- ground thrust-chamber pressure 85 psi / onboard 77-percent thrust;
- ground inlet pressure 150 psi / onboard 160 psi;
- fuel/oxidizer delta-P >25 psi on a ground callout;
- attitude-error/rate limits;
- warning/light criteria.

The reviewed PC+2 section does not state that an analog value must have been sampled within N seconds, confirmed for N samples, or repeated before the rule is actionable.

### Contemporaneous air-ground rule transmission

At about 76:30 GET CAPCOM read the shutdown rules to the crew. The wording distinguishes ground-call criteria from onboard indications but supplies no age window, persistence requirement, or repeat-confirmation count for the analog values.

This is especially important for fuel/oxidizer delta-P: the source says it would require a ground call, but does not define a stale-data timeout for making that call.

### Apollo real-time display architecture

The Apollo Experience Report on the real-time display system confirms that controller information passed through distinct input, computation, and display subsystems. That supports retaining separate sample/receive/process/display times in the simulation. It does **not** establish a mission-specific PC+2 stale threshold for CONTROL observations.

### Postflight data-validity evidence

Apollo postflight data-management documentation explicitly discusses determining whether telemetry-derived data were valid or questionable. This supports keeping validity independent from value and age. It is not evidence for a real-time PC+2 controller timeout and is therefore not used to invent one.

## Implementation consequence

The simulator now distinguishes:

1. **observation time** — when the modeled measurement/product was actually observed or injected;
2. **projection/display time** — when a controller product is rendered/evaluated;
3. **observation age** — display/evaluation GET minus observation GET;
4. **validity** — valid/invalid/unavailable/etc.; and
5. **freshness policy** — deliberately unresolved unless a source defines one.

A carried-forward analog observation therefore retains its original observation timestamp. Projecting it later must **not** silently reset its source/sample time to the current simulation GET.

## Rule-evaluation policy

No automatic `STALE` classification is assigned merely because age is nonzero.

For currently modeled analog shutdown criteria:

- the rule audit records observation age;
- the numerical threshold can still be evaluated if the product is otherwise valid;
- no historical claim is made that Apollo would accept an indefinitely old value;
- future station/procedure evidence may add a source-backed freshness/persistence policy without changing the product timestamp model.

This is intentionally different from the inverter rule, whose mission wording itself requires a **distinct observation after** the switch action. That is an ordering/confirmation requirement derived from source wording, not a generic stale-data timeout.

## Corrected implementation issue

Before this pass, injected chamber-pressure and delta-P values were stored in state but the CONTROL projection stamped `source_time_get` and `sample_time_get` with the current state GET each time products were projected. A value injected at 79:29 and projected at 79:30 could therefore appear newly sampled.

The state now retains explicit observation timestamps for modeled analog values, and the projection layer uses those timestamps while allowing receive/process/display time to reflect the current projection point.

## Research stop condition

Do not continue broad archival searching solely for a generic PC+2 stale timeout. Re-open the question only if:

- a CONTROL procedure/display source directly specifies validity, persistence, or age behavior;
- a reconstructed malfunction depends materially on lost/frozen telemetry; or
- a mission-specific telemetry/display document becomes readily available.

## Sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970. PC+2 Mission Rules Review and shutdown criteria. https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- NASA Apollo 13 Technical/PAO Air-to-Ground Transcription, around 76:30 GET. https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- C. J. Sullivan and L. W. Burbank, *Apollo Experience Report: Real-Time Display System*, NASA-TN-D-8316 / JSC-S-461, 1976, NTRS 19760024152. https://ntrs.nasa.gov/citations/19760024152
- G. B. Foster, Jr., *Apollo Experience Report: Data Management for Postflight Engineering Evaluation*, NASA-TN-D-7684 / JSC-S-393, 1974, NTRS 19740015283. https://ntrs.nasa.gov/citations/19740015283
