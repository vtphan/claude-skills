---
name: design-polylogue-story
description: Co-design a graphic-novel choose-your-own-adventure story with a human author for grade 5–7 students. Produces a JSON story package (`story.json`) conforming to the bundled `schema.json`. Each chapter optionally ends with a foundational comprehension check and/or a thinking-skill decision; the story is Y-shaped with exactly one perspective-taking fork that diverges into different endings. Every challenge targets a named skill from the bundled `skills-reference.md`. Use when an author asks to design, write, build, or draft a polylogue story.
---

# design-polylogue-story

Co-design a graphic-novel CYOA story with a human author. The story has chapters → pages → optional chapter-end teaching moments (a foundational comprehension check, a thinking-skill decision, both, or neither — the chapter's dramatic shape decides). Exactly one perspective-taking fork diverges into different endings. Three pipeline stages do the creative work; you orchestrate.

## Audience and setting

- **Target audience:** grade 5, 6, or 7 students.
- **Reading mode:** each student reads the comic individually on their own laptop.
- **Group mode:** students can ask each other questions and discuss between/at decision points. The polylogue is partly the dialogue inside the comic, partly the *students* talking to each other when they hit a decision.
- **Practical realism:** "individual" challenges may receive peer help anyway. That's acceptable; the individual/group tag signals authoring intent and the elimination-check bar, not enforcement.

## Operating principles

Three principles shape how this skill operates.

### Briefing, not recipe

This skill is designed to be carried out by a capable LLM. It is a briefing for a capable colleague, not a recipe for a procedural worker.

What the file load-bears on (the model can't infer these): the audience and setting above; the taxonomy in `thinking-skills.md` and the working reference in `skills-reference.md`; the schema (`schema.json`); downstream renderer constraints (in `agents/reviewer-editor.md`); the goals the work is trying to achieve.

What the file does *not* try to encode (the model already brings these): step-by-step procedures the model can sequence on its own; numerical micro-prescriptions of format; mechanical validation algorithms when an articulated *question* would do.

Slot tags and other taxonomy signals are *affordances*, not rules. A skill tagged `[gate]` *can* fit a gate slot; the model decides per-chapter whether the staged scene supports it.

### Iterative dialog with the author

The skill operates from cold start — no sample stories yet exist as few-shot ground truth. In compensation, the design process is structured as iterative dialog: the LLM brings concrete options the author can react to; the author holds context, scope, and taste-making standards (much of which is implicit). Iteration substitutes for examples — the author's reactions across multiple rounds encode taste into the artifact.

In practice:

- **Bring an artifact before asking.** Default-and-confirm over ask. Concrete options elicit implicit knowledge that abstract questions don't.
- **First-draft offness is the expected case**, not a failure. The author's correction is the signal the system is designed to elicit. Loopback is the natural rhythm of dialog, not a recovery mechanism.
- **Different authors will produce different stories from the same seed.** The dialog is the personalization mechanism.
- **Once a real story is produced through this skill, it becomes a sample for future runs** (when the author chooses to share it).

### Acceptable artifacts before architectural elegance

Aim for a useful, complete-enough story. Defer complexity that doesn't earn its place by improving the actual output.

## Author's job

1. Provide a seed in Round 0: story-line idea, target thinking skill(s), target minutes (default 15), reading level (5/6/7).
2. React to artifacts: yes / no / revise / change X.
3. Approve the export.

The author can directly edit `polylogue.md` or any `chapters/chapter-NN.md` between rounds; you pick up edits on the next round.

## Artifacts

```
{slug}/
|-- polylogue.md            # master: concept, character bible, art style, chapter list, runtime estimate, debrief, endings
|-- story.json              # final export (Round 8 only)
|-- chapters/
|   |-- chapter-NN.md       # one per chapter; pages (with image prompts) + chapter-end challenges
|   `-- chapter-NNa.md, NNb.md, ...  # one per fork-branch ending (terminal chapters)
`-- rounds/                 # lazy round files (e.g., quality review reports)
```

`polylogue.md` is the single source of truth for the character bible, locked art style, chapter list, endings, and debrief. Chapter files are self-contained per chapter (pages + complete image prompts + comp check + decision + abrupt-end pages where applicable).

## Invocation

`design-polylogue-story <seed-text>` — start a new story. With no args, continue from current artifacts in the working directory.

## The three pipeline stages

The skill orchestrates three pipeline stages, each with a prompt spec in `agents/`. When the round flow names a stage, read the corresponding spec and apply its instructions in your current context.

- **Creative Writer** (`agents/creative-writer.md`) — drafts story plot, characters, dialogue, scene staging, abrupt-end pages.
- **Instructional Designer** (`agents/instructional-designer.md`) — adapts language to grade level, authors all chapter-end challenges (comp checks + decisions) drawing on `skills-reference.md`, runs the elimination check, tracks correct-answer position distribution across the story.
- **Reviewer/Editor** (`agents/reviewer-editor.md`) — polishes, composes complete renderer-facing image prompts (with staging-pedagogy attention), edits silently, flags structural issues, runs sync-checks and Round 7 quality review.

The author sees only the Reviewer's output. Author feedback re-enters the pipeline at the appropriate stage.

## Round flow

The flow is a collaborative dialog with the author, not a sequential checkpoint procedure. Loopback (revise-in-place / re-narrow / re-diverge / re-frame) is callable from any round and is the natural rhythm of authoring under cold-start.

### Round 0 — Seed

Capture: (1) story-line idea, (2) target thinking skill(s), (3) target minutes (default 15), (4) reading level (5/6/7). Validate skill names against `thinking-skills.md`; if author names don't match, surface the closest canonical names and ask whether to map or extend. Initialize `polylogue.md`.

### Round 1 — Concept

Run the Creative Writer to generate 3–5 distinct story concepts (logline, character sketches, arc shape with proposed fork location, tone, theme).

Run the Instructional Designer to layer **two pedagogical dimensions** onto each concept — these are first-class output, not afterthoughts:

- **Skills targeted** — primary + secondary thinking skills the concept naturally implicates (drawing from `skills-reference.md`), with one-line reasoning each. Mention which slot(s) each would fill.
- **Teaching moments** — concrete sketches of the challenges each concept makes available: 2–4 example challenges per concept (mix of comp checks, gates, fork moment), grounded in scenes the concept produces.

Without these two dimensions, the author's concept selection is uninformed on the dimension that matters most for a teaching tool.

Run the Reviewer/Editor to polish. Present to the author. The author picks one or composes by combining elements; the secondary-skill set is confirmed. Update `polylogue.md`.

### Round 2 — Character bible and locked art style

Run the Creative Writer to draft each recurring character (name, role, age, physical description, clothing, distinctive features, expression baseline) and the locked art style (rendering style, palette, lighting, line treatment, aspect ratio).

Visually distinct identifiers per character matter — they're what gives image generation a chance at consistency across pages. The Reviewer/Editor verifies visual unambiguity. Default-and-confirm `aspect_ratio` (default `2:3`).

Write the bible and art style to `polylogue.md`. This is the canonical source for inline character descriptions in image prompts.

### Round 3 — Outline

Run the Creative Writer to draft a Y-shaped chapter outline: chapter beats, fork placement, divergent endings sketch.

Run the Instructional Designer to:

- **Decide which chapter-ends carry challenges.** A chapter end has 0, 1, or 2 challenges (comp check + decision, comp check only, decision only, or neither). The story's dramatic shape decides; not every chapter needs a teaching moment. A chapter without a natural vocabulary moment shouldn't have a comp check forced; a chapter without a real decision shouldn't have a manufactured gate.
- **Assign target skills to challenge slots.** Foundational reading skills to `[comprehension_check]` slots; thinking skills to `[gate]` slots; perspective-taking thinking skills (or SEL-as-content perspective-shift skills) to the single `[fork]` slot. Per-skill slot tags are in `thinking-skills.md`; reference entries with worked examples are in `skills-reference.md`.

Run the Reviewer/Editor to compute the runtime estimate and flag if it exceeds the budget by more than 10%.

### Round 4 — Page drafting

For each chapter, run the full pipeline:

1. The Creative Writer drafts pages — narration + dialogue at the natural length the chapter beats require. Pages are moments; one beat per page.
2. The Instructional Designer adapts language to the chosen grade level. Read each line aloud mentally — would a real student at that grade say this?
3. The Reviewer/Editor polishes for grade-level voice and dialogue authenticity, then composes the complete renderer-facing image prompt per page.

**Staging carries pedagogical weight, varying by skill type at the chapter end.** The image prompt is not independent of the chapter-end challenge:

- *Inferencing gates* — staging must depict the evidence the correct inference combines (body language, environment, action) without editorializing through composition.
- *SEL-as-content gates* — the panel composition is the primary evidence; dialogue can't replace what staging shows about who looks at whom, whose body turns, whose moment gets interrupted.
- *Perspective forks* — staging must keep all correct paths visually approachable (no compositional tilt).
- *Vocabulary-in-context* — image is secondary; the cue lives in dialogue.

See `agents/reviewer-editor.md` for the full staging-for-pedagogy spec and renderer-facing rules.

Write each chapter to `chapters/chapter-NN.md` with transcript and complete image prompt stored together per page. Update the runtime estimate in `polylogue.md` after each chapter.

### Round 5 — Decision and comp-check authoring

Typically interleaved with Round 4 — pages and chapter-end challenges authored together per chapter.

For each chapter end, the Instructional Designer authors the relevant challenge(s):

**Comprehension check** (when present): foundational skill, individual default, formative — does NOT route the story; failure does NOT trigger abrupt-end. 3-MC, 1 correct + 2 wrong (each wrong annotated with `misconception_targeted` from the per-skill failure modes in `skills-reference.md`). Hint after attempt 1 redirects to text or visible evidence. Coin schedule **1/0/0** (1 if correct on first attempt; 0 otherwise — the formative signal).

**Decision** (when present): thinking skill or SEL-as-content, group default, narrative routing.

- *Gate*: 3-MC, 1 correct + 2 wrong (each wrong annotated with `misconception_targeted`). Hint after attempt 1 redirects via group discussion. Coin schedule 3/1/0.
- *Perspective fork* (exactly one per story): 2 correct + 1 incorrect, OR 3 correct + 0 incorrect (per author preference). Each correct choice routes to a different post-fork chapter. For 3-correct/0-incorrect variant, use a `deliberation_prompt` (framing nudge presented when the choice lands) instead of `hint_after_attempt_1`.

**Mandatory elimination check** (Instructional Designer, before handing back). For every challenge ask: could a student lacking the named skill arrive at the correct answer via process of elimination, narrative cues, or common sense? For *group* challenges, the bar is harder — could a *group* discussing collectively arrive at it without using the skill? Sharpen wrong choices until the answer is no.

**Position distribution.** Track correct-answer position (A/B/C) across the story's challenges. Target ≥1 of each across the full story; in chapters with both a comp check and a gate, the two challenges should not share the same correct position. The natural authoring habit gravitates toward (C) — resist it explicitly, because a deterministic correct-position pattern collapses the gate further (3-MC + 2 attempts already conferring ~67% naive-guess success).

Run the Creative Writer to draft abrupt-end pages (1–2 short consequence pages, in-fiction) for any decision with at least one incorrect choice; the Reviewer composes their image prompts.

### Round 6 — Image-prompt review

Present complete image prompts chapter-by-chapter for author review. Author edits staging directly. If the author edits the bible in `polylogue.md`, run sync — the Reviewer/Editor regenerates inline character descriptions in all affected chapter files.

(Often deferrable until actual renders exist, since the prompts are intermediate; review them when there's something concrete to compare against. Skipping this round and going to Round 7 is acceptable.)

### Round 7 — Quality review

The Reviewer/Editor runs a full pass and presents pass/warn/fail per check (full checklist in `agents/reviewer-editor.md`). At minimum:

- **Elimination check** on every gate (group bar for group challenges).
- **Fork legitimacy** — each correct branch is defensible by a thoughtful person valuing that perspective.
- **Ending diff** — branches drastically different in fate, mood, lesson.
- **Runtime fit** within `metadata.estimated_duration_minutes × 1.10`.
- **Bible sync** — every chapter's inline character descriptions match the current bible verbatim.
- **Renderer-facing self-containment** — explicit mechanical scans for cross-page references, cross-chapter comparatives, negative-form instructions to the renderer, bold-printed editorial inside `[Page staging]` blocks.
- **Schema validity / DAG validity** — exactly one `perspective_fork`; `endings.length` equals correct choices in fork; every `next_chapter_id` resolves.
- **Position distribution** — A/B/C distributed across challenges; comp check and gate within the same chapter at different correct positions.
- **Staging-pedagogy** — chapter scene staging supports the evidence the chapter-end challenge asks students to read.

For each failed check, propose a fix. If the author overrides rather than fixes, record an entry in `metadata.author_overrides` with a one-line justification. Warn-and-allow — never block export.

### Round 8 — Export

Read `polylogue.md` for metadata, art style, characters, debrief, endings. Read each `chapters/chapter-NN.md` for pages, comp checks, decisions, abrupt-ends. Run final bible sync. Validate against `schema.json`. Add `version` field (semver; v1 = "1.0.0"). Write `story.json` (or `story-vN.json` if a version exists). Print one-line summary.

## Runtime estimator

```
total_seconds =
  60                                      # setup
  + sum(pages_per_chapter × seconds_per_page)
  + sum(comp_checks × 30)                 # comp check time (read, deliberate, hint, retry, reveal)
  + sum(decisions × 90)                   # decision time (covers 2 attempts + group deliberation)
  + 120                                   # debrief
```

Default coefficients: grade 5 = 35 s/page; grade 6 = 30 s/page; grade 7 = 25 s/page; comp checks = 30 s; decisions (gates and forks) = 90 s. Warn the author when `total_seconds / 60` exceeds `estimated_duration_minutes × 1.10`.

## Bundled assets

- `schema.json` — JSON Schema for `story.json`. Read for Round 7 validation and Round 8 export.
- `skills-reference.md` — per-skill working reference (definitions, mastery signs at G5/6/7, named failure modes with example wrong-choices, worked micro-examples, authoring notes). At cold start, the only concrete pedagogical ground-truth available; treat the worked examples with care, since they're doing the work a sample story would otherwise do.
- `thinking-skills.md` — canonical taxonomy of skill names grouped by category, with slot tags. Used to validate author-named skills in Round 0.
- `agents/` — prompt specs for the three pipeline stages.
- `sample-story.json` — fully-worked example. Not bundled in v1 by design (there are no existing stories at cold start; the first real story produced through the dialog becomes the sample for future versions).

## Communication style

After each round, respond to the author with:

- What artifact changed.
- The most important current shift.
- 1–3 items the author should review or answer next.

Keep chat short. Durable work belongs in the files. The chapter file is the artifact you ship per chapter; `polylogue.md` is the master state.
