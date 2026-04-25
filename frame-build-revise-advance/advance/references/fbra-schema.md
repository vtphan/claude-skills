# FBRA Wave Doc Schema

This schema supports a one-human, one-smart-LLM workflow:

- `frame` discovers and finalizes the brief, then creates or reshapes the wave doc.
- `build` implements the active wave.
- `revise` reviews the active wave against the build, codebase, verification, and human feedback; recommends material corrections; and applies approved revisions while the wave stays active.
- `advance` closes a done wave, recommends material closeout or next-wave choices when needed, and activates exactly one next wave.

The wave doc is a steering surface, not a compliance artifact. Keep it short enough that the human will actually read it.

The working brief is the discovery artifact. The wave doc is the execution artifact derived from the finalized brief.

When commits are permitted, the wave doc and commit messages together form an explainable implementation history. Stable requirement IDs let agents, humans, and later auditors trace work from intent to code to verification.

## File

Use one markdown file per project, usually `docs/<project-slug>-waves.md`.

```yaml
---
wave_doc_version: 1
created: 2026-04-24
last_updated: 2026-04-24
current_wave: W1
status: active
---
```

## Required Sections

```markdown
# <Project> - Waves

## Goal
## Operating Rules
## Must-Have Map
## Waves
## Decisions
## Notes
```

## Goal

One to three paragraphs describing the product goal, intended users, and explicit non-goals.

## Operating Rules

Short project-wide rules for the LLM:

- Implementation freedom: what the LLM may decide independently.
- Decision boundary: when the LLM must ask the human.
- Verification bar: what must be tested or demonstrated before work is called done.
- Decision guidance: how the LLM frames informed options and recommendations for the human.

Default decision boundary:

> The LLM may choose implementation details that are local, reversible, and consistent with existing patterns. Ask before changing product scope, data model, architecture, external services, auth/security behavior, pricing/billing behavior, or user-visible workflow assumptions.

Default decision guidance:

> When asking the human to decide, present 2-3 informed options with tradeoffs and a recommendation. For stack, architecture, persistence, auth/security, deployment, and integrations, evaluate convention density, LLM-buildability, reversibility, verification impact, dependency risk, security blast radius, operational burden, and fit to active-wave scope.

Default verification bar:

> Verify every active-wave must-have requirement with the cheapest credible automated test, scripted check, or manual demo. Run relevant existing tests. Report anything not verified.

## Must-Have Map

A concise system-vision map showing where each must-have will be addressed. Keep this short enough to scan.

```markdown
| Must-have | Why it matters | Addressed in | Notes |
|---|---|---|---|
| W1-MH1: ... | ... | W1 | ... |
```

Rules for the map:

- Every must-have should map to at least one wave, be marked deferred, or be marked as an open decision.
- W1 should include only the must-haves needed for a credible first slice.
- Later waves may address must-haves at a high level until they become active.
- If a wave does not address any must-have, question whether it belongs.

## Wave Sizing

Prefer the fewest waves that preserve clear scope, verification, and auditability. Add waves when a capability, risk boundary, dependency, or human review checkpoint would otherwise be buried inside an oversized wave.

Avoid speculative roadmap detail. Later inactive waves may stay broad until they become active.

## Stable IDs

Use stable IDs for active-wave must-have requirements:

```markdown
- W<N>-MH<K>: <requirement>
```

Use optional IDs for nice-to-haves when they may be referenced by commits or handoffs:

```markdown
- W<N>-NH<K>: <nice-to-have>
```

Rules:

- `frame` assigns IDs when a wave becomes active.
- IDs are stable once assigned. Do not renumber after edits.
- If a requirement is split, keep the old ID as superseded and create new IDs.
- If a requirement is dropped or deferred, record that explicitly; do not delete it silently.
- Commits, verification notes, revise findings, and done-wave summaries should reference IDs where practical.
- Keep IDs focused on requirements and optionally nice-to-haves. Do not ID every task unless the project needs that level of tracking.

