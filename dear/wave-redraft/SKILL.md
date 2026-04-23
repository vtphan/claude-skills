---
name: wave-redraft
description: Use this skill whenever a wave doc exists AND both an execution report and an audit report are available for the current wave, and the user wants the doc advanced to the next version — current wave closed, registers updated based on what was learned and what audit flagged, next wave expanded from sketch into full detail (both spec and plan), remaining waves re-sketched, change log appended. Triggers include phrases like "redraft the wave doc", "close out the current wave", "advance to W<N+1>", "update the wave doc with these reports", "run the R in DEAR", "finalize this wave and plan the next", or whenever a wave doc plus matching execution and audit reports are provided together. Also trigger when the user says "we finished W<N>, now what" following a wave-audit run. Do NOT use when there's no audit yet (run wave-audit first), when no wave doc exists (use wave-draft first), when the user only wants execution (use wave-execute), or when the user wants to modify the doc structurally without corresponding reports (that's a sign something has drifted and should be reconciled by hand).
---

# Wave Redraft

Reconcile a wave doc with its execution and audit reports, producing the next version of the doc. Before anything else, read `references/wave-schema.md` in full — the schema is the contract, and violating it corrupts the doc's audit trail.

This is the most consequential skill in the DEAR loop. The other three produce or implement or verify; this one **interprets**. Every redraft is an opportunity to absorb signal or to dilute it. The discipline below is what keeps the doc honest across redraft cycles rather than drifting into fiction.

## Inputs and outputs

**Inputs:**

- The current wave doc (`<project-slug>-wave-doc.md`).
- The execution report (`<project-slug>-wave-doc.reports/wave-W<N>-execution.md`) where `W<N>` matches the doc's `current_wave`.
- The audit report (`<project-slug>-wave-doc.reports/wave-W<N>-audit.md`) for the same wave.
- Optionally, the source brief/spec — useful when scope changes would affect framing in Section 1.

**Output:** the wave doc, updated in place. The current wave is compressed into a closeout. The next wave is expanded from sketch into full current-wave detail. The registers reflect new reality. The frontmatter is bumped. A new change-log entry is appended at the top of Section 8.

## The one-rule core of this skill

**Evaluate first, edit second.** Before changing a single line, decide what kind of redraft this is. Normal redrafts, substantial redrafts, and pivots look extremely different; doing the wrong kind silently wastes the doc's history. Most failure modes of a redrafter come from rushing to edit — don't.

## Operating principles

### 1. Honor the audit verdict

The audit report carries a verdict. The redrafter does not override it; the redrafter acts on it.

- **pass** — proceed with normal redraft flow.
- **pass-with-findings** — proceed, but every finding gets addressed in the redraft: either absorbed into the next wave's plan, noted in the change log, or resolved through a commitment supersede / assumption replacement. No finding is silently ignored.
- **fail** — do not close out the current wave. Either (a) surface to the user that the wave needs more execution (loop back), or (b) the user accepts the failure and renegotiates scope explicitly (which is itself a redraft action — with a conspicuous change-log entry).

A `fail` that is closed out anyway, without renegotiation, is a silent lie to the doc. Don't.

### 2. Evaluation-first sequencing

The redraft steps are ordered deliberately. Doing them out of order produces a plan that relies on outdated beliefs.

