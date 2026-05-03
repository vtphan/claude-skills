# ACCORD Plan Contract

`plan` codesigns an adaptive implementation path. It may use draft rounds like `intent` and `design`, then promotes an approved draft into canonical `plan.md`.

The LLM chooses the plan shape. The schema protects handoff to `execute`; it does not prescribe waves, milestones, task trees, or any other form.

## Draft Rounds

Use one monotonic draft sequence in `docs/accord/plan/`:

```text
draft_00.md
draft_01.md
plan.md
draft_02.md
```

Drafts are never overwritten. A draft after `plan.md` is a proposed plan revision. `review-update` may update canonical `plan.md` directly because it owns the review/update log and next approved unit.

## Minimum Canonical Contract

`plan.md` must include:

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

## Plan Shape

`Plan Shape` may be a milestone list, task tree, dependency graph, wave-like plan, vertical slice sequence, one-shot plan, or another form the LLM judges fit. The LLM must state why the shape fits the project.

## Review And Update Log

`review-update` records completed-unit outcomes here. Keep entries compact and include report/tag references rather than duplicating report content.

Minimum entry:

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

## Scale Up When

- several valid plan shapes compete
- the next unit is broad or risky
- acceptance criteria are hard to verify
- design has unresolved assumptions
- later work has dependencies that would make a vague sketch dangerous
- the human lead asks for more detail
- `review-update` returns `repair`, `redo`, or `replan`

## Human Decision Points

- plan shape when strategy matters
- scope cuts
- sequencing tradeoffs
- acceptance criteria
- approval of the current unit
- risk acceptance

## LLM Discretion Zone

- straightforward plan shape selection
- task IDs
- low-risk sequencing
- internal organization
- amount of future detail when not consequential

## Promotion And Updates

On initial approval:

- promote the approved draft into `docs/accord/plan/plan.md`
- do not include a canonical change log
- update `docs/accord/accord-state.md` with source draft and tag
- commit explicit paths
- tag `accord-plan-v<N>`

On review/update:

- update `plan.md` directly
- record execution report path and tags in `Review and Update Log`
- set the next approved unit when applicable
- commit explicit paths
- tag `accord-review-<unit-id>`
