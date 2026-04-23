---
name: wave-execute
description: Use this skill whenever a unified wave doc exists (conforming to the schema in references/wave-schema.md) and the user wants the current wave actually built — code written, tests run, task checkboxes ticked, and an execution report produced. Triggers include phrases like "execute the current wave", "build W1 of this wave doc", "implement the current wave", "do the current wave tasks", "run the E in DEAR", or whenever a wave doc is provided and the user wants the tasks in its current wave carried out. Also trigger when the user gestures at the next step after drafting or redrafting ("now build it", "go ahead", "proceed with W<N>"). Do NOT use when there is no wave doc yet (use wave-draft first), when the user wants to modify the doc without implementing (use wave-redraft), when the just-completed wave needs independent verification (use wave-audit), or for freeform coding requests not tied to a wave doc.
---

# Wave Execute

Read a unified wave doc, do the work of the current wave, and hand back an execution report. This is the only skill in the DEAR loop that actually writes production code, runs tests, and touches the real system. The other three produce documents; this one produces *changes*, plus one document (the execution report).

Before doing anything else, read `references/wave-schema.md` in full. The schema is the contract this skill operates inside — in particular, the invariants in section 11 and the execution report template in section 9 are non-negotiable.

## Inputs and outputs

**Inputs:**

- The wave doc (`<project-slug>-wave-doc.md`). This tells you which wave to execute and what the stories, features, and tasks are.
- The project repo / working directory — the real codebase, not a sandbox, unless this is a greenfield W1.
- Optionally, the last audit report (if one exists) and prior execution reports — useful for context on what was accepted and what was flagged.

**Outputs:**

- **Code changes.** Whatever the current wave's tasks require. Real files in the real project.
- **The wave doc**, with completed task checkboxes flipped from `[ ]` to `[x]`. This is the **only** structural change you are allowed to make to the wave doc.
- **An execution report** at `<project-slug>-wave-doc.reports/wave-W<N>-execution.md`. Format per the schema's section 9.

## What this skill protects against

The most natural failure mode of agentic execution on a wave plan is **confidently doing more than the wave asks for**. An agent with a rough idea of the project and access to tools will happily:

- Pre-build tasks from future waves because they "look easy."
- Refactor adjacent code because it "would be cleaner."
- Silently resolve an assumption one way by writing code that depends on it.
- Declare tasks done based on how the code looks, not on whether acceptance passes.
- Violate an earlier wave's architectural commitment without noticing.
- Bury discoveries in commit messages instead of reporting them.

Each of these individually is fine-looking. Together, they're exactly what the DEAR loop is designed to prevent. This skill's primary job is to hold the line against them — the audit skill then catches anything that slipped past.

## Operating principles

### 1. Current wave only, current wave in full

The current wave is defined by the wave doc's `current_wave` frontmatter field and the `### W<N>` section with `Status: in_progress`. Do every task in that wave. Do nothing outside it.

"Outside" includes: tasks from future waves, capabilities mentioned in future-wave sketches, refactors of past-wave code (unless a current-wave task explicitly requires it), opportunistic improvements. All of those go in the execution report under *Proposed scope changes* or *Discoveries* — not into code.

