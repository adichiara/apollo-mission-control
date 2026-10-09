# Apollo 11 Descent Execution Readiness — D-024 Review

Date: 2026-10-08  
Scenario: `apollo11_descent_program_alarm_reference`  
Runtime adapter: `apollo11_descent_v1`

## Purpose

Apply D-024 to the seven model domains currently named by the Apollo 11 descent scenario and separate three different questions that had been conflated:

1. Is the **research** sufficient for the current reference-event/player-product resolution?
2. Is a reusable **causal model** historically validated?
3. Is the **live scenario** ready to execute for players?

These are not interchangeable.

A D-024 result of **SUFFICIENT** does not upgrade a model-profile status from `partial` to `validated`. Likewise, a model can remain incomplete while the current reference-event scenario has enough historical evidence to avoid inventing behavior.

The live scenario remains gated while this review is implemented. This document does not itself enable Apollo 11 session creation.

## Current runtime resolution

The implemented adapter currently provides:

- authoritative continuous GET and scenario-event progression;
- source-controlled PDI reference time and nominal Flight Plan phase anchors;
- explicit station ownership for FLIGHT, CAPCOM, GUIDO, CONTROL, and TELCOM;
- explicit readiness → FLIGHT → CAPCOM authority boundaries;
- a read-only descent projection;
- explicit, caller-supplied landing-radar controller state;
- explicit, caller-supplied guidance-computer state;
- explicit controller-product projection through the Apollo 11 product schema.

It deliberately does **not** currently require:

- a continuously generated as-flown trajectory;
- stochastic landing-radar measurements;
- an automatically generated PGNCS/AGS/MSFN comparison;
- hidden-state-to-controller-product routing;
- automatic alarm disposition or automatic landing GO/NO-GO.

Those distinctions drive the D-024 classifications below.

## Domain review

| Domain / bounded question | D-024 state | Current consequence |
| --- | --- | --- |
| **Guidance computer — are 1201/1202 meaning, restart protection, program/alarm chronology, and controller-product semantics sufficient for a fixed historical/reference-event descent?** | **SUFFICIENT** | The reference runtime may carry explicit source-backed alarm/program events and an explicit guidance-computer state. Exact real-time Executive workload generation is not required at this resolution. |
| **Guidance computer — can the simulator generate historically exact counterfactual 1201/1202 occurrence from workload state?** | **DEFERRED** | No current selected branch requires synthetic alarm creation. Reopen only for counterfactual workload/alarm scenarios. |
| **Backup guidance — must AGS be a causal numerical model for the current reference-event scenario?** | **DEFERRED** | Current station/decision topology can use explicit controller observations/readiness without executing an AGS state propagator. Reopen when a branch depends on AGS causal behavior or backup control. |
| **Guidance monitoring — are source pairs, comparison fields/limits, two-out-of-three topology, and human authority sufficient for the current decision architecture?** | **SUFFICIENT** | Existing explicit controller products and human readiness calls may be used without inventing an automatic comparison decision. |
| **Guidance monitoring — can an automated historically timed PGNCS/AGS/MSFN comparison execute?** | **BLOCKED** | Research 218 leaves permissible inter-source observation-time separation/freshness unresolved. PFP cadence is not a substitute. Do not invent `max_time_separation_s`. |
| **Landing radar — are deterministic Apollo-11-effective DATA GOOD/update chronology, scaling, reference projection, weighting/update logic, and controller field semantics sufficient for explicit reference-event products?** | **SUFFICIENT** | The current adapter may use explicit/source-backed LR states and products. It need not generate a stochastic sensor stream. |
| **Landing radar — can Apollo-11-effective stochastic measurement/error behavior be generated historically?** | **BLOCKED** | LM-5/Apollo-11-effective numerical residual/quantization/error-distribution evidence remains unavailable. |
| **Propulsion — must a historically calibrated LM-5 thrust/mass-flow model execute in the current reference-event adapter?** | **DEFERRED** | The current adapter uses documented phase/reference events rather than generated trajectory. Do not force unresolved propulsion constants into the adapter. |
| **Propulsion — can a generated historical LM-5 powered-descent trajectory rely on flight-effective thrust/calibration?** | **BLOCKED** | LM-5 Operational Calibration Curves and related direct FTP/performance evidence remain on named archival recovery paths. |
| **Translational dynamics — must an exact continuous as-flown trajectory be generated for the current reference-event adapter?** | **DEFERRED** | The current runtime can preserve documented anchors/products without claiming a continuous as-flown truth history. |
| **Translational dynamics — can an exact continuous Apollo 11 flown descent history be treated as documented truth?** | **BLOCKED / RECONSTRUCTED ONLY** | Open archival evidence does not supply a complete direct as-flown trajectory. Any continuous reconstruction must remain explicitly reconstructed/estimated rather than historical truth. |
| **Controller observation — are field semantics and station/decision topology sufficient for the current player-product boundary?** | **SUFFICIENT** | Research 502 and 600 establish the needed field family and front-room authority topology. A neutral project routing layer may carry explicitly supplied products without naming unsupported historical internals. |
| **Controller observation — can exact Mission-G per-field source IDs, engineering conversion, CCATS/RTCC ownership, request cadence, and display timing be claimed?** | **BLOCKED** | The named Mission-G PHO-TR155/Data Formats/data-pack material remains unrecovered. Exact historical internal ownership/cadence must remain absent. |

