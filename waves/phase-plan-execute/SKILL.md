---
name: phase-plan-execute
description: Use this skill whenever a rolling-wave implementation plan exists (conforming to the schema in references/plan-schema.md) and the user wants the current phase actually built — code written, tests run, task checkboxes ticked, and an implementation report produced. Triggers include phrases like "execute the current phase of the plan", "build P1 of this plan", "implement the current wave", "let's do the current phase", "work through the current phase tasks", or whenever a plan file is provided and the user wants the tasks in its current phase carried out. Also trigger when the user gestures at the next step after drafting or updating a plan ("now build it", "go ahead"). Do NOT use when there is no plan file yet (use phase-plan-draft first), when the user wants to modify the plan without implementing (use phase-plan-update), or for freeform coding requests that aren't tied to a rolling-wave plan.
---

# Phase Plan Execute

Read a rolling-wave plan, do the work of the current phase, and hand back an implementation report. This skill is a build skill — it actually writes code, runs tests, and touches the real system. The other three skills in the pipeline produce documents; this one produces *changes*, plus one document (the report).

Before doing anything else, read `references/plan-schema.md` in full. The schema is the contract this skill operates inside — in particular, the invariants in section 9 and the report template in section 8 are non-negotiable.

## Inputs and outputs

**Inputs:**
- The plan file (`<project>-plan.md`). This tells you which phase to execute and what the tasks are.
- The current project repo / working directory. You're working on a real codebase, not a greenfield sandbox, unless the plan is for a brand-new project.
- Optionally, the source requirements document — read it when a task references a story or feature ID and you need to look up what that requirement actually asks for.

**Outputs:**
- Code changes: whatever the phase's tasks require. Real files in the real project.
- The plan file, with completed task checkboxes flipped from `[ ]` to `[x]`. This is the *only* structural change you are allowed to make to the plan.
- An implementation report: `<project>-plan.reports/phase-P<N>-report.md`. The format is the template in `references/plan-schema.md` section 8.

## What this skill protects against

The most natural failure mode of agentic execution on a plan is **confidently doing more than the plan asks for**. An agent with a rough idea of the project and access to tools will happily:

- Pre-build tasks from future phases because they "look easy."
- Refactor adjacent code because it "would be cleaner."
- Silently resolve an assumption one way by writing code that depends on it.
- Declare tasks done based on how the code looks, not on whether acceptance criteria pass.
- Bury discoveries in commit messages or inline comments instead of reporting them.

Each of these individually is fine-looking. Together, they're exactly what rolling-wave planning is designed to prevent. This skill's primary job is to hold the line against them.

## Operating principles

### 1. Current phase only, current phase in full

The current phase is defined by the plan's `current_phase` frontmatter field and the `### P<N>` section marked `Status: in_progress`. Do every task in that phase. Do nothing outside it.

"Outside it" includes: tasks from future phases, capabilities mentioned in future-phase sketches, refactors of past-phase code (unless a current-phase task explicitly requires it), or opportunistic improvements that "feel obvious." All of those go in the report under *Proposed scope changes* or *Discoveries* — not into code.

