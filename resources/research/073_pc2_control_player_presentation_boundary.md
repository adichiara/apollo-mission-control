# Apollo 13 PC+2 — first-pass CONTROL player presentation boundary

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED-PARTIAL — minimum project-rendered CONTROL view defined from mission-specific Apollo 13 display evidence; exact historical CRT reconstruction remains explicitly unclaimed**

## Question

How can the first playable PC+2 slice present CONTROL's already-modeled information without either inventing a historical CRT layout or discarding the documented Apollo display structure?

## Primary-source basis

### Apollo 13 Guidance & Navigation Summary — ASPO 45 CRT Displays

The mission-specific AC Electronics Apollo 13 *Guidance & Navigation Summary* directly documents:

- **MSK 1123 — LM GUID, CONTROL AND PROP RT** (layout ASPO-8 / PDF 186; definitions ASPO-9 / PDF 187);
- **MSK 1137 — LM powered-descent/control display** (layout ASPO-10 / PDF 188; definitions ASPO-11–12 / PDF 189–190).

Earlier project inspection was performed against rendered page images because the 244 MB scan was not usable through normal text extraction. The surviving source proves the display families, labels, units, and broad layout, but it does not prove that every product currently modeled for PC+2 belongs on one specific screen or at one exact field coordinate.

MSK 1137 is especially relevant to a burn-monitor view. Its documented fields include throttle selection/commands, variable-actuator position, LGC thrust command, chamber pressure, guidance/control error and rate quantities, DAP/control state, gimbal direction, warnings, and timing/context fields.

### Important unit/semantic boundary: TCP

Apollo 13 MSK 1137 defines **TCP** as chamber pressure presented as a **percent** quantity.

The current PC+2 executable model instead carries the mission-era LM-7-family measurement **GQ6510P** as thrust-chamber pressure in **psi** because that is the directly supported measurement path used by the implemented shutdown-rule monitor.

No reviewed primary source in the current evidence chain establishes the exact Apollo 13 conversion from GQ6510P engineering units to the MSK 1137 TCP percent field.

Therefore:

> The player-facing psi value must not be labeled `TCP`, converted to percent, or positioned as an exact transcription of the historical 1137 field.

It is rendered as a project field such as **CHAMBER P**, retaining psi and provenance.

### Apollo 13 Mission Operations Report / PC+2 Mission Rules

The PC+2 sources establish CONTROL's required decision information independently of exact CRT routing:

- chamber/thrust performance;
- fuel/oxidizer differential pressure;
- inlet-pressure criterion;
- attitude error and rates;
- gimbal/control-system warnings;
- engine and ullage/control state.

This justifies a minimum player view containing those modeled products even where exact CRT placement is unresolved.

## Presentation decision

The first CONTROL screen is a **project rendering of documented information**, not an Apollo CRT reconstruction.

It must carry an explicit notice:

`PROJECT RENDERING — documented PC+2 CONTROL information; not an exact historical CRT transcription`

The initial view is organized into three functional groups:

1. **BURN / PROPULSION**
   - engine state;
   - throttle phase;
   - chamber pressure in psi when modeled;
   - fuel/oxidizer ΔP when modeled.
2. **ATTITUDE / CONTROL**
   - attitude-error vector when modeled;
   - body-rate vector when modeled;
   - gimbal warning;
   - CES DC failure.
3. **ULLAGE**
   - ullage state;
   - active ullage-jet count.

These section names and field labels are implementation labels, not claims that Apollo 13 used this exact arrangement.

## Deferred fields are not simulated failures

`dps.inlet_pressure_psi` remains a project implementation gap because the singular PC+2 ground-selection/aggregation semantics have not been recovered.

The first presentation **omits** such deferred fields. It does not show them as `UNAVAILABLE`, `BAD`, or failed telemetry, because no historical data failure is implied by the project's incomplete model.

This preserves the distinction established in research note 052 between:

- historical product availability/validity;
- project implementation completeness.

## Hidden integrity remains hidden

The presentation consumes only the ordinary controller-visible product dictionary. Internal integrity annotations are not rendered.

A wrong-but-present product can therefore still appear normally until a controller identifies a conflict through available evidence, consistent with the architecture established in notes 065–066.

## Implementation

Added:

- `src/apollo_mission_control/control_presentation.py`
- `tests/test_control_presentation.py`

The presentation object preserves for each displayed field:

- product key;
- display label;
- value;
- units;
- controller-visible validity;
- source layer;
- provenance;
- optional historical analogue note.

This allows a later exact CRT renderer to replace the project layout without changing the underlying station-product model.

## Explicit non-claims

This pass does **not** claim:

- that the project screen reproduces MSK 1123 or 1137 coordinates;
- that CONTROL used one fixed CRT page throughout PC+2;
- exact CRT request/selection behavior;
- exact refresh cadence;
- that GQ6510P psi is numerically identical to MSK 1137 TCP percent;
- an exact historical field for the modeled ground-only fuel/oxidizer ΔP product;
- exact historical display placement for CES DC failure, gimbal warning, attitude-error vector, or body-rate vector in the current executable representation.

## Sources

Primary / mission-specific:

- AC Electronics, *Apollo 13 Guidance & Navigation Summary*, ASPO 45 CRT Displays, PDF pages 186–190.
- *Mission Operations Report — Apollo 13*, LM CONTROL / PC+2 material.
- Apollo 13 Technical Air-to-Ground Voice Transcription / contemporaneous Mission Rules read-up for PC+2 operational criteria.

Repository evidence:

- `resources/research/029_apollo13_aspo45_direct_inspection.md`
- `resources/research/031_apollo13_msk1137_field_inventory.md`
- `resources/research/035_apollo13_msk1123_field_provenance.md`
- `resources/research/052_pc2_controller_product_projection.md`
- `docs/scenarios/APOLLO13_PC2_PLAYER_PRODUCTS.md`

## Stop condition / next work

The minimum CONTROL presentation boundary is now sufficient to begin player-interface implementation without inventing an Apollo CRT.

The next useful display task should be the **GUIDO first-pass player presentation**, because its PC+2 product set is already modeled and the same MSK 1123/1137 evidence can be applied with clearer LGC/PGNS provenance. Exact field-coordinate reconstruction should remain deferred unless a player decision specifically requires it.
