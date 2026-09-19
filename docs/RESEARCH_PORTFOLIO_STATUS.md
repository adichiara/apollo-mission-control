# Research Portfolio Status

Date: 2026-09-18  
Policy: D-024 / `docs/RESEARCH_SUFFICIENCY.md`

## Purpose

This file applies the D-024 closure gate to active research areas. It is a status/priority artifact, not a historical source and not a replacement for claim-level `DOCUMENTED`, `PARTIALLY DOCUMENTED`, or `UNRESOLVED` labels.

A research state here answers a narrower question: **should active research continue now for a named implementation dependency?**

## Current portfolio summary

| Bounded question | State | Current consequence |
| --- | --- | --- |
| Are the reusable causal-engine layer boundaries sufficiently constrained for current implementation? | **SUFFICIENT** | Continue implementation using separated physical/subsystem, observation/measurement, ground/interface, and exercise-control layers. |
| Must the current engine reproduce an exact historical LMS-wide timestep or numerical method? | **DEFERRED** | Keep project numerical methods explicit and validated; do not assert a historical global LMS timestep. |
| Must current work recover LMS acceptance/correlation tolerances before implementation continues? | **DEFERRED** | Historical tolerances remain unavailable; current software/numerical/source validation layers remain separate. |
| Must current work recover exact LMS instructor malfunction/scripting mechanics from Volume II Sections 2/6? | **DEFERRED** | Generic causal malfunction architecture may proceed; exact LMS injection mechanics are not required until a historical LMS exercise or specific injectability claim depends on them. |
| Must current work recover Section 7 output tables before the measurement/output abstraction proceeds? | **DEFERRED** | Existing measurement/output separation is sufficient for current architecture; exact historical output ownership/routing remains unavailable. |
| Can the public Volume I scan be treated as page-verified `67-14186` and mined for technical claims now? | **DEFERRED** | Do not promote scan identity or contents. Reopen only when a selected implementation dependency requires Volume I content and title/control pages can be inspected. |
| Can the 1971 LMS User's Manual establish Apollo 13 machine/program/loading configuration? | **DEFERRED** | It remains late-program operational evidence only unless Apollo 13 effectivity is independently established. |
| Is the Apollo 13 Lovell-copy LM Malfunction Procedures document sufficiently controlled as a mission-specific operational cross-check? | **SUFFICIENT** | The 16 March 1970 FINAL Lovell scan may be used as an Apollo 13 operational cross-check, preserving page-level markings when pages are extracted. |
| Is the complete Apollo 13 LM malfunction symptom/procedure inventory needed now? | **DEFERRED** | Do not page-mine the entire checklist without a selected failure/decision dependency. |
| Are Apollo 13-period failure-planning principles sufficient for scenario-authoring constraints? | **SUFFICIENT** | Preserve failure scope, applicable procedure/decision path, and negative-training correction as scenario-validation constraints. |
| Must crew malfunction procedures be mapped to LMS injectability now? | **DEFERRED** | Do not equate crew procedures with simulator capability. Reopen for a selected historical LMS exercise or explicit injectability claim. |
| Can the PC+2 historical numerical profile currently close its unresolved D-022/model-profile gates? | **BLOCKED** | Historical numerical validation remains blocked on named mission/vehicle artifacts; this does not block the validation harness or player-interface work. |
| Is Apollo 11 powered-descent/program-alarm research still decision-relevant? | **OPEN** | It directly constrains the second architecture reference and remains active. |

---

## Closure record A — reusable simulator / causal-engine architecture

