---
name: phase-plan-update
description: Use this skill whenever a rolling-wave implementation plan exists AND an implementation report from the executor is available, and the user wants the plan advanced — current phase closed out, registers updated based on what was learned, next phase expanded into full detail, and remaining phases re-sketched. Triggers include phrases like "update the plan with this report", "close out the current phase", "advance the plan", "plan the next phase given what we just learned", "here's the P1 report, update the plan", or whenever both a plan file and a phase-report file are provided together. Also trigger when the user says "we finished the current phase" or "now let's plan the next one" following a phase-plan-execute run. Do NOT use when there is no report (the executor hasn't run yet), when no plan exists (use phase-plan-draft first), or when the user wants to modify plan structure without a corresponding report — that's a sign something has drifted and should be reconciled by hand.
---

# Phase Plan Update

Reconcile a rolling-wave plan with an executor's implementation report, producing the next version of the plan. Before doing anything else, read `references/plan-schema.md` in full — the schema is the contract this skill operates inside, and violating it corrupts the plan's audit trail.

This is the most consequential skill in the pipeline. The other three create or implement; this one interprets. Every update is an opportunity to absorb signal or to dilute it. The discipline below is what keeps the plan honest across update cycles rather than drifting into fiction.

## Inputs and output

**Inputs:**
- The current plan file (`<project>-plan.md`).
- The executor's report (`<project>-plan.reports/phase-P<N>-report.md`) where `P<N>` matches the plan's `current_phase`.
- Optionally, the source requirements document — useful when the report proposes scope changes that would affect requirements coverage.

**Output:** the plan file, updated in place. A new report entry pointer is added to the closed-out phase. The frontmatter's `plan_version` is incremented, `last_updated` bumped, `current_phase` advanced, and the change log has a new entry at the top.

## The one-rule core of this skill

**Evaluate first, edit second.** Before you change a single line of the plan, decide what kind of update this is. Normal updates and pivots look extremely different, and doing the wrong kind silently wastes the plan's history. Most failure modes of a replanner come from rushing to edit — don't.

## Operating principles

### 1. Evaluation-first sequencing

The steps are ordered deliberately. Evaluation sits *before* closeout because closeout's shape depends on what the evaluation concluded.

1. **Evaluate the report** — decide the update type (see [Update type detection](#update-type-detection)) and identify what's different about the world now compared to when the plan was last written.
2. **Close out the current phase** — turn its detailed section into a closeout summary. Use the exit criteria (not the report's self-assessment) as the test for whether the phase is actually done.
3. **Update the registers** — mark assumptions validated or broken, open replacements for broken ones, update or add risks, incorporate discoveries.
4. **Expand the next phase** — take the sketch from the plan, revise it based on what was learned, and fill it out to current-phase level of detail (tasks with acceptance criteria).
5. **Re-sketch remaining phases** — adjust forward sketches where the learnings require it. Preserve intent; revise detail.
6. **Update frontmatter and append change log** — bump `plan_version`, advance `current_phase`, update `status`, write the change log entry describing what you just did.

Doing these out of order — e.g., expanding the next phase before updating assumptions — produces a plan where the next phase relies on outdated beliefs. Order matters.

### 2. Atomic update

The plan is either fully updated or not updated at all. There is no half-updated state. If you can't complete the full sequence — e.g., the report is ambiguous on a critical point — stop and flag it for the user rather than leaving the plan in a partial state.

### 3. Preserve history

The assumption register is never shrunk. Broken assumptions stay as history; new assumptions get new IDs. The change log is never rewritten. Past-phase closeout summaries are never deleted, even as the plan ages.

This matters because when a future update pass encounters a surprise, the path back to understanding *why* the plan looked the way it did runs entirely through the history. Delete the history and the plan becomes impossible to reason about two updates from now.

### 4. Be conservative about scope

Every update is a chance for the plan to accrete features. Resist. New work enters the plan only if:

- The report explicitly proposes it (scope change), and you agree it's necessary to the stated goal; or
- A broken assumption makes it mandatory (the old plan assumed X; X is false; Y must be done to keep the plan working).

"Might be nice" is not sufficient. When in doubt, defer — and note the deferral as an explicit change-log entry so the user can see what you chose not to do.

### 5. Trust the report, verify the claims

The report is the executor's account. It's usually accurate. But the updater is the one checking claims against exit criteria and assumption status, not the executor. If the report says "all tasks complete" but `[ ]` checkboxes remain in the plan, or an exit criterion doesn't obviously map to a completed task, ask — don't rubber-stamp.

## Update type detection

Before editing, classify the update. The three types are structurally different.

### normal-update

Signals:
- All current-phase tasks completed.
- Exit criteria met.
- At most one or two assumptions validated or broken, with clear replacements.
- No major proposed scope changes.
- Discoveries refine future phases but don't redirect them.

Action: the standard sequence. Close out, refine registers, expand the next sketch, light re-sketching of remaining.

### substantial-replan

Signals:
- Multiple assumptions broken with cascading implications.
- Report proposes non-trivial scope changes (add/defer/remove) across multiple future phases.
- One or more future phase goals need rewording based on learnings (not just the sketch detail).
- Possibly the phase *order* needs revisiting.

Action: the standard sequence, but the re-sketching step is substantive — future phase sketches are revised, not just touched up. The change-log entry is longer and explicit about what the user should notice.

### pivot

Signals:
- A core assumption in the plan's goal or approach is broken.
- The report's Proposed scope changes or Discoveries suggest the plan's whole direction should change.
- The phase just completed demonstrated that the stated goal is wrong, unreachable, or misaligned with what users actually need.

Action: different flow. Stop after the evaluation step and present your pivot interpretation to the user for confirmation before editing. A pivot is where you should always loop in the human — getting a pivot wrong is much more expensive than getting a normal update wrong. When you do proceed, set frontmatter `status: pivoted`, retire affected phase IDs (never reuse them), introduce new phase IDs, and write a change-log entry that names the prior phase IDs being retired and the new ones being introduced.

If you're genuinely unsure whether this is a substantial replan or a pivot, treat it as a pivot — the cost of asking the human is low; the cost of silently redirecting the plan is high.

## Closeout procedure

Turning a current phase into a past phase. Replace the detailed phase section with a closeout summary (per `references/plan-schema.md` section 4 "Past phases"). Specifically:

1. Set `Status: complete` (or `pivoted` or `deferred` if applicable — judge from the report). Set `Completed: <date>`.
2. Preserve `Covers:` from the old detail.
3. Write a `Delivered:` paragraph based on the report's *What was built*. This should describe capability, not tasks — a reader should be able to tell what the system can now do without reading the report.
4. Record `Assumptions resolved:` — list each assumption that was validated or broken during this phase and what happened to it (e.g., `A2 validated`, `A4 broken → A6 opened`).
5. Add `Report: <path>` pointing to the archived report.
6. Delete the task list, exit criteria, and other current-phase-only fields. They're captured in the report and no longer need to live in the plan.

If the report indicates any task was NOT completed (the `[~]` notation in the report's Task status):

- If the task is still relevant to the phase and blocks exit criteria: the phase is not actually complete. Either keep P<N> open with the incomplete task, or — if the user agrees — move the task to the next phase and close this one. This is a judgment call; default to keeping the phase open and asking.
- If the task is no longer relevant (e.g., superseded by a scope change): close the phase and note the task as dropped in the change log.

## Register maintenance

### Assumptions

For each assumption in the register that has new status from the report:

- `untested` → `validated`: update the status with the date. Nothing else.
- `untested` → `broken`: mark broken, date it, and open a new assumption that replaces it. The new assumption's body says what we now believe, with `Replaces: A<old>` in its metadata. Phases and tasks referring to the old assumption continue to cite the old ID for traceability; *new* references use the new ID.
- `open` → `validated` or `broken`: same rules as above.

For each new assumption surfaced by the report's *Discoveries*, add a new entry with status `open` (if it's a current-state claim) or `untested` (if it's a claim we'll validate in a future phase).

**Never edit an existing assumption's body** — if the assumption turned out to be wrong, open a replacement. The history of what we believed and when matters.

### Risks

For each risk in the register that was mentioned in the report:

- "R<N> did not materialize" — update status to `retired (did not materialize)`.
- "R<N> materialized, mitigation worked" — update status to `triggered — mitigated`.
- "R<N> materialized, mitigation failed" — update status to `triggered — unresolved`, and either add new mitigation or promote to assumption (if the failure mode is now a belief about how the system works).

For new risks surfaced in the report, add entries with the standard shape.

### Requirements coverage

If the report's scope changes move requirements between phases or to Deferred, update the coverage table. Every story/feature must still be accounted for after the update.

## Expanding the next phase

The next phase sketch in the plan needs to become a fully-detailed phase section with tasks and acceptance criteria. Specifically:

1. Start from the existing sketch. Preserve its goal and covers unless the learnings require changes.
2. Refine the **entry criteria** — these may change based on what the just-closed phase actually produced.
3. Tighten the **exit criteria** — often the sketch was vague; now with the current state known, you can make them testable.
4. Break the work into **tasks with acceptance criteria**. Same rules as `phase-plan-draft`: every task has acceptance, tasks are sized for an agent session, ordering puts uncertainty-reducing tasks first.
5. List **assumptions** this phase depends on — many will already be in the register; add any new ones the phase newly relies on.
6. List **risks** this phase is exposed to.
7. Set `Started: <date>` and `Status: in_progress`.

**Do not pre-plan phase N+2 or beyond.** Only the *single* next phase is expanded per update cycle. The invariant is absolute: one expansion per update.

## Re-sketching remaining phases

For each phase beyond the newly-expanded one, re-read its sketch with the learnings in mind. Ask:

- Is the goal still sensible given what we now know?
- Does the entry criterion still make sense?
- Are new or revised assumptions relevant?
- Do scope changes affect what's in or out?

If yes to any of those, revise the sketch. If no, leave it alone — don't polish sketches that don't need polishing, you'll just waste tokens and risk introducing drift.

**Remember the invariant**: future-phase sketches never get task detail. The re-sketching edit is at the sketch level — goal, entry/exit criteria, assumptions, risks, the 2-4 sentence approach sketch.

## Frontmatter and change log updates

### Frontmatter

- `plan_version`: increment by 1.
- `last_updated`: today's date, ISO format.
- `current_phase`: advance to the next phase's ID.
- `status`: usually stays `in_progress`. Set to `pivoted` if the update is a pivot (and leave as `pivoted` until a subsequent normal or substantial update cycle clears it). Set to `complete` if there are no more phases.

### Change log entry

Append a new entry (at the *top* of Section 7, so most-recent-first is the reader order, but *new* content is appended — don't rewrite existing entries). Format per `references/plan-schema.md` section 7. Be specific:

- Which phase was closed, and whether exit criteria were fully met.
- Which assumptions changed status; which new ones were opened.
- Which risks changed status; which new ones were opened.
- What scope changes were absorbed (adds, removes, defers).
- Which phase was expanded to current; what was materially different about the expansion compared to the previous sketch.
- Which remaining phases were re-sketched (by ID) and why.

A good change-log entry should be readable in isolation — a user coming back six months later should understand what happened in this update from this entry alone.

## Invariants — things to never do

From the schema, restated because these are the most common failure modes for this skill:

1. **Never expand more than one phase per update.** Expand *only* the new current phase. Others stay sketches.
2. **Never delete assumptions.** Broken ones are marked and superseded; they stay in the register.
3. **Never rewrite change log entries.** Only append new ones.
4. **Never silently add or remove scope.** Every add/remove/defer gets an explicit change-log bullet.
5. **Never close out a phase whose exit criteria aren't met** — unless the criteria themselves are being renegotiated, in which case that's a scope change and goes in the change log.
6. **Never reuse retired phase IDs.** After a pivot, P3 stays retired; introduce P5, P6, etc.
7. **Never trust the report without reading the plan.** The report is one input; the plan's own exit criteria and invariants are the check.

## What to do if the report is malformed

If the report doesn't conform to the schema's report template (sections missing, no task status, no assumption update), stop. Don't try to guess what the executor meant. Ask the user to have the executor produce a conformant report, or ask them what they'd like you to infer — but don't invent it.

If the report says "task T<X> complete" but the plan's checkbox is still `[ ]`, cross-check against the exit criteria. If the executor forgot to flip a checkbox but the work is clearly done, go ahead — but note the discrepancy in the change log.

## Worked mini-example

Given:
- A plan with `current_phase: P2` and 4 tasks in P2, all `[x]`.
- A report that says all tasks complete, A4 (single-choice voting) broken, proposes adding a ranked-voting data migration to P3.

The updater's sequence:

1. **Evaluate.** All tasks done, exit criteria look met, one assumption broken with a clear replacement, scope change proposed for P3. Classification: **normal-update** (one broken assumption is within normal bounds; the scope change is contained to one future phase).
2. **Close out P2.** Status → complete. Delivered paragraph drawn from *What was built*. Assumptions resolved: `A4 broken → A7 opened`. Task list gone. Report path added.
3. **Update registers.** `A4` marked broken with date. `A7` opened: "Voting is ranked-choice (single-transferable-vote tie-break)". `Replaces: A4`. No new risks.
4. **Expand P3.** Read the existing sketch. Pull in the proposed migration task. Write tasks with acceptance criteria. Set started date. Status → in_progress.
5. **Re-sketch P4.** P4 used to assume a certain data shape for the scheduling UI; now it needs to inherit the ranked-voting list shape. Revise two sentences of the sketch; no task detail.
6. **Frontmatter.** `plan_version: 2 → 3`. `current_phase: P2 → P3`. `last_updated: today`.
7. **Change log.** New entry at top of Section 7, type `normal-update`, naming P2 closeout, A4/A7 swap, P3 expansion with ranked-voting migration added, P4 re-sketch noting the data-shape inheritance.

Now write the file. Done.

## Handoff

After the update, the plan is ready for the next execute cycle. Tell the user what phase is current, any significant changes they should know about, and point them at the updated plan file. They'll invoke `phase-plan-execute` when ready to start the new phase.
