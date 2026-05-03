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

The review diff is `<base>..accord-exec-<unit-id>` where `<base>` is resolved by the algorithm below. Chained repairs and retries make plain-language rules ambiguous (which "previous unit"? which "original"?), so the agent should follow the algorithm directly.

### Resolution Algorithm

Given a unit being reviewed with id `<unit-id>`:

1. **Parse the unit id.** It has one of three shapes:
   - **Plain**: `u-NNN-slug` (no suffix)
   - **Repair**: `u-NNN-slug-repair-MM`
   - **Retry**: `u-NNN-slug-rMM`

2. **Identify the unit family.** For repair and retry units, the family root is `u-NNN-slug` (strip the suffix). For plain units, the family is just the unit itself.

3. **Find `<base>`** by case:

   - **Plain unit**: most recent `accord-review-*` tag in the project (any prior unit). If none exists, `<base>` is the most recent `accord-plan-v<N>` tag.
   - **Repair unit**: most recent `accord-review-*` tag for the family root (`u-NNN-slug`) or any prior repair in the same family (`u-NNN-slug-repair-<smaller-number>`). The diff shows only this repair's work.
   - **Retry unit**: most recent `accord-review-*` tag for the family root or any prior retry in the same family (`u-NNN-slug-r<smaller-number>`). The diff shows any revert commit plus this retry's work.

4. **Set `<exec>`** = `accord-exec-<unit-id>` matching the full id of the unit being reviewed (with its suffix if any).

5. **The review diff is `<base>..<exec>`.**

### Verification

Inspect `git log <base>..<exec>` — the commit list should be exactly the work attributable to this unit's attempt. If you see commits from another unit or another unit-family, the resolution is wrong; recompute.

If a plan-revision tag (`accord-plan-v<N+1>`) sits inside the range, include those commits in the diff but treat them as state changes, not implementation evidence.

### Source of Tag Information

Read `accord-state.md`'s `Latest Boundaries` for the latest `review_tag` and `plan_tag`. For chained recovery cases, list `git tag --list "accord-review-u-NNN-slug*"` (replacing `u-NNN-slug` with the family root) to find all prior reviews in the family.

### Mechanical Examples

These examples show tag mechanics only; they are not content guidance.

- Plain unit: reviewing `u-002-example` after prior review tag `accord-review-u-001-example` means the diff is `accord-review-u-001-example..accord-exec-u-002-example`.
- First unit: reviewing `u-001-example` with no prior review tag means the diff is the most recent plan tag, such as `accord-plan-v1..accord-exec-u-001-example`.
- Repair unit: reviewing `u-002-example-repair-01` after the original unit was reviewed at `accord-review-u-002-example` means the diff is `accord-review-u-002-example..accord-exec-u-002-example-repair-01`.
- Retry unit: reviewing `u-002-example-r02` after the original unit was reviewed at `accord-review-u-002-example` means the diff is `accord-review-u-002-example..accord-exec-u-002-example-r02`.

## Verdicts

- `pass` — acceptance met, no findings.
- `pass-with-findings` — acceptance met; watch items or accepted debt recorded. Distinguish accepted residual findings from required follow-up.
- `repair` — implementation is mostly valid; targeted follow-up needed. Approve a repair unit `u-NNN-slug-repair-01`.
- `redo` — implementation should not stand. Identify the rejected exec tag; if the bad changes should not remain on the branch, use a new revert commit. Approve a retry unit `u-NNN-slug-r02`.
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

- `docs/accord/plan/plan.md`
- `docs/accord/accord-state.md`
- `docs/accord/commands.md` when changed
- optional `docs/accord/reports/review-<unit-id>.md`

Use a `review:` prefix and tag `accord-review-<unit-id>`.