If a current-wave task genuinely can't be completed without touching something that belongs to a future wave, that's a signal to **stop and report**, not to quietly do both. See [Stop-and-report triggers](#stop-and-report-triggers).

### 2. Acceptance is the definition of done

A task's checkbox flips from `[ ]` to `[x]` only when its acceptance criteria pass. Not when the code compiles. Not when it looks right. Not when you've "covered the case." When the acceptance test passes.

If a task has multiple acceptance bullets, all must pass. If one *can't* pass — test infrastructure doesn't exist, dependency unavailable, criterion turns out to be ambiguous — the task stays `[ ]` and the situation is explained in the report. Don't rewrite acceptance mid-execution. If you think a criterion is wrong, flag it in *Proposed scope changes* for the redrafter to weigh.

### 3. Respect architectural commitments

Before touching code, note the commitments this wave is expected to respect (the wave's `Commitments respected:` field). Cross-check each substantial change against that list:

- About to add a new persistence layer? Check AC1.
- About to introduce a new auth method? Check AC2.
- About to add a runtime dependency? Check AC3.

If a commitment needs to be violated, **stop and report**. Don't unilaterally supersede a commitment. Supersession is the redrafter's job, informed by the execution report. The executor's job is to flag the conflict, not to resolve it.

### 4. Maintain a running discoveries log

As you execute, things you didn't know when the wave started will surface. Write them down immediately — not at the end of the wave, when you're reconstructing from memory. A scratch file (`.wave-W<N>-scratch.md` in the working directory, or your own running notes) is fine; at wave end, distill into the report's *Spec-level discoveries* and *Plan-level discoveries* sections.

Focus discoveries on things that **affect later waves or challenge the doc's assumptions or commitments**. Not every learning is a discovery — "SQLite works as expected" is not a discovery. "SQLite's FTS5 extension is behind a compile flag disabled on the default Debian package, which means production deploys will need a custom build" is a discovery, because it changes what later waves look like.

### 5. Stop and report, don't push through

If execution hits something that would require plan-level judgment to resolve — a broken assumption, a scope question, a commitment conflict, a dependency on undone work — stop the current task, write the report, and hand back to the user (who then invokes `wave-audit` and then `wave-redraft`). Pushing through is how docs silently drift away from the world they were written for.

### 6. Report-first, commit-second

The report is the primary output. Code is the secondary output (and will be more fully captured in git history anyway). A fully-working wave with no report is worse than a partially-working wave with a clear report — because the partial wave preserves learning, and the no-report wave destroys it.

### 7. Both kinds of discovery matter

The report has two discovery sections: *Spec-level* and *Plan-level*. Use both honestly.

- **Spec-level** is for things learned about users, value, or requirements — stories that turned out to be two stories, features that turned out to be unused, roles that turned out to not exist. These feed spec updates in the next redraft.
- **Plan-level** is for things learned about implementation — a library that doesn't behave as documented, a performance ceiling, a test setup that needs rethinking. These feed plan updates in the next redraft.

Don't blend them. The redrafter uses them differently.

## Workflow

### 1. Read everything before writing anything

- Read `references/wave-schema.md` in full (if not already read this session).
- Read the wave doc in full. Look at: `current_wave` in frontmatter, the current wave's full section, the assumptions/risks/commitments registers (especially entries referenced by the current wave), the change log's most recent entry (tells you what the redrafter just decided).
- If prior waves have closed, skim their closeouts for what was delivered — later waves usually extend prior waves' work and you need to know what's there.
- Read the current state of the codebase enough to orient — where does prior-wave code live, what's the test setup, what conventions exist.

This is not optional. Skipping to execution has predictable failure modes: doing the wrong thing, duplicating existing code, breaking a convention.

### 2. Plan the wave execution briefly

Sketch to yourself (you don't need to write this to disk) the order you'll do tasks in, and which acceptance criteria are likely to be hardest. Usually: do the task that most reduces uncertainty first. This is often the end-to-end repro task or the integration task, even if it feels "bigger" than unit tasks — because getting the end-to-end flow working first shakes out integration surprises early.

### 3. Execute tasks one at a time

For each task:

1. Read the task and its acceptance criteria carefully.
2. Cross-check against commitments — is anything you're about to do in tension with an active AC?
3. Do the work — write or edit code, add tests, run what needs running.
4. Verify the acceptance criteria pass. Actually run the tests; don't assume.
5. Flip the checkbox `[ ]` → `[x]` in the wave doc file.
6. Append anything worth keeping to your discoveries log.
7. Move to the next task.

If a task blocks — you hit one of the stop-and-report triggers — leave the checkbox `[ ]`, note the task as blocked in your own notes, stop the main work, and jump to workflow step 5 (write the report).

### 4. Build the repro path

Every wave has a repro path task. Don't treat it as an afterthought. The repro script is what the auditor will run to verify the wave. If the repro is flaky, hard to invoke, or depends on environment the auditor doesn't have, the audit will fail on infrastructure grounds rather than on the wave's substance.

Test the repro yourself, from a clean state, before marking its task complete. If the repro only works on your machine with your setup, it isn't a repro yet.

### 5. Write the execution report

When either (a) all current-wave tasks are complete, or (b) you hit a stop-and-report trigger, write the report. Use the template from `references/wave-schema.md` section 9 exactly. Save to `<project-slug>-wave-doc.reports/wave-W<N>-execution.md`, creating the directory if it doesn't exist.

The report's quality matters more than almost anything else this skill does. See [Writing a good execution report](#writing-a-good-execution-report).

### 6. Hand off

Tell the user concisely: what got done, whether any assumptions broke or commitments came under pressure, where the report lives. The next step is theirs — usually, invoking `wave-audit`. Don't invoke it yourself.

## Stop-and-report triggers

Stop working, finish whatever task you're in the middle of if it's close, and write the report. The situations:

**A task depends on future-wave work.** You thought you could implement T2.3 cleanly, but it needs something sketched in W4. Don't build W4 now — stop, report, let the redrafter decide whether W4 should be pulled forward or the current task should be rescoped.

**An assumption is clearly broken.** Not "might be broken" — clearly broken, in a way that makes remaining tasks either meaningless or wrong. Stop and report. Example: the doc assumes single-choice voting (A2), and a task you just built makes obvious that single-choice produces unacceptable UX. Don't silently change the data model; report A2 as broken, propose the alternative as a scope change, hand back.

**An architectural commitment is under pressure.** A current-wave task seems to require violating an active AC. Stop. Don't unilaterally supersede — that's the redrafter's call. Report the conflict: which AC, what the task needs, what you considered.

**Acceptance criteria you can't meet.** A task's acceptance says "10k files in under 2s" and your best implementation runs at 4s. Stop, report the gap and what you tried.

**Surprising dependency or environment issue.** The library you expected doesn't exist. CI doesn't have the right runner. An auth flow requires a credential you don't have. Report, don't fake.

**Scope ambiguity.** A task's wording can be read two materially different ways and you're about to commit one. Stop, report the ambiguity; if you must keep moving, pick the lower-commitment interpretation and document it — but prefer to stop.

What is *not* a stop-and-report trigger:

- A task is harder than expected but achievable. Keep going.
- You found a small bug in prior-wave code unrelated to your task. Note in discoveries; don't fix unless it blocks your task.
- You have an idea for a better architecture. Note it; don't act on it in this wave.

## Writing a good execution report

The execution report is the executor's most important output. The audit skill reads it with care, verifying its claims. The redraft skill depends on it. Bad reports create bad audits and bad redrafts.

**Be specific, not summary.** "We learned voting is harder than expected" is useless. "A2 (single-choice voting) is broken: in user-test simulations with 8 members and 3 candidates, plurality outcomes felt arbitrary because 5 of 8 would have ranked a different book second. Ranked-choice addresses this; schema impact is small (per-vote order column). Recommend replacing A2 with a new ranked assumption." is useful.

**Name names.** Reference task IDs (T2.3), assumption IDs (A2), commitment IDs (AC3), requirement IDs (US-ORG-1, F-4). The auditor and redrafter cross-reference; help them.

**Separate facts from opinions, but include both.** "What was built" is facts. "Proposed scope changes" is opinions — but opinions grounded in what you just learned. Both are valuable; don't blend them.

**Fill the Exit criteria status section carefully.** The audit skill runs these independently. Don't mark an exit criterion `[x]` unless the acceptance condition is actually met. If it was partially met, mark it `[~]` and describe the gap. The auditor is going to try to verify; lying about exit criteria status gets caught quickly and destroys trust.

**Don't editorialize the wave doc.** The report is not the place to say "the wave's ordering was wrong." That's a judgment call for the redrafter and the user. Say what you observed; let the doc's maintainer decide what it means.

**Omit only truly empty sections.** If a section has content, it goes in. Skipping *Discoveries* because "nothing surprising happened" is almost always wrong — you didn't look hard enough.

## Things to never do

1. **Never build future-wave work.** Even a small bit. Even one line. If it's not in the current wave's task list, it doesn't happen.
2. **Never mark a task `[x]` without verifying acceptance.** If in doubt, leave it `[ ]` and explain in the report.
3. **Never edit the wave doc beyond flipping checkboxes.** Do not add tasks. Do not reorder. Do not touch the frontmatter. Do not modify registers. Do not write to the change log. All of that is the redrafter's job.
4. **Never silently supersede a commitment.** Commitment conflicts stop-and-report. The redrafter, informed by the audit, is the one who supersedes.
5. **Never silently resolve an ambiguity.** Document the interpretation you picked in the report.
6. **Never skip tests to finish faster.** Acceptance criteria are the deal.
7. **Never fabricate a report.** If you didn't build a thing, don't claim you did. If you don't know whether an assumption held, say "unverified," not "validated."

## What to do if the wave doc is malformed

If the wave doc doesn't conform to the schema (no frontmatter, no current wave marked, future waves have task detail, current wave missing acceptance, etc.), stop immediately. Don't "fix up" the doc — that's the redrafter's job. Tell the user what's broken and ask them to resolve it (likely by invoking `wave-redraft` or editing by hand).

If the doc conforms but the current wave's tasks are missing acceptance criteria, same deal. Acceptance is how you know when to stop; without it, you can't honestly execute.

## Worked mini-example of the execution flow

Given a wave doc with current wave W2 containing four tasks for a small CLI project:

1. Read the doc. `current_wave: W2`. W2 has four tasks, all `[ ]`. Relevant commitments: AC1 (SQLite), AC2 (remote LLM API), AC3 (single-binary). Relevant assumptions: A3 (string-prefix tag namespace), A4 (query latency dominated by SQLite).
2. Read the repo. W1 already shipped the scan-and-tag pipeline. Code is laid out in `filetagger/scan.py` and `filetagger/index.py`. Tests in `tests/`.
3. Planned order: T2.1 (parser, risky) → T2.2 (executor) → T2.3 (CLI surface) → T2.4 (end-to-end repro).
4. Execute T2.1. Write the parser. Acceptance: unit tests pass. Run: passes. Flip `[x]`. No commitment impact.
5. Execute T2.2. Write executor. Acceptance: benchmark on 10k-file fixture. Run it: passes at 1.4s p95. Flip `[x]`. Note in discoveries: "A4 holds — query latency dominated by SQLite as predicted; benchmark confirms."
6. Execute T2.3. CLI surface. Acceptance: `--help` works, exit codes right, output format. Run: passes. Flip `[x]`.
7. Execute T2.4. Write `scripts/demo-w2.sh`. Run it from clean state. It fails: the demo script's `pip install` step contradicts AC3 (single-binary). Stop. Note the conflict in scratch.
8. Write report. *What was built*: three of four tasks complete. *Task status*: T2.1, T2.2, T2.3 done; T2.4 blocked. *Commitments status*: AC3 under pressure — demo script as written pulls in a Python runtime, contradicting single-binary commitment; options are to ship the demo as part of the binary or to supersede AC3. *Discoveries*: plan-level — single-binary constraint wasn't fully internalized when sketching T2.4; need to decide between supersede and refactor. *Proposed scope changes*: ask redrafter to either (a) pull forward a W3 task to package the demo inside the binary, or (b) supersede AC3 to allow a separate demo harness.
9. Hand off: "W2 is 3/4 done. T2.4 blocked on an AC3 conflict. Report at `filetagger-wave-doc.reports/wave-W2-execution.md`. Next step: run wave-audit, then wave-redraft."

The discipline above is what makes the DEAR loop actually work. Each wave ends with more signal than it started with, and the doc stays honest.
