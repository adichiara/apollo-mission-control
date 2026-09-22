# Station research status — Apollo 11 continuous descent trajectory boundary

Date: 2026-09-22

## GUIDANCE

**Status: PARTIALLY DOCUMENTED for continuous-model coupling.**

Primary technical evidence supports continuing comparison of onboard guidance/navigation information with independently derived ground tracking during descent. P63/P64/P65/P66 semantics support a guidance/control-mode input to the causal vehicle model.

Not established here: an exact Mission-G display field, continuous Apollo 11 PGNS state history, or a controller-visible value at arbitrary simulation time.

## FIDO

**Status: PARTIALLY DOCUMENTED.**

Ground tracking can support an independently derived trajectory observation path. The exact Apollo-11-effective FIDO powered-descent product set/cadence is not recovered by this pass and must not be inferred from the existence of MSFN processing.

## FLIGHT

**Status: unchanged / sufficient at decision boundary.**

The continuous-model work does not automate FLIGHT decisions. Vehicle state and controller observations remain evidence inputs to human decisions.

## CONTROL

**Status: unchanged.**

DPS architecture supports physical propulsion/resource modeling, but this pass does not establish new CONTROL display fields or thresholds.

## CAPCOM

**Status: unchanged.**

No new crew-facing calls are inferred from continuous dynamics.

## Implementation boundary

A continuous causal state may exist below station products, but stations receive only independently sourced/projected observations. Reconstructed historical trajectories are validation/reference material unless and until their exact product semantics are sourced.

## Evidence status

- **GUIDANCE:** PARTIALLY DOCUMENTED for continuous causal coupling.
- **FIDO:** PARTIALLY DOCUMENTED; exact powered-descent product presentation remains unresolved.
- **FLIGHT:** SUFFICIENT for existing human-decision separation.
- **CONTROL:** no new player-visible claim.
- **CAPCOM:** no new player-visible claim.
