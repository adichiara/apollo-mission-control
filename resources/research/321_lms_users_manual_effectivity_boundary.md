# Research note 321 — LMS User's Manual effectivity boundary

Date: 2026-09-18

## Question

What can the directly identified 22 October 1971 LMS User's Manual establish about Apollo-era LMS operation before its interior pages and change history are recovered?

## Sources checked

### Primary source

- `LMS_Users_Manual.pdf`, cover indexed from the surviving scan at `https://www.ibiblio.org/apollo/Documents/LMS_Users_Manual.pdf`.
- The cover reads **UPDATE #34 / October 22, 1971 / LMS USER'S MANUAL / VOLUME 1**.

### Discovery/context source

- Virtual AGC document library/change log. This is useful for locating scans but is not substituted for the underlying historical document.

## Finding

The cover establishes two facts that matter for evidence control:

1. the surviving Volume 1 is explicitly an **Update #34** state of the manual; and
2. that state is dated **22 October 1971**, roughly eighteen months after Apollo 13.

The word `UPDATE` and update number demonstrate that this is not an undifferentiated timeless description of LMS operation. The surviving object represents a particular late-program document state. Without the update/change pages or an earlier Apollo-13-period issue, there is no source basis for assuming that any interior procedure, machine allocation, device code, initialization sequence, loading workflow, or common-memory practice visible in Update #34 was already in force for Apollo 13.

This is an effectivity/provenance result, not a technical configuration result.

## Retrieval consequence

When the 92.8 MB scan becomes page-extractable, inspect in this order before promoting technical claims:

1. front matter and change/update record;
2. page-level update markers and revision dates;
3. explicit site/simulator identifiers;
4. machine/program ownership statements;
5. initialization/loading/common-memory/peripheral procedures.

For every technical statement recovered from Update #34, classify it as one of:

- **1971 operational fact only**;
- **generic LMS architecture corroborated independently by an earlier source**; or
- **Apollo 13 applicable**, only when a period source or preserved change history establishes that effectivity.

## What this does not establish

Do not infer from Update #34 alone:

- Apollo 13 LMS processor allocation;
- Apollo 13 program loading or initialization workflow;
- Apollo 13 common-memory mapping;
- Apollo 13 peripheral routing/device assignments;
- that all 34 updates were technical revisions rather than some other controlled update mechanism;
- when any particular interior page or procedure first became effective;
- that the October 1971 state was identical at Houston and KSC.

## Project effect

No station maturity, model-profile readiness, causal-engine constants, processor assignment, or executable behavior changes.

The retrieval priority is sharpened: page extraction must begin with document-control/change pages, not isolated computing snippets. Earlier LMS documentation remains required for Apollo 13 effectivity.