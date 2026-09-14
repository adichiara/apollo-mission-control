# Apollo 13 PC+2 — direct inverter-caution / selector telemetry boundary

Date: 2026-09-14  
Status: **REVIEWED / BOUNDED NEGATIVE FINDING — reviewed primary schematics establish telemetry for inverter-bus voltage/frequency but do not establish a direct PCM telemetry path for the derived `GL4046` INVERTER caution or the INV1/INV2 selector position. Do not model either as historical ground telemetry without stronger primary evidence.**

## Question

Research note 116 established a source-backed ground electrical-observation path for inverter-bus frequency `GC0155` and voltage `GC0071`. It deliberately left two narrower questions open:

1. Was the derived onboard INVERTER caution (`GL4046` / `6DS26`) itself directly telemetered to Mission Control?
2. Was the crew's INV1/INV2 selector position independently telemetered to the ground?

This pass asks whether the primary LM instrumentation schematics support either path.

## Primary evidence

### NASA TN D-6845 / MSC-S-294 — Lunar Module Instrumentation Subsystem

Figure 27, **Electrical power subsystem inverter voltage and frequency failure-detection circuit**, explicitly distinguishes the underlying electrical measurements from the derived caution and selection logic.

The figure shows:

- inverter-bus frequency measurement `GC0155` routed through an isolating buffer to **Telemetry PCMTEA GC0155**;
- inverter-bus voltage measurement `GC0071` routed through an isolating buffer to **Telemetry PCMTEA GC0071**;
- frequency/voltage failure-detection logic feeding relay driver `GL4046(C)` and onboard indicator `6DS26`;
- the INV 1 / INV 2 / OFF selector (`4S14`) participating in inverter selection and caution-inhibit logic.

The figure does **not** show a labeled PCMTEA telemetry tap from the `GL4046` caution output or from the `4S14` selector-position wiring.

The report's general instrumentation description confirms that LM measurements intended for ground transmission were prepared for PCMTEA and subsequent MSFN transmission, while caution/warning functions could be separate derived outputs.

Primary source: NASA, *Apollo Experience Report — Lunar Module Instrumentation Subsystem*, NASA TN D-6845 / MSC-S-294, June 1972, Figure 27 and instrumentation architecture.

### Apollo Operations Handbook cross-check

The LM subsystem handbook's inverter/caution diagrams independently identify the INVERTER caution logic and PCMTEA-related measurement paths. The reviewed material does not provide a separately named `GL4046` telemetry parameter or a selector-position telemetry discrete that would override the Figure-27 boundary.

This is a cross-check, not proof that no other Apollo document could contain an additional routing path.

## Interpretation

The reviewed primary schematics support three distinct information classes:

```text
selected inverter bus
      ↓
GC0155 frequency + GC0071 voltage
      ↓
PCMTEA / MSFN
      ↓
ground electrical evidence
```

```text
GC0155 / GC0071 failure-detection logic
      ↓
GL4046 caution output
      ↓
6DS26 onboard INVERTER indication
      ↓
crew observation / report
```

```text
crew selector / breaker action
      ↓
explicit crew-action state / report
      ↓
ground knowledge of which inverter was selected
```

Nothing in the reviewed primary schematics justifies collapsing these into a historical ground Boolean such as `inverter_caution_telemetered = true` or `selected_inverter = 1/2` from direct spacecraft telemetry.

## First-playable boundary

For the current PC+2 first playable:

- ground electrical evidence may use source-backed `GC0155` and `GC0071` values with validity/freshness semantics;
- the onboard INVERTER caution remains a crew-side indication unless a later primary source establishes a direct caution-discrete path;
- selector identity remains known through the explicit scenario-authored crew action/procedure/report path established in notes 112–115;
- a project-rendered derived electrical warning may be calculated from source-backed voltage/frequency limits only if it is clearly labeled as a **project-derived controller aid**, not a recovered Apollo 13 telemetered caution discrete;
- do not invent a selector telemetry word, direct `GL4046` ground indication, or exact TELMU/CONTROL field.

## Evidence limit

This is a **bounded negative finding**, not a universal proof of nonexistence.

The reviewed Figure-27 circuitry positively labels PCMTEA taps for `GC0155` and `GC0071` while not labeling equivalent taps for `GL4046` or selector position. That is sufficient to prevent the first playable from claiming those direct paths. A later mission-era telemetry assignment list, wiring drawing, CCATS routing record, or controller display source could supersede this boundary if it explicitly documents them.

## What remains unresolved

- exact Apollo 13 MSFN/CCATS routing of `GC0155` / `GC0071` to TELMU, CONTROL, or support-room products;
- exact CRT/MSK field, units/format, update cadence, and ground display latency;
- numeric inverter-selection caution-inhibit duration;
- whether another as-yet-unreviewed primary routing source documents a separate caution or selector discrete.

These remain archival refinements, not current physical-play blockers.

## Project consequence

The first-playable information boundary is now stronger than note 116 alone:

> **Use the sourced voltage/frequency telemetry for ground evidence; use explicit crew action/report for inverter identity and onboard caution persistence. Do not give Mission Control a direct caution or selector telemetry channel that the reviewed primary schematics do not establish.**

No station maturity grade changes and no physical-play PASS claim is added.

## Sources

1. David E. O'Brien III and Jared R. Woodfill IV, NASA Manned Spacecraft Center, *Apollo Experience Report — Lunar Module Instrumentation Subsystem*, NASA TN D-6845 / MSC-S-294, June 1972, especially Figure 27, “Electrical power subsystem inverter voltage and frequency failure-detection circuit.” NTRS: https://ntrs.nasa.gov/citations/19720018206
2. Grumman/NASA, *Apollo Operations Handbook — Lunar Module, Subsystems Data*, electrical-power / caution-and-warning inverter diagrams, used as a technical architecture cross-check.