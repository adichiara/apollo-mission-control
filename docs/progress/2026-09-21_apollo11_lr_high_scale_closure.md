# Progress — Apollo 11 LR absolute high-scale closure

Date: 2026-09-21

## Question

Can the absolute Apollo-11-effective landing-radar altitude high-scale conversion be established without silently importing a later LM/Luminary configuration?

## Primary-source result

Yes, as a derived value at the precision already documented by the flown software.

Two Apollo-11-effective primary facts are already established independently:

1. Flown LUMINARY 099 documents the low-scale LR altitude representation as `1.079 ft/count`.
2. MIT Instrumentation Laboratory LUMINARY Memo #85, explicitly for Revision 99, defines `SFR = High Scale Factor / Low Scale Factor = 5`.

Therefore:

`High Scale Factor = 1.079 ft/count × 5 = 5.395 ft/count`.

This does not require assuming continuity from Luminary 1B. MSC-69-FS-4 is instead an independent near-mission cross-check: it explicitly prints 1.0790 ft/count low scale and 5.3950 ft/count high scale.

## Controlled interpretation

The repository may use 5.395 ft/count as an Apollo-11-effective **derived** high-scale conversion. It should not describe that number as a directly quoted LM-5 hardware specification unless such a source is recovered.

The derivation does not establish raw landing-radar serial word sign convention, bias, framing, transfer rounding/truncation, stochastic error behavior, or controller visibility. Those remain separate evidence questions.

## Repository impact

- Roadmap: absolute high-scale conversion removed from the unresolved queue; raw serial encoding becomes the next LR interface target.
- Station status: 5.395 ft/count may be used internally, with no new controller-visible product inferred.
- Source catalog: distinguishes direct primary facts, their arithmetic consequence, and Luminary 1B corroboration.
- Historical stochastic LR generation remains **BLOCKED**.

## Primary sources

- Flown Apollo 11 LUMINARY 099 `CONTROLLED_CONSTANTS.agc` / assembly information:
  https://www.ibiblio.org/apollo/listings/Luminary099/CONTROLLED_CONSTANTS.agc.html
- MIT Instrumentation Laboratory, LUMINARY Memo #85, *LUMINARY Revision 99*, 21 May 1969:
  https://www.ibiblio.org/apollo/Documents/LUM85_text.pdf
- Corroboration: MSC-69-FS-4, *Programmed Guidance Equations for Luminary 1B*:
  https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE PRIMARY:** low scale = 1.079 ft/count.
- **DOCUMENTED, REVISION-99 PRIMARY:** high/low scale-factor ratio = 5.
- **DERIVED, APOLLO-11-EFFECTIVE:** high scale = 5.395 ft/count.
- **INDEPENDENTLY CORROBORATED, NEAR-MISSION PRIMARY:** Luminary 1B explicitly gives 5.3950 ft/count.
- **UNRESOLVED:** raw serial sign/bias/framing, rounding/truncation, controller-visible consequences, stochastic LR error distribution.
