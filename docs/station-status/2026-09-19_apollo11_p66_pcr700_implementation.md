# Station-status addendum — Apollo 11 P66 / PCR-700

Date: 2026-09-19
Research: 329–331

The Apollo 13 station maturity table remains unchanged. This addendum applies only to the D-024 Apollo 11 powered-descent reference.

## Supported vehicle/guidance facts

Apollo 11 LUMINARY 99 carried the PCR-700 P66 lag-compensation mechanism: MIT implementation records identify `LAG/TAU`, and the Mission G prelaunch erasable load supplies `LAG/TAU = 0.413333`.

Research 331 prevents a false effectivity shortcut. The surviving Section 5 Revision 8 front matter places PCR 636 and the recovered 254.2–755 inventory under **Incorporated in Rev. 4 of GSOP**, but does not list PCR-670/PCR-700 there. Section 2 Revision 4 separately names LUMINARY 1A Rev. 099 and lists those changes. Same-numbered section revisions are therefore not a sufficient station/model effectivity chain.

## Station-facing boundary

No finding establishes a new GUIDO, CONTROL, FLIGHT, or other MCC player product. The Section 5 control history does not establish a ground display cadence or prove the January SCB proposal's once-per-second HDOT display behavior in the final flight configuration.

Accordingly:

- no station maturity grade changes;
- no controller display field is added;
- no player-visible cadence is frozen;
- no executable station projection changes.

The remaining station-relevant question is whether the Section 5 state that actually incorporated the Apollo 11 landing changes (or `69-FS-3`) can be tied to LUMINARY 1A Rev. 099 and then to a sourced controller-visible product at the simulation's required resolution.