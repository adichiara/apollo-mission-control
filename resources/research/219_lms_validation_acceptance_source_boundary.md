# Research note 219 — LMS validation / acceptance source boundary

Date: 2026-09-16  
Status: **FORMAL ACCEPTANCE-DOCUMENT SERIES LOCATED; numerical acceptance/correlation criteria not yet recovered.**

## Question

What surviving primary-source evidence constrains how the Lunar Module Mission Simulator was accepted or validated, and what may the project infer now about historical model-validation tolerances?

## 1. NASA archival series confirms formal LMS acceptance documentation existed

The National Archives preliminary inventory for Johnson Space Center Record Group 255 identifies:

**E.155B1. PROJECT FILES ON THE LUNAR MODULE SIMULATOR, 1968–1970, 2 ft.**

The inventory explicitly says the series contains:

- correspondence and memoranda;
- statement of work;
- program and procurement plans;
- **acceptance test plans and procedures**;
- progress and technical reports;
- operations manuals;
- photographs and drawings.

It says most correspondence concerns Kollsman Instrument Corporation and contract **NAS9-8634** for construction of LM simulators at MSC and KSC.

Archive locator:

- old accession: **72A794**
- location: **A-23-16-6**

Primary inventory:
https://www.ibiblio.org/apollo/NARA-SW/Rg255-1.pdf

This is direct evidence that formal simulator acceptance documentation existed in the surviving NASA record set.

## 2. What this does not establish

The inventory description does **not** expose the acceptance-plan contents.

It therefore does not establish:

- numerical error tolerances;
- subsystem-by-subsystem correlation limits;
- reference trajectories or reference hardware used for correlation;
- pass/fail criteria;
- exact test cases;
- update-rate/timestep acceptance limits;
- whether every mathematical model was independently accepted;
- whether the surviving plans correspond to the complete Grumman/Singer-Link LMS software/model acceptance basis rather than a particular simulator component, visual, or contractor work package.

Contract NAS9-8634 is associated in the inventory with Kollsman simulator construction activity. Until folder-level records are inspected, the project must not equate the entire E.155B1 series with a recovered whole-LMS mathematical-model validation specification.

## 3. Simulator Output Tables are a complementary source target

The project source catalog already identifies the Grumman **LMA-790-2-LMS Lunar Module Mission Simulator Instructor's Handbook, Volume II — Simulator Operation, Section 7 — Simulator Output Tables**, MSC accession ***67-16127**.

That source family is potentially complementary to acceptance documentation because it can identify:

- what the simulator exposed as outputs;
- program/math-model ownership or designators;
- the observable quantities available for checkout, operation, and diagnosis.

The existence of output tables does not itself supply acceptance tolerances. Likewise, the existence of acceptance plans does not identify which simulator output fields were used as acceptance observables. Those links remain to be recovered directly.

## 4. Relationship to existing simulator evidence

Research note 215 establishes an AMS architecture precedent with separate program classes and separate physical/system versus telemetry-layer malfunction insertion.

Research note 216 establishes the LMS source hierarchy and cautions against treating the 50 ms AACS study as a simulator-wide timestep.

Research note 217 establishes a later LMS measurement/output dictionary architecture with explicit source/output mapping and telemetry-channel malfunction handling.

This note adds a fourth boundary:

**formal acceptance documentation existed, but its numerical criteria are not presently recovered.**

The evidence supports searching for historical validation artifacts; it does not authorize inventing their contents.

## 5. Project validation architecture consequence

Until an LMS acceptance/correlation document is directly recovered, historical fidelity and modern software correctness remain separate validation layers.

The project should continue to distinguish at least:

1. **Numerical/model verification**  
   Does the implemented equation/integration model behave consistently under declared project numerical settings?

2. **Source/profile validation**  
   Does a historical mission/vehicle profile reproduce quantities for which primary-source targets or ranges actually exist?

3. **Measurement/output validation**  
   Does authoritative state produce the source-backed measurement/output representation without leaking hidden truth or importing unsourced routing?

4. **Causal scenario validation**  
   Do controller actions, crew actions, subsystem consequences, observations, and timing/order propagate through the intended authoritative session logic?

5. **Live integration validation**  
   Does the deployed multi-client/runtime path preserve the same causal and information boundaries?

A modern project test passing one layer must not be labeled a historical LMS acceptance test.

Historical numerical tolerances should enter the project only when the relevant primary acceptance/correlation source supplies them and vehicle/mission applicability is established.

## 6. Source hierarchy for acceptance/correlation claims

For a claimed historical tolerance or acceptance rule, prefer:

1. LMS acceptance test plan/procedure or acceptance report for the relevant model/subsystem;
2. LMS model-specific validation/correlation/check-out report;
3. accepted LMS instructor/output documentation that explicitly states the criterion;
4. mission-era LM subsystem checkout/calibration/performance evidence, when it can be shown to be the simulator's reference basis;
5. FMES/AMS evidence only as methodology precedent unless an explicit LMS bridge is established.

The NARA E.155B1 inventory is a **source-location record**, not a substitute for level 1.

## 7. Next archival targets

Highest-value retrieval targets are now concrete:

- NARA RG 255, **E.155B1**, accession 72A794, location A-23-16-6:
  - acceptance test plans;
  - acceptance procedures;
  - technical/progress reports;
  - statements of work that identify acceptance responsibilities and test articles;
- LMA-790-2-LMS Volume II, Section 7, **Simulator Output Tables**, accession *67-16127;
- LMS-specific model validation/correlation/check-out reports referenced by those documents;
- the Grumman 50 ms AACS study, to determine whether it contains an explicit error/acceptance criterion rather than only a sensitivity study.

## 8. Stop condition

Do not freeze a historical simulator tolerance merely because:

- an acceptance program existed;
- an adjacent FMES/AMS report used a tolerance;
- a spacecraft subsystem specification provides a real-hardware tolerance;
- a project numerical convergence test produces a convenient threshold.

The next promotion from “source located” to “historical acceptance criterion” requires direct primary text tying a criterion to the relevant LMS model/output/test.

## Sources

- National Archives — Southwest Region, *Preliminary Inventory of the Records of the Lyndon B. Johnson Space Center, Record Group 255*, compiled by Kent Carter, 15 Dec 2018, entry E.155B1, pp. 25 / PDF page 28. Public scan: https://www.ibiblio.org/apollo/NARA-SW/Rg255-1.pdf
- NASA/NARA corporate-index record for LMA-790-2-LMS Volume II, Section 7 — *Simulator Output Tables*, accession *67-16127, as cataloged in `resources/source-catalog/APOLLO_SIMULATION_ENGINE_SOURCES.md`.
- Research notes 215–217 for AMS partition/failure insertion, LMS source hierarchy/timestep, and LMS measurement/output boundaries.