## What this means for the model profile

The current `apollo11_g_descent_partial` model profile should remain **not historically validated**.

No domain status is upgraded merely because a bounded D-024 question is sufficient.

Instead, the profile notes should distinguish:

- capabilities sufficient for the fixed reference-event architecture;
- capabilities not exercised by that architecture and therefore deferred;
- capabilities that remain blocked for generated historical behavior.

This prevents the model catalog from becoming a second research-status system.

## What this means for scenario execution

The current strict `execution_requires_validated_model` gate remains conservative and stays closed in this change.

However, the review shows that “all seven model domains must become fully validated” is not the correct long-term execution criterion for the **reference-event** scenario. Several listed domains are deliberately not executed by the adapter.

The next implementation task is therefore to define a scenario-specific execution contract that distinguishes:

### Required before a source-bounded reference-event player session

- explicit player-visible controller-product feed for the selected interval;
- explicit provenance for every populated product;
- no hidden-state back-fill;
- explicit readiness/FLIGHT/CAPCOM authority;
- source-backed event chronology for any replayed onboard/vehicle state;
- visible labeling that this is a historical reference-event reconstruction rather than a continuously validated as-flown trajectory;
- human part-task/playability evidence for the player surface being used.

### Required only before generated historical causal behavior is claimed

- historically timed automated PGNCS/AGS/MSFN freshness/comparison behavior;
- stochastic Apollo-11-effective landing-radar measurement behavior;
- LM-5 flight-effective propulsion calibration for generated descent dynamics;
- historically validated continuous trajectory/dynamics configuration;
- exact Mission-G internal ground-routing/cadence when such ownership/timing is itself asserted.

## Critical paths

### Reference-event runtime

No broad archival search is on the critical path.

The immediate critical path is implementation and validation of an explicit controller-product feed using already sufficient field/decision evidence, followed by human interface checkout.

### Generated historical descent dynamics

Critical archival paths include:

- LM-5 Operational Calibration Curves, Volume II, NARA Fort Worth RG 255, FRC accession 72-A-1116 / agency box 71;
- other named LM-5 FTP/performance records already cataloged;
- any source needed to bound the exact causal outputs that will become player-visible.

### Automated historical guidance cross-check

Critical evidence is a source-backed rule/range for relative PGNCS/AGS/MSFN observation freshness/synchronization. Research 218 explicitly forbids substituting the 0.2/0.4 s PFP processing interval.

### Exact Mission-G product routing

Critical evidence remains the named PHO-TR155 / Mission-G Data Formats / associated display-data-pack or computer-listing material.

## Closure result

The broad question “continue Apollo 11 powered-descent research” should no longer remain OPEN.

The **architecture/reference-event research question is SUFFICIENT** for the current adapter resolution.

Future Apollo 11 research is reopened only for one of the scoped blockers above or another named implementation dependency. The next roadmap work is implementation of the explicit reference-event player-product feed and its validation, not another broad evidence sweep.
