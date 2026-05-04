---
name: review-update
description: Use this ACCORD skill after execute has produced an execution report. Typically invoked in a fresh conversation, possibly with a different LLM, so the review reads cold against artifacts. Triggers include "accord review-update", "review the executed unit", "update the plan after execution", "close this unit", or "what comes next after execute". This skill verifies execution, writes review/update entries into docs/accord/plan.md by default, updates accord-state.md, then commits and tags after human approval.
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

The default output is an update to `docs/accord/plan.md`, not a separate review report. Create `docs/accord/reports/review-<unit-id>.md` only when findings are too complex to fit cleanly in the plan log.

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

The order of reads matters. Read the *requirements* (what should have happened) and the *diff* (what actually happened) **before** reading the execution report (the executor's narrative). The diff is evidence; the report is interpretation. Forming an independent view from the evidence first prevents the report from anchoring the review — a real bias risk even for fresh-context review by a different LLM.

1. Read `docs/accord/accord-state.md` to identify the unit being reviewed.
2. Read canonical `intent.md`, `design.md`, and `plan.md` — the requirements.
3. Read `docs/accord/commands.md` if it exists. The reviewer needs to know the project's verification commands to assess what the executor reports.
4. Inspect the review diff (see Review Diff Baseline below) — the evidence. Form an independent assessment of whether the diff satisfies the unit's acceptance criteria and respects design decisions, before loading the executor's narrative.
5. Read the execution report. Cross-check: does the report's account match the diff? Are there discrepancies in scope, evidence, or claimed verification?
6. Synthesize the final verdict from your independent assessment plus the report's information.
7. Present findings, verdict, and any recovery path; advise consequential vs procedural.
8. After approval, update `plan.md` and `accord-state.md`.
9. Commit explicit paths and tag `accord-review-<unit-id>`.

## Review Diff Baseline

The review diff is `<base>..accord-exec-<unit-id>` where `<base>` is the nearest prior ACCORD approved boundary in the unit's history. "Nearest" is topological, not timestamp-based: choose the boundary tag closest to `<exec>` on the current branch's first-parent ancestry. This rule is uniform across plain, repair, and retry units and covers replans that introduce a new `accord-plan-v<N>` between units.

### Resolution Algorithm

Given a unit being reviewed with id `<unit-id>`:

1. **Set `<exec>` = `accord-exec-<unit-id>`** matching the full id (with repair/retry suffix if any).

2. **Collect candidate boundary tags reachable from `<exec>`.** Boundary tags are any of:
   - `accord-review-*`
   - `accord-plan-v<N>`
   - `accord-design-v<N>`
   - `accord-intent-v<N>`

   Enumerate candidates with `git tag --merged <exec> --list 'accord-review-*'`, `git tag --merged <exec> --list 'accord-plan-*'`, `git tag --merged <exec> --list 'accord-design-*'`, and `git tag --merged <exec> --list 'accord-intent-*'`.

3. **Set `<base>` = the nearest candidate boundary on the first-parent path to `<exec>`.** A robust way to find it is to inspect `git log --first-parent --decorate <exec>` and choose the first ACCORD boundary tag encountered before `<exec>`. This is the approved boundary closest to the unit attempt, whether it was a prior review, a plan revision, a design revision, or an intent revision.

4. **The review diff is `<base>..<exec>`.**

This rule naturally handles every case:
- First unit, no prior review: `<base>` is the nearest `accord-plan-v<N>` ancestor (the plan that approved the unit).
- Subsequent unit, no replan since last review: `<base>` is the prior `accord-review-*`.
- Subsequent unit after a replan: `<base>` is `accord-plan-v<N+1>` (the replan tag, which is nearer to the exec tag than the prior review).
- Repair or retry: `<base>` is the prior review of the same family (or a nearer boundary if one was created between).

### Verification

Inspect `git log <base>..<exec>` — the commit list should be exactly the work attributable to this unit's attempt: the implementation commit(s), the execution report, and the state-file update. If you see commits from another unit or another unit-family, the resolution is wrong; recompute. If you see plan/design/intent-revision commits inside the range, the boundary algorithm picked the wrong tag — re-run step 2 and confirm you used the nearest first-parent ancestor.

### Source of Tag Information

Read `accord-state.md`'s `Latest Boundaries` for `review_tag`, `plan_tag`, `design_tag`, and `intent_tag`. These are useful hints, but `<base>` is still the nearest reachable ACCORD boundary on the first-parent path to `<exec>`. For chained recovery cases, list `git tag --list "accord-review-u-NNN-slug*"` (replacing `u-NNN-slug` with the family root) to find all prior reviews in the family.

### Mechanical Examples

These examples show tag mechanics only; they are not content guidance.

- Plain unit, no replan: reviewing `u-002-example` after prior review tag `accord-review-u-001-example` and no boundary tag in between means `<base>` is `accord-review-u-001-example`. Diff: `accord-review-u-001-example..accord-exec-u-002-example`.
- Plain unit, replan since last review: reviewing `u-002-example` after prior review `accord-review-u-001-example` followed by a replan that produced `accord-plan-v2` means `<base>` is `accord-plan-v2`. Diff: `accord-plan-v2..accord-exec-u-002-example`. The plan-revision commit is not in the diff.
- First unit: reviewing `u-001-example` with no prior review tag means `<base>` is the nearest `accord-plan-v<N>` ancestor. Diff: `accord-plan-v1..accord-exec-u-001-example`.
- Repair unit: reviewing `u-002-example-repair-01` after the original unit was reviewed at `accord-review-u-002-example` and no boundary tag has been created since means `<base>` is `accord-review-u-002-example`. Diff: `accord-review-u-002-example..accord-exec-u-002-example-repair-01`.
- Retry unit: reviewing `u-002-example-r02` after the original review means `<base>` is `accord-review-u-002-example`. If the bad original changes needed removal, that revert was committed by `review-update` before `accord-review-u-002-example` was tagged, so the retry diff contains only the retry unit's work.

## Verdicts

- `pass` — acceptance met, no findings.
- `pass-with-findings` — acceptance met; watch items or accepted debt recorded. Distinguish accepted residual findings from required follow-up.
- `repair` — implementation is mostly valid; targeted follow-up needed. Approve a repair unit `u-NNN-slug-repair-01`.
- `redo` — implementation should not stand. Identify the rejected exec tag. If the bad changes should not remain on the branch, `review-update` creates a new targeted revert commit after human approval of the redo direction and before tagging `accord-review-<unit-id>`. Approve a retry unit `u-NNN-slug-r02`.
- `replan` — execution shows the plan shape or next units are wrong. Update `plan.md` shape or route through `design`. If implementation has invalidated intent itself (rare), route through `intent`.

## Authority Over plan.md

`review-update` may write directly to `plan.md` when the next step is a continuation of the approved plan: marking the current unit complete, recording findings, approving the next unit, or approving a recovery unit. The boundary with `plan` is precise.

**`review-update` may advance the next unit directly when ALL of:**

1. The next unit is already named in `Later Work` with at least an id, summary, AND at least one diff-checkable acceptance criterion already written, OR it is a targeted repair unit (`u-NNN-slug-repair-NN`) or retry unit (`u-NNN-slug-rNN`).
2. The current `Plan Shape` does not change.
3. `review-update` does **not** infer or extend acceptance criteria. Acceptance comes from what `Later Work` already says; if it is missing, vague, or marked `TBD by plan`, route to `plan` instead. Writing acceptance is `plan`'s job, not `review-update`'s.
4. Sequencing in `Later Work` does not change.
5. `Review mode` follows the established convention for this project (default `same-session-ok`; `fresh-required` only when the unit fits the existing fresh-required criteria).

**`review-update` must route to `plan`** (new draft) when ANY of:

- The next unit is not in `Later Work`.
- Acceptance criteria require fresh judgment about scope or what "done" means.
- `Plan Shape` changes, or its `Rationale for Shape` no longer fits.
- Sequencing in `Later Work` changes.
- Multiple units need to be added, removed, or restructured.
- The plan-level risk posture shifts (e.g., units that were `same-session-ok` should now be `fresh-required`, or vice versa).

**`review-update` must route to `design`** when findings invalidate architecture, boundaries, data ownership, dependencies, deployment, security, or verification strategy.

**`review-update` must route to `intent`** when implementation has invalidated the project's goal or success criteria (rare).

For `repair` and `redo` verdicts: `review-update` defines and approves the recovery unit directly within its authority, since scope is bounded by the original unit and the recovery type.

Use `blocked` state when the correct route is known but depends on a human decision, missing dependency, unavailable command, or unresolved dirty working tree. Record the blocker in `accord-state.md` `Next.notes`.

When in doubt about which side of the boundary a case falls on, route to `plan`. The cost of an extra plan round is small; the cost of `review-update` writing a unit that needs replanning is higher.

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

- `docs/accord/plan.md`
- `docs/accord/accord-state.md`
- `docs/accord/commands.md` when changed
- optional `docs/accord/reports/review-<unit-id>.md`
- reverted implementation paths when verdict is `redo` and the approved recovery direction removes the rejected changes before retry

Use a `review:` prefix and tag `accord-review-<unit-id>`.
