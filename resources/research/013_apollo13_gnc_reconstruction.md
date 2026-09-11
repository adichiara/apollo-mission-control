# Research Note 013 — Apollo 13 CSM GNC Reconstruction

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Objective

Determine what can be reconstructed for the Apollo 13 CSM GNC station and whether a known earlier Apollo CRT display can be carried into the Apollo 13 baseline.

## Mission-specific evidence

The Apollo 13 GNC post-mission report gives unusually strong evidence for controller reasoning even though it does not reproduce the console screens.

### SM RCS diagnosis

GNC used:

- Quad D fuel manifold pressure
- Quad D oxidizer manifold pressure
- helium-valve action
- thruster commands
- DAP quad selection
- vehicle rates
- propellant usage indications
- spacecraft electrical-bus state

to reason about available control capability after the oxygen-tank accident.

### Ambiguous valve state

Loss of Main Bus B removed both power to some RCS hardware and the talkback indications for relevant valves.

Therefore GNC could not simply read the valve state.

This is direct evidence for an important simulator principle:

**unpowered indication is not equivalent to a known OFF/CLOSED state.**

### Control recovery

Changing the DAP roll-quad selection and RCS electrical selections restored automatic control.

Thus GNC must understand configuration dependencies, not simply monitor telemetry.

### Entry preparation

CM RCS injector temperature required preheat before use.

Thermal readiness of propulsion/control hardware is therefore within the GNC information domain.

## Cross-mission display lead

AC/Delco Apollo 11 and Apollo 12 documentation contains:

**MSK 683 / display 0683 — CSM GNC PRIMARY TAB**

The display combines:

- time/computer state
- DSKY registers
- RCS/SPS data
- DAP
- control rates/deadband/errors
- vehicle acceleration
- velocity-to-go
- PIPA data
- gimbal/TVC data

These field families fit Apollo 13 GNC's documented responsibilities closely.

## Apollo 13-specific archival evidence

The Smithsonian National Air and Space Museum Archives holds:

**AC Electronics, Apollo 13 Guidance and Navigation Summary, circa 1970**

The archival collection provides digital-content access, and independent catalog descriptions identify a section titled **ASPO 45 CRT Displays**.

The Apollo 11/12 GNC display appears under the same section title.

### Research conclusion

Direct inspection has now confirmed MSK 683 in the Apollo 13 ASPO 45 section. This supersedes the original source-access conclusion in this note. Exact field continuity from Apollo 11/12 still requires a field-by-field comparison.

## Additional primary source

NASA-TM-X-69528 / MSC-02680-SUPPL-1, *Guidance, Navigation, and Control Systems Performance Analysis: Apollo 13 Mission Report*, exists and provides detailed postflight GNC performance analysis.

It is valuable for modeling spacecraft GNC behavior but is not itself evidence of the exact ground-console display layout.

## Next actions

- locate H-2 PHO-TR155 Revision C
- compare Apollo 13 MSK 683 and 966 fields against the earlier manuals
- identify the Apollo 13 GNC panel configuration and station access

## Sources

- Apollo 13 Mission Operations Report, Appendix F
- NTRS 19730017939
- Smithsonian NASM.1986.0158, Box 2 Folder 10
- Apollo 11/12 AC/Delco Guidance and Navigation Summary manuals
- [Research Note 029 — Apollo 13 ASPO 45 direct inspection](029_apollo13_aspo45_direct_inspection.md)
