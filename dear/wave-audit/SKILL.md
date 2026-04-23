---
name: wave-audit
description: Use this skill whenever a wave's execution has completed and the user wants an independent verification before the wave doc is updated — checking that claimed task completions are real, running exit criteria fresh against the repo, verifying assumption-status and commitment-adherence claims, detecting scope creep, and confirming the next wave's entry criteria are satisfied. Triggers include phrases like "audit the current wave", "verify W1", "check the execution report", "independently validate what was built", "run the A in DEAR", or whenever both a wave doc and an execution report are present and the user wants a third-party check before advancing. Also trigger when the user says "I don't trust the report — verify it" or "make sure we can actually move to the next wave." Do NOT use when there's no execution report yet (use wave-execute first), when the wave doc is being changed without execution (use wave-redraft), or when the task is to build, not to verify.
---

# Wave Audit

Independently verify a just-executed wave against the wave doc and the execution report, producing an audit report with a clear verdict. This skill writes no code and modifies no project source; its only outputs are the audit report and, if the audit surfaces issues, a clearly-articulated set of findings for the redrafter.

Before doing anything else, read `references/wave-schema.md` in full — particularly the audit report template in section 10 and the invariants in section 11. The schema is the contract; an audit that deviates from it isn't an audit.

## Inputs and outputs

**Inputs:**

- The wave doc (`<project-slug>-wave-doc.md`). The doc's current-wave section is the spec the audit checks against.
- The execution report (`<project-slug>-wave-doc.reports/wave-W<N>-execution.md`). The claims to be verified.
- The project repo at current state — same state the executor left it in. You exercise this directly.
- Optionally, prior audit reports — useful for pattern recognition (does this wave share a failure mode with a previous one?).

**Output:** a single audit report at `<project-slug>-wave-doc.reports/wave-W<N>-audit.md`, using the template in `references/wave-schema.md` section 10. The report carries a verdict (`pass`, `pass-with-findings`, or `fail`) and a specific, cited set of findings.

## What this skill is for

The audit exists because AI-assisted execution has predictable failure modes that are not caught by the executor self-reporting — because the executor is the one making the errors and has no reason to describe them. Specifically:

- **Acceptance rubber-stamping** — tasks marked `[x]` whose acceptance doesn't actually pass.
- **Silent scope creep** — code changes in the diff that don't map to planned tasks.
- **Wishful assumption claims** — "A2 validated" with no evidence behind it.
- **Commitment drift** — new dependencies, new persistence layers, new auth paths that violate active architectural commitments.
- **Unready handoff** — the next wave's entry criteria aren't actually satisfied, but the executor didn't notice.
- **Repro rot** — the repro script "works on my machine" but fails from a clean checkout.

The audit is independent in spirit: it approaches the wave doc and the report as claims to be verified, not narrative to be accepted. For maximum independence, the audit skill should be invoked as a separate agent run from the executor — not via a thread that shares context with the execution.

## Operating principles

### 1. Verify, don't narrate

An audit is a series of checks, each producing a pass or fail with evidence. The report is not a retelling of the execution report; it's an independent judgment.

If the execution report says "T2.2 done," the audit doesn't say "T2.2 done" — the audit says either "T2.2 acceptance verified by running `tests/test_query.py::test_boolean_ast`; passed" or "T2.2 acceptance NOT verified: benchmark in task acceptance runs at 3.8s p95, not under 2s p95 as specified."

### 2. Run the repro

The wave doc requires a repro path. The single highest-leverage thing the audit does is run it from a clean state. If the repro fails, almost every other check becomes questionable; if it passes, most exit criteria are already verified as a byproduct.

Run the repro in a way that's as clean as practical — fresh checkout if possible, a clean fixture directory, no local state the executor might have relied on unintentionally.

### 3. Exit criteria are verified, not trusted

For each exit criterion in the current wave's section of the wave doc:

- Determine what behavior would demonstrate it (the exit criteria should be phrased for this; if they aren't, that's itself a finding).
- Exercise it — run the script, run the test, run the command.
- Record pass or fail with specific evidence (test name, command output excerpt, observed metric value).

Do not mark an exit criterion verified based on the execution report's claim. The executor may have claimed it in good faith; the audit's job is to re-verify.

### 4. Commitments are checked against the diff

The wave doc's current wave lists commitments the wave is expected to respect. For each:

