# Apollo 13 Station Research Status

Status: **Phase 1 research-sufficient; scenario-focused refinement in progress**

Purpose: track how far each Apollo 13-era station has been reconstructed and prevent workflow evidence from being mistaken for display/console evidence.

## Evidence maturity scale

- **A — Station reference:** official console/display evidence plus mission-specific operational evidence.
- **B — Strong workflow:** mission-specific operational evidence is strong; exact display/console remains incomplete.
- **C — Role baseline:** responsibility is documented, but station-specific operational/display evidence remains limited.
- **D — Not yet reconstructed.**

| Station | Maturity | Detailed spec | Strongest current evidence | Main unresolved gap |
|---|---|---|---|---|
| FLIGHT | B | `APOLLO13_FLIGHT.md` | Flight Director report + restored Flight loop | exact FLIGHT displays/console |
| CAPCOM | B | `APOLLO13_CAPCOM.md` | official role + restored CAPCOM/air-ground audio | exact console/display/procedure staging |
| FIDO | B | `APOLLO13_FIDO.md` | FIDO postflight report, RTCC/vector operations | exact trajectory displays / MSK |
| RETRO | B | `APOLLO13_RETRO.md` | RETRO postflight report, RTE/entry products | exact return/entry displays / MSK |
| GUIDO | B | `APOLLO13_GUIDO.md` | GUIDO report + LUMINARY 1C + 1123/1137 provenance + FP7 DEDA/AEA telemetry evidence | exact telemetry-to-MSK selection / RTCC transforms + console access |
| EECOM | **A** | `APOLLO13_EECOM.md` | official console diagram + two real display formats | full display catalog / keyboard layouts |
| GNC | B | `APOLLO13_GNC.md` | GNC report + earlier CRT continuity lead | 683 field transcription / source mapping |
| TELMU | B | `APOLLO13_TELMU.md` | TELMU report, consumables/power chronology, H-2 display-system implementation provenance | exact H-2 LM systems display/loading |
| CONTROL | B | `APOLLO13_CONTROL.md` | CONTROL report + 1123/1137 layouts + LGC/PCM/AEA provenance | exact telemetry-to-MSK selection / RTCC transforms + console workflow |
| INCO | B | `APOLLO13_INCO.md` | INCO report + comms paper; MSK 1475 known | actual look-angle/command display layouts |
| PROCEDURES | B | `APOLLO13_PROCEDURES.md` | Procedures report; FCOH; MSK 1503 known | console/request/display workflow |
| FAO | B | `APOLLO13_FAO.md` | FAO postflight report + revised flight plan | exact FAO/Ground Timeline displays |
| SURGEON | C | — | organizational role + medical mission material | biomedical display/workflow reconstruction |
| NETWORK | C | — | Network Operations appendix + MCC architecture | console/site/network display reconstruction |
| BOOSTER/BSE | C | — | BSE appendix + Saturn mission data | three-seat console/display reconstruction |
| AFD | C | — | organizational role | working products/console |
| RECOVERY | C | — | Recovery Operations appendix | display/data products and player relevance |
| PAO | C | — | documented role | likely outside core simulation play |
| Mission Director/FOD | C | — | documented management roles | player relevance / operational interface |

## Current interpretation

Phase 1 has reached the project's research-sufficiency threshold. The maturity grades are not expected to reach A across the room before implementation starts.

The active question is now narrower:

> What historically supported information and workflow does each station need for the selected Apollo 13 PC+2 vertical slice?

### Reference-station evidence

**EECOM** remains the only station currently at maturity A because the Apollo 13 Review Board preserves:

- console anatomy;
- two actual high-use CRT formats;
- telemetry labels/codes;
- update rate;
- event/limit behavior.

That reference continues to validate the common station architecture even though EECOM is not a core PC+2 player position.

### PC+2 display/product priorities

The next display work should follow scenario need rather than generic station completeness:

1. **CONTROL** — chamber/thrust, inlet and differential pressure, attitude/rate, gimbal/CES warnings, burn configuration.
2. **GUIDO** — final load status, LGC/P40 state, PGNS target/residuals, AGS cross-check, guidance/computer warnings.
3. **FIDO/RETRO** — final PC+2 target/return product and post-burn trajectory assessment.
4. **TELMU** — burn-configuration power/current and inverter/electrical status needed by the shutdown rules.
5. **INCO** — weak-link/AOS, S-band power, ranging, telemetry/uplink availability required during final preparation.
6. **FLIGHT/CAPCOM** — readiness/polling and crew-report/decision path rather than an omniscient combined display.

