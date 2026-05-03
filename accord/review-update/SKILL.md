---
name: review-update
description: Use this ACCORD skill after execute has produced an execution report and the human lead wants the work reviewed and the plan updated. Triggers include "accord review-update", "review the executed unit", "update the plan after execution", "close this unit", or "what comes next after execute". This skill verifies execution, writes review/update entries into docs/accord/plan/plan.md by default, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Review Update

Verify the executed unit, record findings in `plan.md`, and approve the next unit or recovery path.

The default output is an update to `docs/accord/plan/plan.md`, not a separate review report. Create a separate review report only when findings are too complex to fit cleanly in the plan log.

At first use in a session/project, read:

- `../references/plan-schema.md`
- `../references/execution-report-schema.md`
- `../references/design-schema.md`
- `../references/commands-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

Re-read these references when schema behavior is uncertain or the files changed.

## Review Posture

Review from artifacts and evidence, not from the executor's confidence.

Same-session review is acceptable for small or low-risk units. Fresh-context review is recommended for high-risk, architecture-touching, security-sensitive, broad-scope, or surprising units. If `plan.md` marks the unit `Review mode: fresh-required`, stop and tell the human lead to invoke this skill from fresh context unless they explicitly override the requirement.

## Operating Contract

1. Read `docs/accord/accord-state.md`.
2. Read canonical `intent.md`, `design.md`, and `plan.md`.
3. Read the execution report for the current unit.
4. Inspect the relevant diff or committed range when git is available.
5. Verify execution against approved unit, acceptance criteria, expected scope, and design decisions.
6. Decide verdict: `pass`, `pass-with-findings`, `repair`, `redo`, or `replan`.
7. Present findings and proposed plan updates to the human lead.
8. For `repair`, `redo`, or `replan`, present the recovery path before updating artifacts.
9. After approval, update `plan.md` and `accord-state.md`.
10. Commit explicit paths and tag `accord-review-<unit-id>`.

## Minimum Review Entry

Add an entry to `plan.md` under `## Review and Update Log`:

```text
### <date> - Review after <unit-id>
Verdict:
Execution report:
Exec tag:
Review tag:
Findings:
Plan updates:
Next approved unit:
Human decisions:
```

For recovery verdicts, add:

```text
Recovery:
```

Keep entries compact. Include report path and tags rather than duplicating execution report content.

## Scale-Up Triggers

Scale up the review when:

- verdict is `repair`, `redo`, or `replan`
- security, data loss, privacy, or architecture drift is involved
- the execution report conflicts with the diff
- multiple findings need disposition
- plan shape changes
- fresh-context review produced substantial notes

If embedding findings would make `plan.md` hard to use, create `docs/accord/reports/review-<unit-id>.md` and reference it in the log.

## Recovery Procedures

`repair`: approve a targeted repair unit, usually `u-NNN-slug-repair-02`. Keep the original exec tag unless the faulty code must be removed before repair.

`redo`: identify the rejected exec tag. If the bad changes should not remain on the branch, use a new revert commit rather than rewriting history. Approve a retry unit such as `u-NNN-slug-r02`.

`replan`: update the plan shape or route to `design` when implementation learning invalidates architecture or decisions.

## Human Decisions

Ask for human judgment on accepting findings, accepting debt, approving plan changes, choosing repair/redo/replan, changing design, and approving the next unit.

Do not ask about mechanical status updates, concise wording, carrying unresolved items forward, or preparing an obvious next unit consistent with prior approval.

## Git

After approval, commit:

- `docs/accord/plan/plan.md`
- `docs/accord/accord-state.md`
- `docs/accord/commands.md` when changed
- optional `docs/accord/reports/review-<unit-id>.md`

Use a `review:` prefix and tag `accord-review-<unit-id>`.
