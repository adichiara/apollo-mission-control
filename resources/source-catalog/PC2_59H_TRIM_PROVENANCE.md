# Apollo 13 PC+2 ~59 GET trim-provenance sources

Date: 2026-09-15  
Related note: `resources/research/170_pc2_59h_trim_provenance.md`

## NASA/MSC Flight Control Division Mission Operations Report — Apollo 13

- Report: MSC-02680
- Date: 28 April 1970
- Source class: primary mission-specific postflight controller report
- Relevant section: Flight Dynamics chronology, PC+2 abort-pad activity at approximately 59 GET

### Supports

- A PC+2 abort/block-data pad was passed at approximately 59 GET.
- The DPS trim passed to the crew on that pad was challenged by LM CONTROL.
- LM CONTROL later agreed with Flight Dynamics' data.
- CONTROL's challenged solution had used premission mass properties, which the Flight Dynamics report explicitly says were not the best data available.
- Elsewhere in the same Flight Dynamics chronology, RTCC LM-burn mass-property decks are documented as having been updated to T+55 decks.

### Boundary

The report does not print CONTROL's alternative trim, comparison delta, acceptance criterion, RTCC/RTACF job identifier, or an explicit statement that the specific passed PC+2 trim calculation used a named T+55 deck. T+55 is therefore contextual deck-family provenance, not yet a direct calculation-level link.

## NASA Apollo 13 air-to-ground / mission voice record — ~59:03 GET

- Relevant GET: approximately 59:03–59:05
- Source class: primary mission voice transcription

### Supports

- CAPCOM identifies the two values as DPS trim/GDA angles for PC+2.
- Crew readback gives pitch `5.86°` and roll `6.75°`.
- CAPCOM accepts the readback.

### Joined finding

The time, maneuver, pad, and passed DPS-trim event coincide with the Flight Dynamics report's ~59 GET PC+2 abort-pad dispute. The pair can therefore be classified as the **Flight Dynamics PC+2 abort-pad trim solution passed to the crew at ~59 GET**.

This is stronger than treating `5.86 / 6.75` as an unexplained interim pair, but it does not make the pair measured actuator telemetry or the final post-61:29 PC+2 state.

## NASA Apollo 13 mission commentary — post-61:29 revised PC+2 pad

- Relevant GET: approximately 63:05–63:10
- Source class: primary mission voice/PAO transcription

### Supports

- CAPCOM says the GDA should be okay as it is from the last burn and gives pitch `5.85`, roll `6.74`.
- Crew readback says the GDA should be okay as is and qualifies the pair with "hopefully."

### Boundary

The `0.01°` difference on each axis from the ~59 GET `5.86 / 6.75` solution does not establish a comparison tolerance, recomputation method, or measured actuator change.

## Current provenance chain

`RTCC LM-burn deck family updated to T+55 [context] -> Flight Dynamics ~59 GET PC+2 calculation [job/deck linkage unresolved] -> passed DPS trim 5.86 / 6.75 -> LM CONTROL challenge using premission mass properties -> CONTROL later agrees with Flight Dynamics data -> 61:29 powered-flight compliance -> later PC+2 "as is" reference 5.85 / 6.74 [generation mechanism unresolved]`

## Next source target

Recover the CONTROL/Flight Dynamics working artifact for the ~59 GET disagreement, especially CONTROL's alternative values, comparison/acceptance basis, RTCC job identity, and explicit deck/input provenance.