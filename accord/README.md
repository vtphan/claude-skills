# ACCORD

ACCORD is a lightweight software development process for a human lead working with a capable LLM. It assumes the LLM can codesign, plan, implement, review, and update plans with good judgment. The process supplies enough structure for handoff, approval, verification, commits, and cross-conversation continuity without forcing a fixed work shape.

Core principle:

**Use schemas to protect handoffs, not to micromanage thought.**

## Skills

ACCORD uses five terse skills:

1. `intent` - codesign project intent.
2. `design` - codesign architecture and consequential decisions.
3. `plan` - choose an adaptive plan shape and approve the next executable unit.
4. `execute` - implement the approved unit and write an execution report.
5. `review-update` - verify execution and update `plan.md`.

The human lead invokes each skill manually. Skills do not auto-invoke the next skill. Continuity comes from canonical artifacts, `accord-state.md`, commits, and tags.

## Fit

ACCORD is optional. Use it when a project benefits from explicit human-LLM codesign, durable planning artifacts, and reviewable execution boundaries. Do not bootstrap ACCORD for work whose coordination cost exceeds the value, such as a single trivial edit, throwaway experiment, or change that is already obvious and low-risk outside an ACCORD-managed project.

## Artifacts

Default project artifact layout:

```text
docs/accord/
  accord-state.md
  commands.md
  intent/
    draft_00.md
    intent.md
  design/
    draft_00.md
    design.md
  plan/
    draft_00.md
    plan.md
  reports/
    exec-<unit-id>.md
```

`intent`, `design`, and `plan` use monotonic `draft_NN.md` sequences for human-LLM co-design. Drafts contain proposed thinking. Human approval promotes a draft into the canonical artifact. The canonical artifact is the accepted baseline.

`execute` writes execution reports. `review-update` writes review findings and plan changes into `plan.md` by default.

## Small Work

ACCORD supports a small-work path for trivial or low-risk changes. The human lead may skip `intent` and `design` when current project direction and architecture are irrelevant to the change.

Use this pattern:

- `plan`: set `Plan Shape` to `one-shot` and define one small approved unit.
- `execute`: implement the unit and write a minimal execution report.
- `review-update`: verify, update `plan.md`, and tag the result.

This path is for typo fixes, one-file bugs, docs adjustments, or tightly bounded maintenance. Do not use it when the change touches architecture, security, persistence, deployment, broad behavior, or unclear requirements.

Small Work assumes ACCORD is already initialized on the project. Do not bootstrap ACCORD for a single trivial change.

## Unit IDs

Use stable unit IDs in `plan.md` and tags:

```text
u-001-auth-login
u-002-profile-cache
u-003-docs-typos
```

Do not reuse unit IDs. If work is repaired or redone, use suffixes such as `u-001-auth-login-r02` or `u-001-auth-login-repair-01`.

## Versioning

Approved phase boundaries are committed and tagged:

- `accord-intent-v1`
- `accord-design-v1`
- `accord-plan-v1`
- `accord-exec-<unit-id>`
- `accord-review-<unit-id>`

Canonical artifacts do not carry change logs by default. Version history lives in git commits and tags. `plan.md` is the exception: its `Review and Update Log` is operational project state, not generic artifact history.

## References

Each skill reads the focused reference contracts it needs:

- `references/state-schema.md`
- `references/commands-schema.md`
- `references/draft-conventions.md`
- `references/intent-schema.md`
- `references/design-schema.md`
- `references/plan-schema.md`
- `references/execution-report-schema.md`
- `references/git-conventions.md`

These references define minimum contracts and scale-up triggers. They are not exhaustive templates.

## Reference Read Policy

Skills should read their reference files at first use in a session or when schema behavior is uncertain. They do not need to reread unchanged references on every invocation if the same agent session has already loaded them and the user is continuing the same ACCORD project.

## Scope Assumption

ACCORD v1 assumes one current approved unit at a time. Parallel work is possible by using separate branches and distinct unit IDs, but the core state file remains serial. If a project needs sustained parallel tracks, scale up the state and plan contracts before running parallel execution.

## Completion

For discrete projects, `review-update` may close the project when no next unit remains. Set `accord-state.md` status to `complete`, add a final entry to `plan.md`, commit with `review: complete ACCORD project`, and tag `accord-complete-v1`.
