# ACCORD Draft Conventions

`intent`, `design`, and `plan` use numbered drafts during codesign or planning rounds. Drafts are for thinking; canonical artifacts are for downstream use.

## Codesign Discipline

`intent` and `design` use a strict codesign discipline that prevents premature consensus and sycophantic refinement. Each round produces a new monotonic draft file (never overwrite); each draft begins with a Round Stance block; the central framing of the draft is immutable after round 0; convergence requires a critique pass; the agent's default posture leans away from cosmetic refinement.

### Round Stance

Each draft opens with a short markdown block declaring the agent's choices for the round:

```
**Round N**
- Stance: [refine | expand | critique | subtract | restructure | ask | stop]
- Perspective I'm adopting: [one phrase]
- Substantive changes: [1-2 sentences naming what actually changed in argument, structure, or recommendations — not phrasing]
- Recommendation: [continue | small diff, consider stopping | converged, recommend stopping]
```

The substantive-changes line is a forcing function: if the agent cannot name a substantive change, the round is small-diff and should say so honestly.

### Stance Vocabulary

- `refine` — tighten the existing content
- `expand` — add a dimension, alternative, or consideration that's missing
- `critique` — adopt a skeptical perspective and surface weaknesses, gaps, failure modes
- `subtract` — remove weak arguments, redundant points, or scope creep
- `restructure` — reorganize the logic when the current shape isn't serving the work
- `ask` — surface a question whose answer would meaningfully change the next revision
- `stop` — declare convergence (see below)

Default toward `expand`, `critique`, or `subtract` rather than `refine`. Sycophantic refinement is the failure mode to avoid.

### Immutable Core After Round 0

Each draft carries a central framing — the Idea (intent) or Design Brief (design). After round 0 this is fixed and copied forward unchanged. If the framing seems wrong, surface it as `[Q from LLM]` in `Consider This`; never edit the core silently.

### Convergence Rule

Stop only after **two consecutive small-diff rounds AND** at least one verified critique-stance round in the loaded draft history. Without a verified critique pass, do not declare convergence; either continue or run a critique round next.

A small-diff round is one where the agent cannot articulate substantive changes — only phrasing, ordering, or polish.

### Strict Non-Overwrite

Each round produces a new file. Never overwrite a prior draft. The user may edit any draft between rounds; the agent reads those edits as high-priority signal for the next round.

## Plan Drafts

`plan` uses the numbered-draft mechanism but a lighter discipline:

- The default is one round; multiple rounds happen only when the human pushes back via `Consider This` items.
- The Round Stance block is still useful — it carries the agent's recommendation and rationale.
- The convergence rule does not apply; plan drafts are normally accepted in one round.

See `plan-schema.md`.

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

## Attribution

The codesign discipline above is adapted from the standalone `brainstorm-this` skill. ACCORD inlines what it needs so that the framework remains a self-contained five-skill set; this file is the canonical reference, not a pointer to an external dependency.
