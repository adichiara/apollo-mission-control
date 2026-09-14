# 136 — Orbiter and Project Apollo–NASSP reference assessment

Status: **modern implementation references reviewed; not historical Apollo evidence**

## Sources

### Orbiter Space Flight Simulator

- Repository: https://github.com/orbitersim/orbiter
- Technical wiki: https://www.orbiterwiki.org/wiki/Orbiter
- Dynamics reference source: https://github.com/orbitersim/orbiter/blob/main/Doc/Orbiter%20Technical%20Reference/dynamics.tex
- License: MIT (core repository): https://github.com/orbitersim/orbiter/blob/main/LICENSE

Orbiter describes itself as a Newtonian-mechanics spaceflight simulator. Its technical reference documents translational and rotational state propagation, multiple integration methods, timestep/accuracy considerations, quaternion orientation, and orbit-stabilization techniques.

### Project Apollo — NASSP

- Project site: https://nassp.space/index.php/Main_Page
- Repository: https://github.com/orbiternassp/NASSP
- LM descent-propulsion header: https://github.com/orbiternassp/NASSP/blob/Orbiter2016/Orbitersdk/samples/ProjectApollo/src_lm/lm_dps.h
- LM descent-propulsion implementation: https://github.com/orbiternassp/NASSP/blob/Orbiter2016/Orbitersdk/samples/ProjectApollo/src_lm/lm_dps.cpp
- License: GPL-2.0 lineage: https://github.com/orbiternassp/NASSP/blob/Orbiter2016/NASSP-LICENSE.txt

NASSP is an Orbiter add-on intended as an Apollo study simulator. It supports Virtual AGC and implements extensive command-module and lunar-module panels and systems.

## Evidence classification

Neither project is a primary source for Apollo hardware, Mission Control, or simulator behavior.

Use them as:

- implementation reconnaissance;
- source-discovery aids;
- independent comparison targets;
- examples of numerical and subsystem decomposition;
- warnings about approximation and coupling pitfalls.

Do not cite their behavior as proof that Apollo behaved that way.

## Orbiter: useful role

Orbiter is especially useful for examining:

- integrator choices and error behavior;
- translational/rotational state contracts;
- attitude representation;
- timestep sensitivity and convergence;
- separation between rendering cadence and physical propagation;
- possible independent trajectory regression comparisons.

The MIT license makes reuse legally less restrictive than NASSP, but no Orbiter dependency or code adoption is currently justified. The first project proof is narrower and should remain easy to audit against primary Apollo sources.

## NASSP: useful role

NASSP is particularly useful as a map from a simulated Apollo mechanism to likely documentary provenance. Its LM DPS implementation exposes boundaries for:

- propellant and pressurization inputs;
- engine valves and start/cutoff state;
- throttle command and thrust;
- chamber pressure;
- gimbal actuators;
- specific impulse and mass flow;
- erosion and transient behavior.

The implementation also visibly contains assumptions, simplifications, constants attributed to other documents, and unresolved/TBD behavior. Examples in the reviewed DPS files include fixed placeholder temperatures, simplified venting/erosion behavior, and low-thrust specific-impulse handling created to avoid an unphysical result.

That is useful evidence about what we must make explicit in our own model. It is not a license to inherit the numbers.

## Licensing boundary

NASSP files carry GPL-2.0-or-later notices and the repository is presented as GPL-2.0. Do not copy NASSP code, equations expressed as code, or implementation structure into this project without a deliberate license decision.

For the current work:

- inspect NASSP to discover candidate mechanisms and source citations;
- trace any numeric value or equation back to a primary document;
- write an independent implementation from those primary sources;
- use black-box/result comparisons only when the comparison conditions are documented.

Orbiter's core is MIT-licensed, but source attribution and technical verification are still required before reuse.

## Recommended priority

1. Extract primary LMS/AMS and Apollo spacecraft documentation.
2. Define our narrow model contract and assumptions from those sources.
3. Use Orbiter to challenge numerical-method and convergence choices.
4. Use NASSP to identify missed mechanisms and documentary leads.
5. Compare outputs only after initial conditions, frames, and units are aligned.

This keeps modern simulator work valuable without allowing it to upgrade historical evidence labels.
