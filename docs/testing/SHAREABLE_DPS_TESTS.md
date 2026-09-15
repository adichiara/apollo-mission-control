# Shareable causal-model tests

Open `/admin`, select **MODEL**, then **OPEN CAUSAL MODEL LAB** (or open `/model-tests` directly).
Enter the facilitator token if it is not already available from the test console.

The page is validation infrastructure. It does not create, reset, advance, or modify a mission session.

## DPS numerical suite

Click **Run standard suite** to exercise the mission-neutral DPS model through the protected server API.

The suite checks:

- mass depletion;
- impulse;
- an independent rocket-equation expectation;
- numerical step refinement;
- early/nominal/late cutoff ordering;
- lower thrust;
- thrust direction;
- omitted burn;
- combined errors;
- repeatability;
- multi-segment behavior;
- cutoff followed by coast;
- linear thrust ramps;
- segment-specific effective-Isp override behavior;
- propellant-floor rejection;
- build identity before/after the suite.

Add observations in Notes and download/copy the JSON report when a durable test record is needed.

## Trajectory → tracking observation

The site now exposes the composed endpoint:

`POST /api/admin/model-proof/trajectory-tracking`

The browser shows the causal separation between:

`authoritative trajectory → geometric tracking truth → controller-visible observation`

Inputs include synthetic initial state, thrust/coast duration, mass/Isp, numerical step, observation delay/bias, availability, and validity.

The page intentionally presents the authoritative trajectory and downstream observation separately. The geometric-truth calculation remains an internal causal boundary rather than being relabeled as a controller product.

## Exercise malfunction → explicit causal insertions

The lab exposes:

`POST /api/admin/model-proof/malfunction-plan`

This proof models the exercise/simulator-control layer recovered from Apollo simulator documentation:

`exercise malfunction intent → one or more explicit causal insertions`

A single synthetic malfunction can emit multiple insertions at distinct layers such as `vehicle_system` and `telemetry`. The scheduler also supports manual, preprogrammed, and time-dependent activation semantics.

The proof deliberately stops there. It does not apply the insertions to downstream subsystem, telemetry, controller-product, or mission-outcome models.

The timed-plan test can also demonstrate that an insertion is rejected before its configured activation time.

## Resource → power → observation

The site also exposes:

`POST /api/admin/model-proof/resource-power-observation`

The browser trace is:

`finite resource → electrical source availability → powered receiver → controller observation`

The **Compare before/after depletion** control runs the same chain on both sides of the calculated depletion boundary so the downstream loss of observation can be inspected without a scripted "tracking failed" outcome.

The composed endpoint still rejects direct electrical-source availability override. Source availability must derive from the configured resource coupling.

## Guidance-computer alarm → restart recovery

The lab exposes:

`POST /api/admin/model-proof/guidance-alarm`

The browser supplies the active program, alarm code/meaning, whether the alarm invokes software restart, and whether the active program is restart-protected.

The visible chain is:

`program state → alarm classification → optional software restart → recovery state`

Alarm/restart classification is caller supplied. The generic model does not emulate AGC scheduling, infer guidance validity, or issue an abort/continue recommendation.

The default browser values are synthetic; historical Apollo alarm/program values remain profile/source data, not generic UI defaults.

## Guidance comparison / consensus

The lab exposes:

- `POST /api/admin/model-proof/guidance-crosscheck`
- `POST /api/admin/model-proof/guidance-consensus`

These proof surfaces accept synthetic independent observations, caller-supplied tolerances, observation times/freshness limits, and (for consensus) quorum.

They deliberately do **not**:

- identify a hidden-truth source;
- label a source outside consensus as failed;
- issue GO/NO-GO or abort/continue.

The browser can run pairwise comparison, three-source consensus, and a stale-source case while showing pairwise residual/freshness evidence separately from agreement topology.

## Landing-radar quality → update eligibility

The lab exposes:

`POST /api/admin/model-proof/landing-radar-quality-update`

The chain is:

`raw radar/Data Good state → measurement qualification → qualified channels → update eligibility`

The composed API uses the existing generic measurement-quality and update-gate models. A rejected quality channel is withheld from the downstream update assessment instead of being silently passed through.

The proof requires explicit SI units (`m` and `m/s`) for channels mapped into the update gate. It rejects other units rather than performing an undocumented implicit conversion.

The downstream estimator/filter remains outside this proof.

## Evidence boundary

Every site-facing proof is explicitly labeled **NOT HISTORICALLY VALIDATED**.

The default values are synthetic test values, not Apollo constants. A successful run demonstrates model/API causality and numerical behavior only. It does not establish:

- Apollo 11 or Apollo 13 historical accuracy;
- historical subsystem constants;
- historical display resolution;
- crew behavior;
- controller procedures;
- player-facing station fidelity.

## Reports

DPS suite exports include schema/suite versions, UTC timestamps, build metadata, complete request/response pairs, checks with expected/actual values and tolerances, errors, and optional notes.

Interactive causal-chain runs are also appended to the export as `causal_runs` when a DPS report exists.

Facilitator tokens and request headers are excluded. Do not put secrets in notes. Browser report state is in-memory and is lost on refresh/navigation unless copied or downloaded.

## Reproduction

Use the recorded request object against the same endpoint/build with facilitator authorization. Compare numerical values using explicit tolerances rather than rounded screenshots.

Implementation verification uses repository CI. Browser interaction against the deployed site remains a separate live-validation step.
