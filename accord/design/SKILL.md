---
name: design
description: Use this ACCORD skill when an approved intent exists and the human lead wants to codesign or revise architecture, boundaries, project commands, verification expectations, and consequential decisions. Triggers include "accord design", "draft the design", "revise architecture", "pivot design", or when implementation learning requires a new design version. This skill uses monotonic draft rounds, promotes an approved draft to docs/accord/design/design.md, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Design

Codesign architecture and consequential decisions with the human lead. Drafts carry proposed thinking. Canonical `design.md` is accepted by human approval; there is no separate ratify mode by default.

ACCORD assumes a capable LLM. Preserve VADER's useful design pressure while keeping the artifact lighter and independent of a fixed wave model.

Before doing anything else, read:

- `../references/design-schema.md`
- `../references/intent-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

## Operating Contract

1. Read `docs/accord/accord-state.md` if present.
2. Read canonical `docs/accord/intent/intent.md`.
3. Read current `docs/accord/design/design.md` if this is a revision.
4. If revising after implementation, read current `plan.md`, recent review/update log entries, execution reports, and inspect current implementation enough to avoid greenfield drift.
5. For brownfield projects, orient to existing code before drafting.
6. Find the highest existing `docs/accord/design/draft_NN.md`.
7. Create the next monotonic draft. Never overwrite.
8. Surface consequential human decisions; choose routine implementation conventions yourself.
9. On approval, promote the approved draft to `design.md`, update state, commit, and tag.

## Draft Rounds

Useful default draft structure:

```text
## Round Stance
## Design Brief
## Architecture Summary
## Boundaries and Ownership
## Key Interfaces
## Data and State
## Project Commands
## Verification Expectations
## Decisions
## Human Decisions Needed
## LLM Defaults Chosen
## Consider This
## Perspective I'm Contributing From
## Notes
```

Draft decisions are proposed thinking. Approved canonical decisions are accepted by definition.

## Canonical Artifact

On approval, promote into `docs/accord/design/design.md` using:

```text
## Architecture Summary
## Boundaries and Ownership
## Key Interfaces
## Data and State
## Project Commands
## Verification Expectations
## Decisions
## Handoff to Plan
```

Minimum decision entry:

```text
### D-001: <decision title>
Decision:
Rationale:
Consequences:
Revisability:
```

Add status, supersession, or evidence fields only when the project earns that detail.

## Scale-Up Triggers

Add detail when architecture choices are expensive to reverse, dependencies carry consequences, state ownership is unclear, persistence/auth/security/deployment matters, brownfield code conflicts with the design, or implementation learning invalidates prior decisions.

## Human Decisions

Ask for human judgment on durable architecture tradeoffs, dependencies with consequences, data model commitments, deployment, security posture, and accepted risk/debt.

Do not ask about conventional layout, local naming, routine tests, or ordinary adapter/glue patterns unless they have durable consequences.

## Preserve From VADER

- Brownfield orientation before architecture drafting.
- Explicit project commands.
- Durable decision records for consequential decisions.
- Consequences, including negatives, for material decisions.
- Refusal to over-commit to cheap-to-reverse details.
- Clear separation between design and code.

## Git

After approval, commit:

- `docs/accord/design/draft_NN.md`
- `docs/accord/design/design.md`
- `docs/accord/accord-state.md`

Use a `design:` commit prefix and tag `accord-design-v<N>`.
