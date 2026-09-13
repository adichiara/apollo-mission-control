# Working agreements for agents

Two agents work this repository, and both can commit and open pull requests.

**Prefer independence over coordination.** The two most useful reviews this project has had — the evidence verification audit of 2026-09-11 and the source audit of 2026-09-12 — each found defects the other missed, because they were done separately. Converging before doing the work turns two independent readers into one correlated reader. Coordinate only where a rule below requires it.

Each rule here exists because the thing it prevents already happened.

## Fetch before you propose

Run `git fetch` and read `docs/DECISIONS.md` before writing anything that reasons about the current state.

`main` has moved several hundred commits in a day. A design document written against a stale tree has twice had to be withdrawn and rewritten — once after recommending a first scenario the project had already selected, with better reasoning, in `D-013`.

## Work on a branch; land through a pull request

Not directly on `main`. The review gate is where cross-agent disagreement gets resolved, and prose collisions do not announce themselves the way code conflicts do: two documents can quietly disagree while git reports nothing.

While a pull request is open, its files belong to whoever opened it. Otherwise assume shared.

## Never upgrade an evidence label without opening the source

`DOCUMENTED`, `PARTIALLY DOCUMENTED` and `UNRESOLVED` mean what `docs/PROJECT_PRINCIPLES.md` says they mean. A claim repeated by the other agent is not evidence for it.

This is the failure two agents produce faster than one: a plausible inference gets cited, cited again, and hardens into an established fact without anyone having read a page. The live specimen is in issue #3 — a retrospective recollection of one simulation and the documented record of a different one were merged into a single case, then promoted to "the strongest candidate for a specifically reconstructed historical SimSup case."

## A decision that is not in `docs/DECISIONS.md` did not happen

That file is the handoff mechanism, and it works: it is how the continuous-clock decision (`D-016`) reached an agent still operating on a two-day-old assumption about gated scenes.

## Do not reuse a research-note number

`scripts/audit_documentation.py` reports duplicates. Prefixes 012–015 are already doubled and are retained only to avoid breaking existing links.

## When you need the other agent

Open an issue, or leave a pull-request review. Not a side channel.

The maintainer does not relay messages between agents, and a conversation that produces a decision without leaving it in the repository has produced a decision with no provenance — on a project whose entire premise is provenance.

## Access differs; split work accordingly

Retrieval and page extraction need an agent that can open the source documents. Running the test suite, the real-network smoke and the audit script needs an agent with a shell. Neither should assert the other's half on the strength of a summary.

Before pushing, run what CI runs: `python3 -m unittest discover -s tests`, the `scripts/pc2_multiclient_smoke.py` smoke against a local `uvicorn`, and `python3 scripts/audit_documentation.py`.
