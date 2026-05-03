---
name: wave-update
description: Use this skill at the end of every wave, after `wave-execute` has produced an execution report. The skill reviews the wave (via a fresh-context subagent), surfaces findings to the human for approval, applies any architectural changes, closes the current wave, and expands the next wave's sketch into full detail. Triggers include phrases like "update the wave plan after W<N>", "close out W<N> and plan W<N+1>", "run the review and update", "what comes next after this wave's execution", or whenever an execution report exists for the current wave and the user is ready to advance the cycle. Also trigger when a vision pivot has just happened and the user wants the wave plan reconciled. Do NOT use when no execution report exists yet (run wave-execute first). Do NOT use to write code. Do NOT use mid-wave; this skill operates at wave boundaries only.
---

# Wave Update

Close the current wave, absorb its learnings, and expand the next wave's sketch into full detail. This is the per-cycle hub of VADER. It runs an internal review subagent (fresh context, reads only artifacts) to produce findings, presents them interactively to the human for approval, applies any architectural changes, and saves everything atomically.

There is no separate review report — findings live in the change-log entry of the wave plan. The execution report is the only artifact carried over from the wave; the review's verdict, findings, and absorbed decisions all flow into the wave plan's change log.

This is the most consequential skill in the cycle. Other skills create or build; this one *interprets*. Every update is an opportunity to absorb signal or to dilute it.

Before doing anything else, read `references/wave-schema.md` and `references/architecture-schema.md` in full.

## Inputs and outputs

**Inputs:**
- The wave plan (`<project-slug>-wave-plan.md`).
- The execution report (`<project-slug>-wave-plan.reports/wave-W<N>-execution.md`) where W<N> matches `current_wave`.
- The architecture doc and Decision Log.
- The vision doc (read for goal/non-goals consistency; modified only via `vision pivot`, not this skill).
- The repo and (when git is in use) the wave's diff via the execution report's `wave_start_ref` / `wave_end_ref` frontmatter.

**Outputs:**
- The wave plan, updated in place. Frontmatter bumped (`wave_plan_version`, `current_wave`, `last_updated`); change log appended; current wave closed; next wave expanded.
- The architecture doc, updated where mid-cycle changes were proposed and approved. New Decision Log entries added (status `Accepted` after human approval), superseded entries' `Status` lines updated.
- No separate review report.

## The two-stage workflow

`wave-update` operates in two interactive stages with an explicit human checkpoint between them.

**Stage 1 — Review (subagent).** Spawn a fresh subagent with isolated context. Pass it: the wave plan, the execution report, the architecture doc, the cited Decision Log entries, the wave's diff (from `wave_start_ref`..`wave_end_ref`). The subagent's only output is a structured findings document — it does not edit anything. The subagent's mindset is: "the execution report is one input, not the truth; the artifacts are the source of truth."

**Stage 2 — Update (interactive with human).** You read the subagent's findings, present them to the human in a tight summary, accept feedback/edits, and apply the absorbed changes to the wave plan and architecture doc. The human approves before any save.

## Preflight: working tree state

Before entering Stage 1, if git is in use, run `git status --porcelain`. If the working tree has uncommitted modifications to `<project-slug>-wave-plan.md`, the architecture doc, the vision doc, or any execution report, stop and surface the state to the user. `wave-update` will write to the wave plan (and possibly the architecture doc and vision frontmatter) atomically; mixing those writes with pre-existing manual edits to the same files corrupts the precondition contract (§I).

Three resolutions, in order of preference:
1. Commit the manual edits first under their own commit prefix (e.g., `wave: manual edit to W3 sketch before review`), then re-invoke `wave-update`.
2. Stash with `git stash --include-untracked`, run `wave-update`, then `git stash pop` and reconcile the diff manually.
3. Discard the manual edits if they were exploratory.

Uncommitted changes to *other* files (project code, scripts, etc.) are not blocking — they affect the diff but not the artifacts `wave-update` writes. Note them in the handoff so the human knows the wave's diff baseline isn't perfectly clean.

