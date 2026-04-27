# Seed-and-Iterate Templates

This folder contains the schema templates for the seed-and-iterate process. To use them on a project:

1. Read `conventions.md` once. It defines shared rules for IDs, cross-references, tags, and file format.
2. Copy the templates you need into your project folder. Replace `.template.md` with `.md` and fill in the placeholder fields.
3. Start with `seed.md`. The other documents are drafted by AI skills, not written from scratch.

## The schemas

- **`seed.template.md`** — The minimum specification you commit to. Co-authored with the AI through alternating revisions. One per project.
- **`context.template.md`** — Vision, strategy, personas, success outcomes, constraints, and assumptions. AI-drafted from the Seed. One per project.
- **`goal.template.md`** — What is being built or achieved in this iteration. AI-drafted. One per iteration.
- **`journey.template.md`** — A user experience relevant to the current Goal. AI-drafted. Several per Goal.
- **`story.template.md`** — A deliverable unit of work with requirements. AI-drafted. Many per iteration.

## File naming

- `seed.md` and `context.md` are project-wide; no slug needed.
- `goal-<slug>.md`, `journey-<slug>.md`, `story-<slug>.md` for the others.

## Review order

When the AI drafts a document, it places a "Decision points" section near the top. Read those first — the rest of the document can be skimmed.

## What humans write vs. what AI drafts

- **Human-written or co-authored:** Seed only.
- **AI-drafted, human-reviewed:** Context, Goal, Journey, Story.

Every document, regardless of authorship, ends up in `accepted` status only after the human has reviewed and committed to it.
