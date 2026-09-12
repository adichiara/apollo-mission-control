# Apollo 13 PC+2 Crew Response Sources

Status: active focused source supplement for the CAPCOM ground-call → crew command → physical DPS response boundary.

## 1. Apollo 13 Mission Operations Report

- **Publisher:** NASA / Flight Control Division
- **Date:** 28 April 1970
- **Use:** Establishes the PC+2 shutdown criterion `fuel/oxidizer ΔP >25 psi (based on a ground call-out)` and separates listed-rule shutdowns from other premature shutdowns.
- **Authority:** Primary mission-operations source.
- **Boundary:** Does not specify response latency, exact crew wording, or hypothetical cockpit choreography for an actual ΔP exceedance.

## 2. Apollo 13 Technical Air-To-Ground Voice Transcription

- **Publisher:** NASA
- **Publication date:** April 1970
- **NTRS ID:** 20160014370
- **URL:** https://ntrs.nasa.gov/citations/20160014370
- **Use:** Establishes the pre-burn air-ground briefing structure: the >25 psi differential-pressure item was a ground call and a listed condition called for crew shutdown; the crew read the rule back.
- **Authority:** Primary air-ground transcript.
- **Boundary:** The rule briefing is not evidence that the ΔP exceedance actually occurred during the burn.

## 3. Apollo Operations Handbook — Lunar Module

- **Use:** Existing project research establishes the crew STOP / engine-off command path and the distinction between crew command and subsequent valve/engine response.
- **Authority:** Contemporary primary spacecraft operations documentation.
- **Repository cross-reference:** `PC2_DPS_SHUTDOWN_RESPONSE_SOURCES.md` and research note 069.

## Modeling conclusions supported by these sources

- CAPCOM transmission must not be treated as automatic crew compliance.
- An explicit crew receipt/response event is appropriate before the modeled crew shutdown command.
- The crew shutdown command can reuse the existing operational-action model.
- Crew command and physical engine response must remain distinct.
- No exact response delay, unique cockpit sequence, engine-off delay, chamber-pressure decay curve, or binary telemetry confirmation threshold is sourced for the hypothetical ΔP branch.

## Related repository notes

- `068_pc2_delta_p_ground_callout_shutdown_loop.md`
- `069_pc2_dps_shutdown_command_and_physical_response.md`
- `070_pc2_dps_shutdown_confirmation_evidence.md`
- `083_pc2_crew_response_after_ground_shutdown_call.md`
