---
name: brainstorm-this
description: 'Collaborate with the user on developing an idea through a single shared file, `draft.md`. Use this skill whenever the user invokes `/brainstorm-this` (with or without arguments), asks to "brainstorm this," "iterate on this idea," or "do another round of brainstorming." Each round produces a durable Current Proposal and Rationale (the codesigned working answer and why) alongside clarifying questions, incremental refinements, and transformative reframings — not polished prose, but a working answer plus the reasoning behind it.'
---

# Brainstorm This

Iterate on an idea collaboratively through a single shared file, `draft.md`. The user owns the **Idea** (the problem framing). Claude maintains a **Current Proposal** (the working solution-shape) and a **Rationale** (why this shape) that evolve each round as decisions are taken, plus clarifying questions, incremental moves, and transformative reframes. The goal is to pressure-test and stretch the idea, not to polish prose.

## Invocation

- `/brainstorm-this {free text}` — start a new brainstorm. Creates `draft.md` from the user's free-text idea. If `draft.md` already exists, refuse: "`draft.md` already exists. Delete or rename it first, or run `/brainstorm-this` to continue from it."
- `/brainstorm-this` — read existing `draft.md` and rewrite it in place. If no `draft.md` exists, refuse and tell the user to start with `/brainstorm-this {your idea}`.

The user owns the file between rounds — they may edit any section, including the Idea, before invoking again.

## Draft format

`draft.md` has exactly these sections, in this order:

```
# {short title for the idea — optional, see "Title" below}

## Idea
{the user's problem framing — Claude writes this from free text on round 0; user owns it after}

## Current Proposal
{Claude-maintained, user-editable — concrete shape of the codesigned solution at this round}

## Rationale
{Claude-maintained, user-editable — why this shape; load-bearing assumptions}

## Clarifying Questions
{numbered list — Claude asks questions that would sharpen the Current Proposal if answered}

## Incremental Improvements
{numbered list — Claude suggests moves that would strengthen the Current Proposal}

## Transformative Improvements
{numbered list — Claude suggests reframings that fundamentally change the Idea or Current Proposal}

## Decisions
{persistent log — Claude maintains "Taken" and "Set aside" lists across rounds}

## Notes
{free-form — user answers questions, records thoughts, leaves scratch. Append-preserve.}
```

The eight canonical `##` sections — Idea, Current Proposal, Rationale, Clarifying Questions, Incremental Improvements, Transformative Improvements, Decisions, Notes — must appear in this order. If they're missing or out of order, refuse and tell the user exactly what's wrong. Do not silently normalize. The H1 title is optional — its presence, absence, or content is not a validation error.

Content after `## Notes` is the user's space and can take any form, including additional `##` or `###` headings the user wants to add (e.g., `## Open Questions`, `## References`). Do not treat extra headings *after* the Notes section as a validation error. Inside Notes, prefer `###` subheadings if you ever need to add structure, but the user is free to do as they like.

Within `## Decisions`, `**Taken:**` and `**Set aside:**` are part of the schema, not user-customizable labels. If either subsection is missing, recreate it empty during the round. If the user renames or reorders them, restore the canonical labels and place entries under their canonical subsection — Decisions is load-bearing state Claude reads programmatically, so the labels stay fixed. The user can freely edit entries within either subsection, including deleting them.

Keep the suggestion sections (Clarifying Questions, Incremental Improvements, Transformative Improvements) short and use numbered lists, not paragraphs — the user scans them quickly and responds inline. **Cap each suggestion section at 3 items.** Write fewer if fewer are real — never pad. Within each section, rank in descending order of leverage: the item most worth engaging with goes first. Decisions uses bullets; Notes is free-form. Idea is whatever shape the user wrote.

## Inline responses

After round 0, the user's primary channel for engagement is writing responses directly under the numbered items in Clarifying Questions, Incremental Improvements, and Transformative Improvements — answering a question, accepting, pushing back, or adding a constraint. Inline responses use explicit markers placed between item N and item N+1: prefer a `> blockquote` (default), a `**Lead:**` prefix, or an indented `Response:` line. Unmarked continuation text, line-wrapping inside an item, or edits to the item text itself are not responses. When a chunk is ambiguous (could be a response, could be an edit to the item), treat it conservatively — do not move anything to Decisions on weak evidence; surface the ambiguity in next round's Clarifying Questions instead.

The user will not respond to every item. **Silence is not rejection.** An item without an inline response is still open — carry it forward, drop it for staleness, or replace it with a sharper variant, but do not move it to `Set aside`. Only mark something `Set aside` on explicit rejection (e.g. "no", "skip", "drop this", "set aside").

