# Station-status addendum — PC+2 Luminary V34/N47 branch

Date: 2026-09-15  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical maturity grades remain unchanged. Research note 159 strengthens the PC+2 workflow boundary with Apollo 13 flight-software evidence.

## GUIDO

The crew-side Verb 48/DAP-load behavior is now directly constrained by Luminary 131. At Noun 47, `V34E` terminates R03 before Noun 48; `V33E` instead proceeds through mass/moment processing and then displays Noun 48. A later proceed response can invoke `TRIMGIMB`.

For PC+2, Mission Control's instructed `VERB 34 ENTER` therefore selected a real software termination branch. GUIDO simulation should not automatically advance to Noun 48 after Noun 47.

## CONTROL

The software result strengthens the documented **no-new-trim-load** outcome but does not recover CONTROL's decision basis. The unresolved CONTROL artifact remains a worksheet, calculation, tolerance, retained-state comparison, or mass-properties job showing why the existing gimbal condition was acceptable.

## FLIGHT/CAPCOM

The CAPCOM instruction can now be represented as a historically consequential procedural branch rather than descriptive dialogue. FLIGHT/CAPCOM need not expose a fabricated trim pair; the supported action is to direct termination after Noun 47 when the no-update decision has been made.

## Simulation boundary

Keep separate:

1. controller calculation/acceptance rationale — unresolved;
2. CAPCOM instruction — documented;
3. crew V34 response at Noun 47 — documented;
4. Luminary branch to routine termination — software-confirmed;
5. retained gimbal state — only partially observed;
6. powered-flight GDA response — postflight documented.