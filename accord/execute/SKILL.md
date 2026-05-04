---
name: execute
description: Use this ACCORD skill when canonical intent, design, and plan artifacts exist and the human lead wants the current approved unit implemented. Triggers include "accord execute", "execute the current unit", "implement the approved unit", or "build the next unit". Do not invoke on bare phrases like "go ahead" or "do it" without explicit ACCORD context. This skill writes code, writes docs/accord/reports/exec-<unit-id>.md using the approved u-NNN-slug ID, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Execute

Implement the current approved unit from `plan.md` and write a self-sufficient execution report.

## Posture

`execute` is **agent-led**. The agent implements with professional judgment inside approved boundaries. It stops only for genuinely consequential changes — the list below is examples of when to stop, not a checklist to traverse.

## At First Use In A Session

Read:

- `../references/execution-report-schema.md`
- `../references/plan-schema.md`
- `../references/design-schema.md`
- `../references/commands-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

## Operating Approach

1. Read `docs/accord/accord-state.md`.
2. Read canonical `intent.md`, `design.md`, `plan.md`.
3. Read `docs/accord/commands.md` if it exists. This is the source of truth for verification commands; do not paraphrase or guess if the file is present.
4. Identify the current approved unit ID, acceptance criteria, verification expectations, expected scope, and review mode.
5. Inspect the repo enough to execute in the existing style.
6. If git is in use, inspect dirty files. Continue around unrelated dirty files only when explicit-path commits and verification remain safe; stop and ask when dirty files overlap the approved unit, affect verification, obscure the diff, or make explicit-path commits unsafe.
7. Implement the approved unit.
8. Run appropriate verification (use `commands.md` first, then `design.md` Verification Expectations, else infer and state the inference).
9. Write `docs/accord/reports/exec-<unit-id>.md` as a self-sufficient report (see below).
10. Ask for human approval; advise consequential vs procedural.
11. Commit explicit paths and tag `accord-exec-<unit-id>` using the approved unit ID, including any repair/redo suffix.

## Rejection Before Approval

If the human declines approval at the execute gate, the work is recoverable without git surgery: code is modified but uncommitted, and the `accord-exec-<unit-id>` tag has not been created. The agent does not finalize `accord-state.md`, update `Current Unit.status`, commit, or tag until the human approves an exit from the rejection loop, so state stays in `executing` (or `repairing` / `redoing` for recovery units) while revisions continue.

Rejection paths the agent should support. In all reversal paths, **revert only the edits introduced by this execute attempt** — never use blanket `git restore <path>` when the path may carry pre-existing uncommitted edits, because that wipes work the framework did not create. When path ownership is ambiguous, stop and ask.

- **Revise.** The human points to specific issues. The agent fixes them, re-verifies, updates the report, asks again. May iterate several times. The execution report is a living document during this loop; it is finalized and committed once on approval, not versioned per attempt.
- **Trim scope.** The human says implementation expanded beyond the approved unit. The agent reverts only the out-of-scope edits this attempt introduced — use targeted edits to undo the offending changes. Use `git restore <path>` only when the path was clean at the start of the attempt and the agent is certain no pre-existing uncommitted edits exist on it. If the path's edits are partly attempt-introduced and partly pre-existing, stop and ask the human how to disambiguate. Update the report and ask again.
- **Route to `plan`.** If the rejection implies the approved unit was wrong (acceptance criteria missed the point, scope was incoherent, the design assumption broke during implementation), the agent recommends routing to `plan` for a new draft and asks the human to approve that route. After route approval, set `accord-state.md` `status: replanning`, set `Next.recommended_skill: plan`, record the reason in `Next.notes`, and do not commit the work-in-progress.
- **Discard.** If the human asks to abandon the unit, revert only this attempt's edits. For files the agent created from scratch in this attempt, deletion is safe. For files the agent modified, use targeted edits to undo the attempt's specific changes (or `git restore <path>` only when the path was clean at the start of the attempt). If pre-existing uncommitted edits may exist on any modified path, stop and ask before reverting. The unit remains approved in `plan.md` and can be retried later as a normal `execute` invocation — no exec tag exists yet, so no formal `redo` is needed.

Pre-commit rejection is not the same as `review-update`'s `redo` verdict. `redo` is post-commit, after `accord-exec-<unit-id>` has been created and tagged; it requires reverting or superseding the tagged commit. Pre-commit rejection has no exec tag yet, so iteration in place is the correct response.

## Stop For Human Approval — Examples

The agent stops when its judgment says the change is consequential. Examples:

- expanding scope beyond the approved unit
- changing design decisions
- adding consequential dependencies
- accepting meaningful debt
- weakening acceptance criteria
- choosing repair versus redo after a blocker

These are not a checklist; the agent applies judgment. Routine implementation tactics inside approved scope do not require stopping.

## The Report Is Load-Bearing

The execution report is the executor's only narrative to the reviewing agent and must satisfy principle 9.

For each acceptance criterion, name where in the diff it is satisfied — file paths, function names, test names. Vague claims ("auth works") fail review; concrete pointers ("`auth/login.ts:handleSubmit`; test: `auth/login.test.ts:happy_path`") succeed.

For verification, name commands run and outcomes. The reviewer should be able to re-run them.

See `references/execution-report-schema.md` for the contract.

## Approval Advisory

At the execute gate, advise whether the unit is procedural (clean implementation, evidence aligned) or consequential (deviations, accepted debt, design questions). For `fresh-required` units, the gate is more often consequential.

## Git

After approval, commit code changes, the execution report, `accord-state.md`, and `commands.md` if changed, using explicit paths. Use an `exec:` prefix and tag `accord-exec-<unit-id>`.
