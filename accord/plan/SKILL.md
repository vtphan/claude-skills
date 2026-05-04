---
name: plan
description: Use this ACCORD skill when approved intent and design artifacts exist and the human lead wants the next implementation plan or unit. Triggers include "accord plan", "draft the plan", "choose the next unit", or "revise the plan". This skill is agent-led; the agent picks the plan shape, justifies it against the approved design, defines the next approved unit, and informs the human. Single draft file, default one iteration. Promotes to docs/accord/plan.md, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Plan

Create or revise the implementation plan. The agent leads: it picks the plan shape, justifies it against the approved design, defines the next approved unit, and informs the human. The human reviews and approves at the gate.

## Posture

`plan` is **agent-led**, not codesigned. Per principle 8, the agent leads and the human approves. Drafts use the same single-draft-file mechanism as intent and design but with a lighter discipline: the **default is one iteration**. The agent produces `plan-draft.md`, the human approves, it becomes `plan.md`. Iteration happens only when the human pushes back via `Consider This` items; the draft is overwritten freely.

## At First Use In A Session

Read:

- `../references/plan-schema.md`
- `../references/draft-conventions.md`
- `../references/design-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

## Operating Approach

1. Read `docs/accord/accord-state.md`.
2. Read canonical `docs/accord/intent.md` and `docs/accord/design.md`.
3. Read current `docs/accord/plan.md` if revising.
4. If planning after execution, read relevant execution reports and review/update log entries.
5. Open `docs/accord/plan-draft.md`. Overwrite freely.
6. Choose a plan shape and justify it explicitly against the design (see below).
7. Define the current approved unit with stable `u-NNN-slug` ID, diff-checkable acceptance, expected scope, verification expectations, and review mode.
8. Inform the human; advise consequential vs procedural.
9. On approval, write the cleaned content as `plan.md`, update state, commit, tag.

## Plan Rationale Must Reference Design

The plan's `Rationale for Shape` must explicitly reference the approved `design.md` — what scope, structure, dependencies, or risk in *this* design make *this* plan shape the fit. Generic shape justifications are insufficient. This is the single most important section for preventing redundancy and contradiction (principle 7).

## Acceptance Must Be Diff-Checkable

Acceptance criteria in `Current Approved Unit` must be checkable against a diff (principle 9). Vague criteria fail this test — a reviewing agent reads the criteria and the diff to verify the unit, without needing the executor's report.

## Approval Advisory

At each plan gate, advise whether consequential or procedural. Plan approvals are often procedural (the agent has chosen and the human waves it through), but unit approvals with subtle acceptance criteria, broad scope, or `fresh-required` review mode are consequential — say so directly.

## Scale Up

See `references/plan-schema.md` Scale Up When.

## Git

The framework requires only the promotion commit. Mid-iteration commits, if any, are operator-discretion.

After approval, commit:

- `docs/accord/plan-draft.md`
- `docs/accord/plan.md`
- `docs/accord/accord-state.md`

Use a `plan:` commit prefix and tag `accord-plan-v<N>`.
