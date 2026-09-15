# PC+2 controller-record roadmap — retained-GDA rationale

Date: 2026-09-15  
Research note: `resources/research/165_pc2_retained_gda_rationale.md`

## Roadmap refinement

The unresolved item is no longer simply “why was no PC+2 trim loaded?” CONTROL's primary postflight narrative answers that at operational level: the ground expected the GDA state left by the preceding maneuver's 40%-thrust compliance to provide optimum alignment for PC+2.

### Supported chain

1. LM-burn mass-property reference/deck work existed and T+55 decks were established.
2. A preceding DPS maneuver established a GDA state under 40% thrust compliance.
3. Ground controllers judged that resulting GDA state optimum for PC+2.
4. Flight Director ground rules explicitly required no PC+2 maneuver trims.
5. Crew procedure terminated Verb 48 after Noun 47 with V34, before Noun 48.
6. PC+2 therefore began from retained GDA state; roll GDA then moved unexpectedly at ignition.

### Still unresolved

- exact candidate trim produced for PC+2, if one was produced;
- exact reference/current trim used in the comparison;
- numerical comparison delta or tolerance;
- RTCC job/run identifier and calculation time;
- direct calculation-level linkage to the T+55 LM-burn deck family.

### Next source priority

1. Search/verify the ~59–74 GET Flight Director Log pages using the OCR route from note 164.
2. Seek CONTROL/Flight Dynamics working sheets or console logs.
3. Seek RTCC/RTACF mass-properties outputs or job records.
4. If no calculation artifact survives, preserve the primary CONTROL rationale as the evidence ceiling rather than inventing numerical provenance.