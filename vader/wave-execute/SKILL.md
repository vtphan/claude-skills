---
name: wave-execute
description: Use this skill when a wave doc exists, the current wave is fully planned (in_progress), and the user wants the wave actually built — code written, tests run, task checkboxes ticked, and an execution report produced. Triggers include phrases like "execute the current wave", "build W<N>", "implement the current wave's tasks", "let's do the current wave", "run the wave", or whenever a wave doc is provided and the user wants the tasks in its current wave carried out. Also trigger when the user gestures at next steps after wave-draft or wave-redraft ("now build it", "go ahead"). Do NOT use when no wave doc exists yet (run wave-draft first). Do NOT use to modify the wave doc structurally — only checkbox flips are allowed. Do NOT use when the user wants the wave reviewed or audited — those are wave-audit and architect-review.
---

# Wave Execute

Read the wave doc, do the work of the current wave, and hand back an execution report. This is the build skill — it actually writes code, runs tests, and touches the real system. The other VADER skills produce documents; this one produces *changes*, plus one document (the report).

Before doing anything else, read `references/wave-schema.md` in full — particularly Sections 4 (per-wave structure), 9 (execution report template), and 14 (invariants).

## Inputs and outputs

**Inputs:**
- The wave doc (`<project-slug>-wave-doc.md`). Tells you which wave to execute and what its tasks are.
- The current project repo / working directory.
- The vision doc and architecture doc + ADRs cited by the current wave. Read for context — never modify.

**Outputs:**
- Code changes: whatever the wave's tasks require. Real files in the real project.
- The wave doc, with completed task checkboxes flipped from `[ ]` to `[x]`. This is the *only* structural change to the wave doc allowed by this skill.
- An execution report: `<project-slug>-wave-doc.reports/wave-W<N>-execution.md`, conforming to schema Section 9.

## What this skill protects against

The most natural failure mode of agentic execution on a plan is **confidently doing more than the plan asks for**. An agent with a rough idea of the project will happily:

- Pre-build tasks from future waves because they "look easy."
- Refactor adjacent code because it "would be cleaner."
- Silently resolve an assumption one way by writing code that depends on it.
- Silently violate an ADR because the alternative seemed convenient.
- Declare tasks done based on how the code looks, not on whether acceptance criteria pass.

This skill's primary job is to hold the line against all of those.

## Operating principles

### 1. Current wave only, current wave in full

The current wave is defined by `current_wave` in the wave doc's frontmatter and the `### W<N>` section marked `Status: in_progress`. Do every task in that wave. Do nothing outside it.

"Outside it" includes: tasks from future waves, capabilities mentioned in future-wave sketches, refactors of past-wave code unless a current-wave task explicitly requires it, opportunistic improvements, and cleanups. All of those go in the report under *Discoveries* or *Proposed scope changes* — not into code.

### 2. Acceptance is the definition of done

A task with `[ ]` becomes `[x]` only when its acceptance criteria pass. Not when the code compiles. Not when it looks right. When the acceptance test is green.

If a task has multiple acceptance bullets, all of them must pass. If one cannot pass, the task stays `[ ]` and the situation is explained in the report. Don't rewrite acceptance criteria mid-execution. If you think a criterion is wrong, flag it in *Proposed scope changes*.

### 3. Respect the ADRs cited by this wave

Every task in the wave doc cites the ADRs it touches. Before writing code, read those ADRs. The implementation must respect them. If you find you cannot — the ADR's decision genuinely doesn't fit the task — stop and report. Do not silently violate an ADR; that's exactly the failure mode `architect-review` exists to catch, and silent violations are how plans drift.

### 4. Stop and report, don't push through

If execution hits something that requires plan-level or architecture-level judgment to resolve, stop. Write the execution report. Hand back to the user (who will then invoke `wave-audit`, then `architect-review`, then `wave-redraft`).

Pushing through is how plans silently drift away from the world they were written for.

### 5. Report-first, commit-second

The report is the primary output. Code is captured by git anyway. A fully-working wave with no report is worse than a partially-working wave with a clear report — because the partial wave preserves learning, and the no-report wave destroys it.

