# Research Note 013 — Apollo 13 GNC CRT Source Hunt

**Date:** 2026-09-11  
**Status:** SOURCE LOCATED / CONTENT EXTRACTION PENDING

## Objective

Determine whether the Apollo 13 CSM GNC display set can be reconstructed from a mission-specific source rather than inferred from Apollo 11/12.

## Result

A mission-specific source exists and is publicly linked:

**AC Electronics, Apollo 13 Guidance & Navigation Summary**

The Apollo 13 Flight Journal lists a **244 MB high-resolution scan** in its document collection.

The Smithsonian National Air and Space Museum Archives independently catalogs the same Apollo 13 title in:

- Apollo Flight Guidance Computer Software Collection [Hamilton]
- Box 2, Folder 10
- circa 1970

Contemporary surviving copies and auction catalog descriptions identify the book sections as including:

- CM Software
- LM Software
- **ASPO 45 CRT Displays**
- Launch and Burn Schedule
- Burn Perturbations
- Hardware

## Why this matters

Earlier Apollo 11/12 AC/Delco books preserve a CRT section with:

- MSK 683 — CM
- MSK 966 — CM
- MSK 1123 — LM
- MSK 1137 — LM

and specifically identify display 0683 as **CSM GNC PRIMARY TAB**.

Because the Apollo 13 volume has the same mission-summary document family and an ASPO 45 CRT section, it is now possible in principle to check display continuity directly.

## What is NOT yet proven

The current web environment cannot render the 244 MB PDF; direct web retrieval fails because of file size.

Therefore the project does **not** yet claim:

- Apollo 13 used MSK 683 unchanged;
- Apollo 13 used the same field layout as Apollo 11/12;
- Apollo 13 retained MSK 966, 1123, or 1137 unchanged.

These remain extraction tasks.

## Supporting Apollo 13 GNC operational evidence

The official GNC Post-Mission Report confirms that the station had to reason from:

- SM RCS quad pressures and usage;
- valve/talkback states with electrical dependencies;
- DAP quad/jet selection;
- commanded versus achieved attitude control;
- CM RCS injector temperatures;
- SPS state.

This strongly matches the types of data found on the earlier CSM GNC PRIMARY TAB, but functional similarity is not proof of identical display configuration.

## Sources

1. Apollo 13 Flight Journal — Mission Documents:
   https://apollojournals.org/afj/ap13fj/a13-documents.html

2. Smithsonian NASM — Apollo Flight Guidance Computer Software Collection [Hamilton]:
   https://www.si.edu/object/archives/sova-nasm-1986-0158

3. Apollo 13 GNC Post-Mission Report, NASA/NTRS 19710010485:
   https://ntrs.nasa.gov/citations/19710010485

4. Earlier-mission AC/Delco Guidance & Navigation Summary material used only for cross-mission comparison.

## Next action

Extract the Apollo 13 **ASPO 45 CRT Displays** section from the high-resolution scan and compare it page-for-page against Apollo 11/12 display definitions.
