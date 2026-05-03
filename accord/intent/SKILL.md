---
name: intent
description: Use this ACCORD skill when the human lead wants to codesign or revise project intent. Triggers include "accord intent", "draft project intent", "revise intent", or "pivot intent". This skill uses ACCORD codesign draft rounds, promotes an approved draft to docs/accord/intent/intent.md, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Intent

Codesign the project's intent with the human lead. Use codesign draft rounds for collaborative thinking, then promote the approved draft into a clean canonical `docs/accord/intent/intent.md`.

## Posture

The agent's posture is **elicitive and generative**. Draw out aspects of the project the human hasn't articulated (stakeholders, success states, implicit non-goals, domain constraints). Propose transformative alternatives the human can absorb, redirect, or reject. Sycophantic refinement is the failure mode to avoid.

The codesign discipline (round stances, immutable Idea after round 0, two-small-diff convergence with at least one verified critique pass, strict draft non-overwrite) is the guardrail against premature consensus. See `../references/draft-conventions.md` for the full discipline.

## At First Use In A Session

Read:

- `../references/draft-conventions.md`
- `../references/intent-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

Re-read when schema behavior is uncertain or files changed.

## Operating Approach

The agent uses judgment about round mechanics. Expected behavior:

1. Read current ACCORD state if `docs/accord/accord-state.md` exists.
2. Find the highest existing `docs/accord/intent/draft_NN.md` and create the next monotonic draft. Never overwrite.
3. Apply the codesign draft structure (see `../references/draft-conventions.md`), with the elicitive/generative posture.
4. Surface consequential human decisions; make routine choices independently.
5. On approval, promote the approved draft to `intent.md`, update `accord-state.md`, commit, and tag.

## Consider This Tagging

`Consider This` carries three kinds of items:

- `[from user]` — user contributions and corrections.
- `[Q from LLM]` — questions about ambiguity in the user's input.
- `[suggestion from LLM]` — proactive transformative proposals.

If a `[suggestion from LLM]` item implies the Idea itself was misframed, surface that as `[Q from LLM]` instead. The Idea is immutable after round 0.

## Approval Advisory

At each approval gate, advise whether the moment is consequential (real choice for the human) or procedural (rubber stamp; here is what changed). Most intent gates are consequential by nature; say so directly when they are.

## Cross-LLM Handoff

`intent.md` must be self-sufficient (principle 9). A future agent reading it cold — in a fresh conversation, possibly with a different LLM — should understand the project's direction without conversational context. The promotion step is where this gets enforced: the canonical artifact is a clean rewrite, not draft scaffolding.

## Scale Up

See `references/intent-schema.md` Scale Up When. The agent uses judgment about depth.

## Git

After approval, commit:

- `docs/accord/intent/draft_NN.md`
- `docs/accord/intent/intent.md`
- `docs/accord/accord-state.md`

Use an `intent:` commit prefix and tag `accord-intent-v<N>`. If git is unavailable, save artifacts and tell the human that recovery and review have a weaker baseline.
