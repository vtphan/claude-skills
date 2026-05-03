---
name: plan
description: Use this ACCORD skill when approved intent and design artifacts exist and the human lead wants an adaptive implementation plan or a revised plan. Triggers include "accord plan", "draft the plan", "choose the next unit", "revise the plan", or when planning needs to adapt after review. The skill may use monotonic draft rounds, promotes an approved draft to docs/accord/plan/plan.md, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Plan

Create or revise the adaptive implementation plan. The LLM chooses the plan shape and explains why. The schema protects handoff to `execute`; it does not prescribe waves, milestones, task trees, or any other form.

Before doing anything else, read:

- `../references/plan-schema.md`
- `../references/design-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

## Operating Contract

1. Read `docs/accord/accord-state.md`.
2. Read canonical `intent.md` and `design.md`.
3. Read current `plan.md` if revising.
4. If planning after execution/review, read relevant execution reports and review/update log entries.
5. Decide whether draft rounds are useful. Use drafts when the strategy is still being codesigned; update canonical `plan.md` directly only when `review-update` owns the update.
6. Choose an adaptive plan shape and justify it.
7. Define the current approved unit clearly enough for `execute`.
8. Surface human decisions and acceptance criteria for approval.
9. On approval, promote/update `plan.md`, update state, commit, and tag.

## Draft Rounds

Use monotonic drafts in `docs/accord/plan/` when planning is exploratory:

```text
draft_00.md
draft_01.md
plan.md
draft_02.md
```

Useful default draft structure:

```text
## Round Stance
## Planning Stance
## Plan Shape
## Rationale for Shape
## Current Approved Unit
## Acceptance Criteria
## Verification Expectations
## Expected Scope
## Later Work
## Assumptions / Risks
## Human Decisions Needed
## LLM Defaults Chosen
## Consider This
## Notes
```

## Canonical Artifact

`docs/accord/plan/plan.md` must include:

```text
## Planning Stance
## Plan Shape
## Current Approved Unit
## Acceptance Criteria
## Verification Expectations
## Expected Scope
## Later Work
## Assumptions / Risks
## Review and Update Log
```

`Plan Shape` may be a milestone list, task tree, dependency graph, wave-like plan, vertical slice sequence, one-shot plan, or another form. State why it fits.

## Scale-Up Triggers

Add detail when multiple plan shapes are plausible, the next unit is broad/risky, acceptance is hard to verify, design assumptions are unresolved, later dependencies make vague sketches dangerous, or the human asks for more detail.

## Human Decisions

Ask for human judgment on plan shape when strategy matters, scope cuts, sequencing tradeoffs, acceptance criteria, current-unit approval, and risk acceptance.

## LLM Discretion

Choose straightforward plan shapes, task IDs, low-risk sequencing, internal organization, and future detail level when the choice is not consequential.

## Review Log

`review-update` records completed-unit outcomes in `plan.md`:

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

## Git

After approval, commit:

- `docs/accord/plan/draft_NN.md` when a draft was used
- `docs/accord/plan/plan.md`
- `docs/accord/accord-state.md`

Use a `plan:` commit prefix and tag `accord-plan-v<N>`.
