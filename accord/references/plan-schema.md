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
## Later Work
## Assumptions / Risks
## Review and Update Log
```

## Unit IDs

Every approved unit needs a stable ID:

```text
u-001-auth-login
u-002-profile-cache
u-003-docs-typos
```

Rules:

- use `u-<three digits>-<slug>`
- never reuse IDs
- keep slugs short and descriptive
- use retry suffixes for redo attempts, such as `u-001-auth-login-r02`
- use repair suffixes for targeted repair units when clearer, such as `u-001-auth-login-repair-02`

## Current Approved Unit

At minimum, name:

```text
ID:
Summary:
Acceptance:
Expected scope:
Verification:
Review mode:
```

`Review mode` is `same-session-ok` by default. Use `fresh-required` for high-risk, architecture-touching, security-sensitive, broad-scope, or surprising units. `review-update` must honor `fresh-required`.

These fields live inside `## Current Approved Unit`. Do not duplicate acceptance, verification, expected scope, or review mode as separate top-level sections; duplication invites drift.

## Plan Shape

`Plan Shape` may be a milestone list, task tree, dependency graph, wave-like plan, vertical slice sequence, one-shot plan, or another form the LLM judges fit. The LLM must state why the shape fits the project.

Useful heuristics:

| Shape | Use When |
| --- | --- |
| `one-shot` | Change is trivial, low-risk, or tightly bounded. |
| `single-unit` | One coherent implementation unit is enough but needs explicit acceptance and review. |
| `vertical-slice` | The main risk is integration across layers. |
| `milestone-list` | Work has a small number of observable delivery checkpoints. |
| `task-tree` | Dependencies are mostly hierarchical and implementation order is straightforward. |
| `dependency-graph` | Work has non-linear dependencies or multiple valid execution paths. |
| `wave-like` | Learning from each stage should reshape later work. |
| `risk-first` | One or two uncertainties could invalidate the rest of the plan. |

The LLM may choose another shape, but should explain why the common options are not a better fit.

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

For `repair`, `redo`, and `replan`, include a recovery path:

```text
Recovery:
```

Recovery should name whether the next action is a targeted repair unit, a redo unit, a design revision, or a plan rewrite.

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

## Small Work Path

For trivial or low-risk changes, the human lead may skip `intent` and `design` and create a `one-shot` plan with one small approved unit. This is appropriate for typo fixes, one-file bugs, docs adjustments, and bounded maintenance. Do not use it for architecture, security, persistence, deployment, broad behavior, or unclear requirements.

## Parallelism

ACCORD v1 assumes one current approved unit. Parallel work requires explicit scale-up: separate branches, distinct unit IDs, and a plan section naming how branches will reconcile. Do not run parallel units against one serial `accord-state.md` without this convention.
