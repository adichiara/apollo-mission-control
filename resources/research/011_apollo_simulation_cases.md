# Research Note 011 — Apollo Simulation Cases

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Apollo 13 premission simulation schedule

The Apollo 13 Mission Operations Report preserves a detailed premission MCC/MSFN support schedule.

Named simulation activities include LOI, LM activation/descent, TLI, ascent, descent aborts, launch aborts, reentry, lunar surface, DOI, TEI, FIDO/BSE math-model work, lunar impact, combined CSM/LM ascent/descent, network simulation, and tracking/data-flow and communications validation.

### What this proves

NASA trained discrete mission phases and contingency classes repeatedly rather than treating “Apollo mission simulation” as one monolithic exercise. The schedule does not identify the malfunction set injected into each run, so these are scenario-family evidence, not finished scenarios.

## Simulation-design philosophy evidence

Harold Miller's retrospective NASA paper says simulations were normally segmented by mission phase; developed teamwork and procedures; inserted failures to exercise procedures, ground rules, and communications; closed the command loop; and routed simulated spacecraft data through control-center systems. This strongly supports the project's architecture.

## Apollo 11 lunar-landing simulation evidence — keep the accounts separate

Two related but **not yet proven identical** historical accounts must not be collapsed into one event.

### Miller / Honeycutt recollection

Harold Miller recalls that Dick Koos was lead simulation supervisor for the lunar-landing mission and that Jay Honeycutt handled the lunar-landing segment. Miller specifically says Honeycutt ran a simulation “showing the computer failure light.” Miller's paper does **not** identify that indication as a 1201 or 1202 program alarm, does not date the run, and does not say that this was the simulation that produced the later program-alarm response guidance.

Source: Harold G. Miller, *The Early Days of Simulation and Operations*, NASA historical paper, p. 8 in the current PDF scan: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/MillerHG/MillerHG_paper.pdf

### Program-alarm training account

Separate Apollo 11 historical material documents preflight training involving program-alarm decision response and the importance of distinguishing alarms that required abort from alarms on which flight could continue. That evidence should be cited and reconstructed on its own terms. Until a source explicitly links it to Miller's Honeycutt “computer failure light” recollection, the repository must treat the two as separate evidence threads.

### Resolution of the previous conflation

A previous repository revision called the Honeycutt recollection and the better-known program-alarm training account one “computer-failure/program-alarm simulation.” That identity is **not established by the sources currently reviewed** and is withdrawn.

This does not diminish either account's design value: both show that simulation exposed controller decision-rule gaps. It only prevents us from inventing an equivalence between different indications, personnel assignments, or runs.

## Archive question

Miller states that simulations were documented more systematically after Mercury-Atlas 7 but that he did not know whether the material had survived. Search targets remain JSC History Collection, University of Houston-Clear Lake, National Archives holdings, and individual controller collections for case sheets, SimSup scripts, malfunction lists, debriefs, schedules, and Simulation Design Section material.

## Sources

- Apollo 13 Mission Operations Report: https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
- Harold G. Miller, *The Early Days of Simulation and Operations*: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/MillerHG/MillerHG_paper.pdf
- Apollo 11 Lunar Surface Journal program-alarm materials: https://history.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.1201-fm.html
