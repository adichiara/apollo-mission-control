# Progress — LMS compute growth chronology

Date: 2026-09-17

## Completed

Research note 238 followed the unresolved machine-allocation thread from notes 235–236 with a primary-source-first search for `LMA-790-2-LMS`, DDP-224 assignment, and program-loading/configuration records.

No new directly inspectable primary configuration record was recovered that names the two original machine workloads. The strongest new evidence is James E. Tomayko's NASA-published *Computers in Spaceflight: The NASA Experience* (`NASA-CR-182505`, NTRS `19880069935`), retained explicitly as an official historical synthesis rather than promoted to primary configuration evidence.

That source reports an initial **two-computer LMS allocation**, followed later by addition of a **third computer to simulate the onboard computer**. It also reports 8K words of common memory among the simulator computers.

Cross-read with primary NASA TN D-7112, the evidence now supports a coherent developmental boundary: two-machine initial allocation → later dedicated onboard-computer simulation machine → mature three-machine LMS complex.

## Documentation updated

- `resources/research/238_lms_compute_growth_guidance_machine_chronology.md`
- `resources/source-catalog/LMS_DEPLOYED_COMPUTE_TOPOLOGY.md`
- `docs/roadmap/2026-09-17_lms_compute_growth_chronology.md`
- `docs/station-status/2026-09-17_lms_compute_growth_chronology.md`

## Remaining work

Highest-value unresolved items are now:

1. identify the exact programs/models on the **original two LMS machines** from configuration-controlled records;
2. establish when/site-by-site the third guidance machine became operational;
3. resolve the narrower Houston four-DDP-224 physical-room recollection without inventing a spare/support role;
4. establish Apollo 13-period configuration/effectivity;
5. recover model integration/update schedules independently of processor topology.

No executable causal-engine constant changes from this research pass.