Complete station catalogs remain valuable expansion research, but they no longer outrank PC+2-required products.

## Phase 1 gap categories

Across stations, missing evidence now falls into a small number of repeated categories:

### Console hardware

- physical station layout;
- monitor count;
- DRK/MSK/key legends;
- status/event panels;
- meters/recorders;
- voice panels.

### Display catalog

- display/MSK numbers;
- field layout;
- labels and units;
- update cadence;
- channel/request behavior.

### Data provenance

- raw telemetry;
- ground-computed values;
- RTCC products;
- replay/delog products;
- support-room analysis.

### Action/command authority

- direct ground commands;
- crew-executed procedures through CAPCOM;
- CCATS/MSFN command chain;
- update verification.

### Communications

- exact loops monitored/transmitted;
- backroom loop topology;
- handoff between Flight loop and discipline loops.

## Phase 1 exit condition

Phase 1 does not require every station to reach maturity A.

The working exit condition is now met for the Apollo 13 baseline:

- core player positions are B or better;
- EECOM provides a systems-station display/console reference;
- guidance/flight-dynamics and communications workflows have mission-specific evidence sufficient to validate common architecture;
- major mission-era nomenclature/configuration differences are documented;
- known source conflicts are logged;
- unresolved exact-display details are explicitly separated from documented workflow.

Further historical reconstruction continues when a selected scenario, implementation dependency, or unusually high-value accessible source justifies it.


## 2026-09-11 — Source extraction and comparison status

ASPO 45 pages are accessible and inspected. MSK 1137 has a normalized Apollo 13 definition-group inventory and verified differences from Apollo 11. See research notes 029–031. This advances display evidence without resolving full console configuration, access, refresh behavior, or operational revisions; maturity ratings remain unchanged.

## 2026-09-11 — LM CRT provenance pass

R-567 Rev. 8 has now been mapped against the Apollo 13 LM CRT evidence. This establishes direct LGC origins for many MSK 1123/1137 field families and, equally importantly, identifies fields that must be ground-derived or sourced from non-LGC telemetry.

The strongest new result is the landing-radar chain: the LGC downlink sends time-tagged antenna-axis data one velocity component at a time, while MSK 1137 presents stable-member velocity components and guidance-comparison residuals. Exact RTCC/ground transformation logic is therefore now a high-priority research target.

See research note 032. Maturity ratings remain unchanged at B because display access, ground transforms, non-LGC telemetry provenance, and console workflow are not yet fully reconstructed.

## 2026-09-11 — MSK 1137 non-LGC telemetry pass

Vehicle-specific sources now identify several physical/PCM measurements behind the Apollo 13 MSK 1137 hardware fields:

- GQ6510P — DPS thrust-chamber pressure;
- GQ6806H — variable-injector actuator position;
- GN7563T — LM-7 landing-radar antenna temperature;
- GN7723T — rendezvous-radar antenna temperature.

Apollo-wide NASA telemetry tables independently route GQ6806H, GN7563T, GN7723T, several PGNCS electrical measurements, and PIPA temperature to MSK 1137. Because those routing tables are retrospective, the Apollo 13 profile still requires mission-era confirmation where possible.

CONTROL remains maturity B: the provenance picture is materially better, but exact Apollo 13 display loading, engineering conversions, refresh behavior, and complete console workflow are not yet reconstructed.

See research note 034.

## 2026-09-11 — MSK 1123 provenance pass

Research note 035 begins the same field-provenance treatment for Apollo 13 MSK 1123 that notes 032–034 established for 1137.

The key result is that 1123 is also a composite Mission Control product. It combines LGC/PGNS downlink values, PCM control measurements, AGS/AEA information, radar data, propulsion state, and ground context. Apollo telemetry routing tables explicitly tie RGA rate channels, attitude-error channels, and selected APS/RCS measurements to 1123.

GUIDO and CONTROL remain at B: the display's source architecture is substantially clearer, but mission-specific AGS Flight Program 7 mapping, exact LM-7 PCM routing/calibration, ground transformations, station access, and refresh behavior remain unresolved.

## 2026-09-11 — AGS Flight Program 7 operational pass

Research note 036 adds directly inspected Flight Program 7 DEDA address evidence and, crucially, Apollo 13 in-flight validation.

