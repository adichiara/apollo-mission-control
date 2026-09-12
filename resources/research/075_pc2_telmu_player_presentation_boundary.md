# Apollo 13 PC+2 — first-pass TELMU player presentation boundary

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED-PARTIAL — minimum project-rendered TELMU view defined from mission-specific power/configuration and inverter evidence; exact historical CRT reconstruction remains unclaimed**

## Question

What is the smallest player-facing TELMU information presentation needed for the Apollo 13 PC+2 vertical slice, using existing modeled products without inventing an Apollo console layout or turning reference values into fake telemetry?

## Primary-source findings

### Apollo 13 Mission Operations Report — PC+2 chronology

The report records that LM power-up for PC+2 began at approximately 78:12 GET and that maintaining the LM in burn configuration would require approximately **38–40 amperes**.

It also records PC+2 ignition at 79:27:38.30 GET and the start of LM power-down at approximately 79:34 GET.

These facts establish a real TELMU-relevant configuration sequence:

```text
low-power coast
    ↓
PC+2 burn power-up
    ↓
approximately 38–40 A burn-configuration requirement
    ↓
PC+2 burn
    ↓
immediate post-burn power-down transition
```

The 38–40 A figure is a documented expected/required configuration load. The currently modeled product does **not** contain a live measured-current channel, so the player view must not present the range as though it were current telemetry.

### Apollo 13 TELMU Post Mission Report

TELMU's mission-specific report establishes the station as responsible for LM electrical, environmental, consumables, and related systems. During the contingency, TELMU continuously tracked LM electrical configuration and current/load because vehicle lifetime depended directly on power use.

For the PC+2 slice, this supports presenting configuration state and the documented burn-load reference even though the broader TELMU consumables/lifetime model is intentionally outside the minimum first slice.

### PC+2 inverter rule

The Apollo 13 PC+2 Mission Rules include an inverter-light shutdown criterion **after switching inverters**. The contemporaneous crew-facing rule read-up preserves the same sequence.

The implementation has already separated:

- inverter warning observation;
- inverter-switch operational action;
- later post-switch warning observation;
- shutdown-rule evaluation.

TELMU presentation must preserve those distinctions. A switch attempt is not evidence that the warning cleared, and a warning must not be converted into an automatic diagnosis.

### Apollo 13 Review Board — power conservation context

The Review Board records the LM power-conservation strategy, including keeping guidance capability through the major abort maneuver and then aggressively reducing electrical load. It confirms that Mission Control tracked the LM's electrical configuration closely and powered required equipment back up for subsequent maneuvers.

This supports configuration-centered TELMU presentation without requiring a full life-support dashboard for the bounded PC+2 interval.

## Exact display boundary

The project has **not** recovered enough source evidence to claim an exact Apollo 13 TELMU CRT for these fields.

Unresolved items include:

- exact TELMU CRT/display number used during PC+2;
- exact field coordinates;
- exact wording/abbreviations for the power-configuration products;
- exact inverter-warning telemetry/display routing;
- exact measured-current parameter and update cadence for the burn configuration.

Therefore the first TELMU view is explicitly labeled a **PROJECT RENDERING**.

## First-pass player view

### POWER CONFIGURATION

- `lm.power.mode` → **POWER MODE**
- `lm.power.burn_configuration_expected_current_range_a` → **BURN CONFIG CURRENT REF**
- `lm.powerdown.started` → **POWERDOWN**

The current range is explicitly labeled **REF** so that a player cannot mistake a planning/reference value for a measurement.

### INVERTER / ELECTRICAL CONTINGENCY

- `lm.inverter_warning` → **INVERTER WARN**
- `lm.inverter_switch_attempted` → **INVERTER SWITCH**
- `lm.inverter_switch_attempt_get_s` → **SWITCH GET**

The latter two are project action/audit products, not claimed Apollo CRT literals.

## Deferred fields

The existing projection deliberately keeps actual measured current as an implementation gap:

- `lm.power.current_a`

It is **omitted** from the player screen. It must not appear as `UNAVAILABLE` telemetry merely because the simulator has not modeled the value path.

Other broader TELMU quantities remain outside this first PC+2 screen unless a later player decision requires them:

- water quantity/usage;
- oxygen quantity/usage;
- CO2/LiOH state;
- battery detail;
- cabin thermal state;
- projected consumable lifetimes.

These are historically important to Apollo 13, but not required to perform the selected PC+2 maneuver slice.

## Information-boundary rule

The TELMU screen inherits the same presentation rules as CONTROL and GUIDO:

- show only controller-facing products;
- preserve value, units, validity, source layer, and provenance;
- hide internal integrity metadata;
- omit unmodeled/deferred fields rather than pretending historical telemetry failed;
- do not add automatic diagnostic text.

## Implementation

- `src/apollo_mission_control/telmu_presentation.py`
- `tests/test_telmu_presentation.py`

## Sources

Primary / mission-specific:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, PC+2 chronology and Mission Rules.
- TELMU, *Apollo 13 Post Mission Report*, in the Flight Operations / Network report material.
- *Report of Apollo 13 Review Board*, Appendix B, LM power-conservation and abort-maneuver chronology.
- Apollo 13 contemporaneous air-to-ground rules read-up around 76:31–76:37 GET.

Repository context:

- `docs/stations/APOLLO13_TELMU.md`
- `resources/research/059_pc2_inverter_warning_after_switch.md`
- `resources/research/060_pc2_inverter_contingency_action_report_loop.md`
- `docs/scenarios/APOLLO13_PC2_PLAYER_PRODUCTS.md`

## Stop condition / next work

The minimum TELMU presentation is sufficient for the first playable slice. Do not expand into a full Apollo 13 consumables dashboard yet.

The next player-facing presentation priority should be **FIDO/RETRO**, because the maneuver target, return consequences, and post-burn trajectory assessment are central to understanding whether PC+2 accomplished its mission objective.
