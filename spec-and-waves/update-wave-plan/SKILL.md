---
name: update-wave-plan
description: >-
  Use this skill when the user has a Spec and Waves Wave Plan plus a completed
  Wave Report and wants the plan reconciled. This skill closes or keeps open the
  current wave, updates assumptions and risks, updates backlog coverage if scope
  changed, expands only the next wave into executable tasks, keeps later waves
  as sketches, and writes the Wave Plan change log. Use when the user says
  things like "update the wave plan", "advance to W2", "close W1", "reconcile
  this wave report", or provides docs/spec-and-waves/wave-plan.md and
  docs/spec-and-waves/reports/wave-W<N>-report.md. Do NOT use for executing
  code, drafting the initial backlog, drafting the initial wave plan, or changing
  the Starter Spec/Backlog directly.
---

# Update Wave Plan

Reconcile a Wave Plan with a Wave Report. This is the interpretation step after execution: decide what the report means for the living plan, update execution state, and prepare the next wave.

## Inputs

- Current `docs/spec-and-waves/wave-plan.md`.
- Wave Report for the current wave: `docs/spec-and-waves/reports/wave-W<N>-report.md`.
- Optional Backlog when coverage or scope changes are proposed.

## Output

Updated Wave Plan in place.

Do not edit the Starter Spec or Backlog directly. If they need changes, record that need in the Wave Plan change log and tell the user.

## Core Rule

Update one wave boundary at a time.

Close or keep open the current wave. If advancing, expand only the next wave into executable detail. Later waves remain sketches.

## Workflow

1. Read the Wave Plan and Wave Report.
2. Verify the report matches the current wave.
3. Check acceptance evidence against current-wave exit criteria.
4. Classify the update: normal, replan, or pivot.
5. Decide whether the current wave can close.
6. Update current wave state.
7. Update assumptions and risks.
8. Reconsider sequencing using risk-first planning.
9. Update Backlog Coverage only if the report justifies a scope or sequencing change.
10. If advancing, expand the next wave into current-wave detail with tasks and acceptance checks.
11. Keep later waves as sketches, revising only where discoveries require it.
12. Increment frontmatter `plan_version`, update `last_updated`, update `current_wave`, and write the change-log entry.

## Evidence Gate

Do not close a wave from task status alone. Compare the report's acceptance evidence against:

- current-wave task acceptance checks
- current-wave exit criteria
- assumptions and risks referenced by the wave

If evidence is missing or weak, keep the wave open or record an explicit deferral/scope change.

## Update Types

**normal**

- Most tasks complete.
- Exit criteria met or only minor gaps remain.
- Discoveries refine later waves but do not change direction.

Action: close current wave, update registers, expand next wave.

**replan**

- Meaningful scope, sequencing, assumption, or risk changes affect multiple future waves.
- The project direction still holds.

Action: close or keep open current wave based on exit criteria, revise coverage and future sketches, expand only the next wave.

**pivot**

- The report challenges the Starter Spec, core Backlog intent, or fundamental project direction.

Action: do not silently rewrite the plan. Record the pivot signal and ask the human lead to revise Starter Spec or Backlog before advancing.

## Closing Current Wave

Close the wave only if:

- Required task acceptance checks are verified, or incomplete work is explicitly deferred or dropped.
- Exit criteria are met or deliberately revised.
- The report contains enough acceptance evidence.

When closing, replace current-wave task detail with a compact closeout summary:

```markdown
### W<N> — <Wave name>

Status: complete
Completed: YYYY-MM-DD
Covers: US-..., F-...
Delivered: What the wave actually produced.
Assumptions resolved: A1 validated; A2 broken -> A4 opened
Report: docs/spec-and-waves/reports/wave-W<N>-report.md
```

If a wave is not ready to close, leave it `in_progress`, keep incomplete tasks, update only what is safe, and write a change-log entry explaining why it stayed open.

## Expanding The Next Wave

When advancing, convert the next future wave sketch into current-wave detail:

- Status: `in_progress`
- Started date.
- Goal.
- Covers.
- Depends on.
- Entry criteria.
- Exit criteria.
- Assumptions.
- Risks.
- Tasks with acceptance checks.

Tasks must be executable by an implementation agent and small enough to verify. Every task needs an acceptance check.

Do not expand W<N+2> or later.

## Risk-First Replanning

Before expanding the next wave, ask:

- Did the report validate or break the risk that W1 was meant to test?
- Did a new risk become more urgent than the planned next wave?
- Did a deferred risk become safe to keep deferred?
- Does the next wave still reduce the most important uncertainty, or is it merely the next item in the old sequence?

If risk priority changes, revise Backlog Coverage and future sketches explicitly. Record the rationale in the change log.

## Backlog Coverage

Maintain coverage for every Backlog item. If the report proposes add/remove/defer changes:

- Update the coverage row only when the change is justified and consistent with the approved Backlog.
- If the change requires Backlog revision, mark it as a proposed Backlog update instead of pretending it is approved.
- Never silently drop a story or feature.

Every coverage change needs a rationale in the table or change log.

## Assumptions and Risks

Assumptions:

- `untested` -> `validated`: add date/evidence.
- `untested` -> `broken`: mark broken, open a replacement assumption with a new ID.
- Never delete assumptions.

Risks:

- Mark materialized, mitigated, unresolved, retired, or changed based on the report.
- Add new risks only when they affect future waves or scope.

Do not pad registers.

## Change Log

Add a new top entry with:

- Update type: `normal`, `replan`, or `pivot-signal`.
- Whether the current wave closed.
- Assumptions and risks changed.
- Evidence used to justify closeout or continued work.
- Coverage changes.
- Next wave expanded, if any.
- Future sketches revised, if any.
- Any needed Starter Spec or Backlog review.

## What Not To Do

Do not:

- Execute code.
- Invent missing report evidence.
- Close a wave whose exit criteria are not met unless the change is explicit.
- Expand more than one next wave.
- Add future-wave task lists.
- Rewrite Starter Spec or Backlog.
- Hide scope expansion inside task wording.

## Handoff

Tell the user:

- Whether the current wave closed.
- What wave is now current.
- Any assumptions, risks, or scope changes they should review.
- Whether Starter Spec or Backlog revision is needed before execution continues.

## Commit

When the Wave Plan update is complete, commit only the relevant Wave Plan file. If the update also records a generated report path, the report should already have been committed by `execute-wave`.

Use concise messages that reference the wave boundary and notable IDs:

- `Wave plan: close W1 and expand W2`
- `Wave plan: keep W1 open for T1.3`
- `Wave plan: mark A2 broken after W1`