1. **Evaluate** — decide the redraft type (see [Redraft type detection](#redraft-type-detection)) and identify what's different about the world now compared to when the doc was last written.
2. **Close out the current wave** — turn its detailed section into a closeout summary. Use exit criteria (not the report's self-assessment) as the test for actual doneness.
3. **Update the registers** — mark assumptions validated or broken, open replacements, update risks, supersede commitments where applicable, open new commitments the wave established.
4. **Absorb audit findings** — each finding either triggers a register change, influences the next wave's plan, or gets a change-log note explaining why it's being deferred.
5. **Expand the next wave** — take the existing sketch, revise it in light of learnings, and expand it to current-wave level of detail (stories with acceptance, features, tasks with acceptance, exit criteria, repro path).
6. **Re-sketch remaining waves** — adjust forward sketches where learnings require it. Preserve intent; revise detail.
7. **Update Section 9** (themes not yet waved) if any have been pulled into waves or any new ones have surfaced.
8. **Update frontmatter and append change log** — bump `wave_doc_version`, advance `current_wave`, update `status`, write the change-log entry.

### 3. Atomic redraft

The doc is either fully redrafted or not updated at all. There is no half-redrafted state. If you can't complete the full sequence — e.g., the audit verdict is `fail` or the reports disagree on a critical point — stop and flag it for the user rather than leaving the doc in a partial state.

### 4. Preserve history

Registers are append-only. Broken assumptions stay as history; new assumptions get new IDs. Superseded commitments stay visible with their supersede pointer. The change log is never rewritten. Past-wave closeout summaries are never deleted, even as the doc ages.

This matters because when a future redraft encounters a surprise, the path back to understanding *why* the doc looked the way it did runs entirely through the history. Delete the history and the doc becomes impossible to reason about two redrafts from now.

### 5. Be conservative about scope

Every redraft is a chance for the doc to accrete features. Resist. New work enters only if:

- The execution report explicitly proposes it (scope change), and you agree it's necessary to the stated goal; or
- An audit finding makes it mandatory; or
- A broken assumption or superseded commitment makes it unavoidable (the old doc assumed X; X is false; Y must be done to keep the doc working).

"Might be nice" is not sufficient. When in doubt, defer — and note the deferral as an explicit change-log entry so the user can see what you chose not to do.

### 6. Trust the audit more than the execution report

When the reports disagree:

- The execution report is the executor's account.
- The audit report is the auditor's independent check.
- When the audit contradicts the execution report, the audit wins — because the audit verified claims the executor merely made.

Exception: if you have clear reason to believe the audit was wrong (e.g., it was run without the repro script it should have run), name that explicitly in the change log as a redrafter judgment, and proceed with care. Don't override an audit silently.

### 7. One expansion per redraft

Only the *single* next wave is expanded to full detail per redraft. Wave 4 stays a sketch until wave 3 has executed and been audited. This invariant is absolute — violating it is the most expensive failure mode of redrafting, because it poisons the rolling-wave discipline.

## Redraft type detection

Before editing, classify the redraft. The three types are structurally different.

### normal-redraft

Signals:

- Audit verdict is `pass` or `pass-with-findings`.
- All current-wave tasks completed (or any `[~]` partials are explicitly deferred).
- Exit criteria met.
- At most one or two assumptions validated or broken, with clear replacements.
- Commitments largely respected; zero or one new commitments established; zero or one supersedes.
- Proposed scope changes are contained — refine the next wave, don't reshape waves 3+.
- Discoveries refine future waves but don't redirect them.

Action: standard sequence. Close out, refine registers, absorb findings, expand the next sketch, light re-sketching of remaining.

### substantial-redraft

Signals:

- Audit verdict is `pass-with-findings` with multiple findings, possibly of medium severity.
- Multiple assumptions broken with cascading implications.
- One or more commitments superseded.
- Execution report proposes non-trivial scope changes across multiple future waves.
- One or more future-wave goals need rewording based on learnings (not just the sketch detail).
- Possibly the wave *order* needs revisiting.

Action: standard sequence, but the re-sketching step is substantive — future-wave sketches are revised, not just touched up. The change-log entry is longer and explicit about what the user should notice.

### pivot

Signals:

- Audit verdict is `fail` **and** the user agrees the failure isn't a loop-back-to-execute but a rethink.
- A core assumption in the doc's goal or approach is broken.
- The executed wave demonstrated that the stated goal is wrong, unreachable, or misaligned with what users actually need.
- Architectural commitments from W1 turn out to be wrong in a way that invalidates multiple future waves.

Action: different flow. Stop after the evaluation step and present your pivot interpretation to the user for confirmation **before** editing. A pivot is where you loop in the human — getting a pivot wrong is much more expensive than getting a normal redraft wrong. When you do proceed, set frontmatter `status: pivoted`, retire affected wave IDs (never reuse them), introduce new wave IDs, and write a change-log entry that names the prior IDs being retired and the new ones being introduced.

If you're unsure whether this is a substantial redraft or a pivot, treat it as a pivot — the cost of asking the human is low; the cost of silently redirecting is high.

## Closeout procedure

Turning the current wave into a past wave. Replace the detailed wave section with a closeout summary (per `references/wave-schema.md` section 4 "Past waves"):

1. Set `Status: complete` (or `pivoted` or `deferred` if applicable — judge from the audit verdict and scope-change decisions).
2. Set `Completed: <date>`.
3. Preserve `Theme:` and the wave's name.
4. Write a `Delivered:` paragraph based on the execution report's *What was built*, tempered by what audit verified. Describe capability, not tasks — a reader should see what the system can now do without opening any other file.
5. Record `Assumptions resolved:` — list each assumption that was validated or broken during this wave and what happened (`A2 validated`, `A4 broken → A6 opened`).
6. Record `Commitments established:` — list new ACs from this wave.
7. Record `Stories closed:` and `Features delivered:` — the IDs from the current-wave section that reached acceptance.
8. Add `Execution report:` and `Audit report:` paths.
9. Delete the task list, exit criteria, repro path, and other current-wave-only fields. They're captured in the reports and no longer need to live in the doc.

If the audit flagged an exit criterion as not met but the user has decided to close the wave anyway via scope change:

- Note in the closeout's `Delivered:` paragraph that the exit criterion was explicitly renegotiated.
- The change-log entry names the renegotiation as a scope decision.

If a task was NOT completed (the `[~]` notation in the execution report):

- If the task is still relevant and blocks exit criteria: the wave is not actually complete. Either keep W<N> open with the incomplete task or, with user agreement, move the task to the next wave and close this one.
- If the task is no longer relevant (e.g., superseded by a scope change): close the wave and note the task as dropped in the change log.

## Register maintenance

### Assumptions

For each assumption in the register with new status from the reports:

- `untested` / `open` → `validated`: update status with the date. Nothing else.
- `untested` / `open` → `broken`: mark broken, date it, and open a new assumption that replaces it. The new assumption's body states what we now believe, with `Replaces: A<old>` in its metadata. Waves and tasks referring to the old assumption continue to cite the old ID for traceability; *new* references use the new ID.

For each new assumption surfaced by the report's *Discoveries*, add a new entry with status `open` (for a current-state claim) or `untested` (for a claim a future wave will validate).

**Never edit an existing assumption's body** — if it's wrong, open a replacement.

### Risks

For each risk referenced in the reports:

- "R<N> did not materialize" — status `retired (did not materialize)`.
- "R<N> materialized, mitigation worked" — status `triggered — mitigated`.
- "R<N> materialized, mitigation failed" — status `triggered — unresolved`, and either add new mitigation or promote to assumption.

For new risks surfaced in the execution report or audit findings, add entries with the standard shape.

### Architectural commitments

For each commitment the audit verified as respected: no change needed; the audit-trail entry in the change log records that it was verified.

For each new commitment the execution report claims was established:

- Add the entry to Section 7 with a rationale line and `Established: W<N> (<date>). Status: active.`
- If the rationale isn't stated in the reports, either add your best-faith inference with a caveat note in the change log, or ask the user.

For each commitment superseded:

- Mark the old entry `Status: superseded (<date>) by AC<newid>`.
- Open the new entry with its own rationale and `Established: W<N> (<date>). Status: active.`
- Note the supersede explicitly in the change-log entry — commitment supersedes are substantive events the user should see.

## Absorbing audit findings

Each finding in the audit report gets one of these dispositions in the redraft:

- **Absorbed into next wave's plan** — e.g., "F2 (AC3 at risk due to SMTP code) — add a task to W3 to resolve: bundle SSL or supersede AC3 with documented rationale." The change-log entry names the finding and where it was absorbed.
- **Triggers a register change** — e.g., "F1 (A4 validation premature) — reopen A4 as `untested`; reassign to W3 for re-verification." The change-log names the finding and the register change.
- **Resolved via scope change** — e.g., "F3 (unplanned SSO provider) — accepted as scope; add retroactive task note to W2 closeout, and add SSO polish story to W4 sketch." The change-log documents the scope decision.
- **Explicitly deferred** — e.g., "F4 (cosmetic CLI help formatting) — low severity, deferred with note in themes-not-yet-waved." The change-log records the deferral.

No finding is silently ignored. If a finding is deferred, the deferral is visible. If it's absorbed, it's named.

## Expanding the next wave

The next wave's sketch in the doc needs to become a fully-detailed current-wave section with stories, features, tasks, acceptance criteria, exit criteria, and a repro path. Specifically:

1. Start from the existing sketch. Preserve the goal, theme, and candidate story titles unless learnings require changes.
2. Expand each candidate story into a full story with acceptance. Split any story that turns out to be two stories.
3. Expand anticipated features into full feature entries with descriptions and story references.
4. Refine the **entry criteria** — these may change based on what the just-closed wave actually produced.
5. Tighten the **exit criteria** — often the sketch was vague; now with the current state known, make them testable.
6. Write the **repro path** explicitly — a script or command the next auditor will run.
7. Break the work into **tasks with acceptance criteria**. Same rules as `wave-draft`: every task has acceptance, tasks are sized for an agent session, the uncertainty-reducing task comes first, a repro-path task is included.
8. List **commitments respected** and **anticipated new commitments** for this wave.
9. List **assumptions** and **risks** this wave depends on — many will be in the register already; add any new ones.
10. Set `Started: <date>` and `Status: in_progress`.

**Do not pre-plan waves beyond the newly-expanded one.** Exactly one wave is expanded per redraft. The invariant is absolute.

## Re-sketching remaining waves

For each wave beyond the newly-expanded one, re-read its sketch with the learnings in mind. Ask:

- Is the goal still sensible given what we now know?
- Does the entry-criterion sketch still make sense?
- Are new or revised assumptions relevant?
- Do scope changes affect what's in or out?
- Does a newly-superseded commitment change the approach?

If yes to any, revise the sketch. If no, leave it alone — don't polish sketches that don't need polishing; you'll waste tokens and risk introducing drift.

**The invariant holds**: future-wave sketches never get task detail, story acceptance, or feature definitions. The re-sketching edit is at the sketch level — goal, theme, entry/exit-criterion sketches, candidate story titles, anticipated features, assumptions/risks/commitments references, 2–4 sentence approach sketch.

## Themes not yet waved (Section 9)

- If the execution report or audit surfaced a new theme that's in-vision-but-not-yet-waved, add a bullet.
- If a theme has now been pulled into a wave (either the newly-expanded one or a newly-created wave in a pivot), remove its bullet — note in the change log.
- If the user explicitly deferred something via scope change, add it here with a one-line rationale.

## Frontmatter and change log updates

### Frontmatter

- `wave_doc_version`: increment by 1.
- `last_updated`: today's date, ISO format.
- `current_wave`: advance to the next wave's ID (or set a new ID if a pivot introduced a new wave).
- `status`: usually stays `in_progress`. Set to `pivoted` if the redraft is a pivot. Set to `complete` if there are no more waves.

### Change log entry

Append a new entry at the *top* of Section 8. Format per `references/wave-schema.md` section 8. Be specific:

- Which wave was closed, and whether all exit criteria were fully met (cross-reference the audit verdict).
- Which assumptions changed status; which new ones opened.
- Which risks changed status; which new ones opened.
- Which commitments established, superseded, or retired.
- Which audit findings were absorbed into the next wave, triggered register changes, resulted in scope changes, or were explicitly deferred.
- What scope changes were absorbed (adds, removes, defers).
- Which wave was expanded to current; what was materially different about the expansion compared to the previous sketch.
- Which remaining waves were re-sketched (by ID) and why.

A good change-log entry should be readable in isolation — a user returning six months later should understand this redraft from this entry alone.

## Invariants — things to never do

From the schema, restated because these are the most common failure modes for this skill:

1. **Never expand more than one wave per redraft.** Only the new current wave.
2. **Never delete assumptions, risks, or commitments.** Broken/superseded ones are marked and replaced; they stay in the register.
3. **Never rewrite change-log entries.** Only append new ones.
4. **Never silently add or remove scope.** Every add/remove/defer gets an explicit change-log bullet.
5. **Never close out a wave whose exit criteria aren't met** unless the criteria themselves are explicitly renegotiated (which is a scope decision, logged).
6. **Never reuse retired wave IDs.** After a pivot, W3 stays retired; introduce W5, W6, etc.
7. **Never override the audit verdict silently.** If you disagree with the audit, say so in the change log; don't pretend the audit said something it didn't.
8. **Never edit an assumption's or commitment's body.** If wrong, open a replacement with a new ID.

## What to do if reports are malformed

If either report doesn't conform to the schema's template (sections missing, no task status, no verdict, etc.), stop. Don't try to guess. Ask the user either to re-run the skill that produced it or to patch the report.

If the execution report and audit report disagree in ways you can't reconcile (e.g., one says a task passed and the other says it failed, without sufficient context), stop and surface the disagreement to the user.

If the audit wasn't run at all — only the execution report is available — stop and tell the user to run `wave-audit` first. Redraft without audit is possible in theory but undermines the whole DEAR discipline; don't accept the shortcut without the user explicitly asking for it and acknowledging the tradeoff.

## Worked mini-example

Given:

- A wave doc with `current_wave: W2` and 4 tasks in W2, all `[x]`.
- Execution report: all tasks done, A2 broken, proposes adding a ranked-voting data migration to W3.
- Audit report: verdict `pass-with-findings`. F1: A4 validation premature (benchmark above threshold but report claimed it validated). F2: new commitment AC4 established (ranked-vote data model) but lacks a rationale in the report.

The redrafter's sequence:

1. **Evaluate.** Verdict pass-with-findings; tasks done; one assumption broken with a clear replacement; one commitment added needing a rationale; a scope change proposed for W3. Classification: **normal-redraft**.
2. **Close out W2.** Status → complete. Delivered paragraph drawn from the execution report's *What was built*, tempered by F1 (note: voting UI works end-to-end, A4 query-latency claim deferred to W3 for re-validation). Assumptions resolved: `A2 broken → A6 opened`. Commitments established: AC4 (with rationale added from user dialog or best-faith inference plus a change-log caveat). Stories closed, features delivered listed.
3. **Update registers.** `A2` marked broken with date. `A6` opened: "Voting is ranked-choice (single-transferable-vote tie-break)." `Replaces: A2`. `A4` reopened as `untested`, reassigned to W3. `AC4` opened in the commitments register. No new risks beyond R3 (ranked-choice ties) from the execution report.
4. **Absorb audit findings.** F1 triggers the A4 reopen (register change). F2 resolved by adding a rationale to AC4 (possibly after asking the user).
5. **Expand W3.** Read the existing sketch. Pull in the proposed migration task. Write stories with acceptance; write features; write tasks with acceptance; write exit criteria and repro path; include an A4 re-validation task. Set started date. Status → in_progress.
6. **Re-sketch W4.** W4 used to assume a certain data shape for scheduling UI; now it must inherit the ranked-voting list shape. Revise two sentences of the sketch; no task detail.
7. **Section 9.** No changes; nothing new surfaced, nothing pulled into waves.
8. **Frontmatter.** `wave_doc_version: 2 → 3`. `current_wave: W2 → W3`. `last_updated: <today>`.
9. **Change log.** New entry at the top of Section 8, type `normal-redraft`, naming W2 closeout, A2/A6 swap, A4 reopen triggered by F1, AC4 established, F2 addressed by rationale addition, W3 expansion with ranked-voting migration included, W4 re-sketch noting the data-shape inheritance.

Now write the file. Done.

## Handoff

After the redraft, the doc is ready for the next DEAR cycle. Tell the user: what wave is now current, any significant changes they should know about (broken assumptions, superseded commitments, new scope), the path to the updated doc. They'll invoke `wave-execute` when ready to start the new wave.
