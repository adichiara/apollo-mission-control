# Roadmap continuation — Apollo 11 powered-descent trajectory decision rules

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-21_apollo11_powered_descent_phase_profile.md`

## Bounded question

What mission-effective trajectory/guidance decision rules constrain the Apollo 11 powered descent, without inventing controller displays or hidden vehicle state?

## Primary-source result

The Apollo 11 Flight Mission Rules, prepared by the Flight Control Division, provide direct mission-effective decision boundaries for descent. Section 5 states that landing-radar data are required for landing (rule 5-89) and gives explicit continue/abort criteria around LR acquisition, convergence, dropout/reacquisition, P64, and PGNS-versus-LR altitude disagreement. The same section then defines conditions for terminating powered descent (5-90), while rule 5-91 states that after crew takeover there are no trajectory or guidance constraints that themselves cause abort.

The mission-wide management rule 2-25 supplies an important temporal boundary: through approximately PDI + 5 minutes, when DPS-to-orbit capability remains, loss of required redundancy in critical LM systems favors abort; during the remainder of powered descent, landing and subsequent ascent is preferred unless a failure/trend threatens the capability to land, ascend to a safe orbit, or life support.

These rules establish controller decision semantics, not a particular CRT field or station ownership. They therefore may constrain simulator decisions while the exact GUIDO/FLIGHT display routing remains separately unresolved.

## Implementation consequence

The Apollo 11 architecture reference may now model powered-descent decision gates as explicit rule evaluations rather than generic altitude checkpoints. At minimum keep distinct: LR availability/acceptance/convergence; P64 transition; PGNS-vs-LR altitude disagreement where the rule specifies it; the PDI+5 management boundary; and crew takeover, after which rule 5-91 changes the trajectory/guidance abort-rule regime.

Do not infer that every rule input was displayed on one screen, that GUIDO alone owned every ruling, or that a nominal high-gate state was itself an abort threshold.

## Next bounded target

Recover Apollo-11-effective controller products/call procedure supporting these rules: specifically the GUIDO/FLIGHT-visible cues used for LR convergence and PGNS-versus-LR comparison approaching P64, and identify station ownership only where primary controller documentation supports it.

## Sources

- NASA MSC Flight Control Division, *Flight Mission Rules, Apollo 11 (AS-506/107/LM-5)*, April 16, 1969, especially rules 2-25 and 5-89 through 5-91: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11missionrules.pdf
- NASA, *What Made Apollo a Success?*, SP-287, discussion and reproduced Apollo 11 mission-rule examples: https://ntrs.nasa.gov/api/citations/19720005243/downloads/19720005243.pdf

## Evidence status

- **DOCUMENTED / MISSION-EFFECTIVE RULE:** LR data are required for landing and rule 5-89 defines specific acquisition/convergence/dropout and PGNS-vs-LR disagreement criteria.
- **DOCUMENTED / MANAGEMENT RULE:** the preferred failure response changes after approximately PDI + 5 minutes.
- **DOCUMENTED / RULE BOUNDARY:** after crew takeover, trajectory/guidance constraints are not themselves cause for abort under rule 5-91.
- **UNRESOLVED:** exact Apollo 11 controller display fields, screen routing, and station-specific call procedure by which the rule inputs were monitored.