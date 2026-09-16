# Research note 220 — LMS User's Manual timing-pulse boundary

Date: 2026-09-16  
Status: **DIRECT LMS USER-MANUAL TIMING TEXT RECOVERED; numerical-integration mapping remains unresolved.**

## Question

Does surviving LMS operational documentation clarify the meaning of the recurring 50-millisecond timing evidence, and can that timing be promoted to a simulator-wide numerical integration step?

## Primary-source finding

A public scan titled **LMS User's Manual, Volume 1**, Update #34, dated **22 October 1971**, is present in the Virtual AGC / ibiblio document library:

https://www.ibiblio.org/apollo/Documents/LMS_Users_Manual.pdf

The current web viewer cannot render the approximately 89 MB scan end-to-end, but searchable text indexed from the primary PDF exposes a section titled:

**Operation of C-Computer Clocks and Interrupts**

That section states that when the LMS Central Timing Equipment (CTE) is switched to **half-time**:

- for the A, B2, and C computers, the **50 millisecond pulse is extended to 100 milliseconds**;
- for the C computer, the **10 millisecond pulse** used to increment the T1–T5 readable/programmable clocks is extended to **20 milliseconds**;
- the minute pulse is unaffected.

This is direct evidence that the LMS had multiple explicit computer timing/interrupt cadences and that CTE half-time operation scaled at least some of them.

## What this resolves

The previous evidence base contained a Grumman engineering-memorandum title:

*Effect of LMS Fifty-Millisecond Integration Steps on Simulated Response of Abort Attitude Control System*

Research note 216 correctly treated that title as narrow evidence and refused to promote 50 ms to a universal LMS timestep.

The LMS User's Manual strengthens that caution.

A **50 ms pulse existed as an LMS computer timing/interrupt quantity**. A separate **10 ms C-computer pulse** also existed. Therefore, the appearance of “50 milliseconds” in LMS documentation cannot by itself be interpreted as:

- the sole simulator scheduler rate;
- a universal subsystem update period;
- a universal differential-equation integration step;
- the cadence of every measurement/output path.

The new evidence makes the distinction between **computer timing pulses** and **model integration policy** more important, not less.

## What remains unresolved

The recovered passage does not establish:

- what software functions were serviced by each 50 ms interrupt;
- whether a specific dynamics or subsystem model advanced once per 50 ms pulse;
- whether some models subcycled at 10 ms or another cadence;
- whether the AACS study's phrase “50-millisecond integration steps” referred directly to this same 50 ms interrupt mechanism;
- the integration algorithm;
- numerical error/acceptance tolerances;
- whether Apollo 13-era LMS Update/configuration used the same timing arrangement as the October 1971 manual.

The 1971 User's Manual is later than Apollo 13. It is strong LMS architecture/operation evidence but not automatically Apollo 13 H-2 configuration authority.

## Architecture consequence

Project code should distinguish at least four timing concepts:

1. **authoritative simulation time / GET**;
2. **scheduler or event-service cadence**;
3. **model-specific numerical integration/update step**;
4. **measurement/output sampling or display cadence**.

A common value may be used for more than one layer only when a source or explicit project design establishes that relationship.

This is consistent with the current architecture in which individual numerical models declare their own integration/update policy and historical measurement profiles separately gate sample/output timing.

## Half-time consequence

The manual also establishes that the LMS could deliberately alter simulator timing through CTE half-time operation.

For this project, that supports keeping exercise/runtime time-scaling controls separate from subsystem equations. It does **not** justify automatically doubling every model timestep when a future time-scale feature is used. Time scaling and numerical integration remain separate project controls unless a historical model specifically couples them.

## Relationship to research note 216

Research note 216 remains canonical for the overall source hierarchy and no-global-timestep rule.

This note adds direct operational evidence that:

- 50 ms was an LMS computer timing pulse;
- 10 ms was another LMS timing pulse;
- half-time scaled those pulses;
- multiple timing layers therefore existed in the LMS.

## Next source targets

1. recover the full LMS User's Manual pages around Update #34 and identify the A/B/C computer program roles associated with the timing pulses;
2. recover the Grumman 50 ms AACS engineering memo and determine whether its “integration step” is explicitly tied to the 50 ms computer pulse;
3. recover LMS math-model/program documentation that states individual model update schedules;
4. recover acceptance/correlation documents to determine whether timing-step errors were bounded numerically.

## Evidence boundary

Do not replace the current model-specific integration configuration with a global 50 ms “Apollo LMS timestep.”

The source supports **timing architecture**, not a universal numerical step.

## Sources

- *LMS User's Manual, Volume 1*, Update #34, 22 Oct 1971, public Virtual AGC/ibiblio scan: https://www.ibiblio.org/apollo/Documents/LMS_Users_Manual.pdf
- Virtual AGC document index confirming the public LMS User's Manual scan: https://www.ibiblio.org/apollo/Documents/
- Grumman engineering-memorandum title cataloged by TechWorks: *Effect of LMS Fifty-Millisecond Integration Steps on Simulated Response of Abort Attitude Control System*.
- Research note 216, `resources/research/216_lms_source_hierarchy_timestep_boundary.md`.
