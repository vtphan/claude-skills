# ACCORD Draft Conventions

`intent`, `design`, and `plan` use numbered drafts during codesign or planning rounds. Drafts are for thinking; canonical artifacts are for downstream use.

## Brainstorm-This Foundation

`intent` and `design` adopt the discipline of the `brainstorm-this` skill: round stances, immutable core after round 0, two-small-diff convergence with at least one verified critique pass, strict draft non-overwrite. Read `brainstorm-this/SKILL.md` for the full discipline; ACCORD applies it to intent and design domains specifically.

`plan` uses the same numbered-draft mechanism in lighter form. The default is a single round; multiple rounds happen only when the human pushes back. See `plan-schema.md`.

## Monotonic Drafts

Use one monotonic draft sequence per phase folder:

```
draft_00.md
draft_01.md
<canonical>.md
draft_02.md
```

Drafts are never overwritten. A draft after a canonical artifact is a proposed revision, not automatically a pivot. It becomes accepted only when promoted, committed, and tagged.

## Consider This Tagging

For codesign drafts (`intent`, `design`), `Consider This` carries three kinds of items:

- `[from user]` — user contributions, corrections, items the agent may have missed.
- `[Q from LLM]` — questions about ambiguity in the user's input that would meaningfully change the agent's revision.
- `[suggestion from LLM]` — proactive transformative proposals: alternative framings, simpler MVPs, broader ambitions, adjacent ideas. Suggestions serve the immutable Idea; if a suggestion implies the Idea was misframed, surface that as `[Q from LLM]` instead.

The user manages the lifecycle of `[from user]` items. The agent may delete its own `[Q from LLM]` and `[suggestion from LLM]` items once they have been answered or absorbed into `Proposed Solution` (note disposition briefly in `Rationale`).

## Promotion

On approval, promote the approved draft into the canonical artifact. The canonical artifact should be cleaner and downstream-oriented; it does not need to preserve draft scaffolding.

Record the source draft in `accord-state.md` and the commit body. Do not add canonical change logs by default.
