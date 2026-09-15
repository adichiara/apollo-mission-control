# Research note 216 — LMS source hierarchy and numerical-integration boundary

Date: 2026-09-15  
Status: **SOURCE HIERARCHY VERIFIED; full mathematical/subsystem extraction still pending.**

## Question

Which surviving Lunar Module Mission Simulator sources should govern the next causal-engine extraction, and what can be said now about numerical integration without overclaiming a simulator-wide timestep?

## Located LMS sources

### Lunar Module Mission Simulator Instructor's Handbook, Volume I — Simulator Description

Virtual AGC's document-library change log identifies this handbook as a direct LMS source and describes it as containing:

- detail on simulator switches and displays; and
- information about how the LM subsystems are simulated.

A NASA bibliographic index independently identifies the LMS Instructor's Handbook lineage as Grumman LMA790-2-LMS, dated 1 April 1967, with Volume I and portions of Volume II.

**Use:** subsystem-simulation boundaries, simulator interfaces, controls/displays, and instructor-visible state.

**Do not infer yet:** exact Apollo 13 LMS subsystem equations, constants, failure inventory, or update cadence until the relevant pages are extracted.

### Proposal for LEM Mission Simulator, Volume II — Technical Addendum: Glossary of Symbols

Virtual AGC identifies this direct simulator-design document and notes that, despite the title, it contains many flowcharts showing mathematical equations underlying the LMS.

**Use:** mathematical-model families, variable definitions, equation flow, subsystem coupling, and candidate model interfaces.

**Do not infer yet:** that every proposal equation survived unchanged into the accepted 1967/1970 LMS configuration.

### Grumman LED 500-5 — LMS Math Model: Equations of Motion, Subsystem Interfaces and Visual Display Drive Equations

NASA/NARA corporate-index evidence identifies:

- title;
- date: 22 April 1965;
- MSC accession: *66-10469;
- contract NAS 9-1100.

The title itself establishes an explicit source boundary among:

- equations of motion;
- subsystem interfaces; and
- visual-display drive equations.

**Use now:** source-priority and abstraction-boundary evidence.

**Do not use yet:** specific equations/constants until the report text is directly recovered.

### Grumman LED 500-16 — LEM Guidance Computer Math Model for FMES and LMS

Corporate-index evidence identifies:

- date: 8 June 1966;
- MSC accession: *66-13246;
- contract NAS 9-1100.

This confirms that the LGC had a dedicated simulator math-model boundary shared across FMES/LMS.

**Use now:** preserve guidance-computer model/configuration as a distinct domain/interface rather than folding it into generic trajectory logic.

**Do not use yet:** specific LGC simulator behavior without the report text or equivalent primary material.

## Fifty-millisecond timestep evidence

TechWorks catalogs a Grumman document titled:

*Effect of LMS Fifty-Millisecond Integration Steps on Simulated Response of Abort Attitude Control System*

That title is meaningful but narrow.

It supports only:

- an LMS integration step of 50 ms was relevant to a study of simulated Abort Attitude Control System response; and
- numerical timestep sensitivity was important enough to receive dedicated engineering analysis.

It does **not** establish:

- 50 ms as a universal LMS integration step;
- one shared step for all subsystem models;
- the integration algorithm;
- acceptance error/tolerance;
- that Apollo 13-era LMS retained the same step/configuration.

## Project numerical-integration rule

Until direct LMS mathematical-model or acceptance/correlation evidence establishes otherwise:

1. each reusable numerical model declares its own update/integration policy;
2. no project-wide historical Apollo timestep is asserted;
3. timestep sensitivity is validated numerically for the model being implemented;
4. model-specific step requirements may be mission/profile configuration only when sourced;
5. fixed-step or variable-step choices remain project numerical methods unless historically established.

This is consistent with the existing DPS/translational proof architecture, where `max_step_s` is an explicit numerical configuration rather than an Apollo constant.

## Source hierarchy for future extraction

For an LMS subsystem or equation, prefer evidence in this order:

1. accepted/mission-era LMS math-model or instructor-handbook text;
2. LMS-specific engineering memos, validation/correlation, simulator-output dictionaries, or acceptance documents;
3. spacecraft operations handbooks / subsystem engineering reports for real vehicle mechanism;
4. mission-specific Apollo 13 LM-7 procedures, telemetry/configuration, and flight data for applicability;
5. early proposal material for model lineage/structure only;
6. AMS documents for cross-simulator architecture precedent only.

No lower tier should silently override a higher-tier mission-specific source.

## Architecture consequences

The reusable engine should continue to preserve distinct interfaces for:

- vehicle equations of motion;
- subsystem models;
- guidance-computer behavior;
- instrumentation/display drive;
- simulator/exercise control.

The next extraction should seek the **actual variable/equation interfaces** connecting these domains, not merely additional document titles.

## Next source targets

1. directly extract LMS Instructor's Handbook Volume I subsystem-simulation sections;
2. directly extract the LMS proposal math-flowcharts;
3. recover LED 500-5 or equivalent equations-of-motion/interface pages;
4. recover the 50 ms AACS engineering memo and determine exactly which integration loop/model it studied;
5. locate LMS acceptance, validation, correlation, or simulator-output documents that define numerical tolerances.

## Sources

- Virtual AGC document-library change log, 13 February 2022 LMS additions.
- NASA bibliographic index entry for LMA790-2-LMS Instructor's Handbook, 1 April 1967.
- TechWorks archival-document catalog, Grumman LMS math-model and 50 ms AACS integration-step entries.
- NASA/NARA corporate index records for LED 500-5 and LED 500-16, as cataloged in the project simulation-engine source record.
