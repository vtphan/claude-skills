---
name: review-update
description: Use this ACCORD skill after execute has produced an execution report and the human lead wants the work reviewed and the plan updated. Triggers include "accord review-update", "review the executed unit", "update the plan after execution", "close this unit", or "what comes next after execute". This skill verifies execution, writes review/update entries into docs/accord/plan/plan.md by default, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Review Update

Verify the executed unit, record findings in `plan.md`, and approve the next unit or recovery path.

The default output is an update to `docs/accord/plan/plan.md`, not a separate review report. Create a separate review report only when findings are too complex to fit cleanly in the plan log.

Before doing anything else, read:

- `../references/plan-schema.md`
- `../references/execution-report-schema.md`
- `../references/design-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

## Review Posture

Review from artifacts and evidence, not from the executor's confidence.

Same-session review is acceptable for small or low-risk units. Fresh-context review is recommended for high-risk, architecture-touching, security-sensitive, broad-scope, or surprising units. The human lead controls whether to invoke this skill in the same conversation or a new one.

## Operating Contract

1. Read `docs/accord/accord-state.md`.
2. Read canonical `intent.md`, `design.md`, and `plan.md`.
3. Read the execution report for the current unit.
4. Inspect the relevant diff or committed range when git is available.
5. Verify execution against approved unit, acceptance criteria, expected scope, and design decisions.
6. Decide verdict: `pass`, `pass-with-findings`, `repair`, `redo`, or `replan`.
7. Present findings and proposed plan updates to the human lead.
8. After approval, update `plan.md` and `accord-state.md`.
9. Commit explicit paths and tag `accord-review-<unit-id>`.

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

## Human Decisions

Ask for human judgment on accepting findings, accepting debt, approving plan changes, choosing repair/redo/replan, changing design, and approving the next unit.

Do not ask about mechanical status updates, concise wording, carrying unresolved items forward, or preparing an obvious next unit consistent with prior approval.

## Git

After approval, commit:

- `docs/accord/plan/plan.md`
- `docs/accord/accord-state.md`
- optional `docs/accord/reports/review-<unit-id>.md`

Use a `review:` prefix and tag `accord-review-<unit-id>`.