Actual Apollo 13 contingency-burn procedures used:
- 400+5 body-axis alignment;
- 400+0 attitude hold;
- 404/405/406 reset;
- DEDA 470 burn monitoring.

This narrows the AGS gap from “what did Flight Program 7 expose?” to the more specific **AEA telemetry → ground decoding → MSK 1123 field** path.

GUIDO and CONTROL remain maturity B because that telemetry/display path, station access, and update behavior are still incomplete.

## 2026-09-11 — AGS telemetry / RTCC processing pass

Research note 037 separates the AEA's ground telemetry stream from the crew DEDA interface and documents the mission-era LM-7 handbook's dedicated AEA telemetry-word-list table.

General AGS documentation establishes a 50-word digital telemetry block repeated once per second, but the exact Flight Program 7 word-to-memory assignments are still being extracted rather than copied from Flight Program 6.

The Apollo 13 Mission Operations Report adds a particularly important real-world validation case: after MCC-5 the **RTCC incorrectly processed AGS body angles**. Mission Control rejected the bad ground readout and used the independent FDAI reference, which showed PTC was actually correct.

This confirms that ground-processing validity must be modeled separately from spacecraft/telemetry validity. Station maturity remains unchanged.

## 2026-09-11 — FP7 telemetry continuity matrix

Research notes 038–039 now constrain the missing Apollo 13 AEA telemetry list much more tightly.

The surviving FP6 and FP8 source listings both place their 50-word telemetry block at octal addresses **0325–0406**. Their symbols agree at 49 of 50 positions; address **0371** differs. The Apollo 13 G&N Dictionary independently supplies direct or partial mission-specific meaning for 25 of those 50 candidate addresses, including navigation vectors, time, velocity, selector state, and delta-V monitor words.

This is still **not** treated as a certified Apollo 13 Table 2.1-7. The remaining authority target is the February 1970 LM-7 handbook telemetry table. GUIDO/CONTROL maturity remains B.

## 2026-09-11 — AGS direction-cosine attitude path

Research note 040 documents the attitude representation behind the AGS telemetry architecture.

FP6 and FP8 source listings both show six telemetered direction cosines (X-body and Z-body rows) snapshotted for telemetry, rather than final body Euler angles. This fits Apollo 13's documented RTCC body-angle-processing failure and gives the project a concrete ground-transform boundary for MSK 1123 AGS ATT.

The exact FP7 Table 2.1-7 identifiers and RTCC conversion equations remain unresolved. GUIDO/CONTROL maturity remains B.

## 2026-09-11 — AGS delta-V interface pass

Research note 041 separates the AEA's telemetered delta-V accumulation from the crew DEDA readout path.

The telemetry block carries VD1X/Y/Z at 0404–0406, while Apollo 13 DEDA 470–472 represents separate 2-second navigation-update values. Apollo 13 used 404–406 zeroing and 470 monitoring operationally during contingency burns.

This removes another potential false simplification: MSK 1123 AGS DEL VEL must not be implemented as a mirror of the crew's current DEDA display. Exact CRT routing remains unresolved; maturity stays B.

## 2026-09-11 — AGS ullage provenance pass

Research note 042 separates the AGS ullage measurement, threshold test, consecutive-cycle counter, completion criterion, and controller-visible field.

This removes another ambiguity in MSK 1123: its AGS ULL field is in velocity units and therefore is not simply the MU8 counter or an ullage-acquired Boolean. Exact field calculation/routing remains unresolved; GUIDO/CONTROL maturity stays B.

## 2026-09-11 — MSK 1123 DEDA telemetry pass

Research note 043 ties the DEDA portion of MSK 1123 to explicit AEA telemetry variables: readout-mode flag, DEDA data, clear-mode flag, and DEDA address.

This is another piece of the 1123 page that can now be implemented from a historically separated source path rather than by mirroring a crew display. Exact Apollo 13 masks/formatting and FP7 telemetry IDs remain unresolved; GUIDO/CONTROL remain maturity B.

## 2026-09-11 — consolidated MSK 1123 AGS field matrix

Research note 044 consolidates the AGS portion of MSK 1123 into source-path confidence classes.

Several rows now have strong provenance (AGS time, RGA rates, AGS attitude, AGS attitude error, DEDA state), while ASA rate, AGS velocity, AGS delta velocity, and AGS ullage have constrained but not yet certified source mappings.

