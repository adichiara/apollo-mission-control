# Open Questions

Questions remain open until research or an explicit project decision resolves them.

## Historical research

1. What exact controller complement and console responsibilities apply to each candidate Apollo mission/phase?
2. How did responsibilities change between early and late Apollo missions?
3. Which controller display formats survive in sufficient detail to reconstruct?
4. Which display formats were used by each controller during specific mission phases?
5. What parameters were available at each station, at what update rate, and through which ground processing?
6. Which console controls actually affected display selection/request?
7. What hard-copy products were routinely used?
8. What voice loops were available to each position and how were they used?
9. What Staff Support Room specialists backed each MOCR position?
10. Which documented integrated-simulation malfunction cases survive in usable detail?

Historical gaps should now be prioritized by scenario impact. An unresolved archival detail is not automatically a blocker; see the research-sufficiency rule in `PROJECT_PRINCIPLES.md`.

## Simulation scope

11. **RESOLVED:** first vertical slice is Apollo 13 PC+2 preparation/execution, approximately 74:00–80:00 GET. See Decision D-013 and research note 048.
12. How much of the spacecraft must be physically modeled for the PC+2 interval?
13. How much of MSFN/CCATS/RTCC behavior materially affects PC+2 controller decisions and therefore must be simulated?
14. Which sensor/telemetry failure modes are necessary for the first PC+2 scenario and later nonnominal variants?
15. Should crew actions be scripted, operator-driven, or otherwise represented? The first playable now uses explicit modeled crew-response steps for the ΔP branch, but the general architecture for later scenarios remains open.

## PC+2 vertical-slice definition

30. **RESOLVED for first playable:** initialize near 77:55 GET. See the canonical roadmap and research note 079.
31. **RESOLVED for first playable:** seven original station players are FLIGHT, CAPCOM, CONTROL, TELMU, GUIDO, FIDO/RETRO, and INCO; a source-constrained five-player compact mode is also supported. See notes 091–094.
32. Which additional PC+2-critical fields/products, if any, prove necessary after physical human/device validation for FLIGHT, FIDO/RETRO, GUIDO, CONTROL, TELMU, INCO, and CAPCOM?
33. **RESOLVED for first-playable workflow fidelity:** model the final PC+2 state-vector/target-load process as a staged cross-station workflow rather than a single generic verification flag: final FIDO/RTCC solution, GUIDO load readiness/consistency, INCO uplink configuration, CAPCOM/crew P00 + DATA/ACCEPT + UPDATA LINK configuration, transmission, and final-load completion/computer return. Ranging remains a separate final-prep dependency. Exact Cartesian vector contents, RTCC/CCATS internal command path, exact console/key sequence, and exact transmission duration remain deferred until demanded by propagator, exact-console, or failure-mode work. See research note 098.
34. **RESOLVED for the implemented shutdown branch:** player-observable shutdown criteria/evidence are explicitly separated into controller products/rules, crew callout/report, and fresh telemetry evidence without hidden physical-state leakage. See notes 053–072 and 082–086.
35. **RESOLVED for the current first playable:** immediate post-burn closure is an ordered source-backed transition: nominal cutoff/result and PGNS residual evidence, short post-burn spacecraft assessment, initial LM power-down beginning about 79+34 while retaining functions needed for communications/guidance/PTC, then PTC preparation (detailed procedure read at about 79+52). Exact console keying, an unsupported formal poll, switch-by-switch timing, and full PTC dynamics remain deferred unless physical play or later transearth-coast scope requires them. See research note 101.

## Player scaling

16. **RESOLVED for PC+2 at the current fidelity target:** five players are the minimum supported configuration. See note 094.
17. **RESOLVED for the supported five-player configuration:** TELMU+CONTROL may be assigned to one modern `LM SYSTEMS` player and GUIDO+FIDO/RETRO to one modern `FLIGHT DYNAMICS` player while preserving original station identities. No additional pairing is approved. See notes 091–094 and Decision D-018.
18. Are some positions phase-specific enough to omit rather than combine in later scenarios? For current PC+2, no additional omission is approved.
19. **RESOLVED for the current PC+2 first playable:** Staff Support Room/backroom functions are historically real and explicitly acknowledged, but are not separate playable roles yet. Do not silently transfer unsupported backroom analysis to front-room stations or invent automated expert advice. Reopen when a physical-play or later-scenario decision depends on a specific support-room product, calculation, recommendation, or handoff. See research note 100.

## Interface

20. How closely can phone screens reproduce the useful portion of original console displays without losing legibility? Physical validation remains required.
21. Should the simulated display preserve original aspect/character geometry exactly and use pan/zoom when necessary?
22. **RESOLVED for first playable:** modern join/rejoin, station-set persistence, compact substation switching, and facilitator authentication live outside the historical station-information model and are explicitly labeled project infrastructure. See notes 080, 087–093.
23. **RESOLVED for the initial first-playable packet structure:** use separate common-context, original-station, rule/criterion, nominal phase/procedure, and modern client-operation sections; compact players retain separate original-station sheets. This is a project adaptation, not an Apollo handout reconstruction, and physical usability remains to be validated. See notes 096–097 and `docs/testing/PC2_PLAYER_REFERENCE_PACKET.md`.

## Operations

24. Should simulation time ever be accelerated outside high-workload phases? Currently deferred; first playable runs at normal 1× continuous time.
25. **RESOLVED for first playable:** facilitator/admin controls provide reset/restart and exercise-wide lifecycle operations, separated from controller authority. See notes 087–089.
26. **RESOLVED for first playable:** use a dedicated human facilitator/SimSup function separate from controller stations; its credential/UI mechanics are modern infrastructure, not historical reconstruction. See note 088 and Decision D-017.
27. **RESOLVED for first playable:** post-simulation review uses incident-level evidence plus a structured debrief separating observed facts, participant interpretation, reproducible defects, historical questions, usability-only changes, instructional gaps, and legitimate uncertainty. See notes 095–097 and the live-play report template.

## Repository/resources

28. Should primary PDFs be mirrored under `resources/primary-sources/` or should the repository keep stable source links plus hashes/metadata?
29. What citation convention should code and data files use to identify historical provenance?

## Deferred EECOM / Apollo 13 configuration gaps

These remain useful archival targets but are not PC+2 blockers unless implementation shows otherwise.

36. Can a surviving copy of **PHO-TR155 Mission H-2 Revision C (issued 1970-03-06)** be located?
37. What were the exact Apollo 13 EECOM DRK key legends and arrangement?
38. What were the exact Apollo 13 EECOM limit-sense/event-indicator legends beyond the functions documented by the Review Board?
39. What did the Status/Status Report and Summary Message Enable keyboards do in Apollo 13 EECOM operations?
40. What was the analog-meter selection/use at the EECOM console?
41. What direct ground-command authority, if any, remained at Apollo 13 EECOM?
42. What were the complete EECOM display-format/channel IDs beyond the two preserved Review Board examples?
43. What exact user workflow did EECOM use for HSD Format 30 playback requests and review?