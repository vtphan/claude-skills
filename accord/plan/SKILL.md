---
name: plan
description: Use this ACCORD skill when approved intent and design artifacts exist and the human lead wants the next implementation plan or unit. Triggers include "accord plan", "draft the plan", "choose the next unit", or "revise the plan". This skill is agent-led; the agent picks the plan shape, justifies it against the approved design, defines the next approved unit, and informs the human. Lightweight drafts (default 1 round). Promotes to docs/accord/plan/plan.md, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Plan

Create or revise the implementation plan. The agent leads: it picks the plan shape, justifies it against the approved design, defines the next approved unit, and informs the human. The human reviews and approves at the gate.

## Posture

`plan` is **agent-led**, not codesigned. Per principle 8, the agent leads and the human approves. Drafts use the same numbered-draft mechanism as intent and design for consistency, but with a lighter discipline: the **default is one round**. The agent produces `draft_00.md`, the human approves, it becomes `plan.md`. Multiple rounds happen only when the human pushes back via `Consider This` items.

## At First Use In A Session

Read:

- `../references/plan-schema.md`
- `../references/draft-conventions.md`
- `../references/design-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

## Operating Approach

1. Read `docs/accord/accord-state.md`.
2. Read canonical `intent.md` and `design.md`.
3. Read current `plan.md` if revising.
4. If planning after execution, read relevant execution reports and review/update log entries.
5. Choose a plan shape and justify it explicitly against the design (see below).
6. Define the current approved unit with stable `u-NNN-slug` ID, diff-checkable acceptance, expected scope, verification expectations, and review mode.
7. Inform the human; advise consequential vs procedural.
8. On approval, promote/update `plan.md`, update state, commit, tag.

## Plan Rationale Must Reference Design

The plan's `Rationale for Shape` must explicitly reference the approved `design.md` — what scope, structure, dependencies, or risk in *this* design make *this* plan shape the fit. Generic shape justifications are insufficient. This is the single most important section for preventing redundancy and contradiction (principle 7).

## Acceptance Must Be Diff-Checkable

Acceptance criteria in `Current Approved Unit` must be checkable against a diff (principle 9). Vague criteria fail this test — a reviewing agent reads the criteria and the diff to verify the unit, without needing the executor's report.

## Approval Advisory

At each plan gate, advise whether consequential or procedural. Plan approvals are often procedural (the agent has chosen and the human waves it through), but unit approvals with subtle acceptance criteria, broad scope, or `fresh-required` review mode are consequential — say so directly.

## Scale Up

See `references/plan-schema.md` Scale Up When.

## Git

After approval, commit:

- `docs/accord/plan/draft_NN.md` when a draft was used
- `docs/accord/plan/plan.md`
- `docs/accord/accord-state.md`

Use a `plan:` commit prefix and tag `accord-plan-v<N>`.
