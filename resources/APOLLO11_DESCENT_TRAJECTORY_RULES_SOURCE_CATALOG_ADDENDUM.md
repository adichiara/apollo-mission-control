# Apollo 11 descent trajectory-rules source-catalog addendum

Date: 2026-09-21
Parent: `resources/APOLLO11_POWERED_DESCENT_PHASE_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| NASA MSC Flight Control Division, *Flight Mission Rules, Apollo 11 (AS-506/107/LM-5)*, April 16, 1969 | Mission-effective rules 2-25 and 5-89 through 5-91 define powered-descent failure-management and trajectory/guidance/LR decision boundaries. | Primary authority for rule semantics. Does not by itself establish exact controller CRT fields, station routing, or call ownership. |
| NASA SP-287, *What Made Apollo a Success?* | Reproduces Apollo 11 rule 2-25 and explains the mission-rule/FCOH relationship and decision-rule structure. | Primary NASA corroboration/context; do not substitute its generic operations discussion for Mission-G display configuration. |
| AC Electronics, *Apollo 11 Manual*, MSK-1137 definition | Documents LR range/velocity `GOOD/BAD`, LR body-axis velocities, LR slant range, PGNS altitude, and TGO on an Apollo-11 controller display format. | Establishes controller-visible ingredients; does not establish exact parameter provenance, an automatic `RNG-ALT` calculation, or station-specific call ownership. |
| JSC Oral History Project, Robert L. Carlton interview, 10 April 2001, embedded transcript of Carlton's 20 July 1969 Mission Control console recording | Preserves CONTROL's `position 2 on LR` call, FLIGHT's landing go/no-go poll, separate Guidance and CONTROL responses, FLIGHT's integrated go, and CAPCOM relay. | Use for front-room call topology. The interview transcript reproduces a contemporaneous console recording; do not generalize one excerpt into the full descent-loop phraseology. |
| JSC Oral History Project, Eugene F. Kranz interview, 8 January 1999 | Kranz describes landing-radar telemetry being compared on the ground before the crew was told whether to accept it; Bales worked with back-room guidance support during descent. | Primary retrospective operational account; corroborates function, not an exact Mission-G parameter route or verbatim back-room transcript. |
| NASA Apollo Lunar Surface Journal, *The First Lunar Landing* | Air-ground record includes crew LR lock/`Delta-H`, P64 timing/entry, and Mission Control's go for landing. | Crew-loop corroboration only; do not infer internal controller ownership solely from air-ground traffic. |

## URLs

- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11missionrules.pdf
- https://ntrs.nasa.gov/api/citations/19720005243/downloads/19720005243.pdf
- https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- https://www.nasa.gov/wp-content/uploads/2025/07/carltonrl-4-10-01.pdf
- https://www.nasa.gov/wp-content/uploads/2025/08/kranzef-1-8-99.pdf
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.landing.html

## Controlled conclusion

The mission rules establish the decision semantics. MSK-1137 establishes controller-visible LR/guidance ingredients. The preserved Carlton console recording establishes a front-room landing-poll topology in which CONTROL's LR antenna-position call, Guidance's readiness call, FLIGHT's integration, and CAPCOM's relay remain distinct. Kranz independently corroborates a ground landing-radar comparison/acceptance function with guidance back-room support.

The exact Mission-G per-field ground-processing route and engineering conversion remain blocked on the already named PHO-TR155/Data Formats recovery. Do not invent them, and do not collapse LR antenna position, LR data validity, LR convergence/acceptance, and Guidance readiness into one state.

## Evidence status

- **DOCUMENTED:** Apollo 11 descent decision-rule semantics.
- **DOCUMENTED, APOLLO-11 CONTROLLER DISPLAY:** decision-relevant LR/guidance fields on MSK-1137.
- **DOCUMENTED, CONTEMPORANEOUS CONSOLE RECORD:** front-room landing-poll topology and CONTROL LR-position call.
- **DOCUMENTED, PRIMARY RETROSPECTIVE ACCOUNT:** ground LR comparison/acceptance function and Bales/back-room guidance support.
- **PARTIALLY DOCUMENTED:** exact mapping from rule 5-89 comparison semantics to individual displayed products.
- **BLOCKED:** exact Mission-G LR parameter provenance/engineering conversion and CCATS-versus-RTCC route.
- **DEFERRED:** exact GUIDO/back-room wording and timing unless implementation makes it player-relevant.
