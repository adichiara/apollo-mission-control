# 146 — Apollo 11 three-source guidance monitoring boundary

## Primary evidence

MSC Internal Note 70-FM-80, Floyd V. Bennett, *Lunar Descent and Ascent Trajectories* (21 April 1970), describes real-time Apollo 11 powered-descent guidance monitoring.

Ground controllers continually compared LM velocity components computed by:

1. PGNCS;
2. AGS;
3. the MSFN-powered-flight ground computation.

The note explicitly characterizes this as **two-out-of-three voting comparison logic** used to determine whether PGNCS or AGS performance was degrading. It also states that velocity-residual redlines between PGNCS/MSFN and PGNCS/AGS were established premission.

For Apollo 11, the note records a radial PGNCS/MSFN difference of 18 ft/s at PDI against a 35 ft/s limit. The discrepancy remained into the burn but was interpreted as an initialization/downrange-position effect rather than a system-performance problem.

## Architecture consequence

A pairwise PGNS/AGS comparison is useful but insufficient as the complete Apollo 11 ground-monitoring abstraction.

The reusable observation layer therefore needs:

- multiple independent sources;
- caller-supplied fields/redlines;
- freshness constraints;
- quorum/consensus assessment;
- explicit separation between **outside consensus** and **failed source**.

The new generic multi-source consensus model implements that evidence relationship without embedding Apollo 11 values.

## Boundary

The 35 ft/s example is documented for the PGNCS/MSFN radial comparison at PDI. It is not promoted to a universal PGNS/AGS or all-phase redline.

Exact redlines, source-pair definitions, phase dependence, display routing, and operational response rules remain to be recovered before historical runtime use.

## Source

NASA MSC Internal Note 70-FM-80 / MSC-02419, Floyd V. Bennett, *Project Apollo: Lunar Descent and Ascent Trajectories*, 21 April 1970.
