---
name: brainstorm-this
description: 'Collaborate with the user on developing an idea through structured, iterative brainstorming captured in shared versioned markdown drafts. Use this skill whenever the user invokes `/brainstorm-this` (with or without arguments), asks to "brainstorm this," "iterate on this idea," "do another round of brainstorming," or "advance the draft," references similarly numbered draft files such as `draft_00.md` and `draft_01.md` in a brainstorming context, or shares a markdown draft that already uses this exact section structure: `Round Stance`, `Idea`, `Proposed Solution`, `Rationale`, `Consider This`, `Perspective I''m Contributing From`, and `Notes`. This is a brainstorming and ideation aid — the goal is to help the user develop better ideas through revision, critique, and dialogue, not to produce polished prose.'
---

# Brainstorm This

A workflow for developing an idea collaboratively with the user across multiple rounds. The user and Claude communicate through a structured markdown file. Each round, Claude reads the current draft, considers what the user has changed or added, and produces a revised next draft. Over many rounds, ideas get sharper, weaker arguments fall away, and gaps surface.

This skill is for **ideation and reasoning**, not document polishing. Treat the work as thinking-out-loud that needs to be tested, challenged, and developed — not prose to be smoothed.

## Invocation modes

The skill supports three ways to invoke it.

**Mode 1 — Start a new brainstorm:** `/brainstorm-this {free text description of an idea}`

The free text is the user's raw idea. Claude:
1. Summarizes it into a concise statement and places it in the **Idea** section. (The user can edit this before the next round; from round 1 onward the Idea is immutable to Claude.)
2. Produces a first-pass Proposed Solution, Rationale, and an initial round stance.
3. Saves the result as `draft_00.md` in the current working directory.

**Mode 2 — Work on a specific draft:** `/brainstorm-this draft_07.md`

Claude reads the named file, reads up to 2 prior drafts if they exist for context, and produces the next numbered draft. If the next-numbered file already exists, refuse and surface the conflict — do not overwrite, do not skip ahead. Tell the user: "`draft_<next>.md` already exists. Delete it first if you want to redo this round."

**Mode 3 — Continue from the latest draft:** `/brainstorm-this`

Claude finds the highest-numbered `draft_<number>.md` in the working directory and proceeds as in Mode 2. If no draft files exist, refuse with: "No draft files found. To start a new brainstorm, run `/brainstorm-this {your idea}`. To work on an existing draft, name it: `/brainstorm-this draft_03.md`."

## File naming

Drafts are named `draft_<number>.md` with **at least two digits of zero padding** (`draft_00.md`, `draft_01.md`, ... `draft_99.md`, `draft_100.md`). Keep two digits for rounds 0-99 so files sort cleanly in directory listings. After round 99, continue with natural-width integers; do not wrap, truncate, or reset numbering.

Each round produces a new file. Never overwrite a prior draft. The user may edit any draft between rounds.

## Draft structure

Every draft has these sections, in this order:

```
## Round Stance
[short markdown block — Claude writes this each round]

## Idea
[the user's idea — Claude must NOT modify this after round 0]

## Proposed Solution
[collaborative — Claude revises, user can edit]

## Rationale
[collaborative — Claude revises, user can edit]

## Consider This
[bidirectional — user surfaces gaps; Claude asks questions]

## Perspective I'm Contributing From
[user only — declares their stance for the round]

## Notes
[free-form — either party, persistent commentary]
```

If an existing draft is missing any of these sections, or the sections appear in a different order, refuse and tell the user exactly which sections are missing or misplaced. Do not silently normalize or rewrite a malformed existing draft.

## Round 0: seeding from free text

When invoked in Mode 1, the file does not yet exist. Build `draft_00.md` as follows:

1. **Idea:** Take the user's free-text description and summarize it into a clear, concise statement. Capture what they actually said — the goal, the problem, the scope as they expressed it — without adding interpretation or "improving" the framing. Aim for a few sentences to a short paragraph. The user will review and edit this before the next round if needed; after that, it becomes immutable.

2. **Proposed Solution:** Produce a genuine first-pass solution. This is not a placeholder — engage with the idea substantively. Pick a stance (most often `expand` or `refine`) and put real thinking on the page.

3. **Rationale:** Explain why your Proposed Solution serves the Idea. Surface the assumptions you're making.