### 6. Run the repro

Every wave has a repro path. Build it as part of the wave. Run it. The repro must pass before you mark the wave done.

## Workflow

### 1. Read everything before writing anything

- The wave schema (if you haven't this session).
- The wave doc in full. Look at: `current_wave`, the section for the current wave, the assumptions and risks registers, the ADR references, the most recent change-log entry.
- The vision doc (Goal, Non-goals, Constraints) for sanity-checking scope.
- The architecture doc and the ADRs cited by the current wave's tasks.
- The repo state — where does prior-wave code live, what's the test setup, what conventions exist.

This is not optional. Skipping it has predictable failure modes: doing the wrong thing, duplicating existing code, breaking conventions.

### 2. Plan the wave execution briefly

Sketch (to yourself, no need to write to disk) the order you'll do the tasks in. Usually: do the task that most reduces uncertainty first. For a walking-skeleton W1, this is usually the end-to-end integration task; for later waves, it's whichever task's acceptance criteria are hardest to satisfy.

### 2a. Capture the start ref (if git is in use)

If the project is a git repo, capture `git rev-parse HEAD` as the wave's `wave_start_ref`. Hold it in memory; you'll write it to the execution report's frontmatter at the end. If the project does not use git, leave the field empty and note in the handoff that audit's diff baseline will be approximate.

### 3. Execute tasks one at a time

For each task:

1. Read the task and its acceptance criteria.
2. Read the ADRs the task cites. Confirm you understand the constraints they impose.
3. Do the work — write/edit code, add tests, run what needs running.
4. Verify acceptance criteria pass. Run the tests; don't assume.
5. Flip the checkbox `[ ]` → `[x]` in the wave doc.
6. Note anything worth keeping for the report (assumptions resolved, ADRs challenged, surprising dependencies).
7. Move to the next task.

If a task blocks — you hit a stop-and-report trigger — leave its checkbox `[ ]`, stop, and write the report.

### 4. Run the repro at the end

Once tasks are done, run the wave's repro path. It must pass. If it doesn't, that's a stop-and-report situation: the wave's exit criteria aren't actually met.

### 5. Write the execution report

Use the template from `references/wave-schema.md` Section 9. Save to `<project-slug>-wave-doc.reports/wave-W<N>-execution.md`. Create the directory if it doesn't exist.

The report begins with YAML frontmatter. Fill `wave_start_ref` from the value you captured in step 2a, and `wave_end_ref` from `git rev-parse HEAD` at the moment you write the report. If git is not in use, leave both fields empty (`wave_start_ref:` with no value).

The report's quality matters more than almost anything else. See [Writing a good report](#writing-a-good-report).

### 6. Hand off

Tell the user concisely: what got done, whether any assumptions broke or ADRs were challenged, where the report lives. The next step is `wave-audit`. Don't invoke it yourself.

## Stop-and-report triggers

Stop the current task, finish whatever you're in the middle of if you're close, and write the report.

**A task depends on future-wave work.** You thought you could implement T2.3 cleanly, but it turns out to need something sketched in W4. Don't build W4 work; report.

**An assumption is clearly broken.** Not "might be" — clearly. Stop and report. Don't silently rewrite the data model to accommodate a change that should be a deliberate plan-level decision.

**An ADR is impossible to respect.** The task cites ADR-X, you tried to implement it under ADR-X's constraint, and the implementation just doesn't work. Don't silently violate the ADR. Report; let architect-review consider whether ADR-X should be superseded.

**Acceptance criteria you can't meet.** Stop, report the gap and what you tried.

**Surprising dependency or environment issue.** Library missing, runtime missing, credential missing. Report; don't fake.

**Scope ambiguity.** A task can be read two materially different ways. Stop, report; pick the lower-commitment interpretation only if you must keep moving.

What is *not* a stop-and-report trigger:

- A task is harder than expected but achievable. Keep going.
- You found a small bug in prior-wave code unrelated to your current task. Note in discoveries; don't fix unless it blocks you.
- You have an idea for a better architecture. Note in discoveries; don't act.

## Writing a good report

The execution report is the executor's most important output. The auditor reads it as a set of claims to verify. The architect-reviewer reads it for adherence cues. The redrafter reads it for learning.

**Be specific, not summary.** "Voting is harder than expected" is useless. "A2 (single-choice voting) is broken: ranked-choice scenarios produced 5/8 minority winners; recommend supersede with A6 (ranked)" is useful.

**Name names.** Reference task IDs (T2.3), assumption IDs (A2), ADR IDs (ADR-004), requirement IDs (US-MEM-1, F-3). The auditor will cross-reference; help.

**Separate facts from opinions.** "What was built" is fact. "Proposed scope changes" is opinion grounded in fact. Both go in; they don't blend.

**ADR-adherence section is required.** For each ADR cited by this wave's tasks, say whether the implementation respects it. If not, explain. The architect-reviewer reads this section first.

**Don't editorialize the plan.** The report is not the place to argue the wave was misplanned. Describe what happened; let architect-review and redraft decide what it means.

**Omit only truly empty sections.** Skipping "Discoveries" because "nothing surprising happened" is almost always wrong — you didn't look hard enough.

## Things to never do

1. **Never build future-wave work.** Even one line. Even if it's "obvious."
2. **Never silently violate an ADR.** Either respect it, or stop-and-report so architect-review can consider supersession.
3. **Never mark a task `[x]` without verifying acceptance.** If in doubt, leave `[ ]` and explain.
4. **Never edit the wave doc beyond flipping checkboxes.** Do not add tasks. Do not reorder. Do not change frontmatter. Do not touch registers. Do not write to the change log. All of that is the redrafter's job.
5. **Never silently resolve an ambiguity.** Document in discoveries or scope changes.
6. **Never skip tests to finish faster.** Acceptance criteria are the deal.
7. **Never fabricate a report.** If you didn't build a thing, don't claim you did. If you don't know whether an assumption held, say "unverified," not "validated."

## What to do if the wave doc is malformed

If the wave doc doesn't conform to the schema (no frontmatter, no current wave marked, future waves have tasks, missing acceptance criteria), stop. Don't try to fix it — that's the redrafter's job. Tell the user what's broken.

If the current wave's task list is missing acceptance criteria, same deal. Without acceptance, you can't honestly execute.

## Worked mini-example

Given a wave doc with current wave W2 and four tasks, ADRs cited: ADR-001 (SQLite), ADR-004 (flat vote columns):

1. Read everything. The W2 plan, A2 (single-choice voting), the ADRs.
2. Read the repo. Understand W1's code shape.
3. Plan order: T2.1 (parser, smallest) → T2.2 (executor, the integration risk) → T2.3 (CLI surface) → T2.4 (E2E + repro).
4. Execute T2.1. Write the parser. Tests pass. Flip `[x]`.
5. Execute T2.2. Build the executor. Notice ADR-004's flat-column model can't represent the ranked voting that user-tests revealed users actually want. Stop-and-report trigger: ADR conflict.
6. Write the execution report. Mark T2.2 progress as `[~]` in the report (don't change the doc's `[ ]`). Document A2 as broken with evidence; recommend A6 (ranked). Document ADR-004 as violated; recommend supersession via architect-review.
7. Hand off. "W2 partial. Stopped on T2.2 because ADR-004 conflicts with the ranked-voting model A2 implies. Report at `<path>`. Next step: `wave-audit`."

That's a clean stop-and-report.

## Handoff

When the report is saved, tell the user concisely: what got done, what didn't, where the report is. Suggest `wave-audit` as the next step. Do not invoke it.

**Git.** If the project uses git, suggest the user commit with `exec: W<N> — <one-line summary of what was built>`. The execution report's `wave_start_ref` and `wave_end_ref` frontmatter fields anchor the wave's diff scope; if those fields are empty, suggest also tagging `W<N>-start` on the prior commit and `W<N>-end` on this commit so `wave-audit` has a clean baseline. Add a `Co-authored-by: Claude <noreply@anthropic.com>` trailer. See `references/git-conventions.md`.
