## Scope

Describe one coherent change. If this PR contains separable concerns, split them before review.

## Why

What project decision, roadmap item, bug, research finding, or integration need does this address?

## Evidence / provenance

For historically grounded changes, list the research note(s), source catalog entry, and any unresolved evidence limits. Clearly separate documented facts from project design choices.

## Validation

- [ ] `python -m unittest discover -s tests`
- [ ] `python scripts/audit_documentation.py`
- [ ] New or changed behavior has focused tests where practical
- [ ] I did not rely on external HTTP availability for CI-critical validation

Paste relevant local or CI results here.

## Repository hygiene

- [ ] Branch is based on current `main` or has been updated before merge
- [ ] No unrelated files or generated artifacts are included
- [ ] Documentation/roadmap/decision records are updated when the change alters project state
- [ ] New research-note IDs are unique
- [ ] Any intentionally unresolved issue is recorded rather than silently guessed

## Review notes

Call out anything that deserves special review: rights/licensing judgment, migration risk, historical ambiguity, API compatibility, or follow-up work.
