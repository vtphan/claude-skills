# ACCORD State Schema

`docs/accord/accord-state.md` is skill-maintained process metadata. The human lead may inspect it, but should not normally edit it by hand. If it appears wrong, ask the relevant ACCORD skill to repair or reconcile it.

Keep this file compact. It is an index, not a duplicate plan, process log, risk register, or artifact history.

## Minimum Contract

```text
## Project
slug:
status:

## Approved Artifacts
intent:
design:
plan:

## Current Unit
id:
summary:
status:

## Latest Boundaries
intent_tag:
design_tag:
plan_tag:
exec_tag:
review_tag:

## Next
recommended_skill:
human_decisions:
notes:
```

## Status Values

Use ordinary, readable values. Defaults:

- `intent_drafting`
- `design_drafting`
- `planning`
- `executing`
- `reviewing`
- `complete`
- `paused`

## Scale Up When Needed

Add fields only when a project genuinely needs them, such as:

- multiple active plan branches
- multiple repositories
- optional separate review reports
- non-git baseline tracking
- explicitly paused or blocked states that need recovery instructions

Do not use `accord-state.md` to carry full execution history. Put historical project flow in `plan.md` and git.

## Update Rules

- Update after every approved ACCORD phase.
- Record latest canonical artifact paths and latest tags.
- Record source draft paths when promoting `intent`, `design`, or `plan`.
- Record the latest execution report path when `execute` completes.
- Record the next recommended skill.
- Do not silently overwrite manual edits in a dirty working tree.
