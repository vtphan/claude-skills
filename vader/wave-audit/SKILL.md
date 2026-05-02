---
name: wave-audit
description: Use this skill when a wave has been executed (an execution report exists) and the user wants the wave independently verified before redraft. Triggers include phrases like "audit W<N>", "verify the current wave's execution", "run the audit on the latest wave", "check whether the execution report's claims hold up", "do the wave-audit pass", or whenever an execution report exists and the user is ready to advance the cycle. Also trigger when the user gestures at the next step after wave-execute ("now check it", "verify it"). Do NOT use when no execution report exists yet (run wave-execute first). Do NOT use to write or modify code; this skill verifies, not implements. Do NOT use to modify the wave doc — only the audit report is produced.
---

# Wave Audit

Independently verify the current wave's execution against the wave doc, the architecture/ADRs, and the actual code in the repo. Produce an audit report with a verdict (`pass`, `pass-with-findings`, or `fail`) that gates the rest of the cycle.

Before doing anything else, read `references/wave-schema.md` in full — particularly Section 10 (audit report template), Section 12 (cycle order and gating), and Section 14 (invariants).

## What this skill does

This is the verification gate that protects the wave doc from quietly drifting into fiction. The auditor does not trust the executor's narrative — it re-derives the answer from the artifacts. Three checks are non-negotiable:

1. **Exit-criteria verification.** Run the wave's repro. Run the tests. For each exit criterion, produce an independent pass/fail/unverifiable verdict with a reproduction step.
2. **ADR-adherence check.** For each ADR cited by the wave, independently confirm whether the implementation respects it. Compare with the execution report's claim; flag disagreements.
3. **Scope check.** Walk the diff. Identify changes that don't map to planned tasks, declared discoveries, or scope changes proposed in the report.

The output is a single audit report. The verdict gates the remainder of the cycle.

## Independence is the point

This skill should be invoked as a fresh agent run with no access to the executor's internal reasoning, scratch notes, or chain of thought. It only reads the committed artifacts: the wave doc, the execution report, the repo diff, the architecture doc, the ADRs.

The auditor's mindset is: "The execution report is one input. It is not the truth. The truth is what the artifacts say." Where the report and the artifacts disagree, the artifacts win.

## Inputs and output

**Inputs:**
- The wave doc (`<project-slug>-wave-doc.md`). Required.
- The execution report (`<project-slug>-wave-doc.reports/wave-W<N>-execution.md`) where `W<N>` matches `current_wave` in the wave doc. Required.
- The repo, including the diff for the current wave (`git diff <prior-wave-tag>..HEAD` or equivalent).
- The architecture doc and ADRs cited by the current wave.
- The vision doc (Goal, Non-goals) for scope-leakage checks.

**Output:** `<project-slug>-wave-doc.reports/wave-W<N>-audit.md`, conforming to schema Section 10. Contains a verdict, exit-criteria verification, task verification, assumption verification, ADR adherence, scope findings, entry-criteria check for the next wave, findings, and recommendations.

## Workflow

### 1. Read everything in independence-preserving order

Read in this order, deliberately:
- The wave schema (if not already this session).
- The wave doc (current-wave section, registers, ADR references).
- The architecture doc and the ADRs cited by the current wave.
- The vision doc (Goal, Non-goals, success metrics).
- The repo state — what does the codebase look like now, what's the test setup.
- **Now — only now — read the execution report.** Reading it last preserves your independence; you form expectations from the doc and the artifacts before being primed by the executor's narrative.

### 2. Run the repro

Run the wave's repro script (or equivalent end-to-end check). Note pass/fail per exit criterion. The repro is your primary evidence for exit-criteria verification.

If the repro doesn't exist or doesn't run, that's a finding — the wave's repro path is part of its exit criteria, and a missing repro means the wave can't be honestly audited.

### 3. Walk the diff against the plan

Establish the diff baseline first. Read the execution report's frontmatter — specifically `wave_start_ref` and `wave_end_ref`. Run `git diff <wave_start_ref>..<wave_end_ref>` to see exactly the wave's changes. Record the same refs in your audit report's `diff_baseline` and `diff_head` frontmatter fields so the trail stays explicit.

