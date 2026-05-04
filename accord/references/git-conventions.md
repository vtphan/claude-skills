# ACCORD Git Conventions

Git is part of ACCORD's process state. Commits and lightweight tags mark approved phase boundaries and make cross-conversation handoff precise (principle 9).

If git is unavailable, save artifacts normally and warn that recovery and review have a weaker baseline.

## Commit Prefixes

- `intent:`
- `design:`
- `plan:`
- `exec:`
- `review:`
- `commands:`

## Tags

Use lightweight tags:

- `accord-intent-v<N>`
- `accord-design-v<N>`
- `accord-plan-v<N>`
- `accord-exec-<unit-id>`
- `accord-review-<unit-id>`
- `accord-complete-v1`

Increment version tags when canonical `intent.md`, `design.md`, or `plan.md` is promoted again.

## Commit Rules

- Commit only after human approval.
- Commit explicit paths only.
- Never sweep unrelated user work into a phase commit.
- If the working tree has unrelated dirty files, continue only when explicit-path commits and verification remain safe. Stop and ask when dirty files overlap the intended edit set, affect verification, obscure the diff under review, or make explicit-path commits unsafe.
- Include enough commit body detail to name the approved artifact, source draft if applicable, decisions, scope, and evidence — sufficient for cross-LLM handoff.
- Do not create or move tags silently if a target tag already exists.
- Prefer new commits over history rewriting after an approved ACCORD tag exists.

## Codesign and Plan Commits

The framework requires a commit only at promotion (the approved phase boundary). Drafts are overwritten freely as work progresses; mid-iteration commits are operator-discretion (e.g., end-of-day backup) and carry no special framework metadata.

## Suggested Messages

```
intent: approve project intent

Promotes docs/accord/intent-draft.md to docs/accord/intent.md.
Updates docs/accord/accord-state.md.
Tag: accord-intent-v1
```

```
design: approve architecture and decisions

Promotes docs/accord/design-draft.md to docs/accord/design.md.
Key decisions: D-001 persistence, D-002 deployment, D-003 UX model.
Tag: accord-design-v1
```

```
exec: implement auth-login

Implements approved unit u-001-auth-login.
Report: docs/accord/reports/exec-u-001-auth-login.md.
Tag: accord-exec-u-001-auth-login
```

## Repair And Redo

After an approved `exec:` commit has been tagged, do not amend or reset it as part of normal ACCORD recovery.

### Repair

Use when the implementation is mostly valid but needs targeted follow-up work.

1. `review-update` records verdict `repair`.
2. `plan.md` creates a targeted repair unit, such as `u-001-auth-login-repair-01`.
3. `execute` implements the repair in a new commit.
4. Tag the repair execution: `accord-exec-u-001-auth-login-repair-01`.
5. `review-update` verifies and tags the repair review.

Do not revert the original exec commit unless the faulty code must be removed before repair can proceed.

### Redo

Use when the implementation approach should not stand.

1. `review-update` records verdict `redo` and names the rejected exec tag.
2. If the bad changes should be removed from the branch, `review-update` creates a new targeted revert commit after the human approves the redo direction and before tagging `accord-review-<unit-id>`.
3. The targeted revert commit uses a `review:` prefix, names the rejected exec tag, and includes only the reverted paths plus `plan.md` / `accord-state.md` / optional review report updates needed to record the redo.
4. Approve a retry unit using a suffix in the unit ID: `u-001-auth-login-r02`.
5. `execute` implements the redo in a new commit from the post-review baseline.
6. Tag the retry execution: `accord-exec-u-001-auth-login-r02`.
7. `review-update` verifies and tags the retry review.

If the human lead chooses to keep the original commit for reference but supersede its behavior, record that explicitly in `plan.md`.

### Replan

Use when execution shows the plan shape or next units are wrong.

1. `review-update` records verdict `replan`.
2. `plan` or `review-update` updates `plan.md` with the approved new shape.
3. If design changed, route through `design` before further execution.
4. If the project's goal or success criteria are invalidated (rare), route through `intent`.

## Completion

Suggested completion commit:

```
review: complete ACCORD project

Closes the final approved unit and sets docs/accord/accord-state.md to complete.
Tag: accord-complete-v1
```

## Before Commit / Tag Checklist

- Has the human approved this phase boundary or recovery direction?
- Are only explicit, relevant paths staged for the phase commit?
- Have unrelated dirty files been left out, and do they not obscure verification or review?
- Does the commit body name the artifact, source draft or unit ID, evidence, and intended tag?
- Does the target tag not already exist?
