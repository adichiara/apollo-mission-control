# Progress — LMS true-motion model boundary

Date: 2026-09-14  
Status: **model interface narrowed; primary extraction and implementation remain**

Continuation research identified a second, distinct LMS equation lineage: Grumman **LED-440-3**, *LEM Mission Simulator (LMS) Math Model: True Motion Equations* (August 1965), cited and reconstructed in Brian Woycechowsky's 2021 technical report.

The reconstruction exposes a useful original-model partition: propulsion supplies thrust, Stabilization and Control supplies thrust direction, Weight and Balance supplies mass/inertia/center-of-gravity inputs, and true-motion equations integrate the combined forces and moments. RCS, slosh, stage separation, and ephemeris/gravity are separate inputs rather than a single authored burn-result branch.

Research note 134 records the evidence and limitations. In particular:

- LED-440-3 is not assumed to be identical to indexed Grumman LED 500-5;
- a moon-referenced true-motion model is not automatically the correct full PC+2 trajectory propagator;
- the source boundary is strong enough to define separable Level-1 interfaces, but not to freeze Apollo 13 constants or acceptance tolerances;
- a first code proof may now use an assumption-visible propulsion/translational kernel with convergence and ordering tests while remaining explicitly non-validated as a historical PC+2 numerical model.

No simulation behavior changed in this research pass.
