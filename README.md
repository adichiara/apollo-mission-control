# Apollo Mission Control

A cooperative, historically grounded simulation of Apollo-era Mission Control.

Players sit together as flight controllers. Each player uses a phone as the display/interface for a controller station and uses printed station documentation such as flight rules and procedures. A central server maintains the live mission simulation.

## Project standard

This project is **research first**. Apollo operations, terminology, displays, roles, procedures, telemetry, mission timelines, failure behavior, and simulator scenarios are implemented from historical documentation wherever documentation exists.

If a required detail is not documented or has not yet been found, it is recorded as unresolved. It is not silently invented.

See:

- [Project principles](docs/PROJECT_PRINCIPLES.md)
- [Roadmap](docs/ROADMAP.md)
- [Current FIDO/RETRO presentation roadmap addendum](docs/roadmap/2026-09-12_pc2_fido_retro_presentation.md)
- [Simulation architecture](docs/SIMULATION_ARCHITECTURE.md)
- [Controller information workflow](docs/CONTROLLER_INFORMATION_WORKFLOW.md)
- [Apollo 13 station baseline](docs/APOLLO13_STATION_BASELINE.md)
- [Station research status](docs/STATION_RESEARCH_STATUS.md)
- [PC+2 CONTROL presentation status](docs/station-status/2026-09-12_pc2_control_presentation.md)
- [PC+2 GUIDO presentation status](docs/station-status/2026-09-12_pc2_guido_presentation.md)
- [PC+2 TELMU presentation status](docs/station-status/2026-09-12_pc2_telmu_presentation.md)
- [PC+2 FIDO/RETRO presentation status](docs/station-status/2026-09-12_pc2_fido_retro_presentation.md)
- [Progress log](docs/PROGRESS.md)
- [Latest FIDO/RETRO presentation progress](docs/progress/2026-09-12_pc2_fido_retro_presentation.md)
- [Research resources](resources/README.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

The first implementation-oriented vertical slice is **Apollo 13 PC+2 preparation and execution**.

The framework-neutral Python prototype includes the source-backed nominal event/state model, station-specific product projections, partial shutdown-rule evaluation, scenario injection/action/communication layers, product-integrity handling, premature-shutdown/restart response paths, and first-pass player-facing **CONTROL, GUIDO, TELMU, and FIDO/RETRO** presentation models.

### Player-facing presentation progress

The presentation layer follows a common rule: when exact Apollo display evidence is incomplete, the interface is explicitly labeled a **project rendering** of documented controller information rather than presented as a reconstructed historical CRT. Controller-facing value, units, validity, source layer, and provenance are preserved; hidden simulator integrity is not exposed; and unmodeled fields are omitted rather than portrayed as failed historical telemetry.

**CONTROL** uses the Apollo 13 MSK 1123/1137 evidence where semantics match. In particular, historical `TCP` is chamber pressure in percent, while the implemented `GQ6510P` path is in psi, so the player product remains `CHAMBER P` rather than inventing a conversion.

**GUIDO** groups LGC/guidance status, alignment/load status, and maneuver/residual products. Project assessment/load products are not claimed as verbatim CRT literals.

**TELMU** presents power/configuration mode, the documented **38–40 A burn-configuration current reference**, inverter warning/action state, and post-burn power-down transition. The 38–40 A value is explicitly a reference/configuration figure rather than fabricated live current telemetry.

**FIDO/RETRO** now presents the final PC+2 maneuver target and return-plan products. The final P30 LM PAD read around 77:52 GET gives TIG 79:27:38.30, LVLH delta-V +833.0/-50.9/-213.9 fps, resultant 861.5 fps, and expected perigee 20.5 nmi. The final monitor PAD at 78:00:58 gives the selected mid-Pacific return values: latitude -21.65 degrees, longitude -165.00 degrees, range-to-go 1163.5 nmi, entry-interface velocity 36,292 fps, and predicted 0.05-g GET 142:39:22.

A deliberate gap remains: there is not yet an executable **post-burn FIDO propagated trajectory assessment**. GUIDO residuals are not substituted for that product, and physical burn completion does not automatically mean the return trajectory is satisfactory. The trajectory layer will be added only when integrated gameplay requires it.

### Remaining bounded gaps

The singular PC+2 150-psi ground “engine inlet pressure” rule remains intentionally `NOT_EVALUABLE`: separate LM-7 fuel (`GQ3611P`) and oxidizer (`GQ4111P`) interface-pressure measurements are known, but the historical ground selection/aggregation rule has not been established.

The onboard **77-percent thrust-monitor** criterion also remains `NOT_EVALUABLE`; primary sources confirm the rule but do not yet identify the exact percent-thrust crew display/signal.

Exact console layouts, field coordinates, display-selection behavior, and several routing/cadence details remain unresolved where they do not affect current player decisions.

## Immediate priority

The next station view is **INCO**, because the playable interval begins with weak communications and includes link-quality improvement, ranging configuration, telemetry/voice availability, and uplink support before the burn.

After INCO, only minimum **FLIGHT** and **CAPCOM** views remain before the project shifts directly to **integrated playable PC+2 session orchestration**. Additional subsystem or display research should be demand-driven by a concrete player decision or validation problem.

## Apollo 13 station specifications

Detailed research specifications are under `docs/stations/`:

- [EECOM](docs/stations/APOLLO13_EECOM.md)
- [GNC](docs/stations/APOLLO13_GNC.md)
- [GUIDO](docs/stations/APOLLO13_GUIDO.md)
- [TELMU](docs/stations/APOLLO13_TELMU.md)
- [CONTROL](docs/stations/APOLLO13_CONTROL.md)
- [INCO](docs/stations/APOLLO13_INCO.md)
- [FIDO](docs/stations/APOLLO13_FIDO.md)
- [RETRO](docs/stations/APOLLO13_RETRO.md)
