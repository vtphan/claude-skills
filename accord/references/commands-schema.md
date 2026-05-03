# ACCORD Commands Contract

`docs/accord/commands.md` records project commands used by ACCORD skills for setup, run, test, lint, typecheck, build, and repro checks.

This file prevents routine command drift from forcing a new `design.md` version. `design.md` should reference `commands.md` for operational commands. Bump `design.md` only when command changes reflect a material architecture or verification-strategy change.

`commands.md` must satisfy principle 9 (cross-LLM handoff): a reviewing agent re-runs verification from this file alone.

## Minimum Contract

```
## Setup
## Run
## Test
## Lint / Typecheck
## Build
## Repro / Demo
## Notes
```

Use `n/a` with a reason when a category does not apply.

## Update Rules

- `design` creates the initial `commands.md` when commands are known.
- `execute` may update `commands.md` when implementation changes project commands as part of the approved unit.
- `review-update` may update `commands.md` when review verifies that command documentation drifted.
- The human lead may edit `commands.md` directly between approved units; commit with a `commands:` prefix or fold the edit into the next unit's commit.
- Tactical command updates do not require `accord-design-v<N>`.
- Material changes to architecture, deployment, or verification strategy should still route through `design`.

## Human Decision Points

Ask the human when a command change implies a new dependency, deployment model, CI requirement, or quality gate.

Do not ask for mechanical command-name updates that follow directly from accepted project changes.

## Before Approval Checklist

- Can a fresh agent set up, run, test, lint/typecheck, build, and demo or reproduce from this file alone?
- Does each non-applicable category say `n/a` with a reason?
- Are command changes tactical, or do they imply a design-level change that should route through `design`?
- Are environment assumptions, generated artifacts, or known command limitations recorded in `Notes`?
