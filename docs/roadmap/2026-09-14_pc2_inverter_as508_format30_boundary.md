# Roadmap addendum — PC+2 inverter AS-508 telemetry-format boundary

Date: 2026-09-14

## Research chain

The PC+2 archival chain now extends through research note **120**.

Note 119 established later-LM continuity for `GC0071V` / `GC0155F`: LM-10 telemetry documentation gives explicit format-dependent sample rates and MSK destinations, while LM-7/8/9 documentation confirms the same measurement identities for Apollo 13's vehicle family.

Note 120 adds Apollo 13 mission-specific ground-system evidence from the March 1970 AS-508 MCC/MSFN configuration. AS-508 confirms normal LM-capable transmission formats and separately defines High Speed Format 30 as a **post-pass playback** path for pre-defined high-rate LM/CSM subformats selected through TICC/CEF control.

## New boundary

Do not infer a live PC+2 station cadence from Format 30's 50-s/s or 10-s/s slots.

Keep three layers distinct:

1. spacecraft/network telemetry sample loading;
2. MCC/controller display refresh and latency;
3. high-rate post-pass playback to dedicated recording/review equipment.

The first playable may continue to render source-backed inverter voltage/frequency evidence, but its timing remains project-defined until an AS-508/LM-7 measurement assignment or mission-specific display/load record is recovered.

## Next archival target

1. AS-508 / LM-7 telemetry-format loading or measurement-assignment table for `GC0071V` / `GC0155F`;
2. AS-508 Format-30 LM subformat definitions;
3. Apollo 13 MSK/display loading tying the measurements to TELMU/CONTROL;
4. TICC/controller logs showing actual PC+2 selection or replay use.

## Project priority

This archival refinement does not displace the principal first-playable validation priorities: seven-seat nominal physical play, synthetic ΔP physical play, and five-player compact physical play.
