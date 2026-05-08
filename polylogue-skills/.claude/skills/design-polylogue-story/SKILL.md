---
name: design-polylogue-story
description: Co-design a graphic-novel choose-your-own-adventure story with a human author through a 9-round process. Produces a JSON story package (`story.json`) conforming to the bundled `schema.json`, for a student-facing app. Each chapter ends with a 3-MC decision; the story is Y-shaped with one perspective-taking fork that diverges into different endings. Use when an author asks to design, write, build, or draft a polylogue story.
---

# design-polylogue-story

Co-design a graphic-novel CYOA story with a human author. The story has chapters → pages → chapter-end 3-MC decisions, with exactly one perspective-taking fork that diverges into different endings. The author provides scope (story idea, target thinking skills, grade level, minutes); three bundled subagents do the creative work; you orchestrate.

## Operating principle

- Bring an artifact before asking. Default-and-confirm over ask.
- The human author drives intent and approves; subagents draft; you orchestrate the pipeline and keep `polylogue.md` current.
- Counts (chapters, pages) emerge from the story arc, disciplined only by the runtime budget. Do NOT default to fixed counts.
- The author always sees polished output. The Reviewer/Editor subagent edits minor issues silently and flags structural ones.
- Loopback (revise-in-place / re-narrow / re-diverge / re-frame) is callable from any round.

## Author's job

1. Provide a seed in Round 0: story line idea, target thinking skill(s), target minutes (default 15), reading level (5/6/7).
2. React to artifacts: yes / no / revise / change X.
3. Approve the export.

The author can directly edit `polylogue.md` or any `chapters/chapter-NN.md` between rounds; you pick up edits on the next round.

## Artifacts

```
{slug}/
|-- polylogue.md            # master: concept, character bible, art style, chapter list, runtime estimate
|-- story.json              # final export (Round 8 only)
|-- chapters/
|   `-- chapter-NN.md       # lazy: one per chapter; transcript + complete image prompt per page
`-- rounds/                 # lazy round files when material exceeds polylogue.md
```

`polylogue.md` is the single source of truth for the character bible and locked art style. Chapter files are self-contained per chapter (full pages + complete image prompts + decision + abrupt-end pages).

## Invocation

`design-polylogue-story <seed-text>` — start a new story. With no args, continue from current artifacts in the working directory.

## The three subagents

Dispatch by name in prose to the registered agents:

- **`polylogue-creative-writer`** — drafts story plot, characters, dialogue, scene staging, abrupt-end pages. Free creative latitude.
- **`polylogue-instructional-designer`** — adapts language to grade level, authors all 3-MC decisions with misconception-bearing wrong choices, runs the mandatory elimination check.
- **`polylogue-reviewer-editor`** — polishes, composes complete image prompts, edits silently, flags structural issues, runs sync-checks and Round 7 quality review.

Pipeline per round that produces creative content:

```
polylogue-creative-writer → polylogue-instructional-designer → polylogue-reviewer-editor → human author
```

The author sees only the Reviewer's output. Author feedback re-enters the pipeline at the appropriate role's stage.

## Round flow

### Round 0 — Seed
Capture: (1) story line idea, (2) target thinking skill(s), (3) target minutes (default 15), (4) reading level (5/6/7). Validate skill names against `thinking-skills.md`; if author names don't match, surface the closest canonical names and ask whether to map or extend. Initialize `polylogue.md`. Mark status `Round 0 complete`.

### Round 1 — Concept
Use the `polylogue-creative-writer` subagent to generate 3–5 distinct story concepts (logline, character sketches, arc shape with proposed fork location, tone, theme). Use the `polylogue-instructional-designer` subagent to suggest secondary thinking skills the story naturally implicates, with one-line reasons. Use the `polylogue-reviewer-editor` subagent to polish. Present to the author. The author picks one or composes by combining elements; secondary skills confirmed/dropped/added. Update `polylogue.md`.

### Round 2 — Character bible and locked art style
Use the `polylogue-creative-writer` subagent to draft each recurring character (name, role, age, physical description, clothing, distinctive features, expression baseline) and the locked art style (rendering style, palette, lighting, line treatment, aspect ratio). The Reviewer/Editor verifies visual unambiguity. Default-and-confirm `aspect_ratio` (default `2:3` — portrait, fits two-column tablet/Chromebook reader and matches comic-page proportions; offer `9:16`, `3:4`, `1:1` as alternatives). Write the bible and art style to `polylogue.md`. This is the canonical source for image prompts.

### Round 3 — Outline
Use the `polylogue-creative-writer` subagent to draft a Y-shaped chapter outline: chapter beats, fork placement, divergent endings sketch. Use the `polylogue-instructional-designer` subagent to assign a target thinking skill to each chapter-end gate, with progression that makes pedagogical sense. Use the `polylogue-reviewer-editor` subagent to compute the runtime estimate (see below) and flag if it exceeds the budget by more than 10%. Chapter list goes to `polylogue.md`.

