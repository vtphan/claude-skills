# ACCORD Git Conventions

Git is part of ACCORD's process state. Commits and lightweight tags mark approved phase boundaries and make cross-conversation handoff precise.

If git is unavailable, save artifacts normally and warn that later review has a weaker baseline.

## Commit Prefixes

- `intent:`
- `design:`
- `plan:`
- `exec:`
- `review:`

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
- If the working tree has unrelated dirty files, stop and ask how to proceed.
- Include enough commit body detail to name the approved artifact, source draft if applicable, decisions, scope, and evidence.
- Do not create or move tags silently if a target tag already exists.
- Prefer new commits over history rewriting after an approved ACCORD tag exists.

## Suggested Messages

```text
intent: approve project intent

Promotes docs/accord/intent/draft_02.md to docs/accord/intent/intent.md.
Updates docs/accord/accord-state.md.
Tag: accord-intent-v1
```

```text
design: approve architecture and decisions

Promotes docs/accord/design/draft_04.md to docs/accord/design/design.md.
Key decisions: D-001 persistence, D-002 deployment.
Tag: accord-design-v1
```

```text
exec: implement auth-login

Implements approved unit u-001-auth-login.
Report: docs/accord/reports/exec-u-001-auth-login.md.
Tag: accord-exec-u-001-auth-login
```

## Repair And Redo

After an approved `exec:` commit has been tagged, do not amend or reset it as part of normal ACCORD recovery.

Use these paths:

### Repair

Use when the implementation is mostly valid but needs targeted follow-up work.

1. `review-update` records verdict `repair`.
2. `plan.md` creates a targeted repair unit, such as `u-001-auth-login-repair-02`.
3. `execute` implements the repair in a new commit.
4. Tag the repair execution, such as `accord-exec-u-001-auth-login-repair-02`.
5. `review-update` verifies and tags the repair review.

Do not revert the original exec commit unless the faulty code must be removed before repair can proceed.

### Redo

Use when the implementation approach should not stand.

1. `review-update` records verdict `redo` and names the rejected exec tag.
2. Revert the bad exec commit with a new revert commit if its changes should be removed from the branch.
3. Approve a retry unit using a suffix in the unit ID, such as `u-001-auth-login-r02`.
4. `execute` implements the redo in a new commit.
5. Tag the retry execution, such as `accord-exec-u-001-auth-login-r02`.
6. `review-update` verifies and tags the retry review.

If the human lead chooses to keep the original commit for reference but supersede its behavior, record that explicitly in `plan.md`.

### Replan

Use when execution shows the plan shape or next units are wrong.

1. `review-update` records verdict `replan`.
2. `plan` or `review-update` updates `plan.md` with the approved new shape.
3. If design changed, route through `design` before further execution.

## Completion And Reopening

Suggested completion commit:

```text
review: complete ACCORD project

Closes the final approved unit and sets docs/accord/accord-state.md to complete.
Tag: accord-complete-v1
```

If a completed project later receives new work, do not move or recreate `accord-complete-v1`. Resume normal ACCORD phase tags. If the project is completed again after substantial new work, use `accord-complete-v2`.
