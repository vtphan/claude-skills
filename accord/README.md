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

## Artifacts

Default project artifact layout:

```text
docs/accord/
  accord-state.md
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
- `references/intent-schema.md`
- `references/design-schema.md`
- `references/plan-schema.md`
- `references/execution-report-schema.md`
- `references/git-conventions.md`

These references define minimum contracts and scale-up triggers. They are not exhaustive templates.
