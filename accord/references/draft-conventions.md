# ACCORD Draft Conventions

`intent`, `design`, and `plan` each use a single draft file as a working scratchpad during codesign or planning. The draft is for thinking; the canonical artifact is for downstream use. Drafts move forward only — the current draft is the current best thinking.

## File Layout

Each phase has exactly two files at the top of `docs/accord/`:

```
docs/accord/intent-draft.md      docs/accord/intent.md
docs/accord/design-draft.md      docs/accord/design.md
docs/accord/plan-draft.md        docs/accord/plan.md
```

The draft is overwritten freely as work progresses. The canonical artifact is promoted from the draft on approval.

## Self-Contained Drafts

Each draft is self-contained: full framing, full content, no carried-forward "see earlier round." A reader gets the complete current best thinking from the draft alone — same quality bar as the canonical artifact (principle 9).

The draft is not designed for round-by-round comparison. It always holds the current best version. If a prior idea is reintroduced, it is because the agent or human brings it forward into the current draft, not because anyone diffed against history.

## Codesign Discipline

`intent` and `design` use a strict codesign discipline that prevents premature consensus and sycophantic refinement. The discipline operates on the current draft, not on a sequence of rounds.

### Draft Stance Block

Each draft opens with a short markdown block declaring the agent's posture:

```
**Draft Stance**
- Stance: [refine | expand | critique | subtract | restructure | ask | ready]
- Perspective I'm adopting: [one phrase]
- Stances applied so far: [comma-separated list, including this one]
- Framing change: [none | one sentence describing what about the framing changed and why]
- Recommendation: [continue | propose for promotion]
```

### Stance Vocabulary

- `refine` — tighten the existing content
- `expand` — add a dimension, alternative, or consideration that's missing
- `critique` — adopt a skeptical perspective and surface weaknesses, gaps, failure modes
- `subtract` — remove weak arguments, redundant points, or scope creep
- `restructure` — reorganize the logic when the current shape isn't serving the work
- `ask` — surface a question whose answer would meaningfully change the next revision
- `ready` — declare the draft ready for promotion

Default toward `expand`, `critique`, or `subtract` rather than `refine`. Sycophantic refinement is the failure mode to avoid.

### Critique Pass Before Ready

The agent may declare stance `ready` only if `critique` appears in `Stances applied so far`. The check is self-reported in the current draft's stance block; the human verifies by reading the block and judging whether the named critique was substantive (not perfunctory).

If `Stances applied so far` does not include `critique`, the agent must run a critique-stance pass first.

### Framing Changes Are Explicit

If the current draft changes the framing (Idea for intent, Design Brief for design — including goal, scope, central premise), the `Framing change` line must name what changed and why. Silent re-framing is the failure mode this rule prevents. The human approves framing changes by approving the draft.

### Human Override

The human lead may declare a draft ready at any point, including without a critique stance applied. The agent should advise whether the discipline's preconditions are met (so the human knows what they are skipping) but does not block. Record the override in the stance block: `Recommendation: human override; critique stance was not applied`.

### Small Project Fast Stop

For small or low-risk projects, the human lead may stop after any draft. The agent should not manufacture extra iteration just to satisfy ceremony. Before promotion, still verify that the canonical artifact satisfies its schema, and state in the stance block which safeguards were skipped.

## Plan Drafts

`plan` uses the same single-draft mechanism but with much lighter discipline:

- **Draft Stance is optional.** A 1-iteration plan draft may be the planning content alone (Plan Shape, Rationale for Shape, Current Approved Unit, Later Work, Assumptions / Risks). The agent's posture and rationale are already carried by `Planning Stance` and `Rationale for Shape` in the canonical contract.
- **Use Draft Stance and `Consider This` when iterating.** If the human pushes back, the stance block is the right place to declare what changed, and `Consider This` is the right place to capture the human's items.
- **The critique-pass requirement does not apply.** Plan is agent-led, not codesigned.

See `plan-schema.md`.

## Consider This Tagging

For codesign drafts (`intent`, `design`), `Consider This` carries three kinds of items:

- `[from user]` — user contributions, corrections, items the agent may have missed.
- `[Q from LLM]` — questions about ambiguity in the user's input that would meaningfully change the agent's revision.
- `[suggestion from LLM]` — proactive transformative proposals: alternative framings, simpler MVPs, broader ambitions, adjacent ideas.

The user manages the lifecycle of `[from user]` items. The agent may delete its own `[Q from LLM]` and `[suggestion from LLM]` items once they have been answered or absorbed into the draft.

## Promotion

On approval:

- Strip the Draft Stance block and any `Consider This` scaffolding from the draft content.
- Write the cleaned content as the canonical artifact (`intent.md`, `design.md`, `plan.md`).
- Update `accord-state.md`.
- Commit the draft, canonical, and state file with explicit paths.
- Tag.

## Commits

The framework requires a commit only at promotion. Mid-iteration commits are not part of the discipline; the operator may commit work-in-progress at their discretion (e.g., end-of-day backup or before walking away), but the framework neither requires nor structures these.

Uncommitted draft work between sessions is the operator's responsibility. A cold agent in a new conversation reads what's in the working tree (or git, if the operator pulled fresh); if the prior session left uncommitted work that wasn't pushed, it is lost — same as any project.
