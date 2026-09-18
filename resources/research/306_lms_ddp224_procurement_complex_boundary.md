# Research note 306 — Apollo simulator DDP-224 procurement-complex boundary

Date: 2026-09-18  
Status: **CONTEMPORANEOUS NASA PROCUREMENT RECORD IDENTIFIED; PROCUREMENT COMPLEX COUNT DOES NOT RESOLVE LMS MACHINE OWNERSHIP**

## Question

Can the original Apollo simulator computer procurement narrow the meaning of later two/three/four-machine statements without inventing a machine allocation?

## Primary-source lead

NASA *The Apollo Spacecraft: A Chronology*, Volume IV, records the 21 September 1966 award and explicitly cites the underlying contemporaneous primary record:

- NASA News Release `66-254`, 21 September 1966.

The chronology states that NASA awarded Honeywell, Inc., Computer Control Division, a $4.2 million fixed-price contract to provide digital computer systems for Apollo command- and lunar-module simulators. Critically, it says Honeywell would provide **six separate computer complexes** supporting the Apollo simulators at MSC and Cape Kennedy, with delivery, installation, and checkout planned by the end of March 1967.

NASA chronology scan: https://www.ibiblio.org/apollo/Documents/19800011953.pdf

The original News Release 66-254 scan has not yet been recovered in this pass, so the exact wording above is taken from NASA's chronology transcription/citation rather than silently represented as a directly inspected release.

## What this establishes

The 1966 procurement was framed at the level of **six computer complexes**, not six individual DDP-224 processors. Therefore the procurement count cannot legitimately be used as a processor count for an LMS.

It also provides a dated deployment milestone: the contracted complexes were intended to support simulators at both MSC and Cape Kennedy and to be delivered/installed/checked out by the end of March 1967.

## Important date discrepancy

Tomayko's 1988 NASA history states that Honeywell won the $4.2 million DDP-224 contract on **21 July 1966**. NASA SP-4009 instead places the award on **21 September 1966** and cites NASA News Release `66-254` dated that day.

Until the original release or contracting record is recovered, preserve this discrepancy. Do not silently normalize July to September, although the contemporaneous-release citation makes 21 September the stronger current lead.

## What this does not establish

Do not infer that:

- each of the six complexes contained one computer;
- six complexes means six simulators or one complex per simulator without a contract definition;
- the LMS initially or finally contained any particular number of DDP-224 processors from this procurement statement alone;
- the original two LMS workloads are identified;
- the later guidance-dedicated third LMS machine was part of the initial contracted configuration;
- the Houston four-machine room observation is explained;
- KSC LMS-2's two surviving 1973 DDP-224 systems represent the original procurement quantity;
- the March 1967 planned completion date proves actual acceptance/effectivity on that date;
- the procurement configuration remained unchanged through Apollo 13.

## Relationship to existing evidence

This adds a procurement layer distinct from the existing architecture layers:

1. 1966 procurement: six **computer complexes** for Apollo CM/LM simulators at MSC and Cape Kennedy;
2. mature LMS functional architecture: three-machine complex, one guidance-dedicated machine (TN D-7112);
3. Houston physical-room observation: four DDP-224s retrospectively reported by Jackson;
4. KSC post-Apollo disposition: two LMS-2-provenance DDP-224 systems retained for reuse in 1973.

These counts refer to different units and dates and must not be reconciled arithmetically.

## Project consequence

The source catalog should explicitly distinguish **complex count** from **processor count**. No executable constants, station products, processor/workload assignments, or maturity grades change.

## Next target

Recover NASA News Release `66-254` and, preferably, the Honeywell contract/acceptance records defining each of the six complexes. Continue parallel retrieval of `LMA-790-2-LMS` Volume I/Section 7 and configuration/program-loading records that can identify machine ownership and date effectivity.