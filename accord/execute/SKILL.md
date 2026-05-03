---
name: execute
description: Use this ACCORD skill when canonical intent, design, and plan artifacts exist and the human lead wants the current approved unit implemented. Triggers include "accord execute", "execute the current unit", "implement the approved unit", "build the next unit", or "go ahead" after an approved ACCORD plan. This skill writes code, writes docs/accord/reports/exec-<unit-id>.md using the approved u-NNN-slug ID, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Execute

Implement the current approved unit from `plan.md` and write a minimal execution report with enough evidence for `review-update`.

ACCORD assumes a capable LLM. Execute with professional judgment inside approved boundaries; stop for consequential changes.

At first use in a session/project, read:

- `../references/execution-report-schema.md`
- `../references/plan-schema.md`
- `../references/design-schema.md`
- `../references/commands-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

Re-read these references when schema behavior is uncertain or the files changed.

## Operating Contract

1. Read `docs/accord/accord-state.md`.
2. Read canonical `intent.md`, `design.md`, and `plan.md`.
3. Identify the current approved unit ID, acceptance criteria, verification expectations, expected scope, and review mode.
4. Inspect the repo enough to execute in the existing style.
5. If git is in use, inspect dirty files before editing. Continue around unrelated dirty files only when explicit path commits and verification remain safe; stop and ask when dirty files overlap the approved unit, affect verification, obscure the diff, or make explicit-path commits unsafe.
6. Implement the approved unit.
7. Run appropriate verification.
8. Write `docs/accord/reports/exec-<unit-id>.md`.
9. Ask for human approval of implementation and report.
10. Commit explicit paths and tag `accord-exec-<unit-id>` using the approved unit ID, including any repair/redo suffix.

## Stop For Human Approval

Stop before:

- expanding scope beyond the approved unit
- changing design decisions
- adding consequential dependencies
- accepting meaningful debt
- weakening acceptance criteria
- choosing repair versus redo after a blocker

Do not stop for routine implementation tactics inside the approved scope.

## Execution Report

Minimum report:

```text
## Executed Unit
## Summary of Changes
## Acceptance Evidence
## Verification Evidence
## Deviations / Surprises
## Suggested Plan Updates
```

Scale up the report when the diff is broad, risky, architecture-touching, security-sensitive, weakly tested, or deviates from the approved unit.

## Verification

Use `docs/accord/commands.md` first when present, then `design.md` Verification Expectations. If absent or incomplete, infer from project files and state the inference.

Record command-level evidence. If a relevant check is skipped, give a reason.

## Git

After approval, commit code changes, the execution report, `accord-state.md`, and `commands.md` if it changed, using explicit paths. Use an `exec:` prefix and tag `accord-exec-<unit-id>`.