If git is not in use, this preflight is skipped; the human is responsible for not running `wave-update` while editing the wave plan or architecture doc by hand.

## Stage 1: Review (via fresh subagent)

Spawn a subagent (Task tool, isolated context). If the current agent environment lacks subagent spawning, the human runs a fresh agent session manually with the same briefing inputs, returns the findings document, and resumes — independence comes from the fresh context, not the spawn mechanism.

Brief the subagent (or the fresh manual session) with:

- The wave plan path.
- The execution report path.
- The architecture doc path.
- The architecture schema (`references/architecture-schema.md`) and wave schema (`references/wave-schema.md`) — required reading so any proposed ADR bodies and finding entries match format.
- The wave's diff baseline and head (from execution report frontmatter, or fallback tags).
- The wave's `Expected touched modules` declaration (from the current wave's section in the wave plan), for the scope-drift check.
- If CI is configured for the project (e.g., GitHub Actions, GitLab CI), the CI status for the wave's commit. Treat CI as supplemental evidence, not a replacement for the local repro: if CI fails on something the local repro passed, that's itself a finding worth surfacing. If CI is not configured, note in the verdict that the review is local-only.
- Instructions to produce a findings document covering the categories below.

The subagent's findings document (in-conversation, not saved as a file):

1. **Audit verdict:** `pass` / `pass-with-findings` / `fail`. One paragraph justifying. Note explicitly whether CI was consulted.
2. **Exit criteria verification:** for each criterion, pass / fail / unverifiable, with evidence (e.g., "ran `scripts/demo-w2.sh`, all three checks printed PASS").
3. **Verification matrix verification:** confirm the executor's Verification matrix (execution report §Verification) — spot-check that pass-marked checks actually pass on the diff baseline. Flag rows that should not have been marked `n/a`.
4. **Task verification:** cross-reference the executor's claimed task status against the wave plan's checkboxes and the diff. Flag discrepancies.
5. **Assumption verification:** for each assumption the report claims to have resolved, check the evidence.
6. **ADR adherence (architectural):** for each cited ADR, independently confirm adherence. Flag violations. *Propose new ADRs or supersessions if the diff or discoveries imply structural change.* Each proposed ADR includes a full body (Context, Decision, Consequences with at least one negative, Supersedes if applicable). Each proposed body edit to architecture.md sections is named explicitly.
7. **Scope findings:** changes in the diff that don't map to planned tasks, declared discoveries, or the wave's `Expected touched modules` declaration. Surface any module touched but not declared (drift outward) and any expected module untouched (drift inward — possibly an unmet exit criterion).
8. **Entry-criteria check for next wave:** does the current wave's output satisfy the next wave's sketched entry criteria?
9. **Recommendations:** brief notes on what needs a decision (not prescriptions).

Read the subagent's findings carefully. Do not blindly trust them — but their independence is the value. Where the subagent and the executor disagree on facts (did the test pass?), the subagent wins. Where they disagree on intent (what the executor was trying to do), the executor's report wins.

## Stage 2: Update (interactive with human)

### A. Present the findings

Show the human a tight summary of the subagent's findings:

```
Audit verdict: pass-with-findings
- Exit criteria: 2/3 met (criterion 3 admitted partial: 7s vs 5s p95).
- Task verification: T2.4 marked [x] but admits partial coverage.
- ADR-004 violated by T2.3 (recommend supersede with proposed ADR-007).
- One scope finding: tests/perf/ added without a declared task.
- Discoveries: A2 broken (recommend A6); proposed ADR-007 (if approved, write the full accepted entry to architecture.md Section 8).
- Next-wave entry criteria: satisfied.

Proposed absorption:
- Close W2 with T2.4 partial (carry to W3 scope).
- Open A6, mark A2 broken.
- Add ADR-007 (Accepted), supersede ADR-004.
- Edit architecture.md Section 3 (Data and state) per ADR-007.
- Note tests/perf/ as accepted plumbing in change log.
- Expand W3 from sketch.

Approve? Or push back on specific items first.
```

