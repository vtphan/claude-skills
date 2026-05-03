# ACCORD Execution Report Contract

`execute` writes an execution report for the approved unit. The report is the executor's only narrative to a reviewing agent that may be running in a fresh conversation, possibly with a different LLM (per principle 9). It must be self-sufficient for that handoff.

Reports live at:

```
docs/accord/reports/exec-<unit-id>.md
```

Use the approved unit ID from `plan.md`:

```
docs/accord/reports/exec-u-001-auth-login.md
```

## Minimum Contract

```
## Executed Unit
ID:
Summary:

## Summary of Changes
## Acceptance Evidence
## Verification Evidence
## Deviations / Surprises
## Suggested Plan Updates
```

### Acceptance Evidence

For each acceptance criterion in the unit, name where in the diff the criterion is satisfied — file paths, function names, behavior surfaced in tests. The reviewer reads this against the diff and `plan.md`'s `Current Approved Unit / Acceptance`. Vague claims ("auth flow now works") are insufficient for fresh-context review; concrete pointers ("`auth/login.ts:handleSubmit`; test in `auth/login.test.ts:happy_path`") are.

### Verification Evidence

Name the commands run, their outcomes, and any skipped checks with reasons. The reviewer should be able to re-run them. Use `commands.md` first, then `design.md` Verification Expectations, else infer and state the inference.

## Scale Up When

- the diff is broad
- the unit touches architecture, security, persistence, auth, concurrency, deployment, or data migration
- acceptance is partly subjective
- tests are missing or weak
- work deviates from the approved unit
- meaningful plan updates are proposed
- `Review mode: fresh-required`

Possible scale-up additions:

```
## Files Changed
## Commands Run
## Test Gaps
## Debt Accepted
## Design Questions
## Recovery Path
```

## Human Decision Points (during execute)

The agent stops when its judgment says the change is consequential. Examples:

- expanding scope beyond the approved unit
- changing design decisions
- adding consequential dependencies
- accepting meaningful debt
- weakening acceptance criteria
- choosing repair versus redo after a blocker

These are not a checklist; the agent applies judgment.

## LLM Discretion Zone

- implementation tactics within approved boundaries
- local refactors required by the unit
- test placement
- verification command ordering
- extra report detail when useful

## Completion

On approval:

- save the execution report
- update `docs/accord/accord-state.md`
- commit code, report, and state with explicit paths
- tag `accord-exec-<unit-id>`
