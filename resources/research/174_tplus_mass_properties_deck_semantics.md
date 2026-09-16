# Research note 174 — Apollo 13 T+N mass-properties deck semantics

Date: 2026-09-16

## Question

Can the primary Apollo 13 Flight Dynamics chronology clarify what the `T+55` label means well enough to avoid treating it as either a calculation time or a proven direct input to the ~59 GET PC+2 trim solution?

## Primary source

NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, Flight Dynamics mission narrative, pp. B-3 through B-5. NASA/NTRS record `19710010485`.

The report explicitly limits its narrative to information available in real time.

## Finding

The same mission-specific Flight Dynamics chronology uses the same `T+N` style repeatedly for mass-properties data:

- liftoff `T-6` mass properties (weights, c.g.'s, and aerodynamics) were generated and loaded in RTCC before launch;
- a `T+25` RTCC mass-properties run was compared with `T+6`; no update was needed because pitch/yaw trims were within `0.01°`;
- later, RTCC LM-burn mass-property decks were updated to `T+55` decks.

Within this source, `T+6`, `T+25`, and `T+55` therefore function as **time-tagged mass-properties set/deck labels or reference epochs**. The source does not support reading `T+55` as "the calculation was executed at 55:00 GET" or as a job identifier.

The chronology itself makes that distinction important. The `T+55` deck-update entry is listed before the LM-ingress entries at 53:26 and 54:25 GET. Thus the document's ordering is incompatible with a simplistic interpretation that a `T+55` deck could only be created or loaded at 55:00 GET. The label describes the mass-properties reference set, while the exact generation/load time is not printed in this entry.

## Consequence for PC+2 provenance

This sharpens, but does not close, the ~59 GET chain:

`time-tagged T+55 LM-burn mass-properties deck available in RTCC -> [specific trim job/input linkage unrecovered] -> Flight Dynamics PC+2 DPS trim 5.86 / 6.75 passed at ~59 GET`.

The primary report separately says LM CONTROL challenged that trim using premission mass properties and later accepted Flight Dynamics' data. The newer T+55 deck family is therefore a strong candidate for the superior mass-properties context, but the report still never states that the specific `5.86 / 6.75` run consumed the T+55 deck.

## Evidence boundary

Do not infer:

- that the T+55 deck was generated or loaded exactly at 55:00 GET;
- that `T+55` is an RTCC job number;
- the numerical weights/c.g.'s in the real-time T+55 deck;
- that the T+55 deck directly generated `5.86 / 6.75`;
- CONTROL's alternative trim;
- a PC+2 acceptance criterion from the earlier T+25/T+6 `0.01°` comparison.

The postflight Apollo 13 Mission Report mass-properties table remains a separate validation layer and must not be substituted for the unrecovered T+55 deck contents.

## Simulator implication

Represent a mass-properties deck's **reference epoch** separately from its generation/load timestamp and from the downstream trim-job identity. For Apollo 13, `T+55` may be stored as a source-backed reference-epoch label; generation time, numerical contents, and direct PC+2 job linkage remain unknown.

## Next archival target

Continue searching for the real-time Apollo 13 weight/c.g. or mass-properties output and associated RTCC/RTACF trim request/output behind the ~59 GET disagreement. Priority remains the direct T+55-to-job bridge, CONTROL's competing values, and the PC+2-specific comparison/acceptance basis.