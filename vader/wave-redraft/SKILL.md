---
name: wave-redraft
description: Use this skill when an execution report, an audit report, and an architect-review report all exist for the current wave, and the user wants the wave doc advanced — current wave closed out, registers updated, ADR proposals ratified, next wave expanded into full detail. Triggers include phrases like "redraft the wave doc with these reports", "close out the current wave", "advance the wave doc", "expand the next wave", "here are the W<N> reports — redraft", or whenever the trio of reports is available and the user is ready to advance the cycle. Also trigger when the vision has just been pivoted (`status: pivoted` on the vision doc) and the user wants the wave doc reconciled. Do NOT use when reports are missing or incomplete. Do NOT use to write code. Do NOT use when the audit verdict is `fail` and no scope renegotiation has been agreed — closeout is blocked in that case.
---

# Wave Redraft

Reconcile the wave doc with three reports — execution, audit, and architect-review — producing the next version of the wave doc. Ratify proposed ADRs. Apply architecture body edits. Close out the current wave. Expand the next wave's sketch into full detail. Re-sketch remaining waves where learnings require it.

This is the most consequential skill in the VADER cycle. The other six skills create, build, or check; this one *interprets*. Every redraft is an opportunity to absorb signal or to dilute it. The discipline below is what keeps the wave doc honest across cycles instead of drifting into fiction.

Before doing anything else, read `references/wave-schema.md` and `references/architecture-schema.md` in full.

## Inputs and outputs

**Inputs:**
- The current wave doc (`<project-slug>-wave-doc.md`).
- The execution report (`<project-slug>-wave-doc.reports/wave-W<N>-execution.md`).
- The audit report (`<project-slug>-wave-doc.reports/wave-W<N>-audit.md`). Verdict must be `pass` or `pass-with-findings` for normal closeout. A `fail` verdict means scope renegotiation is happening; user must explicitly say so.
- The architect-review report (`<project-slug>-wave-doc.reports/wave-W<N>-architect-review.md`). Required for normal cycles; absent only when audit verdict was `fail`.
- The vision doc (read for goal/non-goals consistency; modified only via `vision-pivot`, not this skill).
- The architecture doc and ADR log (modified by this skill where the architect-review report indicates).

**Outputs:**
- The wave doc, updated in place. `wave_doc_version` incremented; `last_updated` bumped; `current_wave` advanced; change log appended.
- The architecture doc, updated where architect-review proposed body edits. `architecture_version` incremented if any body edit was applied.
- The ADR log: any `Proposed` ADRs from architect-review that are ratified are moved to `Accepted`. Any superseded ADRs have their `Superseded by:` line updated to point to the successor.

## The one-rule core

