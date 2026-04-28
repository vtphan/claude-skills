---
name: execute-wave
description: >-
  Use this skill when the user has an approved Spec and Waves Wave Plan and
  wants the current wave implemented. This skill reads the Wave Plan, executes
  only the current wave tasks, verifies task acceptance checks, updates task
  checkboxes, records acceptance evidence, and writes a Wave Report. Use when
  the user says things like "execute W1", "build the current wave", "implement
  this wave plan", "work through the wave tasks", "start the current wave", or
  provides docs/spec-and-waves/wave-plan.md and asks to build it. Do NOT use for
  drafting specs, drafting backlogs, drafting wave plans, updating completed wave
  plans from reports, or doing future-wave work.
---

# Execute Wave

Implement the current wave from a Spec and Waves Wave Plan. This is the coding skill in the process. It produces code changes, updates current-wave task checkboxes, and writes a Wave Report.

Read `../templates/wave-report.template.md` before writing the report. If it is unavailable, use the report structure in this skill.

## Inputs

- Approved `docs/spec-and-waves/wave-plan.md`.
- The project repository or working directory.
- Optional Starter Spec and Backlog when task context is unclear.

## Outputs

- Code or project changes required by the current wave.
- Updated Wave Plan with only current-wave task checkboxes changed.
- Wave Report at `docs/spec-and-waves/reports/wave-W<N>-report.md`.

Do not update wave status, assumptions, risks, backlog coverage, future-wave sketches, or the change log. That belongs to `update-wave-plan`.

## Core Rule

Execute the current wave only.

The current wave is the wave named by `current_wave` in frontmatter and marked `Status: in_progress`. Do every current-wave task that can be completed honestly. Do not build future-wave work, even if it looks easy.

## Workflow

1. Read the Wave Plan.
2. Identify the current wave and its tasks.
3. Read relevant Starter Spec or Backlog context only when needed.
4. Inspect the codebase enough to follow existing conventions.
5. Execute tasks one at a time.
6. Verify each task's acceptance check.
7. Mark a task `[x]` only after verification.
8. Record acceptance evidence and discoveries as you go.
9. Write the Wave Report.

## Task Execution Rules

- Acceptance checks define done.
- If acceptance cannot be verified, leave the task unchecked and explain why in the report.
- If a task is partly complete, leave the plan checkbox unchanged and mark it `[~]` only in the report.
- Do not rewrite task acceptance checks during execution.
- Do not add tasks to the Wave Plan.
- Do not reorder waves.
- Do not change future-wave sketches.

## When To Stop And Report

Stop and write a report when:

- A task requires future-wave work.
- A task's acceptance check is impossible or ambiguous.
- An assumption is clearly broken.
- A dependency, credential, service, or environment requirement is unavailable.
- Continuing would silently expand scope.
- The current wave is no longer the right work.

When possible, finish the smallest coherent piece first, then report the blocker.

## Requirement Detail

If a current-wave story needs more precision before implementation, draft only the minimal requirement detail needed for that story. Keep it local to the current wave and record it in the report.

Do not create requirement detail for future waves.

## Wave Report

Use this structure:

```markdown
# W<N> <Wave Name> — Report

Wave: W<N>
Completed: YYYY-MM-DD
Wave plan version at start: <N>

## What was built

## Task status

## Acceptance evidence

## Assumptions and risks

## Discoveries

## Proposed changes

## Next-wave readiness
```

Report facts separately from recommendations:

- `What was built`: actual capability delivered.
- `Task status`: task-by-task completion, partials, or blockers.
- `Acceptance evidence`: tests, commands, manual checks, screenshots, or review notes.
- `Assumptions and risks`: what held, broke, materialized, or stayed untested.
- `Discoveries`: learnings that affect future waves, scope, Starter Spec, or Backlog.
- `Proposed changes`: suggested adds, removes, deferrals, or replans for human/updater review.
- `Next-wave readiness`: prerequisites or warnings before the next wave starts.

Omit a section only if it is truly empty.

## What Not To Do

Do not:

- Build future-wave tasks.
- Mark tasks done without verification.
- Fabricate acceptance evidence.
- Change backlog coverage.
- Close the wave.
- Advance `current_wave`.
- Update assumptions or risks in the Wave Plan.
- Write the Wave Plan change log.
- Perform broad refactors unrelated to current-wave acceptance.

## Handoff

At completion, tell the user:

- What current wave work was completed.
- Whether any tasks remain incomplete.
- Where the Wave Report was written.
- Any significant broken assumptions, risks, or proposed scope changes.

The next process step is `update-wave-plan`.

## Commit

Commit at stable execution handoff points:

- For small waves, one commit may include completed code changes, task checkbox updates, and the Wave Report.
- For larger waves, commit coherent completed task groups during execution, then commit the final Wave Report separately if useful.

Commit only files touched for current-wave work. Do not include unrelated working-tree changes.

Use messages that reference wave and task IDs:

- `Wave W1: complete T1.1 import validation`
- `Wave W1: complete T1.2 preview flow`
- `Wave report: record W1 acceptance evidence`
