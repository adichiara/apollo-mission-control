# 2026-09-14 — Public AMS handbook and modern simulator references

## Completed

- Replaced the inaccessible Scribd route with the public ibiblio/Virtual AGC AMS handbook scan.
- Corrected the source identity: the linked 1965 document is AMS Volume II, while the LMS Volume I handbook is a separate archive item.
- Extracted the AMS operational-program partition, closed equations-of-motion loop, MIU malfunction paths, Mission Control interface, and telemetry boundaries.
- Classified Orbiter as a modern numerical/dynamics reference.
- Classified Project Apollo–NASSP as a modern implementation and source-discovery reference, with an explicit GPL boundary.
- Preserved the distinction between historical primary evidence and modern simulator implementations.

## Architecture effect

The AMS handbook directly strengthens the project's separation of:

- authoritative physical state;
- simulated subsystem state;
- onboard indications and visual outputs;
- telemetry/communications interfaces;
- externally injected physical and observation failures.

Orbiter and NASSP do not change accepted historical claims. They provide implementation-review and validation leads after primary-source extraction.

## Remaining work

- extract the separately archived LMS Instructor's Handbook Volume I;
- locate/extract AMS Volume III output and malfunction tables;
- trace NASSP DPS citations and constants to primary Apollo documentation;
- freeze Apollo 13/LM-7 inputs, frames, and acceptance tolerances before historical-validation claims.
