# Source Mirroring Policy

Status: **proposed — resolves Phase 0's archival item and open question 28**

Purpose: make the project's evidence base verifiable without depending on a third-party URL staying alive, and make page-level citation checkable as Principle 8 requires.

## The problem

The repository cites 88 unique external URLs across 14 hosts. Every material claim depends on one of them resolving, and on the bytes behind it being the same bytes someone read when the claim was recorded. Neither is guaranteed:

- NASA has already moved these files at least once. The 2026-09-11 evidence audit replaced four obsolete paths.
- Two verification passes on this repository reached different subsets of the evidence purely because of network access, not rigor. Each caught defects the other missed.
- One document is cited through several URLs. The Apollo 13 Mission Operations Report appears as `.../alsj/a13/A13_MissionOpReport.pdf`, `.../afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf`, and an `apollojournals.org` path. The LM-10 Operations Handbook is cited under both `ibiblio.org` and `www.ibiblio.org`.
- Nothing records *which bytes* a claim was checked against, so a silently revised scan is undetectable.

## The decision

Three tiers, chosen per document by size and rights rather than by importance.

### Tier 1 — `full`: mirror the whole document

For documents that are US Government works or NASA-contract deliverables, and small enough to live in git comfortably (under 50 MB).

Stored at `resources/primary-sources/files/<id>.pdf`, with SHA-256 and byte size recorded in `SOURCES.lock.json`.

This is the bulk of the PC+2 dependency set: the Mission Operations Report, the Review Board appendices, the AS-508 configuration description, R-567 Section 2, the simulator discrepancy reports, the LM-7/8/9 functional diagrams.

### Tier 2 — `pages`: mirror only the cited pages

For documents too large to commit whole. The AC Electronics *Apollo 13 Guidance & Navigation Summary* is a 244 MB scan; the project does not need 244 MB, it needs the **ASPO 45 CRT Displays** section. Likewise the LM-10 Apollo Operations Handbook and PHO-FAM001.

Extracted pages are stored as `resources/primary-sources/files/<id>-p<range>.pdf`, and the manifest records which page range each claim rests on.

This tier is not a compromise — it is *better* than a whole-document mirror for citation purposes, because it makes the page-level provenance Principle 8 asks for an artifact rather than a note. It is also the tier that would have let the 2026-09-12 audit check the claims it had to leave unverified: the 72 panel-3 limit lights, MSK 1475, the 1044.9 requests/hour figure.

### Tier 3 — `link-only`: record identity and hash, mirror nothing

For catalog records rather than documents (the Smithsonian finding aid), third-party uploads of unclear provenance (Scribd), interactive sites (Apollo in Real Time), and personal transcriptions used as discovery aids (earlyspaceflight.nl).

These keep a manifest entry so their role stays visible, but nothing is committed and no claim should rest on them alone.

## Rights

NASA works are US Government works and not subject to domestic copyright. Apollo-era contractor reports issued as NASA CR/TN/TM documents — Philco-Ford, TRW, MIT/Draper R-567, Grumman handbooks in the NASA series — are in the same position. Third-party *scans* of those documents (Virtual AGC on ibiblio, Internet Archive) are reproductions of public-domain works.

The manifest carries a `rights` field so each entry records the basis rather than leaving it implied. Anything not clearly in that category is Tier 3.

This is an engineering judgment recorded for review, not legal advice. If any entry's status is doubtful, reclassify it to `link-only`; the cost is one unverifiable citation, not a broken repository.

## How it works

```bash
# download every full/pages entry, hash it, write the lock file
python3 scripts/mirror_sources.py fetch

# re-hash what is on disk against the lock and report drift
python3 scripts/mirror_sources.py verify

# what is mirrored, what is pending, how much space
python3 scripts/mirror_sources.py status
```

`fetch` refuses to write a Tier 1 file over 100 MB and warns over 50 MB, naming the entry to reclassify as `pages`. It skips files already present and hash-matching, so re-running is cheap.

`verify` is the check that matters over time: it is the difference between "the URL still resolves" and "the bytes are the ones the claim was recorded against."

## What this changes for citations

Once a document is mirrored, a research note can cite it by manifest id and page, and a reviewer can confirm the page without leaving the repository. The external URL stays in the manifest as provenance for *where the bytes came from*, rather than as the only way to see them.

This is also the answer to **open question 29** — the citation convention for code and data files. A stable id plus a page reference, resolvable against a hashed local file, is a citation an implementation comment can carry.

## Sequencing

1. Fetch Tier 1 for the PC+2 dependency set. Roughly 20 documents; this is the load-bearing work.
2. Extract Tier 2 page ranges for the three oversized scans, starting with the ASPO 45 CRT section.
3. Re-run the two open audit findings against the mirrored pages — the P21/P27 program number and the ITC 1970 paper attribution.
4. Re-check, with pages in hand, the content claims that no audit has yet verified: the limit-light counts, MSK 1475, the display request rate, the TELMU consumables table.
5. Extend the manifest beyond the PC+2 set as later scenarios need documents.

Step 4 is the payoff. Those claims are currently supported by a single reading with no way for a second person to check them cheaply.

## Constraint worth recording

A cloud session's ability to run `fetch` depends on the environment's network access level. At **Trusted** — the default — the source hosts are not reachable and `fetch` fails on every entry. Running it needs either a **Custom** allowlist including the source hosts, **Full** access, or a local run on a normal network.

That constraint is the argument for this policy rather than against it: once the files are committed, nobody needs network access to verify a citation again.
