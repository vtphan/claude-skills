# ACCORD Draft Conventions

`intent`, `design`, and `plan` may use brainstorm-style drafts while the human lead and LLM are codesigning. Drafts are for thinking; canonical artifacts are for downstream use.

## Monotonic Drafts

Use one monotonic draft sequence per phase folder:

```text
draft_00.md
draft_01.md
<canonical>.md
draft_02.md
```

Drafts are never overwritten. A draft after a canonical artifact is a proposed revision, not automatically a pivot. It becomes accepted only when promoted, committed, and tagged.

## Draft Section Vocabulary

Use these section meanings when they appear in draft templates:

- `Round Stance` - the LLM's short statement of what this round did, why, and whether to continue.
- `Consider This` - open questions, concerns, constraints, or challenges for the next round.
- `Perspective I'm Contributing From` - the human lead's declared lens for the round; copy unchanged unless the human edits it.
- `Human Decisions Needed` - consequential choices that need human authority.
- `LLM Defaults Chosen` - obvious or low-risk choices the LLM made without asking.
- `Notes` - sparse commentary that does not fit elsewhere.

## Promotion

On approval, promote the approved draft into the canonical artifact. The canonical artifact should be cleaner and downstream-oriented; it does not need to preserve draft scaffolding.

Record the source draft in `accord-state.md` and the commit body. Do not add canonical change logs by default.
