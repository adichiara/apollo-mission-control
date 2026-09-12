# Apollo 13 PC+2 DPS Shutdown Response Sources

Status: active focused source supplement for the crew STOP command → physical descent-engine response boundary.

## 1. Apollo Operations Handbook — Lunar Module LM10 and Subsequent, Volume I

- **Document:** LMA790-3-LM, *Apollo Operations Handbook — Lunar Module LM10 and Subsequent, Volume I — Subsystems Data*
- **Basic date:** 1 February 1970
- **Source class:** PRIMARY/CONTEMPORARY LM SYSTEMS DOCUMENTATION
- **Searchable copy:** https://ibiblio.org/apollo/Documents/LMA790-3-LM10-ApolloOperationsHandbookLunarModuleLM10AndSubsequent-Volume1-SubsystemsData-SearchableText.pdf
- **Relevant material:** descent-engine control sections around pp. 2.1-19 and 2.1-35/37.
- **Use:** establishes manual descent-engine STOP pushbuttons, engine-off discrete/control routing, pilot-valve actuation, and fuel/oxidizer shutoff-valve closure path.
- **Limitation:** this is LM10-and-subsequent documentation, not a line-by-line recovered LM-7 handbook page. It is used with continuity evidence, not as proof of every LM-7 implementation detail.

## 2. Contemporary LM familiarization / earlier handbook continuity

- **Document family:** LMA790-2 / LMA790-3-LM contemporary LM familiarization and handbook material.
- **Source class:** PRIMARY/CONTEMPORARY CONTRACTOR/NASA DOCUMENTATION
- **Use:** supports continuity of the same manual START/STOP pushbutton and descent-engine command architecture before and after LM-7.
- **Limitation:** not used to invent shutdown timing, pressure decay, or a PC+2-specific controller display.

## Research record

- `resources/research/069_pc2_dps_shutdown_command_and_physical_response.md`
- `resources/research/068_pc2_delta_p_ground_callout_shutdown_loop.md`

## Implementation rule

Supported:

- crew STOP input;
- engine-off command/discrete;
- pilot-valve off actuation;
- fuel/oxidizer shutoff valves commanded closed;
- separate physical engine-off response event.

Not supported yet:

- exact LM-7 shutdown transient duration;
- exact chamber-pressure tailoff;
- exact controller confirmation latency;
- exact engine-off display/discrete field.