- **Status:** **SUFFICIENT**
- **Bounded question:** Is the surviving simulator evidence sufficient to constrain the reusable architecture boundaries needed by the current engine without reconstructing the entire historical LMS?
- **Implementation dependency:** separation of authoritative physical/subsystem state, instrumentation/measurement state, ground/interface products, simulator/exercise control, and malfunction insertion.
- **Decision sensitivity:** a materially different answer could require collapsing or separating domains, changing where failures are inserted, or allowing observation faults to mutate physical truth.
- **Decision-relevant findings:** research 215 supplies direct AMS evidence for separate program classes and separate physical/system versus telemetry malfunction layers. Research 217 independently supplies LMS evidence for an explicit source-variable/measurement-output mapping with spacecraft effectivity and telemetry-console malfunction handling. Research 216 controls the source hierarchy and prevents a model-specific 50 ms study from becoming a global timestep claim. These findings are already reflected in the implemented measurement/output and causal-domain boundaries.
- **Remaining gaps and disposition:** exact LMS program names, model equations, mission-specific constants, machine allocation, historical global cadence, and Apollo 13-specific LMS internals remain unresolved or unextracted. They are **non-decision-relevant at the current architecture layer** and are deferred until a selected scenario/model needs them.
- **Closure challenge:** 2026-09-18 targeted searches for the LMS handbook identity, Section 2 Malfunction Data, and Section 6 Scripting Data Sheets found the same NASA/MSC bibliographic controls and Virginia Tech archival holdings already cataloged; no accessible primary content surfaced that changes the current layer boundaries. The Virginia Tech collection remains open for research and supports reproduction/digitization requests. The direct public Volume I and User's Manual PDFs remain too large for the current web fetch path. No contrary source was found requiring a different current architecture.
- **Reopen triggers:** a selected scenario requires a causal coupling not covered by the current architecture; a recovered LMS primary source contradicts the current partition; implementation requires a historically exact LMS instructor/output mechanism; or a failure cannot be represented without choosing among unresolved historical mechanisms.

### Consequence

Stop broad simulator-architecture searching. Future LMS/AMS retrieval is dependency-driven, not a standing roadmap task.

---

## Closure record B — LMS numerical method and acceptance/correlation criteria

- **Status:** **DEFERRED**
- **Bounded question:** Does the current simulator need an exact historical LMS timestep, integration algorithm, or historical acceptance/correlation tolerance to continue?
- **Implementation dependency:** numerical configuration and validation labeling.
- **Decision sensitivity:** if a historical criterion becomes required, it would constrain a model's integration/update policy or historical-validation threshold.
- **Decision-relevant findings:** research 216 establishes only that a 50 ms LMS integration step was studied for AACS response; it does not establish a global LMS timestep. Research 219 establishes that formal LMS acceptance documentation survives in NASA RG 255 E.155B1 but does not expose numerical criteria. Current project numerical verification is explicitly separate from historical LMS acceptance.
- **Remaining gaps and disposition:** global/model-specific LMS cadence, acceptance tolerances, reference cases, and correlation methods remain unresolved. They are **not required by a current player-visible or scenario decision**, so they are deferred.
- **Closure challenge:** targeted search did not surface direct primary acceptance criteria or a full LMS-wide timestep specification. The known next evidence remains named archival material rather than another broad web-search space.
- **Reopen triggers:** a selected historical scenario/model requires a source-backed update cadence or acceptance threshold; a model-profile admission rule explicitly requires historical correlation; or RG 255/model-specific acceptance material becomes directly available.

### Retrieval condition if reopened

Prefer the relevant LMS acceptance plan/procedure or model-specific validation/correlation report. Do not substitute spacecraft hardware tolerances, AMS/FMES values, or project convergence thresholds.

---

## Closure record C — LMS Volume II Sections 2, 6, and 7

- **Status:** **DEFERRED**
- **Bounded question:** Must current implementation recover the exact LMS malfunction definitions/insertion mechanics, scripting data, and output tables?
- **Implementation dependency:** historical LMS exercise reconstruction, exact instructor scripting/injectability, and historical output/model ownership.
- **Decision sensitivity:** these documents could alter how a specifically reconstructed historical LMS exercise injects a malfunction or maps simulator outputs.
- **Decision-relevant findings:** the Virginia Tech Avitabile finding aid identifies Section 2 **Malfunction Data** (3 folders), Section 6 **Scripting Data Sheets** (2 folders), and Section 7 **Simulator Output Tables** (3 folders, 1 July 1967). NASA/MSC bibliographic control independently identifies the handbook family and Section 7 accession/date. Existing AMS and LMS evidence is already sufficient for the generic causal and measurement/output abstractions.
- **Remaining gaps and disposition:** actual section pages, failure identifiers, scripting syntax, model/program designators, output semantics, revision/effectivity, and Apollo 13 applicability remain unresolved. No currently selected scenario depends on those exact LMS mechanics, so active retrieval is deferred.
- **Closure challenge:** the current Virginia Tech finding aid was rechecked on 2026-09-18. It confirms the collection is open for research and that reproduction/digitization can be requested, but exposes no online Section 2/6/7 technical pages. Targeted web searches surfaced no alternate primary page-level copy.
- **Reopen triggers:** selection of a historical LMS SimSup case; a requirement to claim that a particular malfunction was LMS-injectable; a requirement for exact LMS scripting behavior; or a current station/model product requires an output mapping unavailable from mission-specific sources.