When the user does write inline:
- An answer or elaboration informs the next round's suggestions; it does not necessarily need a Decisions entry.
- An answer that introduces a constraint, scope change, or other shape signal that materially changes the proposal → fold into Current Proposal and surface in Rationale this round (see "Current Proposal" trigger (d)). No explicit Decision required — the proposal update *is* the durable capture.
- Explicit acceptance ("yes, fold this in", "take this") → Decisions → Taken (and fold into Current Proposal).
- Explicit rejection → Decisions → Set aside, with the user's reason if given.
- A response that reframes the question or pivots the idea may warrant a Clarifying Question or a new direction in the next round's suggestions.

**No substantive user signal disappears.** Before rewriting a section, every substantive user signal in the suggestion sections — inline responses, item additions, item rewrites, item deletions — that conveys new context, a constraint, an answer, an acceptance, or a rejection must be captured somewhere durable. In strict preference order:

1. **Fold it into Current Proposal and surface it in Rationale** when the response materially changes the proposal's shape, scope, or constraints. This is the most durable destination — Rationale carries the audit trail. If the response is also an explicit acceptance, pair this with a Decisions → Taken entry.
2. **Fold it into the next round's question or suggestion** so the signal is visibly carried forward — for responses that sharpen, pivot, or elaborate but don't yet reshape the proposal.
3. **Log it in Decisions** (Taken or Set aside) when the response is an explicit acceptance, rejection, or directional commitment that closes off a thread without reshaping Current Proposal.
4. **Append a `**[Claude]:**` block at the end of Notes** only as a last resort, when the signal is important but fits none of (1)–(3). Notes is the user's space — use this sparingly and keep the block to one or two lines.

Pure throwaway acknowledgments ("ok", "sure", "noted") don't need preservation. When in doubt, preserve.

For structural edits specifically: a user rewrite of an item is a sharpened framing (carry it forward); an addition is a direction the user is contributing (preserve as theirs in the next round, or fold into Current Proposal / Decisions if it's clearly a constraint or accepted move); a deletion is ambiguous — handle it like silence (don't move to Set aside without explicit rejection text).

Inline responses are consumed when you rewrite the section — they do not persist verbatim into the next round's draft. The "no signal disappears" rule is what makes this safe: by the time a response is consumed, its content lives somewhere durable.

On round 0, include a one-line hint immediately above `## Clarifying Questions`:

```
_Respond inline under any item. Skipping is fine — silence is not rejection._
```

On subsequent rounds, the hint is **sticky-once-dropped**, decided from the file alone (no lifetime memory required): if the hint is present in `draft.md` at round start AND inline responses appeared this round, omit it from the rewrite. If the hint is already absent, leave it absent — never re-add it, including when the user deleted it before engaging inline. Manual deletion is treated as the user signaling they've absorbed the convention; the hint is a one-shot teaching aid, not a persistent banner. The hint is not part of the canonical schema; its presence or absence is not a validation error.

## How to write each section

### Title (H1)

On the first round, generate a short title (3–8 words) summarizing the idea. On subsequent rounds, copy the title forward unchanged. The user may edit or remove it freely; if they remove it, leave it removed.

### Idea

The user's *problem framing* — the goal, the problem, the scope, the constraints. Distinct from Current Proposal, which is the working solution-shape.

On the first round, take the user's free-text invocation and extract the problem framing: the goal and scope, not the solution-shape if they sketched one (that goes in Current Proposal). Condense into a clear, concise statement — a few sentences to a short paragraph. Do not add interpretation or "improve" their framing.

On every subsequent round, copy the Idea forward unchanged. The user owns it. If something in the Idea seems unclear, contradictory, or wrong, surface it as a Clarifying Question — never edit the Idea itself.

### Current Proposal

The codesigned answer to the Idea — the concrete, structural shape of the solution at this round. Claude maintains it; the user edits freely. Distinct from Idea (which is the problem framing) and from Decisions (which is the per-move log).

**Round 0:** Synthesize a first-pass proposal from the user's free-text invocation. If they sketched a solution-shape, lift it out and tighten it. If their invocation was purely problem-framing, write a minimal first-pass proposal that's clearly first-pass — Claude is opening the conversation, not committing to an answer.

**Subsequent rounds:** Default to copy-forward. Update only when one of these triggers fires:

- (a) A Decision was Taken — fold the accepted move into the proposal.
- (b) The user edited Idea — re-derive the proposal to fit the new framing.
- (c) The user directly edited Current Proposal — read their edit as the new baseline.
- (d) A substantive inline response introduced a constraint, scope change, or shape signal that materially changes the proposal — fold the implication in even without an explicit Decision.

