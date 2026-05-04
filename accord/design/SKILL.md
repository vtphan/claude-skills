---
name: design
description: Use this ACCORD skill when an approved intent exists and the human lead wants to codesign architecture, boundaries, UI/UX, project commands, verification expectations, and consequential decisions. Triggers include "accord design", "draft the design", "revise architecture", or "pivot design". This skill uses ACCORD codesign discipline in a single draft file, promotes an approved draft to docs/accord/design.md, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Design

Codesign architecture, UI/UX, and consequential decisions with the human lead. Drafts carry proposed thinking. Canonical `design.md` is accepted by human approval.

## Posture

The agent's posture is **elicitive and generative** (same as intent). For design, this especially applies to:

- architectural alternatives and tradeoffs
- dependency and platform choices
- boundary and ownership reframings
- **UI/UX**: interaction model, information architecture, accessibility, error/empty/loading states. The agent proposes these rather than waiting to be asked. UI/UX is part of design, not an afterthought.

Codesign discipline applies (Draft Stance block, default away from `refine`, critique pass before declaring `ready`, framing changes named explicitly, self-contained drafts). See `../references/draft-conventions.md`.

## At First Use In A Session

Read:

- `../references/draft-conventions.md`
- `../references/design-schema.md`
- `../references/intent-schema.md`
- `../references/commands-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

Re-read when schema behavior is uncertain or files changed.

## Operating Approach

1. Read `docs/accord/accord-state.md` if present.
2. Read canonical `docs/accord/intent.md`.
3. Read current `docs/accord/design.md` if revising.
4. If revising mid-project, also read current `plan.md`, recent review/update entries, execution reports, and inspect implementation enough to avoid greenfield drift.
5. Open `docs/accord/design-draft.md`. Overwrite freely. If `design.md` already exists, seed fresh content from the canonical artifact and the inputs above.
6. Each draft is self-contained; place a Draft Stance block at the top per `../references/draft-conventions.md`. Apply the elicitive/generative posture; treat UI/UX with the same rigor as architecture.
7. Run at least one critique-stance pass before declaring stance `ready`.
8. On approval, strip the Draft Stance block, write the cleaned content as `design.md`, update state, commit, and tag.

## Consider This Tagging

Three tags: `[from user]`, `[Q from LLM]`, `[suggestion from LLM]`. See `draft-conventions.md`.

## Approval Advisory

At each approval gate, advise whether consequential or procedural. Design gates are usually consequential (architecture, dependencies, UI commitments) — say so directly.

## Canonical Artifact

On approval, promote into `docs/accord/design.md` per the schema in `references/design-schema.md`. The canonical artifact must satisfy principle 9 (cross-LLM handoff): an unfamiliar reviewing agent verifies implementation against this file alone.

Use `docs/accord/commands.md` for concrete project commands. `design.md` may summarize verification strategy and reference `commands.md`. Routine command changes should not force a new design version.

Decision entries record consequential choices; tactical choices stay out of decision records.

## Scale Up

See `references/design-schema.md` Scale Up When.

## Git

The framework requires only the promotion commit. Mid-iteration commits, if any, are operator-discretion.

After approval, commit:

- `docs/accord/design-draft.md` (as it sat at promotion)
- `docs/accord/design.md`
- `docs/accord/commands.md` when created or changed
- `docs/accord/accord-state.md`

Use a `design:` commit prefix and tag `accord-design-v<N>`.