**Evaluate first, edit second.** Before changing a single line, classify the redraft type (see [Update type detection](#update-type-detection)). Normal redrafts and pivots look extremely different, and doing the wrong kind silently wastes the wave doc's history.

## Operating principles

### 1. Evaluation-first sequencing

The steps are ordered deliberately:

1. **Evaluate** — classify the redraft type and identify what's different about the world now.
2. **Close out the current wave** — turn its detailed section into a closeout summary, gated by exit criteria from the wave doc and the audit verdict.
3. **Ratify ADR changes from architect-review** — move proposed ADRs to Accepted; update superseded ADRs' `Superseded by:` field; apply architecture-doc body edits.
4. **Update registers** — assumptions, risks, ADR-references table, themes.
5. **Expand the next wave** — take the sketch, refine based on learnings, fill out to current-wave detail.
6. **Re-sketch remaining waves** — adjust forward sketches where learnings require it. Preserve intent; revise detail.
7. **Update frontmatter and append change log.**

Doing these out of order produces a wave doc where the next wave relies on outdated beliefs. Order matters.

### 2. Atomic update

Either fully updated or not updated at all. There is no half-updated state. If you can't complete the full sequence — e.g., a report is ambiguous on a critical point — stop and flag for the user.

### 3. Preserve history

The assumptions register is never shrunk. Broken assumptions stay as history; new assumptions get new IDs. Superseded ADRs keep their files; `Superseded by:` is updated retroactively. Past-wave closeout summaries are never deleted, even as the doc ages. The change log is never rewritten.

This matters because when a future cycle encounters a surprise, the path back to understanding *why* the doc looks the way it does runs entirely through the history.

### 4. Be conservative about scope

Every redraft is a chance for the wave doc to accrete features. Resist. New work enters only if:

- The execution or audit report explicitly proposes it, and you agree it's necessary; or
- A broken assumption makes it mandatory; or
- The architect-review proposes it as part of an ADR ratification.

"Might be nice" is not sufficient. When in doubt, defer — and note the deferral as an explicit change-log entry.

### 5. Trust the reports, verify against the doc

The reports are accounts. They're usually accurate. But the redrafter is the one checking claims against the wave doc's exit criteria, ADR cross-references, and assumption status. If a report says "all tasks complete" but `[ ]` checkboxes remain in the wave doc, or an exit criterion doesn't obviously map to a completed task, ask — don't rubber-stamp.

## Update type detection

Before editing, classify the redraft.

### normal-redraft

Signals:
- All current-wave tasks completed; audit verdict `pass` or `pass-with-findings`.
- Exit criteria met (or admitted gaps with clear paths forward).
- At most one or two assumptions broken with clear replacements.
- At most one or two ADR supersessions proposed.
- No major scope changes proposed across multiple future waves.

Action: the standard sequence above.

### substantial-redraft

Signals:
- Multiple assumptions broken with cascading implications.
- Multiple ADR supersessions or new ADRs.
- Scope changes proposed across multiple future waves.
- One or more future-wave goals need rewording (not just sketch detail).

Action: standard sequence, but the re-sketching step is substantive — future-wave sketches are revised, not just touched up. The change-log entry is longer and explicit.

### vision-pivot-redraft

Signals (any of these):
- The vision doc's `status` is `pivoted`.
- The vision's value hypothesis, role set, or in-scope/non-goals have changed.
- The architect-review report flags ADRs that conflict with the new vision.

Action: different flow. The wave doc must be reconciled to the new vision before the next wave can be expanded. Specifically:

1. Goal section and Roles section in the wave doc rewritten from the new vision.
2. Walk the wave ladder. For each wave (current and future):
   - Is the goal still consistent with the new vision? If not, retire (status: `pivoted` or `deferred`) and introduce a new wave with a new ID.
   - Are the assumptions, risks, ADRs cited still valid? If not, mark them broken or recommend supersession.
3. The change-log entry type is `vision-pivot-redraft`. List retired wave IDs and any new ones introduced. Frontmatter `status: pivoted` until the next successful execute/audit/architect-review/redraft cycle.
4. Don't expand the next wave in this redraft if the wave being closed isn't the same one whose execution triggered the pivot. The cycle resets: a vision-pivot-redraft produces a reconciled wave ladder; the next normal cycle expands the next wave.

### scope-renegotiation-redraft

Signals:
- Audit verdict was `fail`.
- The user has explicitly chosen to renegotiate scope (rather than loop back to wave-execute).
- The architect-review report is absent (skipped under fail).

Action: very deliberate. The current wave is *not* closed in the normal sense — it's closed via scope change. The change log records what scope was reduced or moved. The next wave expansion accounts for the renegotiation. This is rare and visible; don't disguise it as normal-redraft.

If you're genuinely unsure whether a redraft is substantial or pivot, treat it as a pivot — the cost of asking the user is low; the cost of silently redirecting the doc is high.

## Closeout procedure

Turning a current wave into a past wave. Replace the detailed wave section with a closeout summary per schema Section 4 (Past waves):

1. Set `Status: complete` (or `pivoted` or `deferred` per the situation). Set `Completed: <date>`.
2. Preserve `Theme:` from the current section.
3. Write a `Delivered:` paragraph based on the execution report's *What was built*. Describe capability, not tasks.
4. Record `Assumptions resolved:` — list each assumption that changed status.
5. Record `ADRs established:` and `ADRs superseded:` based on the architect-review report.
6. List `Stories closed:` and `Features delivered:` — IDs only.
7. Add report links: `Execution report:`, `Audit report:`, `Architect-review report:`.
8. Delete the story list, feature list, task list, exit criteria, and other current-wave-only fields. They're captured in the reports.

If a task was incomplete (`[~]` in the report's task status):
- If still relevant and blocks exit criteria: the wave is not actually complete. Either keep open with the incomplete task, or — if user agrees — move the task to the next wave and close. Default to keeping open and asking.
- If no longer relevant: close and note as dropped in the change log.

## Ratifying architect-review proposals

The architect-review report comes with three kinds of proposal: new ADRs, supersessions, and architecture-doc body edits. Each is ratified atomically as part of redraft.

**New ADRs.** Find the proposed ADR file in the ADR log (status `Proposed`). Change its status to `Accepted (today's date). Established by W<N> redraft.` This is the only edit allowed to a proposed ADR — no body changes. If the proposed ADR's body needs revision, that's an architect-review iteration, not redraft's job.

**Supersessions.** For each supersession, the new ADR's `Supersedes:` field already names the old ADR. Update the *old* ADR's `Superseded by:` field to point to the new ADR. This is the only edit ever allowed to an existing accepted ADR. Update the wave doc's ADR-references table accordingly.

**Architecture-doc body edits.** Apply the edits as specified in the architect-review report. Each edit cites the ADR(s) it depends on. Bump `architecture_version` on the architecture doc and `last_updated`. Note the architecture-version bump in the wave doc's change-log entry.

If the architect-review report is malformed (e.g., proposes an ADR but doesn't include the body, or proposes a body edit without naming the ADR it depends on), stop. Don't guess. Tell the user the report needs another architect-review pass.

## Register maintenance

### Assumptions

For each assumption with new status from the reports:
- `untested` → `validated`: update the status with the date.
- `untested` → `broken`: mark broken, dated. Open a new assumption that replaces it. New entry's body says what we now believe, with `Replaces: A<old>`. Existing references to the old ID stay; new references use the new ID.
- `open` → `validated` or `broken`: same rules.

For each new assumption surfaced by report Discoveries, add an entry with status `open` (current-state claim) or `untested` (claim to validate later).

**Never edit an existing assumption's body.** Open a replacement.

### Risks

For each risk mentioned in reports:
- "R<N> did not materialize" → status `retired (did not materialize)`.
- "R<N> materialized, mitigation worked" → `triggered — mitigated`.
- "R<N> materialized, mitigation failed" → `triggered — unresolved`; either add new mitigation or promote to assumption.

For new risks surfaced, add entries with the standard shape.

### ADR-references table (Section 7 of wave doc)

Update this denormalized table whenever the ADR log changes. New ADRs added; supersessions reflected; "Cited by" columns updated based on what waves reference each ADR.

### Themes not yet waved (Section 9)

Themes that became waves are removed. New themes proposed (from execution report scope changes that suggest future work) are added. A theme is added only if it's clearly in vision-scope; otherwise it goes in the change log as a deferred-to-no-where note.

## Expanding the next wave

The next wave's sketch becomes a fully-detailed section with stories, features, tasks, acceptance criteria. Specifically:

1. Start from the existing sketch. Preserve goal and theme unless learnings require change.
2. Refine **entry criteria** based on what the just-closed wave produced.
3. Tighten **exit criteria** — often the sketch was vague; now you can make them testable.
4. Expand **stories** with full acceptance criteria.
5. Expand **features** with descriptions.
6. Break the work into **tasks** with acceptance criteria. Same rules as `wave-draft`: every task has acceptance, sized for one agent session, ordering puts uncertainty-reducing tasks first.
7. Define the **repro path**.
8. List **assumptions, risks, ADRs respected, new ADRs proposed** as appropriate.
9. Set `Started: <date>` and `Status: in_progress`.

**Do not pre-plan wave N+2 or beyond.** Only the *single* next wave is expanded per redraft. Invariant absolute: one expansion per cycle.

## Re-sketching remaining waves

For each wave beyond the newly-expanded one, re-read its sketch with the learnings in mind:

- Is the goal still sensible?
- Does the entry criterion still make sense?
- Are revised assumptions or new ADRs relevant?
- Do scope changes affect what's in or out?

If yes to any, revise the sketch. If no, leave it alone — don't polish unnecessary sketches; you'll waste tokens and risk introducing drift.

**Future-wave sketches never get task detail.** Re-sketching is at the sketch level only.

## Frontmatter and change log

### Frontmatter

- `wave_doc_version`: increment by 1.
- `last_updated`: today's date.
- `current_wave`: advance to the next wave's ID.
- `status`: usually `in_progress`. Set to `pivoted` if this is a vision-pivot-redraft (and leave as `pivoted` until a subsequent normal cycle clears it). Set to `complete` if no more waves.

### Change log entry

Append a new entry at the *top* of Section 8. Format per schema. Be specific:

- Which wave was closed; whether exit criteria were fully met.
- Which assumptions changed status; which new ones opened.
- Which ADRs were ratified, superseded, or introduced. Architecture version bumped.
- Which risks changed status.
- Scope changes absorbed (adds, removes, defers).
- Which wave was expanded to current; what was materially different about the expansion.
- Which remaining waves were re-sketched and why.

A good entry should be readable in isolation — a user coming back six months later should understand what happened from this entry alone.

## Invariants — things to never do

1. **Never expand more than one wave per redraft.** Only the new current wave.
2. **Never delete assumptions.** Broken ones marked and superseded.
3. **Never edit accepted ADR bodies.** Supersede instead. Update only the `Superseded by:` line.
4. **Never rewrite change-log entries.** Append only.
5. **Never silently add or remove scope.** Every change is an explicit change-log bullet.
6. **Never close a wave whose exit criteria aren't met** — unless they're being explicitly renegotiated, in which case it's a scope-renegotiation-redraft and called out.
7. **Never reuse retired wave IDs or superseded ADR IDs.**
8. **Never trust the reports without reading the wave doc.** The reports are inputs; the wave doc's own exit criteria and invariants are the check.
9. **Never edit the vision doc.** That's `vision-pivot`'s job. If the redraft requires a vision change, hand back to the user and ask them to invoke vision-pivot first.
10. **Never auto-invoke the next skill.** The user is the lead; the next step is theirs.

## What to do if a report is malformed

If a report doesn't conform to its schema (sections missing, no verdict, no task status), stop. Don't guess. Ask the user to have the relevant executor / auditor / architect-reviewer produce a conformant report.

If the audit report says `pass` but exit criteria don't obviously map to verified tasks, cross-check yourself. If the executor forgot to flip a checkbox but the work is clearly done, go ahead — note the discrepancy in the change log.

## Worked mini-example

Given:
- Wave doc with `current_wave: W2` and 4 tasks all `[x]`.
- Execution report claims pass, A2 broken, ADR-004 violated, recommends supersession.
- Audit report `pass-with-findings`: verdict justified by the W2 reports plus repro pass; F1 flags T2.4 partial coverage; F2 flags ADR-004 violation (acknowledged).
- Architect-review report: proposes ADR-007 (row-per-rank) superseding ADR-004; proposes one body edit to architecture doc Section 4; one open architectural question for W3.

Sequence:

1. **Evaluate.** Audit verdict good. One assumption broken (A2 → A6). One ADR superseded (ADR-004 → ADR-007). One body edit. One open question. Classification: **substantial-redraft** (because of the ADR supersession, even though only one — substantial-redraft type captures "more than just a normal close-out"). Could argue normal-redraft; either is defensible. Default to substantial since ADR supersession changes the doc's structural foundation.

2. **Close out W2.** Status complete. Delivered paragraph from "What was built". Assumptions resolved: A2 broken → A6 opened. ADRs established: ADR-007. ADRs superseded: ADR-004 → ADR-007. Stories/features closed. Report links added.

3. **Ratify architect-review proposals.** ADR-007 file moved from `Proposed` to `Accepted (2026-06-15). Established by W2 redraft.` ADR-004's `Superseded by:` set to `ADR-007`. Architecture doc Section 4 edited per architect-review's quoted before/after. Architecture version bumped to v4.

4. **Update registers.** A2 broken (dated). A6 opened: `Replaces: A2`. ADR-references table updated.

5. **Expand W3.** Read sketch. Refine entry criteria (now requires the new row-per-rank schema from ADR-007). Tighten exit criteria. Expand stories (US-USR-3 with full acceptance), features, tasks. Set repro path. ADRs respected: ADR-001, ADR-002, ADR-003, ADR-004(historical), ADR-007. Set Started, Status in_progress.

6. **Re-sketch W4.** Touched briefly because it inherits the ranked-voting list shape now confirmed. Two-sentence sketch revision; no task detail.

7. **Frontmatter.** `wave_doc_version: 2 → 3`. `current_wave: W2 → W3`. `last_updated: 2026-06-15`.

8. **Change log.** New entry at top, type `substantial-redraft`. Bullets naming W2 closeout, A2/A6 swap, ADR-004/ADR-007 supersession, architecture v4 bump, W3 expansion noting the row-per-rank dependency, W4 re-sketch.

That's a clean substantial redraft.

## Handoff

After the wave doc is updated, tell the user concisely: what wave is now current, the most significant changes (any pivots, supersessions, scope changes), and where the updated wave doc lives. The next step is theirs — usually `wave-execute` for the new current wave. Do not invoke it.

**Git.** If the project uses git, suggest the user commit with `wave: redraft after W<N> — <key changes>` and tag both `wave-doc-v<N>` (matching the new frontmatter version) and `W<N>-complete` on the redraft commit. For a vision-pivot-redraft, the same commit is also the merge of the pivot branch (if one was used); name it accordingly. Add a `Co-authored-by: Claude <noreply@anthropic.com>` trailer. See `references/git-conventions.md`.
