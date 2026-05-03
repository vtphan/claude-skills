---
name: intent
description: Use this ACCORD skill when the human lead wants to codesign or revise project intent before architecture/design work. Triggers include "accord intent", "draft project intent", "revise intent", "pivot intent", or when a project needs a lightweight approved intent artifact for downstream design and planning. This skill uses monotonic draft rounds, promotes an approved draft to docs/accord/intent/intent.md, updates accord-state.md, then commits and tags after human approval.
---

# ACCORD Intent

Codesign the project's intent with the human lead. Use draft rounds for collaborative thinking, then promote the approved draft into a clean canonical `docs/accord/intent/intent.md`.

ACCORD assumes a capable LLM. Use the schema to protect handoff to `design`, not to micromanage the conversation.

At first use in a session/project, read:

- `../references/draft-conventions.md`
- `../references/intent-schema.md`
- `../references/state-schema.md`
- `../references/git-conventions.md`

Re-read these references when schema behavior is uncertain or the files changed.

## Operating Contract

1. Read current ACCORD state if `docs/accord/accord-state.md` exists.
2. Detect whether this is initial intent drafting or a revision after prior approval.
3. For brownfield projects, briefly orient to existing code before drafting.
4. Find the highest existing `docs/accord/intent/draft_NN.md`.
5. Create the next monotonic draft. Never overwrite.
6. Treat user edits and comments as high-priority signal.
7. Surface consequential human decisions; make obvious LLM-owned choices without burdening the human.
8. When the human approves, promote the approved draft to `intent.md`.
9. Update `accord-state.md`.
10. Commit explicit paths and tag `accord-intent-v<N>` after approval.

## Draft Rounds

Drafts should include enough structure to support codesign. A useful default:

```text
## Round Stance
## Project Frame
## Goal
## Users / Operators
## Success Criteria
## Non-Goals
## Constraints
## Open Questions
## Human Decisions Needed
## LLM Defaults Chosen
## Consider This
## Perspective I'm Contributing From
## Notes
```

After the first draft, do not casually rewrite `Project Frame`. If the frame appears wrong, ask or propose a human-approved revision.

## Canonical Artifact

On approval, promote into `docs/accord/intent/intent.md` using the minimum canonical contract:

```text
## Goal
## Users / Operators
## Success Criteria
## Non-Goals
## Constraints
## Open Questions
## Handoff to Design
```

Add optional sections only when they help downstream work.

## Scale-Up Triggers

Add more structure or ask more questions when:

- the value hypothesis is vague
- users/operators conflict
- non-goals are weak
- success criteria are not testable
- brownfield code constrains intent
- the human lead expresses uncertainty
- implementation learning invalidates accepted intent

## Human Decisions

Ask for human judgment on goal, users/operators, success criteria, non-goals, constraints, and risk/quality bar.

Do not ask for routine wording, grouping, or schema mechanics unless the choice changes meaning.

## Git

After approval, commit:

- `docs/accord/intent/draft_NN.md`
- `docs/accord/intent/intent.md`
- `docs/accord/accord-state.md`

Use an `intent:` commit prefix and tag `accord-intent-v<N>`. If git is unavailable, save the artifacts and tell the user the baseline is weaker.
