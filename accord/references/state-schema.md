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

## Per-Skill Transitions

Each skill has defined pre-state and post-state for state file bookkeeping. A cold agent reading `status` and `Next.recommended_skill` should be able to determine which skill runs next; these transitions ensure state advances coherently after each approved phase.

These rules describe state-file protocol, not LLM behavior. The agent's thinking inside a skill is unrestricted (principle 5); only the bookkeeping at phase boundaries is pinned down here.

### Common Exits

Any phase may exit to:

- `paused` — human lead explicitly stopped work. Record the skill to resume to in `recommended_skill`.
- `blocked` — phase cannot proceed without external resolution. Record the blocker in `Next.notes`; record the resume-to skill in `recommended_skill`.

When `complete`, re-invoking any skill (typically `intent` for new features or revisions) sets status to that phase's drafting state. The `accord-complete-v1` tag stays in git; do not move or recreate it.

### intent

**Pre-state:**
- Greenfield bootstrap: no `accord-state.md` exists. Skill creates the file.
- Re-entry: status `intent_drafting`, or resuming from `paused`/`blocked`/`complete`.

**Post-state on approval:**
- New `intent.md` promoted: set `intent_tag = accord-intent-v<N>`, set `intent_source_draft`, status → `design_drafting`, `recommended_skill: design`.
- Round converged with no change to canonical (stance `stop`): leave `intent_tag` unchanged, status → `design_drafting`, `recommended_skill: design`.

### design

**Pre-state:**
- status `design_drafting`, or resuming.
- `intent.md` exists and `intent_tag` is set.

**Post-state on approval:**
- New `design.md` promoted: set `design_tag = accord-design-v<N>`, set `design_source_draft`, status → `planning`, `recommended_skill: plan`.
- Round converged with no change: leave `design_tag` unchanged, status → `planning`, `recommended_skill: plan`.

### plan

**Pre-state:**
- status `planning` or `replanning`, or resuming.
- `intent.md` and `design.md` with tags exist.

**Post-state on approval:**
- Set `plan_tag = accord-plan-v<N>`, set `plan_source_draft` if a draft was used, populate `Current Unit` with `id` / `summary` / `status: approved` / `review_mode`, status → `executing`, `recommended_skill: execute`.

### execute

**Pre-state:**
- status `executing`, `repairing`, `redoing`, or resuming.
- `Current Unit.id` and `Current Unit.summary` are set.

**Post-state on approval:**
- Set `exec_tag = accord-exec-<unit-id>` (with repair/redo suffix if applicable), set `latest_execution_report` to the report path, set `Current Unit.status: executed`, status → `reviewing`, `recommended_skill: review-update`.

### review-update

**Pre-state:**
- status `reviewing`, or resuming.
- `latest_execution_report` and `exec_tag` are set for the current unit.

**Post-state on approval, by verdict:**

| Verdict | status | Current Unit | recommended_skill |
| --- | --- | --- | --- |
| `pass` (next unit available) | `executing` | replaced with next unit | `execute` |
| `pass` (no next unit) | `complete` | marked complete | `n/a` |
| `pass-with-findings` (continuation) | `executing` | next unit | `execute` |
| `pass-with-findings` (plan change needed) | `planning` | unchanged | `plan` |
| `repair` | `repairing` | replaced with repair unit | `execute` |
| `redo` | `redoing` | replaced with retry unit | `execute` |
| `replan` (plan-only) | `replanning` | unchanged | `plan` |
| `replan` (design changed) | `design_drafting` | unchanged | `design` |
| `replan` (intent changed; rare) | `intent_drafting` | unchanged | `intent` |

In all cases: set `review_tag = accord-review-<unit-id>`, write the Review and Update Log entry in `plan.md`.

## Scale Up When Needed

Add fields only when a project genuinely needs them (e.g., optional separate review reports, non-git baseline tracking, blocked states with recovery instructions).

Do not use `accord-state.md` to carry full execution history. Project flow lives in `plan.md` and git.