The human can:
- Approve all → proceed to step B.
- Push back on specific findings ("the perf finding is wrong, those tests were intended") → revise the absorption plan; re-present.
- Disagree with a proposed ADR ("I don't want ADR-007 yet; let's keep ADR-004 with a flag and revisit in W3") → adjust accordingly.
- Override audit verdict ("fail to pass-with-findings, T2.4's partial coverage is acceptable") → record the override explicitly in the change log.

### B. Handle the verdict gate

- `pass` or `pass-with-findings` → proceed to wave closeout (step C). Change-log Type is `normal-update`, `substantial-update`, or `vision-pivot-update`.
- `fail` → do not close the wave. Skip steps C, D's wave-plan-side updates, F (next-wave expansion), and G. Steps D-architecture-side and E (registers) may still apply if the failing wave produced architectural learnings or assumption breakages worth recording — apply only the ones the human explicitly approves. Step H writes a `blocked-update` change-log entry with the failing findings (with evidence) and the human's chosen recovery path. Frontmatter behavior on `blocked-update`: `wave_plan_version` += 1, `current_wave` unchanged, `last_updated` = today, `status` stays `in_progress` unless the human chooses `paused`.

Recovery paths under `fail` (the human picks one; record explicitly in the change-log Decisions Absorbed list):
- **Loop back to `wave-execute`.** The current wave's tasks remain open; the executor re-attempts. The change-log bullet names which task(s) need re-execution and what acceptance was missed.
- **Renegotiate the current wave's exit criteria.** Allowed only under `fail` and only with an explicit change-log bullet stating the old criterion text, the new criterion text, and the rationale. This is the only place the current wave's structural content can change without the wave being closed.
- **Pause the project.** Frontmatter `status` set to `paused`. The change-log bullet states what condition would unblock resumption.

Save the wave plan with the `blocked-update` entry; hand off without expanding any future wave.

### C. Close the current wave

Replace the current wave's detailed section with a closeout summary per schema Section 4 (Past waves):

1. `Status: complete` (or `pivoted` / `deferred` if applicable). `Completed: <today>`.
2. Preserve `Theme:`.
3. Write `Delivered:` paragraph from the execution report's *What was built*. Describe capability, not tasks.
4. Record `Assumptions resolved:` — list each assumption that changed status.
5. Record `ADRs established:` and `ADRs superseded:`.
6. List `Stories closed:` and `Features delivered:` — IDs only.
7. Add `Execution report: <path>`.
8. Delete the story list, feature list, task list, exit criteria, and other current-wave-only fields.

If a task was incomplete (`[~]` in the execution report):
- If still relevant and blocks exit criteria: the wave is not actually complete. Either keep open with the incomplete task, or — if the human agrees — move the task to the next wave and close. Default to asking.
- If no longer relevant: close and note as dropped in the change log.

### D. Apply architectural changes (if any)

For each new ADR the human approved:
1. Add the entry to the architecture doc's Decision Log section. Status: `Accepted (today). Established by W<N> wave-update.` (or, if the project has graduated to separate ADR files, create the file.)
2. Update the wave plan's Decision Log References table (Section 7).

For each supersession the human approved:
1. The new ADR's `Supersedes:` field names the old one.
2. Update the *old* ADR's `Status` line to `Superseded (today) by ADR-N.` This is the only edit allowed to an existing Accepted entry.
3. Update the wave plan's Decision Log References table.

For each architecture-doc body edit the human approved:
1. Apply the edit to the architecture doc.
2. If the edit is material (modules, boundaries, interfaces, data, dependencies, deployment, guardrails, or a Decision Log change), bump `architecture_version` and `last_updated`. For non-material edits, bump only `last_updated`.

### E. Update registers

**Assumptions:**
- `untested` → `validated`: update with date.
- `untested` → `broken`: mark broken, dated. Open a replacement with new ID. New entry says what we now believe; `Replaces: A<old>`.
- `open` → `validated` / `broken`: same rules.

**Risks:** update status per execution report findings.

**Themes not yet waved:** any theme that becomes a wave is removed; any new theme proposed is added.

