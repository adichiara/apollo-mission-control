# Apollo 11 descent landing-radar controller call workflow

Date: 2026-09-21

Research thread: `apollo11-landing-radar`

## Bounded question

What Apollo-11-specific primary evidence establishes the controller-visible landing-radar comparison and call workflow approaching P64 and the landing go/no-go, without inventing an exact GUIDO screen, back-room phraseology, or hidden station ownership?

## Findings

### The mission-control display exposed the comparison ingredients

The Apollo 11 AC Electronics manual's MSK-1137 definition places several relevant guidance products in one documented LM display format:

- `LR RNG` — landing-radar range-data status, `GOOD/BAD`;
- `VEL` — landing-radar velocity-data status, `GOOD/BAD`;
- `VXB/VYB/VZB` — landing-radar body-axis velocity;
- `RNG` — landing-radar slant range;
- `ALT` — PGNS-computed altitude;
- `TGO` — time to engine cutoff.

This is direct Apollo-11 controller-display evidence for the data products needed to recognize LR validity and compare LR-derived range with the onboard PGNS altitude estimate. It does **not** establish that raw slant range and PGNS altitude were numerically subtracted without geometry/processing, nor does it identify a per-field processor route.

### Ground explicitly judged whether radar data should be accepted

Gene Kranz's JSC oral-history transcript describes the descent workload from the Flight Director perspective. He states that when landing-radar data began arriving they were telemetered to the ground, where the team compared the radar-derived knowledge with the ground's estimate and told the crew whether to accept the radar data. In the same account, Kranz describes Steve Bales working simultaneously with his back-room guidance specialist to determine whether guidance/navigation/control remained healthy while program alarms were being evaluated.

This is a primary retrospective recollection of the operational decision process. It supports a ground comparison-and-recommendation function and GUIDO/back-room participation, but it is not a substitute for a contemporaneous parameter-routing table or a verbatim GUIDO back-room transcript.

### A preserved Apollo 11 console tape establishes the landing poll chain

Robert L. Carlton's JSC oral history includes an editor-transcribed segment of the **20 July 1969 Mission Control intercom recording made from Carlton's console**. Immediately before the landing go/no-go:

1. Kranz reports `TIGO is go`.
2. Carlton (CONTROL) reports, `We have position 2 on LR`.
3. Kranz acknowledges the LR position and announces 20 seconds to the landing go/no-go.
4. FLIGHT then polls RETRO, FIDO, Guidance, CONTROL, TELCOM, GNC, EECOM, and Surgeon.
5. Steve Bales answers `Go` for Guidance.
6. After the poll, FLIGHT tells CAPCOM that Mission Control is go for landing.
7. CAPCOM relays the go to Eagle.

Carlton then explains that each front-room controller had to report readiness to proceed to the next phase, with support-room specialists feeding their front-room controller.

This is direct evidence for the **front-room decision topology**. It also assigns the LR antenna-position-2 call in this excerpt to CONTROL, not GUIDO. That call must not be silently re-labeled as a GUIDO LR-validity call: antenna position and LR data acceptance/convergence are separate states.

### The air-ground record provides crew-visible cross-checks

The NASA Apollo Lunar Surface Journal records the crew reporting good landing-radar lock and a `Delta-H` of about -2,900 ft, followed by Houston's acknowledgement. Later, CAPCOM gives the 30-seconds-to-P64 cue, the crew reports entry into P64, and Mission Control subsequently transmits the go for landing.

This corroborates that LR lock/altitude disagreement, P64 transition, and the landing decision were live operational cues. The air-ground transcript alone does not prove which controller originated each internal assessment.

## Architecture consequence

For the Apollo 11 powered-descent reference, the historically supported player-information boundary is now strong enough to represent:

- a guidance-monitoring product containing LR range/velocity validity, LR body-axis velocity, LR slant range, PGNS altitude, and TGO;
- a separate CONTROL-visible/CONTROL-reported LR antenna-position state;
- front-room station readiness flowing to FLIGHT through a go/no-go poll;
- FLIGHT integrating those station calls and directing CAPCOM;
- CAPCOM alone transmitting the final Mission Control go to the crew.

Do **not** encode an invented automatic rule such as `GUIDO compares MSK-1137 RNG - ALT directly`. MSK-1137 establishes the visible ingredients, while the exact Mission-G engineering transformation and parameter provenance remain blocked on the already named PHO-TR155/Data Formats source recovery.

Do **not** make the `LR position 2` call stand in for LR data-good, LR acceptance, or LR convergence. They are distinct documented conditions.

## Research closure

