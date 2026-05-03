---
name: execute
description: Use this ACCORD skill when canonical intent, design, and plan artifacts exist and the human lead wants the current approved unit implemented. Triggers include "accord execute", "execute the current unit", "implement the approved unit", "build the next unit", or "go ahead". This skill writes code, writes docs/accord/reports/exec-<unit-id>.md using the approved u-NNN-slug ID, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Execute

Implement the current approved unit from `plan.md` and write a self-sufficient execution report.

## Posture

`execute` is **agent-led**. The agent implements with professional judgment inside approved boundaries. It stops only for genuinely consequential changes — the list below is examples of when to stop, not a checklist to traverse.

## At First Use In A Session

Read:

- `../references/execution-report-schema.md`
- `../references/plan-schema.md`
- `../references/design-schema.md`
- `../references/commands-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

## Operating Approach

1. Read `docs/accord/accord-state.md`.
2. Read canonical `intent.md`, `design.md`, `plan.md`.
3. Read `docs/accord/commands.md` if it exists. This is the source of truth for verification commands; do not paraphrase or guess if the file is present.
4. Identify the current approved unit ID, acceptance criteria, verification expectations, expected scope, and review mode.
5. Inspect the repo enough to execute in the existing style.
6. If git is in use, inspect dirty files. Continue around unrelated dirty files only when explicit-path commits and verification remain safe; stop and ask when dirty files overlap the approved unit, affect verification, obscure the diff, or make explicit-path commits unsafe.
7. Implement the approved unit.
8. Run appropriate verification (use `commands.md` first, then `design.md` Verification Expectations, else infer and state the inference).
9. Write `docs/accord/reports/exec-<unit-id>.md` as a self-sufficient report (see below).
10. Ask for human approval; advise consequential vs procedural.
11. Commit explicit paths and tag `accord-exec-<unit-id>` using the approved unit ID, including any repair/redo suffix.

## Stop For Human Approval — Examples

The agent stops when its judgment says the change is consequential. Examples:

- expanding scope beyond the approved unit
- changing design decisions
- adding consequential dependencies
- accepting meaningful debt
- weakening acceptance criteria
- choosing repair versus redo after a blocker

These are not a checklist; the agent applies judgment. Routine implementation tactics inside approved scope do not require stopping.

## The Report Is Load-Bearing

The execution report is the executor's only narrative to the reviewing agent and must satisfy principle 9.

For each acceptance criterion, name where in the diff it is satisfied — file paths, function names, test names. Vague claims ("auth works") fail review; concrete pointers ("`auth/login.ts:handleSubmit`; test: `auth/login.test.ts:happy_path`") succeed.

For verification, name commands run and outcomes. The reviewer should be able to re-run them.

See `references/execution-report-schema.md` for the contract.

## Approval Advisory

At the execute gate, advise whether the unit is procedural (clean implementation, evidence aligned) or consequential (deviations, accepted debt, design questions). For `fresh-required` units, the gate is more often consequential.

## Git

After approval, commit code changes, the execution report, `accord-state.md`, and `commands.md` if changed, using explicit paths. Use an `exec:` prefix and tag `accord-exec-<unit-id>`.