If the execution report's frontmatter doesn't have these fields (the project doesn't use git, or the executor failed to capture them), fall back to `git diff <prior-wave-tag>..HEAD` if a prior tag exists, or to the report's own claims about what was changed. Note the fallback as a finding so the next wave's executor knows to capture refs.

For each task in the current wave's task list:

- Find the diff that implements it.
- Confirm the change matches the task description and acceptance criteria.
- Note discrepancies: a task marked `[x]` with no corresponding diff, a diff that goes beyond the task's scope, an acceptance criterion that the diff doesn't actually satisfy.

For changes in the diff *not* tied to a task:
- Are they declared in the report's Discoveries or Proposed scope changes?
- Are they implicit plumbing (build setup, dependency management) that doesn't need a task?
- Or are they undeclared scope creep? Flag.

### 4. Verify ADR adherence independently

For each ADR cited by the wave (in `ADRs respected:`):
- Read the ADR.
- Look at the implementation in the diff.
- Form your own verdict: respected, violated, or unclear.
- Compare with the execution report's claim.
- If they disagree: the diff wins; flag the disagreement as a finding.

### 5. Verify assumption claims

For each assumption the report claims to have validated or broken:
- What evidence does the report cite?
- Does the evidence actually support the claim?
- For "validated" claims: is the evidence specific enough? "Performance is fine" is not validation; "30-member synthetic test ran in 1.2s p95 against the success metric of 5s" is.
- For "broken" claims: is the proposed replacement assumption named (e.g., A6)? Does it follow from the evidence?

### 6. Check next-wave entry criteria

Read the wave doc's W<N+1> entry criteria (sketch). Do the current wave's outputs satisfy them? If not, what's missing? Flag — the next wave can't start cleanly without this.

### 7. Form a verdict

The verdict gates everything downstream. Three values:

- **`pass`** — All exit criteria met. All claims independently verified. No ADR violations. No undeclared scope changes. Next-wave entry criteria satisfied. The cycle proceeds normally.
- **`pass-with-findings`** — Substantive issues exist but none block closeout. Examples: an exit criterion was admitted as not fully met by the report, an ADR adherence is in question, a finding requires the redrafter's attention. Architect-review and redraft proceed, addressing findings explicitly.
- **`fail`** — One or more exit criteria not met in fact (not just admitted). An ADR violated without a supersede proposal. Next-wave entry criteria unsatisfied. A scope finding that's clearly out of scope and can't be retroactively justified. Closeout cannot proceed.

The bar between `pass-with-findings` and `fail`: if the redrafter can absorb the findings into a clean redraft cycle, it's `pass-with-findings`. If it can't — the wave is truly not done — it's `fail`.

### 8. Write the report

Use the template from schema Section 10 exactly. The report begins with YAML frontmatter; set `verdict` to one of `pass` / `pass-with-findings` / `fail` (this is the canonical machine-readable verdict, used by `vader-next` and other tooling). Set `diff_baseline` and `diff_head` to the refs you used for the diff walk. Then write the body — a one-paragraph summary justifying the verdict, followed by the structured sections.

Be specific in findings — name what's wrong, where, with what severity, and what kind of decision is needed.

The report's *Recommendations to architect-review and redrafter* section is brief — name the issues that need a decision, not prescriptions for how to decide them. The architect-review and redraft skills make those calls.

### 9. Hand off

Tell the user the verdict and where the report is. If `pass` or `pass-with-findings`, the next step is `architect-review`. If `fail`, the user must decide whether to loop back to `wave-execute` or to renegotiate scope explicitly via `wave-redraft`. Don't invoke either.

## Principles to keep in mind

**Re-derive, don't re-grade.** Don't ask "did the executor's claim hold up?" Ask "given the wave doc's acceptance criteria and the artifacts in the repo, what's the actual answer?" The execution report is one source; the artifacts are the source of truth.

**Specificity is verification.** A pass verdict supported by "looks fine" is worthless. A pass verdict supported by "ran scripts/demo-w2.sh in a clean checkout, all three exit-criteria checks printed PASS" is durable.

**Findings are surgical.** Each finding names: what's wrong, the evidence, severity (low/medium/high), and the kind of decision needed. They are not narratives about the wave; they are decision-prompts for downstream skills.

**The report's job is to enable, not decide.** You surface what needs deciding; architect-review decides on architecture; redraft decides on scope. Don't pre-empt.

**No silent verdicts.** Every exit criterion gets an explicit verdict. Every cited ADR gets an explicit adherence verdict. Every assumption claim gets an explicit verification verdict. If you can't verify something, the verdict is `unverifiable`, not silent.

## Anti-patterns to avoid

**Rubber-stamping.** Marking everything `pass` because the executor's report sounds confident. The executor's confidence is one input; the artifacts are another. They must agree.

**Reading the report first and being primed.** The order of reading matters. Read the wave doc and the artifacts first; the report last. Independence is a habit you have to build deliberately.

**Findings without severity.** "There's an issue with X" is not a finding. "F1: ADR-004 violated by T2.3 (severity: medium); the implementation introduces a row-per-rank shape contrary to the flat-columns ADR. Recommendation: surface to architect-review for supersession" is.

**Conflating audit and architect-review.** The auditor reports adherence facts; it does not propose ADR supersessions or new ADRs. That's architect-review's job. Cite the issue; let the next skill decide.

**Re-litigating settled decisions.** If an ADR was respected and works, the auditor doesn't second-guess it. The auditor's scope is "did this wave do what it said it would" — not "was the wave the right plan."

## Things to never do

1. **Never modify the wave doc, the architecture doc, or any ADR.** This skill writes only the audit report.
2. **Never rubber-stamp.** A verdict requires evidence. If you don't have evidence, the verdict is `unverifiable`.
3. **Never trust the report over the artifacts.** Where they disagree, the artifacts win.
4. **Never propose ADR changes.** That's architect-review's job.
5. **Never produce an audit report without running the repro.** If the repro doesn't exist, that's itself a finding.
6. **Never declare a verdict before the findings are specific.** A verdict without supporting findings is rubber-stamping.

## Worked mini-example

Wave: W2 (Query by tag). Four tasks, all marked `[x]` in the wave doc. Execution report claims `pass` self-assessment.

1. Read the wave doc. Note exit criteria (find returns matches; boolean queries work; 10k-file query under 2s p95). Note ADRs cited (ADR-001 SQLite, ADR-004 flat-vote-columns).
2. Read architecture doc, ADRs, vision (Non-goals: no cloud sync).
3. Read repo. Run `git diff` since W1 closeout.
4. Read execution report.
5. Run repro: `scripts/demo-w2.sh`. First two exit criteria PASS. Third (under 2s p95) prints 1.6s — PASS.
6. Walk diff. T2.1, T2.2, T2.3 implementations match tasks. T2.4 (E2E) only covers nominate+vote, not tie-break — report admits this; status `[~]` would be appropriate but doc shows `[x]`. Discrepancy.
7. ADR adherence:
   - ADR-001 (SQLite): respected — only SQLite calls in diff.
   - ADR-004 (flat vote columns): violated — diff introduces a row-per-rank table. Report admits this and proposes supersession to architect-review. Adherence verdict: violated, but acknowledged.
8. Scope: one finding — `tests/perf/` directory added with no corresponding task or discovery. Likely benign (the executor admits in discoveries it added perf tests), but flag.
9. Next-wave entry criteria: W3's sketch entry says "query engine stable enough to verify re-scan correctness." The current wave's outputs satisfy that.
10. Verdict: **pass-with-findings**.
    - F1 (medium): T2.4 marked `[x]` but admits partial coverage. Recommend redrafter set to `[~]` in past-wave section.
    - F2 (medium): ADR-004 violated by T2.3; report acknowledges. Recommend architect-review propose ADR-007 (row-per-rank).
    - F3 (low): undeclared `tests/perf/` directory. Note in scope findings; not blocking.
11. Write report. Hand off to user; next step is architect-review.

## Handoff

After the audit report is saved, tell the user the verdict and the path. Suggest `architect-review` if `pass` or `pass-with-findings`; otherwise explain what blocks closeout. Do not invoke architect-review or wave-redraft.

**Git.** If the project uses git, suggest the user commit with `audit: W<N> — <verdict>` (e.g., `audit: W2 — pass-with-findings`). Add a `Co-authored-by: Claude <noreply@anthropic.com>` trailer. See `references/git-conventions.md`.
