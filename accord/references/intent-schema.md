# ACCORD Intent Contract

`intent` codesigns project intent with the human lead. Draft rounds support thinking; canonical `intent.md` supports downstream design and planning.

## Draft Rounds

Use one monotonic draft sequence in `docs/accord/intent/`:

```text
draft_00.md
draft_01.md
intent.md
draft_02.md
```

Drafts are never overwritten. A draft after `intent.md` is a proposed revision. It becomes accepted only when promoted, committed, and tagged.

Drafts should borrow the `brainstorm-this` pattern: round stance, protected project frame, user signal, open questions, and sparse notes. The exact draft shape may adapt, but it should preserve the user's core framing unless the human explicitly approves a revision.

## Minimum Canonical Contract

`intent.md` must include:

```text
## Goal
## Users / Operators
## Success Criteria
## Non-Goals
## Constraints
## Open Questions
## Handoff to Design
```

Optional when useful:

```text
## Context
## Risks
## Prior Art
## Glossary
```

## Scale Up When

- the value hypothesis is vague
- multiple users/operators have conflicting needs
- non-goals are unclear
- success criteria are not testable
- brownfield code constrains intent
- the human lead expresses uncertainty or disagreement
- later implementation invalidates accepted intent

## Human Decision Points

- goal and priority
- users/operators
- success criteria
- non-goals
- constraints
- acceptable risk and quality bar

## LLM Discretion Zone

- wording
- grouping
- obvious implications
- draft organization
- candidate open questions
- concise handoff wording

## Preserve From VADER

- pressure-test the value hypothesis
- make non-goals load-bearing
- orient to existing code in brownfield projects
- keep canonical intent short
- surface open questions instead of hiding uncertainty

## Promotion

On approval:

- promote the approved draft into `docs/accord/intent/intent.md`
- do not include a canonical change log
- update `docs/accord/accord-state.md` with source draft and tag
- commit explicit paths
- tag `accord-intent-v<N>`
