# Progress — LMS deployed compute-topology boundary

Date: 2026-09-17

## Completed

Research note 230 adds deployed-system evidence that was missing from the simulator-architecture workstream.

A contemporaneous July 1970 technical article by Malcolm O. Brown and John G. Waters describes **each of the two LMS installations** as containing a **three-machine digital computer complex**, digital-conversion electronics, an accurate LM cockpit crew station, an infinity-optics visual system, and an instructor-operator console.

Albert A. Jackson's later first-person account of his Houston LMS instructor experience describes the Houston complex/room as containing **four DDP-224 computers**.

The repository now preserves that discrepancy instead of resolving it by assumption.

## Architecture consequence

No executable constant changed.

The source tension reinforces the current design rule that processor count is not a proxy for simulation-domain count. Dynamics, subsystem state, guidance/computer behavior, instrumentation/telemetry, visual effects, simulator control, and MCC interfaces remain explicit functional boundaries regardless of how the historical LMS distributed those functions across machines.

Likewise, no universal 20 Hz / 50 ms / other solver cadence is inferred from the computer complex. Research note 216's 50-ms AACS evidence remains context-specific.

## Source catalog

Added:

- `resources/source-catalog/LMS_DEPLOYED_COMPUTE_TOPOLOGY.md`

The catalog records the source hierarchy and the unresolved three-machine/four-DDP wording explicitly.

## Next work

Prefer configuration-controlled records that can map:

`DDP-224 machine → loaded program/model → update/integration schedule → output/interface`

Highest-value targets remain LMS Section 7, program-loading/configuration records, and RG 255 E.155B/E.155B1 technical/acceptance holdings.
