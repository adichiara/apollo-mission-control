# Progress — Apollo 11 LR PCR-775 zero-load resolution

Date: 2026-09-21

## Question

Why does the Apollo 11 LUMINARY 99 prelaunch load record `RADSKAL = 00000,00000` and `SKALSKAL = 00000` when the flown Revision-99 source describes `SKALSKAL` as `.2 NOM`?

## Primary-source result

MIT Instrumentation Laboratory LUMINARY Memo #85, dated 21 May 1969 and explicitly describing LUMINARY Revision 99, states that PCR 775 moved landing-radar slant-range Doppler compensation into R12 as an option. It created the pad-loaded erasables `RADSKAL` (double precision) and `SKALSKAL` (single precision).

The memo defines:

- `SFR = High Scale Factor / Low Scale Factor = 5`;
- `SKALSKAL = 1/SFR = 0.2`, scaled B-0;
- for R12-performed Doppler compensation, `RADSKAL` locations 1354–1355 are octal `00023,37462` and `SKALSKAL` location 1356 is octal `06315`;
- if the landing radar performs Doppler compensation, all three registers are set to zero.

The Apollo 11 mission prelaunch load records exactly the latter zero state. This closes the apparent contradiction: `.2 NOM` is the nominal scale-factor ratio used by the R12 implementation, while Apollo 11's zero load selects the alternate radar-performed compensation path.

## Controlled interpretation

This evidence supports modeling the Apollo 11 onboard configuration as radar-performed slant-range Doppler compensation under the PCR-775 selection mechanism. It also directly establishes a Revision-99 high/low altitude scale-factor ratio of 5 (reciprocal 0.2).

It does **not** establish that controllers saw or selected this state, nor does it establish the raw LR serial encoding, stochastic error behavior, or by itself the absolute LM-5 high-scale count value. The adjacent Luminary 1B value 5.3950 ft/count remains corroborating rather than mission-effective absolute-value evidence.

## Repository impact

- Roadmap updated: zero-padload semantics closed; direct 5:1 Revision-99 ratio promoted.
- Station status updated: onboard configuration may encode radar-performed compensation, with no inferred controller-visible control.
- Source catalog updated with LUMINARY Memo #85 and corrected mission-load interpretation.
- Historical stochastic LR generation remains **BLOCKED**.

## Primary source

MIT Instrumentation Laboratory, LUMINARY Memo #85, *LUMINARY Revision 99*, 21 May 1969:
https://www.ibiblio.org/apollo/Documents/LUM85_text.pdf

## Evidence status

- **DOCUMENTED, REVISION-99 PRIMARY:** PCR-775 selection semantics, `SFR = 5`, `SKALSKAL = 0.2`, and exact R12-compensation pad values.
- **DOCUMENTED, APOLLO-11 MISSION LOAD:** all three PCR-775 erasables zero.
- **RESOLVED BY DIRECT CROSS-READ:** Apollo 11 selected radar-performed Doppler compensation under this mechanism; zero is not the physical scale ratio.
- **UNRESOLVED:** direct LM-5 absolute high-scale count value, raw serial encoding/rounding, controller visibility, stochastic LR error model.