## Waves

Each wave has exactly one state:

- `inactive` - future direction, concise.
- `active` - current build scope, detailed enough for execution.
- `done` - completed summary.

Normal state: exactly one wave is `active`. Transitional states may briefly have zero active waves before the first wave is framed, after the project is complete, while the human is reorganizing the doc, or during a deliberate pause. Never have more than one active wave.

### Inactive Wave

```markdown
### W<N> - <Name>
Status: inactive
Goal: One sentence.

Must-have stories:
- ...

Must-have features:
- ...

Notes:
- Optional constraints, dependencies, or known questions.
```

Inactive waves do not have tasks, detailed implementation plans, formal acceptance criteria, or verification commands.

### Active Wave

```markdown
### W<N> - <Name>
Status: active
Goal: One sentence.

Must-have requirements:
- W<N>-MH1: ...

Nice-to-have:
- W<N>-NH1: ...

Implementation notes:
- Existing patterns, constraints, or guidance the LLM should respect.

Tasks:
- [ ] ...

Decisions needed:
- None currently, or use `references/decision-guidance-contract.md` to frame each decision.

Verification:
- Automated: ...
- Manual/demo: ...
- Commands: ...
```

Rules for active waves:

- Must-have requirements are binding. If unmet, the wave is not done.
- Nice-to-have items are optional and must not distort the wave.
- Tasks may be adjusted by the LLM while building if the requirements stay stable.
- The LLM must ask before crossing the decision boundary.
- Verification must be credible, not necessarily exhaustive.

### Done Wave

```markdown
### W<N> - <Name>
Status: done
Completed: 2026-04-24

Delivered:
- W<N>-MH1: ...

Stories completed:
- ...

Features completed:
- ...

Decisions established:
- ...

Follow-up notes:
- ...
```

Done waves keep only durable project memory. Remove task-level detail unless it matters later.

## Decisions

Use this as a compact decision log. Add only decisions that future work should respect.

```markdown
- 2026-04-24 - Use SQLite for local persistence because deployment is single-user and local-first.
```

Do not turn this into a full architecture decision record system unless the project needs it.

## Decision Guidance

When a skill asks the human for a decision, use `references/decision-guidance-contract.md`.

The human should receive informed choices, not an open-ended question. Recommendations should account for implementation by a smart LLM such as Claude Code or Codex. For important decisions, especially tech stack and architecture, discuss convention density, LLM-buildability, testability, reversibility, dependency risk, security blast radius, operational burden, and active-wave fit.

## Notes

Use for open questions, deferred ideas, and things that belong to the product vision but are not yet waved.

## Explainable Implementation History

When commits are permitted, use `references/commit-message-contract.md`.

The trace should be:

```text
Must-have ID -> task(s) -> commit(s) -> verification receipt -> done-wave summary
```

The wave doc is part of the implementation record. Material changes to it should be committed when commits are permitted, or the human should be asked whether to commit them. Material changes include requirement IDs/text, task completion, decisions, verification status, deferrals, drops, supersessions, and wave-state transitions.

Git already records changed files; commit messages should emphasize intent, affected behavior, relevant surfaces, and verification receipts.

## Invariants

1. Keep exactly one active wave during normal Build/Revise/Advance work. Zero active waves is only a transitional state. Never have more than one active wave.
2. Inactive waves stay concise.
3. The Must-Have Map stays concise and maps each must-have to a wave, deferred status, or open decision.
4. Active waves include must-have requirements and verification.
5. Done waves summarize shipped capability and durable decisions.
6. The LLM asks before crossing the decision boundary.
7. If verification was not run or did not pass, say so plainly.
8. Active-wave must-have requirements have stable IDs.
9. Material wave-doc changes are committed when commits are permitted, or the human is asked whether to commit them.
10. Human-facing decision asks include informed options, tradeoffs, and a recommendation.
