# Apollo Simulation Scenario Research Baseline

Status: **Phase 2 selection baseline — first vertical slice selected; historical SimSup-case research continues separately**

Purpose: identify documented Apollo simulation types and known injected-problem cases before designing the broader scenario system, while keeping the first playable slice grounded in a well-documented actual mission event.

The project goal is to base scenarios on actual Apollo simulation practice wherever surviving documentation permits.

## 1. Simulations were segmented by mission phase

Harold G. Miller, who worked in NASA simulation design and operations, later recalled that Apollo simulations were rarely long-duration end-to-end runs. Missions were usually broken into segments, with simulations established for those cases. This is consistent with the Apollo 13 premission simulation/support schedule preserved in the Mission Operations Report.

The Apollo 13 report names LOI, LM activation/descent, TLI, ascent, descent-abort, launch-abort, reentry, lunar-surface, DOI, TEI, FIDO/BSE, lunar-impact, network, combined CSM/LM, MCC/MSFN validation, communications/remoting, and tracking/data-flow simulation activities. These are historically documented categories, not scenario definitions.

## 2. Apollo simulation philosophy

Miller's retrospective account says simulations were intended to develop teamwork, procedures, ground rules, controller communication, and abnormal-problem response. Controllers were expected already to know their systems. This aligns with the intended experience of this project.

## 3. The simulation used the control center as a system

Miller describes simulated spacecraft data being routed through control-center systems rather than fake values being wired directly to individual consoles, with command loops closed so real procedures could be exercised.

Design implication:

> Scenarios should inject faults into the simulated spacecraft/ground system and let the normal telemetry/ground-processing/display path reveal the consequences.

A scenario script should not directly place a diagnostic message on a controller screen unless the historical system itself would have generated that indication.

## 4. Apollo 11 lunar-landing simulation evidence: two threads, not one established case

### Honeycutt / computer-failure-light recollection

Harold Miller recalls Dick Koos as lead simulation supervisor for the lunar-landing mission and Jay Honeycutt handling the lunar-landing segment. He says Honeycutt ran a simulation showing the **computer failure light**. Miller does not identify that indication as a 1201/1202 program alarm, give the run date, or link the run to a particular alarm-response debrief.

### Program-alarm training evidence

Separate Apollo 11 historical accounts describe preflight program-alarm training and the controller decision problem of determining which alarms required abort and which permitted continuation. That evidence is valuable in its own right, but the currently reviewed sources do not establish that it was the same run Miller remembered.

### Evidence rule

The repository previously conflated these into a single “computer-failure/program-alarm simulation.” That equivalence is withdrawn. Until a primary or near-primary source explicitly links them, treat them as separate evidence threads with potentially different indications, personnel, and runs.

Both still demonstrate an important design principle: simulations could expose missing decision rules and force controller/procedure refinement. Exact scripting, timing, injection method, and alarm set remain unresolved.

See `resources/research/011_apollo_simulation_cases.md`.

## 5. Apollo-13-type contingency simulation evidence

Miller also recalls that an Apollo-13-type contingency had been simulated in a more limited form before the actual mission and that controllers had worked out some procedures later useful during the accident. This supports compound contingency cases but does not justify inventing a precise preflight case without its documentation.

## 6. Scenario evidence levels

- **Level A — Reconstructable documented simulation case:** enough evidence for start state, injections, visible consequences, procedures/rules, and expected simulator behavior.
- **Level B — Documented simulation case, incomplete details:** known to have occurred, but some injection details are missing.
- **Level C — Documented simulation category:** a named training category without a known failure set.
- **Level D — Historically plausible but not documented:** use only if the project explicitly authors hypothetical scenarios later.

## 7. Scenario-research priorities after first-slice selection

1. PC+2 nominal vertical-slice model and validation.
2. PC+2 nonnominal variants tied to documented subsystem behavior and flight rules.
3. Apollo 11 lunar-descent program-alarm simulation research, while preserving the Honeycutt recollection as a separate thread unless linkage is proven.
4. Apollo 13 LM activation/descent records.
5. Apollo 13 descent-abort and ascent simulations.
6. Apollo 13 reentry / launch-abort simulations.
7. FIDO/BSE math-model cases.
8. LOI/DOI and TEI simulations.
9. Surviving SimSup scripts/case sheets from archives.

## 8. Important distinction

A real-flight event is not automatically a historical simulator exercise. The selected first vertical slice, **Apollo 13 PC+2 preparation/execution**, reconstructs an **actual flight event**, not a claim that the exact sequence existed as a documented preflight SimSup case. Scenario metadata should preserve that distinction.

## 9. Apollo 13 simulator discrepancy reports

Contemporaneous Simulation Discrepancy Reports reference Apollo 13's LUM 131 Rev. 1 guidance-software configuration. One legible case tested a hardware restart and documented dependent navigation/computation/control effects. These are engineering/simulator-test evidence, not integrated SimSup mission exercises, but they constrain how computer restarts should be modeled.

Source: https://www.ibiblio.org/apollo/Documents/apollo_13_simulator_discrepencies.pdf

## 10. Selected first vertical slice — Apollo 13 PC+2

Decision D-013 selects Apollo 13 PC+2 preparation and execution. Working scope is approximately 74:00–80:00 GET context, playable start near 77:55–78:00, DPS ignition 79:27:38.30 GET, and immediate endpoint at burn verification / initiation of post-burn LM power-down.

See:
- `docs/scenarios/APOLLO13_PC2_VERTICAL_SLICE.md`
- `resources/research/048_first_vertical_slice_candidate_assessment.md`
- `resources/research/049_pc2_controller_action_and_rule_matrix.md`

## 11. Research sufficiency rule for scenario work

Do not delay the vertical slice to resolve an archival detail unless it materially changes controller information, a procedure/decision rule, simulation state evolution, a validation target, or player-role interaction. Missing low-impact console/detail questions remain cataloged and deferred.

## Sources

1. Apollo 13 Mission Operations Report: https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
2. Harold G. Miller, *The Early Days of Simulation and Operations*: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/MillerHG/MillerHG_paper.pdf
3. Apollo 11 Technical Crew Debriefing / Lunar Surface Journal materials: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11tcdb.html
4. Apollo 11 Lunar Surface Journal program-alarm materials: https://history.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.1201-fm.html
5. Apollo 13 Flight Journal PC+2 chronology: https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
