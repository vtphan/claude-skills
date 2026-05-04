---
name: brainstorm-this
description: 'Collaborate with the user on developing an idea through a single shared file, `draft.md`. Use this skill whenever the user invokes `/brainstorm-this` (with or without arguments), asks to "brainstorm this," "iterate on this idea," or "do another round of brainstorming." The goal is to help the user develop better ideas through clarification, incremental refinement, and transformative reframing — not to produce polished prose.'
---

# Brainstorm This

Iterate on an idea collaboratively through a single shared file, `draft.md`. Each round, the user writes or edits the draft, and Claude rewrites it with: clarifying questions to sharpen the idea, incremental improvements that strengthen the existing direction, and transformative improvements that reframe it. The goal is to pressure-test and stretch the idea, not to polish prose.

## Invocation

- `/brainstorm-this {free text}` — start a new brainstorm. Creates `draft.md` from the user's free-text idea. If `draft.md` already exists, refuse: "`draft.md` already exists. Delete or rename it first, or run `/brainstorm-this` to continue from it."
- `/brainstorm-this` — read existing `draft.md` and rewrite it in place. If no `draft.md` exists, refuse and tell the user to start with `/brainstorm-this {your idea}`.

The user owns the file between rounds — they may edit any section, including the Idea, before invoking again.

## Draft format

`draft.md` has exactly these sections, in this order:

```
# {short title for the idea — optional, see "Title" below}

## Idea
{the user's idea — Claude writes this from free text on round 0; user owns it after}

## Clarifying Questions
{numbered list — Claude asks questions that would sharpen the idea if answered}

## Incremental Improvements
{numbered list — Claude suggests dimensions that would strengthen the existing idea}

## Transformative Improvements
{numbered list — Claude suggests reframings that fundamentally change the idea}

## Decisions
{persistent log — Claude maintains "Taken" and "Set aside" lists across rounds}

## Notes
{free-form — user answers questions, records thoughts, leaves scratch. Append-preserve.}
```

The six canonical `##` sections — Idea, Clarifying Questions, Incremental Improvements, Transformative Improvements, Decisions, Notes — must appear in this order. If they're missing or out of order, refuse and tell the user exactly what's wrong. Do not silently normalize. The H1 title is optional — its presence, absence, or content is not a validation error.

Content after `## Notes` is the user's space and can take any form, including additional `##` or `###` headings the user wants to add (e.g., `## Open Questions`, `## References`). Do not treat extra headings *after* the Notes section as a validation error. Inside Notes, prefer `###` subheadings if you ever need to add structure, but the user is free to do as they like.

Within `## Decisions`, `**Taken:**` and `**Set aside:**` are part of the schema, not user-customizable labels. If either subsection is missing, recreate it empty during the round. If the user renames or reorders them, restore the canonical labels and place entries under their canonical subsection — Decisions is load-bearing state Claude reads programmatically, so the labels stay fixed. The user can freely edit entries within either subsection, including deleting them.

Keep the suggestion sections (Clarifying Questions, Incremental Improvements, Transformative Improvements) short and use numbered lists, not paragraphs — the user scans them quickly and responds inline. Decisions uses bullets; Notes is free-form. Idea is whatever shape the user wrote.

## How to write each section

### Title (H1)

On the first round, generate a short title (3–8 words) summarizing the idea. On subsequent rounds, copy the title forward unchanged. The user may edit or remove it freely; if they remove it, leave it removed.

### Idea

On the first round, take the user's free-text invocation and condense it into a clear, concise statement — a few sentences to a short paragraph. Capture what they said: the goal, the problem, the scope. Do not add interpretation or "improve" their framing.

On every subsequent round, copy the Idea forward unchanged. The user owns it. If something in the Idea seems unclear, contradictory, or wrong, surface it as a Clarifying Question — never edit the Idea itself.

### Clarifying Questions

Ask 3–7 questions that, if answered, would meaningfully sharpen the idea or change which improvements are worth proposing. Each question should probe a specific dimension — name it in brackets, e.g. `[audience]`, `[success metric]`, `[constraint]`, `[failure mode]`, `[scope]`, `[mechanism]`.

