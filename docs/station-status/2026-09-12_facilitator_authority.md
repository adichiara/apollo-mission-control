# Station status — facilitator authority boundary

Date: 2026-09-12

No flight-controller station maturity grade changes in this work.

## Research consequence

Primary NASA simulation sources support treating Simulation Supervisor / simulation-control functions as **outside** the operational controller-station identity model.

Therefore:

- FLIGHT, CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, and CAPCOM remain player/controller roles;
- facilitator/SimSup authority is not added as another controller station;
- whole-exercise operations such as source injection, direct simulated vehicle response, lifecycle control, manual validation time, and global audit access require separate facilitator authority in configured deployments;
- controller products and station actions do not gain hidden SimSup information merely because an admin console exists.

This is an information/authority boundary, not a historical claim about Apollo computer authentication.

See `resources/research/088_facilitator_authority_boundary.md` and `resources/source-catalog/FACILITATOR_AUTHORITY_SOURCES.md`.