- **Status:** **SUFFICIENT**
- **Bounded question:** What Apollo-11-specific primary evidence establishes the controller-visible landing-radar comparison and call workflow approaching P64 and the landing go/no-go?
- **Implementation dependency:** station-scoped player products, front-room readiness calls, FLIGHT integration, and CAPCOM relay behavior for the Apollo 11 powered-descent reference.
- **Decision sensitivity:** a materially different answer could move a cue to another station, collapse distinct LR antenna/data-validity states, or incorrectly let CAPCOM or software make a decision that historically belonged to the front-room control chain.
- **Decision-relevant findings:** MSK-1137 exposes LR validity/measurement products together with PGNS altitude and TGO; a preserved 20 July 1969 console recording assigns the LR-position-2 call to CONTROL and records Guidance as a separate FLIGHT poll response; FLIGHT integrates the poll and directs CAPCOM; Kranz independently describes the ground LR-comparison/acceptance decision and Bales's use of back-room guidance support.
- **Remaining gaps and disposition:** exact Mission-G LR parameter provenance/engineering conversion remains **BLOCKED** on the already named PHO-TR155/Data Formats recovery; exact GUIDO/back-room phraseology and timing are **DEFERRED** because current architecture does not require them; an exact ground `Delta-H` computation is **UNRESOLVED** and must not be invented.
- **Closure challenge:** after the last material finding, a focused pass checked the mission rules, the Apollo-11-specific display definition, the preserved landing-poll console record, Kranz's independent operational account, the air-ground descent record, and the surviving Apollo 11 Mission Control audio-channel collection for contrary station ownership or a stronger exact-workflow source. No recovered primary evidence contradicted the CONTROL LR-position call, the separate Guidance go, or the FLIGHT→CAPCOM decision chain. The channel archive confirms richer source material survives, but no searchable verbatim GUIDO/back-room transcript was recovered that changes the current implementation conclusion.
- **Reopen triggers:** exact Mission-G per-field source/engineering conversion becomes required; exact GUIDO/back-room phraseology or timing becomes player-relevant; implementation needs a historical ground PGNS-versus-LR comparison algorithm; a stronger contemporaneous controller-loop source contradicts the station split; or the blocked Mission-G PHO-TR155/Data Formats material is recovered.

## Sources

- AC Electronics, *Apollo 11 Manual*, MSK-1137 definition: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA Johnson Space Center Oral History Project, Robert L. Carlton interview, 10 April 2001, especially pp. 28-38 and the embedded 20 July 1969 intercom-loop transcript: https://www.nasa.gov/wp-content/uploads/2025/07/carltonrl-4-10-01.pdf
- NASA Johnson Space Center Oral History Project, Eugene F. Kranz interview, 8 January 1999, especially pp. 45-47: https://www.nasa.gov/wp-content/uploads/2025/08/kranzef-1-8-99.pdf
- NASA Apollo Lunar Surface Journal, *The First Lunar Landing*, Apollo 11 descent transcript: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.landing.html
- NASA MSC Flight Control Division, *Flight Mission Rules, Apollo 11 (AS-506/107/LM-5)*, 16 April 1969, especially rule 5-89: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11missionrules.pdf

## Evidence status

- **DOCUMENTED, APOLLO-11 CONTROLLER DISPLAY:** MSK-1137 exposes LR range/velocity `GOOD/BAD`, LR body-axis velocities, LR slant range, PGNS altitude, and TGO.
- **DOCUMENTED, CONTEMPORANEOUS APOLLO-11 INTERCOM RECORD:** immediately before the landing poll, CONTROL reports LR antenna position 2 to FLIGHT; FLIGHT then polls Guidance and the other front-room positions before directing CAPCOM to send the go for landing.
- **DOCUMENTED, PRIMARY RETROSPECTIVE OPERATIONAL ACCOUNT:** landing-radar data were telemetered to the ground and compared against the ground estimate before the crew was advised whether to accept the data; Bales worked with back-room guidance support while guidance/program-alarm health was assessed.
- **DOCUMENTED, AIR-GROUND RECORD:** the crew reports LR lock and `Delta-H`, receives the P64 timing cue, reports P64, and receives the go for landing.
- **PARTIALLY DOCUMENTED:** exact mapping between the mission rule's LR convergence/PGNS-LR comparison criteria and the individual MSK-1137 fields.
- **UNRESOLVED / BLOCKED ON NAMED SOURCE RECOVERY:** Mission-G per-field source identifiers, engineering conversion, and CCATS-versus-RTCC provenance for MSK-1137 LR products.
- **UNRESOLVED / DEFERRED:** exact GUIDO/back-room words and exact internal timing for the LR-acceptance/convergence recommendation.
