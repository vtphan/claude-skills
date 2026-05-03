---
name: review-update
description: Use this ACCORD skill after execute has produced an execution report. Typically invoked in a fresh conversation, possibly with a different LLM, so the review reads cold against artifacts. Triggers include "accord review-update", "review the executed unit", "update the plan after execution", "close this unit", or "what comes next after execute". This skill verifies execution, writes review/update entries into docs/accord/plan/plan.md by default, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Review Update

Verify the executed unit, record findings in `plan.md`, decide recovery if needed, and approve the next unit. Most invocations run in a fresh conversation, possibly with a different LLM, so the review reads the work cold against committed artifacts (per principle 9).

## Posture

`review-update` is **agent-led**, but its agent is typically *different* from the executor. The review agent reads only the artifacts; it does not have the executor's conversational context. This is by design — same-session, same-LLM review is biased toward "the code does what I intended."

The skill has four real functions:

1. **Fresh-context verification** — read the diff against `plan.md`'s acceptance criteria and `design.md`'s decisions, without the executor's narrative loaded.
2. **Diff/report cross-check** — does the report describe what the diff actually does? Does the diff exceed the approved scope?
3. **Recovery decision-making** — if something is off, declare repair / redo / replan and propose a recovery path.
4. **Plan/state advance** — record the verdict in `plan.md`'s Review and Update Log, update `accord-state.md`, define the next unit if continuation, tag the review.

The default output is an update to `docs/accord/plan/plan.md`, not a separate review report. Create `docs/accord/reports/review-<unit-id>.md` only when findings are too complex to fit cleanly in the plan log.

## Review Mode

If `plan.md` marks the unit `Review mode: fresh-required`, do not run review in the same session as execute. Tell the human lead to invoke this skill from a fresh conversation, unless they explicitly override the requirement.

Same-session review is acceptable for low-risk units (`Review mode: same-session-ok`). Even then, the agent re-reads the artifacts cold rather than relying on memory of execute.

## At First Use In A Session

Read:

- `../references/plan-schema.md`
- `../references/execution-report-schema.md`
- `../references/design-schema.md`
- `../references/intent-schema.md`
- `../references/commands-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

## Operating Approach

1. Read `docs/accord/accord-state.md` to identify the unit being reviewed.
2. Read canonical `intent.md`, `design.md`, `plan.md`.
3. Read the execution report for the current unit.
4. Inspect the relevant diff or committed range when git is available.
5. Verify execution against the approved unit, acceptance criteria, expected scope, and design decisions. Verification is against the *artifacts*, not the report's narrative.
6. Decide verdict.
7. Present findings, verdict, and any recovery path; advise consequential vs procedural.
8. After approval, update `plan.md` and `accord-state.md`.
9. Commit explicit paths and tag `accord-review-<unit-id>`.

## Verdicts

- `pass` — acceptance met, no findings.
- `pass-with-findings` — acceptance met; watch items or accepted debt recorded. Distinguish accepted residual findings from required follow-up.
- `repair` — implementation is mostly valid; targeted follow-up needed. Approve a repair unit `u-NNN-slug-repair-01`.
- `redo` — implementation should not stand. Identify the rejected exec tag; if the bad changes should not remain on the branch, use a new revert commit. Approve a retry unit `u-NNN-slug-r02`.
- `replan` — execution shows the plan shape or next units are wrong. Update `plan.md` shape or route through `design`. If implementation has invalidated intent itself (rare), route through `intent`.

## Routing

The agent uses judgment about routing:

- update `plan.md` directly when the next step is a continuation of the approved plan (mark unit complete, record findings, approve next anticipated unit, approve targeted repair, approve redo after naming rejected exec tag and any required revert)
- route to `plan` (new draft) when findings change sequencing, plan shape, acceptance criteria, risk posture, or later-work boundaries
- route to `design` before further execution when findings invalidate architecture, boundaries, data ownership, dependencies, deployment, security, or verification strategy
- route to `intent` only when implementation has invalidated the project's goal or success criteria (rare)
- use `blocked` state when the correct route depends on a human decision, missing dependency, unavailable command, or unresolved dirty working tree

## Approval Advisory

Most `pass` verdicts are procedural — say so. `pass-with-findings` may be procedural or consequential depending on the findings; the agent decides and advises. `repair`, `redo`, and `replan` are usually consequential — the human is approving the recovery direction.

## Minimum Review Entry

Add an entry to `plan.md` under `## Review and Update Log`:

```
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

For recovery verdicts, add `Recovery:` naming the next action (targeted repair unit, redo unit, design revision, intent revision, or plan rewrite).

Keep entries compact. Reference report path and tags rather than duplicating execution report content.

## Scale Up

Scale the review when:

- verdict is `repair`, `redo`, or `replan`
- security, data loss, privacy, or architecture drift is involved
- the execution report conflicts with the diff
- multiple findings need disposition
- plan shape changes
- fresh-context review produced substantial notes

If embedding findings would make `plan.md` hard to use, create `docs/accord/reports/review-<unit-id>.md` and reference it in the log.

## Git

After approval, commit:

- `docs/accord/plan/plan.md`
- `docs/accord/accord-state.md`
- `docs/accord/commands.md` when changed
- optional `docs/accord/reports/review-<unit-id>.md`

Use a `review:` prefix and tag `accord-review-<unit-id>`.
