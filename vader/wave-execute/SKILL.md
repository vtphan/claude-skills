---
name: wave-execute
description: Use this skill when a wave plan exists, the current wave is fully planned (in_progress), and the user wants the wave actually built — code written, tests run, task checkboxes ticked, and an execution report produced. Triggers include phrases like "execute the current wave", "build W<N>", "implement the current wave's tasks", "let's do the current wave", "run the wave", or whenever a wave plan is provided and the user wants the tasks in its current wave carried out. Also trigger when the user gestures at next steps ("now build it", "go ahead") *after a successful wave-plan or wave-update* — i.e., the most recent change-log entry's audit verdict was `pass` or `pass-with-findings` and `current_wave` reflects an in-progress, fully-planned wave. Do NOT trigger on "go ahead" after a `blocked-update` (audit verdict `fail`) — re-attempt requires the human to either re-run `wave-execute` for the same current_wave with the explicit recovery path or first run `wave-update` to renegotiate. Do NOT use when no wave plan exists yet (run wave-plan first). Do NOT use to modify the wave plan structurally — only checkbox flips are allowed. Do NOT use when the user wants the wave reviewed and the plan updated — that's wave-update.
---

# Wave Execute

Read the wave plan, do the work of the current wave, and hand back an execution report. This is the only skill that writes code. The other VADER skills produce documents; this one produces *changes*, plus one report.

Before doing anything else, read `references/wave-schema.md` in full — particularly Sections 4 (per-wave structure), 9 (execution report template), and 11 (invariants).

## Inputs and outputs

**Inputs:**
- The wave plan (`<project-slug>-wave-plan.md`). Tells you which wave to execute and what its tasks are.
- The architecture doc + cited Decision Log entries.
- The current project repo / working directory.

**Outputs:**
- Code changes: whatever the wave's tasks require. Real files in the real project.
- The wave plan, with completed task checkboxes flipped from `[ ]` to `[x]`. This is the *only* structural change to the wave plan allowed by this skill.
- An execution report: `<project-slug>-wave-plan.reports/wave-W<N>-execution.md`, conforming to schema Section 9 (with YAML frontmatter including `wave_start_ref` and `wave_end_ref` if git is in use).

## What this skill protects against

The most natural failure mode of agentic execution is **confidently doing more than the plan asks for**. An agent will happily:

- Pre-build tasks from future waves because they "look easy."
- Refactor adjacent code because it "would be cleaner."
- Silently resolve an assumption one way by writing code that depends on it.
- Silently violate a Decision Log entry because the alternative seemed convenient.
- Declare tasks done based on how the code looks, not on whether acceptance criteria pass.

This skill's job is to hold the line against all of those.

## Operating principles

1. **Current wave only, current wave in full.** Do every task in the current wave. Do nothing outside it. Future-wave work, refactors of past-wave code, opportunistic improvements — all go in the report under *Discoveries* or *Proposed scope changes*, not into code.

2. **Acceptance is the definition of done.** A `[ ]` becomes `[x]` only when its acceptance criteria pass. Not when the code compiles. Not when it looks right. When the test is green.

3. **Respect the cited Decision Log entries.** Before writing code for a task, read the ADRs it cites. The implementation must respect them. If you can't, stop and report — don't silently violate.

4. **Stop and report, don't push through.** If execution hits something that requires plan-level or architecture-level judgment, stop. Write the report. Hand back to the user.

5. **Report-first, commit-second.** The report is the primary output. A fully-working wave with no report is worse than a partially-working wave with a clear report — partial preserves learning; no-report destroys it.

6. **Run the repro.** Every wave has a repro path. Build it as part of the wave. Run it. Pass before you mark the wave done.

## Workflow

### 1. Read everything before writing anything

- The wave schema (if not already this session).
- The wave plan in full. Look at: `current_wave`, the section for the current wave, the assumptions/risks registers, the Decision Log references, the most recent change-log entry.
- The vision doc (Goal, Non-goals) for sanity-checking scope.
- The architecture doc and the Decision Log entries cited by the current wave's tasks.
- The repo state — where does prior-wave code live, what's the test setup, what conventions exist.

### 2. Capture the start ref (if git is in use)

If the project is a git repo, capture `git rev-parse HEAD` as the wave's `wave_start_ref`. Hold it in memory; you'll write it to the execution report's frontmatter at the end. If no git, leave the field empty.

### 3. Plan the wave execution briefly

Sketch (mentally; no need to write to disk) the order you'll do the tasks in. Usually: do the task that most reduces uncertainty first. For walking-skeleton W1, this is usually the end-to-end integration task.

### 4. Execute tasks one at a time

For each task:

1. Read the task and its acceptance criteria.
2. Read the ADRs the task cites. Confirm you understand the constraints.
3. Do the work — write/edit code, add tests, run what needs running.
4. Verify acceptance criteria pass. Run the tests; don't assume.
5. Flip the checkbox `[ ]` → `[x]` in the wave plan.
6. Note anything worth keeping for the report.
7. Move to the next task.

