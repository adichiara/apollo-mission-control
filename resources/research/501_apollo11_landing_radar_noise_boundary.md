# Research note 501 — Apollo 11 landing-radar measurement-error boundary

Date: 2026-09-19  
Research thread: `apollo11-landing-radar`

## Bounded question

Can the historical Apollo 11 landing-radar model now generate stochastic velocity measurement error from a source-controlled distribution, or do the surviving primary sources only constrain the boundary around such a model?

## Implementation dependency

A stochastic LR measurement generator would materially affect repeatability, residual rejection, and state-vector convergence. It must not default to a convenient Gaussian model unless Apollo-11-effective evidence supports that distribution and its parameters.

## Findings

NASA TN D-6849, the Manned Spacecraft Center Apollo experience report on the LM landing and rendezvous radars, records a directly LM-5-specific preflight problem. During LM-5 landing-radar subsystem functional verification, a logic race produced a one-count velocity bias. The report states that the logic was altered to eliminate that race before flight.

More importantly for simulation, the same LM-5 test history says the Gaussian distribution assumed for Doppler-spectrum-simulator test limits had to be corrected because the simple three-stage RC low-pass approximation placed more energy in the distribution tails. This is direct evidence against treating that particular test distribution as an adequate Gaussian representation.

The report's Apollo 11 flight section states that LM-5 landing-radar data appeared well within specification limits except for a few low-velocity points near zero Doppler, where tracking was not expected; two questionable points were attributed probably to poor data processing during the LGC overload alarm. It does not, in the inspected material, supply a flight-effective stochastic velocity-error distribution with numerical parameters.

MIT/IL E-1982 is useful earlier design-study evidence: its navigation analysis explicitly models random and bias sensor errors and develops LR measurement weighting statistically. But it is a 1966 design study, not an Apollo-11-effective LM-5 specification. Its assumed simulation error model therefore cannot be promoted to the flown historical profile without a later source tying those assumptions to LM-5.

## Implementation consequence

Do **not** add an arbitrary Gaussian LR velocity-noise generator to the Apollo 11 historical profile. The source-controlled behavior is presently:

- retain the already documented deterministic measurement/update chain;
- allow explicit externally supplied measurement perturbations for tests/scenarios if they are labeled synthetic rather than historical;
- do not reproduce the LM-5 preflight one-count bias as a flight defect, because the primary experience report says the responsible logic was altered;
- preserve low/near-zero-Doppler degradation as a historical research boundary rather than inventing a probability law.

A stochastic historical generator remains blocked on a later LM-5/Apollo-11-effective source that provides the applicable error distribution or enough test/flight data to derive one defensibly.

## Closure state

**BLOCKED** for a flight-authentic stochastic measurement generator. The currently recovered primary evidence materially constrains what must *not* be assumed, but does not provide a numerical Apollo-11-effective distribution. Reopen if an LM-5 end-item specification, qualification/acceptance report, applicable radar performance specification, or sufficiently resolved Apollo 11 flight-data source is recovered.

## Sources

- NASA / Manned Spacecraft Center, Patrick Rozas and Allen R. Cunningham, *Apollo Experience Report — Lunar Module Landing Radar and Rendezvous Radar*, NASA TN D-6849, June 1972: https://ntrs.nasa.gov/api/citations/19720016521/downloads/19720016521.pdf
- MIT Instrumentation Laboratory, B. A. Kriegsman and N. E. Sears, *LEM PGNCS and Landing Radar Operations During the Powered Lunar Landing Maneuver*, E-1982, 1966: https://www.ibiblio.org/apollo/Documents/E-1982_LEM_PGNCS_and_Landing_Radar_Operations.pdf

## Evidence status

- **DOCUMENTED:** LM-5 preflight functional verification found a one-count landing-radar velocity bias caused by a logic race, and the logic was altered to eliminate it.
- **DOCUMENTED:** the LM-5 Doppler-spectrum-simulator test-limit Gaussian assumption was corrected because the test approximation produced heavier distribution tails.
- **DOCUMENTED:** the Apollo 11 experience report describes LM-5 landing-radar flight data as within specification limits apart from low/near-zero-Doppler points where tracking was not expected, with two questionable points probably associated with LGC-overload data processing.
- **PARTIALLY DOCUMENTED:** the qualitative flight-error boundary, including known near-zero-Doppler degradation.
- **UNRESOLVED:** an Apollo-11-effective numerical stochastic velocity measurement-error distribution suitable for historical generation.
