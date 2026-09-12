# 088 — Facilitator / SimSup authority boundary

Date: 2026-09-12  
Status: **IMPLEMENTED — server-side facilitator authority separated from controller identity**

## Question

After separating the normal player client from the validation/SimSup client, what minimum server-side authority should protect session lifecycle, manual-time, source injection, simulated crew/vehicle response, and audit operations without turning the facilitator into a Mission Control station?

## Primary-source findings

### NASA SP-209 — Apollo/Gemini simulation control organization

NASA SP-209, *Applications of Research on Human Decision Making* (1970), describes the simulation system used with Mission Control. The simulation organization is explicitly separate from the operational flight-control organization. Simulation operators monitor MCC data and control simulation-facility activity. Its organization chart places a **Simulation Supervisor** over simulation monitors/coordinators and simulation equipment operators.

The same discussion states that simulation controllers positioned near flight controllers monitored whether an exercise was proceeding normally and could respond when planned faults were not being handled as intended.

Source:

- NASA SP-209, NTRS document `19700013438`.
- https://ntrs.nasa.gov/citations/19700013438

### Gene Kranz NASA oral history

Gene Kranz's NASA oral history separately recalls lunar-mission training as being run by a training team led by the person they called the **Sim Supe / simulation supervisor**. This supports treating simulation control as an exercise/training authority distinct from the flight-controller roles being trained.

Source:

- Eugene F. Kranz oral history, NTRS document `20000027506`.
- https://ntrs.nasa.gov/citations/20000027506

## What the sources do not establish

The historical sources do **not** establish:

- an Apollo-era authentication mechanism;
- passwords, tokens, or access-control headers;
- a one-to-one mapping between every prototype validation endpoint and a historical SimSup console control;
- that the project's facilitator should be presented as a historically exact Apollo SimSup station.

Therefore the HTTP authorization mechanism is a modern software safety boundary, not a reconstruction of Apollo computer security.

## Project decision

Facilitator/SimSup authority is separate from controller station identity.

Controller players continue to authenticate operational authority through their station assignment in the current prototype. A separate facilitator credential protects operations that can alter or inspect the whole exercise:

- session create/reset;
- start/pause/resume;
- manual validation GET advancement;
- source/state injection;
- simulated crew receipt/command/report operations used by the validation harness;
- direct vehicle physical-response operations;
- global audit-log access.

Station-authorized controller operations remain outside this facilitator credential, including FLIGHT decisions, CONTROL callouts/evidence access, readiness reports, and CAPCOM transmission.

## HTTP implementation

`src/apollo_mission_control/web_app.py` now supports `APOLLO_FACILITATOR_TOKEN`.

When configured, protected operations require:

```text
X-Apollo-Facilitator: <token>
```

Comparison uses `hmac.compare_digest`.

Local development remains permissive when the token is absent so source-level development and legacy tests do not require secret setup. A Render deployment fails closed if the token is absent.

`render.yaml` uses Render's supported `generateValue: true` facility to create the deployment secret without committing it to the repository.

The `/admin` browser stores a facilitator token only in `sessionStorage` for the current tab and sends it through the HTTP header. The normal `/` player client never receives or requests this credential.

## Security scope

This is intentionally a **minimum first-playable authority boundary**, not a full authentication system.

It does not yet provide:

- named facilitator accounts;
- token rotation UI;
- durable sessions;
- per-operation facilitator permissions;
- cryptographic player identities;
- protection against a facilitator deliberately revealing the token.

Those are deferred until deployment/playtesting demonstrates a need.

## Deployment-source check

Render's current Blueprint documentation supports generated secret environment values with `generateValue: true`, and its environment-variable guidance recommends keeping secret credentials out of source control.

## Validation

`tests/test_facilitator_authority.py` covers:

- configured deployments reject facilitator operations without the token;
- wrong tokens are rejected;
- correct tokens permit facilitator operations;
- ordinary station actions remain independent of facilitator authority;
- global audit access is facilitator-protected;
- Render fails closed if facilitator authorization is unexpectedly unconfigured.

The complete repository suite is not yet recorded as executed in this automation environment.

## Next boundary

With player/admin presentation separation and server-side facilitator authority established, the next high-value work is **runnable multi-client integration validation** rather than additional authorization complexity:

1. execute the full suite in a checked-out runtime;
2. exercise multiple phone clients plus one facilitator console against one server;
3. validate continuous GET, explicit pause/resume, reload/rejoin, station isolation, and the full synthetic ΔP branch;
4. reopen historical research only when integrated play exposes a concrete missing procedure or information dependency.