When (d) fires, the matching Rationale update must explicitly surface the new constraint or shape signal — that is the audit trail. Never edit cosmetically; wording-only changes don't count.

Format: short paragraphs or a structured bullet list — *not* a design doc. Aim for the level of detail that makes the proposal actionable but still pliable. If it grows past ~10 lines, prune to load-bearing structure.

### Rationale

The argument for *why this shape* — how Current Proposal serves the Idea, what constraints it respects, which assumptions are load-bearing (the ones that, if false, would invalidate the proposal).

**Round 0:** State the reasoning behind the first-pass proposal in 2–4 short bullets. Be honest about what's a guess.

**Subsequent rounds:** Default to copy-forward. Update only when (a) Current Proposal updated this round — rewrite to reflect the new shape and surface any new load-bearing assumptions, or (b) the user directly edited Rationale — treat their edit as the new baseline; only revise it if it now contradicts Current Proposal, and even then prefer surfacing the contradiction in next round's Clarifying Questions over overwriting the user. Each Decision Taken or trigger-(d) update should leave a visible trace — Rationale should explain *why* that move strengthened the proposal or what constraint now binds it, not just acknowledge it.

Format: short bullets, each one a self-contained reason. Surface load-bearing assumptions explicitly, e.g. `Assumes: senior engineers can be reached via existing channels — if false, this forces a discovery-channel build.`

### Clarifying Questions

Ask up to 3 questions that, if answered, would meaningfully sharpen the Current Proposal or change which improvements are worth proposing. Each question should probe a specific dimension — name it in brackets, e.g. `[audience]`, `[success metric]`, `[constraint]`, `[failure mode]`, `[scope]`, `[mechanism]`, `[assumption]`. Rank by leverage: the question whose answer would unlock the most goes first.

