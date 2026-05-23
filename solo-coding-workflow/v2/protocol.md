# Protocol

This file is normative. Commands, skills, and agents must follow it.

## Operating Model

- One `/build` orchestrator runs at a time, within one conversation per phase.
- `/build` invokes the verifier subagent synchronously.
- Git is the source of truth for code changes.
- `.project/` is the source of truth for intent, scope, contracts, and decisions.
- One verified slice produces one Git commit.
- Approved gate artifacts are committed before the next stage starts.
- The human lead makes product and architecture decisions only.
- The orchestrator handles process hygiene and does not ask the human to approve individual slices.
- If a phase does not fit in one conversation, the plan is too large for this workflow as
  written; split the project or re-plan into smaller phases before continuing.

## Required Project Files

```text
.project/
  spec.md
  design.md
  decisions.md
  contracts/
    <contract files as needed>
  slices/
    <slice>/
      status.json
      boundary.md
      acceptance.md
      build.md
      verify.md
```

Per-slice files are the operational source of truth.

## Slice Status

`.project/slices/<slice>/status.json`:

```json
{
  "slice": "<slice>",
  "state": "todo",
  "phase": 1,
  "depends_on": []
}
```

States:

- `todo`: not yet verified.
- `verified`: passed verification and committed.
- `blocked`: a human decision is required before this slice can proceed.

Only build writes status. The verifier never writes status.

## Git Invariants

Before each slice:

- `git status --short` must be clean.

Before `/build` starts:

- approved spec and plan artifacts must be committed.
- gate approval entries must exist in `decisions.md`.

At gates:

- the command stops for human approval;
- if approval is given in the same conversation, the command records the approval in
  `decisions.md`, commits the gate artifacts, and only then tells the human the next command;
- if approval is not yet given, no approval commit is made.

After verifier PASS:

- Build marks the slice `verified` and commits source plus `.project/` updates for that slice in one commit.
- The working tree must be clean before selecting the next slice.

Commit formats:

```text
slice(<slice>): <short outcome>
project: approve spec
project: approve plan
project: approve contract change
integrate: <short outcome>
```

Do not commit on FAIL or BLOCKED.

## Slice Selection

Eligible:

- state is `todo`;
- all dependencies are `verified`;
- no human decision pending;
- Git tree is clean.

Order: lowest `phase` first, then declaration order in `design.md`, then lexical slice name.

When no eligible slices remain:

- if all required slices are `verified`, recommend `/integrate`;
- otherwise report the blocking slices and reason.

## Boundary Preflight

Before editing a slice, build reads:

- `.project/spec.md`
- `.project/design.md`
- `.project/contracts/*`
- `.project/decisions.md`
- the slice's `boundary.md`, `acceptance.md`, `status.json`
- the slice's latest `verify.md` if it has a prior failed attempt

Build classifies expected touches before editing:

- current slice territory: proceed.
- future slice territory: proceed only if necessary; update that slice's `boundary.md` or `acceptance.md` and log to `decisions.md`.
- verified slice territory: stop for gate 2 unless the change is mechanical and every affected
  verified slice can be re-confirmed by a verifier invocation in the same build cycle; log to
  `decisions.md` either way.
- contract: stop for gate 2.

When classifying touches, build must have enough whole-project ownership context to identify
whether a touched file/resource belongs to the current slice, a future slice, or a verified
slice. `design.md` and slice `boundary.md` `Owns` sections are the first authority; read
broader boundary details only when ownership is ambiguous.

## Verifier Invocation

Build invokes the verifier subagent after finishing implementation.

Build passes only:

- the slice name;
- instructions to read `.project/` artifacts (including `decisions.md`) and inspect the Git diff;
- instructions not to trust build's informal summary;
- instructions not to edit source, status, contracts, design, boundaries, acceptance, or build logs.

Verifier writes only `.project/slices/<slice>/verify.md` and returns a concise PASS/FAIL/BLOCKED summary.

If the implementation mechanically touched verified-slice territory, build invokes the
verifier once for the current slice and once for each affected verified slice before any
commit. All invocations must PASS. If any affected verified slice cannot be confidently
re-confirmed from the current diff and checks, build stops for gate 2 instead of committing.

## Verify-Fix Loop

1. Build implements.
2. Verifier checks.
3. On PASS, build marks `verified`, commits, and continues.
4. On FAIL with implementation defects, build fixes and re-verifies.
5. On BLOCKED, or repeated FAIL the orchestrator cannot resolve, build marks `blocked` and stops for the human lead.

Stop immediately for:

- contract change;
- architecture or boundary decision;
- product behavior ambiguity;
- scope drift changing user-visible behavior;
- repeated verification failure the orchestrator cannot resolve.

## Verifier Required Checks

- Acceptance criteria in `acceptance.md` (run listed check commands when available).
- Contract conformance.
- Boundary/scope conformance.
- Spec alignment, accounting for `decisions.md`.
- Unrecorded crossings in the Git diff.
- Verified-slice territory touched without a recorded decision.
- Source files edited without `build.md` logging.

Verifier distinguishes:

- implementation defect: build may fix;
- decision required: human lead must decide;
- protocol error: build must stop and recover or escalate.

Do not mark FAIL for style-only nits. Record nits as notes under PASS.

## Decisions

Append to `.project/decisions.md` for:

- gate approvals;
- contract changes;
- boundary or architecture changes;
- future-slice crossings;
- verified-slice territory crossings;
- repeated verification failure escalations;
- integration approval.

Format:

```markdown
## <ISO timestamp> - <short title>

- Decision: <what was decided>
- Reason: <why>
- Affected slices: <slice list or none>
```

## Human Gates

Stop for the human lead only at:

- gate 0: spec approval;
- gate 1: plan approval;
- gate 2: contract/product/architecture decision;
- repeated verification failure the orchestrator cannot resolve;
- gate 3: integration approval.

When stopping, present: issue, evidence, options, default recommendation, exact files/slices affected.