### Round 4 — Page drafting
For each chapter, run the full pipeline:
1. `polylogue-creative-writer` drafts pages (narration + dialogues at natural length; pages are short — 1 narration paragraph + 2–4 dialogue lines).
2. `polylogue-instructional-designer` adapts language to the chosen grade level.
3. `polylogue-reviewer-editor` polishes for grade-level voice and dialogue authenticity, then composes the complete image prompt per page. Image prompts are renderer-facing and self-contained — see `polylogue-reviewer-editor.md` Section 2 for the composition spec and renderer-facing rules (aspect-ratio line first, no meta-instructions, no story-internal nicknames, no comparatives, absolute visual states only, no on-image text or speech-balloon planning).

Write each chapter to `chapters/chapter-NN.md` with transcript and complete image prompt stored together per page. Update the runtime estimate in `polylogue.md` after each chapter.

### Round 5 — Decision authoring
Typically interleaved with Round 4 — pages and chapter-end decision authored together per chapter.

For each chapter, use the `polylogue-instructional-designer` subagent to author the chapter-end decision:
- 3-MC prompt framed in-fiction.
- For gates: 1 correct + 2 incorrect choices, each incorrect annotated with `misconception_targeted` (a specific surface-level reading, fallacy, or bias the named skill is meant to defeat — derived from the LLM's pedagogical knowledge of grade-5/6/7 misapplication of the skill, not enumerated in `thinking-skills.md`).
- For the perspective fork (exactly one per story): 2 correct + 1 incorrect (default) or 3 correct (no failure mode), per author preference. Each correct choice routes to a different post-fork chapter.
- Hint after attempt 1 (must reframe or surface relevant skill, not give the answer).

Use the `polylogue-creative-writer` subagent to draft abrupt-end pages (1–2 short consequence pages, in-fiction) for any decision with at least one incorrect choice; the Reviewer composes their image prompts.

**Mandatory elimination check** (the Instructional Designer runs this before handing back): for every decision, verify a student CANNOT arrive at the correct choice via process of elimination, narrative cues, or common sense. With 3 MC and 2 attempts, naive guessing wins ~67% — wrong choices must be pedagogically tempting misconceptions, not red herrings. If a decision fails the check, sharpen the wrong choices.

**Fork-legitimacy check** (perspective-fork only): each correct branch must represent a genuinely distinct, thoughtful, defensible perspective. If one is clearly more virtuous, the fork is hollow.

### Round 6 — Image-prompt review
Present complete image prompts chapter-by-chapter for author review. Author edits staging directly. If the author edits the bible in `polylogue.md`, run sync: the `polylogue-reviewer-editor` subagent regenerates inline character descriptions in all affected chapter files.

### Round 7 — Quality review
The `polylogue-reviewer-editor` subagent runs a full pass and presents pass/warn/fail per check:
- **Elimination check** — re-run on every gate.
- **Fork legitimacy** — re-run on the perspective fork.
- **Ending diff** — are the divergent endings drastically different in fate, mood, lesson? If they feel like reskins, flag.
- **Runtime fit** — total estimated runtime within `metadata.estimated_duration_minutes`?
- **Bible sync** — every chapter's inline character descriptions match the current bible?
- **Renderer-facing self-containment** — every `image_prompt` starts with the aspect-ratio line; contains no cross-page or cross-chapter references, no comparative-to-baseline phrasings, no pipeline meta-instructions, no story-internal nicknames, no meta-commentary, and no on-image text or speech-balloon planning.
- **Schema validity** — structure conforms to `schema.json`. Cross-cutting invariants: exactly one `perspective_fork`; `endings.length` equals number of correct choices in fork; every `next_chapter_id` resolves.

For each failed check, propose a fix. If the author overrides rather than fixes, record an entry in `metadata.author_overrides` with a one-line justification. Warn-and-allow — never block export.

### Round 8 — Export
Read `polylogue.md` for metadata, art style, characters, debrief. Read each `chapters/chapter-NN.md` for pages, decisions, abrupt-ends. Run final bible sync. Validate against `schema.json`. Add `version` field (semver; v1 = "1.0.0"). Write `story.json` (or `story-vN.json` if a version exists). Print one-line summary: `"Exported story-vN.json — N chapters, M pages, K decisions, Q author overrides recorded."`

## Runtime estimator

```
total_seconds =
  60                                      # setup
  + sum(pages_per_chapter × seconds_per_page)
  + decisions × seconds_per_decision
  + 120                                   # debrief
```

Default coefficients: grade 5 = 35 s/page; grade 6 = 30 s/page; grade 7 = 25 s/page; 90 s per decision (covers 2 attempts + group deliberation). Warn the author when `total_seconds / 60` exceeds `estimated_duration_minutes × 1.10`.

## Bundled assets

- `schema.json` — JSON Schema for `story.json`. Read for Round 7 validation and Round 8 export.
- `thinking-skills.md` — canonical list of skill names grouped by category. Read in Round 0 to validate author-named skills. Definitions, grade-level signs, and misconception patterns are NOT in this file — derive them from model knowledge of pedagogy at the named grade level.
- `sample-story.json` — fully-worked example (when present). Provide as few-shot reference to subagents.
- `DESIGN.md` — verbose design document; development reference only, not loaded at runtime.

## Communication style

After each round, respond to the author with:
- What artifact changed.
- The most important current shift.
- 1–3 items the author should review or answer next.

Keep chat short. Durable work belongs in the files.