### Retrieval condition if reopened

Use the already identified folders rather than restarting broad discovery:
- Section 2 — 3 folders;
- Section 6 — 2 folders;
- Section 7 — 3 folders.

Request title/control/change pages together with body pages so effectivity is not reconstructed from catalog metadata alone.

---

## Closure record D — LMS Volume I and 1971 User's Manual

- **Status:** **DEFERRED**
- **Bounded question:** Must current work authenticate/extract these large public scans for a current implementation dependency?
- **Implementation dependency:** subsystem-simulation details, mature LMS machine/program/loading practice, or a future exact historical LMS configuration.
- **Decision sensitivity:** recovered technical pages could refine model boundaries or operational computing detail, but no current runtime behavior depends on them.
- **Decision-relevant findings:** research 319 identifies the public Volume I scan as a high-confidence candidate compatible with NASA bibliographic control but not page-verified as accession `67-14186`. Research 320–321 establish the User's Manual scan as Volume 1, Update #34, 22 October 1971 and therefore too late to establish Apollo 13 configuration without change/effectivity evidence.
- **Remaining gaps and disposition:** title/control-page identity for Volume I; User's Manual interior change history; Apollo 13 effectivity; machine/program assignment; loading/common-memory/peripheral details. All are deferred at current scope.
- **Closure challenge:** direct fetches on 2026-09-18 again failed because the public files are approximately 158 MB and 93 MB respectively. Targeted searches recovered bibliographic/index material but no alternate page-level copy that closes the identity/effectivity gates.
- **Reopen triggers:** an implementation requires a specific subsystem-simulation detail or exact LMS operating-computing practice; an alternate smaller/renderable copy becomes available; or a large-file-capable extraction path becomes available.

---

## Closure record E — Apollo 13 LM Malfunction Procedures identity/effectivity

- **Status:** **SUFFICIENT**
- **Bounded question:** Is the public Lovell-copy scan controlled well enough to serve as the mission-specific Apollo 13 operational cross-check defined by research 325?
- **Implementation dependency:** checking selected LM failure symptoms, crew troubleshooting branches, caution/warning indications, and phase restrictions against Apollo 13-period material.
- **Decision sensitivity:** using the wrong document state could import later or non-mission procedure content.
- **Decision-relevant findings:** research 326 records the public scan's own indexed cover as **Apollo 13 LM Malfunction Procedures**, part number `SKB32100076-386`, **FINAL**, **16 March 1970**. NASA final stowage documentation independently links the same part number to Apollo 13 LM Flight Data File carriage.
- **Remaining gaps and disposition:** page-specific change markings and the technical delta to the later 1 April FINAL CHANGE A state remain unresolved. They do not prevent using the 16 March scan as its own controlled document state, provided extracted pages preserve their own markings.
- **Closure challenge:** targeted 2026-09-18 search found additional secondary artifact/auction descriptions of Apollo 13 copies, including inconsistent catalog dating. Those descriptions were not used to override the primary scanned cover control already recorded in research 326. No stronger primary source was found contradicting the current document-state conclusion.
- **Reopen triggers:** direct scan control pages contradict the indexed cover text; a selected procedure page carries a materially different change marking; or implementation needs the Change A delta.

---

## Closure record F — Apollo 13 detailed malfunction inventory and LMS mapping

- **Status:** **DEFERRED**
- **Bounded question:** Must the project now extract the complete malfunction-procedure tab/symptom inventory and map it to LMS Section 2?
- **Implementation dependency:** a selected nonnominal Apollo 13 LM failure, or reconstruction of an Apollo 13-period LMS exercise requiring proof of simulator injectability.
- **Decision sensitivity:** specific symptoms/procedures and LMS availability could change what the player sees and what failure the scenario may legitimately claim to reproduce.
- **Decision-relevant findings:** research 328 directly observes several tab labels from indexed primary OCR but explicitly does not claim a complete inventory. Research 325–326 separate crew operational procedures from instructor-side LMS mechanisms.
- **Remaining gaps and disposition:** complete tab/page inventory, symptom headings, page-level change marks, Change A delta, and any crew-procedure ↔ LMS mapping remain unresolved. No selected current scenario requires a complete inventory, so they are deferred rather than continuously mined.
- **Closure challenge:** the 73.6 MB public scan remains too large for the current direct web fetch path, and targeted searches did not expose a reliable primary page-by-page substitute. Secondary artifact descriptions remain discovery aids only.
- **Reopen triggers:** selection of a specific Apollo 13 LM malfunction branch; need to validate a player-visible symptom/procedure; selection of a documented LMS training case; or acquisition of direct page-level access.

