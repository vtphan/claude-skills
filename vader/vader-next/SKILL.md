---
name: vader-next
description: Use this skill when you want a quick orientation to a VADER project's current state and a recommendation for the next step. Triggers include phrases like "what's next on this VADER project", "where am I in this VADER cycle", "what should I do next", "give me a status check", "I'm coming back to this project — what's the state", or whenever the user has a VADER project (vision-doc, architecture-doc, wave-doc all present) and wants the tool to identify the next skill to invoke before committing to it. Also trigger when the user opens an existing VADER project after a break and asks "where were we." Do NOT use to actually execute any VADER skill — vader-next dispatches the next skill only on explicit user confirmation. Do NOT use to modify any artifact; this is a read-only orientation skill plus dispatch.
---

# vader-next

Read a VADER project's current state, identify the next step in the cycle, present a concise summary, and (on the user's go-ahead) dispatch the next skill. This is the orientation-and-handoff helper that removes the cognitive load of "which skill comes next, and why" without removing the human's decision-making role.

Before doing anything else, read `references/vision-schema.md`, `references/architecture-schema.md`, `references/wave-schema.md`, and `references/git-conventions.md`. The schemas tell you what to read out of each artifact; the git conventions tell you what tags and refs to expect.

## What this skill does

Three things, in order:

1. **Read project state** from existing artifacts (no new state file is created or maintained — the skill is a pure consumer).
2. **Compute the next step** per VADER's gating rules.
3. **Present a tight summary** (3-5 lines) and ask for confirmation before dispatching the next skill as a fresh subagent.

The skill is read-only on artifacts. It never edits the vision doc, architecture doc, ADRs, wave doc, or any report. The only side effect is dispatching the next skill (which the user explicitly approves) and writing transient summaries to the conversation.

## Inputs and output

**Inputs (all read-only):**
- The vision doc (`<project-slug>-vision.md`) — frontmatter for `vision_version` and `status`.
- The architecture doc (`<project-slug>-architecture.md`) — frontmatter for `architecture_version` and `status`.
- The ADR log (`<project-slug>-adr/`) — file listing and each ADR's `Status` field.
- The wave doc (`<project-slug>-wave-doc.md`) — frontmatter for `wave_doc_version`, `current_wave`, and `status`; the latest change-log entry; the current-wave section.
- The reports directory (`<project-slug>-wave-doc.reports/`) — file listing for execution, audit, and architect-review reports of the current wave.
- (When git is in use) the most recent commits and tags for orientation.

**Output:** a 3-5 line summary delivered conversationally, plus (on confirmation) the dispatch of one VADER skill as a fresh subagent. No files are written, no artifacts modified.

## Workflow

### 1. Read state in deterministic order

Read in this order so the skill builds a complete picture before deciding:

1. Vision doc frontmatter — `vision_version`, `status`.
2. Architecture doc frontmatter — `architecture_version`, `status`.
3. ADR log — list files, read each `Status`. Note any with `Status: Proposed`.
4. Wave doc frontmatter — `wave_doc_version`, `current_wave`, `status`. Note any registers.
5. Wave doc Section 8 (Change log) — read the most recent entry's `Type:` field.
6. Reports directory — list which of `wave-W<N>-execution.md`, `wave-W<N>-audit.md`, `wave-W<N>-architect-review.md` exist for the current wave.
7. For each existing report, read its YAML frontmatter (verdict, summary, refs).
8. (Optional, if git in use) most recent commits and tags.

If any required artifact is missing, the project is in an early state — that itself is information.

### 2. Determine the project's state class

Map the readings to one of these state classes:

- **No vision yet.** No vision doc exists. → Next: `vision-shaper`.
- **Vision exists; no architecture.** Vision doc present; architecture doc absent. → Next: `architect-draft`.
- **Architecture drafted; ADRs un-ratified.** Architecture doc present; one or more cited ADRs have `Status: Proposed`. → Next: ratify ADRs (re-invoke `architect-draft` in ratify mode, or have user manually flip status fields).
- **Architecture ratified; no wave doc.** Architecture present, all ADRs Accepted, wave doc absent. → Next: `wave-draft`.
- **Wave doc exists; current wave fully planned, no execution report.** Wave doc shows `current_wave: W<N>` with `Status: in_progress`; no `wave-W<N>-execution.md` exists. → Next: `wave-execute`.
- **Execution report exists; no audit report.** → Next: `wave-audit`.
- **Audit report exists with `pass` or `pass-with-findings`; no architect-review report.** → Next: `architect-review`.
- **Audit verdict was `fail`; no architect-review.** → Special: user must decide between looping back to `wave-execute` (after addressing findings) or invoking `wave-redraft` for explicit scope renegotiation. vader-next presents both options; does not auto-choose.
- **Architect-review report exists; current wave still `in_progress` per wave doc.** → Next: `wave-redraft`.
- **Wave-redraft just ran; new current wave is `in_progress` with no execution report.** → Next: `wave-execute` for the new wave. *Pause naturally here* — wave boundaries are real decision points; the user confirms readiness before kicking off the next wave's execution.
- **Vision status is `pivoted` and the wave doc's most recent change-log entry is not `vision-pivot-redraft`.** → Next: `wave-redraft` (in vision-pivot-redraft mode).
- **All waves complete (wave-doc status is `complete`).** → No next step; the project is done.

