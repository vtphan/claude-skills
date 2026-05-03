# ACCORD Execution Report Contract

`execute` writes an execution report for the approved unit. The report should provide enough evidence for `review-update` to verify what happened. It should not become a heavyweight audit template by default.

Reports live at:

```text
docs/accord/reports/exec-<unit-id>.md
```

Use the approved unit ID from `plan.md`, such as:

```text
docs/accord/reports/exec-u-001-auth-login.md
```

## Minimum Contract

```text
## Executed Unit
ID:
Summary:

## Summary of Changes
## Acceptance Evidence
## Verification Evidence
## Deviations / Surprises
## Suggested Plan Updates
```

## Scale Up When

- the diff is broad
- the unit touches architecture, security, persistence, auth, concurrency, deployment, or data migration
- acceptance is partly subjective
- tests are missing or weak
- work deviates from the approved unit
- meaningful plan updates are proposed
- a fresh-context review is likely

Possible scale-up additions:

```text
## Files Changed
## Commands Run
## Test Gaps
## Debt Accepted
## Design Questions
## Recovery Path
```

## Human Decision Points

- scope expansion
- design change
- dependency addition with consequences
- accepted debt
- weakened acceptance
- repair versus redo when blocked

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
