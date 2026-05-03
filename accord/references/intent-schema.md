# ACCORD Intent Contract

`intent` codesigns project intent with the human lead. Draft rounds support thinking; canonical `intent.md` supports downstream design and planning.

## Posture

The agent's posture is **elicitive and generative**: drawing out aspects of the project the human hasn't articulated yet (stakeholders, success states, implicit non-goals, domain constraints), and proposing transformative alternatives the human can absorb, redirect, or reject. Sycophantic refinement is the failure mode to avoid.

The brainstorm-this discipline (round stances, immutable Idea after round 0, two-small-diff convergence with at least one verified critique pass, strict draft non-overwrite) protects against premature consensus. See `draft-conventions.md`.

## Draft Rounds

Use one monotonic draft sequence in `docs/accord/intent/`:

```
draft_00.md
draft_01.md
intent.md
draft_02.md
```

Drafts are never overwritten. A draft after `intent.md` is a proposed revision. It becomes accepted only when promoted, committed, and tagged.

`Consider This` uses three-tag convention: `[from user]`, `[Q from LLM]`, `[suggestion from LLM]`. See `draft-conventions.md`.

## Minimum Canonical Contract

`intent.md` must include:

```
## Goal
## Users / Operators
## Success Criteria
## Non-Goals
## Constraints
## Open Questions
## Handoff to Design
```

Optional when useful: `## Context`, `## Risks`, `## Prior Art`, `## Glossary`.

`intent.md` must be self-sufficient for cross-LLM handoff (principle 9). A future agent reading it cold should understand the project's direction without conversational context from the codesign session.

## Scale Up When

- the value hypothesis is vague
- multiple users/operators have conflicting needs
- non-goals are unclear
- success criteria are not testable
- the human lead expresses uncertainty or disagreement
- mid-project implementation invalidates accepted intent

## Human Decision Points

- goal and priority
- users / operators
- success criteria
- non-goals
- constraints
- acceptable risk and quality bar

## LLM Discretion Zone

- wording and grouping
- candidate open questions
- candidate `[suggestion from LLM]` items
- draft organization
- concise handoff wording

## Promotion

On approval:

- promote the approved draft into `docs/accord/intent/intent.md`
- update `docs/accord/accord-state.md` with source draft and tag
- commit explicit paths
- tag `accord-intent-v<N>`
