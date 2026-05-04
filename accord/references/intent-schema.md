# ACCORD Intent Contract

`intent` codesigns project intent with the human lead. The single draft supports thinking; canonical `intent.md` supports downstream design and planning.

## Posture

The agent's posture is **elicitive and generative**: drawing out aspects of the project the human hasn't articulated yet (stakeholders, success states, implicit non-goals, domain constraints), and proposing transformative alternatives the human can absorb, redirect, or reject. Sycophantic refinement is the failure mode to avoid.

The codesign discipline (Draft Stance block, default away from `refine`, critique pass before declaring `ready`, framing changes named explicitly, self-contained drafts) protects against premature consensus. See `draft-conventions.md`.

## Draft

Use a single draft file:

```
docs/accord/intent-draft.md
docs/accord/intent.md
```

`intent-draft.md` is overwritten freely as work progresses. The draft moves forward only — it always holds the current best thinking. After `intent.md` is promoted, opening a fresh `intent-draft.md` later is a proposed revision; it becomes accepted only when promoted, committed, and tagged.

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

`intent.md` must satisfy principle 9 (cross-LLM handoff): the artifact alone conveys project direction.

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

- strip the Draft Stance block and any `Consider This` scaffolding from `docs/accord/intent-draft.md`; write the cleaned content as `docs/accord/intent.md`
- update `docs/accord/accord-state.md`
- commit explicit paths
- tag `accord-intent-v<N>`

## Before Approval Checklist

- Does `Goal` name the actual project direction, not just the next implementation task?
- Are `Users / Operators`, `Success Criteria`, `Non-Goals`, and `Constraints` concrete enough for design to make tradeoffs?
- Are success criteria observable or testable enough to guide later review?
- Are open questions limited to issues that can remain open without blocking design?
- Does `Handoff to Design` tell the next agent what design must preserve or decide?
