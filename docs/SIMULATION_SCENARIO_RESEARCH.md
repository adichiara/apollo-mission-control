# Apollo Simulation Scenario Research Baseline

Status: **Phase 2 selection baseline — first vertical slice selected; historical SimSup-case research continues separately**

Purpose: identify documented Apollo simulation types and known injected-problem cases before designing the broader scenario system, while keeping the first playable slice grounded in a well-documented actual mission event.

The project goal is to base scenarios on actual Apollo simulation practice wherever surviving documentation permits.

## 1. Simulations were segmented by mission phase

Harold G. Miller, who worked in NASA simulation design and operations, later recalled that Apollo simulations were rarely long-duration end-to-end runs. Missions were usually broken into segments, with simulations established for those cases.

This is consistent with the Apollo 13 premission simulation/support schedule preserved in the Mission Operations Report.

### Apollo 13 documented simulation families

The report explicitly lists simulation activity including:

- Math Model LOI simulation
- Math Model LM activation/descent simulation
- CMS LOI simulation
- CMS/LMS LM activation/descent simulation
- CMS TLI simulation
- Math Model ascent simulation
- LMS descent-abort simulation
- CMS/LMS ascent simulation
- CMS launch-abort simulation
- CMS reentry simulation
- LM descent simulation
- Math Model lunar-surface simulation
- CMS DOI simulation
- CMS TEI simulation
- CMS launch simulation
- CMS/LMS LM ascent/descent simulation
- Math Model FIDO/BSE simulation
- Math Model lunar-impact simulation
- Network simulation
- CMS/LMS LOI simulation
- CMS reentry + LMS ascent simulation
- Math Model LOI/descent simulation
- CMS LOI/DOI simulation
- MCC/MSFN validation exercises
- communications/remoting tests
- tracking/telemetry loading and data-flow tests

These names are historically documented categories. They are not scenario definitions.

## 2. Apollo simulation philosophy

Miller's retrospective account states that the purpose of the simulations was not to teach controllers basic systems knowledge. Controllers were expected already to understand their systems and trajectories.

The simulations were intended to:

- develop teamwork
- develop/refine procedures
- exercise ground rules
- exercise communication among flight controllers
- prepare the team to handle abnormal problems

He specifically recalls that simulation designers wanted failures that exercised procedures, ground rules, and controller communication.

This aligns closely with the intended experience of this project.

## 3. The simulation used the control center as a system

Miller describes the training architecture as deliberately feeding simulated spacecraft data through the same type of data stream used by the real control center rather than wiring fake values directly to individual consoles.

For Gemini and Apollo, command loops were closed so controllers could practice actual command/abort procedures.

Design implication:

> Scenarios should inject faults into the simulated spacecraft/ground system and let the normal telemetry/ground-processing/display path reveal the consequences.

A scenario script should not directly place a diagnostic message on a controller screen unless the historical system itself would have generated that indication.

## 4. Known documented injected case: Apollo 11 computer-failure/program-alarm simulation

A strong documented example exists for the lunar landing team.

Miller recalls that Jay Honeycutt, serving as simulation supervisor for the lunar landing, ran a case involving the onboard computer failure light.

Other historical accounts identify a pre-Apollo-11 simulation in which a 1201/1202-type program alarm caused the controller team to call an abort. The debrief resulted in further work to determine which program alarms required abort and which permitted continuation.

This case is important because it demonstrates:

- simulation problems could expose missing decision rules
- the correct outcome was not necessarily abort
- a simulation could cause flight-rule/procedure changes
- a simulated failure could later resemble an actual flight event

### Evidence status

The existence of the computer-failure/program-alarm simulation is well supported.

Exact scenario scripting, timing, telemetry injection method, and every alarm presented in the original case remain unresolved.

Do not recreate the scenario in detail until stronger source material establishes those specifics.

## 5. Apollo-13-type contingency simulation evidence

Miller also recalls that an Apollo-13-type contingency had been simulated in a more limited form before the actual mission and that controllers had consequently worked out some procedures later useful during the accident.

Again, this supports using compound contingency cases, but it does **not** justify inventing the precise preflight Apollo 13 simulation without locating the case documentation.

## 6. Scenario evidence levels

Future scenario candidates should be labeled:

### Level A — Reconstructable documented simulation case

Enough evidence survives to reproduce:

- starting mission phase
- injected failures/anomalies
- controller-visible consequences
- relevant procedures/rules
- expected simulator behavior

### Level B — Documented simulation case, incomplete details

The simulation is known to have occurred, but some injection details are missing.

Use only after explicit project decisions resolve the missing pieces.

### Level C — Documented simulation category

Example: "LMS Descent Aborts Sim."

We know NASA trained that mission phase/category, but not the specific failure set.

Useful for research planning, not enough to author a scenario.

### Level D — Historically plausible but not documented

Do not use unless the project explicitly decides to author a hypothetical scenario later.

## 7. Scenario-research priorities after first-slice selection

Historical SimSup-case research remains valuable. PC+2 no longer blocks broad scenario research, but it remains the current implementation/reference case while the reusable causal architecture is proven.

Priority order:

1. PC+2 nominal vertical-slice model and validation as the first reference case.
2. PC+2 nonnominal variants only where a failure can be tied to documented subsystem behavior and flight rules.
3. **Apollo 11 powered-descent program-alarm interval** as the second engineering reference case, using the actual-flight chronology for source-bounded timing and state.
4. Continue research on the documented final Apollo 11 lunar-descent program-alarm simulation as a distinct historical SimSup case; do not invent its unresolved alarm identity/timing.
5. Apollo 13 LM activation/descent simulation records.
6. Apollo 13 descent-abort and ascent simulations.
7. Apollo 13 reentry / launch-abort simulations.
8. FIDO/BSE math-model cases.
9. LOI/DOI and TEI simulations.
10. Any surviving SimSup scripts/case sheets from JSC archives.

## 8. Important distinction

A real-flight event is not automatically a historical simulator exercise.

For example, the Apollo 13 oxygen-tank accident is an excellent historical contingency to simulate, but the project should distinguish:

- replaying the actual mission accident, versus
- recreating a documented premission simulation case.

Both may eventually be valuable, but they have different historical provenance.

The selected first vertical slice, **Apollo 13 PC+2 preparation/execution**, is explicitly a reconstruction of an **actual flight event**, not a claim that the exact PC+2 sequence existed as a documented preflight SimSup case.

That distinction should remain visible in scenario metadata.

## 9. Apollo 13 simulator discrepancy reports

A surviving set of contemporaneous **Simulation Discrepancy Reports** references Apollo 13's **LUM 131 Rev. 1** guidance-software configuration.

One clearly legible case tested the effects of a **hardware restart** on the closed-loop primary guidance system and documented effects on:

- navigation-update frequency;
- P32 input/computation state;
- temporary control reversal in a rate-command mode;
- additional navigation/display behavior still being investigated.

These reports are not the same thing as integrated SimSup mission exercises. They are engineering/simulator test evidence.

They nevertheless provide valuable constraints on how the simulator should represent guidance-computer restarts and configuration problems: as dependent state transitions rather than a single canned failure flag.

Source:
https://www.ibiblio.org/apollo/Documents/apollo_13_simulator_discrepencies.pdf

## 10. Selected first vertical slice — Apollo 13 PC+2

Decision D-013 selects Apollo 13 PC+2 preparation and execution as the first playable vertical slice. Decision D-021 clarifies that this is a validation anchor and first reference implementation, not the eventual scope of the simulator.

Working scope:

- historical context: approximately 74:00–80:00 GET;
- recommended playable start currently near 77:55–78:00 GET, pending final action-sequence mapping;
- DPS ignition: 79:27:38.30 GET;
- immediate endpoint: burn verification and initiation of post-burn LM power-down.

Why this is the current implementation priority:

- strong primary-source chronology and controller reports;
- explicit burn/shutdown rules;
- meaningful multi-station interaction;
- bounded propulsion/guidance event;
- direct compatibility with the Apollo 13-era platform baseline;
- sufficient evidence to validate the project's information-path architecture without implementing the entire oxygen-tank accident first.

See:

- `docs/scenarios/APOLLO13_PC2_VERTICAL_SLICE.md`
- `resources/research/048_first_vertical_slice_candidate_assessment.md`
- `resources/research/049_pc2_controller_action_and_rule_matrix.md`

## 11. Second engineering reference — Apollo 11 powered descent / program alarms

Research note 162 selects the actual Apollo 11 powered-descent alarm interval as the next architecture pressure test after PC+2.

This does **not** make Apollo 11 descent the only next playable scenario. Its purpose is to force the reusable engine to support a substantially different causal chain: landing radar → PGNS/AGS guidance observations → LGC program/restart alarms → continuously evolving descent trajectory → controller continue/abort judgment.

The separately documented preflight program-alarm simulation remains a valuable future SimSup scenario, but Richard Koos explicitly could not recall whether its injected alarm was 1201 or 1202 and surviving evidence does not yet establish exact injection timing. Those gaps must not be silently filled from the actual flight.

See `resources/research/162_second_reference_apollo11_descent_assessment.md`.

## 12. Research sufficiency rule for scenario work

Do not delay the vertical slice to resolve an archival detail unless it materially changes:

- a controller's available information;
- a procedure or decision rule;
- simulation state evolution;
- a validation target;
- player-role interaction.

Missing exact console legends, noncritical CRT fields, complete backroom staffing, or other low-impact details remain cataloged but deferred until implementation proves them necessary.

## Sources

1. Apollo 13 Mission Operations Report, especially Network Operations premission support/simulation schedule and controller appendices.  
   https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf

2. Harold G. Miller, *The Early Days of Simulation and Operations*, NASA historical paper, 2013.  
   https://www.nasa.gov/wp-content/uploads/2025/08/millerhg-paper.pdf

3. Apollo 11 Technical Crew Debriefing / Lunar Surface Journal materials concerning simulator use and program alarms.  
   https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11tcdb.html

4. Apollo 11 Lunar Surface Journal program-alarm materials.  
   https://history.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.1201-fm.html

5. Apollo 13 Flight Journal, Day 4 PC+2 chronology.  
   https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
