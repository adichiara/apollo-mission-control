# Facilitator / SimSup authority sources

Status: **IMPLEMENTATION-SOURCE**

This supplement supports the project boundary between controller stations and facilitator/SimSup authority. It does **not** claim that the modern HTTP credential mechanism is historical Apollo behavior.

## Primary historical sources

### NASA SP-209 — Applications of Research on Human Decision Making

- NASA SP-209, 1970.
- NTRS document: `19700013438`.
- https://ntrs.nasa.gov/citations/19700013438
- Relevant evidence: Apollo/Gemini simulation organization; simulation operators controlling simulation-facility activity; simulation controllers monitoring flight-controller performance; organization chart with Simulation Supervisor above simulation-control functions.

Implementation use:

- supports keeping exercise-control authority separate from flight-controller station identity;
- supports treating source injection and exercise manipulation as facilitator/SimSup functions rather than controller functions.

Does not establish:

- software authentication method;
- HTTP/API security behavior;
- exact mapping of prototype operations to a historical SimSup console.

### Eugene F. Kranz NASA oral history

- Eugene F. Kranz oral history.
- NTRS document: `20000027506`.
- https://ntrs.nasa.gov/citations/20000027506
- Relevant evidence: lunar-mission training team led by the person referred to as the Sim Supe / simulation supervisor.

Implementation use:

- corroborates Simulation Supervisor as a training/exercise role distinct from operational flight-controller roles.

## Current deployment/platform sources

### Render Blueprint YAML Reference

- https://render.com/docs/blueprint-spec
- Relevant current capability: `envVars` may use `generateValue: true` to create a randomized secret value without committing the secret to source control.

### Render Environment Variables and Secrets

- https://render.com/docs/configure-environment-variables
- Relevant current guidance: secret credentials should be supplied through environment configuration rather than committed into application source.

## Derived project boundary

Historical evidence constrains **role separation**. Modern platform sources constrain **credential implementation**.

The project therefore uses a separate facilitator credential for whole-exercise operations while explicitly avoiding any claim that Apollo itself used passwords, bearer tokens, or an analogous access-control protocol.