### F. Expand the next wave

Take the next wave's sketch and expand to full detail per schema Section 4 (Current Wave):
1. Refine **entry criteria** based on what the just-closed wave produced.
2. Tighten **exit criteria** — often the sketch was vague; now you can make them testable.
3. Compute **Expected touched modules**: union of modules the wave's tasks will `Touches:`, plus any cross-cutting plumbing the wave will modify. Module-level granularity, drawn from architecture Section 2.
4. Expand **stories** with full acceptance criteria.
5. Expand **features** with descriptions.
6. Break the work into **tasks** with acceptance criteria. Same rules as `wave-plan`.
7. Define the **repro path**.
8. List **assumptions, risks, ADRs respected, new ADRs anticipated**.
9. Set `Started: <today>` and `Status: in_progress`.

**One expansion per update.** Never pre-plan W<N+2>.

### G. Re-sketch remaining waves

For each wave beyond the newly-expanded one, re-read its sketch with the learnings in mind. Revise where required (goal still sensible? entry criterion still makes sense? new ADRs relevant? scope changes affect what's in or out?). Don't polish sketches that don't need it.

### H. Update frontmatter and write the change-log entry

**Frontmatter:**
- `wave_plan_version` += 1.
- `last_updated` = today.
- `current_wave` = next wave ID **on a non-blocked update**. Unchanged on a `blocked-update`.
- `status` = usually `in_progress`. Set to `pivoted` for vision-pivot-update; `complete` if no more waves; `paused` if the human chose pause as the recovery path on a `blocked-update`.

**Change-log entry** at the top of Section 8. Format must include both findings (with evidence and disposition) AND decisions:

```
### YYYY-MM-DD — Update after W<N>
Type: normal-update | substantial-update | vision-pivot-update | blocked-update
Audit verdict: pass | pass-with-findings | fail

Review findings (from subagent):
- F1 (<severity>, <disposition>[, <action>]): <one-line summary>.
  Evidence: 1-3 sentences naming the specific artifact, file, ADR, or test
  that grounds the finding.
- F2 (...): ...

Decisions absorbed:
- Closed W2 with T2.4 partial...
- A2 marked broken; A6 opened (per F1)...
- ADR-007 added, supersedes ADR-004 (per F2)...
- Architecture v3 → v4 (Section 3 edited per ADR-007).
- Expanded W3 from sketch.
- Re-sketched W4.
```

Severity values: `low` | `medium` | `high`. Disposition values: `accepted` | `rejected (user override: <reason>)` | `deferred to W<N+M>`. The optional `action` slot in the parens captures the most consequential downstream effect ("ratified ADR-007", "opened A6", "carried to W3").

The findings list is the durable review record — it preserves what the subagent surfaced (including findings the human rejected), with disposition AND evidence. A reader six months later can reconstruct both what was found and what was done with it from this single entry, *without* opening the (ephemeral) subagent conversation.

Do not refer to the subagent conversation as the only place where evidence or proposed ADR content exists. Any finding important enough to affect the update must be summarized with evidence in the change log. Any ADR important enough to ratify must be written into the architecture Decision Log before save.

For `blocked-update` entries, the Decisions Absorbed list names the recovery path explicitly (loop back / renegotiate / pause) and what triggered each choice. No "Closed W<N>" or "Expanded W<N+1>" bullets appear — those steps were skipped.

### I. Precondition contract

This is a *checked* atomicity, not a filesystem-atomic write. Before any file is written, verify all of these preconditions are true:

- The human has approved each finding's disposition.
- All approved Decision Log additions and supersessions are reflected in *both* the architecture doc (Section 8) AND the wave plan's Decision Log References table (Section 7).
- The wave plan's frontmatter is bumped (version, last_updated, current_wave on a non-blocked update, status).
- The change-log entry is written with both the Findings list (with evidence) and the Decisions Absorbed list, plus audit verdict and Type.
- If the architecture doc was edited materially (Section 2 boundaries, modules, interfaces, data, deps, deployment, guardrails, or a Decision Log change), its frontmatter is bumped too (architecture_version, last_updated). Non-material edits bump only `last_updated`.
- If this is a vision-pivot-update completing a clean reconciliation, the vision doc's frontmatter `status` field is set to `active` (the only edit to the vision allowed by this skill — see Vision-pivot reconciliation below).

If any precondition fails, do not write any file. Report what's wrong to the user and either fix it inline (with their approval) or hand back.

If all preconditions pass, write the files in this order: wave plan → architecture doc (if edited) → vision doc (if status was flipped). Each write is an in-place file replacement; the OS-level write is not transactional across multiple files. In the rare case a write fails or is interrupted between files, the human can recover by re-running `wave-update`: the precondition check will detect the partial state (e.g., wave plan saved with an ADR-007 reference but architecture doc not yet showing ADR-007 as Accepted) and either complete the remaining writes or roll the wave plan back via `git checkout` (if git is in use). The contract guarantees: no file is written until *all* approvals and content are ready; never write the architecture doc before the wave plan has been written.

### J. Commit and hand off

If git is in use, after saving, commit:
1. `git add` *only the artifacts `wave-update` wrote* — the wave plan, the architecture doc (if edited), and the vision doc (if status was flipped). Do not run `git add -A` or `git add .` (those would sweep up any unrelated user-side changes to project code). Pass each path explicitly.
2. Compose the commit message based on Type:
   - `normal-update` / `substantial-update` / `vision-pivot-update`: `git commit -m "wave: update after W<N> — <key changes>" -m "<details>" -m "Co-authored-by: Claude <noreply@anthropic.com>"`.
   - `blocked-update`: `git commit -m "wave: blocked-update after W<N> — <one-line reason>" -m "<details: failing findings, recovery path>" -m "Co-authored-by: Claude <noreply@anthropic.com>"`.
3. Tag based on Type:
   - On a non-blocked update: `git tag wave-plan-v<N>` (matching the new wave_plan_version), `git tag W<N>-complete`, `git tag W<N+1>-start` (the next wave's baseline).
   - On a `blocked-update`: only `git tag wave-plan-v<N>`. Do *not* tag `W<N>-complete` (the wave isn't closed) or `W<N+1>-start` (no next wave was expanded).
   - If a tag name already exists, warn and ask before overwriting.

For a vision-pivot-update on a pivot branch, the commit lands on that branch; the user's call when to merge to main with `--no-ff`.

Tell the user concisely: the verdict and Type, which wave is now current (unchanged on a `blocked-update`), the most significant changes (pivots, supersessions, scope changes, recovery path), the commit sha, and the tags. Override with `git reset --soft HEAD~1` if amending. The next step is theirs — for a non-blocked update, usually `wave-execute` for the new current wave; for a `blocked-update`, either `wave-execute` (re-attempting under the chosen recovery path) or further human action.

## Vision-pivot reconciliation

If the vision doc's frontmatter shows `status: pivoted` and the wave plan's most recent change-log entry is not yet a `vision-pivot-update`, this update is a vision-pivot reconciliation:

1. Set this update's change-log Type to `vision-pivot-update`.
2. Reconcile the wave plan's Goal and Roles sections from the new vision (Sections 1, 2 of the wave plan).
3. Walk the wave ladder. For each wave, ask: is the goal still consistent with the new vision? If not, retire (Status: pivoted or deferred); introduce new wave IDs as needed (never reuse retired numbers).
4. The review subagent's architecture-adherence check should specifically flag ADRs that conflict with the new vision; supersede them as part of this same update.
5. Wave plan frontmatter `status: pivoted` until the next successful execute → update cycle.
6. Don't expand the next wave in this update if the wave being closed isn't the same one whose execution triggered the pivot. The cycle resets: a vision-pivot-update produces a reconciled wave ladder; the next normal cycle expands the next wave.

**Narrow exception: vision frontmatter `status` field.** When this update completes the vision-pivot reconciliation cleanly (all approved findings absorbed, wave plan reconciled, architecture supersessions applied), wave-update flips the vision doc's frontmatter `status` field from `pivoted` back to `active`. This is the *only* edit to the vision doc that wave-update is permitted to make — body sections, Open Questions, and any other vision content remain untouchable except by the `vision pivot` mode. The justification for the narrow exception: the `status: pivoted` field's whole purpose is to track the cross-skill reconciliation cycle, so the skill that completes the reconciliation is the natural owner of the flip. The precondition contract (§I) verifies this flip happened (when applicable) before save.

For vision-pivot-updates whose reconciliation is *partial* (e.g., the user wants to defer some retirement decisions), leave the vision's `status` as `pivoted`; a subsequent wave-update will flip it once the reconciliation is complete.

## Invariants — things to never do

1. **Never expand more than one wave per update.** Only the new current wave.
2. **Never delete assumptions.** Broken ones marked and superseded.
3. **Never edit Accepted Decision Log entries' bodies.** Supersede instead. Update only the `Status` line.
4. **Never rewrite change-log entries.** Append only.
5. **Never silently add or remove scope.** Every change is an explicit change-log bullet.
6. **Never close a wave whose exit criteria aren't met** — unless they're being explicitly renegotiated, in which case it's a scope-renegotiation and called out in the change log.
7. **Never reuse retired wave IDs or superseded ADR IDs.**
8. **Never skip the review subagent.** The fresh-context review is the audit-independence mechanism. If you find yourself thinking "I'll just do the review myself this time," stop — that's the failure mode the subagent prevents.
9. **Never apply changes without explicit human approval.** Findings → present → approve → save. Always.
10. **Never edit the vision doc body.** Only `vision pivot` mode does that. The narrow exception is the vision frontmatter `status` field, which wave-update flips back to `active` when a vision-pivot-update completes a clean reconciliation. If the update requires any other vision change (body, sections, Open Questions), hand back and ask the user to invoke `vision pivot` first.

## What to do if the execution report is malformed

If the report doesn't conform to the schema (sections missing, no task status), stop. Don't guess. Ask the user to have the executor produce a conformant report.

If the report says "task complete" but the wave plan's checkbox is still `[ ]`, cross-check via the diff. If the executor forgot to flip but the work is clearly done, go ahead — note the discrepancy in the change log.

## Worked mini-example

Inputs: wave plan with `current_wave: W2` and 4 tasks all `[x]`. Execution report claims pass; A2 broken; ADR-004 violated; recommends supersession.

Stage 1 — Review subagent:
- Verdict: pass-with-findings.
- Exit criteria: 3/3 met by repro.
- T2.4 partial; otherwise tasks verified.
- ADR-004 violated; proposes ADR-007 (row-per-rank); if approved, write the full accepted entry to architecture.md Section 8. Proposes architecture.md Section 3 edit.
- Discoveries: A2 broken with concrete evidence; recommends A6.
- One scope finding: tests/perf/ added without task; subagent flags as benign-but-undeclared.
- Next-wave entry criteria satisfied.

Stage 2 — Update:
- Present summary; user approves all but pushes back on T2.4 partial ("OK to defer to W3").
- Close W2: status complete, T2.4 carried to W3 scope (noted in change log).
- Add ADR-007 to Decision Log, superseding ADR-004. Update ADR-004's Status.
- Edit architecture.md Section 3 per ADR-007. Bump architecture_version to 2.
- Mark A2 broken, open A6.
- Update Decision Log References table.
- Expand W3 with the new ranked-voting requirements.
- Re-sketch W4 to inherit ranked-voting list shape.
- Frontmatter: wave_plan_version 2 → 3, current_wave W2 → W3.
- Change-log entry: Type normal-update, audit verdict pass-with-findings, all bullets above.
- Save wave plan + architecture together.

That's a clean cycle.

## Handoff

The handoff happens in step J (commit and hand off) of the workflow above. After the commit, tell the user: which wave is now current, the most significant changes, the commit sha, and the tags set (`wave-plan-v<N>`, `W<N>-complete`, `W<N+1>-start`). The next step is `wave-execute` for the new current wave. Do not invoke it.
