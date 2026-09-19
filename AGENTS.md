# Working agreements for agents

Two agents work this repository, and both can commit and open pull requests.

**Prefer independence over coordination.** The two most useful reviews this project has had — the evidence verification audit of 2026-09-11 and the source audit of 2026-09-12 — each found defects the other missed, because they were done separately. Converging before doing the work turns two independent readers into one correlated reader. Coordinate only where a rule below requires it.

Each rule here exists because the thing it prevents already happened.

## Fetch before you propose

Run `git fetch` and read `docs/DECISIONS.md` before writing anything that reasons about the current state.

`main` has moved several hundred commits in a day. A design document written against a stale tree has twice had to be withdrawn and rewritten — once after recommending a first scenario the project had already selected, with better reasoning, in `D-013`.

## Land code and decisions through a pull request

Code, `docs/DECISIONS.md`, and anything another rule depends on go through a branch and a pull request — never directly on `main`. The review gate is where cross-agent disagreement gets resolved, and prose collisions do not announce themselves the way code conflicts do: two documents can quietly disagree while git reports nothing.

Research notes, progress documents and source catalogs may go direct. At several hundred commits a day a pull request per note is overhead nobody would honour, and pretending otherwise is how this rule eroded to about one commit in seven. The protection for direct pushes is the pre-push check below — run it every time, not most times.

While a pull request is open, its files belong to whoever opened it. Otherwise assume shared.

## Never upgrade an evidence label without opening the source

`DOCUMENTED`, `PARTIALLY DOCUMENTED` and `UNRESOLVED` mean what `docs/PROJECT_PRINCIPLES.md` says they mean. A claim repeated by the other agent is not evidence for it.

This is the failure two agents produce faster than one: a plausible inference gets cited, cited again, and hardens into an established fact without anyone having read a page. The worked specimen is issue #3, resolved in #12 — a retrospective recollection of one simulation and the documented record of a different one were merged into a single case, then promoted to "the strongest candidate for a specifically reconstructed historical SimSup case."

Correcting the note is half the job. Under `D-023` a withdrawn claim must be retired everywhere it appears, and its exact wording added to `resources/audits/withdrawn_claims.json` alongside the note that withdrew it. The audit then fails if it reappears anywhere in the tree — which is how a corrected source attribution was found still sitting in `resources/primary-sources/manifest.json`, a file nobody had thought to check.

## Keep research mechanically retrievable

New research notes use `## Sources` and `## Evidence status`. Do not create another source-heading synonym. Evidence status is claim-scoped: a note may list several `DOCUMENTED`, `PARTIALLY DOCUMENTED`, and `UNRESOLVED` entries rather than pretending the whole note has one state.

The pre-standard notes in `resources/audits/research_metadata_legacy.json` are exempt from the new heading requirement until substantively revisited. That exemption is not evidence. Do not add or upgrade a formal label in a legacy note unless you have opened the underlying source.

When you do substantively revisit one with the source open, normalize the note and remove its filename from the legacy baseline in the same change. Never remove the exemption first and invent labels afterward.

When a research note or source-catalog supplement is added, renamed, or deleted, run `python3 scripts/update_research_indexes.py`. The documentation audit fails if `resources/RESEARCH_INDEX.md` or the scoped-catalog block in `resources/PRIMARY_SOURCE_CATALOG.md` stops covering the tree.

## A decision that is not in `docs/DECISIONS.md` did not happen

That file is the handoff mechanism, and it works: it is how the continuous-clock decision (`D-016`) reached an agent still operating on a two-day-old assumption about gated scenes.

## Do not reuse a research-note number

`scripts/audit_documentation.py` fails on duplicates under `D-023`, so a collision blocks CI rather than appearing in a report. No doubled prefixes remain; the last of them were renumbered into the 200s.

**Claim a fresh hundred-block when you open a new research thread.** Two threads drawing from one counter collide — 141/143–147 (Apollo 11 against Apollo 13) and 234–236 (LMS against mission-specific) both happened that way, and the second took `main` red for 29 commits.

Treat the existing 000–399 ranges as closed legacy space:

- 000–199: general/legacy research;
- 200–299: renumbered collision repairs and later legacy research;
- 300–399: mixed legacy. It is predominantly the LMS lineage through 324, but 314 is player-interaction/playability research and 325–328 are Apollo 13 LM malfunction/procedure research. Those exceptions are historical misallocations, not precedent.

For a new independent research thread, claim the next unused hundred-block starting at 400. **Claim the block by updating this allocation map through a pull request before creating the thread's first note.** Once claimed, that hundred-block belongs to that thread until deliberately retired or reassigned.

## When you need the other agent

Open an issue, or leave a pull-request review. Not a side channel.

The maintainer does not relay messages between agents, and a conversation that produces a decision without leaving it in the repository has produced a decision with no provenance — on a project whose entire premise is provenance.

## Access differs; split work accordingly

Retrieval and page extraction need an agent that can open the source documents. Running the test suite, the real-network smoke and the audit script needs an agent with a shell. Neither should assert the other's half on the strength of a summary.

Before pushing, run what CI runs: `python3 -m unittest discover -s tests`, the `scripts/pc2_multiclient_smoke.py` smoke against a local `uvicorn`, and `python3 scripts/audit_documentation.py`.