4. **Consider This:** Leave this empty, or seed it with 1-3 `[Q from LLM]` items if there are genuine ambiguities in the user's free text that materially affect the Proposed Solution. Do not invent questions for the sake of populating the section.

5. **Perspective I'm Contributing From:** Leave empty with a placeholder line: `_(user fills in next round)_`. The user did not declare a perspective in their initial invocation.

6. **Notes:** Empty.

7. **Round Stance:** Fill in normally (see "Round Stance" below). For round 0, stance is typically `expand` or `refine` and recommendation is `continue`.

## Round 1+: workflow

When invoked in Mode 2 or Mode 3 on an existing draft:

1. **Find the source draft.** In Mode 2, the user named it. In Mode 3, find the highest-numbered `draft_<number>.md` in the working directory.

2. **Read the source draft and 1-2 prior drafts** if they exist. Seeing trajectory matters — without it, you risk drifting from earlier intent or repeating moves you already made. Do not load more than the most recent 2 prior drafts; older history dilutes attention.

3. **Read carefully before writing.** Specifically:
   - The **Idea** — fixed ground. Everything else serves it.
   - **Consider This** — the user's high-priority inputs for this round, plus any open `[Q from LLM]` questions you asked previously that the user has now answered.
   - **Perspective I'm Contributing From** — the lens the user is reasoning through this round. Use it to interpret their edits and to calibrate your response.
   - The **diff** between the source draft and the prior one — what did the user change? Their edits are signal about what they think is right or wrong with the current direction.

4. **Decide what kind of round this should be.** You have several options and should pick deliberately, not default to "refine":
   - **Refine** — tighten the existing Proposed Solution and Rationale
   - **Expand** — add a dimension, alternative, or consideration that's missing
   - **Critique** — adopt a skeptical perspective and surface weaknesses, gaps, failure modes
   - **Subtract** — remove weak arguments, redundant points, or scope creep
   - **Restructure** — reorganize the logic when the current shape isn't serving the Idea
   - **Ask** — if a Consider This item or part of the Idea is genuinely ambiguous and would meaningfully change your revision, prefer asking a question over guessing
   - **Stop** — declare convergence (see "Stopping" below)

5. **Write the next-numbered draft** as a new file. Do not overwrite. If the target filename already exists, refuse and ask the user to resolve the conflict.

## How to handle each section

### Round Stance

Write a short markdown block at the top of the new draft. Use ordinary markdown text and bullets, not a code fence. This is your one-paragraph declaration of what you did this round and why. Structure:

```
**Round N**
- Stance: [refine | expand | critique | subtract | restructure | ask | stop]
- Perspective I'm adopting: [one phrase]
- Substantive changes: [1-2 sentences naming what actually changed in argument, structure, or recommendations — not phrasing]
- Recommendation: [continue | small diff, consider stopping | converged, recommend stopping]
```

The "substantive changes" line is a forcing function. If you cannot name a substantive change in 1-2 sentences, you didn't make one — that's a small-diff round.

### Idea

After round 0, copy unchanged. Do not modify, "clarify," or "improve" this section. If the Idea seems unclear or contradictory, surface that as a `[Q from LLM]` item in Consider This — never edit the Idea itself.

### Proposed Solution

Revise according to your chosen stance. Be willing to make substantial changes when the round calls for it (especially in critique, expand, or restructure rounds). Avoid cosmetic editing — if you find yourself rewording sentences without changing meaning, stop and reconsider whether this round should be `stop` instead.

### Rationale

Update to reflect any changes you made to Proposed Solution. Also: for each Consider This item the user added since the last round, note briefly here how you incorporated it (or why you judged it not relevant this round). This creates a visible trail of how user inputs shape the work.

### Consider This

Two kinds of items live here:
- **`[from user]`** — the user's contributions. Treat these as high-priority signal. They are things the user thinks you may have missed: directions, constraints, concerns, corrections, references.
- **`[Q from LLM]`** — questions you raise when something is genuinely ambiguous and a revision based on guessing would be unproductive. Tag every question this way so the user can find them at a glance.

Carry forward unaddressed user items unchanged. The user manages the lifecycle of their items — do not delete them on their behalf. You may delete your own `[Q from LLM]` items once they have been answered (note the answer briefly in Rationale).

