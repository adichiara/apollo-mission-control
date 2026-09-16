# Progress — Apollo 11 guidance-monitoring timing boundary

Date: 2026-09-15

## Recovered

MSC Internal Note 69-FM-36 supplies Mission G MSFN powered-flight-processor timing evidence:

- high-speed tracking input: 10 measurements/s;
- expected measurement-processing interval: 0.2 or 0.4 s;
- processor observation/state outputs are time-tagged;
- observation-time quantization follows the selected processing interval;
- a real-time observation lag is part of the processor requirements, but its numeric value is not recovered in this pass.

## Boundary preserved

These values describe the MSFN/PFP source-production path. They do not establish the maximum permitted age/time separation between PGNCS, AGS, and MSFN/PFP observations for a controller comparison.

Accordingly:

- historical profile timing metadata is now source-backed and inspectable;
- `max_time_separation_s` remains `null`;
- historical `GuidanceCrosscheckConfig` construction remains blocked;
- no 0.2- or 0.4-second freshness rule is invented.

## Next timing target

Recover explicit controller/source synchronization or freshness requirements if they survive. Otherwise keep the comparison non-executable until a source-bounded closure path exists.