If the readings don't map cleanly to any state class — e.g., vision is `pivoted` and a `vision-pivot-redraft` already happened but the wave-doc status is still `pivoted` and another execute hasn't happened — that's an *ambiguous state*. Fail loud (see [Ambiguity handling](#ambiguity-handling)).

### 3. Compose the summary

The summary is exactly four lines, in this order:

```
State: <where you are> — <one-line context>
Next: <skill name> (<one-line why>)
Recent: <one notable item from registers, ADRs, or change log; or "—" if nothing>
Confirm? (yes / show more / skip)
```

Examples:

```
State: W2 in_progress; audit complete (pass-with-findings).
Next: architect-review (audit flagged ADR-004 violation; needs structural decision).
Recent: 2 proposed ADRs in audit findings; 1 assumption broken (A2 → A6).
Confirm? (yes / show more / skip)
```

```
State: vision pivoted to v2; downstream reconciliation pending.
Next: wave-redraft (vision-pivot-redraft to reconcile wave doc).
Recent: 3 wave goals affected; 1 ADR may need supersession.
Confirm? (yes / show more / skip)
```

Keep each line under ~80 characters. The summary should be skimmable in 5 seconds.

### 4. Handle the user's response

- **"yes" (or equivalent: "go", "proceed"):** Dispatch the next skill as a fresh subagent (Task tool, isolated context). Read only the resulting artifact (report or doc); do not embed the subagent's reasoning. Inform the user when the dispatched skill is done and where its output lives.
- **"show more":** Expand the summary with more context — read the relevant report's body, the latest change-log entry, the proposed ADRs' bodies, etc. Keep the expansion focused on what's relevant to the next decision; don't dump everything. After the expansion, re-prompt with the four-line summary and confirm question.
- **"skip" (or "no"):** Do nothing. The user knows better. Acknowledge and exit.
- **Any other response:** Treat as conversational; respond naturally, but do not dispatch.

### 5. Dispatch as a fresh subagent

Critical for VADER's audit independence: when dispatching `wave-audit` (or any skill where independence matters), use the Task tool with a fresh subagent and isolated context. Do *not* pass your conversation history into the subagent — the subagent should read only the committed artifacts. The subagent writes its output to a file; you read that file when it's done. You report the result to the user; you do not interpret it.

For non-independence-critical skills (e.g., `wave-execute`, `wave-redraft`), dispatching as a subagent is still preferred for separation of concerns, but it's not strictly required for correctness.

### 6. Stop at wave boundaries

After `wave-redraft` closes a wave and advances `current_wave`, vader-next does *not* auto-suggest running `wave-execute` on the next wave. The boundary between waves is a real decision point — "am I ready for another cycle? do I have time? has anything else come up?" — and shouldn't be papered over with momentum.

The user invokes vader-next again when they're ready for the next wave; at that point the state is "wave-doc shows new current_wave in_progress, no execution report yet" and vader-next will recommend `wave-execute`.

## Ambiguity handling

vader-next *fails loud* when the artifacts don't map cleanly to a state class. This is a feature: schema drift, stale state, or unexpected hand-edits surface here rather than producing a confidently-wrong "next" recommendation.

Examples of ambiguities and how to surface them:

- **Vision is `pivoted` but no vision-pivot-redraft change-log entry exists, AND the most recent change-log entry isn't recent enough to predate the pivot.** Output: "Vision is `pivoted` (v3, last_updated 2026-08-12) but the wave doc's latest change-log entry is `normal-redraft` from 2026-07-20 (older than the pivot). I'm not sure where you are. Confirm: just pivoted and need wave-redraft? Or did wave-redraft already run but didn't update vision status?"
- **Audit report exists but verdict frontmatter field is missing.** Output: "Audit report at <path> doesn't have a parseable `verdict` frontmatter field — please check that it conforms to schema Section 10. I can't tell if architect-review is unblocked."
- **Multiple ADRs have `Status: Proposed` but the wave doc's current wave is past W1.** Output: "ADRs ADR-NNN, ADR-NNN are still Proposed, but the wave doc is on W3. These should have been ratified by `wave-redraft` long ago. Manual reconciliation needed."
- **`current_wave` in wave doc points to a wave whose section is missing from Section 4.** Output: "Wave doc says current_wave is W4 but the W4 section in Section 4 doesn't exist. The wave doc may be malformed."
- **Reports exist for the wrong wave (e.g., wave-W1-execution.md but current_wave is W3).** Output: "Stale or out-of-place reports found: <list>. Possibly leftover from a pivot or hand-cleanup. Manual reconciliation may be needed."