Skip questions you can answer yourself from context. Skip questions the user has already answered in Notes or by editing the Idea. Drop answered questions on the next round (don't reprint them) and fold the answer into the next round's improvements.

### Incremental Improvements

Suggest up to 3 moves that would strengthen the Current Proposal without changing its core, ranked by leverage (the strongest move first). Each item names a **dimension** and proposes a **concrete move** along it. Techniques for finding dimensions:

- A stakeholder, audience, or context the idea hasn't accounted for
- A quality that could be lifted (cost, accessibility, durability, speed, clarity, UX)
- A failure mode worth hardening against
- A scope adjustment (tighter or wider) that preserves the core
- A measurement or feedback loop the idea is missing
- A sequencing or staging change (what to do first vs. later)

Format each item as: `**{dimension}** — {concrete move and why it helps}`. Be specific. "Improve UX" is not a move; "add a single-keystroke way to dismiss the prompt because users hit it constantly" is.

### Transformative Improvements

Suggest up to 3 reframings that fundamentally change the Idea or the Current Proposal, ranked by leverage (the most provocative or load-bearing reframe first). These should be uncomfortable on purpose — the user is unlikely to take all of them, and that's fine. The job here is to widen the option space, not to converge. Techniques:

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
- {one-line summary of what was accepted or folded into Current Proposal}

**Set aside:**
- {one-line summary, plus a brief reason if the user gave one}
```

Use Decisions to avoid re-litigating settled ground. Each round, before drafting Clarifying Questions, Incremental Improvements, and Transformative Improvements, scan Decisions and skip anything already there. Update Decisions before rewriting the suggestion sections, based on what the user signaled this round: inline responses, edits to Idea, direct edits to Current Proposal or Rationale that clearly accept or reject a previously-proposed move, statements in Notes, or explicit acceptance/rejection.

**Silence is not rejection.** If the user did not respond to a prior suggestion, leave it out of Decisions — items without engagement remain open. Only `Set aside` on explicit rejection. If the acceptance/rejection signal is ambiguous, leave Decisions alone and ask in Clarifying Questions. Don't guess — wrongly logging something as "Set aside" silently kills a direction the user wanted to keep open.

Decisions accumulates over the life of the brainstorm. Don't aggressively prune — staleness here is much cheaper than re-proposing rejected directions. The user may edit Decisions freely; respect their edits.

### Notes

The user's space, not yours. Read it carefully each round — it's where longer-form thoughts, decisions context, and scratch live. (Item-level responses go inline under the suggestion items, not here — see "Inline responses".) Treat Notes as **append-preserve**: never delete, rewrite, reorder, or "tidy" existing content. If you genuinely need to add something here (rare — most of the time, the right place for Claude's content is a different section), append a clearly-marked block at the end, e.g. `**[Claude]:** ...`. The user will move or delete it if they want.

## The iteration loop

Each round:

1. Read the current `draft.md`. The Decisions section is your record of what's been accepted and rejected across prior rounds — rely on it instead of trying to reconstruct history from prose alone.
2. Identify user signals not yet reflected in Decisions, in this priority order: **inline responses under suggestion items (the primary channel after round 0)**, edits to Idea, edits to Current Proposal or Rationale, new content in Notes, additions or deletions in the suggestion sections, explicit acceptance or rejection. If `draft.md` is tracked in git *and* the user has been committing rounds, `git diff draft.md` and `git log -1 -p draft.md` can show what changed since the last commit — useful evidence when available, but not authoritative (uncommitted state, missing prior commits, or a mismatched baseline can all mislead). Treat git output as a hint, not a record of truth. Without git, or when the diff baseline is unclear, treat anything in Notes or in the suggestion sections that doesn't yet appear in Decisions as potentially new and read it carefully.
3. Update Decisions first: log any newly-accepted moves and any newly-rejected ones based on user signal. If Decisions is missing the `**Taken:**` or `**Set aside:**` subsection, recreate it empty before adding entries.
4. Update Current Proposal and Rationale only if one of these triggers fires: (a) a Decision was Taken this round, (b) the user edited Idea, (c) the user directly edited Current Proposal or Rationale, or (d) a substantive inline response introduced a constraint, scope change, or shape signal that materially changes the proposal. Otherwise copy them forward unchanged. When (d) fires, Rationale must explicitly surface the new constraint or shape signal — that is the audit trail. Wording-only rewrites are noise — leave them alone. See the "Current Proposal" and "Rationale" section guidance for trigger-by-trigger handling.
5. Rewrite Clarifying Questions, Incremental Improvements, and Transformative Improvements end-to-end, anchoring against the (now-updated) Current Proposal. Skip anything already in Decisions. Drop stale questions and unattractive suggestions rather than reprinting them.
6. Copy the title and Idea forward unchanged. Preserve Notes append-only — never delete or rewrite user content there.
7. Lean toward challenge over agreement. The user is here to pressure the idea, not have it validated.

## End-of-round briefing

After rewriting `draft.md`, post a short briefing in chat (not in the file). The file is the durable record; the briefing is the pointer that orients the user before they open it.

Include:
- One-line diff summary: what changed this round (Proposal/Rationale updates, Decisions taken/set aside, new questions, dropped suggestions, reframes). If Proposal and Rationale didn't change, say so explicitly — that's load-bearing information.
- 1–3 highlighted items the user should look at first — typically the question whose answer would unlock the most, or the suggestion most worth engaging with this round.
- Any convergence signal (see "Convergence" below).

Keep the briefing under ~6 bullets. Don't restate the file — point at it. If nothing meaningful changed (cosmetic round), say so plainly rather than padding.

## Things to avoid

- **Cosmetic edits.** If your only changes are wording, the round is empty. Say so and recommend stopping.
- **Padding.** Each suggestion section caps at 3, but writing fewer is fine — even zero. Don't fabricate items to fill the section.
- **Sycophancy.** Default to challenging the idea, not endorsing it.
- **Editing the user's Idea section.** Use Clarifying Questions instead. The user owns the Idea.
- **Cosmetic Proposal or Rationale rewrites.** Update Current Proposal or Rationale only on a defined trigger: a Decision was Taken, the user edited Idea, the user edited those sections directly, or a substantive inline response materially changes the proposal's shape or constraints (trigger (d) in the section guidance). Wording-only edits are noise — copy forward unchanged instead.
- **Repeating yourself.** If a move is already in Decisions (Taken or Set aside), don't propose it again. If it's not in Decisions but you proposed it last round and the user didn't engage, either drop it or reframe it — don't reprint verbatim.
- **Collapsing transformative into incremental.** Transformative items should feel like a different idea, not a stronger version of the same one. If everything you wrote in the transformative section could fit in the incremental section, you haven't pushed hard enough.
- **Treating silence as rejection.** If the user didn't respond to an item, it's open, not killed. Do not move it to `Set aside` without an explicit rejection.

## Convergence

Brainstorming is done when the user says it is, or when you cannot offer a substantive new question, incremental move, or transformative reframe that wasn't already in Decisions or last round's draft, *and* Current Proposal and Rationale are stable (no pending Decisions to fold in). State it plainly by appending a block at the end of Notes: `**[Claude]:** No substantive new moves this round — consider stopping, or seed a new direction in Idea.` Then write a minimal pass (skip empty suggestion sections rather than padding them) and let the user decide. The Current Proposal at convergence is the codesigned outcome.
