# Station research status — Apollo 11 P66 manual-landing monitoring

Date: 2026-09-21

## GUIDANCE

**Status: research-sufficient for the manual-takeover monitoring boundary.** NASA TM X-58038 establishes continued descent guidance monitoring through comparisons among PGNS, AGS, and MSFN-derived ground tracking. P66/manual takeover changes who controls the landing trajectory; it does not erase ground navigation observations.

Do not infer an exact Mission-G CRT field or a dedicated `P66` ground annunciator from this evidence.

## FLIGHT

**Status: research-sufficient for decision semantics.** Flight Mission Rule 5-91 establishes that, after crew takeover, trajectory/guidance constraints are not themselves abort causes. FLIGHT may therefore continue receiving controller assessment while the meaning of a trajectory deviation changes from the automatic-guidance phase.

This is not evidence that all abort authority disappears. Propellant, systems, and other independently sourced abort criteria remain separate.

## CONTROL

**Status unchanged for systems/propellant monitoring.** The manual-control transition does not supersede the already documented CONTROL propellant-countdown path. The later landing-radar-data loss is an observation event and must remain distinct from hidden physical truth.

## CAPCOM

**Status unchanged.** No primary evidence recovered in this pass establishes a special CAPCOM P66 call. Do not invent one.

## Simulator station boundary

After P66:

`station observations continue → GUIDANCE/other stations assess → FLIGHT receives assessment → trajectory deviation alone is not an abort trigger`

The station projections should therefore preserve observations across the manual-takeover transition while the decision-gate layer changes the applicable rule semantics.

## Next station work

Implementation should add the sourced P66/manual-control state to the Apollo 11 descent decision gate before further broad display research. Reopen exact P66 ground indication/keying only if a player-facing station product makes it material.

## Evidence status

- **GUIDANCE:** sufficient for continued-monitoring semantics; exact display unresolved.
- **FLIGHT:** sufficient for post-takeover trajectory-rule semantics.
- **CONTROL:** no change; countdown evidence remains separately sourced.
- **CAPCOM:** no unique P66 call established.