If a current-phase task genuinely can't be completed without touching something that belongs to a future phase, that's a signal to **stop and report**, not to quietly do both phases. See [Stop-and-report triggers](#stop-and-report-triggers).

### 2. Acceptance is the definition of done

A task with `[ ]` becomes `[x]` only when its acceptance criteria pass. Not when the code compiles. Not when it looks right. Not when you've "covered the case." When the acceptance test is green.

If a task has multiple acceptance bullets, all of them must pass. If one of them *can't* pass — the test infrastructure doesn't exist, the dependency isn't available, the criterion turns out to be ambiguous — the task stays `[ ]` and the situation is explained in the report. Don't rewrite acceptance criteria mid-execution. If you think a criterion is wrong, flag it in *Proposed scope changes* for the updater to weigh.

### 3. Maintain a running discoveries log

As you execute, things you didn't know when the phase started will surface. Write them down immediately — not at the end of the phase, when you're reconstructing from memory. A scratch file (`.phase-P<N>-scratch.md` in the working directory, or your own running notes) is fine; at phase end, distill it into the report's *Discoveries* and *Assumptions status* sections.

Focus discoveries on things that **affect later phases or challenge the plan's assumptions**. Not every learning is a discovery — "SQLite works as expected" is not a discovery. "SQLite's FTS5 extension is behind a compile flag that's disabled on the default Debian package, which means production deploys will need a custom build" is a discovery, because it changes what P3 looks like.

### 4. Stop and report, don't push through

If execution hits something that would require plan-level judgment to resolve — a broken assumption, a scope question, a dependency on work that's not yet done — stop the current task, write the report, and hand back to the user (who will then invoke `phase-plan-update` with the report). Pushing through is how plans silently drift away from the world they were written for. See [Stop-and-report triggers](#stop-and-report-triggers).

### 5. Report-first, commit-second

The report is the primary output. Code is the secondary output (and will be more fully captured in git history anyway). A fully-working phase with no report is worse than a partially-working phase with a clear report — because the partial phase preserves learning, and the no-report phase destroys it.

## Workflow

### 1. Read everything before writing anything

- Read `references/plan-schema.md` in full (if you haven't this session).
- Read the plan file in full. Look at: `current_phase` in frontmatter, the section for the current phase, the assumptions and risks registers (especially entries referenced by the current phase), the change log (most recent entries — they tell you what the updater just did).
- Read the requirements doc for any story/feature the current-phase tasks cite.
- Read the current state of the codebase enough to orient — where does prior-phase code live, what's the test setup, what conventions exist.

This is not optional. Skipping to execution has predictable failure modes: doing the wrong thing, duplicating existing code, breaking a convention the project already established.

### 2. Plan the phase execution briefly

Before starting tasks, sketch to yourself (you don't need to write this to disk) the order you'll do the tasks in, and which acceptance criteria are likely to be harder to satisfy. Usually: do the task that most reduces uncertainty first. Often this is the end-to-end integration task, even if it feels "bigger" than a unit task.

### 3. Execute tasks one at a time

For each task:

1. Read the task and its acceptance criteria carefully.
2. Do the work — write or edit code, add tests, run what needs running.
3. Verify the acceptance criteria pass. Actually run the tests — don't assume.
4. Flip the checkbox `[ ]` → `[x]` in the plan file.
5. Append anything worth keeping to your discoveries log.
6. Move to the next task.

If a task blocks — you hit one of the stop-and-report triggers — mark it `[~]` in your own notes (don't edit the plan's checkbox to `[~]`, that's not a valid state for the plan), stop, and jump to step 4 of the workflow.

### 4. Write the report

When either (a) all current-phase tasks are complete, or (b) you've hit a stop-and-report trigger, write the report. Use the template from `references/plan-schema.md` section 8 exactly. Save to `<project>-plan.reports/phase-P<N>-report.md`, creating the directory if it doesn't exist.

The report's quality matters more than almost anything else this skill does. See [Writing a good report](#writing-a-good-report).

### 5. Hand off

Tell the user, concisely: what got done, whether any assumptions broke, where the report lives. The next step is theirs — usually, invoking `phase-plan-update` with the report. Don't invoke it yourself.

## Stop-and-report triggers

Stop working, finish whatever task you're in the middle of if it's close, and write the report. These are the situations:

**A task depends on future-phase work.** You thought you could implement T2.3 cleanly, but it turns out to need something that's sketched in P4. Don't build P4 work now — stop, report, let the updater decide whether P4 needs to be pulled forward or the current-phase task needs to be rescoped.

**An assumption is clearly broken.** Not "might be broken" — clearly broken, in a way that makes remaining tasks either meaningless or wrong. Stop and report. An example: the plan assumes single-choice voting (A2), and a task you just built makes it obvious that single-choice produces unacceptable UX. Don't silently change the data model to ranked voting; report A2 as broken, propose ranked voting as a scope change, hand back.

**Acceptance criteria you can't meet.** A task's acceptance says "10k files in under 2s" and your best implementation runs at 4s. Stop, report the gap and what you tried; let the updater decide whether to extend the phase, split the task, or revise the criterion.

**Surprising dependency or environment issue.** The library you expected doesn't exist. The CI system doesn't have the right runner. An auth flow requires a credential you don't have. Report, don't fake.

**Scope ambiguity.** A task's wording can be read two materially different ways and you're about to commit one of them. Stop, report the ambiguity, and pick the lower-commitment interpretation if you must keep moving — but prefer to stop.

What is *not* a stop-and-report trigger:

- A task is harder than expected but achievable. Keep going.
- You found a small bug in prior-phase code unrelated to your current task. Note in discoveries; don't fix unless you're sure it blocks your task.
- You have an idea for a better architecture. Note it; don't act on it in this phase.

## Writing a good report

The report is the executor's most important output. The updater skill reads it with care; downstream phases depend on it. Bad reports create bad updates.

**Be specific, not summary.** "We learned that voting is harder than expected" is useless. "A2 (single-choice voting) is broken: in user-test simulations with 8 members and 3 candidates, the 'winner by plurality' outcome felt arbitrary because 5 out of 8 would have ranked a different book second. Ranked-choice addresses this; schema impact is small (per-vote order column). Recommend replacing A2 with A6 (ranked)." is useful.

**Name names.** Reference task IDs (T2.3), assumption IDs (A2), requirement IDs (US-ORG-1, F-4). The updater is going to cross-reference; help it.

**Separate facts from opinions, but include both.** "What was built" is facts. "Proposed scope changes" is opinions — but opinions grounded in what you just learned. Both are valuable; just don't blend them.

**Don't editorialize the plan.** The report is not the place to say "the plan had the wrong phase ordering." That's a judgment call for the human + updater. Say what you observed; let the plan's maintainer decide what it means for the plan.

**Omit only truly empty sections.** If a section has content, it goes in. Skipping the *Discoveries* section because "nothing surprising happened" is almost always wrong — you just didn't look for surprises hard enough.

## Things to never do

1. **Never build future-phase work.** Even the smallest bit. Even if it's one line. Even if you're "just setting up for it." If it's not in the current phase's task list, it doesn't happen.
2. **Never mark a task `[x]` without verifying acceptance.** If in doubt, leave it `[ ]` and explain in the report.
3. **Never edit the plan beyond flipping checkboxes.** Do not add tasks. Do not reorder phases. Do not change the frontmatter. Do not touch registers. Do not write to the change log. All of that is the updater's job.
4. **Never silently resolve an ambiguity.** If you have to pick an interpretation, document it in the report under *Discoveries* or *Proposed scope changes*.
5. **Never skip tests to finish faster.** Acceptance criteria are the deal. If you can't meet them, say so.
6. **Never fabricate a report.** If you didn't build a thing, don't claim you did. If you don't know whether an assumption held, say "unverified," not "validated."

## What to do if the plan is malformed

If you start reading the plan and it doesn't conform to the schema (no frontmatter, no current phase marked, future phases have tasks, etc.), stop immediately. Don't try to "fix up" the plan — that's the updater's job. Tell the user what's broken and ask them to fix it or run `phase-plan-update` first.

If the plan conforms but the current phase's task list is missing acceptance criteria, same deal. Acceptance criteria are how you know when to stop; without them, you can't honestly execute.

## Worked mini-example of the execution flow

Given a plan with current phase P1 containing four tasks for a small CLI project:

1. Read the plan. `current_phase: P1`. P1 has four tasks, `[ ]` all around. Relevant assumptions: A1 (SQLite is fast enough), A3 (string-prefixed tag namespace). No risks specific to P1 to worry about.
2. Read the repo. It's mostly empty — greenfield project.
3. Planned order: T1.1 (project scaffold) → T1.3 (tagger pipeline, the risky one) → T1.2 (file walker) → T1.4 (end-to-end test).
4. Execute T1.1. Scaffold the project: `pyproject.toml`, a `filetagger/` package, a minimal CLI entry point. Acceptance: `filetagger --help` exits 0. Run it: passes. Flip `[x]`.
5. Execute T1.3. Write the tagger. Acceptance: "tags a sample text file with at least one accurate topic tag." Write code, run against a test fixture, verify at least one expected tag appears. Along the way, notice that the LLM tagger is ~40× slower than the file-walker will be — log a discovery: "tagger throughput may dominate end-to-end time; may affect P3 re-scan design." Flip `[x]`.
6. Execute T1.2. Walk the directory. Acceptance: walks a 1000-file fixture in under 2s. Run: passes. Flip `[x]`.
7. Execute T1.4. Wire it all together, write the E2E test. Acceptance: tag a fixture directory, then query; results match. Run: passes. Flip `[x]`.
8. Write report. "What was built" = the CLI end-to-end. "Task status" = all four done. "Assumptions" = A1 validated (SQLite fine at 1k files), A3 unverified (only used one namespace in P1). "Discoveries" = the tagger-throughput observation, with a specific recommendation for P3. No proposed scope changes. No risks encountered.
9. Hand off: "P1 complete. Report at `filetagger-plan.reports/phase-P1-report.md`. Run phase-plan-update when you're ready to close out P1 and advance to P2."

The discipline above is what makes this loop actually work. Each phase ends with more signal than it started with, and the plan stays honest.
