# 166 — Apollo 11 powered-descent guidance monitoring fields and limits

## Purpose

Close part of the Apollo 11 second-reference guidance cross-check gap without inventing a freshness rule or collapsing Mission Control's multi-source guidance monitoring into a single boolean.

## Primary Apollo 11 evidence

MSC Internal Note 70-FM-20, *The Apollo 11 Adventure* (5 February 1970), describes the Guidance Analysis Section's real-time monitoring philosophy.

For lunar descent, Mission Control evaluated the LM Primary Guidance and Navigation System (PGNS) and Abort Guidance System (AGS) for descent-abort and guidance-switchover decisions. Guidance-system performance was assessed primarily through comparison of navigation and attitude references. Navigation comparisons used at least three independent systems:

1. PGNS;
2. AGS;
3. a groundtrack / powered-flight processor based on MSFN data.

The same report's Figure 4, *MCC velocity residual monitoring*, records the Apollo 11 powered-descent residual-monitoring logic.

Source scan:

- https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- Guidance Analysis Section: pp. 2-161 through 2-162.
- Figure 4, MCC velocity residual monitoring: p. 2-30.

## Source-bounded comparison fields and limits

The powered-descent flowchart supports the following profile entries.

### AGS versus PGNS — in-plane problem detection

Compared components:

- radial velocity residual;
- downrange velocity residual.

Limit represented in the flow: **10 ft/s** for each component.

An exceedance is not itself an automatic abort. It sends the monitoring logic to an independent powered-flight-processor/PGNS comparison to help isolate the discrepant system.

### Powered-flight processor / MSFN versus PGNS — in-plane isolation

Compared components:

- radial velocity residual;
- downrange velocity residual.

Isolation limit: **10 ft/s** for each component.

This is a separate independent comparison path, not another name for AGS/PGNS.

### Powered-flight processor / MSFN versus PGNS — PGNS failure limits

After the logic has identified a possible PGNS problem, Figure 4 gives larger flight limits:

- radial velocity residual: **35 ft/s**;
- downrange velocity residual: **30 ft/s**.

Apollo 11 Mission Rule 3-50 separately states that powered descent from PDI to low gate is to be aborted for PGNS navigation errors that cause AGS-PGNS or MSFN-PGNS velocity differences to violate the PGNS failure limits, with the rule's stated pre-landing-radar-incorporation applicability.

The project therefore stores the limits as monitoring evidence, but the generic comparison layer still does not issue an abort.

### AGS versus PGNS — crossrange problem detection

Figure 4 gives an AGS/PGNS crossrange monitoring limit of **20 ft/s**.

The remainder of the crossrange/misalignment logic is not encoded in this pass because several labels in the surviving scan are difficult to read and their exact applicability should be independently verified before becoming configuration.

## Important architecture consequence

Apollo 11 guidance monitoring should not be represented as:

`AGS agrees with PGNS = true/false`

The historical structure is closer to:

`AGS-PGNS residual -> independent PFP/MSFN-PGNS residual -> trajectory/altitude/radar context -> controller judgment`

This directly supports the project's independent-observation architecture.

## Freshness / cadence boundary

The reviewed primary material establishes comparison fields, source pairing, and several numerical limits, but it does **not** yet establish a safe executable value for:

- maximum allowed time separation between the compared observations;
- controller display update cadence;
- sample synchronization;
- maximum observation age for a GO/abort judgment.

The new historical profile therefore stores `max_time_separation_s = null`.

The profile loader refuses to construct an executable `GuidanceCrosscheckConfig` while that value is unresolved. This is intentional: the implementation must not turn a missing historical timing rule into a guessed one-second or multi-second freshness window.

## Attitude-reference boundary

The Guidance Analysis Section documents that attitude references were part of the comparison philosophy and shows AGS/PGNS attitude-related channels for powered-flight monitoring examples. This pass does not freeze a descent-specific attitude comparison tolerance because the reviewed Apollo 11 source does not yet give a sufficiently clear powered-descent numerical limit for that field.

## Model-profile consequence

The Apollo 11 `backup_guidance` domain remains **partial**, but the gap is narrower:

Resolved:

- source identities used in the comparison architecture;
- in-plane radial/downrange monitoring fields;
- 10-ft/s problem/isolation limits;
- 35/30-ft/s PFP/PGNS failure limits;
- 20-ft/s AGS/PGNS crossrange problem-detection limit.

Still unresolved:

- freshness/update cadence;
- complete descent attitude comparison fields/limits;
- remaining crossrange/misalignment thresholds;
- exact controller display presentation;
- complete alarm-to-abort/continue decision rule.

## Sources

1. NASA MSC Internal Note 70-FM-20, *The Apollo 11 Adventure*, 5 February 1970.
2. Apollo 11 Mission Rules, powered-descent Mission Rule 3-50.
3. NASA, *Apollo 11 Mission Report*, November 1969.

Adjacent Mission H-2-and-subsequent technique documents may be used to understand later architecture, but their limits are not substituted for Apollo 11 values in this profile.