Skip questions you can answer yourself from context. Skip questions the user has already answered in Notes or by editing the Idea. Drop answered questions on the next round (don't reprint them) and fold the answer into the next round's improvements.

If you have fewer than 3 genuine questions, write fewer. Don't pad.

### Incremental Improvements

Suggest 3–5 moves that would strengthen the existing idea without changing its core. Each item names a **dimension** and proposes a **concrete move** along it. Techniques for finding dimensions:

- A stakeholder, audience, or context the idea hasn't accounted for
- A quality that could be lifted (cost, accessibility, durability, speed, clarity, UX)
- A failure mode worth hardening against
- A scope adjustment (tighter or wider) that preserves the core
- A measurement or feedback loop the idea is missing
- A sequencing or staging change (what to do first vs. later)

Format each item as: `**{dimension}** — {concrete move and why it helps}`. Be specific. "Improve UX" is not a move; "add a single-keystroke way to dismiss the prompt because users hit it constantly" is.

### Transformative Improvements

Suggest 3–5 reframings that fundamentally change the idea. These should be uncomfortable on purpose — the user is unlikely to take all of them, and that's fine. The job here is to widen the option space, not to converge. Techniques:

- **Invert the core assumption.** What is the idea silently assuming? What if the opposite were true?
- **Reframe the problem.** Maybe this is solving the wrong problem, or the right problem at the wrong altitude.
- **Swap the metaphor.** Treat it as a service instead of a product, a habit instead of an event, a marketplace instead of a tool, infrastructure instead of an app.
- **Port an adjacent-domain structure.** How would this work if it were structured like {open-source project / a subscription / a game / a school / a protocol}?
- **10x extreme.** What does this look like 10x bigger, 10x smaller, 10x faster, 10x cheaper, 10x narrower? Extremes expose what's actually load-bearing.
- **Drop a "fixed" constraint.** Pick something the user is treating as immovable. What does the idea become if it moves?
- **Combine with something unrelated.** What does this look like crossed with {a domain that has nothing to do with it}?

Format each item as: `**{technique or reframe label}** — {the move, stated as a concrete alternative idea}`. Don't hedge. State each as if you were proposing it for real.

If the user keeps rejecting transformative moves on a particular axis, drop that axis on subsequent rounds and try different ones.

### Decisions

A persistent log Claude maintains across rounds, with two subsections:

```
**Taken:**
- {one-line summary of what was folded into Idea or accepted}

**Set aside:**
- {one-line summary, plus a brief reason if the user gave one}
```

Use Decisions to avoid re-litigating settled ground. Each round, before drafting Clarifying Questions, Incremental Improvements, and Transformative Improvements, scan Decisions and skip anything already there. Update Decisions before rewriting the suggestion sections, based on what the user signaled this round (edits to Idea, statements in Notes, or explicit acceptance/rejection).

If you can't tell whether the user accepted or rejected a prior suggestion, leave Decisions alone and ask in Clarifying Questions. Don't guess — wrongly logging something as "Set aside" silently kills a direction the user wanted to keep open.

Decisions accumulates over the life of the brainstorm. Don't aggressively prune — staleness here is much cheaper than re-proposing rejected directions. The user may edit Decisions freely; respect their edits.

### Notes

The user's space, not yours. Read it carefully each round — it's where the user's responses, decisions signal, and scratch live. Treat Notes as **append-preserve**: never delete, rewrite, reorder, or "tidy" existing content. If you genuinely need to add something here (rare — most of the time, the right place for Claude's content is a different section), append a clearly-marked block at the end, e.g. `**[Claude]:** ...`. The user will move or delete it if they want.

## The iteration loop

Each round:

1. Read the current `draft.md`. The Decisions section is your record of what's been accepted and rejected across prior rounds — rely on it instead of trying to reconstruct history from prose alone.
2. Identify user signals not yet reflected in Decisions: new content in Notes, edits to the Idea, additions or deletions in the suggestion sections, explicit acceptance or rejection. If `draft.md` is tracked in git *and* the user has been committing rounds, `git diff draft.md` and `git log -1 -p draft.md` can show what changed since the last commit — useful evidence when available, but not authoritative (uncommitted state, missing prior commits, or a mismatched baseline can all mislead). Treat git output as a hint, not a record of truth. Without git, or when the diff baseline is unclear, treat anything in Notes or in the suggestion sections that doesn't yet appear in Decisions as potentially new and read it carefully.
3. Update Decisions first: log any newly-accepted moves and any newly-rejected ones based on user signal. If Decisions is missing the `**Taken:**` or `**Set aside:**` subsection, recreate it empty before adding entries.
4. Rewrite Clarifying Questions, Incremental Improvements, and Transformative Improvements end-to-end. Skip anything already in Decisions. Drop stale questions and unattractive suggestions rather than reprinting them.
5. Copy the title and Idea forward unchanged. Preserve Notes append-only — never delete or rewrite user content there.
6. Lean toward challenge over agreement. The user is here to pressure the idea, not have it validated.

## Things to avoid

- **Cosmetic edits.** If your only changes are wording, the round is empty. Say so and recommend stopping.
- **Padding.** If you have 3 strong items, write 3. Don't fabricate a 5th to fill the section.
- **Sycophancy.** Default to challenging the idea, not endorsing it.
- **Editing the user's Idea section.** Use Clarifying Questions instead. The user owns the Idea.
- **Repeating yourself.** If a move is already in Decisions (Taken or Set aside), don't propose it again. If it's not in Decisions but you proposed it last round and the user didn't engage, either drop it or reframe it — don't reprint verbatim.
- **Collapsing transformative into incremental.** Transformative items should feel like a different idea, not a stronger version of the same one. If everything you wrote in the transformative section could fit in the incremental section, you haven't pushed hard enough.

## Convergence

Brainstorming is done when the user says it is, or when you cannot offer a substantive new question, incremental move, or transformative reframe that wasn't already in Decisions or last round's draft. State it plainly by appending a block at the end of Notes: `**[Claude]:** No substantive new moves this round — consider stopping, or seed a new direction in Idea.` Then write a minimal pass (skip empty suggestion sections rather than padding them) and let the user decide.
