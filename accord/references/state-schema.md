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

Use ordinary, readable values. Defaults:

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

Use `paused` when the human lead explicitly stops ACCORD work before the next phase can proceed. Resume by setting the status to the phase being restarted and recording the next recommended skill.

Use `blocked` when the current phase cannot proceed without a human decision, missing dependency, unavailable command, or unresolved repository state. Record the blocker in `Next` and set `recommended_skill` to the skill that should resume after the blocker is resolved.

## State Transitions

Keep transitions simple and explicit. ACCORD v1 assumes one current approved unit at a time, so `status`, `Current Unit`, `Latest Boundaries`, and `Next` should tell the next agent where to resume.

Default lifecycle:

```text
intent_drafting -> design_drafting -> planning -> executing -> reviewing
reviewing -> planning | executing | complete
```

Promotion transitions:

- After approved `intent`, set `status: design_drafting`, record `intent`, `intent_source_draft`, `intent_tag`, and set `recommended_skill: design`.
- After approved `design`, set `status: planning`, record `design`, `design_source_draft`, `design_tag`, and set `recommended_skill: plan`.
- After approved `plan`, set `status: executing`, record `plan`, `plan_source_draft` when applicable, `plan_tag`, current unit fields, and set `recommended_skill: execute`.
- After approved `execute`, set `status: reviewing`, record `exec_tag`, `latest_execution_report`, current unit status, and set `recommended_skill: review-update`.
- After approved `review-update`, set `status` based on the verdict and next action.

Review verdict transitions:

| Verdict | Next status | Next recommended skill |
| --- | --- | --- |
| `pass` with a next approved unit | `executing` | `execute` |
| `pass` with no next unit | `complete` | `n/a` |
| `pass-with-findings` with accepted follow-up in scope | `executing` | `execute` |
| `pass-with-findings` needing plan changes | `planning` | `plan` |
| `repair` | `repairing` | `execute` for the approved repair unit |
| `redo` | `redoing` | `execute` for the approved redo unit, after any required revert commit |
| `replan` | `replanning` | `plan`, or `design` when design decisions changed |

Use `blocked` instead of advancing when the next action is known but cannot start safely. Use `paused` only when the human lead intentionally stops ACCORD work.

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
- Record `review_mode` for the current approved unit when it is `fresh-required`.
- Record the next recommended skill.
- Do not silently overwrite manual edits in a dirty working tree.