- Look at what the wave changed (git diff from the prior wave's end state, or from the last audited state).
- Ask: does anything in the diff conflict with this commitment? New persistence? New runtime? Mismatched stack?
- If yes, that's a finding — regardless of whether the execution report mentioned it.

For each commitment the execution report claims this wave established (new commitments), check that:

- It appears in the wave doc's commitments register with a rationale.
- The code evidences the commitment (e.g., if AC4 is "SQLite full-text search via FTS5," the index creation SQL actually uses FTS5).

### 5. Scope findings are named, not shrugged off

A diff contains every change the executor made. Cross-reference the diff against the planned tasks and the discoveries in the execution report. Anything in the diff that can't be explained by either is a scope finding — potentially benign (refactor of a shared utility the task incidentally touched) or potentially not (an entire new feature was built).

Don't editorialize; report. "The diff includes `auth/sso_provider.py` (new file, 180 lines). No task in W2 mentions SSO; no discovery explains it. Finding Fn: unplanned SSO provider added." Let the redrafter decide what to do.

### 6. Entry criteria for the next wave are a hard check

The wave doc's W<N+1> section (sketch) carries entry criteria. The audit's job is to confirm the current wave's outputs actually satisfy those entry criteria. If not, that's a finding — likely a severe one — because the redrafter will otherwise expand W<N+1> based on a false premise.

If the current wave's outputs do satisfy most of the next wave's entry criteria but leave one or two gaps, name them specifically. "W3 entry criterion 'index schema stable' is met (no schema changes in the last two passes). W3 entry criterion 'query engine callable from W3's scheduler' is NOT met — the query engine is currently CLI-only; no internal API exposed."

### 7. Verdict is the last thing, not the first

The verdict falls out of the findings. Don't decide the verdict first and then curate findings to fit it. Collect the findings honestly; apply the rubric at the end.

Verdict rubric:
- **pass**: all exit criteria verified, all assumption/commitment claims cross-checked, no scope findings, next wave's entry criteria satisfied.
- **pass-with-findings**: substantive issues exist but none prevent closeout. Every finding is named, evidenced, and has severity indicated. The redrafter addresses findings in the change log and possibly in the next wave's plan.
- **fail**: one or more of: an exit criterion not met in fact (not just admitted), a commitment violated without a supersede proposal, entry criteria for the next wave unsatisfied, or substantial unreported scope changes in the diff. A fail verdict blocks redraft closeout; the user either loops back to execute or explicitly renegotiates via scope change.

## Workflow

### 1. Read everything first

- `references/wave-schema.md` — the contract.
- The wave doc in full, paying special attention to: the current wave's entry criteria, exit criteria, tasks with acceptance, commitments the wave respects, commitments the wave proposes to establish, and assumptions referenced.
- The execution report in full. Note every claim that will need verification.
- The W<N+1> sketch — its entry criteria are what you'll check at the end.
- The repo state. Particularly, the diff since the prior wave's end (or since the last audit, if this isn't the first wave audit).

### 2. Run the repro

Run `scripts/demo-w<N>.sh` (or whatever the wave doc names as its repro path) from a clean state. Record what happened — passed, failed, partial. If the repro is missing or doesn't exist yet at the declared path, that's the first finding.

### 3. Verify exit criteria

For each exit-criterion bullet in the wave doc's current-wave section:

- Identify the mechanical way to check it.
- Run that check.
- Record pass/fail with specific evidence.

When in doubt about what would count as verifying an exit criterion, err toward more checking rather than less. It's cheap to verify and expensive to miss.

### 4. Verify task status

Cross-reference:

- The wave doc's current-wave task checkboxes (`[x]` / `[ ]`).
- The execution report's *Task status* section.
- The diff — does the code evidence the task's work?

Flag any task where the three disagree. Common patterns:

- Doc says `[x]`, report says done, diff is thin — maybe the acceptance wasn't really met.
- Doc says `[ ]`, report says `[~]` (partial) — normal, note what's left.
- Doc says `[x]`, report omits the task entirely — something was skipped in the handoff.

### 5. Verify assumption-status claims

For each assumption the report claims to have validated or broken:

- Find the evidence (a test output, user-testing notes, a benchmark run, a code artifact).
- Judge whether the evidence actually supports the claim.
- Record the check: "A2 marked broken, evidence is user-test transcript at `research/w2-voting.md`, confirmed." Or: "A4 marked validated, evidence claimed is benchmark in T2.2, but benchmark output shows 1.4s — above untested threshold. Finding Fn: validation may be premature."