In every ambiguous case, vader-next presents the evidence and lets the user decide. It does *not* guess.

## Principles to keep in mind

**Read-only on artifacts.** vader-next never writes to the vision, architecture, ADRs, wave doc, or any report. Its only writes are conversational summaries and (on confirmation) skill dispatches.

**Fail loud on ambiguity.** A confidently-wrong next-step recommendation is worse than admitting uncertainty. If the state is unclear, say so.

**Independence is preserved through subagent dispatch.** When dispatching `wave-audit` (and ideally all dispatched skills), use a fresh subagent with isolated context. The subagent reads committed artifacts, not your conversation history.

**Stop at wave boundaries.** After `wave-redraft`, the next wave's `wave-execute` is a deliberate human decision. Don't auto-suggest it; let the user invoke vader-next again when they're ready.

**The summary is four lines.** State, Next, Recent, Confirm. More than that and the cognitive load is back. If the state is too complex for four lines, the project may genuinely need a longer conversation; offer "show more" rather than expanding inline.

**Treat schema as the contract for state detection.** Frontmatter fields and well-defined section headings are stable signals. Prose extraction at fixed locations (e.g., audit report's `## Verdict` heading) is acceptable; prose extraction at variable locations is not. If a field you need is missing or ambiguous, surface that explicitly.

## Anti-patterns to avoid

**Auto-advancing through multiple steps.** vader-next is a one-step-at-a-time tool. Don't chain dispatches. Each invocation produces one summary and at most one dispatch.

**Embedding subagent reasoning into your context.** When dispatching, the subagent's only durable output is the artifact it writes (report file, ADR file, etc.). Read that artifact; don't reason from the subagent's response text.

**Guessing on ambiguity.** Better to say "I can't tell — here's what I see" than to recommend the wrong next step.

**Bloated summaries.** Four lines means four lines. Resist the urge to add detail; the "show more" path is for when detail is wanted.

**Modifying artifacts.** Even small edits ("just bumping the timestamp") are out of scope. If a fix is needed, surface it and let the user (or the appropriate skill) make the edit.

**Re-running successful steps "for safety."** If `wave-audit` already produced a `pass` verdict, don't suggest re-running it. Trust the artifact.

## Things to never do

1. **Never modify any VADER artifact.** Read-only.
2. **Never auto-advance past a wave boundary.** After redraft, the user re-invokes vader-next when ready.
3. **Never dispatch a skill without explicit user confirmation.** "Yes" or equivalent must come from the user.
4. **Never dispatch with shared context.** Fresh subagent, isolated state.
5. **Never guess on ambiguous state.** Surface the ambiguity; let the user resolve.
6. **Never produce a summary longer than four lines.** Use the "show more" path for detail.

## Worked mini-example

Project: `bookclub`, mid-cycle, with W2 just executed.

vader-next reads:
- `bookclub-vision.md` frontmatter: `vision_version: 1`, `status: active`.
- `bookclub-architecture.md` frontmatter: `architecture_version: 1`, `status: active`.
- ADR log: ADR-001 through ADR-005 all `Status: Accepted`.
- `bookclub-wave-doc.md` frontmatter: `wave_doc_version: 2`, `current_wave: W2`, `status: in_progress`.
- Wave doc latest change-log entry: `2026-05-26 — Redraft after W1 closeout. Type: normal-redraft.`
- Reports directory contains: `wave-W2-execution.md` (frontmatter has `wave_end_ref: a3f2c1e`), but no `wave-W2-audit.md`.

State class: "Execution report exists; no audit report." → Next: `wave-audit`.

Composes summary:

```
State: W2 in_progress; execution complete (4 tasks done, 1 partial).
Next: wave-audit (verify execution against plan and ADR adherence).
Recent: T2.4 partial — tie-break E2E deferred to W3.
Confirm? (yes / show more / skip)
```

User says "yes." vader-next dispatches wave-audit as a fresh subagent. When wave-audit produces `wave-W2-audit.md`, vader-next reads its `verdict` frontmatter field and tells the user: "Audit complete. Verdict: pass-with-findings. Report at <path>. Re-run vader-next to see the next step."

That's a clean cycle through the helper.

## Handoff

vader-next's "handoff" after a dispatch is to inform the user where the new artifact lives and to invite the user to re-invoke vader-next when ready for the next step. It does not chain — one invocation, one summary, at most one dispatch.

**Git.** vader-next does not produce a commit (no artifact is written). After a dispatched skill runs, the dispatched skill's own handoff suggests the appropriate commit message — vader-next just relays that suggestion.