The main research bottleneck has shifted from “what does the page contain?” to **exact FP7 telemetry membership and RTCC/display transformation rules**. GUIDO/CONTROL remain at B.

## 2026-09-11 — MSK 1123 velocity-row semantics and ground-format context

Research note 045 separates five adjacent velocity-related rows using the Apollo 11/12 AC/Delco display definitions: **AGS VEL** (indicated velocity), **LGC DEL VEL** (two-second PIPA output), **AGS DEL VEL** (measured velocity), **AGS ULL** (ullage measurement), and **ACT VEL** (accumulated velocity along thrust). The older display definitions also constrain their historical precision without proving that the Apollo 13 masks were unchanged.

A January 1970 MIT Instrumentation Laboratory report independently reproduces the 1123-style page as a **Typical Data Format for Ground Consoles**, including the AEA/LGC/PCM header and the same velocity rows. This strengthens the evidence that the page is a composite ground-monitoring product rather than a direct mirror of a single onboard source.

The new evidence does **not** identify the exact Apollo 13 FP7 telemetry word or RTCC transformation feeding AGS VEL / DEL VEL / ULL, nor does it establish that the AEA/LGC/PCM header boxes were dynamic validity indicators. GUIDO and CONTROL therefore remain at maturity B.

## 2026-09-11 — AEA telemetry-word-list recovery

Research note 046 recovers Table 2.1-7's telemetry structure and engineering descriptions from a later contemporary LMA790-3-LM configuration. The source chronology is now explicit: Apollo 13's **LM-7 and Subsequent** handbook is Basic Date **15 December 1968**, Change Date **1 February 1970**; the searchable **LM-10 and Subsequent** copy is Basic Date **1 February 1970**, Change Date **15 June 1970**. The LM-10 table is therefore retained as continuity evidence until the exact LM-7 page is directly compared.

The telemetry list independently confirms distinct products for present LM inertial velocity, compensated 20-ms body-axis incremental velocity, a dimensionless ullage counter, and a separate three-word sensed body-axis velocity-increment family. It also confirms DEDA-state and attitude-direction-cosine telemetry families.

This removes “what velocity products are actually available in the AEA telemetry stream?” as the main uncertainty. The remaining high-value problem is **which telemetry product and ground transformation feeds each MSK 1123 row**. GUIDO and CONTROL remain maturity **B** because controller-facing selection, RTCC transformation, station access, and refresh behavior remain incomplete.

## 2026-09-12 — AGS ullage test narrowed

Research note 047 adds primary AGS specification evidence that ullage qualification is based on **accumulated +X-axis velocity increment over each 2-second computer cycle**, with the threshold required for three consecutive cycles. The inspected specification states a **0.2 ft/s** threshold; a later LM handbook expresses the equivalent condition as average +X acceleration greater than **0.1 ft/s²** over the same cycle.

That makes a velocity-valued quantity in the two-second ullage-test chain the strongest current physical candidate behind the controller's **AGS ULL** measurement. It still does not identify the exact telemetry word or RTCC/display transformation. **AGS ULL** and **ACT VEL** remain distinct unresolved parameters, and GUIDO/CONTROL remain maturity **B**.

## 2026-09-12 — PC+2 vertical-slice initialization readiness

Research note 050 and `docs/scenarios/APOLLO13_PC2_PARAMETERS.md` now define a bounded nominal information contract beginning at **77:55:00 GET**.

This does not promote any station maturity grade, because the grades measure historical station reconstruction rather than scenario implementability. It does, however, establish that the selected slice can proceed without resolving every station's full console catalog.

Scenario-specific readiness now includes:

- **FIDO/RETRO:** final LVLH maneuver PAD and return/landing products are documented; a complete RTCC Cartesian state vector and exact CRT layout are deferred until the trajectory propagator/display implementation actually requires them.
- **GUIDO:** alignment acceptance, planned/executed IMU-coordinate velocity-to-be-gained, LGC/P40 state, warning conditions and post-burn residuals are documented strongly enough for the nominal slice; complete MSK 1123 routing remains deferred.
- **CONTROL:** chamber/thrust, inlet-pressure and differential-pressure shutdown criteria, attitude/rate limits, gimbal/CES warning logic and nominal burn sequence are documented; exact nominal pressure readings are not invented from the thresholds.
- **TELMU:** the burn-configuration load of approximately **38–40 A** and inverter/electrical shutdown relevance are sufficient for first-slice scope; the entire LM consumables model is not required yet.
- **INCO:** the weak link at scenario start, subsequent S-band power-amplifier improvement, ranging requirement, and telemetry/uplink availability are scenario-relevant; MSK 1475's full layout is not a blocker.
- **FLIGHT/CAPCOM:** the final GO/NO-GO and air-ground decision/readback path is documented and remains intentionally separate from raw subsystem state.