When you ask a question, prefer making a minimal revision (or none) that round. Asking *and* guessing *and* revising defeats the purpose of asking.

### Perspective I'm Contributing From

Copy unchanged. This is the user's voice, not yours. If the user has not yet filled it in, leave the placeholder line.

### Notes

Free-form. You may add observations or meta-commentary here. Keep it sparse — Notes is for things that don't fit elsewhere, not a dumping ground.

## Stopping

You can declare convergence and recommend stopping. The criterion is **two consecutive small-diff rounds**, where "small-diff" means you cannot articulate substantive changes — only phrasing, ordering, or polish.

Only recommend `stop` if you can verify from the source draft and the prior drafts you loaded for context that at least one visible round adopted a genuinely skeptical or stress-testing perspective (`critique` or equivalent). If you cannot verify that from the drafts you read, do not recommend stopping on this pass; prefer `continue` or run a critique round instead.

How this works in practice:

- Round N: you make a small revision and write in your Round Stance: `Recommendation: small diff, consider stopping`.
- Round N+1: the user may have edited Consider This or other sections in between. You revise again. If this round is *also* small-diff, write: `Recommendation: converged, recommend stopping. Make no further revisions this round.` In this case, copy the prior draft forward unchanged except for your Round Stance block.
- If round N+1 has substantive changes (often because the user added new Consider This items), the convergence clock resets — continue normally.

**Stopping is a valid and valuable outcome.** Do not revise for the sake of revising. A small cosmetic edit when the work is done is worse than declaring convergence. The user explicitly wants you to stop when the iteration is no longer productive.

The user can override your stop recommendation by editing the draft and asking for another round. That's expected.

## Failure modes to avoid

- **Premature convergence.** Do not declare convergence unless the loaded draft history shows at least one round that adopted a critical perspective and looked for weaknesses. If you cannot verify that from the drafts you read, the work is not ready to stop.
- **Cosmetic revision.** If your only changes are word choice and sentence order, the round is small-diff. Say so honestly in the Round Stance rather than dressing up a small edit as a substantive one.
- **Editing the Idea.** Never (after round 0). Use `[Q from LLM]` in Consider This instead.
- **Drift across rounds.** If you find yourself re-introducing an argument the user removed two rounds ago, or undoing a structural change from a prior round, stop and reconsider. Either the user's edit was wrong (in which case raise it via Consider This) or yours was — don't silently fight it across rounds.
- **Sycophantic refinement.** It is tempting to treat the current draft as mostly right and just polish. Resist this. The user is using this skill *because* they want pressure on the idea, not validation of it. When in doubt, lean toward critique or expand over refine.
- **Defaulting to refine.** Before revising, explicitly consider whether expand, critique, or subtract would serve the Idea better. Refine is the right move sometimes — but it should be a chosen move, not a default.
- **Overwriting drafts.** Never. Each round produces a new file. If the target filename exists, refuse and surface the conflict.

## Example Round Stance blocks

**A round-0 first pass:**
```
**Round 0**
- Stance: expand
- Perspective I'm adopting: collaborative ideator
- Substantive changes: Seeded the Idea from the user's free-text invocation. Drafted an initial Proposed Solution covering scope, mechanics, and one open question about timeline. Surfaced two [Q from LLM] items in Consider This.
- Recommendation: continue
```

**A critique round:**
```
**Round 4**
- Stance: critique
- Perspective I'm adopting: skeptical IRB reviewer
- Substantive changes: Surfaced two assumptions in the recruitment plan that aren't justified by the Rationale, and added a failure-mode analysis for the consent flow. Did not change the high-level Proposed Solution.
- Recommendation: continue
```

**A small-diff round leaning toward stopping:**
```
**Round 6**
- Stance: refine
- Perspective I'm adopting: clarifier
- Substantive changes: Tightened the wording of step 3; merged two redundant points in Rationale. No changes to argument, structure, or recommendations.
- Recommendation: small diff, consider stopping
```

**An ask round:**
```
**Round 2**
- Stance: ask
- Perspective I'm adopting: implementer
- Substantive changes: None. Added one [Q from LLM] item to Consider This about the timeline constraint. The answer materially changes whether the current Proposed Solution is feasible.
- Recommendation: continue (after question is answered)
```
