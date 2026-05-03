# ACCORD State Schema

`docs/accord/accord-state.md` is skill-maintained process metadata. The human lead may inspect it but should not normally edit it by hand. If it appears wrong, ask the relevant ACCORD skill to repair or reconcile it.

The state file is an index, not a duplicate plan or process log. It must be sufficient for a cold agent (per principle 9) to identify what has happened and what is next.

## Minimum Contract

```
## Project
slug:
status:

## Approved Artifacts
intent:
intent_source_draft:
design:
design_source_draft:
plan:
plan_source_draft:

## Current Unit
id:
summary:
status:
review_mode:

## Latest Boundaries
intent_tag:
design_tag:
plan_tag:
exec_tag:
review_tag:
latest_execution_report:

## Next
recommended_skill:
human_decisions:
notes:
```

## Status Values

- `intent_drafting`
- `design_drafting`
- `planning`
- `executing`
- `reviewing`
- `repairing`
- `redoing`
- `replanning`
- `blocked`
- `complete`
- `paused`

Use `paused` when the human lead explicitly stops ACCORD work. Use `blocked` when the current phase cannot proceed without a human decision, missing dependency, unavailable command, or unresolved repository state. Record the blocker in `Next`.

## Update Rules

- Update after every approved ACCORD phase.
- Record latest canonical artifact paths and latest tags.
- Record source draft paths when promoting `intent`, `design`, or `plan`.
- Record the latest execution report path when `execute` completes.
- Record `review_mode` for the current approved unit when it is `fresh-required`.
- Record the next recommended skill.
- Do not silently overwrite manual edits in a dirty working tree.

## Scale Up When Needed

Add fields only when a project genuinely needs them (e.g., optional separate review reports, non-git baseline tracking, blocked states with recovery instructions).

Do not use `accord-state.md` to carry full execution history. Project flow lives in `plan.md` and git.