If a task blocks — you hit a stop-and-report trigger — leave its checkbox `[ ]`, stop, and write the report.

### 5. Run the repro at the end

Once tasks are done, run the wave's repro path. It must pass. If it doesn't, that's a stop-and-report situation: the wave's exit criteria aren't actually met.

### 6. Write the execution report (still uncommitted)

Use the template from `references/wave-schema.md` Section 9. Save to `<project-slug>-wave-plan.reports/wave-W<N>-execution.md`. Create the directory if it doesn't exist.

Fill `wave_start_ref` from the value captured in step 2a. Leave `wave_end_ref` blank for now — it will be set in step 7 after the commit.

### 7. Commit and capture wave_end_ref

Show the user a brief summary of the report's verdict (tasks done, assumptions broken, ADRs challenged, repro pass/fail). Ask for approval to commit.

On approval, if git is in use (`git rev-parse --is-inside-work-tree` succeeds):
1. `git add` all changed files (code + execution report).
2. `git commit -m "exec: W<N> — <one-line summary>" -m "<details>" -m "Co-authored-by: Claude <noreply@anthropic.com>"`.
3. Capture the resulting commit sha as `wave_end_ref`.
4. Open the execution report and fill in `wave_end_ref` in the frontmatter.
5. Amend the commit to include the now-complete execution report: `git commit --amend --no-edit`.
6. Tag the commit: `git tag W<N>-end`. If the tag name already exists (e.g., a previous `wave-execute` ran for this wave and was reset), warn the user and ask before overwriting.

**Do not push between steps 2 and 5.** Step 5 rewrites the just-made commit; if you've already pushed step 2, step 5 produces a divergent history and the user has to force-push. If you suspect an upstream remote is auto-syncing, capture `wave_end_ref` differently: write the report with a placeholder, commit, then on the next `wave-execute` invocation or via the next skill, the report's `wave_end_ref` is filled retroactively from `git rev-parse W<N>-end`. The amend approach is cleaner when push is fully under the human's control, which is the assumed default.

If git is not in use, leave `wave_end_ref` empty in the report and note in the handoff that `wave-update`'s review subagent will have a fuzzier diff baseline.

### 8. Hand off

Tell the user concisely: what got done, what didn't, where the report is, the commit sha, and the `W<N>-end` tag (if set). The next step is `wave-update`.

## Stop-and-report triggers

**A task depends on future-wave work.** Don't build the future work; report.

**An assumption is clearly broken.** Stop and report; don't silently rewrite the data model.

**A Decision Log entry is impossible to respect.** Don't silently violate; report; let `wave-update`'s review consider supersession.

**Acceptance criteria you can't meet.** Stop, report the gap.

**Surprising dependency or environment issue.** Report; don't fake.

**Scope ambiguity.** Stop, report.

What is *not* a stop-and-report trigger:
- A task is harder than expected but achievable. Keep going.
- You found a small bug in prior-wave code unrelated to your current task. Note in discoveries; don't fix unless it blocks you.
- You have an idea for a better architecture. Note; don't act.

## Writing a good report

**Be specific, not summary.** "Voting is harder than expected" is useless. "A2 (single-choice voting) is broken: ranked-choice scenarios produced 5/8 minority winners; recommend supersede with A6 (ranked)" is useful.

**Name names.** Reference task IDs (T2.3), assumption IDs (A2), Decision Log entry IDs (ADR-004), requirement IDs (US-MEM-1).

**Separate facts from opinions.** "What was built" is fact. "Proposed scope changes" is opinion grounded in fact.

**ADR-adherence section is required.** For each ADR cited by this wave's tasks, say whether the implementation respects it. If not, explain.

**Don't editorialize the plan.** Describe what happened; let `wave-update`'s review interpret what it means.

**Omit only truly empty sections.**

## Things to never do

1. **Never build future-wave work.** Even one line.
2. **Never silently violate a Decision Log entry.** Either respect it, or stop-and-report.
3. **Never mark a task `[x]` without verifying acceptance.**
4. **Never edit the wave plan beyond flipping checkboxes.** All other plan changes are wave-update's job.
5. **Never silently resolve an ambiguity.** Document in discoveries.
6. **Never skip tests to finish faster.**
7. **Never fabricate a report.** If you didn't build a thing, don't claim you did.

## Handoff

When the commit is made, tell the user concisely: what got done, what didn't, where the report is, the commit sha and tag. Suggest `wave-update` as the next step. Do not invoke it.

**Git.** Workflow described in step 7 above. Skill commits both code and execution report (in two phases: initial commit, then amend after writing the final `wave_end_ref` into the report). Tags `W<N>-end`. If the user wants to amend further, `git commit --amend` is straightforward; for a wholesale do-over, `git reset --soft HEAD~1`. See `../references/git-conventions.md`.
