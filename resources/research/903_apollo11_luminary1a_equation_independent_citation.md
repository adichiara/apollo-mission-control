# 903 — Apollo 11 LUMINARY 1A equation authority

Research thread: `apollo11-descent-runtime`

## Bounded question

Can Apollo-11-effective primary evidence establish the implemented P66 control topology without importing later LUMINARY behavior, despite the unrecovered MSC-69-FS-3 body?

## Findings

NASA/MSC Mission G documentation independently cites *Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program*, Flight Software Branch, Flight Support Division, May 1969. MSC-69-FS-4 separately identifies that predecessor as MSC-69-FS-3 and states that the 1B document is a complete reissue updated from 1A.

A stronger Apollo-11-effective implementation source is also recoverable. The Virtual AGC `Luminary099` transcription derives from digitized hardcopy held by the MIT Museum. Its source header identifies LUMINARY 1A build 099 as Apollo 11 LM AGC software and preserves a July 14, 1969 LMY99 assembly notation.

The Apollo-11-effective `LUNAR_LANDING_GUIDANCE_EQUATIONS.agc` directly preserves the implemented descent logic:

- the vertical phase routes to `VERTGUID`;
- P66 entry initializes desired altitude rate from current altitude rate;
- `RODCOMP` applies ROD-switch counts to `VDGVERT`;
- P66 computation is scheduled on a one-second cycle;
- the computation derives altitude rate from the current state/PIPA-derived velocity, compares it with desired altitude rate through `TAUROD`, constrains commanded acceleration between force/mass limits, and calls the throttle routine.

`THROTTLE_CONTROL_ROUTINES.agc` separately shows desired guidance thrust and present thrust being converted into throttle commands and includes engine-response-lag compensation.

## Runtime consequence

The missing 69-FS-3 body no longer blocks establishing the **implemented Apollo 11 P66 control topology**. It remains required for claims specifically about the GSOP document's exact prose/equation presentation.

The flight-code transcription has a documented correction history. Exact opcode, constant scaling, or textual-identity claims must therefore be checked against the preserved page images when material. No numerical P66 constants are admitted by this note merely because labels or encoded values are visible in the transcription.

## Closure consequence

For current runtime architecture this bounded question is **SUFFICIENT**. Reopen exact 69-FS-3 recovery only if a future implementation or validation claim specifically requires that document rather than Apollo-11-effective flight-code behavior.

The next open P66 question is narrower: which constants/scales are actually required by the bounded runtime, and can each be validated against Apollo-11-effective code/page evidence before admission?

## Recovery lead

The Neil A. Armstrong papers finding aid at Purdue catalogs adjacent Mission G guidance material, including Apollo Project Memo 7-69, *What is LUMINARY 1A?* (30 Jan 1969), and *Guidance, Navigation and Control Lunar Module Functional Description and Operation Using Flight Program Luminary (Rev. 069)* (5 Jun 1969). These remain archival leads, not substitutes for 69-FS-3.

## Sources

1. NASA/MSC, Mission G rendezvous documentation, references section: *Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program*, Flight Software Branch, Flight Support Division, May 1969.
2. NASA/MSC, MSC-69-FS-4, *Programmed Guidance Equations for LUMINARY 1B Manned LM Earth Orbital and Lunar Program*, Page Change Record.
3. MIT Instrumentation Laboratory / NASA, LUMINARY 1A build 099 Apollo 11 AGC source hardcopy, transcribed by the Virtual AGC project from MIT Museum page images: `Luminary099/LUNAR_LANDING_GUIDANCE_EQUATIONS.agc` and `Luminary099/THROTTLE_CONTROL_ROUTINES.agc`.
4. Purdue University Libraries, Neil A. Armstrong papers, MSA 5 finding aid, Box 35 Folder 3.

## Evidence status

- **DOCUMENTED:** Mission G-era NASA/MSC documentation independently cites the May 1969 LUMINARY 1A programmed-guidance-equation document.
- **DOCUMENTED:** MSC-69-FS-4 identifies the predecessor as MSC-69-FS-3 and describes the 1A→1B reissue/change relationship.
- **DOCUMENTED:** Apollo-11-effective LUMINARY 1A build 099 flight code establishes the implemented P66 mode-entry, ROD-command, vertical-rate feedback, force-limit, and throttle-call topology.
- **SUFFICIENT FOR CURRENT IMPLEMENTATION:** exact P66 control topology no longer depends on recovering 69-FS-3.
- **BLOCKED ON DOCUMENT RECOVERY:** authenticated 69-FS-3 body and exact GSOP page/equation text where a future claim specifically requires that document.
