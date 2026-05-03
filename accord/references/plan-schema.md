# ACCORD Plan Contract

`plan` is the agent-led planning skill. The agent picks a plan shape, justifies it against the approved design, defines the next approved unit, and informs the human. The human approves at the gate; per principle 6, most plan approvals are procedural with an advisory.

## Posture

`plan` is agent-led, not codesigned. Drafts use the same numbered-draft mechanism as intent and design for consistency, but with a lighter discipline: the **default is one round**. The agent produces `draft_00.md`, the human approves, it becomes `plan.md`. Multiple rounds happen only when the human pushes back via `Consider This` items.

## Draft Rounds

Use one monotonic draft sequence in `docs/accord/plan/`:

```
draft_00.md
draft_01.md
plan.md
draft_02.md
```

Drafts are never overwritten. A draft after `plan.md` is a proposed plan revision. `review-update` may also update canonical `plan.md` directly because it owns the review/update log and next approved unit.

## Minimum Canonical Contract

`plan.md` must include:

```
## Planning Stance
## Plan Shape
## Rationale for Shape
## Current Approved Unit
## Later Work
## Assumptions / Risks
## Review and Update Log
```

`plan.md` must satisfy principle 9 (cross-LLM handoff). The acceptance criteria in `Current Approved Unit` must be literally checkable against a diff.

## Plan Shape

`Plan Shape` may be a milestone list, task tree, dependency graph, wave-like plan, vertical slice sequence, one-shot, or another form the agent judges fit. The agent chooses; the human approves.

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

## Rationale For Shape

`Rationale for Shape` must explicitly reference the approved `design.md` — what scope, structure, dependencies, or risk in *this* design make *this* plan shape the fit. Generic shape justifications ("milestones for delivery checkpoints") are insufficient. This is the single most important section for preventing redundancy and contradiction (principle 7): a plan whose shape doesn't tie to design is more likely to drift.

## Unit IDs

Every approved unit needs a stable ID:

```
u-001-auth-login
u-002-profile-cache
u-003-docs-typos
```

Rules:

- use `u-<three digits>-<slug>`
- never reuse IDs
- keep slugs short and descriptive
- use retry suffixes for redo attempts: `u-001-auth-login-r02`
- use repair suffixes for targeted repair units: `u-001-auth-login-repair-01`

## Current Approved Unit

At minimum, name:

```
ID:
Summary:
Acceptance:
Expected scope:
Verification:
Review mode:
```

`Acceptance` must be diff-checkable — a reviewer should verify the diff against it without needing the executor's report.

`Review mode` is `same-session-ok` by default. Use `fresh-required` for high-risk, architecture-touching, security-sensitive, broad-scope, or surprising units. `review-update` must honor `fresh-required`.

## Later Work

Each `Later Work` entry should include `id`, `summary`, and at least one diff-checkable acceptance criterion. `review-update` may advance a `Later Work` entry to the current unit only when its acceptance is already written; if acceptance is unknown at planning time, mark it `Acceptance: TBD by plan` so `review-update` knows to route back to `plan` when the unit becomes current. Inferring or extending acceptance is `plan`'s job, not `review-update`'s.

## Review And Update Log

`review-update` records completed-unit outcomes here. Keep entries compact and reference report/tags rather than duplicating execution report content.

Minimum entry:

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

For `repair`, `redo`, and `replan`, include `Recovery:` naming whether the next action is a targeted repair unit, a redo unit, a design revision, an intent revision, or a plan rewrite.

## Scale Up When

- several valid plan shapes compete
- the next unit is broad or risky
- acceptance criteria are hard to verify against a diff
- design has unresolved assumptions
- later work has dependencies that would make a vague sketch dangerous
- the human asks for more detail

## Human Decision Points

- approval of the current unit
- scope cuts
- sequencing tradeoffs that affect risk or delivery

## LLM Discretion Zone

- plan shape selection (with rationale)
- unit IDs and slugs
- low-risk sequencing
- internal organization
- amount of future detail

## Promotion And Updates

On initial approval:

- promote the approved draft into `docs/accord/plan/plan.md`
- update `docs/accord/accord-state.md`
- commit explicit paths
- tag `accord-plan-v<N>`

On review/update:

- record execution report path and tags in `Review and Update Log`
- `review-update` may advance the next unit directly within its authority — see the precise criteria in `review-update/SKILL.md` (Authority Over plan.md). When any criterion fails, route to `plan` for a new draft.
- route to `design` before further execution when findings invalidate architecture, boundaries, data ownership, dependencies, deployment, security, or verification strategy
- route to `intent` only when implementation has invalidated the project's goal or success criteria (rare)
- commit explicit paths
- tag `accord-review-<unit-id>`

## Before Approval Checklist

- Does `Rationale for Shape` cite concrete facts from the approved `design.md`, not generic planning wisdom?
- Is `Current Approved Unit.Acceptance` checkable against a diff without relying on the executor's narrative?
- Is `Expected scope` narrow enough to tell the executor what is out of bounds?
- Are verification expectations tied to `commands.md` or `design.md` when those artifacts exist?
- Does each advanceable `Later Work` item already include a diff-checkable acceptance criterion, and are unknowns marked `Acceptance: TBD by plan`?
- Is `Review mode` appropriate for the unit's risk?
