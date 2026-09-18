# Research note 217 — LMS Console Directory output/telemetry boundary

Date: 2026-09-15  
Status: **DIRECT PRIMARY-SOURCE INDEX TEXT REVIEWED; page-level PDF extraction incomplete because the public scan timed out in the available viewer.**

## Question

Can surviving LMS documentation constrain how authoritative simulator state was mapped into exposed measurements/telemetry channels, and can it help separate physical/source variables from telemetry-console malfunction insertion?

## Primary source located

**LMS Console Directory**, dated **13 August 1971**.

Public scan: https://www.ibiblio.org/apollo/Documents/LMS_Console_Directory.pdf

The searchable public index exposes the directory's opening definitions even though the full PDF timed out in the current viewer.

## 1. The LMS maintained an explicit measurement/output dictionary

The directory states that active telemetry channels are listed by **measurement number** and defines columns including:

- measurement ID;
- measurement description;
- telemetry-console dial number;
- event bit number;
- PCM telemetry channel number;
- PDT table order;
- PCM table bit number;
- input-data source;
- range / fixed value for analog measurements;
- bit function for event measurements;
- spacecraft effectivity.

This is direct evidence that the LMS did not treat telemetry as an undifferentiated view of hidden simulation state. It maintained an explicit mapping from simulator/source data into named/measured output channels with metadata.

## 2. Input-data source was a first-class field

The first-page column definition explicitly describes input-data source in terms including subsystem variable, redundant channel input, or fixed value.

Project consequence: preserve source/model state separately from the measurement/output definition that chooses a source and representation.

A reusable output definition may therefore need output/measurement ID, source model/domain, source variable/path, representation/type, units, availability/effectivity, provenance, and observation/telemetry transformation or validity policy. Exact LMS field names or numeric encodings should not be copied until the full directory is extracted.

## 3. Spacecraft effectivity was explicit

The directory includes a spacecraft-effectivity column and notes that no entry indicates applicability to all spacecraft.

Historical measurement/output availability therefore belongs in mission/vehicle profile data, not in the generic measurement engine. This reinforces D-021.

## 4. Telemetry-console malfunction insertion was distinct from source definition

The opening instructions describe special behavior when prime, multi-redundant, or redundant channels are malfunctioned at the telemetry console.

The indexed text is imperfect, and the full page could not be visually verified in this pass. Therefore the exact redundant-channel consequence wording is **not frozen here**.

What is safe to conclude:

- the LMS telemetry console had channel-level malfunction capability;
- malfunction handling was tied to measurement/channel definitions;
- this was separate enough from source-variable description to be documented as output-channel behavior.

Project consequence: retain separate failure insertion points for source/subsystem state and measurement/telemetry output. A telemetry malfunction must be able to alter or invalidate an exposed measurement without mutating the upstream physical/source variable.

## 5. Do not overgeneralize the 1971 directory to Apollo 13

The directory is dated August 1971, after Apollo 13. It is strong evidence for LMS output-dictionary architecture and late-program simulator telemetry practice, but it does **not** prove that every listed measurement existed in the Apollo 13 H-2 LMS configuration, that channel/dial numbers are valid for Apollo 13, or that 1971 malfunction rules were unchanged from 1970.

Apollo 13-specific telemetry membership/routing still requires H-2/LM-7 configuration evidence.

## 6. Reusable architecture consequence

Add an explicit reusable layer: source/model state → output/measurement definition → telemetry/indication value + validity → ground/interface processing → controller product.

The output-definition layer should be inspectable and profile-driven. It should not infer diagnoses, select controller decisions, mutate physical truth when an observation channel fails, or embed one mission's channel inventory as generic Apollo behavior.

## 7. Relationship to existing project models

This source strengthens existing truth/observation boundaries in tracking observation, landing-radar qualification, resource→power→observation composition, source-state injections, and malfunction-plan insertion layers.

That reusable abstraction is now implemented in `src/apollo_mission_control/measurement_output_model.py`, with mission/profile data separated in `measurement_profiles.py` and a site-facing historical-measurement proof in the Causal Model Lab. This source therefore now serves as historical support and a regression constraint on that existing boundary rather than as a request for another abstraction.

## 8. Next extraction targets

1. Obtain a reliably renderable/text-extractable copy of the full LMS Console Directory.
2. Extract representative analog, event, and redundant-channel rows.
3. Determine whether measurement definitions reference model-variable names that can be matched to LMS math/instructor-handbook variables.
4. Extract the now-located 1971 `LMS User's Manual` for program-loading, computer-operation, and peripheral-use evidence; see research note 312.
5. Determine whether the User's Manual explicitly references the Console Directory or its measurement/output identifiers.
6. Cross-check any candidate Apollo 13 measurement against LM-7/H-2 telemetry/configuration sources before adopting historical IDs/channels.

## Evidence boundary

The public PDF result exposed first-page definitions in searchable text. The full PDF timed out in the current web viewer, and the screenshot backend could not render the failed fetch. This note therefore does not claim page-by-page review or exact reconstruction of the redundant-channel malfunction instructions.

## Sources

- LMS Console Directory, 13 August 1971, public Virtual AGC/ibiblio scan.
- Virtual AGC change log, 22 January 2025, identifying the LMS Console Directory as a newly added source that appears to list available telemetry measurements.
- Research note 215 for independent AMS evidence that telemetry faults were a separate simulator malfunction layer.