### 6. Verify commitment adherence and additions

For each commitment referenced by the current wave:

- Check the diff for patterns that conflict with the commitment.
- Note adherence or flag a conflict.

For each new commitment the report claims the wave established:

- Check the register entry exists with a rationale.
- Check the code evidences the commitment.

### 7. Scope findings

Look at the diff one more time, top to bottom. For each change:

- Does a planned task explain it?
- Does a declared discovery explain it?
- If neither, it's a finding.

Don't include noise findings (whitespace changes, import reordering) unless they signal something larger.

### 8. Next wave's entry criteria

Open the wave doc's W<N+1> section. For each entry-criterion bullet:

- Can the current state of the repo satisfy it?
- If yes, note satisfied.
- If no, name the gap specifically.

### 9. Synthesize and write the audit report

Using the template in `references/wave-schema.md` section 10, produce the audit report. Apply the verdict rubric after collecting findings — do not pre-commit to a verdict.

Save to `<project-slug>-wave-doc.reports/wave-W<N>-audit.md`. Report to the user: verdict, the one or two most consequential findings if any, where the full report lives.

## What a good finding looks like

A finding has:

- **An ID** (F1, F2, ...).
- **A severity** — low, medium, high. High findings block closeout; medium and low don't.
- **A crisp statement** — what's wrong, in one or two sentences.
- **Evidence** — what the auditor observed (test output, diff snippet, command output, absence of a required artifact).
- **An implication** — what breaks or might break because of this.
- **A recommendation for the redrafter** — not a prescription, a suggestion. The redrafter decides.

Example:

> **F2** — AC3 (single-binary) at risk due to new SMTP code path added in T2.3.
> Severity: medium.
> Evidence: `filetagger/notify.py` (new, 140 lines) imports `smtplib` and assumes runtime Python; PyInstaller build previously did not include the `ssl` module needed by SMTP.
> Implication: a `pyinstaller --onefile` build against current code will either fail at build time or produce a binary that can't send mail at runtime.
> Recommendation for redrafter: either (a) supersede AC3 to explicitly allow an external SMTP binary, or (b) add a W<N+1> task to bundle SSL support and verify the single-binary build still works end-to-end.

Findings like the above are useful. Findings like "the code could be cleaner" are not and should not appear in the audit report.

## What this skill does NOT do

- **Does not edit the wave doc.** Only `wave-redraft` modifies the wave doc. Audit produces a report.
- **Does not edit project code.** Even to "fix" a finding. If the code needs to change, that's execution's job, triggered by a redraft decision.
- **Does not rewrite the execution report.** The audit's disagreements go in the audit report, not by mutating the executor's output.
- **Does not prescribe the next plan.** The audit surfaces what needs a decision; the redrafter makes the decision.
- **Does not decide pivots.** A `fail` verdict signals something is wrong, but "wrong" is a spectrum — could be a small loop-back or could be a pivot. The redrafter, in dialog with the user, decides.

## How to handle a missing or malformed report or doc

If the execution report is missing, stop and ask the user whether execute actually ran. If it ran but no report was produced, that's itself a finding — but you can't audit absent an executor's claims, so the appropriate action is to surface the gap, not to construct claims from the diff alone.

If the wave doc is malformed (no current wave marked, future waves have task detail, etc.), stop and flag. Don't try to reconstruct what the doc should say; that's the redrafter's job.

If the repro path is missing or points to a nonexistent script, that's itself a high-severity finding — the wave is fundamentally not audit-ready. The audit report's verdict is `fail`; the single finding is the missing repro; redraft will need to handle it.

## When the audit is "boring"

On a well-run wave, the audit often comes back clean — verdict `pass`, no findings. This isn't a failure of the audit; it's the system working. The audit's value isn't in finding problems every time; it's in credibly being *able* to find problems when they exist. An audit that never finds anything because it didn't look hard would be worse than useless. An audit that often finds nothing because the executor was disciplined is exactly the expected steady state.

Still write the full report even for a clean audit. The empty sections are themselves a record: we checked, nothing to flag. Six months later, that record is what the user refers to when asking "how did we verify this?"

## Handoff

After the audit, the wave is ready for redraft. Tell the user: verdict, the one or two most consequential findings if any, the path to the audit report. Suggest the next step: invoke `wave-redraft`. If the verdict is `fail`, say so plainly and indicate that redraft can't close out the wave until the issue is addressed — either by looping back to execute with corrections or by the user explicitly renegotiating scope.