All affected stations remain at their existing maturity grades. The next station research should be driven by the minimum PC+2 player-facing product set rather than by generic console completeness.

## 2026-09-12 — PC+2 ullage/throttle command chronology

Research note 051 freezes the first-slice procedure/command sequence relevant to CONTROL and CAPCOM: manual two-jet ullage begins at **TIG−10 s**, minimum throttle begins at ignition, 40-percent throttle is commanded at **TIG+5 s**, and maximum throttle is commanded after the documented 21-second 40-percent segment.

The crew's later 40-percent and 100-percent voice reports remain separate communication events. This is important for station modeling because CONTROL should not receive a perfect throttle-state transition merely because the crew procedure commanded one; physical engine response, telemetry indication and crew report are different information layers.

This improves scenario fidelity but does **not** resolve exact CONTROL CRT timing, telemetry-to-display routing, or detailed physical engine-response dynamics. CONTROL therefore remains maturity **B**.

## 2026-09-12 — PC+2 controller-product projection and shutdown-rule boundary

Research notes 052–053 now connect the research model to the executable information path without changing station maturity grades.

The first station-specific product projection is implemented for **CONTROL, GUIDO, FIDO/RETRO, TELMU, INCO, FLIGHT, and CAPCOM**. Products carry validity, timestamp fields, source layer, and provenance. Critically, required historical measurements whose nominal numeric values have not yet been modeled are tracked as **implementation-deferred fields**, not falsely presented as unavailable Apollo telemetry.

This preserves several station boundaries:

- **FLIGHT** receives phase/decision context rather than a hidden all-systems health dashboard.
- **CAPCOM** receives the maneuver-PAD/voice path and crew reports rather than authoritative subsystem state.
- **CONTROL** receives modeled propulsion/control state and warnings, while exact chamber/inlet/delta-P and attitude/rate numerics remain deferred.
- **GUIDO** receives LGC/P40, warning, load/target and residual products without collapsing them into CONTROL's hardware view.
- **TELMU** distinguishes the documented 38–40 A burn-configuration expectation from an as-yet-unmodeled actual current measurement.
- **INCO** retains the communications/ranging/uplink path rather than becoming a generic data-valid flag.

The PC+2 Mission Rules have also been converted into a **partial derived audit evaluator**. Modeled warnings such as engine-gimbal, LGC, and CES DC can evaluate clear/triggered, while pressure, delta-P, attitude/rate, crew analog indications, positive ISS+program-alarm, and positive inverter-after-switch cases remain `not_evaluable` until their observation paths are genuinely modeled.

A primary-source wording conflict is now logged rather than normalized: the Mission Operations Report places the startup-transient exception with the attitude-rate criterion, while the crew readback places it with attitude error. The exact scope remains unresolved.

No station is promoted: this is implementation of documented information boundaries, not new exact console/display evidence. CONTROL, GUIDO, FIDO, RETRO, TELMU, INCO, FLIGHT and CAPCOM remain maturity **B**.

## 2026-09-14 — H-2 Display System / PHO-TR155 implementation boundary

Research note **124** adds mission-specific Philco evidence that the **Mission H-2 Display System was configured in accordance with PHO-TR155 Revision C**, that Revision C was implemented in March 1970, and that **no equipment configuration changes were necessary** for that implementation.

For TELMU this narrows the unresolved display problem without promoting maturity:

- the Apollo 13/H-2 operational display configuration was real and implemented before flight;
- Revision C does not justify inventing new physical TELMU display hardware, monitor count, or modules;
- source-backed inverter measurements `GC0071V` / `GC0155F` may continue to appear in a project-rendered TELMU product;
- exact H-2 indicator/module position, CRT/display request, DRK/MSK workflow, cadence, precision, latency, and console labeling remain unresolved until Revision C, data-pack Revision N, or equivalent loading records are recovered.

TELMU therefore remains maturity **B**. The new evidence strengthens configuration provenance, not exact station reconstruction.