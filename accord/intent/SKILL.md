---
name: intent
description: Use this ACCORD skill when the human lead wants to codesign or revise project intent. Triggers include "accord intent", "draft project intent", "revise intent", or "pivot intent". This skill uses ACCORD codesign discipline in a single draft file, promotes an approved draft to docs/accord/intent.md, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Intent

Codesign the project's intent with the human lead. Use the single draft file as a working scratchpad for collaborative thinking, then promote the approved draft into a clean canonical `docs/accord/intent.md`.

## Posture

The agent's posture is **elicitive and generative**. Draw out aspects of the project the human hasn't articulated (stakeholders, success states, implicit non-goals, domain constraints). Propose transformative alternatives the human can absorb, redirect, or reject. Sycophantic refinement is the failure mode to avoid.

The codesign discipline (Draft Stance block, default away from `refine`, critique pass before declaring `ready`, framing changes named explicitly, self-contained drafts) is the guardrail against premature consensus. See `../references/draft-conventions.md` for the full discipline.

## At First Use In A Session

Read:

- `../references/draft-conventions.md`
- `../references/intent-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

Re-read when schema behavior is uncertain or files changed.

## Operating Approach

1. Read current ACCORD state if `docs/accord/accord-state.md` exists.
2. Open `docs/accord/intent-draft.md`. Overwrite freely. If `intent.md` already exists, the new draft is a proposed revision — seed fresh content from the canonical artifact.
3. Each draft is self-contained; place a Draft Stance block at the top per `../references/draft-conventions.md`. Apply the elicitive/generative posture.
4. Run at least one critique-stance pass before declaring stance `ready` (recorded in `Stances applied so far`).
5. Surface consequential human decisions; make routine choices independently.
6. On approval, strip the Draft Stance block, write the cleaned content as `intent.md`, update `accord-state.md`, commit, and tag.

## Consider This Tagging

`Consider This` carries three kinds of items:

- `[from user]` — user contributions and corrections.
- `[Q from LLM]` — questions about ambiguity in the user's input.
- `[suggestion from LLM]` — proactive transformative proposals.

If a `[suggestion from LLM]` item implies the Idea itself was misframed, surface that as `[Q from LLM]` instead, and if the human accepts the reframing, name the change explicitly in the next draft's Draft Stance block (`Framing change` line).

## Approval Advisory

At each approval gate, advise whether the moment is consequential (real choice for the human) or procedural (rubber stamp; here is what changed). Most intent gates are consequential by nature; say so directly when they are.

## Cross-LLM Handoff

The promotion step enforces principle 9: the canonical `intent.md` is a clean rewrite, not draft scaffolding.

## Scale Up

See `references/intent-schema.md` Scale Up When. The agent uses judgment about depth.

## Git

The framework requires only the promotion commit. Mid-iteration commits, if any, are operator-discretion.

After approval, commit:

- `docs/accord/intent-draft.md` (as it sat at promotion)
- `docs/accord/intent.md`
- `docs/accord/accord-state.md`

Use an `intent:` commit prefix and tag `accord-intent-v<N>`. If git is unavailable, save artifacts and tell the human that recovery and review have a weaker baseline.