---

## Closure record G — Apollo 13 simulation failure-planning rule

- **Status:** **SUFFICIENT**
- **Bounded question:** Is there enough Apollo 13-period evidence to constrain scenario failure selection at the operational level without reconstructing LMS instructor mechanics?
- **Implementation dependency:** scenario-authoring and validation rule.
- **Decision sensitivity:** failure scope and persistence can change the procedure players should execute and can create negative training if represented incorrectly.
- **Decision-relevant findings:** research 327 uses the Apollo 13 Mission Operations Report to establish that failure scope determines applicable procedure, simulated failures should be selected to exercise the intended procedure, and simulation mistakes should be corrected rather than preserved as negative training.
- **Remaining gaps and disposition:** exact LMS controls, scripts, and injectability remain separate/deferred. They are not needed for this operational authoring rule.
- **Closure challenge:** the LMS archival searches above produced no evidence contradicting this operational rule and no requirement to bind it to a particular LMS injection mechanism.
- **Reopen triggers:** a stronger Apollo 13-period source materially contradicts the rule or a selected historical exercise requires instructor behavior beyond this operational constraint.

---

## Closure record H — PC+2 historical numerical-model readiness

- **Status:** **BLOCKED**
- **Bounded question:** Can the current Apollo 13 PC+2 model profile close its unresolved historical numerical gates by recovery or D-022 demonstrated irrelevance?
- **Implementation dependency:** promoting the PC+2 numerical/model profile from partial/unresolved historical readiness to a historically validated state at controller-product resolution.
- **Decision sensitivity:** mass properties, DPS performance, trim, trajectory/tracking configuration, or historical acceptance criteria could alter historically claimed numerical behavior.
- **Decision-relevant findings:** research 214 surveyed the open gates and found **no valid fully sourced same-input interval** for a D-022 endpoint test. Semantically different values and generic hardware limits may not be converted into invented uncertainty ranges.
- **Remaining gaps and disposition:** the missing same-input bounds/values remain material to historical numerical validation. The validation harness, causal architecture, player lab, and multi-human play work may continue, but the historical numerical-readiness claim remains blocked.
- **Closure challenge:** the survey already enumerated the candidate artifacts required to change the result. No current source supplies the missing same-input ranges. Repeating D-022 tests without new source evidence would not be meaningful.
- **Reopen triggers:** recovery of Apollo 13 DPS Supplement 2; LM-7 acceptance/calibration or PC+2 high-speed propulsion data; H-2 mass-property/depletion working records; the final PC+2 GDA/P30 artifact; or a source-backed historical product resolution/tolerance paired with a valid input range.

### Consequence

Stop broad numerical-gate searching and do not schedule D-022 sensitivity work until one of the named source conditions is met. Keep this status distinct from software correctness and playability validation.

---

## Active exception — Apollo 11 powered-descent reference

- **Status:** **OPEN**
- **Reason:** the second architecture reference still has explicit current dependencies: landing-radar geometry/reference computation, downstream estimator/filter behavior, powered-descent trajectory/propulsion, controller-product interfaces, and sourced decision rules. Those questions can materially change the reusable engine and eventual Apollo 11 runtime.
- **Stop condition:** apply D-024 separately to each bounded question as those dependencies are resolved. Do not keep the entire Apollo 11 domain permanently OPEN.

## Portfolio operating rule

After this review:

1. Do not use "continue LMS research" as a standing roadmap task.
2. Use named reopen triggers and retrieval conditions from this file.
3. A new source discovery may be cataloged without automatically reopening a closed/deferred question.
4. A DEFERRED question becomes OPEN only when a current implementation dependency is named.
5. A BLOCKED question receives targeted retrieval work, not repeated broad searches.
6. SUFFICIENT means sufficient for the stated implementation scope, not historically complete.
