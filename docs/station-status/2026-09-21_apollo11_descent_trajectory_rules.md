# Station research status — Apollo 11 descent trajectory rules

Date: 2026-09-21

## New evidence boundary

Apollo 11 Flight Mission Rules §5 now supplies source-backed descent decision semantics independent of any guessed console layout. Rule 5-89 requires landing-radar data for landing and defines LR acquisition/convergence/dropout/reacquisition and PGNS-versus-LR altitude-comparison criteria around P64. Rules 5-90/5-91 further bound powered-descent termination and the post-crew-takeover trajectory/guidance regime. Rule 2-25 changes the preferred failure response around PDI + 5 minutes.

## Station consequence

**GUIDO:** decision-rule relevance is strengthened, but exact Mission-G display fields and call workflow remain unresolved. Do not promote a reconstructed PGNS/LR comparison display merely from the rule text.

**FLIGHT:** the mission rules are legitimate decision constraints for the architecture, but the rules alone do not prove which underlying values FLIGHT directly saw versus received by controller call.

**CONTROL:** no new propulsion display or throttle-recovery product is established by this evidence. Keep CONTROL presentation maturity unchanged.

## Next research target

Recover primary controller/FCOH/checklist/display evidence for the actual GUIDO/FLIGHT cues and calls used to evaluate LR convergence and PGNS-versus-LR disagreement approaching P64. Keep station ownership unresolved until that evidence is recovered.

## Evidence status

- **DOCUMENTED:** mission-effective descent trajectory/guidance rule semantics.
- **PARTIAL:** controller decision relevance for GUIDO/FLIGHT.
- **UNRESOLVED:** exact display fields, routing, station ownership, and call sequence.