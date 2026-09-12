# Apollo 13 PC+2 ΔP Ground-Callout Sources

Status: active focused source supplement for the PC+2 fuel/oxidizer differential-pressure shutdown path and first playable session integration.

## 1. Mission Operations Report — Apollo 13

- **Organization:** NASA Manned Spacecraft Center / Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** establishes the PC+2 shutdown criterion `ΔP fuel/oxidizer >25 psi` and explicitly states that it is based on a ground call-out.
- **Additional use:** establishes that restart applies only to early shutdowns for reasons other than the listed shutdown criteria.
- **Accessible copy:** NASA Apollo 13 Mission Operations Report.
- **Relevant location:** PC+2 Mission Rules review, p. III-25 in the searchable copy.
- **Limitation:** does not define the exact ground ΔP transformation, call wording, internal voice-loop sequence, or cockpit shutdown control.

## 2. Apollo 13 Technical Air-To-Ground Voice Transcription

- **Organization:** NASA
- **Publication date:** April 1970
- **NTRS document ID:** 20160014370
- **Source class:** PRIMARY, contemporaneous mission transcript
- **Use:** records the PC+2 rules read-up and crew readback around 76:30 GET. The exchange confirms that fuel/oxidizer ΔP >25 psi is a ground call to the crew and that the crew should shut down for the listed condition.
- **Limitation:** the reviewed exchange is a pre-burn rules briefing, not an actual ΔP exceedance event during PC+2.

## 3. Apollo Flight Journal — Day 4 Part 1

- **Source class:** SECONDARY TRANSCRIPT ACCESS / CROSS-CHECK
- **Use:** searchable corrected access copy for locating the 076:30 GET Brand/Haise rules exchange in the NASA technical transcript.
- **Evidence rule:** historical claims should cite the NASA technical transcript and Mission Operations Report as the primary basis; AFJ is an access/correction aid.

## Research record

- `resources/research/058_pc2_fuel_oxidizer_delta_p_observation_path.md`
- `resources/research/068_pc2_delta_p_ground_callout_shutdown_loop.md`
- `resources/research/082_pc2_delta_p_session_integration_boundary.md`

## Implemented integration boundary

The first playable nonnominal path now preserves these distinct stages:

1. scenario/source injection of the ground ΔP observation;
2. CONTROL-visible product;
3. common shutdown-rule evaluation;
4. explicit CONTROL callout decision;
5. project CAPCOM queue;
6. explicit CAPCOM transmission.

The CAPCOM queue is labeled as a **project routing abstraction**. The reviewed primary sources establish the ground callout to the crew but do not establish the exact internal CONTROL→FLIGHT→CAPCOM approval/voice-loop sequence.

A 26-psi value appears only in tests as a synthetic source-bounded threshold case. It is not an Apollo 13 measurement.

## Implementation rule

Do not infer:

- an onboard ΔP readout for this criterion;
- an exact CONTROL→FLIGHT→CAPCOM approval sequence;
- exact callout wording;
- exact cockpit shutdown control;
- crew compliance merely from CAPCOM transmission;
- physical engine shutdown merely from a recorded crew command.
