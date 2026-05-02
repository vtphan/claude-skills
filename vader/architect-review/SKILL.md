---
name: architect-review
description: Use this skill at the architecture-review checkpoint of a VADER cycle — after wave-execute and wave-audit have produced their reports, and before wave-redraft is invoked. Triggers include phrases like "run the architect review for W<N>", "do the architecture review pass on this wave's reports", "check whether any ADRs need supersession given what we just learned", "review the architecture against the W<N> execution and audit", or whenever both an execution report and an audit report exist for the current wave and the user is ready to advance the cycle. Also trigger when the user explicitly says "let's check the architecture before redrafting." Do NOT use for the initial architecture draft (that's architect-draft). Do NOT use to write code or modify implementations. Do NOT use when the audit verdict is `fail` — architect-review is gated by audit pass.
---

# Architect Review

Read the wave's execution and audit reports, evaluate whether the architecture and ADR log need revision, and produce an architect-review report. This is the second verification gate in the VADER cycle. Where `wave-audit` checks whether the wave's *outcome* claims hold up, `architect-review` checks whether the architecture's *adherence* claims hold up — and proposes ADRs or supersessions when they don't.

Before doing anything else, read `references/architecture-schema.md` in full. The schema defines the architecture doc shape, the ADR template, supersession rules, and the architect-review report format (Section 6).

## What this skill does

After a wave is executed and audited, this skill is the deliberate moment in the cycle where the architecture itself is reconsidered. The skill does three things:

1. **Verify ADR adherence.** Cross-reference the audit report's ADR-adherence section with the actual diff. Resolve any disagreement between the execution report's self-claim and the audit's independent verdict.
2. **Identify needed changes.** Decide whether new ADRs need to be drafted, existing ADRs superseded, or the architecture body edited to reflect supersessions.
3. **Produce the architect-review report.** A single document that the redrafter consumes. It contains adherence checks, proposed ADRs (full bodies inline), proposed body edits, and open architectural questions for future cycles.

The skill does *not* write to the wave doc. It does not edit the architecture doc body or the ADR log directly — those edits are made by `wave-redraft` when it ratifies the proposed changes from this report.

## Inputs and output

**Inputs:**
- The wave doc (`<project-slug>-wave-doc.md`). Required.
- The execution report (`<project-slug>-wave-doc.reports/wave-W<N>-execution.md`). Required.
- The audit report (`<project-slug>-wave-doc.reports/wave-W<N>-audit.md`). Required. Verdict must be `pass` or `pass-with-findings` — a `fail` verdict blocks this skill.
- The architecture doc (`<project-slug>-architecture.md`).
- The ADR log (`<project-slug>-adr/`).
- The vision doc (`<project-slug>-vision.md`). Read to confirm proposed changes don't drift from vision; not modified.
- The repo diff for the wave (the changes since the previous wave's closeout). Use `git diff` or equivalent.

**Output:**
- A new file: `<project-slug>-wave-doc.reports/wave-W<N>-architect-review.md`, conforming to architecture-schema Section 6.
- Optionally: draft ADR files written into the ADR directory with `Status: Proposed`. The redrafter will move them to `Accepted` when it ratifies them. Drafting them now is acceptable; ratifying them is not this skill's job.

## Workflow

### 1. Read everything in order

Read the inputs in this order: wave doc (current-wave section), execution report, audit report, vision doc (relevant constraints and non-goals), architecture doc, ADRs cited by the wave. Then walk the diff.

The order matters: starting with the wave doc orients you to what was supposed to happen; the reports tell you what did happen; the architecture and ADRs tell you what was supposed to be true; the diff tells you what is actually true.

### 2. Resolve adherence disagreements

For each ADR cited in the wave doc's `ADRs respected:` field, compare:
- The execution report's claim about adherence.
- The audit report's independent verdict about adherence.
- Your own reading of the diff.

If all three agree, note "respected" and move on. If they disagree, you must reconcile. The audit report's verdict generally wins for factual claims; the execution report wins for intent ("we tried to respect this but it didn't work because..."). Document the resolution in your report's Adherence Check section.

If an ADR was violated by the implementation:
- Was the violation deliberate? (Executor mentions it in discoveries and proposes a supersession.) → Propose the supersession in your report.
- Was the violation accidental? (Audit caught it but executor didn't acknowledge.) → Propose a fix path: either revert the violating code, or supersede the ADR if the new behavior is correct.

### 3. Decide whether to propose new ADRs

Walk the discoveries and proposed scope changes from the execution report. For each:
- Does this discovery imply a structural choice that should be captured as an ADR? (Often yes for things like "we added an SMTP dependency", "we introduced a queue abstraction", "we changed the data shape of X".)
- If yes, draft the ADR's body inline in your report. Use the full ADR template from architecture-schema Section 4. Status: `Proposed`.

Do not propose an ADR for everything. The bar is the same as architect-draft's: at least one negative consequence, and the decision is structural rather than tactical. "We optimized the SQL query" is not an ADR.

### 4. Decide whether to propose supersessions

For each existing ADR that was challenged in this wave:
- Does the new evidence invalidate the ADR's decision in a meaningful way? Or does it just refine our understanding without changing the choice?
- If the decision is invalidated, draft a superseding ADR. The superseding ADR's `Supersedes:` field names the old ID. Its body explains the new decision in light of what was learned.
- The old ADR is *not* edited as part of this skill (its `Superseded by:` field will be updated by the redrafter when the new ADR is ratified).

A supersession is a substantive event. Don't propose them lightly. Multiple supersessions in one cycle is a sign that the wave's architectural foundation was weak — flag this as an open architectural question rather than just rubber-stamping each supersession individually.

### 5. Decide on body edits

Some architecture-doc body sections must change to keep the doc consistent with newly-accepted ADRs. Common cases:
- A superseded ADR's data model decision is replaced — Section 4 (Data model) of the architecture doc must change.
- A new ADR introduces a new module — Section 2 (Module decomposition) must be updated.
- A non-functional consideration is now ADR-governed when it wasn't before — Section 7 must cite the new ADR.

State each proposed body edit in your report as a quoted before/after, with the ADR ID it depends on. The redrafter will apply the edits when it ratifies the ADRs.

### 6. Surface open architectural questions

Some things the wave revealed are not yet decisions — they are open architectural questions for future cycles. For example: "the SMTP dependency works for solo deployment but creates a question about multi-tenant deployment that we're deferring to W5." These belong in the report's Open Architectural Questions section, not as ADRs. They will be revisited when relevant.

This section mirrors the vision doc's Open Questions, at the architecture layer.

### 7. Write the report

Use the template from `references/architecture-schema.md` Section 6 exactly. Save to `<project-slug>-wave-doc.reports/wave-W<N>-architect-review.md`.

The report begins with YAML frontmatter. Set `summary` to one of `no-changes` / `new-adrs-proposed` / `supersessions-proposed` / `body-edits-required` — this is the canonical machine-readable verdict that `vader-next` and the redrafter consume. The body's `## Summary` section is the human-readable justification.

If you drafted proposed ADR files, save them to the ADR directory with `Status: Proposed`. They are *not* binding until the redrafter ratifies them.

Tell the user concisely: what the review concluded (no changes / new ADRs / supersessions / body edits), where the report is, and that the next step is `wave-redraft`.

## Principles to keep in mind

**Independence is the value.** This skill is the deliberate "step back from the wave's narrative and check the structure" pass. Don't be persuaded by the executor's framing of an issue; verify against the diff and the architecture doc.

**Supersession preserves history.** Never edit an existing ADR's body — propose a successor instead. The history of what we believed and why matters.

**Be specific about proposed changes.** A vague "the data model needs updating" is useless to the redrafter. A specific "ADR-004 superseded by proposed ADR-007 (full body below); architecture doc Section 4 'votes' table description replaced with: <new schema>" is actionable.

**An ADR with no downsides is not an ADR.** Force the negative consequence. If you can't articulate a downside to a supersession, the supersession may not be needed (or you haven't thought hard enough).

**Architectural questions deferred are not architectural questions ignored.** The Open Architectural Questions section is how you keep deferrals visible to future cycles.

## Anti-patterns to avoid

**Rubber-stamping.** Concluding "no changes needed" without doing the adherence checks against the diff. The redrafter will trust your report; if it's shallow, downstream cycles drift.

**Bureaucratic ADRs.** Drafting an ADR for every minor refinement. ADRs are for decisions whose revision has real cost. A choice that's easy to undo doesn't need one.

**Editorializing the wave's decisions.** Your job is to surface what the architecture says about the wave's outcomes — not to relitigate decisions made in earlier cycles. If you disagree with an existing ADR that was respected this wave, that's an open architectural question, not a finding.

**Mixing audit findings with architecture findings.** The audit's findings are about acceptance and scope. Your findings are about structural decisions. Don't duplicate; cite the audit's findings when they're architecturally relevant and add architectural commentary where the audit can't.

**Pre-empting the redrafter.** Do not edit the wave doc, the architecture doc body, or any existing ADR. Propose. The redrafter ratifies.

## What to do if the architecture is silent on something the wave revealed

Sometimes a wave reveals that an entire area of the system has no ADR coverage at all — e.g., the wave introduces an SMTP dependency and no ADR governs how external dependencies are managed. This is not a violation; it's a gap. Two responses are appropriate:

- Propose a new ADR to cover the area, drafted inline in your report, status `Proposed`.
- If the area is genuinely not yet ready to be decided (e.g., we don't yet know whether external dependencies will be a recurring pattern), put it in Open Architectural Questions and wait.

Either is acceptable. Don't pretend coverage that doesn't exist; don't manufacture coverage prematurely.

## What to do if the wave was a deferred or no-op wave

A wave whose audit verdict is `pass-with-findings` and whose findings are all in non-architectural areas (UI polish, test infrastructure, etc.) may genuinely produce a `no changes` architect-review. That's fine. The report still gets written, conclusion `no changes`, with a brief explanation. The empty pass keeps the cycle's audit trail complete.

A wave whose verdict is `fail` blocks this skill. Do not run; tell the user the audit needs to be addressed first.

## Handoff

After the architect-review report is saved, tell the user the next step is `wave-redraft`. Summarize the report's conclusion in one or two sentences (e.g., "Found one ADR that needs supersession (ADR-004 → ADR-007 row-per-rank voting); two body edits proposed for architecture doc Section 4. Two open architectural questions for W3 to resolve.") so the user knows what's coming. Do not invoke wave-redraft yourself.

**Git.** If the project uses git, suggest the user commit with `arch-review: W<N> — <one-line conclusion>` (e.g., "no changes" or "propose ADR-007 supersedes ADR-004"). The proposed ADR files (status `Proposed`) are part of this commit. Add a `Co-authored-by: Claude <noreply@anthropic.com>` trailer. See `references/git-conventions.md`.
