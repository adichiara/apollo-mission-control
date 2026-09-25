# Apollo 11 P66 load sources

Sources controlling numerical-load claims for the Apollo 11 powered-descent runtime.

## Flight-code authority

LUMINARY 1A build 099 / Revision 1, MIT Instrumentation Laboratory document 2021112-061. The Apollo-11-effective source uses RODSCALE/RODSCAL1, TAUROD, LAG/TAU, MINFORCE, and MAXFORCE in P66 while the erasable-assignment listing classifies the corresponding values as erasable I-values. This establishes algorithm/storage semantics, not mission-loaded numerical values.

## Apollo-era simulation-load evidence

Apollo 11 Landing Digital Simulation (1969), MIT Instrumentation Laboratory digital-simulation printout preserved from Don Eyles's collection. The load listing contains RODSCALE = 0.003048 M/CS, TAUROD = 150 CS, LAG/TAU = 0.413333, and force-limit words. Treat these as a simulation-load profile unless separately confirmed as LM-5 flight loads.

## Claim boundary

Do not promote simulation pad-load values to Apollo-11 as-flown values without flight-effectivity evidence. Do not infer LM-5 physical thrust calibration from AGC force-command limits.

See research 904.
