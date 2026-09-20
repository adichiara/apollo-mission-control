# Progress — Apollo 11 LR numerical-error source retrieval

Date: 2026-09-20

## Work completed

The next unresolved landing-radar item was the lack of a flight-effective numerical measurement-error/noise basis. A primary-source search identified:

- D. A. Dyer, *LM landing radar test for the F mission — Project Apollo*
- MSC-69-EG-14 / NASA-TM-X-64374
- 11 March 1969
- NTRS document 19700025433

The NASA Technical Reports Server record describes the document as determining LM landing-radar test requirements for the F mission. The public record is authoritative for identity/scope metadata, but the PDF itself was not retrievable through the available NTRS download path during this pass.

## Result

This is a useful primary precursor and a concrete retrieval target, but it does **not** close the Apollo 11 stochastic LR model. No numerical contents were visible, and the document is F-mission rather than Mission-G/LM-5 evidence. Therefore:

1. no error magnitude, distribution, bias, dropout rate, or noise process has been added;
2. no executable simulation behavior changes;
3. after direct retrieval, any quantitative value must be checked for Mission-G/LM-5 applicability before integration.

## Documentation synchronized

- focused Apollo 11 landing-radar roadmap;
- landing-radar station-status addendum;
- Apollo 11 / Luminary 1A source-catalog addendum;
- this progress record.

## Next discriminating evidence

Retrieve MSC-69-EG-14 / NASA-TM-X-64374 and inspect it for quantitative LR accuracy/error/test requirements. If quantitative requirements exist, search Mission-G/LM-5 qualification, acceptance, configuration, or flight documentation for an explicit applicability bridge. In parallel, the higher-level MSK-1137 per-field D/L-versus-RTCC routing and GUIDO console-workflow gaps remain unresolved.

## Evidence status

**DOCUMENTED, ADJACENT EFFECTIVITY / CONTENT NOT YET INSPECTED.** The source identity and F-mission test-requirements scope are established by NASA NTRS metadata. Numerical contents and Apollo-11 applicability are not established.
