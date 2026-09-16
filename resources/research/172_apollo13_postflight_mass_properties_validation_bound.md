# Apollo 13 postflight mass-properties validation bound

Date: 2026-09-15

## Question

Can a mission-specific primary source recover the mass-properties values behind the ~59 GET PC+2 trim disagreement identified in notes 170–171?

## Primary source reviewed

NASA Manned Spacecraft Center, *Apollo 13 Mission Report*, MSC-02680, September 1970, Appendix A.5, Table A-I, **Mass Properties**. NASA NTRS citation 19710003598.

Primary PDF: https://ntrs.nasa.gov/api/citations/19710003598/downloads/19710003598.pdf

## Finding

The mission report provides a mission-specific postflight mass-properties table for significant events. For the event labeled **Second midcourse correction**, it gives:

| State | Weight (lb) | X c.g. (in.) | Y c.g. (in.) | Z c.g. (in.) |
|---|---:|---:|---:|---:|
| Ignition | 95,959.9 | 378.8 | 4.9 | 0.7 |
| Cutoff | 95,647.1 | 379.4 | 5.0 | 0.7 |

The table also supplies moments and products of inertia for both states. It separately gives the subsequent **Transearth injection** state, with ignition weight 95,424.0 lb and c.g. 379.7 / 5.0 / 0.7 in.

The report explains that its mass-property values represent conditions determined from **postflight analyses of expendable loadings and usage during flight**. They are therefore reconstructed mission results, not evidence that these exact values were present in a real-time T+55 controller deck or used in the ~59 GET trim calculation.

## What this resolves

This recovers an authoritative Apollo 13 mission-specific numerical mass-properties reference near the contingency maneuver sequence. It is useful as a future simulator/postflight validation target and as a discriminator for any archival weight/c.g. sheet recovered later.

It also sharpens the provenance requirement: a future candidate controller artifact should not be accepted as the operational source merely because its values resemble Table A-I. The operational artifact must independently establish its time, deck/input identity, and relationship to the trim calculation.

## What this does not resolve

This source does **not** recover:

- CONTROL's alternative numerical trim;
- the real-time mass-properties values used by CONTROL;
- the real-time Flight Dynamics weight/c.g. table used for `5.86 / 6.75`;
- a T+55-to-`5.86 / 6.75` calculation link;
- the RTCC/RTACF job/request identity;
- the comparison delta or acceptance criterion.

Do not substitute the postflight Table A-I values for the missing real-time deck.

## Research consequence

The archival target remains the Apollo 13 real-time weight/c.g./mass-properties output and associated trajectory-processor trim artifact. Table A-I now provides a **postflight validation layer** against which such an artifact can be compared, while remaining provenance-distinct from it.

## Next unresolved item

Search mission-specific Flight Dynamics/CONTROL working records for the real-time weight/c.g. table, trim output, or request/job sheet behind the ~59 GET disagreement. Priority fields remain CONTROL's competing values, real-time input/deck identity, job/run identity, and the comparison/acceptance basis.